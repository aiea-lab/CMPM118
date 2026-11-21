"""Refer to the instructions for this file.

Implement a Vision Transformer (ViT) from scratch, following
"An Image is Worth 16x16 Words" (https://arxiv.org/pdf/2010.11929).

You may use standard PyTorch building blocks (nn.Linear, nn.Conv2d, nn.LayerNorm,
nn.GELU, nn.Dropout, nn.Parameter, ...). You may NOT use nn.MultiheadAttention,
nn.TransformerEncoder, nn.TransformerEncoderLayer, F.scaled_dot_product_attention,
or any pre-built ViT (torchvision.models, timm, ...).

Notation used in the docstrings below:
    B = batch size        C = input channels      H = W = img_size
    P = patch_size        N = number of patches   D = embed_dim
"""

import torch
import torch.nn as nn


class PatchEmbedding(nn.Module):
    """Split an image into non-overlapping P x P patches and linearly project each to D dims.

    Input:  (B, C, H, W)
    Output: (B, N, D)   where N = (H / P) * (W / P)
    """

    def __init__(self, img_size, patch_size, in_channels, embed_dim):
        super().__init__()
        # TODO: check that img_size is divisible by patch_size (use an assert)
        # TODO: store self.num_patches as an int (the ViT class and the tests rely on it)
        # TODO: nn.Conv2d(in_channels -> embed_dim) with kernel_size = stride = patch_size.
        #       Each output position of this conv is one projected patch.
        raise NotImplementedError

    def forward(self, x):
        # TODO: apply the nn.Conv2d    (B, C, H, W) -> (B, D, H/P, W/P)
        # TODO: flatten the spatial dims and transpose   -> (B, N, D)
        #       (no layer needed: use tensor.flatten and tensor.transpose)
        raise NotImplementedError


class MultiHeadSelfAttention(nn.Module):
    """Multi-head scaled dot-product self-attention (paper Eq. 5-8 / Appendix A).

    Input:  (B, N, D)
    Output: (B, N, D)
    """

    def __init__(self, embed_dim, num_heads, dropout=0.0):
        super().__init__()
        # TODO: check that embed_dim is divisible by num_heads (use an assert)
        # TODO: store self.num_heads and self.head_dim as ints
        # TODO: Q, K, V projections: three nn.Linear(embed_dim -> embed_dim) layers, with bias
        #       (or one nn.Linear(embed_dim -> 3 * embed_dim) that you split into Q, K, V)
        # TODO: output projection: nn.Linear(embed_dim -> embed_dim), with bias
        # TODO: nn.Dropout(dropout), applied to the attention weights
        raise NotImplementedError

    def forward(self, x):
        # TODO:
        #   1. project x to Q, K, V with the nn.Linear layer(s)
        #   2. split into heads with reshape + transpose (no layer needed):
        #                                   (B, N, D) -> (B, num_heads, N, head_dim)
        #   3. attention weights:           softmax(Q K^T / sqrt(head_dim))
        #                                   (use the @ operator and torch.softmax, no layer needed)
        #   4. apply the nn.Dropout to the attention weights
        #   5. weighted sum of V            (use the @ operator)
        #   6. merge heads back with transpose + reshape:
        #                                   (B, num_heads, N, head_dim) -> (B, N, D)
        #   7. apply the output nn.Linear
        raise NotImplementedError


class MLP(nn.Module):
    """Position-wise feed-forward block: Linear -> GELU -> Dropout -> Linear -> Dropout.

    Input:  (B, N, D)
    Output: (B, N, D)
    """

    def __init__(self, embed_dim, mlp_dim, dropout=0.0):
        super().__init__()
        # TODO: define these layers in this order (you can wrap them in an nn.Sequential):
        #   1. nn.Linear(embed_dim -> mlp_dim)
        #   2. nn.GELU()
        #   3. nn.Dropout(dropout)
        #   4. nn.Linear(mlp_dim -> embed_dim)
        #   5. nn.Dropout(dropout)
        raise NotImplementedError

    def forward(self, x):
        # TODO: pass x through the layers above in order
        raise NotImplementedError


class TransformerEncoderBlock(nn.Module):
    """One pre-norm Transformer encoder layer (paper Eq. 2-3):

        x = x + MSA(LayerNorm(x))
        x = x + MLP(LayerNorm(x))

    Input:  (B, N, D)
    Output: (B, N, D)
    """

    def __init__(self, embed_dim, num_heads, mlp_dim, dropout=0.0):
        super().__init__()
        # TODO: nn.LayerNorm(embed_dim), applied before attention
        # TODO: MultiHeadSelfAttention(embed_dim, num_heads, dropout)  (your class above)
        # TODO: a second nn.LayerNorm(embed_dim), applied before the MLP
        # TODO: MLP(embed_dim, mlp_dim, dropout)  (your class above)
        raise NotImplementedError

    def forward(self, x):
        # TODO: x = x + attention(first LayerNorm(x))
        # TODO: x = x + MLP(second LayerNorm(x))
        raise NotImplementedError


