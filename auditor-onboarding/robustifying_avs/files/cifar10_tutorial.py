import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

########################################################################
# The output of torchvision datasets are PILImage images of range [0, 1].
# We transform them to Tensors of normalized range [-1, 1].
########################################################################

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def main():

    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )

    batch_size = 64

    trainset = torchvision.datasets.CIFAR10(
        root="./data", train=True, download=True, transform=transform
    )

    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=batch_size, shuffle=True, num_workers=10
    )

    testset = torchvision.datasets.CIFAR10(
        root="./data", train=False, download=True, transform=transform
    )

    testloader = torch.utils.data.DataLoader(
        testset, batch_size=batch_size, shuffle=False, num_workers=10
    )

    classes = (
        "plane",
        "car",
        "bird",
        "cat",
        "deer",
        "dog",
        "frog",
        "horse",
        "ship",
        "truck",
    )

    def imshow(img):
        img = img / 2 + 0.5  # unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()

    ########################################################################
    # 2. Define a Convolutional Neural Network
    ########################################################################

    import torch.nn as nn
    import torch.nn.functional as F

    class Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = torch.flatten(x, 1)  # flatten all dimensions except batch
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    net = Net().to(device)

    ########################################################################
    # 3. Define a Loss function and optimizer
    ########################################################################

    import torch.optim as optim

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    ########################################################################
    # 4. Train the network
    ########################################################################

    num_epochs = 10

    for epoch in range(num_epochs):
        net.train()
        running_loss = 0.0

        train_bar = tqdm(trainloader, desc=f"Epoch {epoch + 1}/{num_epochs} [Train]")

        for i, data in enumerate(train_bar):
            inputs, labels = data[0].to(device), data[1].to(device)

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            train_bar.set_postfix(
                batch_loss=f"{loss.item():.4f}",
                avg_loss=f"{running_loss / (i + 1):.4f}",
            )

        ####################################################################
        # Validation after each epoch
        ####################################################################
        net.eval()
        val_correct = 0
        val_total = 0
        val_running_loss = 0.0

        val_bar = tqdm(testloader, desc=f"Epoch {epoch + 1}/{num_epochs} [Val]")

        with torch.no_grad():
            for j, data in enumerate(val_bar):
                inputs, labels = data[0].to(device), data[1].to(device)

                outputs = net(inputs)
                loss = criterion(outputs, labels)

                _, predicted = torch.max(outputs, 1)
                val_total += labels.size(0)
                val_correct += (predicted == labels).sum().item()
                val_running_loss += loss.item()

                val_bar.set_postfix(
                    val_loss=f"{val_running_loss / (j + 1):.4f}",
                    val_acc=f"{100.0 * val_correct / val_total:.2f}%",
                )

    print("Finished Training")

    ########################################################################
    # Save trained model
    ########################################################################

    PATH = "./cifar_net.pth"
    torch.save(net.state_dict(), PATH)

    ########################################################################
    # 5. Test the network on the test data
    ########################################################################

    net = Net().to(device)
    net.load_state_dict(torch.load(PATH, weights_only=True))
    net.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        test_bar = tqdm(testloader, desc="Final Test")

        for data in test_bar:
            inputs, labels = data[0].to(device), data[1].to(device)

            outputs = net(inputs)
            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            test_bar.set_postfix(accuracy=f"{100.0 * correct / total:.2f}%")

    print(
        f"Accuracy of the network on the 10000 test images: {100 * correct // total} %"
    )

    ########################################################################
    # Per-class accuracy
    ########################################################################

    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}

    with torch.no_grad():
        class_bar = tqdm(testloader, desc="Per-class Accuracy")

        for data in class_bar:
            images, labels = data[0].to(device), data[1].to(device)
            outputs = net(images)
            _, predictions = torch.max(outputs, 1)

            for label, prediction in zip(labels, predictions):
                label_idx = label.item()
                pred_idx = prediction.item()

                if label_idx == pred_idx:
                    correct_pred[classes[label_idx]] += 1
                total_pred[classes[label_idx]] += 1

    for classname, correct_count in correct_pred.items():
        accuracy = 100 * float(correct_count) / total_pred[classname]
        print(f"Accuracy for class: {classname:5s} is {accuracy:.1f} %")


if __name__ == "__main__":
    main()
