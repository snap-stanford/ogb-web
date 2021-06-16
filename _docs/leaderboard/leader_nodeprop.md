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
|  1  |  **SAGN+SLE**  | 0.8428 ± 0.0014   | 0.9287 ± 0.0003 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2104.09376), [Code](https://github.com/skepsun/SAGN_with_SLE) | 2,179,678 | Tesla V100 (16GB GPU) | Apr 19, 2021 |
|  2  |  **MLP + C&S**  | 0.8418 ± 0.0007   | 0.9147 ± 0.0009 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 96,247 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  3  |  **Linear + C&S**  | 0.8301 ± 0.0001   | 0.9134 ± 0.0001 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 10,763 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  4  |  **UniMP**  | 0.8256 ± 0.0031   | 0.9308 ± 0.0017 |[Yunsheng Shi (PGL team)](mailto:shiyunsheng01@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp) | 1,475,605 | Tesla V100 (32GB) | Sep 8, 2020 |
|  5  |  **Plain Linear + C&S**  | 0.8254 ± 0.0003   | 0.9103 ± 0.0001 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 4,747 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  6  |  **DeeperGCN+FLAG**  | 0.8193 ± 0.0031   | 0.9221 ± 0.0037 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 253,743 | NVIDIA Tesla V100 (32GB GPU) | Oct 20, 2020 |
|  7  |  **GAT+FLAG**  | 0.8176 ± 0.0045   | 0.9251 ± 0.0006 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 751,574 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  8  |  GraphSAGE + C&S + node2vec  | 0.8154 ± 0.0050   | 0.9238 ± 0.0006 | [HuiXuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/ytchx1999/PyG-ogbn-products/tree/main/sage%2Bnode2vec) | 103,983 | Tesla V100 (32GB) | Apr 6, 2021 |
|  9  |  **SAGN**  | 0.8120 ± 0.0007   | 0.9309 ± 0.0004 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2104.09376), [Code](https://github.com/skepsun/SAGN_with_SLE) | 2,233,391 | Tesla V100 (16GB GPU) | Apr 19, 2021 |
|  10  |  **DeeperGCN**  | 0.8098 ± 0.0020   | 0.9238 ± 0.0009 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 253,743 | NVIDIA Tesla V100 (32GB GPU) | Jun 28, 2020 |
|  11  |  GAT w/NS + C&S  | 0.8092 ± 0.0037   | 0.9263 ± 0.0008 | [HuiXuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/ytchx1999/PyG-ogbn-products/tree/main/gat) | 753,622 | Tesla V100 (32GB) | Apr 4, 2021 |
|  12  |  SIGN  | 0.8052 ± 0.0016   | 0.9299 ± 0.0004 | [Lingfan Yu (DGL Team)](mailto:lingfan.yu@nyu.edu) | [Paper](https://arxiv.org/abs/2004.11198), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/sign) | 3,483,703 | Tesla T4 (15 GB GPU) | Nov 5, 2020 |
|  13  |  GraphSAGE w/NS + C&S  | 0.8041 ± 0.0022   | 0.9238 ± 0.0007 | [HuiXuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/ytchx1999/PyG-ogbn-products/tree/main/sage) | 207,919 | Tesla V100 (32GB) | Apr 5, 2021 |
|  14  |  **GraphSAINT-inductive**  | 0.8027 ± 0.0026   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Hanqing Zeng](mailto:zengh@usc.edu) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/GraphSAINT/GraphSAINT/tree/master/graphsaint/open_graph_benchmark) | 331,661 | Tesla P100 (16GB GPU) | Jul 13, 2020 |
|  15  |  ClusterGCN+residual+3 layers  | 0.7971 ± 0.0042   | 0.9188 ± 0.0008 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/Chillee/ogb_baselines) | 456,034 | GeForce RTX 2080 (11GB GPU) | Oct 6, 2020 |
|  16  |  GAT with NeighborSampling  | 0.7945 ± 0.0059   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/rusty1s/pytorch_geometric/blob/master/examples/ogbn_products_gat.py) | 751,574 | GeForce RTX 2080 (11GB GPU) | May 24, 2020 |
|  17  |  **GraphSAGE+FLAG**  | 0.7936 ± 0.0057   | 0.9205 ± 0.0007 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 206,895 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  18  |  Cluster-GAT  | 0.7923 ± 0.0078   | 0.8985 ± 0.0022 | [Xiang Song](mailto:classicxsong@gmail.com) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/cluster-gat) | 1,540,848 | EC2 P3.2xlarge (V100) | Aug 2, 2020 |
|  19  |  GraphSAINT (SAGE aggr)  | 0.7908 ± 0.0024   | 0.9162 ± 0.0008 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  20  |  ClusterGCN (SAGE aggr)  | 0.7897 ± 0.0033   | 0.9212 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  21  |  NeighborSampling (SAGE aggr)  | 0.7870 ± 0.0036   | 0.9170 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  22  |  Full-batch GraphSAGE  | 0.7850 ± 0.0014   | 0.9224 ± 0.0007 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 206,895 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  23  |  GraphSAGE  | 0.7829 ± 0.0016   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Quan Gan (DGL Team)](mailto:quagan@amazon.com) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-products/graphsage) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 12, 2020 |
|  24  |  Full-batch GCN  | 0.7564 ± 0.0021   | 0.9200 ± 0.0003 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 103,727 | Quadro RTX 8000 (48GB GPU) | Jun 20, 2020 |
|  25  |  Label Propagation  | 0.7434 ± 0.0000   | 0.9091 ± 0.0000 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](http://pages.cs.wisc.edu/~jerryzhu/pub/thesis.pdf), [Code](https://github.com/Chillee/CorrectAndSmoothOGB) | 0 | GeForce RTX 2080 (11GB GPU) | Oct 3, 2020 |
|  26  |  **GraphZoom (Node2vec)**  | 0.7406 ± 0.0026   | 0.9066 ± 0.0011 |[Xiuyu Li - GraphZoom](mailto:xl289@cornell.edu) | [Paper](https://openreview.net/forum?id=r1lGO0EKDH), [Code](https://github.com/cornell-zhang/GraphZoom/tree/master/ogb/ogbn-products) | 120,251,183 | NVIDIA TITAN RTX (24GB GPU) | Oct 6, 2020 |
|  27  |  Node2vec  | 0.7249 ± 0.0010   | 0.9032 ± 0.0006 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 313,612,207 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  28  |  **MLP+FLAG**  | 0.6241 ± 0.0016   | 0.7688 ± 0.0014 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 103,727 | GeForce RTX 2080 Ti (11GB GPU) | Nov 17, 2020 |
|  29  |  MLP  | 0.6106 ± 0.0008   | 0.7554 ± 0.0014 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/products) | 103,727 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |


<a name="ogbn-proteins"/>

------

### Leaderboard for [ogbn-proteins](../nodeprop/#ogbn-proteins)
##### The ROC-AUC score on the test and validation sets. The higher, the better.

#### Package: >=1.1.1

| Rank  | Method | Test ROC-AUC | Validation ROC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GAT+BoT**  | 0.8765 ± 0.0008   | 0.9280 ± 0.0008 |[Yangkun Wang (DGL Team)](mailto:espylapiza@gmail.com) | [Paper](https://arxiv.org/abs/2103.13355), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-proteins) | 2,484,192 | Tesla A100 (40GB GPU) | Jun 16, 2021 |
|  2  |  GAT + labels + node2vec  | 0.8711 ± 0.0007   | 0.9217 ± 0.0011 | [Huixuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/ytchx1999/PyG-OGB-Tricks/tree/main/DGL-ogbn-proteins) | 6,360,470 | Tesla V100 (32GB) | Jun 7, 2021 |
|  3  |  **GIPA**  | 0.8700 ± 0.0010   | 0.9187 ± 0.0003 |[Qinkai Zheng (GeaLearn Team)](mailto:qinkai.zheng1028@gmail.com) | [Paper](https://arxiv.org/abs/2105.06035), [Code](https://github.com/yongchao-liu/gipa) | 4,831,056 | GeForce Titan RTX (24GB GPU) | May 13, 2021 |
|  4  |  **UniMP+CrossEdgeFeat**  | 0.8691 ± 0.0018   | 0.9258 ± 0.0009 |[Yelrose (PGL Team)](mailto:huangzhengjie@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/ogbn-proteins/unimp_cross_feat) | 1,959,984 | Tesla V100 (32GB) | Nov 24, 2020 |
|  5  |  GAT+EdgeFeatureAtt  | 0.8682 ± 0.0021   | 0.9194 ± 0.0003 | [Yangkun Wang (DGL Team)](mailto:espylapiza@gmail.com) | [Paper](https://arxiv.org/abs/2103.13355), [Code](https://github.com/Espylapiza/dgl/tree/master/examples/pytorch/ogb/ogbn-proteins) | 2,475,232 | p3.8xlarge (15GB GPU) | Nov 6, 2020 |
|  6  |  **UniMP**  | 0.8642 ± 0.0008   | 0.9175 ± 0.0006 |[Yunsheng Shi (PGL team)](mailto:shiyunsheng01@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp) | 1,909,104 | Tesla V100 (32GB) | Sep 8, 2020 |
|  7  |  **DeeperGCN+FLAG**  | 0.8596 ± 0.0027   | 0.9132 ± 0.0022 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 2,374,568 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  8  |  **DeeperGCN**  | 0.8580 ± 0.0017   | 0.9106 ± 0.0016 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 2,374,568 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  9  |  **DeepGCN**  | 0.8496 ± 0.0028   | 0.8971 ± 0.0011 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](http://openaccess.thecvf.com/content_ICCV_2019/papers/Li_DeepGCNs_Can_GCNs_Go_As_Deep_As_CNNs_ICCV_2019_paper.pdf), [Code](https://github.com/lightaime/deep_gcns_torch/blob/master/examples/ogb/ogbn_proteins) | 2,374,456 | NVIDIA Tesla V100 (32GB GPU) | Jun 20, 2020 |
|  10  |  **MWE-DGCN**  | 0.8436 ± 0.0065   | 0.8973 ± 0.0057 |[Zhengdao Chen](mailto:zc1216@nyu.edu) | [Paper](https://cims.nyu.edu/~chenzh/files/GCN_with_edge_weights.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-proteins) | 538,544 | NVIDIA Tesla V100 (16GB GPU) | Jul 20, 2020 |
|  11  |  GEN + FLAG + node2vec  | 0.8251 ± 0.0043   | 0.8656 ± 0.0037 | [HuiXuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/ytchx1999/PyG-ogbn-proteins/tree/main/gen%2Bflag) | 487,436 | Tesla V100 (32GB) | Apr 15, 2021 |
|  12  |  **GeniePath-BS**  | 0.7825 ± 0.0035   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Zhengwei WU (AGL Team)](mailto:zejun.wzw@alipay.com) | [Paper](http://arxiv.org/abs/2006.05806), [Code](https://github.com/xavierzw/ogb-geniepath-bs) | 316,754 | Intel Xeon E5-2682 v4 (512GB CPU) | Jun 10, 2020 |
|  13  |  GaAN  | 0.7803 ± 0.0073   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Wenjin Wang (PGL Team)](mailto:wangwenjin02@baidu.com) | [Paper](https://arxiv.org/abs/1803.07294), [Code](https://github.com/PaddlePaddle/PGL/tree/master/examples/GaAN) | [Please tell us](mailto:ogb@cs.stanford.edu) | [Please tell us](mailto:ogb@cs.stanford.edu) | May 26, 2020 |
|  14  |  GraphSAGE  | 0.7768 ± 0.0020   | 0.8334 ± 0.0013 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 193,136 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  15  |  GCN  | 0.7251 ± 0.0035   | 0.7921 ± 0.0018 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 96,880 | GeForce RTX 2080 (11GB GPU) | Jul 17, 2020 |
|  16  |  MLP  | 0.7204 ± 0.0048   | 0.7706 ± 0.0014 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 96,880 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  17  |  Node2vec  | 0.6881 ± 0.0065   | 0.7007 ± 0.0053 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/proteins) | 17,094,000 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |


<a name="ogbn-arxiv"/>

---------

### Leaderboard for [ogbn-arxiv](../nodeprop/#ogbn-arxiv)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.1.1

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  GAT+label reuse+self KD  | 0.7416 ± 0.0008   | 0.7514 ± 0.0004 | [Shunli Ren(CMIC@SJTU)](mailto:shunli_ren@163.com) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/ShunliRen/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,441,580 |  GeForce RTX 1080Ti (11GB GPU) | Dec 15, 2020 |
|  2  |  GAT+label+reuse+topo loss  | 0.7399 ± 0.0012   | 0.7513 ± 0.0009 | [Mengyang Niu (DAMO DI)](mailto:mengyang.nmy@alibaba-inc.com) | [Paper](https://arxiv.org/abs/1710.10903), [Code](https://github.com/mengyangniu/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,441,580 | Tesla V100 (16GB) | Dec 10, 2020 |
|  3  |  **AGDN (GAT-HA+3_heads+labels)**  | 0.7398 ± 0.0009   | 0.7519 ± 0.0009 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2012.15024), [Code](https://github.com/skepsun/adaptive_graph_diffusion_networks_with_hop-wise_attention) | 1,508,555 | Tesla V100 (32GB GPU) | Jan 3, 2021 |
|  4  |  **UniMP_v2**  | 0.7397 ± 0.0015   | 0.7506 ± 0.0009 |[Weiyue Su (PGL Team)](mailto:suweiyue@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/ogbn-arxiv/unimp_appnp_vnode_smooth) | 687,377 | Tesla V100 (32GB) | Nov 24, 2020 |
|  5  |  GAT(norm.adj.)+label reuse+C&S  | 0.7395 ± 0.0012   | 0.7519 ± 0.0008 | [Yangkun Wang (DGL Team)](mailto:espylapiza@gmail.com) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Espylapiza/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,441,580 | p3.8xlarge (15GB GPU)	 | Nov 24, 2020 |
|  6  |  GAT+norm. adj.+label reuse  | 0.7391 ± 0.0012   | 0.7516 ± 0.0008 | [Yangkun Wang (DGL Team)](mailto:espylapiza@gmail.com) | [Paper](https://arxiv.org/abs/2103.13355), [Code](https://github.com/Espylapiza/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,441,580 | p3.8xlarge (15GB GPU) | Nov 11, 2020 |
|  7  |  **GAT + C&S**  | 0.7386 ± 0.0014   | 0.7484 ± 0.0007 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 1,567,000 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  8  |  **UniMP_large**  | 0.7379 ± 0.0014   | 0.7475 ± 0.0008 |[Yunsheng Shi (PGL team)](mailto:shiyunsheng01@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp) | 1,162,515 | Tesla V100 (32GB) | Sep 25, 2020 |
|  9  |  **AGDN (GAT-HA+3_heads)**  | 0.7375 ± 0.0021   | 0.7483 ± 0.0009 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2012.15024), [Code](https://github.com/skepsun/adaptive_graph_diffusion_networks_with_hop-wise_attention) | 1,447,115 | Tesla V100 (32GB GPU) | Jan 3, 2021 |
|  10  |  **GAT+FLAG**  | 0.7371 ± 0.0013   | 0.7496 ± 0.0010 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 1,628,440 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  11  |  GAT+norm. adj.+labels  | 0.7366 ± 0.0011   | 0.7508 ± 0.0009 | [Yangkun Wang (DGL Team)](mailto:espylapiza@gmail.com) | [Paper](https://arxiv.org/abs/2103.13355), [Code](https://github.com/Espylapiza/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,441,580 | p3.8xlarge (15GB GPU) | Oct 29, 2020 |
|  12  |  GAT+norm.adj.+labels  | 0.7365 ± 0.0011   | 0.7504 ± 0.0006 | [Yangkun Wang (DGL Team)](mailto:wyangkun@amazon.com) | [Paper](https://arxiv.org/abs/2103.13355), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 1,628,440 | p3.8xlarge (15GB GPU) | Sep 17, 2020 |
|  13  |  GCN_res + C&S_v2  | 0.7313 ± 0.0017   | 0.7445 ± 0.0011 | [HuiXuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/ytchx1999/GCN_res-CS-v2) | 155,824 | Tesla V100 (32GB) | Mar 26, 2021 |
|  14  |  **MLP + C&S**  | 0.7312 ± 0.0012   | 0.7391 ± 0.0015 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 175,656 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  15  |  **UniMP**  | 0.7311 ± 0.0020   | 0.7450 ± 0.0005 |[Yunsheng Shi (PGL team)](mailto:shiyunsheng01@baidu.com) | [Paper](https://arxiv.org/pdf/2009.03509.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/ogb_examples/nodeproppred/unimp) | 473,489 | Tesla V100 (32GB) | Sep 8, 2020 |
|  16  |  GCN+linear+labels  | 0.7306 ± 0.0024   | 0.7442 ± 0.0012 | [Yangkun Wang (DGL Team)](mailto:wyangkun@amazon.com) | [Paper](https://arxiv.org/abs/2103.13355), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ogbn-arxiv) | 238,632 | g4dn.12xlarge, T4 (15GB GPU) | Sep 5, 2020 |
|  17  |  GCN_res + C&S  | 0.7297 ± 0.0022   | 0.7423 ± 0.0014 | [HuiXuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/ytchx1999/PyG-GCN_res-CS) | 155,824 | Tesla T4（16GB） | Mar 24, 2021 |
|  18  |  GCN+residual+6 layers  | 0.7286 ± 0.0016   | 0.7382 ± 0.0007 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/Chillee/ogb_baselines) | 122,542 | GeForce RTX 2080 (11GB GPU) | Oct 6, 2020 |
|  19  |  GCN+residual+node2vec  | 0.7278 ± 0.0013   | 0.7414 ± 0.0008 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/Chillee/ogb_baselines) | 21,885,098 | GeForce RTX 2080 (11GB GPU) | Oct 3, 2020 |
|  20  |  GCN_res + 8 layers + FLAG  | 0.7276 ± 0.0024   | 0.7389 ± 0.0012 | [Huixuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/ytchx1999/GCN_res-FLAG) | 155,824 | Tesla T4（16GB） | Feb 23, 2021 |
|  21  |  **GCNII**  | 0.7274 ± 0.0016   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Ming Chen](mailto:chennnming@outlook.com) | [Paper](https://arxiv.org/abs/2007.02133), [Code](https://github.com/chennnM/GCNII/tree/master/PyG/ogbn-arxiv) | 2,148,648 | Quadro RTX 8000 (48GB GPU) | Jul 7, 2020 |
|  22  |  GCN_res + 8 layers  | 0.7262 ± 0.0037   | 0.7369 ± 0.0021 | [Huixuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/ytchx1999/ogbn_arxiv_GCN_res) | 155,824 | Tesla T4（16GB） | Feb 20, 2021 |
|  23  |  **Linear + C&S**  | 0.7222 ± 0.0002   | 0.7368 ± 0.0004 |[Horace He](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 15,400 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  24  |  **EGC-S (100k)**  | 0.7219 ± 0.0016   | 0.7338 ± 0.0022 |[Shyam Tailor](mailto:sat62@cam.ac.uk) | [Paper](https://arxiv.org/abs/2104.01481), [Code](https://github.com/shyam196/egc) | 100,648 | GTX1080Ti/RTX2080Ti | Apr 6, 2021 |
|  24  |  JKNet (GCN-based)  | 0.7219 ± 0.0021   | 0.7335 ± 0.0007 | [Weiran Huang](mailto:huangweiran1998@outlook.com) | [Paper](https://arxiv.org/pdf/1806.03536.pdf), [Code](https://github.com/EtoDemerzel0427/ogbn-arxiv-baselines/blob/master/JKNet.py) | 89,000 | Tesla T4 | Aug 26, 2020 |
|  24  |  **GraphSAGE+FLAG**  | 0.7219 ± 0.0021   | 0.7349 ± 0.0009 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 218,664 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  25  |  **DeeperGCN+FLAG**  | 0.7214 ± 0.0019   | 0.7311 ± 0.0009 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 491,176 | NVIDIA Tesla V100 (32GB GPU) | Oct 20, 2020 |
|  26  |  **DAGNN**  | 0.7209 ± 0.0025   | 0.7290 ± 0.0011 |[Meng Liu - DIVE@TAMU](mailto:mengliu@tamu.edu) | [Paper](https://arxiv.org/abs/2007.09296), [Code](https://github.com/mengliu1998/DeeperGNN) | 43,857 | GeForce RTX 2080 Ti (11GB GPU) | Aug 19, 2020 |
|  27  |  **GCN+FLAG**  | 0.7204 ± 0.0020   | 0.7330 ± 0.0010 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 142,888 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  28  |  GaAN  | 0.7197 ± 0.0024   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hui Zhong (PGL Team)](mailto:zhonghui03@baidu.com) | [Paper](https://arxiv.org/abs/1803.07294), [Code](https://github.com/PaddlePaddle/PGL/tree/master/ogb_examples/nodeproppred/ogbn-arxiv) | 1,471,506 | NVIDIA Tesla V100 (16GB GPU) | Jun 16, 2020 |
|  29  |  **EGC-M (100k)**  | 0.7196 ± 0.0023   | 0.7334 ± 0.0013 |[Shyam Tailor](mailto:sat62@cam.ac.uk) | [Paper](https://arxiv.org/abs/2104.01481), [Code](https://github.com/shyam196/egc) | 99,464 | GTX1080Ti/RTX2080Ti | Apr 6, 2021 |
|  30  |  SIGN  | 0.7195 ± 0.0011   | 0.7323 ± 0.0006 | [Lingfan Yu (DGL Team)](mailto:lingfan.yu@nyu.edu) | [Paper](https://arxiv.org/abs/2004.11198), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/sign) | 3,566,128 | Tesla T4 (15GB) | Nov 5, 2020 |
|  31  |  **DeeperGCN**  | 0.7192 ± 0.0016   | 0.7262 ± 0.0014 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 491,176 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  32  |  GCN  | 0.7174 ± 0.0029   | 0.7300 ± 0.0017 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 142,888 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  33  |  GraphSAGE  | 0.7149 ± 0.0027   | 0.7277 ± 0.0016 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 218,664 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  34  |  **Plain Linear + C&S**  | 0.7126 ± 0.0001   | 0.7300 ± 0.0001 |[Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/2010.13993), [Code](https://github.com/Chillee/CorrectAndSmooth) | 5,160 | GeForce RTX 2080 (11GB GPU) | Oct 27, 2020 |
|  35  |  **GraphZoom (Node2vec)**  | 0.7118 ± 0.0018   | 0.7220 ± 0.0007 |[Xiuyu Li - GraphZoom](mailto:xl289@cornell.edu) | [Paper](https://openreview.net/forum?id=r1lGO0EKDH), [Code](https://github.com/cornell-zhang/GraphZoom/tree/master/ogb/ogbn-arxiv) | 8,963,624 | GeForce GTX 1080 Ti (11GB GPU) | Jul 2, 2020 |
|  36  |  Node2vec  | 0.7007 ± 0.0013   | 0.7129 ± 0.0013 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 21,818,792 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  37  |  Label Propagation  | 0.6832 ± 0.0000   | 0.7014 ± 0.0000 | [Horace He (Cornell)](mailto:hh498@cornell.edu) | [Paper](http://pages.cs.wisc.edu/~jerryzhu/pub/ssl_survey.pdf), [Code](https://github.com/Chillee/CorrectAndSmoothOGB) | 0 | GeForce RTX 2080 (11GB GPU) | Oct 2, 2020 |
|  38  |  **MLP+FLAG**  | 0.5602 ± 0.0019   | 0.5817 ± 0.0011 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 110,120 | GeForce RTX 2080 Ti (11GB GPU) | Oct 20, 2020 |
|  39  |  MLP  | 0.5550 ± 0.0023   | 0.5765 ± 0.0012 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/arxiv) | 110,120 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |



<a name="ogbn-papers100M"/>

---------

### Leaderboard for [ogbn-papers100M](../nodeprop/#ogbn-papers100M)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.2.0

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **SAGN+SLE**  | 0.6800 ± 0.0015   | 0.7131 ± 0.0010 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2104.09376), [Code](https://github.com/skepsun/SAGN_with_SLE) | 8,556,888 | Tesla V100 (16GB GPU) | Apr 19, 2021 |
|  2  |  TransformerConv  | 0.6736 ± 0.0010   | 0.7172 ± 0.0005 | [Xiaonan Song (NVIDIA SAE China team)](mailto:xiaonans@nvidia.com) | [Paper](https://arxiv.org/abs/2009.03509), [Code](https://github.com/nvidia-china-sae/WholeGraph) | 883,378 | NVIDIA DGX-2 (16*32GB GPUs) | Mar 4, 2021 |
|  3  |  GraphSAGE_res_incep  | 0.6706 ± 0.0017   | 0.7032 ± 0.0011 | [Mengyang Niu (DAMO DI)](mailto:mengyang.nmy@alibaba-inc.com) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/mengyangniu/ogbn-papers100m-sage) | 5,755,172 | Tesla V100 (16GB) | Feb 28, 2021 |
|  4  |  **SAGN**  | 0.6675 ± 0.0084   | 0.7034 ± 0.0099 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2104.09376), [Code](https://github.com/skepsun/SAGN_with_SLE) | 6,098,092 | Tesla V100 (16GB GPU) | Apr 19, 2021 |
|  5  |  **SIGN-XL**  | 0.6606 ± 0.0019   | 0.6984 ± 0.0006 |[Fabrizio Frasca](mailto:ffrasca@twitter.com) | [Paper](https://arxiv.org/abs/2004.11198), [Code](https://github.com/twitter-research/sign) | 7,180,460 | NVIDIA K80 GPU (12GB GPU) | Nov 4, 2020 |
|  6  |  **SIGN**  | 0.6568 ± 0.0006   | 0.6932 ± 0.0006 |[Emanuele Rossi](mailto:emanuele.rossi1909@gmail.com) | [Paper](https://arxiv.org/abs/2004.11198), [Code](https://github.com/twitter-research/sign) | 1,008,812 | NVIDIA K80 GPU (12GB GPU) | Nov 4, 2020 |
|  7  |  SGC  | 0.6329 ± 0.0019   | 0.6648 ± 0.0020 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.07153), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 144,044 | Xeon E7-8890x (1.5TB CPU) | Jun 10, 2020 |
|  8  |  Node2vec  | 0.5560 ± 0.0023   | 0.5807 ± 0.0028 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 14,215,818,412 | Xeon E7-8890x (1.5TB CPU) | Jun 26, 2020 |
|  9  |  MLP  | 0.4724 ± 0.0031   | 0.4960 ± 0.0029 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/papers100M) | 144,044 | Xeon E7-8890x (1.5TB CPU) | Jun 10, 2020 |




<a name="ogbn-mag"/>

---------

### Leaderboard for [ogbn-mag](../nodeprop/#ogbn-mag)
##### The classification accuracy on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **NARS**  | 0.5240 ± 0.0016   | 0.5372 ± 0.0009 |[Lingfan Yu](mailto:ly979@nyu.edu) | [Paper](https://arxiv.org/pdf/2011.09679.pdf), [Code](https://github.com/facebookresearch/NARS) | 4,130,149 | Tesla T4 (15GB) | Feb 18, 2021 |
|  2  |  **R-HGNN**  | 0.5204 ± 0.0026   | 0.5361 ± 0.0022 |[Le Yu](mailto:yule@buaa.edu.cn) | [Paper](https://arxiv.org/abs/2105.11122), [Code](https://github.com/yule-BUAA/R-HGNN.git) | 5,638,053 | NVIDIA Tesla T4 (15 GB) | May 24, 2021 |
|  3  |  R-GSN + metapath2vec  | 0.5109 ± 0.0038   | 0.5295 ± 0.0042 | [Huixuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/2103.07877), [Code](https://github.com/ytchx1999/PyG-ogbn-mag/tree/main/rgsn%2Bmetapath2vec) | 309,777,252 | Tesla V100 (32GB) | May 23, 2021 |
|  4  |  **HGConv**  | 0.5045 ± 0.0017   | 0.5300 ± 0.0018 |[Le Yu](mailto:yule@buaa.edu.cn) | [Paper](https://arxiv.org/abs/2012.14722), [Code](https://github.com/yule-BUAA/HGConv.git) | 2,850,405 | NVIDIA TITAN Xp (12GB) | Feb 14, 2021 |
|  5  |  **R-GSN**  | 0.5032 ± 0.0037   | 0.5182 ± 0.0041 |[Xinliang Wu](mailto:912251635@qq.com) | [Paper](https://arxiv.org/pdf/1703.06103.pdf), [Code](https://github.com/xjtuwxliang/R-GSN/tree/main) | 154,373,028 | GeForce GTX 1080Ti | Jan 29, 2021 |
|  6  |  HGT (TransE embs)  | 0.4982 ± 0.0013   | 0.5124 ± 0.0046 | [Lingfan Yu](mailto:ly979@nyu.edu) | [Paper](https://arxiv.org/pdf/2003.01332.pdf), [Code](https://github.com/lingfanyu/pyHGT/tree/master/ogbn-mag) | 26,877,657 | Tesla T4 (15GB) | Feb 17, 2021 |
|  7  |  GraphSAINT + metapath2vec  | 0.4966 ± 0.0022   | 0.5066 ± 0.0017 | [HuiXuan Chi](mailto:1520655940@qq.com) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/ytchx1999/PyG-ogbn-mag/tree/main/saint%2Bmetapath2vec) | 309,764,724 | Tesla V100 (32GB) | Apr 9, 2021 |
|  8  |  **HGT (LADIES Sample)**  | 0.4927 ± 0.0061   | 0.4989 ± 0.0047 |[Ziniu Hu](mailto:bull@cs.ucla.edu) | [Paper](https://arxiv.org/abs/2003.01332), [Code](https://github.com/acbull/pyHGT/tree/master/ogbn-mag) | 21,173,389 | Tesla K80 (12GB GPU) | Jan 26, 2021 |
|  9  |  GraphSAINT (R-GCN aggr)  | 0.4751 ± 0.0022   | 0.4837 ± 0.0026 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  10  |  **R-GCN+FLAG**  | 0.4737 ± 0.0048   | 0.4835 ± 0.0036 |[Kezhi Kong](mailto:kong@cs.umd.edu) | [Paper](https://arxiv.org/abs/2010.09891), [Code](https://github.com/devnkong/FLAG) | 154,366,772 | GeForce RTX 2080 Ti (11GB GPU) | Oct 21, 2020 |
|  11  |  NeighborSampling (R-GCN aggr)  | 0.4678 ± 0.0067   | 0.4761 ± 0.0068 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  12  |  SIGN  | 0.4046 ± 0.0012   | 0.4068 ± 0.0010 | [Lingfan Yu (DGL Team)](mailto:lingfan.yu@nyu.edu) | [Paper](https://arxiv.org/abs/2004.11198), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/sign) | 3,724,645 | Tesla T4 (15GB GPU) | Nov 5, 2020 |
|  13  |  Full-batch R-GCN  | 0.3977 ± 0.0046   | 0.4084 ± 0.0041 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1703.06103), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | Quadro RTX 8000 (48GB GPU) | Jun 26, 2020 |
|  14  |  ClusterGCN (R-GCN aggr)  | 0.3732 ± 0.0037   | 0.3840 ± 0.0031 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 154,366,772 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  15  |  MetaPath2vec  | 0.3544 ± 0.0036   | 0.3506 ± 0.0017 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://ericdongyx.github.io/papers/KDD17-dong-chawla-swami-metapath2vec.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 94,479,069 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |
|  16  |  MLP  | 0.2692 ± 0.0026   | 0.2626 ± 0.0016 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/nodeproppred/mag) | 188,509 | GeForce RTX 2080 (11GB GPU) | Jun 26, 2020 |





