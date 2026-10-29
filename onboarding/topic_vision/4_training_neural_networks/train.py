"""Refer to section 3 of the instructions for this file"""

def train_one_epoch(model, train_loader, loss_fn, optimizer, device):
    #TODO:
    return

def evaluate(model, test_loader, loss_fn, device):
    #TODO:
    return


if __name__ == "__main__":
    import torch
    from torch import nn
    from torch.utils.data import DataLoader, TensorDataset

    data = TensorDataset(torch.randn(64, 1, 28, 28), torch.randint(0, 10, (64,)))
    loader = DataLoader(data, batch_size=32)

    model = nn.Sequential(nn.Flatten(), nn.Linear(28 * 28, 10))
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    train_loss = train_one_epoch(model, loader, loss_fn, optimizer, "cpu")
    test_loss, accuracy = evaluate(model, loader, loss_fn, "cpu")

    assert isinstance(train_loss, float)
    assert isinstance(test_loss, float)
    assert 0.0 <= accuracy <= 1.0

    print("All tests passed!")
