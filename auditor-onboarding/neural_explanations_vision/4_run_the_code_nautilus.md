# TEMPLATE VISION Task 4: Run the Code (Nautilus)

Status: Backlog
Quarter: winter26

# Neural Explanations (Vision) Project

The goal of this week is to run the code you tested in Task 2 on Nautilus. 

- [ ]  Request a served/pod with at least 20GB of RAM
- [ ]  Download/clone/move the repository into your nautilus space
- [ ]  Download the precomputed segmentation masks at the following link:
    - [ ]  Link 1: https://drive.google.com/file/d/1tUX1OAbnM7Gdu7kke3Umd7k6lUrZbSWA/view?usp=sharing and unzip it in the directory at the path <repo_dir>/data/cache
    - [ ]  (or if the first doesn’t work) Link 2: https://drive.google.com/file/d/1O2FunAmj2Vaw4bf-1RfxZyucwG8tRGOb/view?usp=drive_link

              !!You need to create the missing directories!

- [ ]  Prepare the environment by installing all dependencies and requirements
    - [ ]  Document every problem you encounter and its solution!
- [ ]  Generate the compositional explanations for **10 random units** for the resnet18 model for the highest activations (i.e., set the number of clusters to 1)
    - [ ]  Note: if the loading process of the sparse masks or the computation of the activation is too slow (e.g., after waiting for a couple of minutes, it will still need hours to complete), please try asking for more cpu (4) and ensure that you are using a GPU/cuda while running your script (use the flags!)

## Deliverables

- Submit a small video that shows the code output inside Nautilus and references to your nautilus username
- Submit a short textual description highlighting any steps you had to follow in order to prepare your nautilus environment and successfully run the script