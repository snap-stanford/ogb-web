---
title: Leaderboards for Node Property Prediction
permalink: /docs/leader_nodeprop/
---

##### Check leaderboards for
###### - [ogbn-proteins](#ogbn-proteins)
###### - [ogbn-products](#ogbn-products)

**Note:** The **bold** method name indicates that the implementation is **official** (by the author of the original paper).

<a name="ogbn-proteins"/>

------

### Leaderboard for [ogbn-proteins](../nodeprop/#ogbn-proteins)
The ROC-AUC score on the test set. The higher, the better.

| Rank  | Method | ROC-AUC | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  ClusterGCN  | 0.7513 ± 0.0044   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | Mar 20, 2020 | 
|  2  |  node2vec  | 0.6216 ± 0.0101   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | Mar 20, 2020 | 


<a name="ogbn-products"/>

---------

### Leaderboard for [ogbn-products](../nodeprop/#ogbn-products)
The classification accuracy on the test set. The higher, the better.


| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  Full-batch GraphSAGE  | 0.7803 ± 0.0022   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Mar 20, 2020 | 
|  2  |  Full-batch GCN  | 0.7565 ± 0.0020   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Mar 20, 2020 | 
|  3  |  ClusterGCN  | 0.7241 ± 0.0032   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Mar 20, 2020 | 
|  4  |  node2vec  | 0.7212 ± 0.0024   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Mar 20, 2020 | 

