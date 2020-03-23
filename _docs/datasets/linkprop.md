---
title: Link Property Prediction
permalink: /docs/linkprop/
---

##### The task is to predict properties of edges (pairs of nodes).

### Summary

#### - Datasets

Scale | Name      | #Nodes | #Edges\* | #Task | Split Type   | Task Type     | Metric       |
|------------------|--------|----------|----------|-------------------------------------------------|-----------------------|----------------------------------|----------------|
Small | [ogbl-reviews-groc](#ogbl-reviews)         | 168,816 |    915,088 |     1      | Time  | Link value regression   |     RMSE              |
Medium | [ogbl-reviews-book](#ogbl-reviews) | 2,560,437    | 21,731,986 | 1      |   Time   | Link value regression      |    RMSE         |
Medium | [ogbl-ppa](#ogbl-ppa)         | 576,289 |    21,231,931 |     1      | Throughput  | Link prediction   |     Hits@100              |


\* Note that for undirected graphs, the loaded graphs will have the doubled number of edges becausewe add the bidirectional edges automatically.

#### - Module
We prepare different [data loader](#loader) variants: (1) [Pytorch Geometric one](#pyg) (2) [DGL one](#dgl) and (3) [library-agnostic one](#libagn).
We also prepare a unified [performance evaluator](#eval).

----------

<a name="ogbl-reviews"/>
### Dataset `ogbl-reviews`: ([Leaderboard](../leader_linkprop/#ogbl-reviews))

**Graph:** `ogbl-reviews-groc` and `ogbl-reviews-book` are unweighted bipartite graphs constructed from the "Grocery and Gourmet Food" category and the "Books" category in Amazon Review Data [1,2], respectively. `ogbl-reviews-groc` serves as a small-scale dataset, while `ogbl-reviews-book` is a medium-scale dataset.
Nodes represent either Amazon products or users, where they are associated with 301-dimensional feature vectors. The first dimension indicates whether a given node is a product node or user node: the value of 0 indicates a product node, and 1 indicates a user node. For the next 300 features of the product nodes, we use the Glove vectors [3] averaged over words in the product descriptions. For the user nodes, we simply set the next 300 features to be all-zero.
The edges in the graph represent reviews written by users about products (thus, we have a bipartite graph).
The edges are always between product nodes and user nodes and are assigned integer rating values ranging from 1 to 5.

**Prediction task:** 
The task is to predict the ratings assigned to the edges as accurately as possible, which are measured by the root mean squared error between true ratings and predicted ratings.

**Dataset splitting:** We provide a time split of the edges into training/validation/test edges, meaning that the goal is to use the past ratings to predict future ratings.

#### References

[1] https://nijianmo.github.io/amazon/index.html <br/>
[2] Ni, J., Li, J., & McAuley, J. (2019). Justifying Recommendations using Distantly-Labeled Reviews and Fine-Grained Aspects. EMNLP 2019. <br/>
[3] Pennington, J., Socher, R., & Manning, C. D. (2014). Glove: Global vectors for word representation. EMNLP 2014.

----------

<a name="ogbl-ppa"/>
### Dataset `ogbl-ppa`: ([Leaderboard](../leader_linkprop/#ogbl-ppa))

**Graph:** `ogbl-ppa` is an undirected, unweighted graph. Nodes represent proteins from 58 different species, and edges indicate biologically meaningful associations between proteins (e.g., physical interactions, co-expression, homology, genomic neighborhood) [1]. We provide a graph object constructed from training edges (no validation and test edges are contained). Each node comes with a 58-dimensional one-hot feature indicating which species the corresponding protein comes from. 

**Prediction task:** The task is to predict new association edges given training edges. 

**Dataset splitting:** We provide a biological throughput split of the edges into training/validation/test edges, meaning that the goal is to predict a particular type of protein association (i.e., physical protein-protein interactions) from other types of protein associations (i.e., co-expression, homology, genomic neighborhood, etc.).

- Training edges: A list of edges that are present in the training graph. All the edges have positive labels (indicated by 1).
- Validation and test edges: A list of additional edges for evaluating link prediction models. We include both positive edges (unseen during training) and negative edges (randomly sampled and no overlap with positive edges).

The evaluation is based on how well a model ranks positive test edges higher than negative test edges. This is measured by Hits@100, which ranks each positive edge among all the negative edges and counts the ratio of positive edges that are ranked at 100-th place or above.

#### References

[1] Szklarczyk, D., Gable, A.L., Lyon, D., Junge, A., Wyder, S., Huerta-Cepas, J., Simonovic, M., Doncheva, N.T., Morris, J.H., Bork, P. and Jensen, L.J., 2018. STRING v11: protein–protein association networks with increased coverage, supporting functional discovery in genome-wide experimental datasets. Nucleic Acids Research, 47(D1), pp.D607-D613.

----------

<a name="loader"/>

### Data Loader

To load a dataset, replace `d_name` with the dataset name (e.g., `"ogbl-ppa"`).

<a name="pyg"/>

#### Pytorch Geometric Loader

```python
from ogb.linkproppred import PygLinkPropPredDataset

dataset = PygLinkPropPredDataset(name = d_name) 

splitted_edge = dataset.get_edge_split()
train_edge, train_edge_label = splitted_edge["train_edge"], splitted_edge["train_edge_label"]
valid_edge, valid_edge_label = splitted_edge["valid_edge"], splitted_edge["valid_edge_label"]
test_edge, test_edge_label = splitted_edge["test_edge"], splitted_edge["test_edge_label"]
graph = dataset[0] # pyg graph object containing only training edges
```

<a name="dgl"/>

#### DGL Loader

```python
from ogb.linkproppred import DglLinkPropPredDataset

dataset = DglLinkPropPredDataset(name = d_name)

splitted_edge = dataset.get_edge_split()
train_edge, train_edge_label = splitted_edge["train_edge"], splitted_edge["train_edge_label"]
valid_edge, valid_edge_label = splitted_edge["valid_edge"], splitted_edge["valid_edge_label"]
test_edge, test_edge_label = splitted_edge["test_edge"], splitted_edge["test_edge_label"]
graph = dataset[0] # dgl graph object containing only training edges
```
`{train,valid,edge}_edge` are torch tensors of size `(num_edges,2)`, where each row represents a directed edge, and the first/second column represents the source/sink node indices. 
An undirected graph should include bidirectional edges for each pair of nodes that are connected by an edge. We include the bidirectional edges in the graph object so that messages in GNNs flow in both directions. To keep a low-memory footprint, we did not duplicate edges in `{train,valid,edge}_edge`.
`{train,valid,edge}_edge_label` are torch tensors of length `num_edges`, where the specific shape depends on the dataset at hand. The i-th entry of `{train,valid,edge}_edge_label` corresponds to that of `{train,valid,edge}_edge`, representing some label(s) assigned to the i-th edge.

<a name="libagn"/>

#### Library-Agnostic Loader
```python
from ogb.linkproppred import LinkPropPredDataset

dataset = LinkPropPredDataset(name = d_name)

splitted_edge = dataset.get_edge_split()
train_edge, train_edge_label = splitted_edge["train_edge"], splitted_edge["train_edge_label"]
valid_edge, valid_edge_label = splitted_edge["valid_edge"], splitted_edge["valid_edge_label"]
test_edge, test_edge_label = splitted_edge["test_edge"], splitted_edge["test_edge_label"]
graph = dataset[0] # graph: library-agnostic graph object
```
The library-agnostic graph object is a dictionary containing the following keys: `edge_index`, `edge_feat`, `node_feat`, and `num_nodes`, which are detailed below.
- `edge_index`: numpy arrays of shape `(2, num_edges)`, where each column represents an edge. The first row and the second row represent the indices of source and target nodes. Undirected edges are represented by bi-directional edges.
- `edge_feat`: numpy arrays of shape `(num_edges, edgefeat_dim)`, where `edgefeat_dim` is the dimensionality of edge features and i-th row represents the feature of i-th edge. This can be `None` if no input edge features are available.
- `node_feat`: numpy arrays of shape `(num_nodes, nodefeat_dim)`, where `nodefeat_dim` is the dimensionality of node features and i-th row represents the feature of i-th node. This can be `None` if no input node features are available.
- `num_nodes`: number of nodes in the graph.

----------

<a name="eval"/>

### Performance Evaluator

Evaluators are customized for each dataset.
We require users to pass a pre-specified format to the evaluator.
First, please learn the input and output format specification of the evaluator as follows.

```python
from ogb.linkproppred import Evaluator

evaluator = Evaluator(name = d_name)
print(evaluator.expected_input_format) 
print(evaluator.expected_output_format) 
```

Then, you can pass the input dictionary (denoted by `input_dict` below) of the specified format, and get the performance of your prediction.

```python
# In most cases, input_dict is
# input_dict = {"y_true": y_true, "y_pred": y_pred}
result_dict = evaluator.eval(input_dict)
```

