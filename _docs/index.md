---
title: Getting Started
permalink: /docs/home/
redirect_from: /docs/index.html
---

### Overview

OGB contains graph datasets that are managed by data loaders. The loaders handle downloading and pre-processing of the datasets.
Additionally, OGB has standardized evaluators and leaderboards to keep track of state-of-the-art results.

<p align = "center">
<img width="90%" src="{{ "/assets/img/ogb_overview.png" | relative_url }}" class="img-responsive">
</p>

The OGB components are closely tied to OGB Python package, as detailed below.

-----

### Updates

###### - **May 1st, 2020**: We have made our first major release of OGB! The package version is `1.1.*`.
###### - **May 4th, 2020**: Our paper will be on Arxiv!

-----

### Package Installation

You can install OGB using Python package manager pip.

```bash
pip install ogb
```

Please check the version is `1.1.*`.
```bash
python -c "import ogb; print(ogb.__version__)"
# This should print "1.1.*". Otherwise, please update the version by
pip install -U ogb
# Then, delete all the downloaded dataset folders.
```

#### Requirements
 - Python 3.5
 - PyTorch>=1.2
 - DGL>=0.4.1 or torch-geometric>=1.3.1
 - Numpy>=1.16.0
 - pandas>=0.24.0
 - urllib3>=1.24.0
 - scikit-learn>=0.20.0

------

### Package Usage

Next, we outline two key features of the OGB package, easy-to-use data loaders, and standardized model evaluators.

#### Data Loaders

We prepare easy-to-use [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/) and [DGL](https://www.dgl.ai/) data loaders that handle dataset downloading and standardized dataset splits.

Following is an example in PyTorch Geometric showing that a few lines of code are sufficient to prepare and split the dataset. You can enjoy the same convenience for DGL. For those who do not use neither of them, we also prepare library-agnostic dataset loaders that only depend on basic Python libraries (e.g., numpy, pickle) and thus can be used with other deep learning libraries such as Tensorflow.

```python
from ogb.graphproppred import PygGraphPropPredDataset
from torch_geometric.data import DataLoader

dataset = PygGraphPropPredDataset(name = "ogbg-molhiv")
 
split_idx = dataset.get_idx_split() 
train_loader = DataLoader(dataset[split_idx["train"]], batch_size=32, shuffle=True)
valid_loader = DataLoader(dataset[split_idx["valid"]], batch_size=32, shuffle=False)
test_loader = DataLoader(dataset[split_idx["test"]], batch_size=32, shuffle=False)
```

#### Evaluators

We prepare standardized evaluators for testing and comparing different methods. The evaluator takes `input_dict` (a dictionary whose format is specified in `evaluator.expected_input_format`) as input and returns a dictionary storing performance metric, which is appropriate for a particular dataset.

```python
from ogb.graphproppred import Evaluator

evaluator = Evaluator(name = "ogbg-molhiv")
# You can learn the input and output format specification of the evaluator as follows.
# print(evaluator.expected_input_format) 
# print(evaluator.expected_output_format) 
input_dict = {"y_true": y_true, "y_pred": y_pred}
result_dict = evaluator.eval(input_dict) # E.g., {"rocauc": 0.7321}
```

--------
### You are ready to explore OGB [datasets](../dataset_overview/)!
