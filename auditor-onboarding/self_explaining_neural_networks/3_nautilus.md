# TEMPLATE SENN Task 3: Nautilus

Status: Backlog
Quarter: winter26

# Nautilus

- [ ]  Go through the Nautilus guide:
    
    [Nautilus Guide 2.0](https://www.notion.so/Nautilus-Guide-2-0-2f9c03a14c2c80bd838bf9c7853f4d4d?pvs=21) 
    
    [Nautilus Guide](https://www.notion.so/Nautilus-Guide-f486e7601e6b496e94d9ffeae1bd1f87?pvs=21)
    
    - [ ]  Start with Getting An Account
    - [ ]  Get added to our namespace
        - Ask on the nautilus channel on discord
    - [ ]  Watch at least 1 tutorial
    - [ ]  Read [Nautilus Guide 2.0](https://www.notion.so/Nautilus-Guide-2-0-2f9c03a14c2c80bd838bf9c7853f4d4d?pvs=21)
    - [ ]  To get experienced using Nautilus, complete the following:
        - [ ]  Use nautilus jupyterhub - https://jupyterhub-west.nrp-nautilus.io/hub/
            - [ ]  Upload this python notebook and get it to run
                
                [cifar10_tutorial.ipynb](TEMPLATE%20VISION%20Task%203%20Nautilus/cifar10_tutorial.ipynb)
                
                - You will need to pip install all necessary packages
                - It is normal to have to wait
        - [ ]  Create PVC
            - [ ]  name is `cruzid-task3`
            - [ ]  size `5Gi`
        - [ ]  Create Deployment
            - [ ]  Create a deployment and attach created PVC to it
            - [ ]  Train this CNN Classifier on the deployment
                
                [cifar10train.py](TEMPLATE%20VISION%20Task%203%20Nautilus/cifar10train.py)
                
                - Can either attach VS Code session or use SCP to transfer file from local to deployment
            - [ ]  Delete Deployment
                - This is very important, as Deployments last indefinitely, so never let it go idle.
        - [ ]  Create Job
            - [ ]  Attach to the same PVC
                - Keep in mind, if your PVC says `ReadWriteOnce`, then only one pod can connect at a time, you make sure your previous deployment is closed.
            - [ ]  Modify YAML file to run `cifar10train.py` by changing `command` spec in the YAML
            - [ ]  Delete Job
                - Jobs are efficient, as they deallocate resources when the script specified is completed. Deleting a Job after it is completed is best practice.
            - Note: Never do sleep infinity on a job, sleep infinity is fine when creating Deployments, and Pods, but not Jobs.

## Deliverables

- Write one page about  Nautilus and the job/deployment you ran to get started.
- Present your writeup in one of the status meetings
- Screenshot showing the training log of cifar10.py
    - Expected
        
        ![image.png](TEMPLATE%20VISION%20Task%203%20Nautilus/image.png)
        
        - Notably we will check if your device is cuda

## Hints

- If you get errors when you do `kubectl get pods`, then redownload the config file, and paste it in the `~/.kube` folder. If you’re still getting an error, then manually set the namespace to `aiea-auditors`.
- VS Code extension for kubernetes and dev containers is helpful to manage pod/deployment/job
- k9s is another helpful tool
    - https://k9scli.io/
- Resources
    - [Nautilus Guide](https://www.notion.so/Nautilus-Guide-f486e7601e6b496e94d9ffeae1bd1f87?pvs=21)
    - https://nrp.ai/documentation/