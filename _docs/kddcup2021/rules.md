---
title: OGB-LSC @ KDD Cup 2021
permalink: /docs/kddcup2021/rules/
layout: kdd_rules
---

#### **Learn about the rules of the competition**  
- **Please read carefully about what are/aren't allowed in the competition.**  

-------


##### **Data Split**
We allow our participants to use training and validation sets in any ways. For example, there is no need to use the validation set only for model selection (you can directly train your model on the validation set if you find useful).
Also, the validation data can be defined by contestants themselves (you can use larger/smaller validation set if you find useful.
In OGB-LSC, we still provide the "standardized" validation sets since they have particular practical meaning (e.g., time splits in MAG240M-LSC and WikiKG90M-LSC, and the scaffold split in PCQM4M-LSC) and can be used as a way for participants to understand how test submissions are evaluated.

For the test data, you should only use them for your model inference (make prediction and save it for your test submissions). In other words, your model should be developed only based on training and validation sets and should not touch the test data except for the final inference.
The only exception is the MAG240M-LSC, where you can use the test nodes in any ways, since the dataset is modeled as a transductive prediction task (i.e., test nodes are part of the entire graph).

------

##### **Use of External Data**
During the KDD Cup, we **do not** allow the use of any external datasets to train models. For each dataset, models need to be developed only using the provided data.

---------

##### **Code Submission by Winners**
We require public code submission for the winners of the contest, which will be publicized on our webpage and need to remain public even after the KDD Cup.
Our goals are two-fold:
- To make it easier for the community to follow and build on top of the strong solutions.
- To incentivize the participants to follow the rules described above. Otherwise, the community would be able to find any misconduct by scrutinizing the code. The winners will be disqualified if there is any misconduct found in the code.

---------

##### **Public Data Source**
All of our datasets are constructed from public database.
To avoid trivial test label leakage, we have anonymized the data as much as we can, removing any obvious clues (e.g., data identifier, raw text information) that can be used to map nodes or graphs into the entities in the public database. At the same time, to keep our datasets practically-relevant and realistic, our anonymization may not be perfect (e.g., we need to provide the real graph connectivity, node features, and SMILES strings). Although we believe it is nearly impossible to recover ground-truth test labels, we still significantly discourage the participants to try to de-anonymize the datasets during the competition.
Keep in mind that once you win the contest, you will need to share all the code to reproduce your solution through public Github repository. 
This means that any obvious misconduct (e.g., training or doing early stopping on test labels, directly using the test labels as predictions) will be revealed.
