# TEMPLATE VISION Task 2: Neural Expl Vision Onboarding

Status: Backlog
Quarter: winter26

# Neural Explanations for Computer Vision

- [ ]  Read the documentation associated with the Clustered Compositional Explanations Repository
    - [ ]  [https://github.com/KRLGroup/Clustered-Compositional-Explanations](https://github.com/KRLGroup/Clustered-Compositional-Explanations)
- [ ]  Download/clone the repository
- [ ]  Download the precomputed segmentation masks at one of the following links (the one that works for you)
    - [ ]  Link 1: https://drive.google.com/file/d/1tUX1OAbnM7Gdu7kke3Umd7k6lUrZbSWA/view?usp=sharing and unzip it in the directory at the path <repo_dir>/data/cache
    - [ ]  (or if the first doesn’t work) Link 2: https://drive.google.com/file/d/1O2FunAmj2Vaw4bf-1RfxZyucwG8tRGOb/view?usp=drive_link
    
                  !!You need to create the missing directories!
    
- [ ]  Prepare your local environment by installing all dependencies and requirements specified in the repository
    - [ ]  Document every problem you encounter and its solution!
- [ ]  Generate the compositional explanations for **10 random units** for the resnet18 model for the highest activations (i.e., set the number of clusters to 1)
    - Hint: Read the documentation and use one of the scripts in the repo to generate them!
    - Note: This task requires a workstation with at least 16GB of RAM. If your local workstation does not meet these requirements, please run the script until it crashes and submit the deliverable described below. In this case, all tasks for this project **must** be performed on Nautilus.
- [ ]  Create a github repo and upload there your starting code.

## Deliverables

- [ ]  Submit the the list of the neurons explanations. Each item in the list should be in the following format: `<Neuron ID>` - `<Cluster Number>` - `<Explanation>`
    - [ ]  If your workstation does not meet the RAM requirements and the script crashed after loading the layer activation, please submit a screenshot including the computer name and the information printed by the script before crashing
- [ ]  Submit a short textual description highlighting your workstation setup (GPU, amount of RAM, OS, number of CPUs) and any additional steps you had to follow in order to prepare your local environment and successfully run the script on your specific setup (OS, environment, etc). Include the github repo link.
    - If you followed the instructions in the repository documentation and you didn’t have to take any additional steps, please include only the workstation setup the sentence “I didn’t need any addition steps to run the script.”