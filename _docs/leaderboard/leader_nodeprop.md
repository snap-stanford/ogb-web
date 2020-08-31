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

The **bold** method name indicates that the implementation is **official** (by the author of the original paper). <br/>
**Package** denotes the required package version for each dataset to be eligible for the leaderboard.


<a name="ogbn-products"/>

---------

### Leaderboard for [ogbn-products](../nodeprop/#ogbn-products)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.1.1


| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **DeeperGCN**  | 0.8098 ± 0.0020   | 0.9238 ± 0.0009 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 253,743 | NVIDIA Tesla V100 (32GB GPU) | Jun 28, 2020 |
|  2  |  **GraphSAINT-inductive**  | 0.8027 ± 0.0026   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Hanqing Zeng](mailto:zengh@usc.edu) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/GraphSAINT/GraphSAINT/tree/master/graphsaint/open_graph_benchmark) | 331,661 | Tesla P100 (16GB GPU) | Jul 13, 2020 |
|  3  |  GAT with NeighborSampling  | 0.7945 ± 0.0059   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/rusty1s/pytorch_geometric/blob/master/examples/ogbn_products_gat.py) | 1,751,574 | GeForce RTX 2080 (11GB GPU) | May 24, 2020 |
|  4  |  Cluster-GAT  | 0.7923 ± 0.0078   | 0.8985 ± 0.0022 | [Xiang Song](mailto:classicxsong@gmail.com) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/cluster-gat) | 1,540,848 | EC2 P3.2xlarge (V100) | Aug 2, 2020 |
|  5  |  GraphSAINT (SAGE aggr)  | 0.7908 ± 0.0024   | 0.9162 ± 0.0008 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  6  |  ClusterGCN (SAGE aggr)  | 0.7897 ± 0.0033   | 0.9212 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  7  |  NeighborSampling (SAGE aggr)  | 0.7870 ± 0.0036   | 0.9170 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  8  |  Full-batch GraphSAGE  | 0.7850 ± 0.0014   | 0.9224 ± 0.0007 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  9  |  GraphSAGE  | 0.7829 ± 0.0016   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Quan Gan (DGL Team)](mailto:quagan@amazon.com) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-products/graphsage) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 12, 2020 |
|  10  |  Full-batch GCN  | 0.7564 ± 0.0021   | 0.9200 ± 0.0003 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 103,727 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  11  |  Node2vec  | 0.7249 ± 0.0010   | 0.9032 ± 0.0006 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 313,612,207 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  12  |  MLP  | 0.6106 ± 0.0008   | 0.7554 ± 0.0014 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 103,727 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |


<a name="ogbn-proteins"/>

------

### Leaderboard for [ogbn-proteins](../nodeprop/#ogbn-proteins)
##### The ROC-AUC score on the test and validation sets. The higher, the better.

#### Package: >=1.1.1