class ViT(nn.Module):
    """Vision Transformer for image classification (paper Eq. 1-4).

    Input:  (B, C, H, W)
    Output: (B, num_classes) logits
    """

    def __init__(
        self,
        img_size,
        patch_size,
        in_channels,
        num_classes,
        embed_dim,
        depth,
        num_heads,
        mlp_dim,
        dropout=0.0,
    ):
        super().__init__()
        # TODO: store self.num_classes as an int
        # TODO: self.patch_embed -> PatchEmbedding(img_size, patch_size, in_channels, embed_dim)
        #       (your class above)
        # TODO: self.cls_token   -> nn.Parameter of shape (1, 1, D)
        #       (e.g. nn.Parameter(torch.zeros(1, 1, embed_dim)))
        # TODO: self.pos_embed   -> nn.Parameter of shape (1, N + 1, D), filled with small
        #       random values, not zeros (e.g. torch.randn(...) * 0.02)
        # TODO: nn.Dropout(dropout), applied after adding position embeddings
        # TODO: `depth` TransformerEncoderBlock(embed_dim, num_heads, mlp_dim, dropout)
        #       layers (your class above), held in an nn.ModuleList or nn.Sequential
        # TODO: final nn.LayerNorm(embed_dim)
        # TODO: self.head        -> nn.Linear(embed_dim -> num_classes)
        raise NotImplementedError

    def forward(self, x):
        # TODO:
        #   1. self.patch_embed                    (B, C, H, W) -> (B, N, D)
        #   2. prepend self.cls_token              (B, N, D)    -> (B, N + 1, D)
        #      (expand it to batch size B with tensor.expand, then torch.cat along dim 1)
        #   3. add self.pos_embed, then apply the nn.Dropout
        #   4. pass through each TransformerEncoderBlock
        #   5. apply the final nn.LayerNorm
        #   6. take the class token's output       (B, N + 1, D) -> (B, D)
        #      (index position 0 along the token dimension)
        #   7. self.head (nn.Linear)               (B, D)        -> (B, num_classes)
        raise NotImplementedError


if __name__ == "__main__":
    torch.manual_seed(0)

    # Small config for running tests
    cfg = dict(
        img_size=32, patch_size=4, in_channels=3, num_classes=10,
        embed_dim=64, depth=2, num_heads=4, mlp_dim=128, dropout=0.1,
    )
    B, N, D = 8, (32 // 4) ** 2, 64
    x_img = torch.randn(B, 3, 32, 32)
    x_tok = torch.randn(B, N + 1, D)

    def count_params(m):
        return sum(p.numel() for p in m.parameters())

    #  PatchEmbedding 
    pe = PatchEmbedding(img_size=32, patch_size=4, in_channels=3, embed_dim=D)
    assert pe.num_patches == N
    assert pe(x_img).shape == (B, N, D)
    assert count_params(pe) == 3 * 4 * 4 * D + D

    #  MultiHeadSelfAttention 
    msa = MultiHeadSelfAttention(embed_dim=D, num_heads=4)
    assert msa.num_heads == 4 and msa.head_dim == D // 4
    assert msa(x_tok).shape == (B, N + 1, D)
    assert count_params(msa) == 4 * (D * D + D)  # Q, K, V, and output projections
    try:
        MultiHeadSelfAttention(embed_dim=D, num_heads=5)
        raise RuntimeError("embed_dim not divisible by num_heads should raise an error")
    except (AssertionError, ValueError):
        pass

    #  MLP 
    mlp = MLP(embed_dim=D, mlp_dim=128)
    assert mlp(x_tok).shape == (B, N + 1, D)
    assert any(isinstance(m, nn.GELU) for m in mlp.modules())
    assert count_params(mlp) == (D * 128 + 128) + (128 * D + D)

    #  TransformerEncoderBlock 
    blk = TransformerEncoderBlock(embed_dim=D, num_heads=4, mlp_dim=128)
    assert blk(x_tok).shape == (B, N + 1, D)
    assert sum(isinstance(m, nn.LayerNorm) for m in blk.modules()) == 2
    assert count_params(blk) == count_params(msa) + count_params(mlp) + 2 * (2 * D)

    #  ViT 
    model = ViT(**cfg)
    assert isinstance(model, nn.Module)
    assert model.num_classes == 10
    assert isinstance(model.cls_token, nn.Parameter) and model.cls_token.shape == (1, 1, D)
    assert isinstance(model.pos_embed, nn.Parameter) and model.pos_embed.shape == (1, N + 1, D)
    assert model.pos_embed.abs().sum() > 0, "initialize pos_embed with small random values"
    assert model(x_img).shape == (B, 10)
    assert sum(isinstance(m, TransformerEncoderBlock) for m in model.modules()) == 2
    expected = (
        count_params(pe)
        + D                    # class token
        + (N + 1) * D          # position embeddings
        + 2 * count_params(blk)
        + 2 * D                # final LayerNorm
        + (D * 10 + 10)        # head
    )
    assert count_params(model) == expected, f"{count_params(model)} params, expected {expected}"

    # Samples in a batch must not affect each other
    model.eval()
    with torch.no_grad():
        assert torch.allclose(model(x_img)[:2], model(x_img[:2]), atol=1e-5)

    # Gradients reach every parameter
    model.train()
    model(x_img).sum().backward()
    for name, p in model.named_parameters():
        assert p.grad is not None, f"no gradient for {name}"

    print("All tests passed")
