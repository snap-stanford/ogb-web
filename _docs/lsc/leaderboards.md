---
title: OGB-LSC Leaderboards
permalink: /docs/lsc/leaderboards/
---

---------

##### **Steps to submit to leaderboards**
- Carefully read the **[rules](/docs/lsc/rules/)**.
- Develop models and save test-dev prediction using the OGB Evaluator.
- Submit your result via **[this page](https://ogb-save.stanford.edu/leaderboard/)**.

---------

##### **Leaderboards policies**
- For each email address on each dataset, another leaderboard submission cannot be made within one week after the last submission. Our system will automatically reject such submissions. **Please do not use multiple email addresses within the same team.**
- Extra information (hardware information, training/inference time, validation performance, technical report etc) is required for the OGB-LSC leaderboard submissions. Please check **[the submission page](https://ogb-save.stanford.edu/leaderboard/)** early to understand what is required.

---------

##### **Check out leaderboards**
- **[MAG240M](#mag240m)**
- **[WikiKG90Mv2](#wikikg90mv2)**
- **[PCQM4Mv2](#pcqm4mv2)**

**Package** denotes the required package version for each dataset to be eligible for the leaderboards.


<a name="mag240m"/>

---------

### Leaderboard for [MAG240M](/docs/lsc/mag240m)
##### Classification accuracy on the test-dev and validation sets. The higher, the better.

#### Package: >=1.3.2


| Rank  | Method | Ensemble | Test-dev Accuracy | Validation Accuracy | Team | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **R-GAT (NS)**  | No | 0.6931  | 0.7002 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 12,255,385 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  2  |  **R-GraphSAGE (NS)**  | No | 0.6878  | 0.6986 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 12,234,905 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  3  |  **GAT (NS)**  | No | 0.6671  | 0.6715 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 4,890,777 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  4  |  **GraphSAGE (NS)**  | No | 0.6621  | 0.6679 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 4,884,633 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  5  |  **MLP+C&S**  | No | 0.6605  | 0.6698 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 473,241 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  6  |  **SIGN**  | No | 0.6603  | 0.6664 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 3,758,233 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  7  |  **SGC**  | No | 0.6530  | 0.6582 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 736,921 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  8  |  **LabelProp**  | No | 0.5638  | 0.5844 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 0 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  9  |  **MLP**  | No | 0.5276  | 0.5267 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 473,241 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |


<a name="wikikg90mv2"/>

---------

### Leaderboard for [WikiKG90Mv2](/docs/lsc/wikikg90mv2)
##### MRR on the test-dev and validation sets. The higher, the better.

#### Package: >=1.3.2


| Rank  | Method | Ensemble | Test-dev MRR | Validation MRR | Team | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **ComplEx-Concat**  | No | 0.1833  | 0.2118 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m-v2) | 18,246,707,000 | 1 Quadro RTX 8000 (45GB GPU) | Sep 8, 2021 |
|  2  |  **TransE-Concat**  | No | 0.1820  | 0.2116 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m-v2) | 18,246,707,000 | 1 Quadro RTX 8000 (45GB GPU) | Sep 8, 2021 |
|  3  |  **ComplEx-MPNet**  | No | 0.1053  | 0.1303 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m-v2) | 307,600 | 1 Quadro RTX 8000 (45GB GPU) | Sep 8, 2021 |
|  4  |  **ComplEx-Shallow**  | No | 0.1035  | 0.1259 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m-v2) | 18,246,399,400 | 1 Quadro RTX 8000 (45GB GPU) | Sep 8, 2021 |
|  5  |  **TransE-MPNet**  | No | 0.0920  | 0.1174 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m-v2) | 307,600 | 1 Quadro RTX 8000 (45GB GPU) | Sep 8, 2021 |
|  6  |  **TransE-Shallow**  | No | 0.0917  | 0.1190 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/wikikg90m-v2) | 18,246,399,400 | 1 Quadro RTX 8000 (45GB GPU) | Sep 8, 2021 |


<a name="pcqm4mv2"/>

---------

### Leaderboard for [PCQM4Mv2](/docs/lsc/pcqm4mv2)
##### MAE on the test-dev and validation sets. The lower, the better.

#### Package: >=1.3.2


| Rank  | Method | Ensemble | Test-dev MAE | Validation MAE | Team | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GIN-virtual**  | No | 0.1084  | 0.1083 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 6,656,406 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  2  |  **GCN-virtual**  | No | 0.1152  | 0.1153 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 4,850,401 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  3  |  **GIN**  | No | 0.1218  | 0.1195 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 3,761,406 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  4  |  **GCN**  | No | 0.1398  | 0.1379 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 1,955,401 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  5  |  **MLP-Fingerprint**  | No | 0.1760  | 0.1753 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 16,107,201 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |



