---
title: Leaderboards for Link Property Prediction
permalink: /docs/leader_linkprop/
---

##### Check leaderboards for
###### - [ogbl-reviews](#ogbn-reviews)
###### - [ogbl-ppa](#ogbn-ppa)

**Note:** The **bold** method name indicates that the implementation is **official** (by the author of the original paper).

------

<a name="ogbl-reviews"/> 
### Leaderboard for [ogbl-reviews](../linkprop/#ogbl-reviews)
The Root Mean Squared Error (RMSE) on the test set. The lower, the better.

#### ogbl-reviews-groc

| Rank  | Method | RMSE | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  Matrix Factorization  | 1.1455 ± 0.0018   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://datajobs.com/data-science-repo/Recommender-Systems-[Netflix].pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/reviews) | Mar 20, 2020 | 



#### ogbl-reviews-book

| Rank  | Method | RMSE | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  Matrix Factorization  | 0.9190 ± 0.0010   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://datajobs.com/data-science-repo/Recommender-Systems-[Netflix].pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/reviews) | Mar 20, 2020 | 


-------

<a name="ogbl-ppa"/>
### Leaderboard for [ogbl-ppa](../linkprop/#ogbl-ppa)
The Hits@100 score on the test set. The higher, the better.

| Rank  | Method | Hits@100 | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  Matrix Factorization  | 0.3229 ± 0.0094   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://datajobs.com/data-science-repo/Recommender-Systems-[Netflix].pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | Mar 20, 2020 | 

