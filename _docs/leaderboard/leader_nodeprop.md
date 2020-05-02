---
title: Leaderboards for Node Property Prediction
permalink: /docs/leader_nodeprop/
---

##### Check leaderboards for
###### - [ogbn-products](#ogbn-products)
###### - [ogbn-arxiv](#ogbn-arxiv)
###### - [ogbn-proteins](#ogbn-proteins)

**Note:** The **bold** method name indicates that the implementation is **official** (by the author of the original paper).


<a name="ogbn-products"/>

---------

### Leaderboard for [ogbn-products](../nodeprop/#ogbn-products)
The classification accuracy on the test set. The higher, the better.


| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  GraphSAINT (SAGE aggr)  | 0.7729 ± 0.0019   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | May 1, 2020 | 
|  2  |  ClusterGCN (SAGE aggr)  | 0.7518 ± 0.0041   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | May 1, 2020 | 
|  3  |  Node2vec  | 0.7212 ± 0.0024   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | May 1, 2020 | 
|  4  |  MLP  | 0.6112 ± 0.0010   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](OGB), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | May 1, 2020 | 


<a name="ogbn-arxiv"/>

---------

### Leaderboard for [ogbn-arxiv](../nodeprop/#ogbn-arxiv)
The classification accuracy on the test set. The higher, the better.


| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  GCN  | 0.7174 ± 0.0029   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | May 1, 2020 | 
|  2  |  GraphSAGE  | 0.7149 ± 0.0027   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | May 1, 2020 | 
|  3  |  Node2vec  | 0.7007 ± 0.0013   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | May 1, 2020 | 
|  4  |  MLP  | 0.5550 ± 0.0023   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](OGB), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | May 1, 2020 | 



<a name="ogbn-proteins"/>

------

### Leaderboard for [ogbn-proteins](../nodeprop/#ogbn-proteins)
The ROC-AUC score on the test set. The higher, the better.

| Rank  | Method | ROC-AUC | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  GraphSAGE  | 0.7768 ± 0.0020   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | May 1, 2020 | 
|  2  |  MLP  | 0.7204 ± 0.0048   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](OGB), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | May 1, 2020 | 
|  3  |  Node2vec  | 0.6881 ± 0.0065   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | May 1, 2020 | 
|  4  |  GCN  | 0.6511 ± 0.0152   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | May 1, 2020 | 


