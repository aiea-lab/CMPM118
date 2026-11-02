"""Refer to section 2 of the instructions for this file"""

def get_mnist(batch_size):
    # TODO:
    return


if __name__ == "__main__":
    import torch

    train_loader, test_loader = get_mnist(batch_size=32)

    instance, _ = next(iter(train_loader))

    assert isinstance(train_loader, torch.utils.data.DataLoader)
    assert instance.shape == (32, 1, 28, 28)

    print("All tests passed!")

