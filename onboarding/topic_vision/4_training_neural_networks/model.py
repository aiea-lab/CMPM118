"""Refer to section 1 of the instructions for this file"""

class Model():
    # TODO:
    pass





if __name__ == "__main__":
    import torch
    import torch.nn as nn

    model = Model(input_dim=1*28*28, hidden_dim=128, num_classes=10)
    layers = [type(m) for m in model.modules() if len(list(m.children())) == 0]
    dummy_x = torch.zeros(8, 1, 28, 28)

    # tests
    assert isinstance(model, nn.Module)
    assert model(dummy_x).shape == (8, 10)
    assert model.num_classes == 10 and model.input_dim == 1*28*28 and model.hidden_dim == 128
    assert layers == [nn.Flatten, nn.Linear, nn.ReLU, nn.Linear]

    print("All tests passed!")
