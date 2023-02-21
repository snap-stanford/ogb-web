---
title: OGB-LSC Leaderboards
permalink: /docs/lsc/leaderboards/
---

---------

##### **Steps to submit to leaderboards**
- Carefully read the **[rules](/docs/lsc/rules/)**.
- Develop models and save test-dev prediction using the OGB Evaluator.
- Submit your result via **[this page](https://ogb-save.stanford.edu/leaderboard/)**.
- Wait at least one week until your test result shows up on our leaderboard. Please **[contact us](mailto:ogb-lsc@cs.stanford.edu)** if this is not the case.

---------

##### **Leaderboards policies**
- For each email address on each dataset, another leaderboard submission cannot be made within one week after the last submission. Our system will automatically reject such submissions. **Please do not use multiple email addresses within the same team.**
- Extra information (hardware information, training/inference time, validation performance, technical report etc) is required for the OGB-LSC leaderboard submissions. Please check **[the submission page](https://ogb-save.stanford.edu/leaderboard/)** early to understand what is required.
- **Please do not submit a placeholder Github repository / technical report.** You will be permanently disqualified if we find your submission is based on the placeholder.

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
|  2  |  **MDGNN (OGB-LSC'22 3rd)**  | Yes | 0.7535  | 0.7756 | CogDL | [Yukuo Cen](mailto:cenyk1230@gmail.com) (Tsinghua / Zhipu AI) | [Paper](https://github.com/cenyk1230/MDGNN_MAG240M/blob/master/MDGNN_MAG240M_2022.pdf), [Code](https://github.com/cenyk1230/MDGNN_MAG240M) | 1,297,305 | 1 NVIDIA A100 GPU (80GB memory) | Nov 21, 2022 |
|  3  |  **MPNN+BGRL (KDDCup'21 2nd)**  | Yes | 0.7507  | 0.7710 | Academic | [Petar Velickovic](mailto:petarv@google.com) (DeepMind) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_Academic.pdf), [Code](https://github.com/deepmind/deepmind-research/tree/master/ogb_lsc/mag) | N/A | 4 Google Cloud TPUv4 | Mar 9, 2022 |
|  4  |  **Cleora+EMDE (KDDCup'21 3rd)**  | Yes | 0.7457  | N/A | Synerise AI | [Jacek Dabrowski](mailto:jack.dabrowski@synerise.com) (Synerise) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_SyneriseAI.pdf), [Code](https://github.com/Synerise/kdd-cup-2021) | N/A | Tesla V100 (16GB) | Mar 9, 2022 |
|  5  |  **MPLP+finetune (KDDCup'21 4th)**  | Yes | 0.7440  | N/A | Topology_mag | [Wencai Cao](mailto:caowencai@oppo.com) (OPPO Research) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_Topology_mag.pdf), [Code](https://github.com/qypeng-ustc/mplp) | N/A | V100 GPU (32GB memory) | Mar 9, 2022 |
|  6  |  **SGC+R-GAT+Finetune (KDDCup'21 5th)**  | Yes | 0.7377  | 0.7420 | passages | [ Kaiyuan Li](mailto:tsotfsk@bupt.edu.cn) (Nanjing University / BUPT) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_passages.pdf), [Code](https://github.com/passages-kddcup2021/KDDCUP2021_OGB_LSC_MAG240M) | N/A | GeForce RTX 3090 GPU (24GB) | Mar 9, 2022 |
|  7  |  **GNN180M (KDDCup'21 6th)**  | Yes | 0.7340  | N/A | DeeperBiggerBetter | [Guohao Li](mailto:guohao.li@kaust.edu.sa) (KAUST / Intel) | [Paper](https://ogb.stanford.edu/paper/kddcup2021/mag240m_DeeperBiggerBetter.pdf), [Code](https://github.com/zarzarj/DeeperBiggerBetter_KDDCup) | N/A | 4 NVIDIA GeForce RTX 6000 (48G) | Mar 9, 2022 |
|  8  |  **R-GAT (NS)**  | No | 0.6931  | 0.7002 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 12,255,385 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  9  |  **R-GraphSAGE (NS)**  | No | 0.6878  | 0.6986 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 12,234,905 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  10  |  **GAT (NS)**  | No | 0.6671  | 0.6715 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 4,890,777 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  11  |  **GraphSAGE (NS)**  | No | 0.6621  | 0.6679 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 4,884,633 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  12  |  **MLP+C&S**  | No | 0.6605  | 0.6698 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 473,241 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  13  |  **SIGN**  | No | 0.6603  | 0.6664 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 3,758,233 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  14  |  **SGC**  | No | 0.6530  | 0.6582 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 736,921 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  15  |  **LabelProp**  | No | 0.5638  | 0.5844 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 0 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  16  |  **MLP**  | No | 0.5276  | 0.5267 | OGB-LSC | [Matthias Fey](mailto:matthias.fey@tu-dortmund.de) (TU Dortmund) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/mag240m) | 473,241 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |


<a name="wikikg90mv2"/>

---------

### Leaderboard for [WikiKG90Mv2](/docs/lsc/wikikg90mv2)
##### MRR on the test-dev and validation sets. The higher, the better.

#### Package: >=1.3.3


| Rank  | Method | Ensemble | Test-dev MRR | Validation MRR | Team | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **BESS + diverse KGE ensemble**  | Yes | 0.2539  | 0.2919 | Graphcore | [Daniel Justus](mailto:danielj@graphcore.ai) (Graphcore) | [Paper](https://arxiv.org/abs/2211.12281), [Code](https://github.com/graphcore/distributed-kge-poplar) | 23,356,393,344 | Graphcore Bow Pod16 | Dec 1, 2022 |
|  2  |  **DGLKE+RuleMining+ManualFeature**  | Yes | 0.2493  | 0.2916 | DNAKG | [Xiaojun Ma](mailto:xiaojunma@microsoft.com) (MSRA) | [Paper](https://ogb.stanford.edu/paper/neurips2022/wikikg90mv2_DNAKG.pdf), [Code](https://github.com/AprLie/DNAKG.git) | 18,247,074,200 | 2x TitanV,800GB memory | Nov 20, 2022 |
|  3  |  **PIE-RM**  | Yes | 0.2115  | 0.2540 | USTCWiki | [HongChao Gu](mailto:ustcghc@mail.ustc.edu.cn) (USTC / iflytek) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/TingJShen/Wikikg90mV2) | 18,247,074,200 | 4 Telsla M40 | Oct 26, 2022 |
|  4  |  **TransE-ens**  | Yes | 0.1903  | 0.2931 | CogDL | [Xiao Liu](mailto:xiao190525@gmail.com) (Tsinghua / Zhipu.AI) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/anyezhiya368/ogb-lsc-2022) | 18,247,074,200 | 1 A100 | Oct 31, 2022 |
|  5  |  **TransE-Shallow-PIE**  | No | 0.1883  | 0.2342 | Ant Group KG&NLP | [Linlin Chao](mailto:chulin.cll@antgroup.com) (Ant Group) | [Paper](https://arxiv.org/abs/2204.13957), [Code](https://github.com/alipay/Parameter_Inference_Efficient_PIE) | 18,247,074,200 | Tesla P100 (16GB GPU)	 | May 2, 2022 |
|  6  |  **TransE-Concat**  | No | 0.1761  | 0.2060 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,707,000 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  6  |  **ComplEx-Concat**  | No | 0.1761  | 0.2048 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,707,000 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  7  |  **ComplEx**  | No | 0.1412  | 0.1816 | GraphLARS | [Ling Yue](mailto:yueling.me@qq.com) (EE, Tsinghua / 4paradigm) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,707,000 | 1*A100 | Sep 1, 2022 |
|  8  |  **ComplEx-MPNet**  | No | 0.0988  | 0.1258 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 307,600 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  9  |  **ComplEx-Shallow**  | No | 0.0985  | 0.1150 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,399,400 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  10  |  **TransE-MPNet**  | No | 0.0860  | 0.1128 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 307,600 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |
|  11  |  **TransE-Shallow**  | No | 0.0824  | 0.1103 | OGB-LSC | [Hongyu Ren](mailto:hyren@cs.stanford.edu) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/google-research/smore/blob/wikikgv2/README_wikikgv2.md) | 18,246,399,400 | 1 Quadro RTX 8000 (45GB GPU) | Oct 12, 2021 |


<a name="pcqm4mv2"/>

---------

### Leaderboard for [PCQM4Mv2](/docs/lsc/pcqm4mv2)
##### MAE on the test-dev and validation sets. The lower, the better.

#### Package: >=1.3.2


| Rank  | Method | Ensemble | Test-dev MAE | Validation MAE | Team | Contact | References | #Params | Hardware | Date 
|:----:|:-----:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|-----:|:-----:|:-----:|
|  1  |  **GPS++**  | Yes | 0.0720  | 0.0778 | GraphcoreValenceMILA | [Dominic Masters](mailto:dominicm@graphcore.ai) (Graphcore/Valence/MILA) | [Paper](https://github.com/graphcore/ogb-lsc-pcqm4mv2/raw/main/GPSplusplus.pdf), [Code](https://github.com/graphcore/ogb-lsc-pcqm4mv2) | 44,291,413 | Graphcore BOW-POD16 | Nov 18, 2022 |
|  2  |  **MolNet_Ensemble**  | Yes | 0.0753  | 0.0797 | polixir.ai | [zouxiaochuan](mailto:zouxiaochuan1984@gmail.com) (polixir.ai) | [Paper](https://github.com/zouxiaochuan/code_ogblsc2022/blob/main/molnet2022_arxiv.pdf), [Code](https://github.com/zouxiaochuan/code_ogblsc2022) | 32,047,874 | 8 RTX3090 | Nov 1, 2022 |
|  3  |  **Global-ViSNet**  | No | 0.0766  | 0.0784 | ViSNet | [Tong Wang](mailto:watong@microsoft.com) (Microsoft Research AI4Science) | [Paper](https://github.com/ogb-visnet/Global-ViSNet/blob/master/ViSNet_Tech_Report.pdf), [Code](https://github.com/ogb-visnet/Global-ViSNet) | 78,450,692 | 4 NVIDIA A100 GPUs | Oct 26, 2022 |
|  4  |  **Transformer-M**  | No | 0.0782  | 0.0772 | FML Lab@PKU | [Shengjie Luo](mailto:luosj@stu.pku.edu.cn) (Peking University) | [Paper](https://arxiv.org/abs/2210.01765), [Code](https://github.com/lsj2408/Transformer-M) | 68,957,249 | 4 NVIDIA Tesla A100 GPUs (40GB) | Oct 5, 2022 |
|  5  |  **GEM-2**  | No | 0.0806  | 0.0793 | PaddleHelix | [Donglong He](mailto:hedonglong@baidu.com) (Baidu) | [Paper](https://arxiv.org/abs/2208.05863), [Code](https://github.com/PaddlePaddle/PaddleHelix/tree/dev/apps/pretrained_compound/ChemRL/GEM-2) | 32,086,707 | 16 NVIDIA A100 | Aug 11, 2022 |
|  6  |  **Deep graph transformer**  | Yes | 0.0843  | 0.0891 | NVIDIA-PCQM4Mv2 | [Jiwei Liu](mailto:jiweil@nvidia.com) (NVIDIA) | [Paper](https://github.com/daxiongshu/PCQM4Mv2_subs/blob/main/tech_report.pdf), [Code](https://github.com/daxiongshu/PCQM4Mv2_subs) | 63,600,000 | 1 NVIDIA V100 GPU 32 GB | Oct 26, 2022 |
|  7  |  **Deep graph transformer**  | Yes | 0.0844  | 0.0891 | NVIDIA-PCQM4Mv2 | [Jiwei Liu](mailto:jiweil@nvidia.com) (NVIDIA) | [Paper](https://github.com/daxiongshu/PCQM4Mv2_subs/blob/main/tech_report.pdf), [Code](https://github.com/daxiongshu/PCQM4Mv2_subs) | 63,600,000 | 1 NVIDIA V100 GPU 32 GB | Oct 19, 2022 |
|  8  |  **Deep graph transformer**  | Yes | 0.0852  | 0.0891 | NVIDIA-PCQM4Mv2 | [Jiwei Liu](mailto:jiweil@nvidia.com) (NVIDIA) | [Paper](https://github.com/daxiongshu/PCQM4Mv2_subs/blob/main/tech_report.pdf), [Code](https://github.com/daxiongshu/PCQM4Mv2_subs) | 63,600,000 | 1 NVIDIA V100 GPU 32 GB | Oct 11, 2022 |
|  9  |  **GPS**  | No | 0.0862  | 0.0852 | Mila | [Ladislav Rampasek](mailto:rampasek@gmail.com) (Mila / Universite de Montreal) | [Paper](https://arxiv.org/abs/2205.12454), [Code](https://github.com/rampasek/GraphGPS) | 13,807,345 | 1 NVIDIA A100 (40GB) | Nov 10, 2022 |
|  9  |  **EGT**  | No | 0.0862  | 0.0857 | EFT-AIRC | [Md Shamim Hussain](mailto:snirjhar@gmail.com) (RPI / IBM) | [Paper](https://arxiv.org/abs/2108.03348), [Code](https://github.com/shamim-hussain/egt_pytorch) | 89,326,465 | 8 Tesla V100 (32GB) | Jun 24, 2022 |
|  10  |  **CoAtGIN-base**  | No | 0.0866  | 0.0859 | xfcui@sdu | [Xuefeng Cui](mailto:xfcui.uw@gmail.com) (Shandong University) | [Paper](https://www.biorxiv.org/content/10.1101/2022.08.26.505499v1), [Code](https://github.com/xfcui/CoAtGIN) | 9,938,433 | 8 NVIDIA A40 | Sep 30, 2022 |
|  11  |  **EGT+LSPE+HIERA_clustering**  | No | 0.0868  | 0.0863 | rwlspegate2 | [YEOM JE YOON](mailto:a01082177535@gmail.com) (University of Seoul) | [Paper](https://github.com/emforce77/rwlspegate2/blob/c3b83ac0a1f0d1dc67e3f59d928eb092dd797cd4/technical_report.pdf), [Code](https://github.com/emforce77/rwlspegate2.git) | 90,102,913 | NVIDIA A100 80GB HBM2E SXM4 | Feb 16, 2023 |
|  12  |  **EGT**  | No | 0.0872  | 0.0869 | EGT-AIRC | [Md Shamim Hussain](mailto:snirjhar@gmail.com) (RPI / IBM) | [Paper](https://arxiv.org/abs/2108.03348), [Code](https://github.com/shamim-hussain/egt_pytorch) | 89,326,465 | 8 Tesla V100 (32GB) | Jan 26, 2022 |
|  13  |  **GRPE-Large**  | No | 0.0876  | 0.0867 | WonWoo | [Wonpyo Park](mailto:wppark.pio@gmail.com) (SNU / Standigm) | [Paper](https://arxiv.org/abs/2201.12787), [Code](https://github.com/lenscloth/GRPE) | 118,300,000 | 8 A100-SXM4-40GB | Aug 14, 2022 |
|  14  |  **GraphSelfAttention**  | No | 0.0898  | 0.0890 | WonWoo | [Wonpyo Park](mailto:pionpark@gmail.com) (Standigm) | [Paper](https://arxiv.org/abs/2201.12787), [Code](https://github.com/lenscloth/GraphSelfAttention) | 46,199,041 | 4 A100 GPU | Nov 15, 2021 |
|  15  |  **Deep graph transformer**  | Yes | 0.0904  | 0.0891 | NVIDIA-PCQM4Mv2 | [Jiwei Liu](mailto:jiweil@nvidia.com) (NVIDIA) | [Paper](https://github.com/daxiongshu/PCQM4Mv2_subs/blob/main/tech_report.pdf), [Code](https://github.com/daxiongshu/PCQM4Mv2_subs) | 63,600,000 | 1 NVIDIA V100 GPU 32 GB | Oct 3, 2022 |
|  16  |  **CoAtGIN-tiny**  | No | 0.0908  | 0.0901 | xfcui@sdu | [Xuefeng Cui](mailto:xfcui.uw@gmail.com) (Shandong University) | [Paper](https://www.biorxiv.org/content/10.1101/2022.08.26.505499v1), [Code](https://github.com/xfcui/CoAtGIN) | 6,395,393 | 1 NVIDIA A40 | Sep 20, 2022 |
|  17  |  **TokenGT (Lap)**  | No | 0.0919  | 0.0910 | vl-kaist | [Jinwoo Kim](mailto:jinwoo-kim@kaist.ac.kr) (KAIST) | [Paper](https://arxiv.org/abs/2207.02505), [Code](https://github.com/jw9730/tokengt) | 48,492,289 | NVIDIA RTX 3090 x 8 | Aug 8, 2022 |
|  18  |  **CoAtGIN-tiny**  | No | 0.0921  | 0.0916 | xfcui@sdu | [Xuefeng Cui](mailto:xfcui.uw@gmail.com) (Shandong University) | [Paper](https://www.biorxiv.org/content/10.1101/2022.08.26.505499v1), [Code](https://github.com/xfcui/CoAtGIN) | 6,183,425 | 1 NVIDIA A40 | Sep 8, 2022 |
|  19  |  **CoAtGIN-tiny**  | No | 0.0935  | 0.0933 | xfcui@sdu | [Xuefeng Cui](mailto:xfcui.uw@gmail.com) (Shandong University) | [Paper](https://www.biorxiv.org/content/10.1101/2022.08.26.505499v1), [Code](https://github.com/xfcui/CoAtGIN) | 5,460,225 | NVIDIA A40 | Aug 29, 2022 |
|  20  |  **HFAGNN**  | No | 0.1010  | 0.1005 | Zhuque Zhejianglab | [Can Xu](mailto:leoxc1571@163.com) (Zhejiang Lab) | [Paper](https://github.com/Tigerrr07/HFAGNN/blob/master/technical_report.pdf), [Code](https://github.com/Tigerrr07/HFAGNN) | 3,949,959 | 1 NVIDIA TITAN V GPU(12GB memory) | Oct 30, 2022 |
|  21  |  **GIN-virtual**  | No | 0.1084  | 0.1083 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 6,656,406 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  22  |  **GCN-virtual**  | No | 0.1152  | 0.1153 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 4,850,401 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  23  |  **GIN**  | No | 0.1218  | 0.1195 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 3,761,406 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  24  |  **GraphGPS without PE (subset)**  | No | 0.1395  | 0.1334 | GraphLARS | [Xu Wang](mailto:wangxu01@4paradigm.com) (4Paradigm && EE Tsinghua) | [Paper](https://arxiv.org/abs/2205.12454), [Code](https://github.com/rampasek/GraphGPS) | 6,155,089 | 1 RTX3090 (24GB GPU) | Sep 2, 2022 |
|  25  |  **GCN**  | No | 0.1398  | 0.1379 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 1,955,401 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  26  |  **MLP-Fingerprint**  | No | 0.1760  | 0.1753 | OGB-LSC | [Weihua Hu](mailto:weihua916@gmail.com) (Stanford) | [Paper](https://openreview.net/pdf?id=qkcLxoC52kL), [Code](https://github.com/snap-stanford/ogb/tree/master/examples/lsc/pcqm4m-v2) | 16,107,201 | 1 GeForce RTX 2080 (11GB GPU) | Sep 8, 2021 |
|  27  |  **MolNet_Ensemble**  | Yes | 0.9899  | 0.0847 | polixir.ai | [xiaochuan zou](mailto:zouxiaochuan1984@gmail.com) (polixir.ai) | [Paper](https://github.com/zouxiaochuan/code_ogblsc2022/blob/main/molnet2022_arxiv.pdf), [Code](https://github.com/zouxiaochuan/code_ogblsc2022) | 32,047,874 | 8 RTX3090 | Oct 24, 2022 |



