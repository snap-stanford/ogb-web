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
###### - [ogbl-vessel](#ogbl-vessel)

The **bold** method name indicates that the implementation is **official** (by the author of the original paper). <br/>
**Package** denotes the required package version for each dataset to be eligible for the leaderboard.


<a name="ogbl-ppa"/>

-------

### Leaderboard for [ogbl-ppa](../linkprop/#ogbl-ppa)
##### The Hits@100 score on the test and validation sets. The higher, the better.

#### Package: >=1.1.1

| Rank  | Method | Ext. data | Test Hits@100 | Validation Hits@100 | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GraphGPT(SMTP)**  | No | 0.7655 ± 0.0067   | 0.7712 ± 0.0065 |[Qifang Zhao(Alibaba)](mailto:james.zqf@alibaba-inc.com) | [Paper](https://arxiv.org/abs/2401.00529), [Code](https://github.com/alibaba/graph-gpt) | 2,032,859,200 | 32 Nvidia L40S | Oct 28, 2024 |
|  2  |  **Refined-GAE**  | No | 0.7374 ± 0.0092   | 0.7390 ± 0.0180 |[Weishuo Ma(Peking University)](mailto:2200013081@stu.pku.edu.cn) | [Paper](https://arxiv.org/abs/2411.03845), [Code](https://github.com/GraphPKU/Refined-GAE) | 295,848,449 | RTX 4090 (24GB) | Nov 23, 2024 |
|  3  |  **Refined-GAE**  | No | 0.7334 ± 0.0092   | 0.7391 ± 0.0178 |[Weishuo Ma(Peking University)](mailto:2200013081@stu.pku.edu.com) | [Paper](https://arxiv.org/html/2411.03845v1), [Code](https://github.com/GraphPKU/Refined-GAE) | 295,848,449 | RTX 4090 (24GB) | Nov 7, 2024 |
|  4  |  **GraphGPT(SMTP)**  | No | 0.6876 ± 0.0067   | 0.7017 ± 0.0044 |[Qifang Zhao(Alibaba)](mailto:james.zqf@alibaba-inc.com) | [Paper](https://arxiv.org/abs/2401.00529), [Code](https://github.com/alibaba/graph-gpt) | 145,263,360 | 8 Nvidia L40S | Oct 8, 2024 |
|  5  |  **MPLP**  | No | 0.6524 ± 0.0150   | 0.6685 ± 0.0073 |[Kaiwen Dong (University of Notre Dame)](mailto:kevindong1994@gmail.com) | [Paper](https://arxiv.org/pdf/2309.00976.pdf), [Code](https://github.com/Barcavin/efficient-node-labelling) | 147,794,531 | NVIDIA A100 GPU (80G RAM) | Jan 16, 2024 |
|  6  |  GCN (node embedding)  | No | 0.6354 ± 0.0121   | 0.6524 ± 0.0096 | [Shuming Liang (UTS)](mailto:shuming.liang@uts.edu.au) | [Paper](https://arxiv.org/abs/2411.14711), [Code](https://github.com/astroming/GNNHE) | 148,144,898 | NVIDIA A100 (40G) | Nov 24, 2024 |
|  7  |  **SIEG**  | No | 0.6322 ± 0.0174   | 0.6533 ± 0.0234 |[anonymous20221001](mailto:anonymous20221001@126.com) | [Paper](https://github.com/anonymous20221001/SIEG_OGB/blob/master/OGB_VESSEL_SIEG.pdf), [Code](https://github.com/anonymous20221001/SIEG_OGB) | 1,993,965 | P100 (16GB) | Mar 24, 2023 |
|  8  |  **Neural Common Neighbor **  | No | 0.6119 ± 0.0085   | 0.6021 ± 0.0037 |[Xiyuan Wang (Peking University)](mailto:wangxiyuan@pku.edu.cn) | [Paper](https://arxiv.org/abs/2302.00890), [Code](https://github.com/GraphPKU/NeuralCommonNeighbor) | 33,538 | RTX 4090 (24GB) | Mar 17, 2023 |
|  9  |  **NGNN + SEAL**  | No | 0.5971 ± 0.0245   | 0.5995 ± 0.0205 |[Yakun Song(DGL)](mailto:ereboas@sjtu.edu.cn) | [Paper](https://arxiv.org/abs/2111.11638), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ngnn_seal) | 735,426 | Tesla T4(16GB) | Sep 21, 2022 |
|  10  |  **SUREL+**  | No | 0.5432 ± 0.0044   | 0.5492 ± 0.0112 |[Haoteng Yin (Purdue University)](mailto:yinht@purdue.edu) | [Paper](https://arxiv.org/abs/2303.03379), [Code](https://github.com/Graph-COM/SUREL_Plus) | 52,802 | NVIDIA A100 (80G) | Feb 20, 2023 |
|  11  |  **RA+Edge Proposal Set**  | No | 0.5324 ± 0.0000   | 0.5142 ± 0.0000 |[Qian Huang (Stanford)](mailto:qhwang@stanford.edu) | [Paper](https://arxiv.org/abs/2106.15810), [Code](https://github.com/CUAI/Edge-Proposal-Sets) | 0 | GeForce RTX 2080 Ti (11GB GPU) | Oct 5, 2021 |
|  12  |  **MLP+CN&RA&AA**  | No | 0.5062 ± 0.0035   | 0.4906 ± 0.0029 |[Shitao Lu](mailto:lusto32768@gmail.com) | [Paper](https://github.com/lustoo/OGB_link_prediction/blob/main/Link%20prediction%20with%20structural%20information.pdf), [Code](https://github.com/lustoo/OGB_link_prediction) | 163,330 | Geforce GTX 1080 Ti (11GB) | Aug 9, 2021 |
|  13  |  **BUDDY**  | No | 0.4934 ± 0.0098   | 0.4931 ± 0.0025 |[Ben Chamberlain](mailto:benjamin.chamberlain@gmail.com) | [Paper](https://openreview.net/pdf?id=m1oqEOAozQU), [Code](https://github.com/melifluos/subgraph-sketching) | 644 | Tesla K80 (12GB GPU) | Aug 23, 2023 |
|  14  |  Resource Allocation  | No | 0.4933 ± 0.0000   | 0.4722 ± 0.0000 | [Shen Fan(Alibaba Group)](mailto:ofanshen@gmail.com) | [Paper](https://arxiv.org/pdf/0901.0553.pdf), [Code](https://github.com/fs302/EasyLink/blob/main/example/ogbl_ppa_ra.py) | 0 | Tesla-V100(32GB GPU) | Jul 5, 2021 |
|  15  |  **SEAL**  | No | 0.4880 ± 0.0316   | 0.5125 ± 0.0252 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 709,122 | GeForce RTX 2080S (8GB GPU) | Oct 14, 2020 |
|  16  |  **S3GRL (PoS Plus)**  | No | 0.4242 ± 0.0180   | 0.6512 ± 0.0109 |[Paul Louis (Ontario Tech University)](mailto:paul.louis@ontariotechu.net) | [Paper](https://arxiv.org/pdf/2301.12562.pdf), [Code](https://github.com/venomouscyanide/S3GRL_OGB) | 32,270,001 | GeForce GTX 1080 Ti (11 GB) | May 2, 2023 |
|  17  |  **AGDN**  | No | 0.4123 ± 0.0159   | 0.4332 ± 0.0092 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2012.15024), [Code](https://github.com/skepsun/Adaptive-Graph-Diffusion-Networks) | 36,904,259 | Tesla V100 (16GB GPU) | Sep 2, 2022 |
|  18  |  **NGNN + GraphSAGE**  | No | 0.4005 ± 0.0138   | 0.4058 ± 0.0123 |[Yakun Song(DGL)](mailto:ereboas@sjtu.edu.cn) | [Paper](https://arxiv.org/abs/2111.11638), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ngnn) | 556,033 | Tesla-V100(16GB GPU) | Aug 16, 2022 |
|  19  |  **NGNN + GCN**  | No | 0.3683 ± 0.0099   | 0.3834 ± 0.0082 |[Yakun Song(DGL)](mailto:ereboas@sjtu.edu.cn) | [Paper](https://arxiv.org/abs/2111.11638), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ngnn) | 410,113 | Tesla-V100(16GB GPU) | Aug 16, 2022 |
|  20  |  Adamic Adar  | No | 0.3245 ± 0.0000   | 0.3268 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.1370&rep=rep1&type=pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  21  |  Matrix Factorization  | No | 0.3229 ± 0.0094   | 0.3228 ± 0.0428 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 147,662,849 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  22  |  DeepWalk  | No | 0.2888 ± 0.0153   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 150,138,741 | g4dn.2xlarge, T4 (15GB GPU) | Jul 23, 2020 |
|  23  |  Common Neighbor  | No | 0.2765 ± 0.0000   | 0.2823 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  24  |  DeepWalk  | No | 0.2302 ± 0.0163   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 150,138,741 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  25  |  Node2vec  | No | 0.2226 ± 0.0083   | 0.2253 ± 0.0088 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 73,878,913 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  26  |  GCN  | No | 0.1867 ± 0.0132   | 0.1845 ± 0.0140 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 278,529 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  27  |  GraphSAGE  | No | 0.1655 ± 0.0240   | 0.1724 ± 0.0264 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 424,449 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |




<a name="ogbl-collab"/>

-------

### Leaderboard for [ogbl-collab](../linkprop/#ogbl-collab)
##### The Hits@50 score on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Ext. data | Test Hits@50 | Validation Hits@50 | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **HyperFusion**  | No | 0.7129 ± 0.0018   | 0.7385 ± 0.0099 |[Xinwei Zhang (Tsinghua University)](mailto:xinwei-z21@mails.tsinghua.edu.cn) | [Paper](https://github.com/zhangxwww/HyperFusion/blob/master/Multi_Model_Ensemble_on_Hypergraph.pdf), [Code](https://github.com/zhangxwww/HyperFusion) | 1,064,446,212 | RTX 3080 | Feb 24, 2024 |
|  2  |  **GIDN@YITU**  | No | 0.7096 ± 0.0055   | 0.9620 ± 0.0040 |[Zixiao Wang, Yu Zhang(ZhejiangLab, HUST)](mailto:zwang62@hust.edu.cn) | [Paper](https://arxiv.org/abs/2210.01301), [Code](https://github.com/WizcoxYu/ogbl) | 60,449,025 | DepGraph@SCTS/CGCL | Oct 10, 2022 |
|  3  |  **PLNLP + SIGN**  | No | 0.7087 ± 0.0033   | 1.0000 ± 0.0000 |[Liang Yao (Tencent)](mailto:dryao@tencent.com) | [Paper](https://github.com/yao8839836/ogb_report/blob/main/ogb_report.pdf), [Code](https://github.com/yao8839836/ogb_report) | 34,980,864 | Tesla-P40 (24G GPU) | Apr 7, 2022 |
|  4  |  **PLNLP (random walk aug.)**  | No | 0.7059 ± 0.0029   | 1.0000 ± 0.0000 |[Zhitao Wang (WeChat@Tencent)](mailto:wztzenk@gmail.com) | [Paper](https://arxiv.org/abs/2112.02936), [Code](https://github.com/zhitao-wang/PLNLP) | 34,980,864 | Tesla-P40 (24G GPU) | Dec 21, 2021 |
|  5  |  **HOP-REC**  | No | 0.7012 ± 0.0016   | 1.0000 ± 0.0000 |[Bo-Yu Lin (CFDA & CLIP Labs)](mailto:sofar106703046@gmail.com) | [Paper](https://dl.acm.org/doi/10.1145/3240323.3240381), [Code](https://github.com/brucenccu/OGB_collab_project) | 30,191,104 | CPU | Oct 21, 2021 |
|  6  |  PLNLP+ LRGA  | No | 0.6909 ± 0.0055   | 1.0000 ± 0.0000 | [Hao Xu](mailto:kingsleyhsu1@gmail.com) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/KingsleyHsu/OGB-LPP) | 35,200,656 | NVIDIA Tesla V100 (32GB GPU) | Jun 26, 2022 |
|  7  |  **PLNLP (val as input)**  | No | 0.6872 ± 0.0052   | 1.0000 ± 0.0000 |[Zhitao Wang (WeChat@Tencent)](mailto:wztzenk@gmail.com) | [Paper](https://arxiv.org/pdf/2112.02936.pdf), [Code](https://github.com/zhitao-wang/PLNLP) | 35,112,192 | Tesla-P40 (24G GPU) | Dec 7, 2021 |
|  8  |  **Refined-GAE**  | No | 0.6816 ± 0.0041   | 1.0000 ± 0.0000 |[Weishuo Ma(Peking University)](mailto:2200013081@stu.pku.edu.com) | [Paper](https://arxiv.org/abs/2411.03845), [Code](https://github.com/GraphPKU/Refined-GAE) | 13,816,833 | RTX 4090 (24GB) | Nov 7, 2024 |
|  8  |  **Refined-GAE**  | No | 0.6816 ± 0.0041   | 1.0000 ± 0.0000 |[Weishuo Ma(Peking University)](mailto:2200013081@stu.pku.edu.cn) | [Paper](https://arxiv.org/abs/2411.03845), [Code](https://github.com/GraphPKU/Refined-GAE) | 126,669,825 | RTX 4090 (24GB) | Nov 23, 2024 |
|  9  |  **TopoLink**  | No | 0.6792 ± 0.0074   | 0.6771 ± 0.0083 |[Lizhi Liu (China UnionPay)](mailto:liulizhi1996@gmail.com) | [Paper](https://drive.google.com/file/d/1eKFbYFDu3F97eiNyVscwEuxbjVp9fUyA/view?usp=drive_link), [Code](https://github.com/liulizhi1996/TopoLink) | 483,363,845 | RTX 4090 (24GB GPU) | Sep 9, 2024 |
|  10  |  **S3GRL (PoS Plus)**  | No | 0.6683 ± 0.0030   | 0.9861 ± 0.0006 |[Paul Louis (Ontario Tech University)](mailto:paul.louis@ontariotechu.net) | [Paper](https://arxiv.org/pdf/2301.12562.pdf), [Code](https://github.com/venomouscyanide/S3GRL_OGB) | 5,913,025 | GeForce GTX 1080 Ti (11 GB) | Apr 25, 2023 |
|  11  |  **ELPH**  | No | 0.6636 ± 0.5876   | 0.6631 ± 0.0021 |[Ben Chamberlain](mailto:benjamin.chamberlain@gmail.com) | [Paper](https://openreview.net/pdf?id=m1oqEOAozQU), [Code](https://github.com/melifluos/subgraph-sketching) | 3,284,065 | Tesla K80 (12GB GPU) | Jul 3, 2023 |
|  12  |  **BUDDY**  | No | 0.6572 ± 0.0053   | 0.6621 ± 0.0016 |[Ben Chamberlain](mailto:benjamin.chamberlain@gmail.com) | [Paper](https://openreview.net/pdf?id=m1oqEOAozQU), [Code](https://github.com/melifluos/subgraph-sketching) | 1,184,867 | Tesla K80 (12GB GPU) | Jul 2, 2023 |
|  13  |  **Adamic Adar+Edge Proposal Set**  | No | 0.6548 ± 0.0000   | 0.9735 ± 0.0000 |[Qian Huang (Cornell University)](mailto:qh53@cornell.edu) | [Paper](https://arxiv.org/pdf/2106.15810.pdf), [Code](https://github.com/CUAI/Edge-Proposal-Sets) | 0 | GeForce RTX 2080 Ti (11GB GPU) | Jul 13, 2021 |
|  14  |  **SEAL-nofeat (val as input)**  | No | 0.6474 ± 0.0043   | 0.6495 ± 0.0043 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 501,570 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2021 |
|  15  |  Adamic Adar  | No | 0.6417 ± 0.0000   | 0.6349 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.1370&rep=rep1&type=pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  16  |  Common Neighbor  | No | 0.6137 ± 0.0000   | 0.6036 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  17  |  **SEAL-nofeat**  | No | 0.5471 ± 0.0049   | 0.6495 ± 0.0043 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 501,570 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2021 |
|  18  |  GraphSAGE  (val as input)  | No | 0.5463 ± 0.0112   | 0.5688 ± 0.0077 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 460,289 | GeForce RTX 2080 (11GB GPU) | Oct 19, 2020 |
|  19  |  **NGNN + GraphSAGE**  | No | 0.5359 ± 0.0056   | 0.6281 ± 0.0046 |[Yakun Song(DGL)](mailto:ereboas@sjtu.edu.cn) | [Paper](https://arxiv.org/abs/2111.11638), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ngnn) | 591,873 | Tesla-V100(16GB GPU) | Aug 16, 2022 |
|  20  |  **NGNN + GCN**  | No | 0.5348 ± 0.0040   | 0.6273 ± 0.0040 |[Yakun Song(DGL)](mailto:ereboas@sjtu.edu.cn) | [Paper](https://arxiv.org/abs/2111.11638), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ngnn) | 428,033 | Tesla-V100(16GB GPU) | Aug 16, 2022 |
|  21  |  **DeeperGCN**  | No | 0.5273 ± 0.0047   | 0.6187 ± 0.0045 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 117,383 | NVIDIA Tesla V100 (32GB GPU) | Oct 21, 2020 |
|  22  |  **LRGA + GCN**  | No | 0.5221 ± 0.0072   | 0.6088 ± 0.0059 |[Omri Puny](mailto:omri.puny@weizmann.ac.il) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/omri1348/LRGA/tree/master/ogb/examples/linkproppred) | 1,069,489 | Tesla P100 (16GB GPU) | Aug 5, 2020 |
|  23  |  **Jaccard Index**  | No | 0.5050 ± 0.0000   | 0.6098 ± 0.0000 |[Mehrdad Rafiepour (University of Kashan)](mailto:mehrdad.rafie.p@gmail.com) | [Paper](https://arxiv.org/abs/2501.06721), [Code](https://github.com/rafiepour/ClusteringEffect) | 0 | CPU (32GB RAM) | Jan 15, 2025 |
|  24  |  DeepWalk  | No | 0.5037 ± 0.0034   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 61,390,187 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  25  |  Node2vec  | No | 0.4888 ± 0.0054   | 0.5703 ± 0.0052 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 30,322,945 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  26  |  GraphSAGE  | No | 0.4810 ± 0.0081   | 0.5688 ± 0.0077 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 460,289 | GeForce RTX 2080 (11GB GPU) | Jun 24, 2020 |
|  27  |  GCN (val as input)  | No | 0.4714 ± 0.0145   | 0.5263 ± 0.0115 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 296,449 | GeForce RTX 2080 (11GB GPU) | Oct 19, 2020 |
|  28  |  GCN  | No | 0.4475 ± 0.0107   | 0.5263 ± 0.0115 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jun 24, 2020 |
|  29  |  Matrix Factorization  | No | 0.3886 ± 0.0029   | 0.4896 ± 0.0029 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 60,514,049 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |




<a name="ogbl-ddi"/>

-------

### Leaderboard for [ogbl-ddi](../linkprop/#ogbl-ddi)
##### The Hits@20 score on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Ext. data | Test Hits@20 | Validation Hits@20 | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **HyperFusion**  | No | 0.9972 ± 0.0004   | 0.9956 ± 0.0001 |[Xinwei Zhang(Tsinghua University)](mailto:xinwei-z21@mails.tsinghua.edu.cn) | [Paper](https://github.com/zhangxwww/HyperFusion/blob/master/Multi_Model_Ensemble_on_Hypergraph.pdf), [Code](https://github.com/zhangxwww/HyperFusion) | 976,022,023 | RTX 3080 | Feb 24, 2024 |
|  2  |  **ELGNN**  | No | 0.9777 ± 0.0037   | 0.8965 ± 0.0021 |[Zhen Hao Wong (EE Tsinghua)](mailto:huang-zh20@mails.tsinghua.edu.cn) | [Paper](https://arxiv.org/abs/2310.14166), [Code](https://github.com/wongzhenhao/ELGNN) | 10,512,391 |  NVIDIA A100 GPU (80G RAM) | Oct 23, 2023 |
|  3  |  GCN (node embedding)  | No | 0.9549 ± 0.0073   | 0.9098 ± 0.0294 | [Shuming Liang (UTS)](mailto:shuming.liang@uts.edu.au) | [Paper](https://arxiv.org/abs/2411.14711), [Code](https://github.com/astroming/GNNHE/tree/main) | 5,125,250 | NVIDIA Quadro P6000 (24G) | Nov 24, 2024 |
|  4  |  **GIDN@YITU**  | No | 0.9542 ± 0.0000   | 0.8258 ± 0.0000 |[Zixiao Wang, Yu Zhang(Zhejiang Lab,HUST)](mailto:zwang62@hust.edu.cn) | [Paper](https://arxiv.org/abs/2210.01301), [Code](https://github.com/WizcoxYu/ogbl_d) | 3,506,691 | DepGraph@SCTS/CGCL | Oct 11, 2022 |
|  5  |  **AGDN (AUC loss)**  | No | 0.9538 ± 0.0094   | 0.8943 ± 0.0281 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2012.15024), [Code](https://github.com/skepsun/Adaptive-Graph-Diffusion-Networks) | 3,506,691 | Tesla V100 (16GB GPU) | Sep 2, 2022 |
|  6  |  **Refined-GAE**  | No | 0.9443 ± 0.0057   | 0.7526 ± 0.0240 |[Weishuo Ma(Peking University)](mailto:2200013081@stu.pku.edu.com) | [Paper](https://arxiv.org/html/2411.03845v1), [Code](https://github.com/GraphPKU/Refined-GAE) | 13,816,833 | RTX 4090 (24GB) | Nov 7, 2024 |
|  6  |  **Refined-GAE**  | No | 0.9443 ± 0.0057   | 0.7979 ± 0.0159 |[Weishuo Ma(Peking University)](mailto:2200013081@stu.pku.edu.cn) | [Paper](https://arxiv.org/abs/2411.03845), [Code](https://github.com/GraphPKU/Refined-GAE) | 13,816,833 | RTX 4090 (24GB) | Nov 23, 2024 |
|  7  |  **PSG**  | No | 0.9284 ± 0.0047   | 0.8306 ± 0.0134 |[Jingsong Lv(Zhuque@ZhejiangLab)](mailto:jingsonglv@zhejianglab.com) | [Paper](https://arxiv.org/pdf/2208.05781.pdf), [Code](https://github.com/jingsonglv/PSG) | 3,499,009 | Tesla V100(32G GPU) | Aug 12, 2022 |
|  8  |  **PLNLP**  | No | 0.9088 ± 0.0313   | 0.8242 ± 0.0253 |[Zhitao Wang (WeChat@Tencent)](mailto:wztzenk@gmail.com) | [Paper](https://arxiv.org/abs/2112.02936), [Code](https://github.com/zhitao-wang/PLNLP) | 3,497,473 | Tesla-P40(24GB GPU) | Dec 7, 2021 |
|  9  |  **GDNN**  | No | 0.9037 ± 0.0193   | 0.8599 ± 0.0286 |[Haifan Zhou(Ainnocence)](mailto:zhouhf@connect.hku.hk) | [Paper](https://github.com/zhf3564859793/GDNN), [Code](https://github.com/zhf3564859793/GDNN) | 3,761,665 | A40-NVLink(48GB) | Aug 30, 2022 |
|  10  |  **GraphSAGE + Edge Attr**  | No | 0.8781 ± 0.0474   | 0.8044 ± 0.0404 |[Jing Yang](mailto:jyangboston@gmail.com) | [Paper](https://github.com/lustoo/OGB_link_prediction/blob/main/Link%20prediction%20with%20structural%20information.pdf), [Code](https://github.com/lustoo/OGB_link_prediction) | 3,761,665 | Tesla V100 (32GB) | Aug 9, 2021 |
|  11  |  **CFLP (w/ JKNet)**  | No | 0.8608 ± 0.0198   | 0.8405 ± 0.0284 |[Tong Zhao](mailto:tzhao2@nd.edu) | [Paper](https://arxiv.org/pdf/2106.02172.pdf), [Code](https://github.com/DM2-ND/CFLP) | 837,635 | GeForce RTX 2080 Ti (11GB GPU) | Nov 17, 2021 |
|  11  |  **CFLP (w/ JKNet)**  | No | 0.8608 ± 0.0198   | 0.8405 ± 0.0284 |[Tong Zhao (University of Notre Dame)](mailto:tzhao2@nd.edu) | [Paper](https://arxiv.org/pdf/2106.02172.pdf), [Code](https://github.com/DM2-ND/CFLP) | 837,635 | GeForce RTX 2080 Ti (11GB GPU) | Nov 17, 2021 |
|  12  |  **GraphSAGE+anchor distance**  | No | 0.8239 ± 0.0437   | 0.8206 ± 0.0298 |[Boning Li (SJTU)](mailto:lbn187@sjtu.edu.cn) | [Paper](https://www.dropbox.com/s/is3f4dfvtvnis7w/DEGNN_linkPrediction.pdf?dl=0), [Code](https://github.com/lbn187/DLGNN) | 3,760,134 | Tesla V100 (16GB GPU) | May 20, 2021 |
|  13  |  **NeuralCommonNeighbor**  | No | 0.8232 ± 0.0610   | 0.7172 ± 0.0025 |[Xiyuan Wang (Peking University)](mailto:wangxiyuan@pku.edu.cn) | [Paper](https://arxiv.org/pdf/2302.00890.pdf), [Code](https://github.com/GraphPKU/NeuralCommonNeighbor) | 1,412,098 | RTX 4090 (24GB) | Mar 17, 2023 |
|  14  |  **ELPH**  | No | 0.7704 ± 0.0582   | 0.6928 ± 0.0096 |[Ben Chamberlain](mailto:benjamin.chamberlain@gmail.com) | [Paper](https://openreview.net/pdf?id=m1oqEOAozQU), [Code](https://github.com/melifluos/subgraph-sketching) | 2,910,817 | Tesla K80 (12GB GPU) | Jul 5, 2023 |
|  15  |  DEA + JKNet  | No | 0.7672 ± 0.0265   | 0.6713 ± 0.0071 | [Yichen Yang](mailto:jeffrey576826145@outlook.com) | [Paper](https://github.com/JeffJeffy/CS224W-OGB-DEA-JK/blob/main/CS224w_final_report.pdf), [Code](https://github.com/JeffJeffy/CS224W-OGB-DEA-JK) | 1,763,329 | Tesla T4 (16GB GPU) | Mar 21, 2021 |
|  16  |  **BUDDY**  | No | 0.7654 ± 0.0459   | 0.6927 ± 0.0054 |[Ben Chamberlain](mailto:benjamin.chamberlain@gmail.com) | [Paper](https://openreview.net/pdf?id=m1oqEOAozQU), [Code](https://github.com/melifluos/subgraph-sketching) | 2,712,931 | Tesla K80 (12GB GPU) | Jul 4, 2023 |
|  17  |  **GraphSAGE+Edge Proposal Set**  | No | 0.7495 ± 0.0317   | 0.6696 ± 0.0198 |[Qian Huang (Cornell University)](mailto:qh53@cornell.edu) | [Paper](https://arxiv.org/pdf/2106.15810.pdf), [Code](https://github.com/CUAI/Edge-Proposal-Sets) | 1,421,057 | GeForce RTX 2080 Ti (11GB GPU) | Jul 21, 2021 |
|  18  |  LRGA+GCN(Node2Vec+Augment)  | No | 0.7385 ± 0.0871   | 0.7225 ± 0.0047 | [Chuanqi Chen](mailto:chuanqi.chen@gmail.com) | [Paper](https://github.com/chuanqichen/cs224w/blob/main/the_study_of_drug_drug_interaction_learning_through_various_graph_learning_methods.pdf), [Code](https://github.com/chuanqichen/cs224w) | 10,235,281 | Tesla V100 (32GB) | Mar 21, 2021 |
|  19  |  **MAD Learning**  | No | 0.6781 ± 0.0294   | 0.7010 ± 0.0082 |[Yi Luo](mailto:cf020031308@163.com) | [Paper](https://arxiv.org/abs/2102.05246), [Code](https://github.com/cf020031308/mad-learning/blob/master/ogbl-ddi.py) | 1,228,897 | Geforce GTX 1080 Ti (11GB GPU) | Feb 10, 2021 |
|  20  |  **LRGA + GCN**  | No | 0.6230 ± 0.0912   | 0.6675 ± 0.0058 |[Omri Puny](mailto:omri.puny@weizmann.ac.il) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/omri1348/LRGA/tree/master/ogb/examples/linkproppred) | 1,576,081 | Tesla P100 (16GB GPU) | Aug 5, 2020 |
|  21  |  GCN+JKNet  | No | 0.6056 ± 0.0869   | 0.6776 ± 0.0095 | [Horace He  (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/Chillee/ogb_ddi) | 1,421,571 | Geforce GTX 1080 Ti (11GB GPU) | Sep 15, 2020 |
|  22  |  **NGNN + GraphSAGE**  | No | 0.5770 ± 0.1523   | 0.7323 ± 0.0040 |[Yakun Song(DGL)](mailto:ereboas@sjtu.edu.cn) | [Paper](https://arxiv.org/abs/2111.11638), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ngnn) | 1,618,433 | Tesla-V100(16GB GPU) | Aug 16, 2022 |
|  23  |  **NGNN + GCN**  | No | 0.5483 ± 0.1581   | 0.7121 ± 0.0038 |[Yakun Song(DGL)](mailto:ereboas@sjtu.edu.cn) | [Paper](https://arxiv.org/abs/2111.11638), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ngnn) | 1,487,361 | Tesla-V100(16GB GPU) | Aug 16, 2022 |
|  24  |  GraphSAGE  | No | 0.5390 ± 0.0474   | 0.6262 ± 0.0037 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,421,057 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  25  |  GCN  | No | 0.3707 ± 0.0507   | 0.5550 ± 0.0208 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,289,985 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  26  |  **SEAL**  | No | 0.3056 ± 0.0386   | 0.2849 ± 0.0269 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 531,138 | GeForce RTX 2080S (8GB GPU) | Oct 14, 2020 |
|  27  |  DeepWalk  | No | 0.2642 ± 0.0610   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 11,543,913 | g4dn.2xlarge, T4 (15GB GPU) | Jul 23, 2020 |
|  28  |  Node2vec  | No | 0.2326 ± 0.0209   | 0.3292 ± 0.0121 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 645,249 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  29  |  DeepWalk  | No | 0.2246 ± 0.0290   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 1,543,913 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  30  |  Adamic Adar  | No | 0.1861 ± 0.0000   | 0.0966 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.1370&rep=rep1&type=pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  31  |  Common Neighbor  | No | 0.1773 ± 0.0000   | 0.0947 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  32  |  Matrix Factorization  | No | 0.1368 ± 0.0475   | 0.3370 ± 0.0264 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,224,193 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |




<a name="ogbl-citation2"/>

-------

### Leaderboard for [ogbl-citation2](../linkprop/#ogbl-citation2)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.4
###### Deprecated `ogbl-citation` leaderboard can be found [here](../leader_deprecated/#ogbl-citation).

| Rank  | Method | Ext. data | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GraphGPT(d1n30)**  | No | 0.9305 ± 0.0020   | 0.9295 ± 0.0022 |[Qifang Zhao(Alibaba)](mailto:james.zqf@alibaba-inc.com) | [Paper](https://arxiv.org/abs/2401.00529), [Code](https://github.com/alibaba/graph-gpt) | 133,096,832 | 8 Nvidia L20 | Oct 28, 2024 |
|  2  |  **MPLP**  | No | 0.9072 ± 0.0012   | 0.9074 ± 0.0011 |[Kaiwen Dong (University of Notre Dame)](mailto:kevindong1994@gmail.com) | [Paper](https://arxiv.org/pdf/2309.00976.pdf), [Code](https://github.com/Barcavin/efficient-node-labelling) | 749,757,283 | NVIDIA A100 GPU (80G RAM) | Jan 16, 2024 |
|  3  |  **GraphGPT(SMTP)**  | No | 0.9055 ± 0.0016   | 0.9042 ± 0.0014 |[Qifang Zhao (Alibaba)](mailto:james.zqf@alibaba-inc.com) | [Paper](https://arxiv.org/abs/2401.00529), [Code](https://github.com/alibaba/graph-gpt) | 46,784,128 | 8 Nvidia L20 | Oct 10, 2024 |
|  4  |  **SIEG**  | No | 0.9018 ± 0.0015   | 0.9011 ± 0.0015 |[anonymous20221001 (anonymous)](mailto:anonymous20221001@126.com) | [Paper](https://github.com/anonymous20221001/SIEG_OGB/blob/master/OGB_VESSEL_SIEG.pdf), [Code](https://github.com/anonymous20221001/SIEG_OGB) | 2,428,365 |  P100 (16GB) | Oct 23, 2023 |
|  5  |  **CFG**  | No | 0.9003 ± 0.0007   | 0.8992 ± 0.0007 |[Jingsong Lv (Zhuque@ZhejiangLab)](mailto:jingsonglv@zhejianglab.com) | [Paper](https://arxiv.org/abs/2309.06574), [Code](https://github.com/jingsonglv/CFG) | 686,253 | NVIDIA A100 (80GB GPU) | Sep 30, 2023 |
|  6  |  **CFG**  | No | 0.8997 ± 0.0015   | 0.8987 ± 0.0011 |[Jingsong LV (Zhuque@ZhejiangLab)](mailto:jingsonglv@zhejianglab.com) | [Paper](http://arxiv.org/abs/2309.06574), [Code](https://github.com/jingsonglv/CFG) | 686,253 | NVIDIA A100 (80GB GPU) | Sep 14, 2023 |
|  7  |  **SIEG**  | No | 0.8987 ± 0.0018   | 0.8978 ± 0.0018 |[anonymous20221001 (anonymous)](mailto:anonymous20221001@126.com) | [Paper](https://github.com/anonymous20221001/SIEG_OGB/blob/master/OGB_VESSEL_SIEG.pdf), [Code](https://github.com/anonymous20221001/SIEG_OGB) | 667,821 | P100 (16GB) | Jan 29, 2023 |
|  8  |  **SIEG**  | No | 0.8957 ± 0.0010   | 0.8948 ± 0.0008 |[anonymous20221001 (anonymous)](mailto:anonymous20221001@126.com) | [Paper](https://github.com/anonymous20221001/SIEG_OGB/blob/master/OGB_VESSEL_SIEG.pdf), [Code](https://github.com/anonymous20221001/SIEG_OGB) | 256,802 | P100 | Dec 25, 2022 |
|  9  |  GCN + Heuristic Encoding  | No | 0.8891 ± 0.0005   | 0.8892 ± 0.0005 | [Shuming Liang (UTS)](mailto:shuming.liang@uts.edu.au) | [Paper](https://arxiv.org/abs/2411.14711), [Code](https://github.com/astroming/GNNHE) | 372,674 | NVIDIA A100 (40G) | Nov 24, 2024 |
|  9  |  **NGNN + SEAL**  | No | 0.8891 ± 0.0022   | 0.8879 ± 0.0022 |[Yakun Song(DGL)](mailto:ereboas@sjtu.edu.cn) | [Paper](https://arxiv.org/abs/2111.11638), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/ngnn_seal) | 1,134,402 | Tesla T4(16GB) | Nov 6, 2022 |
|  10  |  **SUREL**  | No | 0.8883 ± 0.0018   | 0.8891 ± 0.0021 |[Haoteng Yin (Purdue University)](mailto:yinht@purdue.edu) | [Paper](https://arxiv.org/abs/2202.13538), [Code](https://github.com/Graph-COM/SUREL) | 79,617 | Quadro RTX 6000 | Mar 18, 2022 |
|  11  |  **S3GRL (PoS Plus)**  | No | 0.8814 ± 0.0008   | 0.8809 ± 0.0074 |[Paul Louis (Ontario Tech University)](mailto:paul.louis@ontariotechu.net) | [Paper](https://arxiv.org/pdf/2301.12562.pdf), [Code](https://github.com/venomouscyanide/S3GRL_OGB) | 142,275,001 | GeForce GTX 1080 Ti (11 GB) | May 2, 2023 |
|  12  |  **BUDDY**  | No | 0.8796 ± 0.0008   | 0.8793 ± 0.0008 |[Ben Chamberlain](mailto:benjamin.chamberlain@gmail.com) | [Paper](https://openreview.net/pdf?id=m1oqEOAozQU), [Code](https://github.com/melifluos/subgraph-sketching) | 166,531 | Tesla K80 (12GB GPU) | Aug 29, 2023 |
|  13  |  **SEAL**  | No | 0.8767 ± 0.0032   | 0.8757 ± 0.0031 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 260,802 | Tesla V100 (32GB GPU) | Feb 12, 2021 |
|  14  |  **AGDN w/GraphSAINT**  | No | 0.8549 ± 0.0029   | 0.8556 ± 0.0033 |[Chuxiong Sun](mailto:chuxiongsun@gmail.com) | [Paper](https://arxiv.org/abs/2012.15024), [Code](https://github.com/skepsun/Adaptive-Graph-Diffusion-Networks) | 306,716 | Tesla V100 (16GB GPU) | Sep 2, 2022 |
|  15  |  **PLNLP**  | No | 0.8492 ± 0.0029   | 0.8490 ± 0.0031 |[Zhitao Wang (WeChat@Tencent)](mailto:wztzenk@gmail.com) | [Paper](https://arxiv.org/pdf/2112.02936.pdf), [Code](https://github.com/zhitao-wang/PLNLP) | 146,514,551 | Tesla-V100 (32G GPU) | Dec 7, 2021 |
|  16  |  Full-batch GCN  | No | 0.8474 ± 0.0021   | 0.8479 ± 0.0023 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | Quadro RTX 8000 (48GB GPU) | Jan 4, 2021 |
|  17  |  **HPE - Pre-trained Initialized**  | No | 0.8432 ± 0.0003   | 0.8422 ± 0.0002 |[Chi-Hung Chang (CFDA & CLIP Labs)](mailto:chihung861224@gmail.com) | [Paper](https://dl.acm.org/doi/10.1145/2959100.2959169), [Code](https://github.com/chang861224/HPE_OGB) | 749,558,528 | CPU | Dec 7, 2021 |
|  18  |  Full-batch GraphSAGE  | No | 0.8260 ± 0.0036   | 0.8263 ± 0.0033 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 460,289 | Quadro RTX 8000 (48GB GPU) | Jan 4, 2021 |
|  19  |  NeighborSampling (SAGE aggr)  | No | 0.8044 ± 0.0010   | 0.8054 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 460,289 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  20  |  ClusterGCN (GCN aggr)  | No | 0.8004 ± 0.0025   | 0.7994 ± 0.0025 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  21  |  GraphSAINT (GCN aggr)  | No | 0.7985 ± 0.0040   | 0.7975 ± 0.0039 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  22  |  Node2vec  | No | 0.6141 ± 0.0011   | 0.6124 ± 0.0011 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 374,911,105 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  23  |  Adamic Adar  | No | 0.5189 ± 0.0000   | 0.5167 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.1370&rep=rep1&type=pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  24  |  Matrix Factorization  | No | 0.5186 ± 0.0443   | 0.5181 ± 0.0436 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 281,113,505 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  25  |  Common Neighbor  | No | 0.5147 ± 0.0000   | 0.5119 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |



<a name="ogbl-wikikg2"/>

-------

### Leaderboard for [ogbl-wikikg2](../linkprop/#ogbl-wikikg2)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.4
###### Deprecated `ogbl-wikikg` leaderboard can be found [here](../leader_deprecated/#ogbl-wikikg).

| Rank  | Method | Ext. data | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **RelEns**  | No | 0.7392 ± 0.0011   | 0.7509 ± 0.0009 |[Quanming Yao (EE Tsinghua)](mailto:qyaoaa@mail.tsinghua.edu.cn) | [Paper](https://arxiv.org/pdf/2310.08917.pdf), [Code](https://github.com/LARS-research/RelEns) | 2,176,767,622 | Tesla A100(80GB) | Oct 15, 2023 |
|  2  |  **StarGraph + TripleRE + Text**  | Yes | 0.7305 ± 0.0010   | 0.7442 ± 0.0006 |[Liang Yao (Tencent)](mailto:dryao@tencent.com) | [Paper](https://github.com/yao8839836/ogb_report/blob/main/StarGraph_Text/wikikg2_report.pdf), [Code](https://github.com/yao8839836/ogb_report/tree/main/StarGraph_Text) | 1,927,395,330 | Tesla V100 (32GB) | Jan 4, 2023 |
|  3  |  **InterHT+**  | No | 0.7293 ± 0.0018   | 0.7391 ± 0.0023 |[Baoxin Wang (HFL)](mailto:destin.bxwang@gmail.com) | [Paper](https://arxiv.org/abs/2202.04897), [Code](https://github.com/destwang/InterHT) | 156,332,770 | Tesla A100 (80GB) | Dec 23, 2022 |
|  4  |  **StarGraph + TripleRE**  | No | 0.7286 ± 0.0009   | 0.7335 ± 0.0011 |[Linhui Feng (360AI)](mailto:fenglinghui@360.cn) | [Paper](https://arxiv.org/abs/2205.14209), [Code](https://github.com/hzli-ucas/StarGraph) | 93,039,522 | Tesla A100 (40GB) | Jan 3, 2023 |
|  5  |  **InterHT+ (256dim)**  | No | 0.7257 ± 0.0018   | 0.7370 ± 0.0022 |[Baoxin Wang (HFL)](mailto:destin.bxwang@gmail.com) | [Paper](https://arxiv.org/abs/2202.04897v2), [Code](https://github.com/destwang/InterHT) | 148,000,738 | Tesla A100 (40GB) | Dec 26, 2022 |
|  6  |  **StarGraph + TripleRE**  | No | 0.7201 ± 0.0011   | 0.7288 ± 0.0008 |[Hongzhu Li (360AI)](mailto:lihongzhu@360.cn) | [Paper](https://arxiv.org/abs/2205.14209), [Code](https://github.com/hzli-ucas/StarGraph) | 86,762,146 | Tesla A100(40GB) | May 30, 2022 |
|  7  |  **CompoundE3D**  | No | 0.7006 ± 0.0011   | 0.7175 ± 0.0015 |[Xiou Ge (USC)](mailto:ge.xiou.2012@gmail.com) | [Paper](https://arxiv.org/abs/2304.00378), [Code](https://github.com/hughxiouge/CompoundE3D) | 750,662,700 | Tesla A100 (40GB GPU) | Dec 29, 2023 |
|  8  |  **TranS**  | No | 0.6939 ± 0.0011   | 0.7058 ± 0.0018 |[Xuanyu Zhang (DXM AI)](mailto:xuanyuzhang94@gmail.com) | [Paper](https://arxiv.org/abs/2204.08401), [Code](https://github.com/xyznlp/trans) | 38,430,804 | Tesla V100 (16GB) | Apr 19, 2022 |
|  9  |  **TranS**  | No | 0.6882 ± 0.0019   | 0.6988 ± 0.0006 |[Xuanyu Zhang (DXM AI)](mailto:xuanyuzhang94@gmail.com) | [Paper](https://arxiv.org/abs/2204.08401), [Code](https://github.com/xyznlp/trans) | 19,215,402 | Tesla V100 (16GB) | Apr 28, 2022 |
|  10  |  **TripleRE + NodePiece**  | No | 0.6866 ± 0.0014   | 0.6955 ± 0.0008 |[Long Yu (360AI)](mailto:yulong_i@163.com) | [Paper](https://vixra.org/abs/2112.0095), [Code](https://github.com/LongYu-360/TripleRE-Add-NodePiece-v2) | 36,421,802 | Tesla A100(40GB) | Feb 24, 2022 |
|  11  |  **InterHT**  | No | 0.6779 ± 0.0018   | 0.6893 ± 0.0015 |[Baoxin Wang (HFL)](mailto:destin.bxwang@gmail.com) | [Paper](https://arxiv.org/abs/2202.04897), [Code](https://github.com/destwang/InterHT) | 19,215,402 | Tesla V100 (32GB) | Feb 10, 2022 |
|  12  |  **A*Net**  | No | 0.6711 ± 0.0045   | 0.6796 ± 0.0070 |[Zhaocheng Zhu (Mila)](mailto:zhaocheng.zhu@umontreal.ca) | [Paper](https://arxiv.org/abs/2206.04798), [Code](https://github.com/DeepGraphLearning/AStarNet/) | 6,831,201 | Tesla A100 (40GB) | May 21, 2023 |
|  13  |  **TripleRE + NodePiece**  | No | 0.6582 ± 0.0020   | 0.6616 ± 0.0018 |[Long Yu (360AI)](mailto:yulong_i@163.com) | [Paper](https://vixra.org/abs/2112.0095), [Code](https://github.com/LongYu-360/TripleRE-Add-NodePiece) | 7,289,002 | Tesla A100(40GB) | Dec 25, 2021 |
|  14  |  **ComplEx-RP (50dim)**  | No | 0.6392 ± 0.0045   | 0.6561 ± 0.0070 |[Yihong Chen (UCL NLP & FAIR London)](mailto:yihong.chen@cs.ucl.ac.uk) | [Paper](https://openreview.net/pdf?id=Qa3uS3H7-Le), [Code](https://github.com/facebookresearch/ssl-relation-prediction) | 250,167,400 | Tesla V100 (32GB) | Nov 23, 2021 |
|  15  |  **TransERR**  | No | 0.6359 ± 0.0020   | 0.6518 ± 0.0012 |[Jiang Li (IMU-AI)](mailto:futuretopdelli@163.com) | [Paper](https://arxiv.org/pdf/2306.14580.pdf), [Code](https://github.com/dellixx/TransERR) | 500,441,802 | Tesla V100 (32GB) | Jun 26, 2023 |
|  16  |  **tripleRE**  | No | 0.5794 ± 0.0020   | 0.6045 ± 0.0024 |[Long Yu (360AI)](mailto:yulong_i@163.com) | [Paper](https://vixra.org/abs/2112.0095), [Code](https://github.com/LongYu-360/TripleRE) | 500,763,337 | Tesla P40(24GB) | Dec 17, 2021 |
|  17  |  **NodePiece + AutoSF**  | No | 0.5703 ± 0.0035   | 0.5806 ± 0.0047 |[Mikhail Galkin (Mila)](mailto:mikhail.galkin@mila.quebec) | [Paper](https://arxiv.org/abs/2106.12144), [Code](https://github.com/migalkin/NodePiece/tree/main/ogb) | 6,860,602 | Tesla V100 (32 GB) | Jul 17, 2021 |
|  18  |  **Rot-Pro**  | No | 0.5602 ± 0.0016   | 0.5740 ± 0.0008 |[Tengwei Song(BUAA-NLSDE)](mailto:songtengwei@gmail.com) | [Paper](https://arxiv.org/pdf/2110.14450.pdf), [Code](https://github.com/Tigter/ogblwikikg2-RotPro) | 1,000,669,602 | Tesla V100(32GB) | Sep 5, 2022 |
|  19  |  **AutoSF**  | No | 0.5458 ± 0.0052   | 0.5510 ± 0.0063 |[Yongqi Zhang (4Paradigm)](mailto:zhangyongqi@4paradigm.com) | [Paper](https://arxiv.org/pdf/1904.11682.pdf), [Code](https://github.com/AutoML-4Paradigm/AutoSF/tree/AutoSF-OGB) | 500,227,800 | Quadro RTX 8000 (45GB GPU) | Apr 2, 2021 |
|  20  |  **PairRE (200dim)**  | No | 0.5208 ± 0.0027   | 0.5423 ± 0.0020 |[Linlin Chao](mailto:chulin.cll@antgroup.com) | [Paper](https://arxiv.org/abs/2011.03798), [Code](https://github.com/alipay/KnowledgeGraphEmbeddingsViaPairedRelationVectors_PairRE) | 500,334,800 | Tesla P100 (16GB GPU) | Jan 28, 2021 |
|  21  |  RotatE (250dim)  | No | 0.4332 ± 0.0025   | 0.4353 ± 0.0028 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,435,750 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  22  |  TransE (500dim)  | No | 0.4256 ± 0.0030   | 0.4272 ± 0.0030 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  23  |  ComplEx (250dim)  | No | 0.4027 ± 0.0027   | 0.3759 ± 0.0016 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  24  |  ComplEx (50dim)  | No | 0.3804 ± 0.0022   | 0.3534 ± 0.0052 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  25  |  DistMult (500dim)  | No | 0.3729 ± 0.0045   | 0.3506 ± 0.0042 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  26  |  DistMult (100dim)  | No | 0.3447 ± 0.0082   | 0.3150 ± 0.0088 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  27  |  TransE (100dim)  | No | 0.2622 ± 0.0045   | 0.2465 ± 0.0020 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  28  |  RotatE (50dim)  | No | 0.2530 ± 0.0034   | 0.2250 ± 0.0035 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,087,150 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |


<a name="ogbl-biokg"/>

-------

### Leaderboard for [ogbl-biokg](../linkprop/#ogbl-biokg)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.0

| Rank  | Method | Ext. data | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **RelEns**  | No | 0.9618 ± 0.0002   | 0.9627 ± 0.0004 |[Quanming Yao (EE Tsinghua)](mailto:qyaoaa@mail.tsinghua.edu.cn) | [Paper](https://arxiv.org/pdf/2310.08917.pdf), [Code](https://github.com/LARS-research/RelEns) | 849,427,106 | Tesla A100 (80GB) | Oct 15, 2023 |
|  2  |  **ComplEx^2**  | No | 0.8583 ± 0.0005   | 0.8592 ± 0.0004 |[Lorenzo Loconte (Univ. of Edinburgh)](mailto:l.loconte@sms.ed.ac.uk) | [Paper](https://arxiv.org/abs/2305.15944), [Code](https://github.com/april-tools/gekcs) | 187,648,000 | NVIDIA RTX A6000 (48GB) | Oct 28, 2023 |
|  3  |  **UniBi**  | No | 0.8550 ± 0.0003   | 0.8553 ± 0.0001 |[Ruilin Luo (THU)](mailto:lrl23@mails.tsinghua.edu.cn) | [Paper](https://arxiv.org/pdf/2309.13834.pdf), [Code](https://github.com/lrlbbzl/unibi_ogb) | 181,654,170 | RTX 4090 (24GB) | Dec 2, 2023 |
|  4  |  **AutoBLM-KGBench**  | No | 0.8536 ± 0.0003   | 0.8548 ± 0.0002 |[Yongqi Zhang (4Paradigm && EE Tsinghua)](mailto:zhangyongqi@4paradigm.com) | [Paper](https://arxiv.org/pdf/2107.00184.pdf), [Code](https://github.com/AutoML-Research/KGBench) | 192,047,104 | Tesla A100 (80G) | Jun 17, 2022 |
|  5  |  **ComplEx-RP (1000dim)**  | No | 0.8492 ± 0.0002   | 0.8497 ± 0.0002 |[Yihong Chen (UCL NLP & FAIR London)](mailto:yihong.chen@cs.ucl.ac.uk) | [Paper](https://openreview.net/pdf?id=Qa3uS3H7-Le), [Code](https://github.com/facebookresearch/ssl-relation-prediction) | 187,750,000 | Tesla V100 (16GB) | Nov 23, 2021 |
|  6  |  **TripleRE**  | No | 0.8348 ± 0.0007   | 0.8360 ± 0.0006 |[LongYu(360AI)](mailto:yulong_i@163.com) | [Paper](https://vixra.org/abs/2112.0095), [Code](https://github.com/LongYu-360/TripleRE-biokg) | 469,630,002 | Tesla A100(40GB) | Jan 28, 2022 |
|  7  |  **AutoSF**  | No | 0.8309 ± 0.0008   | 0.8317 ± 0.0007 |[Yongqi Zhang (4Paradigm)](mailto:zhangyongqi@4paradigm.com) | [Paper](https://arxiv.org/pdf/1904.11682.pdf), [Code](https://github.com/AutoML-4Paradigm/AutoSF/tree/AutoSF-OGB) | 93,824,000 | GeForce RTX 2080 (11GB GPU) | Apr 2, 2021 |
|  8  |  **PairRE**  | No | 0.8164 ± 0.0005   | 0.8172 ± 0.0005 |[LinlinChao (AntGroup KG&NLP)](mailto:chulin.cll@antgroup.com) | [Paper](https://arxiv.org/abs/2011.03798), [Code](https://github.com/alipay/KnowledgeGraphEmbeddingsViaPairedRelationVectors_PairRE) | 187,750,000 | Tesla P100 (16GB GPU) | Nov 9, 2020 |
|  9  |  ComplEx  | No | 0.8095 ± 0.0007   | 0.8105 ± 0.0001 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  10  |  DistMult  | No | 0.8043 ± 0.0003   | 0.8055 ± 0.0003 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  11  |  RotatE  | No | 0.7989 ± 0.0004   | 0.7997 ± 0.0002 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,597,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  12  |  TransE  | No | 0.7452 ± 0.0004   | 0.7456 ± 0.0003 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |


<a name="ogbl-vessel"/>

-------

### Leaderboard for [ogbl-vessel](../linkprop/#ogbl-vessel)
##### The ROC-AUC score on the test and validation sets. The higher, the better.

#### Package: >=1.3.4

| Rank  | Method | Ext. data | Test ROC-AUC | Validation ROC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GAV**  | No | 0.9838 ± 0.0002   | 0.9837 ± 0.0002 |[Bastian Wittmann (UZH)](mailto:bastian.wittmann@uzh.ch) | [Paper](https://arxiv.org/abs/2303.14501), [Code](https://github.com/bwittmann/GAV) | 8,194 | Tesla V100 (32 GB GPU) | Mar 28, 2023 |
|  2  |  **SIEG(SPG)**  | No | 0.9687 ± 0.0001   | 0.9687 ± 0.0001 |[anonymous20221001 (anonymous)](mailto:anonymous20221001@126.com) | [Paper](https://github.com/anonymous20221001/SIEG_OGB/blob/master/OGB_VESSEL_SIEG.pdf), [Code](https://github.com/anonymous20221001/SIEG_OGB) | 1,306,956 | P100 (16GB) | Aug 15, 2023 |
|  3  |  **MLP+DiffPredictor**  | No | 0.9414 ± 0.0001   | 0.9415 ± 0.0002 |[Chuxiong Sun (CTRI)](mailto:chuxiongsun@gmail.com) | [Paper](https://github.com/skepsun/ogbl_vessel_baselines/blob/main/ogbl_vessel_baselines.pdf), [Code](https://github.com/skepsun/ogbl_vessel_baselines) | 16,961 | Tesla V100 (16GB GPU) | Aug 7, 2023 |
|  4  |  **SIEG w/o NF**  | No | 0.8798 ± 0.0100   | 0.8803 ± 0.0100 |[anonymous20221001 (anonymous)](mailto:anonymous20221001@126.com) | [Paper](https://github.com/anonymous20221001/SIEG_OGB/blob/master/OGB_VESSEL_SIEG.pdf), [Code](https://github.com/anonymous20221001/SIEG_OGB) | 752,716 | P100 (16GB) | Mar 27, 2023 |
|  5  |  **SUREL+**  | No | 0.8496 ± 0.0068   | 0.8489 ± 0.0067 |[Haoteng Yin (Purdue University)](mailto:yinht@purdue.edu) | [Paper](https://arxiv.org/abs/2303.03379), [Code](https://github.com/Graph-COM/SUREL_Plus) | 56,353 | Quadro RTX 6000 (24GB) | Feb 28, 2023 |
|  6  |  **SIEG**  | No | 0.8307 ± 0.0044   | 0.8315 ± 0.0044 |[anonymous20221001 (anonymous)](mailto:anonymous20221001@126.com) | [Paper](https://github.com/anonymous20221001/SIEG_OGB/blob/master/OGB_VESSEL_SIEG.pdf), [Code](https://github.com/anonymous20221001/SIEG_OGB) | 407,338 | P100 (16GB) | Jan 29, 2023 |
|  7  |  **SIEG**  | No | 0.8249 ± 0.0041   | 0.8255 ± 0.0040 |[anonymous20221001 (anonymous)](mailto:axel.hb@alibaba-inc.com) | [Paper](https://github.com/anonymous20221001/SIEG_OGB/blob/master/OGB_VESSEL_SIEG.pdf), [Code](https://github.com/anonymous20221001/SIEG_OGB) | 594,498 | P100 (16GB) | Oct 1, 2022 |
|  8  |  SEAL (no-xfeat)  | No | 0.8077 ± 0.0001   | 0.8073 ± 0.0001 | [Huixuan Chi (Meituan)](mailto:chihuixuan99@gmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/ytchx1999/ogbl-vessel) | 43,714 | Tesla V100 (32GB) | Aug 28, 2022 |
|  9  |  **S3GRL (PoS Plus)**  | Yes | 0.8056 ± 0.0006   | 0.8065 ± 0.0022 |[Paul Louis (Ontario Tech University)](mailto:paul.louis@ontariotechu.net) | [Paper](https://arxiv.org/pdf/2301.12562.pdf), [Code](https://github.com/venomouscyanide/S3GRL_OGB) | 2,382,849 | GeForce GTX 1080 Ti (11 GB) | May 2, 2023 |
|  10  |  **SEAL**  | No | 0.8050 ± 0.0021   | 0.8053 ± 0.0022 |[Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](https://arxiv.org/abs/1802.09691), [Code](https://github.com/facebookresearch/SEAL_OGB) | 172,610 | Quadro RTX 8000 Ti (48GB GPU) | Aug 24, 2022 |
|  11  |  **Homogeneity Index**  | No | 0.5460 ± 0.0000   | 0.5459 ± 0.0000 |[Mehrdad Rafiepour (University of Kashan)](mailto:mehrdad.rafie.p@gmail.com) | [Paper](https://arxiv.org/abs/2501.06721), [Code](https://github.com/rafiepour/ClusteringEffect) | 0 | CPU (32GB RAM) | Jan 15, 2025 |
|  12  |  LRGA  | No | 0.5415 ± 0.0437   | 0.5418 ± 0.0439 | [Yuanchen Bei (Meituan)](mailto:iyuanchenbei@gmail.com) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/YuanchenBei/LRGA-vessel) | 26,577 | Tesla A100 (80GB) | Aug 31, 2022 |
|  13  |  SGC  | No | 0.5009 ± 0.0011   | 0.5010 ± 0.0011 | [Hao Xu(Meituan)](mailto:kingsleyhsu1@gmail.com) | [Paper](https://arxiv.org/pdf/1902.07153.pdf), [Code](https://github.com/KingsleyHsu/SMPLP) | 897 | Tesla V100(32GB) | Aug 24, 2022 |
|  14  |  SAGE+JKNet  | No | 0.5001 ± 0.0007   | 0.5014 ± 0.0004 | [Huixuan Chi (Meituan)](mailto:chihuixuan99@gmail.com) | [Paper](http://proceedings.mlr.press/v80/xu18c/xu18c.pdf), [Code](https://github.com/ytchx1999/ogbl-vessel) | 273 | Tesla V100 (32GB) | Aug 22, 2022 |
|  15  |  **Matrix Factorization**  | No | 0.4997 ± 0.0005   | 0.4999 ± 0.0006 |[Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/vessel) | 8,641 | Quadro RTX 8000Ti (48GB GPU) | Aug 18, 2022 |
|  16  |  **GraphSAGE**  | No | 0.4989 ± 0.0678   | 0.4993 ± 0.0676 |[Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/vessel) | 396,289 | Quadro RTX 8000 Ti (48GB GPU) | Aug 20, 2022 |
|  17  |  GCN w/Node2Vec  | No | 0.4954 ± 0.0057   | 0.4960 ± 0.0061 | [Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/vessel) | 226,744,513 | Quadro RTX 8000 Ti (48GB GPU) | Aug 21, 2022 |
|  18  |  **Jaccard Index**  | No | 0.4854 ± 0.0000   | 0.4855 ± 0.0000 |[Mehrdad Rafiepour (University of Kashan)](mailto:mehrdad.rafie.p@gmail.com) | [Paper](https://arxiv.org/abs/2501.06721), [Code](https://github.com/rafiepour/ClusteringEffect) | 0 | CPU (32GB RAM) | Jan 15, 2025 |
|  19  |  Common Neighbors  | No | 0.4849 ± 0.0000   | 0.4850 ± 0.0000 | [Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | Quadro RTX 8000 Ti (48GB GPU) | Aug 20, 2022 |
|  19  |  Adamic Adar  | No | 0.4849 ± 0.0000   | 0.4849 ± 0.0000 | [Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](https://www.cs.toronto.edu/~bor/303s19/docs/adamic-adar.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | Quadro RTX 8000 Ti (48GB GPU) | Aug 20, 2022 |
|  20  |  **MLP**  | No | 0.4794 ± 0.0133   | 0.4801 ± 0.0132 |[Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/vessel) | 1,037,577 | Quadro RTX 8000 Ti (48GB GPU) | Aug 19, 2022 |
|  21  |  GraphSAGE w/Node2VEc  | No | 0.4735 ± 0.0136   | 0.4736 ± 0.0136 | [Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/vessel) | 226,892,737 | Quadro RTX 8000 Ti (48GB GPU) | Aug 21, 2022 |
|  22  |  **Heterogeneity Index**  | No | 0.4540 ± 0.0000   | 0.4541 ± 0.0000 |[Mehrdad Rafiepour (University of Kashan)](mailto:mehrdad.rafie.p@gmail.com) | [Paper](https://arxiv.org/abs/2501.06721), [Code](https://github.com/rafiepour/ClusteringEffect) | 0 | CPU (32GB RAM) | Jan 15, 2025 |
|  23  |  **GCN**  | No | 0.4353 ± 0.0961   | 0.4349 ± 0.0961 |[Julian McGinnis (TUM)](mailto:julian.mcginnis@tum.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/blob/master/examples/linkproppred/vessel) | 396,289 | Quadro RTX 8000 Ti (48GB GPU) | Aug 20, 2022 |





