---
title: Leaderboards for Graph Property Prediction
permalink: /docs/leader_graphprop/
---

##### Check leaderboards for
###### - [ogbg-molhiv](#ogbg-molhiv)
###### - [ogbg-molpcba](#ogbg-molpcba)
###### - [ogbg-ppa](#ogbg-ppa)

**Note:** The **bold** method name indicates that the implementation is **official** (by the author of the original paper).

<a name="ogbg-molhiv"/>

-------------

### Leaderboard for [ogbg-molhiv](../graphprop/#ogbg-mol)

The ROC-AUC score on the test set. The higher, the better. 

| Rank  | Method | ROC-AUC | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  **GIN+virtual node**  | 0.7707 ± 0.0149   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | May 1, 2020 | 
|  2  |  GCN  | 0.7606 ± 0.0097   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | May 1, 2020 | 
|  3  |  GCN+virtual node  | 0.7599 ± 0.0119   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | May 1, 2020 | 
|  4  |  **GIN**  | 0.7558 ± 0.0140   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | May 1, 2020 | 


<a name="ogbg-molpcba"/>

-----------------

### Leaderboard for [ogbg-molpcba](../graphprop/#ogbg-mol)

The PRC-AUC score on the test set. The higher, the better. 

| Rank  | Method | PRC-AUC | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  **GIN+virtual node**  | 0.2655 ± 0.0027   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | May 1, 2020 | 
|  2  |  GCN+virtual node  | 0.2397 ± 0.0023   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | May 1, 2020 | 
|  3  |  **GIN**  | 0.2217 ± 0.0023   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | May 1, 2020 | 
|  4  |  GCN  | 0.1983 ± 0.0016   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | May 1, 2020 | 


<a name="ogbg-ppa"/>

---------------------

### Leaderboard for [ogbg-ppa](../graphprop/#ogbg-ppa)

The multi-class classification accuracy on the test set. The higher, the better. 

| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  **GIN+virtual node**  | 0.7037 ± 0.0107   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | May 1, 2020 | 
|  2  |  **GIN**  | 0.6892 ± 0.0100   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | May 1, 2020 | 
|  3  |  GCN+virtual node  | 0.6857 ± 0.0061   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | May 1, 2020 | 
|  4  |  GCN  | 0.6839 ± 0.0084   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppa) | May 1, 2020 | 
