"""Refer to section 4 of the instructions for this file"""

# we do this for you, but you should learn how to do this
def get_pytorch_device():
    import torch
    device = "cpu"
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    return device

def main(num_epochs, batch_size, learning_rate=0.01):
    device = get_pytorch_device()
    # TODO:
    return


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch_size", type=int, default=64)
    args = parser.parse_args() # you can access the values using args.<value name>

    main(num_epochs=args.epochs, batch_size=args.batch_size)
