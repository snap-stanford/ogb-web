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
|  1  |  **MLP + C&S**  | 0.8418 ± 0.0007   | 0.9147 ± 0.0009 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 96,247 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  2  |  **Linear + C&S**  | 0.8301 ± 0.0001   | 0.9134 ± 0.0001 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 10,763 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  3  |  **UniMP**  | 0.8256 ± 0.0031   | 0.9308 ± 0.0017 |[Yunsheng Shi (PGL team)](mailto:shiyunsheng01@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp) | 1,475,605 | Tesla V100 (32GB) | Sep 8, 2020 |
|  4  |  **Plain Linear + C&S**  | 0.8254 ± 0.0003   | 0.9103 ± 0.0001 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 4,747 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  5  |  **DeeperGCN+FLAG**  | 0.8193 ± 0.0031   | 0.9221 ± 0.0037 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 253,743 | NVIDIA Tesla V100 (32GB GPU) | Oct 20, 2020 |
|  6  |  **GAT+FLAG**  | 0.8176 ± 0.0045   | 0.9251 ± 0.0006 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 751,574 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  7  |  **DeeperGCN**  | 0.8098 ± 0.0020   | 0.9238 ± 0.0009 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 253,743 | NVIDIA Tesla V100 (32GB GPU) | Jun 28, 2020 |
|  8  |  **GraphSAINT-inductive**  | 0.8027 ± 0.0026   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Hanqing Zeng](mailto:zengh@usc.edu) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/GraphSAINT/GraphSAINT/tree/master/graphsaint/open_graph_benchmark) | 331,661 | Tesla P100 (16GB GPU) | Jul 13, 2020 |
|  9  |  ClusterGCN+residual+3 layers  | 0.7971 ± 0.0042   | 0.9188 ± 0.0008 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/Chillee/ogb_baselines) | 456,034 | GeForce RTX 2080 (11GB GPU) | Oct 6, 2020 |
|  10  |  GAT with NeighborSampling  | 0.7945 ± 0.0059   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/rusty1s/pytorch_geometric/blob/master/examples/ogbn_products_gat.py) | 751,574 | GeForce RTX 2080 (11GB GPU) | May 24, 2020 |
|  11  |  **GraphSAGE+FLAG**  | 0.7936 ± 0.0057   | 0.9205 ± 0.0007 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 206,895 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  12  |  Cluster-GAT  | 0.7923 ± 0.0078   | 0.8985 ± 0.0022 | [Xiang Song](mailto:classicxsong@gmail.com) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/cluster-gat) | 1,540,848 | EC2 P3.2xlarge (V100) | Aug 2, 2020 |
|  13  |  GraphSAINT (SAGE aggr)  | 0.7908 ± 0.0024   | 0.9162 ± 0.0008 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  14  |  ClusterGCN (SAGE aggr)  | 0.7897 ± 0.0033   | 0.9212 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  15  |  NeighborSampling (SAGE aggr)  | 0.7870 ± 0.0036   | 0.9170 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  16  |  Full-batch GraphSAGE  | 0.7850 ± 0.0014   | 0.9224 ± 0.0007 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  17  |  GraphSAGE  | 0.7829 ± 0.0016   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Quan Gan (DGL Team)](mailto:quagan@amazon.com) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-products/graphsage) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 12, 2020 |
|  18  |  Full-batch GCN  | 0.7564 ± 0.0021   | 0.9200 ± 0.0003 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 103,727 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  19  |  Label Propagation  | 0.7434 ± 0.0000   | 0.9091 ± 0.0000 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](http://pages.cs.wisc.edu/~jerryzhu/pub/thesis.pdf), [Code](https://github.com/Chillee/CorrectAndSmoothOGB) | 0 | GeForce RTX 2080 (11GB GPU) | Oct 3, 2020 |
|  20  |  **GraphZoom (Node2vec)**  | 0.7406 ± 0.0026   | 0.9066 ± 0.0011 |[Xiuyu Li - GraphZoom](mailto:xl289@cornell.edu) | [Paper](https://openreview.net/forum?id=r1lGO0EKDH), [Code](https://github.com/cornell-zhang/GraphZoom/tree/master/ogb/ogbn-products) | 120,251,183 | NVIDIA TITAN RTX (24GB GPU) | Oct 6, 2020 |
|  21  |  Node2vec  | 0.7249 ± 0.0010   | 0.9032 ± 0.0006 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 313,612,207 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  22  |  MLP  | 0.6106 ± 0.0008   | 0.7554 ± 0.0014 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 103,727 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |


<a name="ogbn-proteins"/>

------

### Leaderboard for [ogbn-proteins](../nodeprop/#ogbn-proteins)
##### The ROC-AUC score on the test and validation sets. The higher, the better.

#### Package: >=1.1.1

| Rank  | Method | Test ROC-AUC | Validation ROC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **UniMP**  | 0.8642 ± 0.0008   | 0.9175 ± 0.0006 |[Yunsheng Shi (PGL team)](mailto:shiyunsheng01@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp) | 1,909,104 | Tesla V100 (32GB) | Sep 8, 2020 |
|  2  |  **DeeperGCN+FLAG**  | 0.8596 ± 0.0027   | 0.9132 ± 0.0022 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 2,374,568 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  3  |  **DeeperGCN**  | 0.8580 ± 0.0017   | 0.9106 ± 0.0016 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 2,374,568 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  4  |  **DeepGCN**  | 0.8496 ± 0.0028   | 0.8971 ± 0.0011 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](http://openaccess.thecvf.com/content_ICCV_2019/papers/Li_DeepGCNs_Can_GCNs_Go_As_Deep_As_CNNs_ICCV_2019_paper.pdf), [Code](https://github.com/lightaime/deep_gcns_torch/blob/master/examples/ogb/ogbn_proteins) | 2,374,456 | NVIDIA Tesla V100 (32GB GPU) | Jun 20, 2020 |
|  5  |  **MWE-DGCN**  | 0.8436 ± 0.0065   | 0.8973 ± 0.0057 |[Zhengdao Chen](mailto:zc1216@nyu.edu) | [Paper](https://cims.nyu.edu/~chenzh/files/GCN_with_edge_weights.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-proteins) | 538,544 | NVIDIA Tesla V100 (16GB GPU) | Jul 20, 2020 |
|  6  |  **GeniePath-BS**  | 0.7825 ± 0.0035   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Zhengwei WU (AGL Team)](mailto:zejun.wzw@alipay.com) | [Paper](http://arxiv.org/abs/2006.05806), [Code](https://github.com/xavierzw/ogb-geniepath-bs) | 316,754 | Intel Xeon E5-2682 v4 (512GB CPU) | Jun 10, 2020 |
|  7  |  GaAN  | 0.7803 ± 0.0073   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Wenjin Wang (PGL Team)](mailto:wangwenjin02@baidu.com) | [Paper](https://arxiv.org/abs/1803.07294), [Code](https://github.com/PaddlePaddle/PGL/tree/master/examples/GaAN) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 26, 2020 |
|  8  |  GraphSAGE  | 0.7768 ± 0.0020   | 0.8334 ± 0.0013 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 193,136 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  9  |  GCN  | 0.7251 ± 0.0035   | 0.7921 ± 0.0018 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 96,880 | GeForce RTX 2080 (11GB GPU) | Jul 17, 2020 |
|  10  |  MLP  | 0.7204 ± 0.0048   | 0.7706 ± 0.0014 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 96,880 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  11  |  Node2vec  | 0.6881 ± 0.0065   | 0.7007 ± 0.0053 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 17,094,000 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |


<a name="ogbn-arxiv"/>

---------

### Leaderboard for [ogbn-arxiv](../nodeprop/#ogbn-arxiv)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.1.1

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  GAT+norm. adj.+label reuse  | 0.7399 ± 0.0010   | 0.7518 ± 0.0004 | [Yangkun Wang (DGL Team)](mailto:espylapiza@gmail.com) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/Espylapiza/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,441,580 | p3.8xlarge (15GB GPU) | Oct 29, 2020 |
|  2  |  **GAT + C&S**  | 0.7386 ± 0.0014   | 0.7484 ± 0.0007 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 1,567,000 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  3  |  **UniMP_large**  | 0.7379 ± 0.0014   | 0.7475 ± 0.0008 |[Yunsheng Shi (PGL team)](mailto:shiyunsheng01@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp) | 1,162,515 | Tesla V100 (32GB) | Sep 25, 2020 |
|  4  |  **GAT+FLAG**  | 0.7371 ± 0.0013   | 0.7496 ± 0.0010 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 1,628,440 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  5  |  GAT+norm. adj.+labels  | 0.7366 ± 0.0011   | 0.7508 ± 0.0009 | [Yangkun Wang (DGL Team)](mailto:espylapiza@gmail.com) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/Espylapiza/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,441,580 | p3.8xlarge (15GB GPU) | Oct 29, 2020 |
|  6  |  GAT+norm.adj.+labels  | 0.7365 ± 0.0011   | 0.7504 ± 0.0006 | [Yangkun Wang (DGL Team)](mailto:wyangkun@amazon.com) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,628,440 | p3.8xlarge (15GB GPU) | Sep 17, 2020 |
|  7  |  **MLP + C&S**  | 0.7312 ± 0.0012   | 0.7391 ± 0.0015 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 175,656 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  8  |  **UniMP**  | 0.7311 ± 0.0020   | 0.7450 ± 0.0005 |[Yunsheng Shi (PGL team)](mailto:shiyunsheng01@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp) | 473,489 | Tesla V100 (32GB) | Sep 8, 2020 |
|  9  |  GCN+linear+labels  | 0.7306 ± 0.0024   | 0.7442 ± 0.0012 | [Yangkun Wang (DGL Team)](mailto:wyangkun@amazon.com) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 238,632 | g4dn.12xlarge, T4 (15GB GPU) | Sep 5, 2020 |
|  10  |  GCN+residual+6 layers  | 0.7286 ± 0.0016   | 0.7382 ± 0.0007 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/Chillee/ogb_baselines) | 122,542 | GeForce RTX 2080 (11GB GPU) | Oct 6, 2020 |
|  11  |  GCN+residual+node2vec  | 0.7278 ± 0.0013   | 0.7414 ± 0.0008 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/Chillee/ogb_baselines) | 21,885,098 | GeForce RTX 2080 (11GB GPU) | Oct 3, 2020 |
|  12  |  **GCNII**  | 0.7274 ± 0.0016   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Ming Chen](mailto:chennnming@outlook.com) | [Paper](https://arxiv.org/abs/2007.02133), [Code](https://github.com/chennnM/GCNII/tree/master/PyG/ogbn-arxiv) | 2,148,648 | Quadro RTX 8000 (48GB GPU) | Jul 7, 2020 |
|  13  |  **Linear + C&S**  | 0.7222 ± 0.0002   | 0.7368 ± 0.0004 |[Horace He](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 15,400 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  14  |  JKNet (GCN-based)  | 0.7219 ± 0.0021   | 0.7335 ± 0.0007 | [Weiran Huang](mailto:huangweiran1998@outlook.com) | [Paper](https://arxiv.org/pdf/1806.03536.pdf), [Code](https://github.com/EtoDemerzel0427/ogbn-arxiv-baselines/blob/master/JKNet.py) | 89,000 | Tesla T4 | Aug 26, 2020 |
|  14  |  **GraphSAGE+FLAG**  | 0.7219 ± 0.0021   | 0.7349 ± 0.0009 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 218,664 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  15  |  **DeeperGCN+FLAG**  | 0.7214 ± 0.0019   | 0.7311 ± 0.0009 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 491,176 | NVIDIA Tesla V100 (32GB GPU) | Oct 20, 2020 |
|  16  |  **DAGNN**  | 0.7209 ± 0.0025   | 0.7290 ± 0.0011 |[Meng Liu - DIVE@TAMU](mailto:mengliu@tamu.edu) | [Paper](https://arxiv.org/abs/2007.09296), [Code](https://github.com/mengliu1998/DeeperGNN) | 43,857 | GeForce RTX 2080 Ti (11GB GPU) | Aug 19, 2020 |
|  17  |  **GCN+FLAG**  | 0.7204 ± 0.0020   | 0.7330 ± 0.0010 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 142,888 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  18  |  GaAN  | 0.7197 ± 0.0024   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hui Zhong (PGL Team)](mailto:zhonghui03@baidu.com) | [Paper](https://arxiv.org/abs/1803.07294), [Code](https://github.com/PaddlePaddle/PGL/tree/master/ogb_examples/nodeproppred/ogbn-arxiv) | 1,471,506 | NVIDIA Tesla V100 (16GB GPU) | Jun 16, 2020 |
|  19  |  **DeeperGCN**  | 0.7192 ± 0.0016   | 0.7262 ± 0.0014 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 491,176 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  20  |  GCN  | 0.7174 ± 0.0029   | 0.7300 ± 0.0017 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 142,888 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  21  |  GraphSAGE  | 0.7149 ± 0.0027   | 0.7277 ± 0.0016 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 218,664 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  22  |  **Plain Linear + C&S**  | 0.7126 ± 0.0001   | 0.7300 ± 0.0001 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 5,160 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  23  |  **GraphZoom (Node2vec)**  | 0.7118 ± 0.0018   | 0.7220 ± 0.0007 |[Xiuyu Li - GraphZoom](mailto:xl289@cornell.edu) | [Paper](https://openreview.net/forum?id=r1lGO0EKDH), [Code](https://github.com/cornell-zhang/GraphZoom/tree/master/ogb/ogbn-arxiv) | 8,963,624 | GeForce GTX 1080 Ti (11GB GPU) | Jul 2, 2020 |
|  24  |  Node2vec  | 0.7007 ± 0.0013   | 0.7129 ± 0.0013 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 21,818,792 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  25  |  Label Propagation  | 0.6832 ± 0.0000   | 0.7014 ± 0.0000 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](http://pages.cs.wisc.edu/~jerryzhu/pub/ssl_survey.pdf), [Code](https://github.com/Chillee/CorrectAndSmoothOGB) | 0 | GeForce RTX 2080 (11GB GPU) | Oct 2, 2020 |
|  26  |  **MLP+FLAG**  | 0.5602 ± 0.0019   | 0.5817 ± 0.0011 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 110,120 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  27  |  MLP  | 0.5550 ± 0.0023   | 0.5765 ± 0.0012 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 110,120 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |



<a name="ogbn-papers100M"/>

---------

### Leaderboard for [ogbn-papers100M](../nodeprop/#ogbn-papers100M)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.2.0

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **SIGN-XL**  | 66.0600 ± 0.1900   | 69.8400 ± 0.0600 |[Fabrizio Frasca](mailto:ffrasca@twitter.com) | [Paper](https://arxiv.org/abs/2004.11198), [Code](https://github.com/twitter-research/sign) | 7,180,460 | NVIDIA K80 GPU (12GB GPU) | Nov 4, 2020 |
|  2  |  **SIGN**  | 65.6800 ± 0.0600   | 69.3200 ± 0.0600 |[Emanuele Rossi](mailto:emanuele.rossi1909@gmail.com) | [Paper](https://arxiv.org/abs/2004.11198), [Code](https://github.com/twitter-research/sign) | 1,008,812 | NVIDIA K80 GPU (12GB GPU) | Nov 4, 2020 |
|  3  |  SGC  | 0.6329 ± 0.0019   | 0.6648 ± 0.0020 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.07153), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 144,044 | Xeon E7-8890x (1.5TB CPU) | Jun 10, 2020 |
|  4  |  Node2vec  | 0.5560 ± 0.0023   | 0.5807 ± 0.0028 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 14,215,818,412 | Xeon E7-8890x (1.5TB CPU) | Jun 26, 2020 |
|  5  |  MLP  | 0.4724 ± 0.0031   | 0.4960 ± 0.0029 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 144,044 | Xeon E7-8890x (1.5TB CPU) | Jun 10, 2020 |




<a name="ogbn-mag"/>

---------

### Leaderboard for [ogbn-mag](../nodeprop/#ogbn-mag)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **HGT (LADIES Sample)**  | 0.5007 ± 0.0043   | 0.5124 ± 0.0039 |[Ziniu Hu](mailto:bull@cs.ucla.edu) | [Paper](https://arxiv.org/abs/2003.01332), [Code](https://github.com/acbull/pyHGT/tree/master/ogbn-mag) | 21,173,389 | Tesla K80 (12GB GPU) | Jul 7, 2020 |
|  2  |  GraphSAINT (R-GCN aggr)  | 0.4751 ± 0.0022   | 0.4837 ± 0.0026 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  3  |  **R-GCN+FLAG**  | 0.4737 ± 0.0048   | 0.4835 ± 0.0036 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 154,366,772 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  4  |  NeighborSampling (R-GCN aggr)  | 0.4678 ± 0.0067   | 0.4761 ± 0.0068 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  5  |  Full-batch R-GCN  | 0.3977 ± 0.0046   | 0.4084 ± 0.0041 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1703.06103), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | Quadro RTX 8000 (48GB GPU) | Jun 26, 2020 |
|  6  |  ClusterGCN (R-GCN aggr)  | 0.3732 ± 0.0037   | 0.3840 ± 0.0031 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  7  |  MetaPath2vec  | 0.3544 ± 0.0036   | 0.3506 ± 0.0017 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://ericdongyx.github.io/papers/KDD17-dong-chawla-swami-metapath2vec.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 94,479,069 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  8  |  MLP  | 0.2692 ± 0.0026   | 0.2626 ± 0.0016 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 188,509 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |





