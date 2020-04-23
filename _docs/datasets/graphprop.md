---
title: Graph Property Prediction
permalink: /docs/graphprop/
---

##### The task is to predict properties of entire graphs or subgraphs.

### Summary

#### - Datasets

##### **The current datasets are subject to change until the paper is released (expected to be around mid April).**

Scale | Name     | #Graphs   | #Nodes per graph | #Edges per graph\* | #Task | Split Type  | Task Type   | Metric                           |
|-------------------------|----------|----------|----------|----------------|---------------------|------------------------|----------|
Small | [ogbg-molhiv](#ogbg-mol) | 41,127 | 25.5 | 27.5 | 1   | Scaffold  |  Binary classification | ROC-AUC  |
Medium | [ogbg-molpcba](#ogbg-mol) | 437,929 | 26.0 | 28.1 | 128   | Scaffold  |  Binary classification | PRC-AUC  |
Medium | [ogbg-ppi](#ogbg-ppi) | 158,100 | 243.4 | 2,266.1 | 1  | Species  |  Multi-class classification | Accuracy  |


**Note:** For undirected graphs, the loaded graphs will have the doubled number of edges because we add the bidirectional edges automatically.


#### - Module
We prepare different [data loader](#loader) variants: (1) [Pytorch Geometric one](#pyg) (2) [DGL one](#dgl) and (3) [library-agnostic one](#libagn).
We also prepare a unified [performance evaluator](#eval).

<a name="ogbg-mol"/>

----------

### Datasets `ogbg-molhiv` ([Leaderboard](../leader_graphprop/#ogbg-molhiv)) and `ogbg-molpcba` ([Leaderboard](../leader_graphprop/#ogbg-molpcba)):

**Graph:** `ogbg-molhiv` and `ogbg-molpcba` are two molecular property prediction datasets of different sizes: `ogbg-molhiv` (small) and `ogbg-molpcba` (medium). They are adopted from the MoleculeNet [1], and are among the largest of the MoleculeNet datasets. All the molecules are pre-processed using RDKit [2]. Each graph represents a molecule, where nodes are atoms, and edges are chemical bonds. Input node features are 9-dimensional, containing atomic number, chirality, and other additional atom features. Input edge features are 3-dimensional, containing bond type, bond stereochemistry, and one additional feature indicating whether the bond is conjugated or not. 
The full description of the features is provided in [code](https://github.com/snap-stanford/ogb/blob/master/ogb/utils/features.py). The script to convert the SMILES string [3] to the above graph object can be found [here](https://github.com/snap-stanford/ogb/blob/master/examples/graphproppred/mol/smiles2graph.py).
Note that the script requires [RDkit](https://www.rdkit.org/docs/GettingStartedInPython.html) to be installed. The script can be used to pre-process external molecule datasets so that those datasets share the same input feature space as the OGB molecule datasets. This is particularly useful for pre-training graph models, which has great potential to significantly increase generalization performance on the (*downstream*) OGB datasets [4].

Beside the two main datasets, we additionally provide 10 smaller datasets from MoleculeNet. They are `ogbg-moltox21`, `ogbg-molbace`, `ogbg-molbbbp`, `ogbg-molclintox`, `ogbg-molmuv`, `ogbg-molsider`, and `ogbg-moltoxcast` for (multi-task) binary classification, and `ogbg-molesol`, `ogbg-molfreesolv`, and `ogbg-mollipo` for regression. Evaluators are also provided for these datasets. These datasets can be used to stress-test molecule-specific methods or transfer learning [4].

For encoding these raw input features, we prepare simple modules called `AtomEncoder` and `BondEncoder`. They can be used as follows to embed raw atom and bond features to obtain `atom_emb` and `bond_emb`.
```python
from ogb.graphproppred.mol_encoder import AtomEncoder, BondEncoder
atom_encoder = AtomEncoder(emb_dim = 100)
bond_encoder = BondEncoder(emb_dim = 100)

atom_emb = atom_encoder(x) # x is input atom feature in Pytorch Geometric
edge_emb = bond_encoder(edge_attr) # edge_attr is input edge feature in Pytorch Geometric
```

#### Datasets

**Prediction task:**  The task is to predict the target molecular properties as accurately as possible, where the molecular properties are cast as binary labels, e.g., whether a molecule inhibits HIV virus replication or not. 
For evaluation metric, we closely follow Wu et al [1].
Specifically, `ogbg-molhiv`, we use ROC-AUC for evaluation. For `ogbg-molpcba`, as the class balance is extremely skewed (only 1.4% of data are positive) and it contains multiple classification tasks, we use the PRC-AUC averaged over the tasks as the evaluation metric.


**Dataset splitting:**
We adopt the *scaffold splitting* procedure (implmented in [RDkit](https://www.rdkit.org/docs/GettingStartedInPython.html)) that splits the molecules based on their two-dimensional structural frameworks. The scaffold splitting attempts to separate structurally different molecules into different subsets, which provides a more realistic estimate of model performance in prospective experimental settings [1].

#### References

[1] Wu, Z., Ramsundar, B., Feinberg, E. N., Gomes, J., Geniesse, C., Pappu, A. S., Leswing, K. & Pande, V. (2018). MoleculeNet: a benchmark for molecular machine learning. Chemical science, 9(2), 513-530. <br/>
[2] Landrum, G. (2006). RDKit: Open-source cheminformatics. <br/>
[3] Anderson, Eric, Gilman D. Veith, and David Weininger. SMILES: a line notation and computerized interpreter for chemical structures. (1987). <br/>
[4] Hu, W., Liu, B., Gomes, J., Zitnik, M., Liang, P., Pande, V., & Leskovec, J. (2020). Strategies for pre-training graph neural networks. ICLR 2020.

<a name="ogbg-ppi"/>

----------

### Dataset `ogbg-ppi` ([Leaderboard](../leader_graphprop/#ogbg-ppi)): 

**Graph:** `ogbg-ppi` is a set of undirected, unweighted protein association neighborhoods extracted from the protein-protein association networks of 1581 different species [1] that cover 37 broad taxonomic groups (e.g., mammals, bacterial families, archaeans) and span the tree of life [2]. To construct the neighborhoods, we randomly selected 100 proteins from each species and constructed 2-hop protein association neighborhoods centered on each of the selected proteins [3]. We then removed the center node from each neighborhood and subsampled the neighborhood to ensure the final protein association graph is small enough (less than 300 nodes). Nodes in each protein association graph represent proteins, and edges indicate biologically meaningful associations between proteins. The edges are associated with 7-dimensional features, where each element takes a value between 0 and 1 and represents the strength of a particular type of protein protein association such as gene co-occurrence, gene fusion events, and co-expression.


**Prediction task:** Given a protein association graph, the task is a 37-way multi-class classification to predict what taxonomic group the graph originates from.
The ability to successfully tackle this problem has implications for understanding the evolution of protein complexes across species, the rewiring of protein interactions over time, the discovery of functional associations between genes even for otherwise rarely-studied organisms, and would give us insights into key bioinformatics tasks, such as biological network alignment.

**Dataset splitting:** We adopt the *species split*, where the model is asked to predict taxonomic groups of graphs originating from species, which are not seen during training but belong to one of the 37 taxonomic groups.
This split stress-tests the model's capability to extract graph features that are essential to the prediction of the taxonomic groups, which is important for biological understanding of protein interactions.


#### References
[1] Szklarczyk, D., Gable, A. L., Lyon, D., Junge, A., Wyder, S., Huerta-Cepas, J., ... & Jensen, L. J. (2019). STRING v11: protein–protein association networks with increased coverage, supporting functional discovery in genome-wide experimental datasets. Nucleic acids research, 47(D1), D607-D613. <br/>
[2] Hug, L. A., Baker, B. J., Anantharaman, K., Brown, C. T., Probst, A. J., Castelle, C. J., ... & Suzuki, Y. (2016). A new view of the tree of life. Nature microbiology, 1(5), 16048. <br/>
[3] Zitnik, M., Feldman, M. W., & Leskovec, J. (2019). Evolution of resilience in protein interactomes across the tree of life. Proceedings of the National Academy of Sciences, 116(10), 4426-4433.

<a name="loader"/>

----------------

### Data Loader

To load a dataset replace, d_name with the dataset name (e.g., `"ogbg-molhiv"`).

<a name="pyg"/>

#### Pytorch Geometric Loader

```python
from ogb.graphproppred import PygGraphPropPredDataset
from torch_geometric.data import DataLoader

dataset = PygGraphPropPredDataset(name = d_name) 
num_tasks = dataset.num_tasks # obtaining the number of prediction tasks in a dataset

splitted_idx = dataset.get_idx_split() 
train_loader = DataLoader(dataset[splitted_idx["train"]], batch_size=32, shuffle=True)
valid_loader = DataLoader(dataset[splitted_idx["valid"]], batch_size=32, shuffle=False)
test_loader = DataLoader(dataset[splitted_idx["test"]], batch_size=32, shuffle=False)
```
Note that the prediction targets are stored in `dataset.y`.

<a name="dgl"/>

#### DGL Loader

```python
from ogb.graphproppred import DglGraphPropPredDataset, collate_dgl
from torch.utils.data import DataLoader

dataset = DglGraphPropPredDataset(name = d_name)
num_tasks = dataset.num_tasks # obtaining the number of prediction tasks in a dataset

splitted_idx = dataset.get_idx_split()
train_loader = DataLoader(dataset[splitted_idx["train"]], batch_size=32, shuffle=True, collate_fn=collate_dgl)
valid_loader = DataLoader(dataset[splitted_idx["valid"]], batch_size=32, shuffle=False, collate_fn=collate_dgl)
test_loader = DataLoader(dataset[splitted_idx["test"]], batch_size=32, shuffle=False, collate_fn=collate_dgl)
```
Note that the i-th example and its prediction targets can be obtained by `graph, label = dataset[i]`.

<a name="libagn"/>

#### Library-Agnostic Loader
```python
from ogb.graphproppred import GraphPropPredDataset

dataset = GraphPropPredDataset(name = d_name)
num_tasks = dataset.num_tasks # obtaining the number of prediction tasks in a dataset

splitted_idx = dataset.get_idx_split()
train_idx, valid_idx, test_idx = splitted_idx["train"], splitted_idx["valid"], splitted_idx["test"]

### set i as an arbitrary index
graph, label = dataset[i] # graph: library-agnostic graph object
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
from ogb.graphproppred import Evaluator

evaluator = Evaluator(name = d_name)
print(evaluator.expected_input_format) 
print(evaluator.expected_output_format)  
```

Then, you can pass the input dictionary (denoted by `input_dict` below) of the specified format and get the performance of your prediction.

```python
# In most cases, input_dict is
# input_dict = {"y_true": y_true, "y_pred": y_pred}
result_dict = evaluator.eval(input_dict)
```

