# TEMPLATE VISION Task 9: Clustering

Status: Backlog
Quarter: winter26

# Neural Explanations (Vision) Project

The goal of this week is to test the robustness of explanations with respect to the clustering algorithm used for extracting activation ranges.

- [ ]  Modify the script to compute explanation by changing the clustering algorithm (K-Means) parameters or the clustering algorithm itself. Search for parameters/algorithms that still produce “meaningful” explanations but significantly different (at least 33% of the labels should be different) from the (10) ones computed in the previous tasks.
    - Notes:
        - Watch out for the timing! You are free to change any parameter you prefer (or use any algorithm you prefer), but please consider the time required to run the algorithm. You cannot wait 3 days for each unit! Therefore, prioritize faster configurations/algorithms.
        - “meaningful explanation” means that the same explanation is not repeated over all the clusters and all the units (i.e., it is a degenerate behavior).
        - The script uses a cache to avoid “recomputing” explanations for already analyzed units. Since the script is “blind” to the modification in the clustering algorithm, you will need to specify a new results directory for each new configuration in order to store and compute explanations for different clustering configurations (but for the same units and layers).
        - If it is not possible to find such a configuration/algorithm in a reasonable time, **please document and report** every configuration you tested.
    - Tip: To speed up the process, first test your modifications on a few units (e.g., 2 or 3). Reserve the full tests (on all 10 units) only for very promising configurations/algorithms.

- Useful Links:
    - [ ]  [https://scikit-learn.org/stable/modules/clustering.html](https://scikit-learn.org/stable/modules/clustering.html)
    - [ ]  [https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans)
- [ ]  Commit your changes to the github repo.

## Deliverables

- [ ]  Discuss your findings on the robustness of explanations in a report (max 1 page)/presentation. Discuss how easy or hard is to find a configuration that changes the explanations in general and how easy or hard is to find a configuration that significantly changes the explanations. Discuss any trade-off in terms of time/space/other factors you observe.
- [ ]  Please include the link to the specific commits related to this task.