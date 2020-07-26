---
title: Leaderboards for Graph Property Prediction
permalink: /docs/leader_graphprop/
---

##### Check leaderboards for
###### - [ogbg-molhiv](#ogbg-molhiv)
###### - [ogbg-molpcba](#ogbg-molpcba)
###### - [ogbg-ppa](#ogbg-ppa)
###### - [ogbg-code](#ogbg-code)

The **bold** method name indicates that the implementation is **official** (by the author of the original paper). <br/>
**Package** denotes the required package version for each dataset to be eligible for the leaderboard.

<a name="ogbg-molhiv"/>

-------------

### Leaderboard for [ogbg-molhiv](../graphprop/#ogbg-mol)
##### The ROC-AUC score on the test set. The higher, the better. 

#### Package: >=1.1.1

| Rank  | Method | Test ROC-AUC | Validation ROC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **HIMP**  | 0.7880 ± 0.0082   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2006.12179), [Code](https://github.com/rusty1s/himp-gnn) | 153,029 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  2  |  **DeeperGCN**  | 0.7858 ± 0.0117   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 531,976 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  3  |  **WEGL**  | 0.7757 ± 0.0111   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Navid Naderializadeh](mailto:nnaderializadeh@hrl.com) | [Paper](https://arxiv.org/abs/2006.09430), [Code](https://github.com/navid-naderi/WEGL) | 361,064 | NVIDIA Tesla P100 (16GB GPU) | Jun 26, 2020 |
|  4  |  **GIN+virtual node**  | 0.7707 ± 0.0149   | 0.8479 ± 0.7707 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 3,336,306 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  5  |  GCN  | 0.7606 ± 0.0097   | 0.8204 ± 0.0141 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 527,701 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  6  |  GCN+virtual node  | 0.7599 ± 0.0119   | 0.8384 ± 0.0091 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,978,801 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  7  |  **GIN**  | 0.7558 ± 0.0140   | 0.8232 ± 0.0090 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,885,206 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |


<a name="ogbg-molpcba"/>

-----------------

### Leaderboard for [ogbg-molpcba](../graphprop/#ogbg-mol)
##### The PRC-AUC score on the test set. The higher, the better. 

#### Package: >=1.1.1

| Rank  | Method | Test PRC-AUC | Validation PRC-AUC | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **DeeperGCN+virtual node**  | 0.2745 ± 0.0025   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 5,550,208 | NVIDIA Tesla V100 (32GB GPU) | Jul 12, 2020 |
|  2  |  **HIMP**  | 0.2739 ± 0.0017   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Matthias Fey](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2006.12179), [Code](https://github.com/rusty1s/himp-gnn) | 3,224,534 | GeForce RTX 2080 (11GB GPU) | Jun 22, 2020 |
|  3  |  **GIN+virtual node**  | 0.2655 ± 0.0027   | 0.2754 ± 0.0027 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 3,374,533 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  4  |  GCN+virtual node  | 0.2397 ± 0.0023   | 0.2472 ± 0.0023 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 2,017,028 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  5  |  **GIN**  | 0.2217 ± 0.0023   | 0.2232 ± 0.0023 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 1,923,433 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  6  |  GCN  | 0.1983 ± 0.0016   | 0.2039 ± 0.0030 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | 565,928 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |


<a name="ogbg-ppa"/>

---------------------

### Leaderboard for [ogbg-ppa](../graphprop/#ogbg-ppa)
##### The multi-class classification accuracy on the test set. The higher, the better. 

#### Package: >=1.1.1

| Rank  | Method | Test Accuracy | Validation Accuracy | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **DeeperGCN**  | 0.7712 ± 0.0071   | [Please tell us](mailto:ogb@cs.stanford.edu) |[Guohao Li - DeepGCNs.org](mailto:guohao.li@kaust.edu.sa) | [Paper](https://arxiv.org/abs/2006.07739), [Code](https://github.com/lightaime/deep_gcns_torch/tree/master/examples/ogb) | 2,336,421 | NVIDIA Tesla V100 (32GB GPU) | Jun 16, 2020 |
|  2  |  **GIN+virtual node**  | 0.7037 ± 0.0107   | 0.6678 ± 0.0105 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 3,288,042 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  3  |  **GIN**  | 0.6892 ± 0.0100   | 0.6562 ± 0.0107 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 1,836,942 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  4  |  GCN+virtual node  | 0.6857 ± 0.0061   | 0.6511 ± 0.0048 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 1,930,537 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |
|  5  |  GCN  | 0.6839 ± 0.0084   | 0.6497 ± 0.0034 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | 479,437 | GeForce RTX 2080 (11GB GPU) | May 1, 2020 |



<a name="ogbg-code"/>

---------------------

### Leaderboard for [ogbg-code](../graphprop/#ogbg-code)
##### The F1 score on the test set. The higher, the better. 

#### Package: >=1.2.0

| Rank  | Method | Test F1 score | Validation F1 score | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  GCN+virtual node  | 0.3263 ± 0.0013   | 0.3062 ± 0.0007 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 12,476,210 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  2  |  **GIN+virtual node**  | 0.3204 ± 0.0018   | 0.3020 ± 0.0016 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 13,833,715 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  3  |  GCN  | 0.3163 ± 0.0018   | 0.2973 ± 0.0014 | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 11,025,110 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
|  3  |  **GIN**  | 0.3163 ± 0.0020   | 0.2981 ± 0.0014 |[Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/code) | 12,382,615 | GeForce RTX 2080 (11GB GPU) | Jun 10, 2020 |
