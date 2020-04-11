---
title: Leaderboards for Graph Property Prediction
permalink: /docs/leader_graphprop/
---

##### Check leaderboards for
###### - [ogbg-molhiv](#ogbg-molhiv)
###### - [ogbg-molpcba](#ogbg-molpcba)
###### - [ogbg-ppi](#ogbg-ppi)

**Note:** The **bold** method name indicates that the implementation is **official** (by the author of the original paper).

<a name="ogbg-molhiv"/>

-------------

### Leaderboard for [ogbg-molhiv](../graphprop/#ogbg-mol)

The ROC-AUC score on the test set. The higher, the better. 

| Rank  | Method | ROC-AUC | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  **GIN+virtual node**  | 0.7707 ± 0.0149   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | Mar 20, 2020 | 
|  2  |  **GIN**  | 0.7558 ± 0.0140   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | Mar 20, 2020 | 


<a name="ogbg-molpcba"/>

-----------------

### Leaderboard for [ogbg-molpcba](../graphprop/#ogbg-mol)

The PRC-AUC score on the test set. The higher, the better. 

| Rank  | Method | ROC-AUC | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  **GIN+virtual node**  | 0.2655 ± 0.0027   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | Mar 20, 2020 | 
|  2  |  **GIN**  | 0.2217 ± 0.0023   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/mol) | Mar 20, 2020 | 


<a name="ogbg-ppi"/>

---------------------

### Leaderboard for [ogbg-ppi](../graphprop/#ogbg-ppi)

The multi-class classification accuracy on the test set. The higher, the better. 

| Rank  | Method | Accuracy | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  **GIN+virtual node**  | 0.7037 ± 0.0107   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppi) | Mar 20, 2020 | 
|  2  |  **GIN**  | 0.6892 ± 0.0100   | [Weihua Hu -- OGB team](mailto:weihuahu@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1810.00826), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/graphproppred/ppi) | Mar 20, 2020 | 
