# Task 7: Implementing a Vision Transformer

## Goal

Last week you read "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
(<https://arxiv.org/pdf/2010.11929>). In this task you will implement the Vision Transformer (ViT) from that paper from scratch in PyTorch.

We give you the code scaffolding in `model.py`. Each module has a docstring and step-by-step `TODO` comments that explain what to build, along with references to the matching equations in the paper. Your job is to fill in every `TODO`.

## Running the Tests

`model.py` comes with tests. Run them with:

```bash
python3 model.py
```

Each test checks a different module, in the order the modules appear in the file (`PatchEmbedding`, `MultiHeadSelfAttention`, `MLP`, `TransformerEncoderBlock`, `ViT`). **Test often:** run the file after you finish each module, so you catch mistakes before you build on top of them. When every module is finished, the script prints `All tests passed`.

## Rules

- Use only standard PyTorch building blocks. The top of `model.py` lists what you may and may not use.
- The scaffolding and the paper are all you need. Many ViT implementations exist online, but the instructions in `model.py` are detailed enough that you should not need any other resources. If you do use an outside resource (a tutorial, blog post, video, documentation page, or someone else's code), you must list it in your write-up.
- **No AI tools are allowed** (e.g. ChatGPT, Claude, Copilot, or any other AI coding assistant).

## Submission

Submit:

1. Your completed `model.py`. It must pass all the tests.
2. A short write-up containing:
    - One or two sentences per module (`PatchEmbedding`, `MultiHeadSelfAttention`, `MLP`, `TransformerEncoderBlock`, `ViT`) explaining what the module does and why ViT needs it. For example, what is the point of `PatchEmbedding`? What does `MultiHeadSelfAttention` let the model do?
    - A list of any outside resources you used. Write "None" if you used none.
