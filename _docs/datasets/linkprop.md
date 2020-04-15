---
title: Link Property Prediction
permalink: /docs/linkprop/
---

##### The task is to predict properties of edges (pairs of nodes).

### Summary

#### - Datasets

##### **The current datasets are subject to change until the paper is released (expected to be around mid April).**

Scale | Name      | #Nodes | #Edges\* | #Task | Split Type   | Task Type     | Metric       |
|------------------|--------|----------|----------|-------------------------------------------------|-----------------------|----------------------------------|----------------|
Medium | [ogbl-ppa](#ogbl-ppa)         | 576,289 |    21,231,931 |     1      | Throughput  | Link prediction   |     Hits@100              |


**Note:** For undirected graphs, the loaded graphs will have the doubled number of edges because we add the bidirectional edges automatically.

#### - Module
We prepare different [data loader](#loader) variants: (1) [Pytorch Geometric one](#pyg) (2) [DGL one](#dgl) and (3) [library-agnostic one](#libagn).
We also prepare a unified [performance evaluator](#eval).

<a name="ogbl-ppa"/>

----------

### Dataset `ogbl-ppa` ([Leaderboard](../leader_linkprop/#ogbl-ppa)):

**Graph:** `ogbl-ppa` is an undirected, unweighted graph. Nodes represent proteins from 58 different species, and edges indicate biologically meaningful associations between proteins, e.g., physical interactions, co-expression, homology or genomic neighborhood [1]. We provide a graph object constructed from training edges (no validation and test edges are contained). Each node contains a 58-dimensional one-hot feature vector that indicates the species that the corresponding protein comes from.

**Prediction task:** The task is to predict new association edges given the training edges.
The evaluation is based on how well a model ranks positive test edges over negative test edges.
Specifically, we rank each positive edge in the validation/test set against 3,000,000 randomly-sampled negative edges, and count the ratio of positive edges that are ranked at 100-th place or above (Hits@100). 

**Dataset splitting:** We provide a biological throughput split of the edges into training/validation/test edges.
Training edges are known *non*-physical protein associations, and validation/test edges denote physical protein association.
In particular, the goal is to predict a particular type of protein association, i.e., physical protein-protein interaction, from other types of *non*-physical protein associations (e.g., co-expression, homology, or genomic neighborhood) that are known to be strongly correlated with the physical associations that we are interested in.

The following summarizes the traing/validation/test edges that we provide.

- Training edges: A list of edges that are present in the training graph. All the edges have positive labels (indicated by 1).
- Validation and test edges: A list of additional edges for evaluating link prediction models. We include both positive edges (indicated by 1, unseen during training) and negative edges (indicated by 0, randomly sampled and no overlap with the positive edges).


#### References

[1] Szklarczyk, D., Gable, A.L., Lyon, D., Junge, A., Wyder, S., Huerta-Cepas, J., Simonovic, M., Doncheva, N.T., Morris, J.H., Bork, P. and Jensen, L.J., 2018. STRING v11: protein–protein association networks with increased coverage, supporting functional discovery in genome-wide experimental datasets. Nucleic Acids Research, 47(D1), pp.D607-D613.

<a name="loader"/>

----------

### Data Loader

To load a dataset, replace `d_name` with the dataset name (e.g., `"ogbl-ppa"`).

<a name="pyg"/>

#### Pytorch Geometric Loader

```python
from ogb.linkproppred import PygLinkPropPredDataset

dataset = PygLinkPropPredDataset(name = d_name) 

splitted_edge = dataset.get_edge_split()
train_edge, valid_edge, test_edge = splitted_edge["train"], splitted_edge["valid"], splitted_edge["test"]
graph = dataset[0] # pyg graph object containing only training edges
```

<a name="dgl"/>

#### DGL Loader

```python
from ogb.linkproppred import DglLinkPropPredDataset

dataset = DglLinkPropPredDataset(name = d_name)

splitted_edge = dataset.get_edge_split()
train_edge, valid_edge, test_edge = splitted_edge["train"], splitted_edge["valid"], splitted_edge["test"]
graph = dataset[0] # dgl graph object containing only training edges
```
`{train,valid,edge}_edge` contains the splitting of edges whose format is dataset-dependent. For instance, it can be a dictionary containing positive and negative edges. For KG, it is a dictionary containing three keys: `head`, `relation`, and `tail`, and i-th triplet in KG is simply i-th elements of `head`, `relation`, and `tail`.
An undirected graph should include bidirectional edges for each pair of nodes that are connected by an edge. We include the bidirectional edges in the graph object so that messages in GNNs flow in both directions. To keep a low-memory footprint, we did not duplicate edges in `{train,valid,edge}_edge`.

<a name="libagn"/>

#### Library-Agnostic Loader
```python
from ogb.linkproppred import LinkPropPredDataset

dataset = LinkPropPredDataset(name = d_name)

splitted_edge = dataset.get_edge_split()
train_edge, valid_edge, test_edge = splitted_edge["train"], splitted_edge["valid"], splitted_edge["test"]
graph = dataset[0] # graph: library-agnostic graph object
```
The library-agnostic graph object is a dictionary containing the following keys: `edge_index`, `edge_feat`, `node_feat`, and `num_nodes`, which are detailed below.
- `edge_index`: numpy arrays of shape `(2, num_edges)`, where each column represents an edge. The first row and the second row represent the indices of source and target nodes. Undirected edges are represented by bi-directional edges.
- `edge_feat`: numpy arrays of shape `(num_edges, edgefeat_dim)`, where `edgefeat_dim` is the dimensionality of edge features and i-th row represents the feature of i-th edge. This can be `None` if no input edge features are available.
- `node_feat`: numpy arrays of shape `(num_nodes, nodefeat_dim)`, where `nodefeat_dim` is the dimensionality of node features and i-th row represents the feature of i-th node. This can be `None` if no input node features are available.
- `num_nodes`: number of nodes in the graph.

**Node:** Some graph datasets may contain additional meta-information in node or edges such as their time stamps. Although they are not given as default input features, researchers should feel free to exploit these additional information.

<a name="eval"/>

----------

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

