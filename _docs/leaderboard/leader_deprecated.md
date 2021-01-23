---
title: Deprecated Leaderboards
permalink: /docs/leader_deprecated/
---

##### Check leaderboards for
###### - [ogbl-citation](#ogbl-citation)
###### - [ogbl-wikikg](#ogbl-wikikg)
###### **Note:** These leaderboards are deprecated and will no longer updated.

The **bold** method name indicates that the implementation is **official** (by the author of the original paper). <br/>
**Package** denotes the required package version for each dataset to be eligible for the leaderboard.



<a name="ogbl-citation"/>

-------

### Deprecated Leaderboard for ogbl-citation
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.1.1, <=1.2.3
###### Deprecated due to a bug in test/val negative samples. [`ogbl-citation2`](../linkprop/#ogbl-citation2) fixes the issue.
###### The new leaderboard for [`ogbl-citation2`](../linkprop/#ogbl-citation2)  can be found [here](../leader_linkprop/#ogbl-citation2).

| Rank  | Method | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **SEAL**  | 0.8527 ± 0.0091   | 0.8509 ± 0.0088 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/1802.09691.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 871,106 | Tesla V100 (32GB GPU) | Oct 14, 2020 |
|  2  |  Full-batch GCN  | 0.8456 ± 0.0110   | 0.8449 ± 0.0108 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | 296,449 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  3  |  DeepWalk  | 0.8284 ± 0.0005   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 757,943,019 | g4dn.2xlarge, T4 (15GB GPU) | Jul 23, 2020 |
|  4  |  Full-batch GraphSAGE  | 0.8228 ± 0.0084   | 0.8217 ± 0.0086 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | 460,289 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  5  |  DeepWalk  | 0.8148 ± 0.0004   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 757,943,019 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  6  |  NeighborSampling (SAGE aggr)  | 0.8048 ± 0.0015   | 0.8048 ± 0.0015 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | 460,289 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  7  |  ClusterGCN (GCN aggr)  | 0.8021 ± 0.0029   | 0.7999 ± 0.0027 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  8  |  GraphSAINT (GCN aggr)  | 0.7943 ± 0.0043   | 0.7933 ± 0.0046 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  9  |  Node2vec  | 0.5964 ± 0.0011   | 0.5944 ± 0.0011 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | 374,911,105 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  10  |  Matrix Factorization  | 0.5316 ± 0.0565   | 0.5311 ± 0.0565 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | 281,113,505 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |



<a name="ogbl-wikikg"/>

-------

### Deprecated Leaderboard for ogbl-wikikg
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.1.1, <=1.2.3
###### Deprecated due to a bug in test/val negative samples. [`ogbl-wikikg2`](../linkprop/#ogbl-wikikg2) fixes the issue.
###### The new leaderboard for [`ogbl-wikikg2`](../linkprop/#ogbl-wikikg2) can be found [here](../leader_linkprop/#ogbl-wikikg2).

| Rank  | Method | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **PairRE**  | 0.5289 ± 0.0030   | 0.5529 ± 0.0010 |[Linlin Chao (AntGroup KG&NLP)](mailto:chulin.cll@antgroup.com) | [Paper](https://arxiv.org/abs/2011.03798), [Code](https://github.com/alipay/KnowledgeGraphEmbeddingsViaPairedRelationVectors_PairRE) | 500,334,800 | Tesla P100 (16GB GPU) | Nov 9, 2020 |
|  2  |  TransE (600dim)  | 0.4536 ± 0.0028   | 0.4587 ± 0.0031 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | 1,500,683,400 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  3  |  ComplEx (300dim)  | 0.4028 ± 0.0033   | 0.3787 ± 0.0036 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | 1,500,683,400 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  4  |  ComplEx (50dim)  | 0.3877 ± 0.0051   | 0.3612 ± 0.0063 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  5  |  RotatE (300dim)  | 0.3626 ± 0.0041   | 0.3613 ± 0.0031 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | 1,500,522,900 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  6  |  DistMult (600dim)  | 0.3612 ± 0.0030   | 0.3403 ± 0.0009 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | 1,500,683,400 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  7  |  DistMult (100dim)  | 0.3434 ± 0.0079   | 0.3142 ± 0.0066 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  8  |  RotatE (50dim)  | 0.2681 ± 0.0047   | 0.2366 ± 0.0043 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | 250,087,150 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  9  |  TransE (100dim)  | 0.2535 ± 0.0036   | 0.2314 ± 0.0035 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |





