---
title: OGB-LSC @ KDD Cup 2021
permalink: /kddcup2021/participate/
layout: kdd_participate
---

#### **Learn about team registration and test submissions**  
- **All the deadlines are on 23:59pm PST.** 

<a name="registration"/>

-------

#### **Team registration**: Deadline April 30th, 2021
<!-- ##### **[Google form](https://docs.google.com/forms/d/e/1FAIpQLSep990DhDqzkz8DZ4_6LU9aqbpk9iua2cniPAg7v-7GY4Jpwg/viewform)** -->
##### **[Google form (coming soon)](../form)**
**Every team must be registered through the Google form in order to be eligible for the subsequent test submissions.** 
**For each dataset, no members can be shared across different teams. If your team wants to work on multiple datasets, you will need to register separately.**
In the Google form, you will need to fill in the following information. 

- **Email:** Your own email address that you check daily.
- **Dataset:** MAG240M-LSC, WikiKG90M-LSC, or PCQM4M-LSC.
- **Team name:** Try to come up with a unique name!
- **Google group subscription**: From each team, we require at least one email address to be subscribed to our **[Google group](https://groups.google.com/g/open-graph-benchmark)**. We will use the group to make any announcements.
- **Team member information:** For each member, we require
    - Full real name
    - Institution
    - Email address
- **Rules**: Promise to follow the [rules](../rules).
- **Honer code**: You acknowledge that you have entered your own email address and the correct team member information. Whenever we ask you, you will have to respond immediately through the registered email and prove the correctness of the information you have provided. Otherwise, you may be disqualified from the competition.

**After the registration, you will receive a response receipt. Please keep it for your subsequent test submissions.**

Also, keep in mind that **your team name will be made publicly available** in our leaderboards together with your model performance. For the top 3 winners of each dataset, **the team member information will be also made publicly available.**

<a name="initial"/>

-------

#### **Initial test submission**: Deadline May 10th, 2021
##### **[Google form (coming soon)](../form)**
**Each team can optionally do one initial test submission to ensure the smooth final test submission.**
In the Google form, you will need to fill in the following information.

- **Email:** As registered before.
- **Dataset:** As registered before.
- **Team name**: As registered before.
- **Package version**: Package version used for experiments. Must match the required package for the dataset.
- **Prediction file**: Upload the model's prediction on the test set (format specified in the dataset page).

The submission will be evaluated over 5% of the hidden test data. The submitted performance will be made public in the leaderboards by May 14th. Note that the performance at the initial stage does *not* affect the winner selection.

-------

<a name="final"/>

#### **Final test submission**: Deadline June 8th, 2021
##### **[Google form (coming soon)](../form)**
**Each team submits its own final prediction result.**
In the Google form, you will need to fill in the following information. 

- **Email:** As registered before.
- **Dataset:** As registered before.
- **Team name**: As registered before.
- **Prediction file**: Upload the model's prediction on the test set (format specified in the dataset page).
- **Package version**: Package version used for experiments. Must match the required package for the dataset.
- **Extra information (irrelevant to winner decision)**:
    - Validation performance (if you use our official validation set for model selection).
    - Training hardware and time
    - Test inference hardware and time
    - List of optimized hyper-parameters
    - Number of learnable parameters
        - In Pytorch, it can be calculated by `sum(p.numel() for p in model.parameters())`.
    - Availability of the pre-trained model
        - **We highly encourage you to save the best pre-trained model that you use to make the final prediction.**

The prediction will be evaluated over the entire test data. The winners as well as all the submitted performance will be publicly announced.