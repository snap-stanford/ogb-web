---
title: Leaderboards
permalink: /docs/leader_overview/
---

Public leaderboards allow researchers to keep track of state-of-the-art models.

-----

### How Leaderboards Work?

Once you have developed your model and got results, you can submit your test results to our leaderboard. 
To make your results official, we require you to submit the following information for each dataset.

- **Method name**: Name of your method.
- **Contact**: A primary email address to contact you with results and inquiries about the code. 
- **Code**: The Github repository must contain all code to reproduce your results. A placeholder repository is not allowed.
    - We recommend using Pytorch.
    - The authors are responsible for addressing any inquiry about their code. Please make sure results are easily reproducible by giving enough instruction in your repository.
- **Paper**: The paper describing the approach. Always include link to the original paper describing methodology used in experiments. 
- **OGB version**: The OGB version used to conduct the experiments.
- **Results**: Raw results output by OGB model evaluators, where average (`torch.mean`) and unbiased standard deviation (`torch.std`) need to be taken over 10 different random seeds.

We will remove any submissions that are invalidated, so please make sure all the results are correct and reproducible before submitting them.
Please [contact us](ogb@cs.stanford.edu) if there is anything unclear or you have found any problematic submission on the leaderboards.

----

### How to Submit?

Use the [Google form](https://forms.gle/7PB7375i5P1rHgng6) to make a submission. 

The results will be posted after we check the model validity (expect to take about about a week). 

-----

### Explore Leaderboards

* [Node Property Prediction](../leader_nodeprop)

* [Link Property Prediction](../leader_linkprop)

* [Graph Property Prediction](../leader_graphprop)
