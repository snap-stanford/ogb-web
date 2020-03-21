---
title: Leaderboards
permalink: /docs/leader_overview/
---

Public leaderboards allow researchers to keep track of state-of-the-art methods and encourage reproducible research.

-----

### How Leaderboards Work?

Once you have developed your model and got results, you can submit your test results to our leaderboards. 
To make your results official, we require you to submit the following information for each dataset.

- **OGB version**: The OGB version used to conduct the experiments.
- **Method**: The name of the method.
- **Dataset**: The name of an OGB dataset that you use to evaluate the method.
- **Performance**: Raw performance output by OGB model evaluators, where **average (`torch.mean`) and unbiased standard deviation (`torch.std`) must be taken over 10 different random seeds.** You can either not fix random seeds at all, or use the random seeds from 0 to 9. We highly discourage you to tune the random seeds.
- **Contact**: A person's name and email address to contact about the method and code. 
- **Code**: The Github repository or directory containining all code to reproduce the result. **A placeholder repository is not allowed.**
    - We recommend using Pytorch.
    - The authors are responsible for addressing any inquiry about their code. Please make sure results are easily reproducible by giving enough instruction in your repository.
- **Paper**: The original paper describing the method (arXiv link is recommended. paper needs not be peer-reviewed). 
- **Officiality**: Whether the implementation is **official** (implementation by authors who proposed the method) or **unofficial** (re-implementation of the method by non-authors).

**Note:** OGB is a platform for reproducible and reliable research. We will remove any invalid submissions, so please make sure all the results are correct and reproducible before submitting them.
Please [contact us](ogb@cs.stanford.edu) if there is anything unclear or you have found any problematic submission on the leaderboards.

**To authors of original papers/methods:** We highly encourage you to contribute your **official result** to the OGB leaderboards. Even if your method is published *before* the OGB release, please still evaluate your method on OGB datasets and contribute to the leaderboards. **This would be a great opporunity to let people know about your work and compare with it.**

**To contributors who re-implement existing methods:** Even if you are not the original authors, we still encourage you to contribute your **unofficial result** to the leaderboards. This would be valuable especially when your own implementation of existing methods achieve **significantly better** performance than the official counterpart (e.g., by running for longer epochs, or by tuning hyper-parameters more carefully).
Simple tricks can sometimes make methods significantly better!

----

### How to Submit?

Use the [Google form](https://forms.gle/7PB7375i5P1rHgng6) to make a submission. 

The results will be posted after we check the model validity (expect to take about about a week). 

-----

### Explore Leaderboards

* [Node Property Prediction](../leader_nodeprop)

* [Link Property Prediction](../leader_linkprop)

* [Graph Property Prediction](../leader_graphprop)
