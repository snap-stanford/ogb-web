---
title: Leaderboards for Link Property Prediction
permalink: /docs/leader_linkprop/
---

##### Check leaderboards for
###### - [ogbl-ppa](#ogbl-ppa)
###### - [ogbl-collab](#ogbl-collab)
###### - [ogbl-citation](#ogbl-citation)
###### - [ogbl-wikikg](#ogbl-wikikg)

**Note:** The **bold** method name indicates that the implementation is **official** (by the author of the original paper).


<a name="ogbl-ppa"/>

-------

### Leaderboard for [ogbl-ppa](../linkprop/#ogbl-ppa)
The Hits@100 score on the test set. The higher, the better.

| Rank  | Method | Hits@100 | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  Matrix Factorization  | 0.3229 ± 0.0094   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | May 1, 2020 | 
|  2  |  Node2vec  | 0.2226 ± 0.0083   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | May 1, 2020 | 
|  3  |  GCN  | 0.1155 ± 0.0153   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | May 1, 2020 | 
|  4  |  GraphSAGE  | 0.1063 ± 0.0244   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/ppa) | May 1, 2020 | 




<a name="ogbl-collab"/>

-------

### Leaderboard for [ogbl-collab](../linkprop/#ogbl-collab)
The Hits@10 score on the test set. The higher, the better.

| Rank  | Method | Hits@10 | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  Node2vec  | 0.4281 ± 0.0140   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | May 1, 2020 | 
|  2  |  Matrix Factorization  | 0.3805 ± 0.0018   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | May 1, 2020 | 
|  3  |  GCN  | 0.3329 ± 0.0190   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1609.02907), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | May 1, 2020 | 
|  4  |  GraphSAGE  | 0.3121 ± 0.0620   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1706.02216), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/collab) | May 1, 2020 | 





<a name="ogbl-citation"/>

-------

### Leaderboard for [ogbl-citation](../linkprop/#ogbl-citation)
The MRR score on the test set. The higher, the better.

| Rank  | Method | MRR | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  ClusterGCN (GCN aggr)  | 0.7997 ± 0.0037   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1905.07953), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | May 1, 2020 | 
|  2  |  GraphSAINT (GCN aggr)  | 0.7875 ± 0.0060   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1907.04931), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | May 1, 2020 | 
|  3  |  Matrix Factorization  | 0.6162 ± 0.0012   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/2005.00687), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | May 1, 2020 | 
|  4  |  Node2vec  | 0.5960 ± 0.0013   | [Matthias Fey -- OGB team](mailto:matthias.fey@tu-dortmund.de) | [Paper](https://arxiv.org/abs/1607.00653), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/citation) | May 1, 2020 | 





<a name="ogbl-wikikg"/>

-------

### Leaderboard for [ogbl-wikikg](../linkprop/#ogbl-wikikg)
The MRR score on the test set. The higher, the better.

| Rank  | Method | MRR | Contact | References | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|
|  1  |  ComplEx  | 0.3877 ± 0.0051   | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1606.06357), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | May 1, 2020 | 
|  2  |  DistMult  | 0.3434 ± 0.0079   | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1412.6575), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | May 1, 2020 | 
|  3  |  RotatE  | 0.2681 ± 0.0047   | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://arxiv.org/abs/1902.10197), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | May 1, 2020 | 
|  4  |  TransE  | 0.2535 ± 0.0036   | [Hongyu Ren -- OGB team](mailto:hyren@cs.stanford.edu) | [Paper](https://papers.nips.cc/paper/5071-translating-embeddings-for-modeling-multi-relational-data.pdf), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/linkproppred/wikikg) | May 1, 2020 | 





