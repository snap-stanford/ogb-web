---
title: Graph Property Prediction
permalink: /docs/graphprop/
---

##### The task is to predict properties of entire graphs or subgraphs.

### Summary

#### - Datasets

Scale | Name     | #Graphs   | #Nodes per graph | #Edges per graph\* | #Task | Split Type  | Task Type   | Metric                           |
|-------------------------|----------|----------|----------|----------------|---------------------|------------------------|----------|
Small | [ogbg-mol-hiv](#ogbg-mol) | 41,127 | 25.5 | 27.5 | 1   | Scaffold  |  Binary classification | ROC-AUC  |
Medium | [ogbg-mol-pcba](#ogbg-mol) | 437,929 | 26.0 | 28.1 | 128   | Scaffold  |  Binary classification | ROC-AUC  |
Medium | [ogbg-ppi](#ogbg-ppi) | 158,100 | 243.4 | 2,266.1 | 1  | Species  |  Multi-class classification | Accuracy  |


\* Note that for undirected graphs, the loaded graphs will have the doubled number of edges becausewe add the bidirectional edges automatically.


#### - Module
We prepare different [data loader](#loader) variants: (1) [Pytorch Geometric one](#pyg) (2) [DGL one](#dgl) and (3) [library-agnostic one](#libagn).
We also prepare a unified [performance evaluator](#eval).

----------

<a name="ogbg-mol"/>
### Dataset `ogbg-mol`: ([Leaderboard](../leader_graphprop/#ogbg-mol))

**Graph:** `ogbg-mol` is *a set of* molecular property prediction datasets adopted from MoleculeNet [1]. All the molecules are pre-processed using RDKit [2].
Each graph represents a molecule, where nodes are atoms, and edges are chemical bonds.
Input node features are 9-dimensional, containing atomic number, chirality, formal charge, etc. Input edge features are 3-dimensional, containing bond type, bond stereo, etc.
For further details, please refer to the [code](https://github.com/snap-stanford/ogb/blob/master/ogb/utils/features.py). The script to convert the SMILES string [3] to the above graph object can be found [here](../../assets/script/smiles2graph.py).
Note that the script requires [RDkit](https://www.rdkit.org/docs/GettingStartedInPython.html) to be installed. The script can be used to pre-process external molecule datasets so that those datasets share the same input feature space as the OGB molecule datasets. This is particularly useful for pre-training graph models, which has great potential to significantly increase generalization performance on the (*downstream*) OGB datasets [4].

For encoding these raw input features, we prepare simple modules called `AtomEncoder` and `BondEncoder`. They can be used as follows to embed raw atom and bond features to obtain `atom_emb` and `bond_emb`.
```python
from ogb.graphproppred.mol_encoder import AtomEncoder, BondEncoder
atom_encoder = AtomEncoder(emb_dim = 100)
bond_encoder = BondEncoder(emb_dim = 100)

atom_emb = atom_encoder(x) # x is input atom feature in Pytorch Geometric
edge_emb = bond_encoder(edge_attr) # edge_attr is input edge feature in Pytorch Geometric
```

#### Datasets

**Prediction task:**  From MoleculeNet [1], we selected and processed two molecular property prediction datasets: `ogbg-mol-hiv`, `ogbg-mol-pcba`, that are of small and medium sizes, respectively.
A detailed description of each dataset can be found in [1].
Each dataset can contain multiple labels/tasks to predict, and the performance averaged over these tasks is to be evaluated.

The task is to predict the target chemical properties as accurately as possible.
All the raw molecule data (including the SMILES strings) can be found in the `raw` directory in the downloaded dataset folder, e.g., `dataset/ogbg_mol_hiv_pyg/raw/hiv.csv.gz`.

Beside the two main datasets, we also provide the other MoleculeNet datasets that are readily available from the OGB package. They are `ogbg-mol-tox21`, `ogbg-mol-bace`, `ogbg-mol-bbbp`, `ogbg-mol-clintox`, `ogbg-mol-muv`, `ogbg-mol-sider`, and `ogbg-mol-toxcast` for binary classification, `ogbg-mol-esol`, `ogbg-mol-freesolv`, and `ogbg-mol-lipo` for regression. Evaluators are also provided for these datasets. We encourage you to also test on these datasets if you are working on molecule-specific models.

**Dataset splitting:** We adopt the *scaffold splitting* (implmented in [RDkit](https://www.rdkit.org/docs/GettingStartedInPython.html)) that splits the molecules based on their two-dimensional structural frameworks. The scaffold splitting attempts to separate structurally different molecules into different subsets, which provides a more realistic estimate of model performance in prospective settings [1].

#### References

[1] Wu, Z., Ramsundar, B., Feinberg, E. N., Gomes, J., Geniesse, C., Pappu, A. S., Leswing, K. & Pande, V. (2018). MoleculeNet: a benchmark for molecular machine learning. Chemical science, 9(2), 513-530. <br/>
[2] Landrum, G. (2006). RDKit: Open-source cheminformatics. <br/>
[3] Anderson, Eric, Gilman D. Veith, and David Weininger. SMILES: a line notation and computerized interpreter for chemical structures. (1987). <br/>
[4] Hu, W., Liu, B., Gomes, J., Zitnik, M., Liang, P., Pande, V., & Leskovec, J. (2020). Strategies for pre-training graph neural networks. ICLR 2020.

----------

<a name="ogbg-ppi"/>
### Dataset `ogbg-ppi`: ([Leaderboard](../leader_graphprop/#ogbg-ppi))

**Graph:** TDA

**Prediction task:** TDA

**Dataset splitting:** TDA


#### References

----------------

<a name="loader"/>

### Data Loader

To load a dataset replace, d_name with the dataset name (e.g., `"ogbg-mol-hiv"`).

<a name="pyg"/>

#### Pytorch Geometric Loader

```python
from ogb.graphproppred.dataset_pyg import PygGraphPropPredDataset
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
from ogb.graphproppred.dataset_dgl import DglGraphPropPredDataset, collate_dgl
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
from ogb.graphproppred.dataset import GraphPropPredDataset

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

----------

<a name="eval"/>

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

