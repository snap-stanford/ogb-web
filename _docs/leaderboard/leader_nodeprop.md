---
title: Leaderboards for Node Property Prediction
permalink: /docs/leader_nodeprop/
---

##### Check leaderboards for
###### - [ogbn-products](#ogbn-products)
###### - [ogbn-proteins](#ogbn-proteins)
###### - [ogbn-arxiv](#ogbn-arxiv)
###### - [ogbn-papers100M](#ogbn-papers100M)
###### - [ogbn-mag](#ogbn-mag)


**Note:** The **bold** method name indicates that the implementation is **official** (by the author of the original paper).


<a name="ogbn-products"/>

---------

### Leaderboard for [ogbn-products](../nodeprop/#ogbn-products)
The classification accuracy on the test set. The higher, the better.


| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  GAT with NeighborSampling  | 0.7945 ± 0.0059   | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/rusty1s/pytorch_geometric/blob/master/examples/ogbn_products_gat.py) | May 24, 2020 | 
|  2  |  GraphSAINT (SAGE aggr)  | 0.7908 ± 0.0024   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Jun 10, 2020 | 
|  3  |  ClusterGCN (SAGE aggr)  | 0.7897 ± 0.0033   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Jun 10, 2020 | 
|  4  |  NeighborSampling (SAGE aggr)  | 0.7870 ± 0.0036   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Jun 10, 2020 | 
|  5  |  GraphSAGE  | 0.7829 ± 0.0016   | [Quan Gan (DGL Team)](mailto:quagan@amazon.com) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-products/graphsage) | May 12, 2020 | 
|  6  |  Node2vec  | 0.7249 ± 0.0010   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Jun 10, 2020 | 
|  7  |  MLP  | 0.6106 ± 0.0008   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | Jun 10, 2020 | 


<a name="ogbn-proteins"/>

------

### Leaderboard for [ogbn-proteins](../nodeprop/#ogbn-proteins)
The ROC-AUC score on the test set. The higher, the better.

| Rank  | Method | ROC-AUC | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  **GeniePath-BS**  | 0.7825 ± 0.0035   | [Zhengwei WU (AGL Team)](mailto:zejun.wzw@alipay.com) | [Paper](http://arxiv.org/abs/2006.05806), [Code](https://github.com/xavierzw/ogb-geniepath-bs) | Jun 10, 2020 | 
|  2  |  GaAN  | 0.7803 ± 0.0073   | [Wenjin Wang (PGL Team)](mailto:wangwenjin02@baidu.com) | [Paper](https://arxiv.org/abs/1803.07294), [Code](https://github.com/PaddlePaddle/PGL/tree/master/examples/GaAN) | May 26, 2020 | 
|  3  |  GraphSAGE  | 0.7768 ± 0.0020   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | May 1, 2020 | 
|  4  |  MLP  | 0.7204 ± 0.0048   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | May 1, 2020 | 
|  5  |  Node2vec  | 0.6881 ± 0.0065   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | May 1, 2020 | 
|  6  |  GCN  | 0.6511 ± 0.0152   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | May 1, 2020 | 


<a name="ogbn-arxiv"/>

---------

### Leaderboard for [ogbn-arxiv](../nodeprop/#ogbn-arxiv)
The classification accuracy on the test set. The higher, the better.


| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  GaAN  | 0.7197 ± 0.0024   | [Hui Zhong (PGL Team)](mailto:zhonghui03@baidu.com) | [Paper](https://arxiv.org/abs/1803.07294), [Code](https://github.com/PaddlePaddle/PGL/tree/master/ogb_examples/nodeproppred/ogbn-arxiv) | Jun 16, 2020 | 
|  2  |  GCN  | 0.7174 ± 0.0029   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | May 1, 2020 | 
|  3  |  GraphSAGE  | 0.7149 ± 0.0027   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | May 1, 2020 | 
|  4  |  Node2vec  | 0.7007 ± 0.0013   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | May 1, 2020 | 
|  5  |  MLP  | 0.5550 ± 0.0023   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | May 1, 2020 | 


<a name="ogbn-papers100M"/>

---------

### Leaderboard for [ogbn-papers100M](../nodeprop/#ogbn-papers100M)
The classification accuracy on the test set. The higher, the better.


| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  SGC  | 0.6329 ± 0.0019   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.07153), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | Jun 10, 2020 | 
|  2  |  MLP  | 0.4724 ± 0.0031   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | Jun 10, 2020 | 



<a name="ogbn-mag"/>

---------

### Leaderboard for [ogbn-mag](../nodeprop/#ogbn-mag)
The classification accuracy on the test set. The higher, the better.


| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  GraphSAINT (R-GCN aggr)  | 0.4770 ± 0.0024   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | Jun 10, 2020 | 
|  2  |  NeighborSampling (R-GCN aggr)  | 0.4662 ± 0.0046   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | Jun 10, 2020 | 
|  3  |  ClusterGCN (R-GCN aggr)  | 0.3749 ± 0.0040   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | Jun 10, 2020 | 
|  4  |  MetaPath2vec  | 0.3551 ± 0.0030   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://ericdongyx.github.io/papers/KDD17-dong-chawla-swami-metapath2vec.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | Jun 10, 2020 | 
|  5  |  MLP  | 0.2682 ± 0.0031   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | Jun 10, 2020 | 





