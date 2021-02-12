---
title: Leaderboards for Link Property Prediction
permalink: /docs/leader_linkprop/
---

##### Check leaderboards for
###### - [ogbl-ppa](#ogbl-ppa)
###### - [ogbl-collab](#ogbl-collab)
###### - [ogbl-ddi](#ogbl-ddi)
###### - [ogbl-citation2](#ogbl-citation2)
###### - [ogbl-wikikg2](#ogbl-wikikg2)
###### - [ogbl-biokg](#ogbl-biokg)

The **bold** method name indicates that the implementation is **official** (by the author of the original paper). <br/>
**Package** denotes the required package version for each dataset to be eligible for the leaderboard.


<a name="ogbl-ppa"/>

-------

### Leaderboard for [ogbl-ppa](../linkprop/#ogbl-ppa)
##### The Hits@100 score on the test and validation sets. The higher, the better.

#### Package: >=1.1.1

| Rank  | Method | Test Hits@100 | Validation Hits@100 | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **SEAL**  | 0.4880 ± 0.0316   | 0.5125 ± 0.0252 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/1802.09691.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 709,122 | GeForce RTX 2080S (8GB GPU) | Oct 14, 2020 |
|  2  |  Matrix Factorization  | 0.3229 ± 0.0094   | 0.3228 ± 0.0428 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 147,662,849 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  3  |  DeepWalk  | 0.2888 ± 0.0153   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 150,138,741 | g4dn.2xlarge, T4 (15GB GPU) | Jul 23, 2020 |
|  4  |  Common Neighbor  | 0.2765 ± 0.0000   | 0.2823 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  5  |  DeepWalk  | 0.2302 ± 0.0163   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 150,138,741 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  6  |  Node2vec  | 0.2226 ± 0.0083   | 0.2253 ± 0.0088 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 73,878,913 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  7  |  GCN  | 0.1867 ± 0.0132   | 0.1845 ± 0.0140 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 278,529 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  8  |  GraphSAGE  | 0.1655 ± 0.0240   | 0.1724 ± 0.0264 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 424,449 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |




<a name="ogbl-collab"/>

-------

### Leaderboard for [ogbl-collab](../linkprop/#ogbl-collab)
##### The Hits@50 score on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Test Hits@50 | Validation Hits@50 | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **SEAL (val as input)**  | 0.6364 ± 0.0071   | 0.6389 ± 0.0049 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/1802.09691.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 76,482 | GeForce RTX 2080S (8GB GPU) | Oct 22, 2020 |
|  2  |  Common Neighbor  | 0.6137 ± 0.0000   | 0.6036 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  3  |  GraphSAGE  (val as input)  | 0.5463 ± 0.0112   | 0.5688 ± 0.0077 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 460,289 | GeForce RTX 2080 (11GB GPU) | Oct 19, 2020 |
|  4  |  **SEAL**  | 0.5371 ± 0.0047   | 0.6389 ± 0.0049 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/1802.09691.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 76,482 | GeForce Tesla P100 (16GB GPU) | Oct 14, 2020 |
|  5  |  **DeeperGCN**  | 0.5273 ± 0.0047   | 0.6187 ± 0.0045 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 117,383 | NVIDIA Tesla V100 (32GB GPU) | Oct 21, 2020 |
|  6  |  **LRGA + GCN**  | 0.5221 ± 0.0072   | 0.6088 ± 0.0059 |[Omri Puny](mailto:omri.puny@weizmann.ac.il) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/omri1348/LRGA/tree/master/ogb/examples/linkproppred) | 1,069,489 | Tesla P100 (16GB GPU) | Aug 5, 2020 |
|  7  |  DeepWalk  | 0.5037 ± 0.0034   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 61,390,187 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  8  |  Node2vec  | 0.4888 ± 0.0054   | 0.5703 ± 0.0052 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 30,322,945 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  9  |  GraphSAGE  | 0.4810 ± 0.0081   | 0.5688 ± 0.0077 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 460,289 | GeForce RTX 2080 (11GB GPU) | Jun 24, 2020 |
|  10  |  GCN (val as input)  | 0.4714 ± 0.0145   | 0.5263 ± 0.0115 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 296,449 | GeForce RTX 2080 (11GB GPU) | Oct 19, 2020 |
|  11  |  GCN  | 0.4475 ± 0.0107   | 0.5263 ± 0.0115 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jun 24, 2020 |
|  12  |  Matrix Factorization  | 0.3886 ± 0.0029   | 0.4896 ± 0.0029 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 60,514,049 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |




<a name="ogbl-ddi"/>

-------

