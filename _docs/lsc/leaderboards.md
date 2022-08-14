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
|  1  |  **R-UNIMP (KDDCup'21 1st)**  | Yes | 0.7539  | 0.7773 | BD-PGL | [Yunsheng Shi](mailto:shiyunsheng01@baidu.com) (Baidu) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_BD-PGL.pdf), [Code](https://github.com/PaddlePaddle/PGL/tree/main/examples/kddcup2021/MAG240M/r_unimp) | N/A | V100 (32GB) | Mar 9, 2022 |
|  2  |  **MPNN+BGRL (KDDCup'21 2nd)**  | Yes | 0.7507  | 0.7710 | Academic | [Petar Velickovic](mailto:petarv@google.com) (DeepMind) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_Academic.pdf), [Code](https://github.com/deepmind/deepmind-research/tree/master/ogb_lsc/mag) | N/A | 4 Google Cloud TPUv4 | Mar 9, 2022 |
|  3  |  **Cleora+EMDE (KDDCup'21 3rd)**  | Yes | 0.7457  | N/A | Synerise AI | [Jacek Dabrowski](mailto:jack.dabrowski@synerise.com) (Synerise) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_SyneriseAI.pdf), [Code](https://github.com/Synerise/kdd-cup-2021) | N/A | Tesla V100 (16GB) | Mar 9, 2022 |
|  4  |  **MPLP+finetune (KDDCup'21 4th)**  | Yes | 0.7440  | N/A | Topology_mag | [Wencai Cao](mailto:caowencai@oppo.com) (OPPO Research) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_Topology_mag.pdf), [Code](https://github.com/qypeng-ustc/mplp) | N/A | V100 GPU (32GB memory) | Mar 9, 2022 |
|  5  |  **SGC+R-GAT+Finetune (KDDCup'21 5th)**  | Yes | 0.7377  | 0.7420 | passages | [ Kaiyuan Li](mailto:tsotfsk@bupt.edu.cn) (Nanjing University / BUPT) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_passages.pdf), [Code](https://github.com/passages-kddcup2021/KDDCUP2021_OGB_LSC_MAG240M) | N/A | GeForce RTX 3090 GPU (24GB) | Mar 9, 2022 |
|  6  |  **GNN180M (KDDCup'21 6th)**  | Yes | 0.7340  | N/A | DeeperBiggerBetter | [Guohao Li](mailto:guohao.li@kaust.edu.sa) (KAUST / Intel) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_DeeperBiggerBetter.pdf), [Code](https://github.com/zarzarj/DeeperBiggerBetter_KDDCup) | N/A | 4 NVIDIA GeForce RTX 6000 (48G) | Mar 9, 2022 |
|  7  |  **R-GAT (NS)**  | No | 0.6931  | 0.7002 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 12,255,385 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  8  |  **R-GraphSAGE (NS)**  | No | 0.6878  | 0.6986 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 12,234,905 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  9  |  **GAT (NS)**  | No | 0.6671  | 0.6715 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 4,890,777 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  10  |  **GraphSAGE (NS)**  | No | 0.6621  | 0.6679 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 4,884,633 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  11  |  **MLP+C&S**  | No | 0.6605  | 0.6698 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 473,241 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  12  |  **SIGN**  | No | 0.6603  | 0.6664 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 3,758,233 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  13  |  **SGC**  | No | 0.6530  | 0.6582 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 736,921 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  14  |  **LabelProp**  | No | 0.5638  | 0.5844 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 0 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  15  |  **MLP**  | No | 0.5276  | 0.5267 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 473,241 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |


<a name="wikikg90mv2"/>

---------

### Leaderboard for [WikiKG90Mv2](/docs/lsc/wikikg90mv2)
##### MRR on the test-dev and validation sets. The higher, the better.

#### Package: >=1.3.3


| Rank  | Method | Ensemble | Test-dev MRR | Validation MRR | Team | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **TransE-Shallow-PIE**  | No | 0.1883  | 0.2342 | Ant Group KG&NLP | [Linlin Chao](mailto:chulin.cll@antgroup.com) (Ant Group) | [Paper](https://arxiv.org/abs/2204.13957), [Code](https://github.com/alipay/Parameter_Inference_Efficient_PIE) | 18,247,074,200 | Tesla P100 (16GB GPU)	 | May 2, 2022 |
|  2  |  **TransE-Concat**  | No | 0.1761  | 0.2060 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,707,000 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  2  |  **ComplEx-Concat**  | No | 0.1761  | 0.2048 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,707,000 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  3  |  **ComplEx-MPNet**  | No | 0.0988  | 0.1258 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 307,600 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  4  |  **ComplEx-Shallow**  | No | 0.0985  | 0.1150 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,399,400 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  5  |  **TransE-MPNet**  | No | 0.0860  | 0.1128 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 307,600 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  6  |  **TransE-Shallow**  | No | 0.0824  | 0.1103 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,399,400 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |


<a name="pcqm4mv2"/>

---------

### Leaderboard for [PCQM4Mv2](/docs/lsc/pcqm4mv2)
##### MAE on the test-dev and validation sets. The lower, the better.

#### Package: >=1.3.2


| Rank  | Method | Ensemble | Test-dev MAE | Validation MAE | Team | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GEM-2**  | No | 0.0806  | 0.0793 | PaddleHelix | [Donglong He](mailto:hedonglong@baidu.com) (Baidu) | [Paper](https://arxiv.org/abs/2208.05863), [Code](https://github.com/PaddlePaddle/PaddleHelix/tree/dev/apps/pretrained_compound/ChemRL/GEM-2) | 32,086,707 | 16 NVIDIA A100 | Aug 11, 2022 |
|  2  |  **EGT**  | No | 0.0862  | 0.0857 | EFT-AIRC | [Md Shamim Hussain](mailto:snirjhar@gmail.com) (RPI / IBM) | [Paper](https://arxiv.org/abs/2108.03348), [Code](https://github.com/shamim-hussain/egt_pytorch) | 89,326,465 | 8 Tesla V100 (32GB) | Jun 24, 2022 |
|  3  |  **EGT**  | No | 0.0872  | 0.0869 | EGT-AIRC | [Md Shamim Hussain](mailto:snirjhar@gmail.com) (RPI / IBM) | [Paper](https://arxiv.org/abs/2108.03348), [Code](https://github.com/shamim-hussain/egt_pytorch) | 89,326,465 | 8 Tesla V100 (32GB) | Jan 26, 2022 |
|  4  |  **GraphSelfAttention**  | No | 0.0898  | 0.0890 | WonWoo | [Wonpyo Park](mailto:pionpark@gmail.com) (Standigm) | [Paper](https://arxiv.org/abs/2201.12787), [Code](https://github.com/lenscloth/GraphSelfAttention) | 46,199,041 | 4 A100 GPU | Nov 15, 2021 |
|  5  |  **TokenGT (Lap)**  | No | 0.0919  | 0.0910 | vl-kaist | [Jinwoo Kim](mailto:jinwoo-kim@kaist.ac.kr) (KAIST) | [Paper](https://arxiv.org/abs/2207.02505), [Code](https://github.com/jw9730/tokengt) | 48,492,289 | NVIDIA RTX 3090 x 8 | Aug 8, 2022 |
|  6  |  **GIN-virtual**  | No | 0.1084  | 0.1083 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 6,656,406 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  7  |  **GCN-virtual**  | No | 0.1152  | 0.1153 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 4,850,401 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  8  |  **GIN**  | No | 0.1218  | 0.1195 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 3,761,406 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  9  |  **GCN**  | No | 0.1398  | 0.1379 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 1,955,401 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  10  |  **MLP-Fingerprint**  | No | 0.1760  | 0.1753 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 16,107,201 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |



