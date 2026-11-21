# Task 6: Reading a Paper: Vision Transformers

## Goal

In the previous task, you worked on a CNN classifier. Now, you will learn about Vision Transformers (ViT).

Read the paper "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
https://arxiv.org/pdf/2010.11929

By the end you should be able to:

- Follow an image through ViT, from raw pixels to a class prediction, and give the tensor shape at every step
- Explain what *inductive bias* means, and compare the inductive biases of a CNN and a ViT
- Explain why ViT needs much more training data than a CNN to perform well

## Annotations

You must hand annotate this paper. Typed notes are *not* accepted. You may annotate by hand by printing and scanning, or using a tablet.
You may only skim the appendix. Focus on sections 1-5.

Some things to include in your annotations:
- **Summarize** each section in one or two sentences in your own words.
- **Define** write down terms you had to look up and did not understand
- **Connect to Task 5.** Wherever the paper compares ViT to CNNs, note how the comparison applies to the model you built.
- **Question.** Mark anything you didn't understand or don't believe with a "?" and write down your question.

As you read, make sure your annotations answer these questions:

1. How is an image turned into a sequence of tokens? What does the patch size P control, and what does it cost?
2. What is the `[class]` token for? What would you use instead? (See Appendix D.3.)
3. Position embeddings: why are they needed, what kind does ViT use, and what does Figure 7 (center) show they learn?
4. The paper says ViT has much less image-specific inductive bias than a CNN. Which parts of ViT are local or translation-equivariant, and which are not?
5. How does ViT compare to ResNets on ImageNet, ImageNet-21k, and JFT-300M? Why does this happen?

## Write-up

Write about half a page to a page answering:

- In your own words, what is ViT's core idea, and what is its main result?
- Compare ViT with the CNN you built in Task 5. If you had trained a ViT from scratch on your Task 5 dataset,
  would you expect it to beat your CNN? Use evidence from the paper to justify your answer.
- One thing in the paper you found confusing or would want to test yourself.

