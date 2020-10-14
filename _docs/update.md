---
title: Updates from OGB
permalink: /docs/update/
---

##### **Please update your package to [1.2.3](https://github.com/snap-stanford/ogb/releases/tag/1.2.3)** (Sep 12nd, 2020).

-----

#### **Recent Updates**

###### - **Oct 13rd, 2020**: [Rules](../leader_rules) for the experimental protocol clarified.

###### - **Oct 11st, 2020**: Call for dataset contribution.
We opened the dataset contribution from our community. If you have interesting graph datasets, we are looking forward to hearing from you (details [here](https://docs.google.com/document/d/1bSVtHGtSMwu6B3setIrEAnNxI4qBYRoFIClAkk7aOAg/edit?usp=sharing))!

###### - **Sep 25th, 2020**: [OGB paper](https://arxiv.org/abs/2005.00687) accepted to [NeurIPS](https://neurips.cc/).

###### - **Sep 12nd, 2020**: Package updated to [`1.2.3`](https://github.com/snap-stanford/ogb/releases/tag/1.2.3).
- Made `ogbn-papers100M` data loading more tractable by using compressed binary files (fix [issue](https://github.com/snap-stanford/ogb/issues/46)).
- Introduced [DatasetSaver](https://github.com/snap-stanford/ogb/blob/master/ogb/io/README.md) module for external contributors.
- Made dataset object compatible to DGL v0.5 (not backward compatible for heterogeneous graph datasets).

###### - **Aug 11st, 2020**: Package updated to [`1.2.2`](https://github.com/snap-stanford/ogb/releases/tag/1.2.2).
**We changed the evaluation metric of `ogbg-molpcba` from PRC-AUC to Average Precision (AP)**. AP is shown to be more appropriate to summarize the non-convex nature of the Precision Recall Curve [1]. The leaderboard and our paper have been updated accordingly.

[1] Jesse Davis and Mark Goadrich. The relationship between precision-recall and roc curves. InInternational Conference on Machine Learning (ICML), pp. 233–240, 2006.

###### - **July 25th, 2020**: Leaderboard policy updated.
In the leaderboard submission, we additionally require reporting **validation performance** and **tuned hyper-parameters**. 
Our goal is to encourage the fair model selection procedure, by preventing the development of models that are over-tuned to our public test sets. Please refer to [here](../leader_overview) for more details. We thank the community for the great suggestion.
If you have previously made leaderboard submissions, please [tell us](mailto:ogb@cs.stanford.edu) the above two information. 

###### - **June 27th, 2020**: Leaderboard policy updated.
1. Additional information is required for leaderboard submission (thanks to the suggestion from [Google group discussion](https://groups.google.com/forum/#!topic/open-graph-benchmark/duLzqer4mUE) and [Github issue](https://github.com/snap-stanford/ogb/issues/39)).
- We additionally require reporting **hardwares** and **#parameters** in the leaderboard submission. Please refer to [here](../leader_overview) for more details.
- If you have previously made leaderboard submissions, please [tell us](mailto:ogb@cs.stanford.edu) the above two information.

2. The package version requirement has been added for each dataset.
- To make sure all the leaderboard submissions use the same datasets and evaluators, we have added the package version requirement for each dataset. It can be checked at both dataset pages (e.g., [here](../nodeprop/)) and leaderboard pages (e.g., [here](../leader_nodeprop/)).
- We highly recommend always using the newest package version. Our data loader only downloads and processes the modified datasets.

###### - **June 26th, 2020**: Package updated to [`1.2.1`](https://github.com/snap-stanford/ogb/releases/tag/1.2.1).
- **[Bug fix]** The [`ogbn-mag`](../nodeprop/#ogbn-mag) dataset has been changed to exclude duplicated edges (fix [issue](https://github.com/snap-stanford/ogb/issues/40)).
- **[Bug fix]** The Evaluator for [`ogbl-collab`](../linkprop/#ogbl-collab) and [`ogbl-ddi`](../linkprop/#ogbl-ddi) has been changed to use **Hits@50** and **Hits@20**, respectively.
- **[Bug fix]** The DGL data loader for the two heterogeneous graph datasets ([`ogbn-mag`](../nodeprop/#ogbn-mag) and [`ogbl-biokg`](../linkprop/#ogbl-biokg)) is fixed (fix [issue](https://github.com/snap-stanford/ogb/issues/36)).
- Baseline performance on [`ogbn-mag`](../leader_nodeprop/#ogbn-mag), [`ogbl-collab`](../leader_linkprop/#ogbl-collab), [`ogbl-ddi`](../leader_linkprop/#ogbl-ddi), [`ogbl-ppa`](../leader_linkprop/#ogbl-ppa) has been updated.
- [Arxiv paper](https://arxiv.org/abs/2005.00687) has been updated accordingly.

###### - **June 11st, 2020**: Second major release of OGB.
- 5 new datasets ([`ogbn-papers100M`](../nodeprop/#ogbn-papers100M), [`ogbn-mag`](../nodeprop/#ogbn-mag), [`ogbl-biokg`](../linkprop/#ogbl-biokg), [`ogbl-ddi`](../linkprop/#ogbl-ddi), and [`ogbg-code`](../graphprop/#ogbg-code)) and their [benchmark experiments](https://github.com/snap-stanford/ogb/tree/master/examples) have been added.
- Our [arXiv paper](https://arxiv.org/abs/2005.00687) has been updated accordingly.
- Our package has been updated to [`1.2.0`](https://github.com/snap-stanford/ogb/releases/tag/1.2.0) that includes the new datasets. **No change has been applied to the existing datasets.**
- Baseline performance on [`ogbn-products`](../leader_nodeprop/#ogbn-products) and [`ogbl-citation`](../leader_linkprop/#ogbl-citation) has been improved.

###### - **May 4th, 2020**: First major release of OGB.
###### - **May 4th, 2020**: Package updated to [`1.1.1`](https://github.com/snap-stanford/ogb/releases/tag/1.1.1). 
###### - **May 4th, 2020**: Paper uploaded to [arXiv](https://arxiv.org/abs/2005.00687).
###### - **May 1th, 2020**: Package updated to [`1.1.0`](https://github.com/snap-stanford/ogb/releases/tag/1.1.0). 