| Rank  | Method | Test ROC-AUC | Validation ROC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **DeeperGCN**  | 0.8580 ± 0.0017   | 0.9106 ± 0.0016 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 2,374,568 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  2  |  **DeepGCN**  | 0.8496 ± 0.0028   | 0.8971 ± 0.0011 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](http://openaccess.thecvf.com/content_ICCV_2019/papers/Li_DeepGCNs_Can_GCNs_Go_As_Deep_As_CNNs_ICCV_2019_paper.pdf), [Code](https://github.com/lightaime/deep_gcns_torch/blob/master/examples/ogb/ogbn_proteins) | 2,374,456 | NVIDIA Tesla V100 (32GB GPU) | Jun 20, 2020 |
|  3  |  **MWE-DGCN**  | 0.8436 ± 0.0065   | 0.8973 ± 0.0057 |[Zhengdao Chen](mailto:zc1216@nyu.edu) | [Paper](https://cims.nyu.edu/~chenzh/files/GCN_with_edge_weights.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-proteins) | 538,544 | NVIDIA Tesla V100 (16GB GPU) | Jul 20, 2020 |
|  4  |  **GeniePath-BS**  | 0.7825 ± 0.0035   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Zhengwei WU (AGL Team)](mailto:zejun.wzw@alipay.com) | [Paper](http://arxiv.org/abs/2006.05806), [Code](https://github.com/xavierzw/ogb-geniepath-bs) | 316,754 | Intel Xeon E5-2682 v4 (512GB CPU) | Jun 10, 2020 |
|  5  |  GaAN  | 0.7803 ± 0.0073   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Wenjin Wang (PGL Team)](mailto:wangwenjin02@baidu.com) | [Paper](https://arxiv.org/abs/1803.07294), [Code](https://github.com/PaddlePaddle/PGL/tree/master/examples/GaAN) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 26, 2020 |
|  6  |  GraphSAGE  | 0.7768 ± 0.0020   | 0.8334 ± 0.0013 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 193,136 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  7  |  GCN  | 0.7251 ± 0.0035   | 0.7921 ± 0.0018 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 96,880 | GeForce RTX 2080 (11GB GPU) | Jul 17, 2020 |
|  8  |  MLP  | 0.7204 ± 0.0048   | 0.7706 ± 0.0014 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 96,880 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  9  |  Node2vec  | 0.6881 ± 0.0065   | 0.7007 ± 0.0053 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 17,094,000 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |


<a name="ogbn-arxiv"/>

---------

### Leaderboard for [ogbn-arxiv](../nodeprop/#ogbn-arxiv)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.1.1

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GCNII**  | 0.7274 ± 0.0016   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Ming Chen](mailto:chennnming@outlook.com) | [Paper](https://arxiv.org/abs/2007.02133), [Code](https://github.com/chennnM/GCNII/tree/master/PyG/ogbn-arxiv) | 2,148,648 | Quadro RTX 8000 (48GB GPU) | Jul 7, 2020 |
|  2  |  GCN  | 0.7248 ± 0.0012   | 0.7375 ± 0.0012 | [Yangkun Wang](mailto:wyangkun@amazon.com) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/dmlc/dgl/blob/master/examples/pytorch/ogb/ogbn-arxiv/gcn.py) | 110,120 | g4dn.12xlarge, T4 (15GB GPU) | Aug 31, 2020 |
|  3  |  JKNet (GCN-based)  | 0.7219 ± 0.0021   | 0.7335 ± 0.0007 | [Weiran Huang](mailto:huangweiran1998@outlook.com) | [Paper](https://arxiv.org/pdf/1806.03536.pdf), [Code](https://github.com/EtoDemerzel0427/ogbn-arxiv-baselines/blob/master/JKNet.py) | 89,000 | Tesla T4 | Aug 26, 2020 |
|  4  |  **DAGNN**  | 0.7209 ± 0.0025   | 0.7290 ± 0.0011 |[Meng Liu - DIVE@TAMU](mailto:mengliu@tamu.edu) | [Paper](https://arxiv.org/abs/2007.09296), [Code](https://github.com/mengliu1998/DeeperGNN) | 43,857 | GeForce RTX 2080 Ti (11GB GPU) | Aug 19, 2020 |
|  5  |  GaAN  | 0.7197 ± 0.0024   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hui Zhong (PGL Team)](mailto:zhonghui03@baidu.com) | [Paper](https://arxiv.org/abs/1803.07294), [Code](https://github.com/PaddlePaddle/PGL/tree/master/ogb_examples/nodeproppred/ogbn-arxiv) | 1,471,506 | NVIDIA Tesla V100 (16GB GPU) | Jun 16, 2020 |
|  6  |  **DeeperGCN**  | 0.7192 ± 0.0016   | 0.7262 ± 0.0014 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 491,176 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  7  |  GCN  | 0.7174 ± 0.0029   | 0.7300 ± 0.0017 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 142,888 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  8  |  GraphSAGE  | 0.7149 ± 0.0027   | 0.7277 ± 0.0016 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 218,664 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  9  |  **GraphZoom (Node2vec)**  | 0.7118 ± 0.0018   | 0.7220 ± 0.0007 |[Xiuyu Li - GraphZoom](mailto:xl289@cornell.edu) | [Paper](https://openreview.net/forum?id=r1lGO0EKDH), [Code](https://github.com/cornell-zhang/GraphZoom/tree/master/ogb/ogbn-arxiv) | 8,963,624 | GeForce GTX 1080 Ti (11GB GPU) | Jul 2, 2020 |
|  10  |  Node2vec  | 0.7007 ± 0.0013   | 0.7129 ± 0.0013 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 21,818,792 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  11  |  MLP  | 0.5550 ± 0.0023   | 0.5765 ± 0.0012 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 110,120 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |



<a name="ogbn-papers100M"/>

---------

### Leaderboard for [ogbn-papers100M](../nodeprop/#ogbn-papers100M)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.2.0

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  SGC  | 0.6329 ± 0.0019   | 0.6648 ± 0.0020 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.07153), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 144,044 | Xeon E7-8890x (1.5TB CPU) | Jun 10, 2020 |
|  2  |  Node2vec  | 0.5560 ± 0.0023   | 0.5807 ± 0.0028 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 14,215,818,412 | Xeon E7-8890x (1.5TB CPU) | Jun 26, 2020 |
|  3  |  MLP  | 0.4724 ± 0.0031   | 0.4960 ± 0.0029 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 144,044 | Xeon E7-8890x (1.5TB CPU) | Jun 10, 2020 |




<a name="ogbn-mag"/>

---------

### Leaderboard for [ogbn-mag](../nodeprop/#ogbn-mag)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **HGT (LADIES Sample)**  | 0.5007 ± 0.0043   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Ziniu Hu](mailto:bull@cs.ucla.edu) | [Paper](https://arxiv.org/abs/2003.01332), [Code](https://github.com/acbull/pyHGT/tree/master/ogbn-mag) | 21,173,389 | Tesla K80 (12GB GPU) | Jul 7, 2020 |
|  2  |  GraphSAINT (R-GCN aggr)  | 0.4751 ± 0.0022   | 0.4837 ± 0.0026 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  3  |  NeighborSampling (R-GCN aggr)  | 0.4678 ± 0.0067   | 0.4761 ± 0.0068 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  4  |  Full-batch R-GCN  | 0.3977 ± 0.0046   | 0.4084 ± 0.0041 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1703.06103), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | Quadro RTX 8000 (48GB GPU) | Jun 26, 2020 |
|  5  |  ClusterGCN (R-GCN aggr)  | 0.3732 ± 0.0037   | 0.3840 ± 0.0031 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  6  |  MetaPath2vec  | 0.3544 ± 0.0036   | 0.3506 ± 0.0017 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://ericdongyx.github.io/papers/KDD17-dong-chawla-swami-metapath2vec.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 94,479,069 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  7  |  MLP  | 0.2692 ± 0.0026   | 0.2626 ± 0.0016 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 188,509 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |





