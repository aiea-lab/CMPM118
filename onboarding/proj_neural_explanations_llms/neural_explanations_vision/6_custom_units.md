# TEMPLATE VISION Task 6: Custom Units

Status: Backlog
Quarter: winter26

# Neural Explanations (Vision) Project

- [ ]  Print the list of the model’s layers and the total number of neurons within each layer
- [ ]  Modify the script to allow the user to specify the exact units for which to compute compositional explanations.
- [ ]  Generate compositional explanations for the 10 units of your choice (they must be different from the random one selected in Task 2 (Onboarding))
- [ ]  Commit your changes to the github repo.

## Deliverables

- [ ]  Submit the the list of the neurons explanations for the selected units. Report only the explanations associated with the highest numbered cluster. Each entry in the list should follow this format: `<Neuron ID>` - `<Cluster Number>` - `<Explanation>`
- [ ]  Submit the complete list of layer and units in each layer in the following format: `<Layer Name/Full Position>` Num Neurons: `<NUM UNITS>`
- [ ]  Briefly comment on the differences and similarities between explanations computed for these neurons and the neurons explained in Task 2 (Onboarding)
- [ ]  Please include the link to the specific commits related to this task.
- [ ]  Choose one of the convolutional layers in the network and claim it with the teaching team. Be sure to specify the **full(complete/absolute)** position of the layer in the network (e.g., convX within the block X of layer X)
    - Note: FIFO policy, each team must to choose a different layer