### Leaderboard for [ogbl-ddi](../linkprop/#ogbl-ddi)
##### The Hits@20 score on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Test Hits@20 | Validation Hits@20 | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **MAD Learning**  | 0.6781 ± 0.0294   | 0.7010 ± 0.0082 |[Yi Luo](mailto:cf020031308@163.com) | [Paper](https://arxiv.org/abs/2102.05246), [Code](https://github.com/cf020031308/mad-learning/blob/master/ogbl-ddi.py) | 1,228,897 | Geforce GTX 1080 Ti (11GB GPU) | Feb 10, 2021 |
|  2  |  **LRGA + GCN**  | 0.6230 ± 0.0912   | 0.6675 ± 0.0058 |[Omri Puny](mailto:omri.puny@weizmann.ac.il) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/omri1348/LRGA/tree/master/ogb/examples/linkproppred) | 1,576,081 | Tesla P100 (16GB GPU) | Aug 5, 2020 |
|  3  |  GCN+JKNet  | 0.6056 ± 0.0869   | 0.6776 ± 0.0095 | [Horace He  (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/Chillee/ogb_ddi) | 1,421,571 | Geforce GTX 1080 Ti (11GB GPU) | Sep 15, 2020 |
|  4  |  GraphSAGE  | 0.5390 ± 0.0474   | 0.6262 ± 0.0037 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,421,057 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  5  |  GCN  | 0.3707 ± 0.0507   | 0.5550 ± 0.0208 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,289,985 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  6  |  **SEAL**  | 0.3056 ± 0.0386   | 0.2849 ± 0.0269 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/1802.09691.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 531,138 | GeForce RTX 2080S (8GB GPU) | Oct 14, 2020 |
|  7  |  DeepWalk  | 0.2642 ± 0.0610   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 11,543,913 | g4dn.2xlarge, T4 (15GB GPU) | Jul 23, 2020 |
|  8  |  Node2vec  | 0.2326 ± 0.0209   | 0.3292 ± 0.0121 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 645,249 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  9  |  DeepWalk  | 0.2246 ± 0.0290   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 1,543,913 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  10  |  Common Neighbor  | 0.1773 ± 0.0000   | 0.0947 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  11  |  Matrix Factorization  | 0.1368 ± 0.0475   | 0.3370 ± 0.0264 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,224,193 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |




<a name="ogbl-citation2"/>

-------

### Leaderboard for [ogbl-citation2](../linkprop/#ogbl-citation2)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.4
###### Deprecated `ogbl-citation` leaderboard can be found [here](../leader_deprecated/#ogbl-citation).

| Rank  | Method | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **SEAL**  | 0.8767 ± 0.3216   | 0.8757 ± 0.3119 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 260,802 | Tesla V100 (32GB GPU) | Feb 12, 2021 |
|  2  |  Full-batch GCN  | 0.8474 ± 0.0021   | 0.8479 ± 0.0023 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | Quadro RTX 8000 (48GB GPU) | Jan 4, 2021 |
|  3  |  Full-batch GraphSAGE  | 0.8260 ± 0.0036   | 0.8263 ± 0.0033 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 460,289 | Quadro RTX 8000 (48GB GPU) | Jan 4, 2021 |
|  4  |  NeighborSampling (SAGE aggr)  | 0.8044 ± 0.0010   | 0.8054 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 460,289 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  5  |  ClusterGCN (GCN aggr)  | 0.8004 ± 0.0025   | 0.7994 ± 0.0025 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  6  |  GraphSAINT (GCN aggr)  | 0.7985 ± 0.0040   | 0.7975 ± 0.0039 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  7  |  Node2vec  | 0.6141 ± 0.0011   | 0.6124 ± 0.0011 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 374,911,105 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  8  |  Matrix Factorization  | 0.5186 ± 0.0443   | 0.5181 ± 0.0436 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 281,113,505 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  9  |  Common Neighbor  | 0.5147 ± 0.0000   | 0.5119 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |



<a name="ogbl-wikikg2"/>

-------

### Leaderboard for [ogbl-wikikg2](../linkprop/#ogbl-wikikg2)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.4
###### Deprecated `ogbl-wikikg` leaderboard can be found [here](../leader_deprecated/#ogbl-wikikg).

| Rank  | Method | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **PairRE (200dim)**  | 0.5208 ± 0.0027   | 0.5423 ± 0.0020 |[Linlin Chao](mailto:chulin.cll@antgroup.com) | [Paper](https://arxiv.org/abs/2011.03798), [Code](https://github.com/alipay/KnowledgeGraphEmbeddingsViaPairedRelationVectors_PairRE) | 500,334,800 | Tesla P100 (16GB GPU) | Jan 28, 2021 |
|  2  |  RotatE (250dim)  | 0.4332 ± 0.0025   | 0.4353 ± 0.0028 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,435,750 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  3  |  TransE (500dim)  | 0.4256 ± 0.0030   | 0.4272 ± 0.0030 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  4  |  ComplEx (250dim)  | 0.4027 ± 0.0027   | 0.3759 ± 0.0016 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  5  |  ComplEx (50dim)  | 0.3804 ± 0.0022   | 0.3534 ± 0.0052 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  6  |  DistMult (500dim)  | 0.3729 ± 0.0045   | 0.3506 ± 0.0042 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  7  |  DistMult (100dim)  | 0.3447 ± 0.0082   | 0.3150 ± 0.0088 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  8  |  TransE (100dim)  | 0.2622 ± 0.0045   | 0.2465 ± 0.0020 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  9  |  RotatE (50dim)  | 0.2530 ± 0.0034   | 0.2250 ± 0.0035 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,087,150 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |





<a name="ogbl-biokg"/>

-------

### Leaderboard for [ogbl-biokg](../linkprop/#ogbl-biokg)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.0

| Rank  | Method | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **PairRE**  | 0.8164 ± 0.0005   | 0.8172 ± 0.0005 |[LinlinChao (AntGroup KG&NLP)](mailto:chulin.cll@antgroup.com) | [Paper](https://arxiv.org/abs/2011.03798), [Code](https://github.com/alipay/KnowledgeGraphEmbeddingsViaPairedRelationVectors_PairRE) | 187,750,000 | Tesla P100 (16GB GPU) | Nov 9, 2020 |
|  2  |  ComplEx  | 0.8095 ± 0.0007   | 0.8105 ± 0.0001 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  3  |  DistMult  | 0.8043 ± 0.0003   | 0.8055 ± 0.0003 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  4  |  RotatE  | 0.7989 ± 0.0004   | 0.7997 ± 0.0002 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,597,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  5  |  TransE  | 0.7452 ± 0.0004   | 0.7456 ± 0.0003 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |





