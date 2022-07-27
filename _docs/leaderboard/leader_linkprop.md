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
|  1  |  **RA+Edge Proposal Set**  | No | 0.5324 ± 0.0000   | 0.5142 ± 0.0000 |[Qian Huang (Stanford)](mailto:qhwang@stanford.edu) | [Paper](https://arxiv.org/abs/2106.15810), [Code](https://github.com/CUAI/Edge-Proposal-Sets) | 0 | GeForce RTX 2080 Ti (11GB GPU) | Oct 5, 2021 |
|  2  |  **MLP+CN&RA&AA**  | No | 0.5062 ± 0.0035   | 0.4906 ± 0.0029 |[Shitao Lu](mailto:lusto32768@gmail.com) | [Paper](https://github.com/lustoo/OGB_link_prediction/blob/main/Link%20prediction%20with%20structural%20information.pdf), [Code](https://github.com/lustoo/OGB_link_prediction) | 163,330 | Geforce GTX 1080 Ti (11GB) | Aug 9, 2021 |
|  3  |  Resource Allocation  | No | 0.4933 ± 0.0000   | 0.4722 ± 0.0000 | [Shen Fan(Alibaba Group)](mailto:ofanshen@gmail.com) | [Paper](https://arxiv.org/pdf/0901.0553.pdf), [Code](https://github.com/fs302/EasyLink/blob/main/example/ogbl_ppa_ra.py) | 0 | Tesla-V100(32GB GPU) | Jul 5, 2021 |
|  4  |  **SEAL**  | No | 0.4880 ± 0.0316   | 0.5125 ± 0.0252 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 709,122 | GeForce RTX 2080S (8GB GPU) | Oct 14, 2020 |
|  5  |  Adamic Adar  | No | 0.3245 ± 0.0000   | 0.3268 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.1370&rep=rep1&type=pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  6  |  Matrix Factorization  | No | 0.3229 ± 0.0094   | 0.3228 ± 0.0428 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 147,662,849 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  7  |  DeepWalk  | No | 0.2888 ± 0.0153   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 150,138,741 | g4dn.2xlarge, T4 (15GB GPU) | Jul 23, 2020 |
|  8  |  Common Neighbor  | No | 0.2765 ± 0.0000   | 0.2823 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  9  |  DeepWalk  | No | 0.2302 ± 0.0163   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 150,138,741 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  10  |  Node2vec  | No | 0.2226 ± 0.0083   | 0.2253 ± 0.0088 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 73,878,913 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  11  |  GCN  | No | 0.1867 ± 0.0132   | 0.1845 ± 0.0140 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 278,529 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  12  |  GraphSAGE  | No | 0.1655 ± 0.0240   | 0.1724 ± 0.0264 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | 424,449 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |




<a name="ogbl-collab"/>

-------

### Leaderboard for [ogbl-collab](../linkprop/#ogbl-collab)
##### The Hits@50 score on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Ext. data | Test Hits@50 | Validation Hits@50 | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **PLNLP + SIGN**  | No | 0.7087 ± 0.0033   | 1.0000 ± 0.0000 |[Liang Yao (Tencent)](mailto:dryao@tencent.com) | [Paper](https://github.com/yao8839836/ogb_report/blob/main/ogb_report.pdf), [Code](https://github.com/yao8839836/ogb_report) | 34,980,864 | Tesla-P40 (24G GPU) | Apr 7, 2022 |
|  2  |  **PLNLP (random walk aug.)**  | No | 0.7059 ± 0.0029   | 1.0000 ± 0.0000 |[Zhitao Wang (WeChat@Tencent)](mailto:wztzenk@gmail.com) | [Paper](https://arxiv.org/abs/2112.02936), [Code](https://github.com/zhitao-wang/PLNLP) | 34,980,864 | Tesla-P40 (24G GPU) | Dec 21, 2021 |
|  3  |  **HOP-REC**  | No | 0.7012 ± 0.0016   | 1.0000 ± 0.0000 |[Bo-Yu Lin (CFDA & CLIP Labs)](mailto:sofar106703046@gmail.com) | [Paper](https://dl.acm.org/doi/10.1145/3240323.3240381), [Code](https://github.com/brucenccu/OGB_collab_project) | 30,191,104 | CPU | Oct 21, 2021 |
|  4  |  PLNLP+ LRGA  | No | 0.6909 ± 0.0055   | 1.0000 ± 0.0000 | [Hao Xu](mailto:kingsleyhsu1@gmail.com) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/KingsleyHsu/OGB-LPP) | 35,200,656 | NVIDIA Tesla V100 (32GB GPU) | Jun 26, 2022 |
|  5  |  **PLNLP (val as input)**  | No | 0.6872 ± 0.0052   | 1.0000 ± 0.0000 |[Zhitao Wang (WeChat@Tencent)](mailto:wztzenk@gmail.com) | [Paper](https://arxiv.org/pdf/2112.02936.pdf), [Code](https://github.com/zhitao-wang/PLNLP) | 35,112,192 | Tesla-P40 (24G GPU) | Dec 7, 2021 |
|  6  |  **Adamic Adar+Edge Proposal Set**  | No | 0.6548 ± 0.0000   | 0.9735 ± 0.0000 |[Qian Huang (Cornell University)](mailto:qh53@cornell.edu) | [Paper](https://arxiv.org/pdf/2106.15810.pdf), [Code](https://github.com/CUAI/Edge-Proposal-Sets) | 0 | GeForce RTX 2080 Ti (11GB GPU) | Jul 13, 2021 |
|  7  |  **SEAL-nofeat (val as input)**  | No | 0.6474 ± 0.0043   | 0.6495 ± 0.0043 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 501,570 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2021 |
|  8  |  Adamic Adar  | No | 0.6417 ± 0.0000   | 0.6349 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.1370&rep=rep1&type=pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  9  |  Common Neighbor  | No | 0.6137 ± 0.0000   | 0.6036 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  10  |  **SEAL-nofeat**  | No | 0.5471 ± 0.0049   | 0.6495 ± 0.0043 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 501,570 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2021 |
|  11  |  GraphSAGE  (val as input)  | No | 0.5463 ± 0.0112   | 0.5688 ± 0.0077 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 460,289 | GeForce RTX 2080 (11GB GPU) | Oct 19, 2020 |
|  12  |  **DeeperGCN**  | No | 0.5273 ± 0.0047   | 0.6187 ± 0.0045 |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 117,383 | NVIDIA Tesla V100 (32GB GPU) | Oct 21, 2020 |
|  13  |  **LRGA + GCN**  | No | 0.5221 ± 0.0072   | 0.6088 ± 0.0059 |[Omri Puny](mailto:omri.puny@weizmann.ac.il) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/omri1348/LRGA/tree/master/ogb/examples/linkproppred) | 1,069,489 | Tesla P100 (16GB GPU) | Aug 5, 2020 |
|  14  |  DeepWalk  | No | 0.5037 ± 0.0034   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 61,390,187 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  15  |  Node2vec  | No | 0.4888 ± 0.0054   | 0.5703 ± 0.0052 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 30,322,945 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  16  |  GraphSAGE  | No | 0.4810 ± 0.0081   | 0.5688 ± 0.0077 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 460,289 | GeForce RTX 2080 (11GB GPU) | Jun 24, 2020 |
|  17  |  GCN (val as input)  | No | 0.4714 ± 0.0145   | 0.5263 ± 0.0115 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 296,449 | GeForce RTX 2080 (11GB GPU) | Oct 19, 2020 |
|  18  |  GCN  | No | 0.4475 ± 0.0107   | 0.5263 ± 0.0115 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jun 24, 2020 |
|  19  |  Matrix Factorization  | No | 0.3886 ± 0.0029   | 0.4896 ± 0.0029 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | 60,514,049 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |




<a name="ogbl-ddi"/>

-------

### Leaderboard for [ogbl-ddi](../linkprop/#ogbl-ddi)
##### The Hits@20 score on the test and validation sets. The higher, the better.

#### Package: >=1.2.1

| Rank  | Method | Ext. data | Test Hits@20 | Validation Hits@20 | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **PLNLP**  | No | 0.9088 ± 0.0313   | 0.8242 ± 0.0253 |[Zhitao Wang (WeChat@Tencent)](mailto:wztzenk@gmail.com) | [Paper](https://arxiv.org/abs/2112.02936), [Code](https://github.com/zhitao-wang/PLNLP) | 3,497,473 | Tesla-P40(24GB GPU) | Dec 7, 2021 |
|  2  |  **GraphSAGE + Edge Attr**  | No | 0.8781 ± 0.0474   | 0.8044 ± 0.0404 |[Jing Yang](mailto:jyangboston@gmail.com) | [Paper](https://github.com/lustoo/OGB_link_prediction/blob/main/Link%20prediction%20with%20structural%20information.pdf), [Code](https://github.com/lustoo/OGB_link_prediction) | 3,761,665 | Tesla V100 (32GB) | Aug 9, 2021 |
|  3  |  **CFLP (w/ JKNet)**  | No | 0.8608 ± 0.0198   | 0.8405 ± 0.0284 |[Tong Zhao](mailto:tzhao2@nd.edu) | [Paper](https://arxiv.org/pdf/2106.02172.pdf), [Code](https://github.com/DM2-ND/CFLP) | 837,635 | GeForce RTX 2080 Ti (11GB GPU) | Nov 17, 2021 |
|  3  |  **CFLP (w/ JKNet)**  | No | 0.8608 ± 0.0198   | 0.8405 ± 0.0284 |[Tong Zhao (University of Notre Dame)](mailto:tzhao2@nd.edu) | [Paper](https://arxiv.org/pdf/2106.02172.pdf), [Code](https://github.com/DM2-ND/CFLP) | 837,635 | GeForce RTX 2080 Ti (11GB GPU) | Nov 17, 2021 |
|  4  |  **GraphSAGE+anchor distance**  | No | 0.8239 ± 0.0437   | 0.8206 ± 0.0298 |[Boning Li (SJTU)](mailto:lbn187@sjtu.edu.cn) | [Paper](https://www.dropbox.com/s/is3f4dfvtvnis7w/DEGNN_linkPrediction.pdf?dl=0), [Code](https://github.com/lbn187/DLGNN) | 3,760,134 | Tesla V100 (16GB GPU) | May 20, 2021 |
|  5  |  DEA + JKNet  | No | 0.7672 ± 0.0265   | 0.6713 ± 0.0071 | [Yichen Yang](mailto:jeffrey576826145@outlook.com) | [Paper](https://github.com/JeffJeffy/CS224W-OGB-DEA-JK/blob/main/CS224w_final_report.pdf), [Code](https://github.com/JeffJeffy/CS224W-OGB-DEA-JK) | 1,763,329 | Tesla T4 (16GB GPU) | Mar 21, 2021 |
|  6  |  **GraphSAGE+Edge Proposal Set**  | No | 0.7495 ± 0.0317   | 0.6696 ± 0.0198 |[Qian Huang (Cornell University)](mailto:qh53@cornell.edu) | [Paper](https://arxiv.org/pdf/2106.15810.pdf), [Code](https://github.com/CUAI/Edge-Proposal-Sets) | 1,421,057 | GeForce RTX 2080 Ti (11GB GPU) | Jul 21, 2021 |
|  7  |  LRGA+GCN(Node2Vec+Augment)  | No | 0.7385 ± 0.0871   | 0.7225 ± 0.0047 | [Chuanqi Chen](mailto:chuanqi.chen@gmail.com) | [Paper](https://github.com/chuanqichen/cs224w/blob/main/the_study_of_drug_drug_interaction_learning_through_various_graph_learning_methods.pdf), [Code](https://github.com/chuanqichen/cs224w) | 10,235,281 | Tesla V100 (32GB) | Mar 21, 2021 |
|  8  |  **MAD Learning**  | No | 0.6781 ± 0.0294   | 0.7010 ± 0.0082 |[Yi Luo](mailto:cf020031308@163.com) | [Paper](https://arxiv.org/abs/2102.05246), [Code](https://github.com/cf020031308/mad-learning/blob/master/ogbl-ddi.py) | 1,228,897 | Geforce GTX 1080 Ti (11GB GPU) | Feb 10, 2021 |
|  9  |  **LRGA + GCN**  | No | 0.6230 ± 0.0912   | 0.6675 ± 0.0058 |[Omri Puny](mailto:omri.puny@weizmann.ac.il) | [Paper](https://arxiv.org/abs/2006.07846), [Code](https://github.com/omri1348/LRGA/tree/master/ogb/examples/linkproppred) | 1,576,081 | Tesla P100 (16GB GPU) | Aug 5, 2020 |
|  10  |  GCN+JKNet  | No | 0.6056 ± 0.0869   | 0.6776 ± 0.0095 | [Horace He  (Cornell)](mailto:hh498@cornell.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/Chillee/ogb_ddi) | 1,421,571 | Geforce GTX 1080 Ti (11GB GPU) | Sep 15, 2020 |
|  11  |  GraphSAGE  | No | 0.5390 ± 0.0474   | 0.6262 ± 0.0037 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,421,057 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  12  |  GCN  | No | 0.3707 ± 0.0507   | 0.5550 ± 0.0208 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,289,985 | GeForce RTX 2080 (11GB GPU) | Jun 25, 2020 |
|  13  |  **SEAL**  | No | 0.3056 ± 0.0386   | 0.2849 ± 0.0269 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 531,138 | GeForce RTX 2080S (8GB GPU) | Oct 14, 2020 |
|  14  |  DeepWalk  | No | 0.2642 ± 0.0610   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 11,543,913 | g4dn.2xlarge, T4 (15GB GPU) | Jul 23, 2020 |
|  15  |  Node2vec  | No | 0.2326 ± 0.0209   | 0.3292 ± 0.0121 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 645,249 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  16  |  DeepWalk  | No | 0.2246 ± 0.0290   | [Please tell us](mailto:ogb@cs.stanford.edu) | [Hao Xiong (DGL)](mailto:taxuexh@sjtu.edu.cn) | [Paper](https://arxiv.org/pdf/1403.6652.pdf), [Code](https://github.com/dmlc/dgl/tree/master/examples/pytorch/ogb/deepwalk) | 1,543,913 | g4dn.2xlarge, T4 (15GB GPU) | Jun 30, 2020 |
|  17  |  Adamic Adar  | No | 0.1861 ± 0.0000   | 0.0966 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.1370&rep=rep1&type=pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  18  |  Common Neighbor  | No | 0.1773 ± 0.0000   | 0.0947 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  19  |  Matrix Factorization  | No | 0.1368 ± 0.0475   | 0.3370 ± 0.0264 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ddi) | 1,224,193 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |




<a name="ogbl-citation2"/>

-------

### Leaderboard for [ogbl-citation2](../linkprop/#ogbl-citation2)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.4
###### Deprecated `ogbl-citation` leaderboard can be found [here](../leader_deprecated/#ogbl-citation).

| Rank  | Method | Ext. data | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **SUREL**  | No | 0.8883 ± 0.0018   | 0.8891 ± 0.0021 |[Haoteng Yin (Purdue University)](mailto:yinht@purdue.edu) | [Paper](https://arxiv.org/abs/2202.13538), [Code](https://github.com/Graph-COM/SUREL) | 79,617 | Quadro RTX 6000 | Mar 18, 2022 |
|  2  |  **SEAL**  | No | 0.8767 ± 0.0032   | 0.8757 ± 0.0031 |[Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://arxiv.org/pdf/2010.16103.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 260,802 | Tesla V100 (32GB GPU) | Feb 12, 2021 |
|  3  |  **PLNLP**  | No | 0.8492 ± 0.0029   | 0.8490 ± 0.0031 |[Zhitao Wang (WeChat@Tencent)](mailto:wztzenk@gmail.com) | [Paper](https://arxiv.org/pdf/2112.02936.pdf), [Code](https://github.com/zhitao-wang/PLNLP) | 146,514,551 | Tesla-V100 (32G GPU) | Dec 7, 2021 |
|  4  |  Full-batch GCN  | No | 0.8474 ± 0.0021   | 0.8479 ± 0.0023 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | Quadro RTX 8000 (48GB GPU) | Jan 4, 2021 |
|  5  |  **HPE - Pre-trained Initialized**  | No | 0.8432 ± 0.0003   | 0.8422 ± 0.0002 |[Chi-Hung Chang (CFDA & CLIP Labs)](mailto:chihung861224@gmail.com) | [Paper](https://dl.acm.org/doi/10.1145/2959100.2959169), [Code](https://github.com/chang861224/HPE_OGB) | 749,558,528 | CPU | Dec 7, 2021 |
|  6  |  Full-batch GraphSAGE  | No | 0.8260 ± 0.0036   | 0.8263 ± 0.0033 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 460,289 | Quadro RTX 8000 (48GB GPU) | Jan 4, 2021 |
|  7  |  NeighborSampling (SAGE aggr)  | No | 0.8044 ± 0.0010   | 0.8054 ± 0.0009 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 460,289 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  8  |  ClusterGCN (GCN aggr)  | No | 0.8004 ± 0.0025   | 0.7994 ± 0.0025 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  9  |  GraphSAINT (GCN aggr)  | No | 0.7985 ± 0.0040   | 0.7975 ± 0.0039 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 296,449 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  10  |  Node2vec  | No | 0.6141 ± 0.0011   | 0.6124 ± 0.0011 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 374,911,105 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  11  |  Adamic Adar  | No | 0.5189 ± 0.0000   | 0.5167 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.1370&rep=rep1&type=pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |
|  12  |  Matrix Factorization  | No | 0.5186 ± 0.0443   | 0.5181 ± 0.0436 | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation2) | 281,113,505 | GeForce RTX 2080 (11GB GPU) | Jan 4, 2021 |
|  13  |  Common Neighbor  | No | 0.5147 ± 0.0000   | 0.5119 ± 0.0000 | [Muhan Zhang](mailto:muhan.zhang@hotmail.com) | [Paper](http://www.eecs.harvard.edu/~michaelm/CS222/linkpred.pdf), [Code](https://github.com/facebookresearch/SEAL_OGB) | 0 | GeForce RTX 2080S (8GB GPU) | Feb 12, 2021 |



<a name="ogbl-wikikg2"/>

-------

### Leaderboard for [ogbl-wikikg2](../linkprop/#ogbl-wikikg2)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.4
###### Deprecated `ogbl-wikikg` leaderboard can be found [here](../leader_deprecated/#ogbl-wikikg).

| Rank  | Method | Ext. data | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **AutoWeird**  | No | 0.7353 ± 0.0006   | 0.7362 ± 0.0006 |[Hansi Yang (HKUST & 4Paradigm & EE, THU)](mailto:hyangbw@cse.ust.hk) | [Paper](https://arxiv.org/abs/2207.11673), [Code](https://github.com/jerermyyoung/AutoWeird) | 19,215,402 | GeForce RTX 3090 (24GB GPU) | Jul 27, 2022 |
|  2  |  **StarGraph + TripleRE**  | No | 0.7201 ± 0.0011   | 0.7288 ± 0.0008 |[Hongzhu Li (360AI)](mailto:lihongzhu@360.cn) | [Paper](https://arxiv.org/abs/2205.14209), [Code](https://github.com/hzli-ucas/StarGraph) | 86,762,146 | Tesla A100(40GB) | May 30, 2022 |
|  3  |  **TranS**  | No | 0.6939 ± 0.0011   | 0.7058 ± 0.0018 |[Xuanyu Zhang (DXM AI)](mailto:xuanyuzhang94@gmail.com) | [Paper](https://arxiv.org/abs/2204.08401), [Code](https://github.com/xyznlp/trans) | 38,430,804 | Tesla V100 (16GB) | Apr 19, 2022 |
|  4  |  **TranS**  | No | 0.6882 ± 0.0019   | 0.6988 ± 0.0006 |[Xuanyu Zhang (DXM AI)](mailto:xuanyuzhang94@gmail.com) | [Paper](https://arxiv.org/abs/2204.08401), [Code](https://github.com/xyznlp/trans) | 19,215,402 | Tesla V100 (16GB) | Apr 28, 2022 |
|  5  |  **TripleRE + NodePiece**  | No | 0.6866 ± 0.0014   | 0.6955 ± 0.0008 |[Long Yu (360AI)](mailto:yulong_i@163.com) | [Paper](https://vixra.org/abs/2112.0095), [Code](https://github.com/LongYu-360/TripleRE-Add-NodePiece-v2) | 36,421,802 | Tesla A100(40GB) | Feb 24, 2022 |
|  6  |  **InterHT**  | No | 0.6779 ± 0.0018   | 0.6893 ± 0.0015 |[Baoxin Wang (HFL)](mailto:destin.bxwang@gmail.com) | [Paper](https://arxiv.org/abs/2202.04897), [Code](https://github.com/destwang/InterHT) | 19,215,402 | Tesla V100 (32GB) | Feb 10, 2022 |
|  7  |  **TripleRE + NodePiece**  | No | 0.6582 ± 0.0020   | 0.6616 ± 0.0018 |[Long Yu (360AI)](mailto:yulong_i@163.com) | [Paper](https://vixra.org/abs/2112.0095), [Code](https://github.com/LongYu-360/TripleRE-Add-NodePiece) | 7,289,002 | Tesla A100(40GB) | Dec 25, 2021 |
|  8  |  **ComplEx-RP (50dim)**  | No | 0.6392 ± 0.0045   | 0.6561 ± 0.0070 |[Yihong Chen (UCL NLP & FAIR London)](mailto:yihong.chen@cs.ucl.ac.uk) | [Paper](https://openreview.net/pdf?id=Qa3uS3H7-Le), [Code](https://github.com/facebookresearch/ssl-relation-prediction) | 250,167,400 | Tesla V100 (32GB) | Nov 23, 2021 |
|  9  |  **tripleRE**  | No | 0.5794 ± 0.0020   | 0.6045 ± 0.0024 |[Long Yu (360AI)](mailto:yulong_i@163.com) | [Paper](https://vixra.org/abs/2112.0095), [Code](https://github.com/LongYu-360/TripleRE) | 500,763,337 | Tesla P40(24GB) | Dec 17, 2021 |
|  10  |  **NodePiece + AutoSF**  | No | 0.5703 ± 0.0035   | 0.5806 ± 0.0047 |[Mikhail Galkin (Mila)](mailto:mikhail.galkin@mila.quebec) | [Paper](https://arxiv.org/abs/2106.12144), [Code](https://github.com/migalkin/NodePiece/tree/main/ogb) | 6,860,602 | Tesla V100 (32 GB) | Jul 17, 2021 |
|  11  |  **AutoSF**  | No | 0.5458 ± 0.0052   | 0.5510 ± 0.0063 |[Yongqi Zhang (4Paradigm)](mailto:zhangyongqi@4paradigm.com) | [Paper](https://arxiv.org/pdf/1904.11682.pdf), [Code](https://github.com/AutoML-4Paradigm/AutoSF/tree/AutoSF-OGB) | 500,227,800 | Quadro RTX 8000 (45GB GPU) | Apr 2, 2021 |
|  12  |  **PairRE (200dim)**  | No | 0.5208 ± 0.0027   | 0.5423 ± 0.0020 |[Linlin Chao](mailto:chulin.cll@antgroup.com) | [Paper](https://arxiv.org/abs/2011.03798), [Code](https://github.com/alipay/KnowledgeGraphEmbeddingsViaPairedRelationVectors_PairRE) | 500,334,800 | Tesla P100 (16GB GPU) | Jan 28, 2021 |
|  13  |  RotatE (250dim)  | No | 0.4332 ± 0.0025   | 0.4353 ± 0.0028 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,435,750 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  14  |  TransE (500dim)  | No | 0.4256 ± 0.0030   | 0.4272 ± 0.0030 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  15  |  ComplEx (250dim)  | No | 0.4027 ± 0.0027   | 0.3759 ± 0.0016 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  16  |  ComplEx (50dim)  | No | 0.3804 ± 0.0022   | 0.3534 ± 0.0052 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  17  |  DistMult (500dim)  | No | 0.3729 ± 0.0045   | 0.3506 ± 0.0042 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 1,250,569,500 | Quadro RTX 8000 (45GB GPU) | Jan 23, 2021 |
|  18  |  DistMult (100dim)  | No | 0.3447 ± 0.0082   | 0.3150 ± 0.0088 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  19  |  TransE (100dim)  | No | 0.2622 ± 0.0045   | 0.2465 ± 0.0020 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,113,900 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |
|  20  |  RotatE (50dim)  | No | 0.2530 ± 0.0034   | 0.2250 ± 0.0035 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg2) | 250,087,150 | GeForce RTX 2080 (11GB GPU) | Jan 23, 2021 |


<a name="ogbl-biokg"/>

-------

### Leaderboard for [ogbl-biokg](../linkprop/#ogbl-biokg)
##### The MRR score on the test and validation sets. The higher, the better.

#### Package: >=1.2.0

| Rank  | Method | Ext. data | Test MRR | Validation MRR | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **AutoBLM-KGBench**  | No | 0.8536 ± 0.0003   | 0.8548 ± 0.0002 |[Yongqi Zhang (4Paradigm && EE Tsinghua)](mailto:zhangyongqi@4paradigm.com) | [Paper](https://arxiv.org/pdf/2107.00184.pdf), [Code](https://github.com/AutoML-Research/KGBench) | 192,047,104 | Tesla A100 (80G) | Jun 17, 2022 |
|  2  |  **ComplEx-RP (1000dim)**  | No | 0.8492 ± 0.0002   | 0.8497 ± 0.0002 |[Yihong Chen (UCL NLP & FAIR London)](mailto:yihong.chen@cs.ucl.ac.uk) | [Paper](https://openreview.net/pdf?id=Qa3uS3H7-Le), [Code](https://github.com/facebookresearch/ssl-relation-prediction) | 187,750,000 | Tesla V100 (16GB) | Nov 23, 2021 |
|  3  |  **TripleRE**  | No | 0.8348 ± 0.0007   | 0.8360 ± 0.0006 |[LongYu(360AI)](mailto:yulong_i@163.com) | [Paper](https://vixra.org/abs/2112.0095), [Code](https://github.com/LongYu-360/TripleRE-biokg) | 469,630,002 | Tesla A100(40GB) | Jan 28, 2022 |
|  4  |  **AutoSF**  | No | 0.8309 ± 0.0008   | 0.8317 ± 0.0007 |[Yongqi Zhang (4Paradigm)](mailto:zhangyongqi@4paradigm.com) | [Paper](https://arxiv.org/pdf/1904.11682.pdf), [Code](https://github.com/AutoML-4Paradigm/AutoSF/tree/AutoSF-OGB) | 93,824,000 | GeForce RTX 2080 (11GB GPU) | Apr 2, 2021 |
|  5  |  **PairRE**  | No | 0.8164 ± 0.0005   | 0.8172 ± 0.0005 |[LinlinChao (AntGroup KG&NLP)](mailto:chulin.cll@antgroup.com) | [Paper](https://arxiv.org/abs/2011.03798), [Code](https://github.com/alipay/KnowledgeGraphEmbeddingsViaPairedRelationVectors_PairRE) | 187,750,000 | Tesla P100 (16GB GPU) | Nov 9, 2020 |
|  6  |  ComplEx  | No | 0.8095 ± 0.0007   | 0.8105 ± 0.0001 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  7  |  DistMult  | No | 0.8043 ± 0.0003   | 0.8055 ± 0.0003 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  8  |  RotatE  | No | 0.7989 ± 0.0004   | 0.7997 ± 0.0002 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,597,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  9  |  TransE  | No | 0.7452 ± 0.0004   | 0.7456 ± 0.0003 | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/biokg) | 187,648,000 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |


<a name="ogbl-vessel/>

-------

### Leaderboard for [ogbl-vessel](../linkprop/#ogbl-vessel)
##### The ROC-AUC score on the test and validation sets. The higher, the better.

#### Package: >=1.3.4

| Rank  | Method | Test ROC-AUC | Validation ROC-AUC | Contact | References | #Params | Hardware | Date 





