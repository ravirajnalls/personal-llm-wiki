---
title: "Storage & data"
summary: 373 talks (46 case studies) across 32 events; organizations include PlanetScale, PingCAP, Google, eBay, Pivotal, Massive.
tags: [category, storage-data]
generated: categories
---

# Storage & data

> 373 talks across 32 events, oldest first: 46 case studies where an organization reports its own experience, plus concept talks and tutorials.

Keywords: storage, csi, rook, ceph, persistent volume, stateful, database, postgres, etcd, vitess, tikv, backup, velero, data on kubernetes (edit under `categories:` in wiki.yaml).

## Over time

| Year | Talks | Case studies |
| --- | --- | --- |
| 2016 | 7 | 0 |
| 2017 | 13 | 3 |
| 2018 | 44 | 4 |
| 2019 | 57 | 7 |
| 2020 | 34 | 4 |
| 2021 | 35 | 6 |
| 2022 | 20 | 4 |
| 2023 | 34 | 4 |
| 2024 | 56 | 7 |
| 2025 | 43 | 2 |
| 2026 | 30 | 5 |

## Organizations with case studies

PlanetScale (3), PingCAP (3), Google (2), eBay, Pivotal, Massive, Intuit, HubSpot, JD.com, Nozzle, Lyft, Chronosphere, Tencent, OVHcloud, Elastic, Alibaba Cloud, Niantic, Amazon, Loophole Labs, Cortex, Cisco, Viettel Group, Preferred Networks

## Talks by event

### 2016 · [KubeCon + CloudNativeCon North America 2016 (Seattle)](../sources/PLj6h78yzYM2PqgIGU1Qmi8nY7dqn9PCr4.md)

- **concept** · [Lightning Talk - Kubernetes and Ceph Integration: From Deployment to Production by Huamin Chen](https://www.youtube.com/watch?v=xWQui5IxS1c)
- **concept** · [Monitoring MySQL and MongoDB with Prometheus by Vadim Tkachenko, Percona](https://www.youtube.com/watch?v=19c_gNQT2dM). Shows how to monitor MySQL and MongoDB with Prometheus.
- **concept** · [Chronix as Long Term Storage for Prometheus by Moritz Kammerer, QAware GmbH](https://www.youtube.com/watch?v=4fhXSgRmLHM). Presents Chronix as a long-term storage backend for Prometheus.
- **concept** · [Lightning Talk - Say what? You're Running the Storage Platform IN Kubernetes?](https://www.youtube.com/watch?v=aAYpXS9bFMY)
- **concept** · [Torus: Focusing Storage for Kubernetes by Barak Michener, CoreOS, Inc.](https://www.youtube.com/watch?v=f8Ipew7JYFU)
- **concept** · [New Features in Kubernetes Storage by Brad Childs, Red Hat](https://www.youtube.com/watch?v=V6eX9S7N7Rk)
- **concept** · [Configuring and Deploying Stateful Applications with PetSet by David Oppenheimer](https://www.youtube.com/watch?v=EuJoAKTCCXg)

### 2017 · [KubeCon + CloudNativeCon Europe 2017 (Berlin)](../sources/PLj6h78yzYM2PAavlbv0iZkod4IVh_iGqV.md)

- **concept** · [Integrating Long-Term Storage with Prometheus [A] - Julius Volz, Prometheus](https://www.youtube.com/watch?v=MuHkckZg5L0)
- **concept** · [Building a Cloud-Native SQL Database [I] - Alex Robinson, Cockroach Labs](https://www.youtube.com/watch?v=rNXcvZCo448)
- **concept** · [Building a Storage Cluster with Kubernetes [I] - Bassam Tabbara, Quantum Corp.](https://www.youtube.com/watch?v=6p0GKjrYzg4). Shows how to build a storage cluster on Kubernetes using the Rook approach.

### 2017 · [KubeCon + CloudNativeCon North America 2017 (Austin)](../sources/PLj6h78yzYM2P-3-xqvmWaZbbI1sW-ulZb.md)

- **case study** · [Persistent Storage with Kubernetes in Production - Which Solution and Why? [I] - Cheryl Hung](https://www.youtube.com/watch?v=hqE5c5pyfrk)
- **case study** · [Evolving and Supporting Stateful, Multi-Tenant Decisioning Applications in Production](https://www.youtube.com/watch?v=UHVW01ksg-s)
- **case study** · [eBay Geo-Distributed Database on Kubernetes [A] - Chengyuan Li & Xinglang Wang, eBay](https://www.youtube.com/watch?v=2t_HVmih4IM) — eBay. eBay describes running a geo-distributed database on Kubernetes.
- **concept** · [You Have Stateful Apps - What if Kubernetes Would Also Run Your Storage? - Annette Clewett](https://www.youtube.com/watch?v=Fgpr2lMnBVY)
- **concept** · [Kubernetes Storage Evolution: Enabling High Performance Distributed Datastores](https://www.youtube.com/watch?v=5O5MIfGxCrI). Covers the evolution of Kubernetes storage to support high-performance distributed datastores.
- **concept** · [Economics of using Local Storage Attached to VMs on Cloud Providers [I] - Pavel Snagovsky](https://www.youtube.com/watch?v=ePLUqOnbdp4)
- **concept** · [Local Ephemeral Storage Resource Management - Jing Xu, Google](https://www.youtube.com/watch?v=cvK1t1h15XM)
- **concept** · [Distributed Database DevOps Dilemmas? Kubernetes to the Rescue - Denis Magda, GridGain](https://www.youtube.com/watch?v=k1y0Uoqepak)
- **concept** · [Kube-native Postgres [I] - Josh Berkus, RedHat](https://www.youtube.com/watch?v=Zn1vd7sQ_bc)
- **concept** · [Don’t Hassle Me, I’m Stateful - Jeff Bornemann & Michael Surbey, Red Hat](https://www.youtube.com/watch?v=yUfPd39-jHo)

### 2018 · [KubeCon + CloudNativeCon China 2018 (Shanghai)](../sources/PLj6h78yzYM2OK087kzLgc4jTPVbZjuNfs.md)

- **case study** · [When Distributed Database Meets Cloud - Lessons Learned - Yanqing Weng, Pivotal](https://www.youtube.com/watch?v=9zfPUFJ0j-0) — Pivotal. Pivotal shares lessons learned from running a distributed database in the cloud.
- **case study** · [Running Vitess on Kubernetes at Massive Scale: JD.com Case Study - Jiten Vaidya & Xin Lv](https://www.youtube.com/watch?v=I5g4EEJhRWQ) — Massive
- **concept** · [Upgrading Stateful Sets in Constrained Environment - Kishore Yerrapragada, A10 Networks](https://www.youtube.com/watch?v=feinZNMEyMk)
- **concept** · [Protecting Stateful Workloads With CSI Snapshot - Xing Yang, Huawei & Jing Xu, Google](https://www.youtube.com/watch?v=kOJ3qnTen3Q)
- **concept** · [Intro: Rook - Jared Watts, Upbound](https://www.youtube.com/watch?v=hjEq1n7Ow44)
- **concept** · [Provisioning the Distributed Database TiDB on Kubernetes - Shuan Deng, PingCAP](https://www.youtube.com/watch?v=O-vFoiVIGwU)
- **concept** · [Deep Dive: CNCF Storage WG - Xing Yang & Quinton Hoole, Huawei](https://www.youtube.com/watch?v=2qoynPoDOdk). Deep dive into the CNCF Storage Working Group and its cloud native storage work.
- **concept** · [Deep Dive: Rook - Jared Watts, Upbound](https://www.youtube.com/watch?v=9MQphnWAEY8). Deep dive into Rook for orchestrating storage on Kubernetes.
- **concept** · [Operator Framework to Manage Production Grade Stateful Workloads - Xin Xu & Xinglang Wang](https://www.youtube.com/watch?v=a34zzP2B6PA)
- **concept** · [Auto-Deployment of Ceph Cluster With Rook on Top of Kubernetes - Dennis Chen, Arm](https://www.youtube.com/watch?v=gLA9PwclpCA)
- **concept** · [Intro: CNCF Storage WG - Xing Yang & Quinton Hoole, Huawei](https://www.youtube.com/watch?v=FrKXx1CSxFg)

### 2018 · [KubeCon + CloudNativeCon Europe 2018 (Copenhagen)](../sources/PLj6h78yzYM2N8GdbjmhVU65KYm_68qBmo.md)

- **concept** · [Rook Project Intro – Bassam Tabbara, Tony Allen & Jared Watts, Upbound (Any Skill Level)](https://www.youtube.com/watch?v=To1ldyb_9NA)
- **concept** · [TSDB: The Past, Present and the Future - Goutham Veeramachaneni, IIT Hyderabad](https://www.youtube.com/watch?v=0UvKEHFNu4Q). Covers the history, current state and future of the Prometheus TSDB.
- **concept** · [Understanding Distributed Consensus in etcd and Kubernetes - Laura Frank, CloudBees](https://www.youtube.com/watch?v=n9VKAKwBj_0)
- **concept** · [Storage WG Intro – Ben Hindman, Mesosphere, Clint Kitson, VMware & Quinton Hoole, Huawei](https://www.youtube.com/watch?v=9Vt1B4vBvy8). Introduces the CNCF Storage working group and its goals.
- **concept** · [SIG Storage (K8s) Intro - Saad Ali, Google (Any Skill Level)](https://www.youtube.com/watch?v=GvrTl2T-Tts)
- **concept** · [Clusters as Cattle: How to Seamlessly Migrate Apps Across Kubernetes Clusters - Andy Goldstein](https://www.youtube.com/watch?v=5kMz2oJgV0A). Shows how to treat clusters as disposable and migrate applications between Kubernetes clusters.
- **concept** · [Storage WG Deep Dive – Ben Hindman, Mesosphere, Clint Kitson, VMware & Quinton Hoole, Huawei](https://www.youtube.com/watch?v=Nks3qOx8YcI)
- **concept** · [Rook Deep Dive – Bassam Tabbara, Tony Allen & Jared Watts, Upbound](https://www.youtube.com/watch?v=yknGKzJw7_k)
- **concept** · [Integrating Prometheus and InfluxDB - Paul Dix, InfluxData (Intermediate Skill Level)](https://www.youtube.com/watch?v=6UjVX-RTFmo). Explains how Prometheus and InfluxDB can be integrated for long-term storage and querying of metrics.
- **concept** · [Vitess and a Kubernetes Operator - Sugu Sougoumarane, YouTube (Intermediate Skill Level)](https://www.youtube.com/watch?v=paOiIkASDjg)
- **concept** · [Container Storage Interface: Present and Future - Jie Yu, Mesosphere, Inc.](https://www.youtube.com/watch?v=ktwY1anKN58)
- **concept** · [Using Kubernetes Local Storage for Scale-Out Storage Services - Michelle Au & Ian Chakeres](https://www.youtube.com/watch?v=eqkgiPppZN8)
- **tutorial** · [Kubernetes Storage Lingo 101 - Saad Ali, Google (Beginner Skill Level)](https://www.youtube.com/watch?v=uSxlgK1bCuA)

### 2018 · [KubeCon + CloudNativeCon North America 2018 (Seattle)](../sources/PLj6h78yzYM2PZf9eA7bhWnIh_mK1vyOfU.md)

- **case study** · [Kafka on Kubernetes - From Evaluation to Production at Intuit - Shrinand Javadekar, Intuit](https://www.youtube.com/watch?v=1SBxxMzlLAc) — Intuit. Intuit describes taking Kafka on Kubernetes from evaluation to production.
- **case study** · [Vitess at HubSpot: How We Moved Hundreds of MySQL Databases into... - Tom Petr & Alex Charis](https://www.youtube.com/watch?v=ZjTraLkMjYM) — HubSpot
- **concept** · [Lightning Talk: How Fast Was My Database? - Josh Berkus, Red Hat](https://www.youtube.com/watch?v=k-jAzGzhMXk)
- **concept** · [Lightning Talk: Kubegres: Accessing K8s From Postgres - Liz Frost, Heptio](https://www.youtube.com/watch?v=csM8LpedO3E)
- **concept** · [Intro: Rook - Jared Watts, Upbound](https://www.youtube.com/watch?v=pwVsFHy2EdE)
- **concept** · [Debugging etcd - Joe Betz & Jingyi Hu, Google](https://www.youtube.com/watch?v=NVMZBBQ9hsM)
- **concept** · [Exploring Application Portability Across Public Cloud Providers Using K8s - Erin Boyd & Ivan Font](https://www.youtube.com/watch?v=5W0UGxVOrD4). Explores how well applications can be moved across public cloud providers using Kubernetes.
- **concept** · [What's Next for etcd Cluster Management? - Gyuho Lee, Amazon Web Services & Sam Batschelet, Red Hat](https://www.youtube.com/watch?v=5kAVOQ4APok). Discusses upcoming directions for etcd cluster management and operations.
- **concept** · [Intro: Vitess - Dan Kozlowski & Sugu Sougoumarane, PlanetScale](https://www.youtube.com/watch?v=XeG-XTvymeY)
- **concept** · [Intro: Storage SIG - Saad Ali, Google](https://www.youtube.com/watch?v=PN-Cr6hBuX8)
- **concept** · [Deep Dive: Vitess - Dan Kozlowski & Sugu Sougoumarane, PlanetScale](https://www.youtube.com/watch?v=bd1na3mqJ7M)
- **concept** · [Day 2 with Stateful Applications - Implementing a Data Protection... - Deepika Dixit & Vaibhav Kamra](https://www.youtube.com/watch?v=4PJ6fHMFbVU). Covers designing a data protection strategy for stateful applications on Kubernetes.
- **concept** · [Deep Dive: CNCF Storage WG - Alex Chircop, StorageOS & Quinton Hoole, Huawei](https://www.youtube.com/watch?v=4giqFkBmLJ0). Deep dive into the CNCF Storage working group and its work.
- **concept** · [Intro: CNCF Storage WG - Alex Chircop, StorageOS & Quinton Hoole, Huawei](https://www.youtube.com/watch?v=JTS0WMBDPaY)
- **concept** · [Big Data Operations Using Kubernetes and Local Storage - Dan Norris, NetApp](https://www.youtube.com/watch?v=ozgOyh75hzM)
- **concept** · [Deep Dive: Rook - Travis Nielsen, Red Hat & Alexander Trost, Cloudibility](https://www.youtube.com/watch?v=Mb7oiXQb1ZE)
- **concept** · [How to Build Deep Learning Inference Through Knative Server... - Huamin Chen & Yehuda Sadeh-Weinraub](https://www.youtube.com/watch?v=-zUqmKb-BVk). Shows how to build deep learning inference on Knative serverless infrastructure.
- **concept** · [Kubernetes The Database - Jonathan Owens & Maryum Styles, New Relic](https://www.youtube.com/watch?v=eja7b3tahMg)
- **concept** · [Adding a New Storage Provider to Rook - Jared Watts, Upbound](https://www.youtube.com/watch?v=Ke0vmhnV3lc)
- **concept** · [Deep Dive: etcd - Xiang Li, Alibaba & Wenjia Zhang, Google](https://www.youtube.com/watch?v=GJqO1TYzVDE)

### 2019 · [KubeCon + CloudNativeCon China 2019 (Shanghai)](../sources/PLj6h78yzYM2Njj5PvNc4Mtcril2YyR95d.md)

- **case study** · [Two Years with Vitess: How JD.com Runs the World's Largest Vitess - Xuhaihua & Jin Ke Xie , JD.com](https://www.youtube.com/watch?v=qww4UVNG3Io) — JD.com
- **case study** · [Storage Version Migrator: Never Worry About Stale API Objects Again - Chao Xu, Google](https://www.youtube.com/watch?v=NWXC4W0dqkE) — Google
- **concept** · [TiKV Best Practices - James Zhang, PingCAP](https://www.youtube.com/watch?v=44kHIspniFs). Best practices for running and tuning TiKV.
- **concept** · [Rook Deployed Scalable NFS Clusters Exporting CephFS - Patrick Donnelly, Red Hat](https://www.youtube.com/watch?v=8yszaltPrYM). Shows how Rook deploys scalable NFS clusters exporting CephFS.
- **concept** · [Exploring High Availability in Kubernetes with Vitess - Jiten Vaidya, PlanetScale](https://www.youtube.com/watch?v=RebUhv2byyE)
- **concept** · [SPDK Based User Space NVMe Over TCP Transport Solution - Ziye Yang, Intel](https://www.youtube.com/watch?v=6Wsk0HsEzpI). Presents an SPDK-based user-space NVMe over TCP transport and its design and performance.
- **concept** · [CNCF Storage Working Group - Xing Yang, OpenSDS](https://www.youtube.com/watch?v=wAQBDBLfebc)
- **concept** · [Extending Kubernetes with Storage Transformers - Andrew Lytvynov, Google](https://www.youtube.com/watch?v=oGDb-Zm7qRQ)
- **concept** · [Deep Dive: Rook - Jared Watts, Upbound & Dmitry Yusupov, Nexenta Systems](https://www.youtube.com/watch?v=h38FCAuOehc)
- **concept** · [Intro: Vitess - Jiten Vaidya, PlanetScale & Toliver Jue, PlanetScale](https://www.youtube.com/watch?v=d_elo7uzvQY)
- **concept** · [Understanding Scalability and Performance in the Kubernetes Master - Xingyu Chen & Fansong Zeng](https://www.youtube.com/watch?v=1ThhTbMO1NE). Explains the scalability and performance characteristics of the Kubernetes master components.
- **concept** · [Benchmark Your Cloud Native Database - Josh Berkus, Red Hat](https://www.youtube.com/watch?v=Ui4RB_zQTVg)
- **concept** · [Translating Vitess: The Beginning - Roni He & Toliver Jue, PlanetScale](https://www.youtube.com/watch?v=rlZT-ACw58o)
- **concept** · [VMware SIG: Cloud Provider Moving Out of Tree+CSI - What it Mean... Steven Wong & Fabio Rapposelli](https://www.youtube.com/watch?v=9ogOnaH_JJQ). VMware SIG covers what moving the cloud provider out of tree and adopting CSI means for users.
- **concept** · [HDFS CSI Plugin: Speed Up Kubernetes in On-Premises Big Data Cluster - Yi Chen & Junping Du, Tencent](https://www.youtube.com/watch?v=GuAJFPC9pXs)
- **concept** · [Anomaly Detection for Cloud Native Storage - Seiya Takei & Xing Yang](https://www.youtube.com/watch?v=7TK9TgqITE0). Explores detecting anomalies in cloud native storage systems.
- **concept** · [Flowchain - Building Distributed Network Storage Using Blockchain Technology - Jollen Chen](https://www.youtube.com/watch?v=2d6a60vNJaY). Presents Flowchain, a distributed network storage design built on blockchain technology.
- **concept** · [Deep Dive: etcd - Jingyi Hu, Google](https://www.youtube.com/watch?v=DrtdrdwDpZE)
- **tutorial** · [Introduction to JanusGraph Database - Jason Plurad, IBM](https://www.youtube.com/watch?v=neNefqAjNYo)

### 2019 · [KubeCon + CloudNativeCon Europe 2019 (Barcelona)](../sources/PLj6h78yzYM2PpmMAnvpvsnR4c27wJePh3.md)

- **concept** · [Intro: Rook - Alexander Trost, Cloudibility & Travis Nielsen, Red Hat](https://www.youtube.com/watch?v=jFbfNWbvW9c)
- **concept** · [Benchmarking Cloud Native Storage - Josh Berkus, Red Hat](https://www.youtube.com/watch?v=4V-4yPSfN3U). Discusses approaches and challenges in benchmarking cloud native storage.
- **concept** · [Deep Dive: Rook - Jared Watts & Bassam Tabbara, Upbound](https://www.youtube.com/watch?v=ngVXcLXvcfo)
- **concept** · [Deconstructing Apache Hadoop: A Dialogue About a Cloud-Native Refactor - Anu Engineer & Marton Elek](https://www.youtube.com/watch?v=-LQDbT_HSfo). Dialogue on refactoring Apache Hadoop into a cloud-native architecture.
- **concept** · [Intro: Vitess - Sugu Sougoumarane & Deepthi Sigireddi, PlanetScale](https://www.youtube.com/watch?v=H4B5zLBfGN8)
- **concept** · [Data Without Borders - Using Rook Storage Orchestration at a Global Scale - Jared Watts, Upbound](https://www.youtube.com/watch?v=BUOIZawnIlk)
- **concept** · [Improving Availability for Stateful Applications in Kubernetes - Michelle Au, Google](https://www.youtube.com/watch?v=Cd7aJiQLIpM)
- **concept** · [Build a Kubernetes Based Cloud Native Storage Solution From Scratch - Sheng Yang, Rancher Labs](https://www.youtube.com/watch?v=XVAZ1BM_hpM)
- **concept** · [Storage Provisioning for Kubernetes on Windows - Anusha Ragunathan & Jean Rouge, Docker](https://www.youtube.com/watch?v=GyhByfDOqpY)
- **concept** · [Secrets Store CSI Driver-Bring Your Own Enterprise Secrets Store to K8s - Rita Zhang](https://www.youtube.com/watch?v=bIC4kLnrKN0)
- **concept** · [Deep Dive: Vitess - Jiten Vaidya & Dan Kozlowski, PlanetScale](https://www.youtube.com/watch?v=OZl4HrB9p-8)
- **concept** · [Intro + Deep Dive: Kubernetes Storage SIG - Saad Ali, Google](https://www.youtube.com/watch?v=PcMairR7-4U)
- **concept** · [Intro + Deep Dive: CNCF Storage WG - Alex Chircop, StorageOS](https://www.youtube.com/watch?v=V2uPGhRt4m8)
- **tutorial** · [Tutorial: Back to Basics: Hands-On Deployment of Stateful Workloads on Kubernetes - David Zhu](https://www.youtube.com/watch?v=ZvUvCA_SbJI)
- **tutorial** · [Kubernetes Storage 101 - Jan Šafránek, Red Hat & David Zhu, Google](https://www.youtube.com/watch?v=_qfSzrPn9Cs)
- **tutorial** · [Rook, Ceph, and ARM: A Caffeinated Tutorial - Federico Lucifredi & Sébastien Han, Red Hat](https://www.youtube.com/watch?v=pNz0UyaqlE8)

### 2019 · [KubeCon + CloudNativeCon North America 2019 (San Diego)](../sources/PLj6h78yzYM2NDs-iu8WU5fMxINxHXlien.md)

- **case study** · [Scaling Resilient Systems: A Journey into Slack's Database Service - Rafael Chacon & Guido Iaquinti](https://www.youtube.com/watch?v=aTItjMJE17c)
- **case study** · [Building a Database as a Service on Kubernetes - Abhi Vaidyanatha & Lucy Burns, PlanetScale](https://www.youtube.com/watch?v=469NOldFOgw) — PlanetScale. PlanetScale describes building its database as a service on Kubernetes.
- **case study** · [How to Migrate a MySQL Database to Vitess - Sugu Sougoumarane & Morgan Tocker](https://www.youtube.com/watch?v=OCS45iy5v1M)
- **case study** · [Gone in 60 Minutes: Migrating 20 TB from AKS to GKE in an Hour with Vitess - Derek Perkins, Nozzle](https://www.youtube.com/watch?v=KpygSD-v_ws) — Nozzle
- **case study** · [Running Large-Scale Stateful Workloads On Kubernetes at Lyft - Surinder Singh & Anmol Khurana, Lyft](https://www.youtube.com/watch?v=ECeVQoble0g) — Lyft
- **concept** · [Intro: OpenEBS - Amit Kumar Das, MayaData & Vishnu Itta, MayaData](https://www.youtube.com/watch?v=0I54gMUqWmE). Introduction to the OpenEBS container-attached storage project.
- **concept** · [Building Blocks: How Raw Block PVs Changed the Way We Look at Storage - Jose A. Rivera & Rohan Gupta](https://www.youtube.com/watch?v=5j4ViEfVcWg). Explains how raw block persistent volumes work in Kubernetes and how they change storage design.
- **concept** · [How to Backup and Restore Your Kubernetes Cluster - Annette Clewett & Dylan Murray, Red Hat](https://www.youtube.com/watch?v=JyzgS-KKuoo)
- **concept** · [Beyond Storage Management - Andrew Large & Yinan Li, Google](https://www.youtube.com/watch?v=m-9MX9Pxh6A)
- **concept** · [Vitess: Stateless Storage in the Cloud - Sugu Sougoumarane, PlanetScale](https://www.youtube.com/watch?v=z63dtNj6ctY)
- **concept** · [KubeDirector - Deploying Complex Stateful Applications on Kubernetes - Joel Baxter & Thomas Phelan](https://www.youtube.com/watch?v=X2kEk5wLe9g)
- **concept** · [Rook: Cloud-Native Storage Orchestr... Jared Watts, Bassam Tabbara, Travis Nielsen & Alexander Trost](https://www.youtube.com/watch?v=f3Wyk968VR8)
- **concept** · [Storage on Kubernetes - Learning From Failures - Hemant Kumar & Jan Šafránek, Red Hat](https://www.youtube.com/watch?v=zuGjw595OiQ)
- **concept** · [Kubernetes Storage Cheat Sheet for VM Administrators - Manu Batra & Jing Xu, Google](https://www.youtube.com/watch?v=Qbfp2QJ-Png)
- **concept** · [Intro: vSphere Cloud Provider and CSI - Fabio Rapposelli, VMware](https://www.youtube.com/watch?v=o6e_mYBfTng)
- **concept** · [Intro to the CNCF SIG Storage - Quinton Hoole, Futurewei & Alex Chircop, StorageOS](https://www.youtube.com/watch?v=-OMC0k5gIkQ). Introduction to the CNCF SIG Storage and its work.
- **concept** · [Intro + Deep Dive: Kubernetes Storage SIG - Saad Ali, Google](https://www.youtube.com/watch?v=UdwiJRPRoho)
- **concept** · [How Container Networking Affects Database Performance - Tyler Duzan & Vadim Tkachenko, Percona](https://www.youtube.com/watch?v=EXqEzZPm4I0)
- **concept** · [CSI Volume Snapshots: On the Way to Faster and Better Backups - Adnan Abdulhussein & Nolan Brubaker](https://www.youtube.com/watch?v=CbA40krYZf0)
- **concept** · [Geo-partitioning with Vitess - Deepthi Sigireddi, PlanetScale & Jitendra Vaidya, PlanetScale](https://www.youtube.com/watch?v=-Hz6LFJu1cY). Explains how Vitess supports geo-partitioning of data across regions.
- **tutorial** · [Cortex 101: Horizontally Scalable Long Term Storage for Prometheus - Chris Marchbanks, Splunk](https://www.youtube.com/watch?v=f8GmbH0U_kI)
- **tutorial** · [Intro to Longhorn: Open Source Cloud-Native Distributed Block Storage Built On and For... Sheng Yang](https://www.youtube.com/watch?v=hvVnfZf9V6o)

### 2020 · [KubeCon + CloudNativeCon Europe 2020 - Virtual](../sources/PLj6h78yzYM2O1wlsM-Ma-RYhfT5LKq0XC.md)

- **case study** · [Speed Racer: Local Persistent Volumes in Production - Matt Schallert, Chronosphere](https://www.youtube.com/watch?v=6RjjtSpLar0) — Chronosphere. Chronosphere shares its experience running local persistent volumes in production for performance.
- **case study** · [Vitess Intro: How to Migrate a MySQL Database to Vitess - Sugu Sougoumarane & Morgan Tocker](https://www.youtube.com/watch?v=WRNftOqRVVY)
- **concept** · [etcd Watchers Not Working? Improving Error Handling in Your Applications - Guillermo Nunez, IBM](https://www.youtube.com/watch?v=ftfZli-BvJ8)
- **concept** · [Five Great Ways to Lose Data on Kubernetes (And How to Avoid Them) - Robert Hodges, Altinity LTD](https://www.youtube.com/watch?v=zW7gLyPln3w)
- **concept** · [Zero Database Downtime with etcd-operator - Tyler Lisowski & Kodie Glosser, IBM](https://www.youtube.com/watch?v=Za9RkS42nbU)
- **concept** · [Cloudstate—Towards Stateful Serverless - Jonas Bonér & James Roper, Lightbend](https://www.youtube.com/watch?v=D3bYGIo2kiQ)
- **concept** · [Multicloud Vitess over Network Service Mesh - Tim Swanson, Cisco & John Watson, PlanetScale](https://www.youtube.com/watch?v=NulLc7DxXg8)
- **concept** · [Zero Downtime Data Relocation with Vitess - Liz van Dijk & Deepthi Sigireddi, PlanetScale](https://www.youtube.com/watch?v=6--4bQKMNF4). Shows how Vitess relocates data with zero downtime.
- **concept** · [TiKV: A Cloud Native Key-Value Database - Dongxu Huang & Nick Cameron, PingCAP](https://www.youtube.com/watch?v=1B4riWTTAZg). Describes the design of TiKV, a cloud native distributed key-value database.
- **concept** · [Sponsor Demo: VMware- Cluster API in TKG Service Architecture and Data Protection on TMC and Velero](https://www.youtube.com/watch?v=ON1Lc_j1PAY)
- **concept** · [Is There a Place For Distributed Storage For AI/ML on Kubernetes? - Diane Feddema & Kyle Bader](https://www.youtube.com/watch?v=9XhbXtPKttM). Discusses the role of distributed storage for AI/ML workloads on Kubernetes.
- **concept** · [Rook Deep Dive: Ceph - Travis Nielsen & Sebastien Han, Red Hat](https://www.youtube.com/watch?v=eTSokJ3-c-A)
- **concept** · [Performance Optimization – Rook on Kubernetes - Mark Darnell & Ryan Tidwell, SUSE](https://www.youtube.com/watch?v=v1u6bPM4SQU)
- **concept** · [Serving Trillion-Record Table on TiKV - Yi Wu, PingCAP](https://www.youtube.com/watch?v=TcxtkWjSo44)
- **concept** · [Introduction to Data Protection WG in Kubernetes - Xing Yang, VMware & Xiangqian Yu, Google](https://www.youtube.com/watch?v=6lVJcskauTU). Introduces the Kubernetes Data Protection Working Group and its goals.
- **concept** · [Stateful Serverless and the Elephant in the Room - Stephan Ewen, Ververica](https://www.youtube.com/watch?v=7iAvBcMtaKI). Explores the challenges of stateful serverless and how Flink approaches state.
- **concept** · [It’s a Polyglot World of Stateless Functions and Stateful Actors - Yaron Schneider & Aman Bhardwaj](https://www.youtube.com/watch?v=cut8YazrUhM)
- **concept** · [How to Use Kubernetes to Build a Data Lake for AI Workloads - Peter MacKinnon & Uday Boppana](https://www.youtube.com/watch?v=0HIelZ3qMLE). Shows how to build a data lake for AI workloads on Kubernetes.
- **tutorial** · [Intro to Rook: Storage for Kubernetes - Jared Watts, Upbound & Alexander Trost, Cloudical](https://www.youtube.com/watch?v=dA29dIK6g5o)
- **tutorial** · [Intro to Longhorn: Open Source Cloud-Native Storage For K8s - Sheng Yang, Rancher Labs](https://www.youtube.com/watch?v=zJY2uxLtwUk)
- **tutorial** · [OpenEBS 101: Hyperconverged Kubernetes Native Storage - Kiran Mova & Vishnu Itta, MayaData](https://www.youtube.com/watch?v=ELqukg4HrPg)
- **tutorial** · [CNCF SIG Storage – An Intro to Cloud Native Storage - Alex Chircop, StorageOS & Erin Boyd, Red Hat](https://www.youtube.com/watch?v=Ofw6gpvvROk)

### 2020 · [KubeCon + CloudNativeCon North America 2020 - Virtual](../sources/PLj6h78yzYM2Pn8RxfLh2qrXBDftr6Qjut.md)

- **case study** · [Codename VIFL - How to Migrate MySQL Database Clusters to Vitess - Guido Iaquinti & Rafael Chacon](https://www.youtube.com/watch?v=k51L0xdClGQ)
- **case study** · [Improved TiKV Observability: How We Trace Events under Nanoseconds Latency- Wish Shi & Zhenchi Zhong](https://www.youtube.com/watch?v=50ExGNo1vao) — PingCAP. PingCAP engineers describe how they improved TiKV observability to trace events at nanosecond latency.
- **concept** · [TiFlash: Make TiKV 10x Faster and HTAP-able - Xiaoyu Ma & Liquan Pei, PingCAP](https://www.youtube.com/watch?v=Wob_D0ZWF1c)
- **concept** · [Rook: Intro and Ceph Deep Dive - Blaine Gardner, Alexander Trost, & Travis Nielsen, Sébastien Han](https://www.youtube.com/watch?v=aO-n4FuOU2w)
- **concept** · [Whatever Can Go Wrong, Will Go Wrong – Rook/Ceph and Storage Failures - Sagy Volkov, Red Hat](https://www.youtube.com/watch?v=e0_M1Keed6M)
- **concept** · [The Stateful Landscape: The Then and Now and the Future - Erin Boyd, Quinton Hoole & Alex Chircop](https://www.youtube.com/watch?v=mo5Te2xiiU4)
- **concept** · [Optimizing Storage Assignment via Pod Scheduling Under Disturbance Factors - Kenji Morimoto, Cybozu](https://www.youtube.com/watch?v=P5wQmyby8GI)
- **concept** · [Vitess: Introduction and New Features - Sugu Sougoumarane & Deepthi Sigireddi, Planetscale, Inc.](https://www.youtube.com/watch?v=Nqzhgzg5WCw)
- **concept** · [Elastic Scheduling with TiKV - Song Gao & Yutong Liang, PingCAP](https://www.youtube.com/watch?v=rY2h-0TZaEo)
- **concept** · [Beyond File and Block Storage in Kubernetes - Sidhartha Mani, MinIO](https://www.youtube.com/watch?v=Y3GgJb71Cwo)
- **tutorial** · [Tutorial: Introduction to Using the Container Storage Interface (CSI) Primitives - Michael Mattsson](https://www.youtube.com/watch?v=AnfAd6goq-o)
- **tutorial** · [Hands-On Stateful Serverless Applications with K8s and Stateful Functions - Seth Wiesman, Ververica](https://www.youtube.com/watch?v=CPbN_adhxsQ)

### 2021 · [KubeCon + CloudNativeCon + Open Source Summit China 2021](../sources/PLj6h78yzYM2PjmJ9A98QCXnMsmONhU--t.md)

- **case study** · [How to Efficiently Manage Tens of Thousands of etcd Clusters? - Cong Tang & Chaofan Wang, Tencent](https://www.youtube.com/watch?v=6o_5D02NYmQ) — Tencent. Tencent describes how it manages tens of thousands of etcd clusters in production.
- **concept** · [Rook: Intro and Ceph Deep Dive - Travis Nielsen, Red Hat & Satoru Takeuchi, Cybozu, Inc.](https://www.youtube.com/watch?v=UG2AQ9SCAE4)
- **concept** · [Protect your database workloads in Kubernetes - Yang Liu & Yongjie Gong, Shanghai Jibu Technology Co](https://www.youtube.com/watch?v=G-S3ewNLq_Y)
- **concept** · [Milvus 2.0: A Vector Database With Cloud-Native Architecture - Xiaomeng Yi, Zilliz](https://www.youtube.com/watch?v=0WdIZarlPYs). Presents the cloud-native architecture of Milvus 2.0 vector database.
- **concept** · [Kubernetes SIG Storage Introduction and Update - Xing Yang, VMware & Michelle Au, Google](https://www.youtube.com/watch?v=H5P1miRL8vc)
- **concept** · [Keep Persistent Volumes Healthy for Stateful Workloads - Xing Yang, VMware & Yuquan Ren, ByteDance](https://www.youtube.com/watch?v=TJr8dmUM0Dw)
- **concept** · [Continuous Performance Benchmarking for Vitess - Alkin Tezuysal & Florent Poinsard & Manan Gupta](https://www.youtube.com/watch?v=fLullHPddvg)
- **concept** · [Cloud Native Storage: Storage TAG intro, Projects, Landscape & T... Alex Chircop & Raffaele Spazzoli](https://www.youtube.com/watch?v=_OkGsyc4h3w)

### 2021 · [KubeCon + CloudNativeCon Europe 2021](../sources/PLj6h78yzYM2MqBm19mRz9SYLsw4kfQBrC.md)

- **case study** · [Lessons Learned from Operating ETCD - Pierre Zemb, OVHcloud](https://www.youtube.com/watch?v=IrJyrGQ_R9c) — OVHcloud
- **concept** · [Graduated Project Lightning Talk: Rook: Enterprise Storage for Kubernetes - Travis Nielsen, Red Hat](https://www.youtube.com/watch?v=x0Bm9Gi8xg0)
- **concept** · [Secrets Store CSI Driver: Keeping Secrets Secret - Anish Ramasekar, Microsoft & Tommy Murphy, Google](https://www.youtube.com/watch?v=w0k7MI6sCJg)
- **concept** · [Rook: Intro and Ceph Deep Dive - Blaine Gardner, Red Hat & Satoru Takeuchi, Cybozu, Inc.](https://www.youtube.com/watch?v=j86OXjC1Jr8)
- **concept** · [CSI Volume Attacks – The SRE Strikes Back - Hendrik Land, NetApp](https://www.youtube.com/watch?v=A9IwOHGt7gM). Examines attacks via CSI volumes and how SREs can defend against them.
- **concept** · [Cloud Native Distributed Event Streaming from TiKV - Zixiong Liu, PingCAP](https://www.youtube.com/watch?v=lnXeONAaQfs)
- **concept** · [Graduated Project Lightning Talk: Time to Live (TTL) Support for TiKV - Bokang Zhang](https://www.youtube.com/watch?v=6Nojm3xnKl0). Lightning talk on adding time-to-live support to TiKV.
- **concept** · [Graduated Project Lightning Talk: Vitess, are we Fast Yet? - Akilan Selvacoumar, Florent Poinsard](https://www.youtube.com/watch?v=h1bd1yxA4ec)
- **concept** · [Sponsored Session: Kasten - Introducing Kubestr: Identify, Validate, & Evaluate Storage in Kubern...](https://www.youtube.com/watch?v=vqnwnWI2sJQ)
- **concept** · [Cloud Native Storage - a View of the Landscape, Projects... Alex Chircop, Xing Yang & Quinton Hoole](https://www.youtube.com/watch?v=mEUv92PFJwU)
- **concept** · [Sponsored Session: Commvault - Many Apps. Many Locations. One Storage Solution.](https://www.youtube.com/watch?v=Az2dq4KwwfA)
- **keynote** · [Sponsored Lightning Talk: How to Follow the 3-2-1 Backup Rule in Kubernetes - Michael Cade, Kasten](https://www.youtube.com/watch?v=5wRt1bJfKBw). Sponsored lightning talk on applying the 3-2-1 backup rule in Kubernetes.

### 2021 · [KubeCon + CloudNativeCon North America 2021](../sources/PLj6h78yzYM2Nd1U4RMhv7v88fdiFqeYAP.md)

- **case study** · [How We Reduced Write Latency in TiKV? - Liqi Geng, PingCAP](https://www.youtube.com/watch?v=3BefLqw-4Go) — PingCAP. PingCAP explains how it reduced write latency in its own TiKV storage engine.
- **case study** · [What You Need to Know Before Using Local Persistent Volumes - Sebastien Guilloux, Elastic](https://www.youtube.com/watch?v=8TskPf51wgI) — Elastic. Elastic shares what it learned using local persistent volumes in Kubernetes.
- **case study** · [Large-Scale Practice of Persistent Memory in Alibaba Cloud - Junbao Kan & Qingcan Wang, Alibaba](https://www.youtube.com/watch?v=3MKbk7AS8Jw) — Alibaba Cloud. Alibaba Cloud reports on its large-scale production use of persistent memory with Kubernetes.
- **case study** · [Context Aware Traffic Routing for Stateful Services using Envoy - Renana Yacobi & Piaw Na, Niantic](https://www.youtube.com/watch?v=0W7aYTjtVwM) — Niantic. Niantic describes using Envoy for context-aware traffic routing of its stateful services.
- **concept** · [Taking Your Database Beyond the Border of a Single Kubernetes Cl... Christopher Bradford & Ty Morton](https://www.youtube.com/watch?v=Fz3CYmil_Yg)
- **concept** · [Real-Time Data Anonymization the Serverless Way - Yuval Lifshitz & Huamin Chen, Red Hat](https://www.youtube.com/watch?v=1E5Q-ErF2sI). Shows how to anonymize data in real time using a serverless approach on Kubernetes.
- **concept** · [Disaster Recovery of Stateful Applications in a Multi-Cl... Orit Wasserman & Shyamsundar Ranganathan](https://www.youtube.com/watch?v=1TSeilqoHSg). Shows how to design disaster recovery for stateful apps across multiple clusters.
- **concept** · [Postgres Extensions in Kubernetes - Álvaro Hernández, OnGres](https://www.youtube.com/watch?v=hCp6p-0cxco)
- **concept** · [Storage and Networking: Rook on Multus - Sébastien Han & Rohan Gupta, Red Hat](https://www.youtube.com/watch?v=zIS5qaG_HRw)
- **concept** · [Rook: Intro and Ceph Deep Dive - Travis Nielsen, Sebastien Han, Blaine Gardner & Satoru Takeuchi](https://www.youtube.com/watch?v=VBVVqiKvlCI)
- **concept** · [Kubernetes SIG Storage Introduction and Update - Xing Yang, VMware & Michelle Au, Google](https://www.youtube.com/watch?v=-r8t24qVvUA). Kubernetes SIG Storage introduces its work and gives an update on recent and upcoming storage features.
- **concept** · [Vitess: Intro and New Features - Deepthi Sigireddi, Alkin Tezuysal, Andrew Mason & Malcolm Akinje](https://www.youtube.com/watch?v=uKdMR89mfdE)
- **concept** · [How to put a Database in Kubernetes - Jeffrey Carpenter, DataStax](https://www.youtube.com/watch?v=UgtYlvIv36Q)
- **concept** · [Thanos: Highly Available, Pluggable, Long Term Metric Storage for Everyone!- Wiard van Rij, Fullstaq](https://www.youtube.com/watch?v=VG_TtLg84ME)
- **concept** · [Cloud Native Storage: Storage TAG Intro, Projects, Landscape &... Alex Chircop & Raffaele Spazzoli](https://www.youtube.com/watch?v=8EGaImhCBFI). The CNCF Storage TAG introduces its projects and the cloud native storage landscape.

### 2022 · [KubeCon + CloudNativeCon Europe 2022](../sources/PLj6h78yzYM2MCEgkd8zH0vJWF7jdQ-GRR.md)

- **concept** · [Rook: Intro and Deep Dive with Ce... Travis Nielsen, Sebastien Han & Blaine Gardner, Satoru Takeuchi](https://www.youtube.com/watch?v=TwGJsTa3F2g)
- **concept** · [Adapting TiKV for Cloud Storage - Xinye Tao & Jinpeng Zhang, PingCAP](https://www.youtube.com/watch?v=hzzHn6oiOp8)
- **concept** · [Cloud Native Storage: The CNCF Storage TAG, Projects... Alex Chircop, Xing Yang, Raffaele Spazzoli](https://www.youtube.com/watch?v=lqDaOxGHbPM)
- **concept** · [Kubernetes SIG Storage Deep Dive - Xing Yang, VMware & Jan Šafránek, Red Hat](https://www.youtube.com/watch?v=dsEeQqRSg74)
- **concept** · [Scaling Databases with Vitess - Harshit Gangal & Manan Gupta, Planetscale](https://www.youtube.com/watch?v=HgSlmzC7O-E)

### 2022 · [KubeCon + CloudNativeCon North America 2022](../sources/PLj6h78yzYM2O5aNpRM71NQyx3WUe1xpTn.md)

- **case study** · [Migrating From Single-Node Kubernetes Control Plane To HA In Product... Cong Yue & David Oppenheimer](https://www.youtube.com/watch?v=7nLvblrEaDQ) — Google. Describes migrating a single-node Kubernetes control plane to HA in production.
- **case study** · [Multi-Cluster Stateful Set Migration: A Solution To Upgrade Pain - Peter Schuurman & Matt Schallert](https://www.youtube.com/watch?v=hkyUqgwTZL8)
- **case study** · [How We Make TiKV- a Distributed Storage, More Cost-Effective On the Cloud - Sunny Bains & Yang Zhang](https://www.youtube.com/watch?v=vYMbmb01IsU)
- **case study** · [Lessons Learned From Etcd the Data Inconsistency Issues - Marek Siarkowicz & Benjamin Wang](https://www.youtube.com/watch?v=_nSJ_vozyqk)
- **concept** · [Data On Kubernetes, Deploying And Running PostgreSQL And... - Chris Milsted & Gabriele Bartolini](https://www.youtube.com/watch?v=99uSJXkKpeI). Covers how to deploy and run PostgreSQL on Kubernetes using an operator.
- **concept** · [Stateful Apps On Kubernetes - Bring Them On!](https://www.youtube.com/watch?v=x8MJlUNhsO0)
- **concept** · [Storage Wars - Seán C McCord, Sidero Labs](https://www.youtube.com/watch?v=dfDb-Z8y7lo)
- **concept** · [Lightning Talk: Back To Basics: How To Measure Etcd Performance And Not To... David Perez Rodriguez](https://www.youtube.com/watch?v=efzlFKRqK3E)
- **concept** · [Stateless Collectors For Stateful Data: Scaling Prometheus As a Node Agent - Danny Clark, Google](https://www.youtube.com/watch?v=yk2aaAyxgKw)
- **concept** · [One VTOrc To Rule Them All – High Availability In a Distributed Database System - Deepthi & Manan](https://www.youtube.com/watch?v=upmByX8uD6E)
- **concept** · [So, What If I Don’t Want My Persistent Storage To Be Yet Another Bindmount? -Deep Debroy & Feng Wang](https://www.youtube.com/watch?v=h3z8Jl0NP1I)
- **concept** · [Vitess: Introduction And New Features - Deepthi Sigireddi, Matt Lord & Rohit Nayak, PlanetScale](https://www.youtube.com/watch?v=cPQuj4eTCdY)
- **concept** · [Rook: Intro And Deep Dive With...- Travis Nielsen & Blaine Gardner, Alexander Trost, Satoru Takeuchi](https://www.youtube.com/watch?v=qhfRG04Qa84)
- **concept** · [Kubernetes SIG Storage Deep Dive - Xing Yang, VMware & Mauricio Poppe, Google](https://www.youtube.com/watch?v=_XXn3-yDZA0)
- **concept** · [Cloud Native Storage: The CNCF Storage TAG, Projects, Technology...- Alex Chircop, Raffaele Spazzoli](https://www.youtube.com/watch?v=UuflBTeM_Hw)

### 2023 · [KubeCon + CloudNativeCon + Open Source Summit China 2023](../sources/PLj6h78yzYM2OJcjIuAsbbhXAaDrAnuKRB.md)

- **concept** · [Post-Exploiting a Compromised ETCD - Luis Toro Puig, NCC Group](https://www.youtube.com/watch?v=qtDV3GPoBdE)
- **concept** · [Best Practice for Cloud Native Storage in Finance Industry - Yang Cao & Jie Chu, Alex Zheng](https://www.youtube.com/watch?v=WPgpbKuU7FE)
- **concept** · [Build a High Performance Remote Storage for Prometheus with Unlimited Time Series - Yang Xiang](https://www.youtube.com/watch?v=7pQZyYEz1l4). Presents a high performance remote storage design for Prometheus with unlimited time series.
- **concept** · [Kubernetes Data Protection WG Deep Dive - Xiangqian Yu, Google](https://www.youtube.com/watch?v=1jYrKcdOO8s). Deep dive into the Kubernetes Data Protection working group's goals and backup-related designs.
- **concept** · [Cloud Native Storage CubeFS, Empowering AI Acceleration - Hu Yao, OPPO](https://www.youtube.com/watch?v=JOio7Nps_II)
- **concept** · [Cloud Native Storage: Storage TAG Intro, Projects... - Alex Chircop, Xing Yang, Raffaele Spazzoli](https://www.youtube.com/watch?v=14AD4Ec1_U0). Introduces the Storage TAG and the storage projects in the CNCF landscape.
- **concept** · [Kubernetes SIG Storage Intro & Deep Dive - Xing Yang, VMware & Michelle Au, Google](https://www.youtube.com/watch?v=SPfJrDnnprs)

### 2023 · [KubeCon + CloudNativeCon Europe 2023](../sources/PLj6h78yzYM2PyrvCoOii4rAopBswfz1p7.md)

- **case study** · [Tales from on-Call: Fun with Operating Etcd at Scale - Geeta Gharpure & Chao Chen, Amazon](https://www.youtube.com/watch?v=p4o0eSS_ANI) — Amazon
- **concept** · [Kubernetes SIG Storage: Intro and Deep Dive - Xing Yang, VMware & Jan Šafránek, Red Hat](https://www.youtube.com/watch?v=zZFN9KMs5sI)
- **concept** · [Rook: Intro and Deep Dive with...Travis Nielsen & Blaine Gardner, Alexander Trost & Deepika Upadhyay](https://www.youtube.com/watch?v=2LAJfLL_cfM). Intro and deep dive on Rook, the cloud-native storage orchestrator for Ceph.
- **concept** · [On the Hunt for Etcd Data Inconsistencies - Marek Siarkowicz, Google](https://www.youtube.com/watch?v=IIMs0EjQZHg)
- **concept** · [Cloud Native Storage: The CNCF Storage TAG, Projects, Technology & Landscape - Chircop & Spazzoli](https://www.youtube.com/watch?v=-Nn5VXsSUNQ). Overview of the CNCF Storage TAG, its projects and the cloud native storage landscape.
- **concept** · [Kubernetes Database Operators Landscape - Xing Yang, Melissa Logan, Sergey Pronin, Alvaro Hernandez](https://www.youtube.com/watch?v=TmDdkBPW_hI)
- **concept** · [Setting up Etcd with Kubernetes to Host Clusters with Thousands of Nodes - M Zięba & L Bernaille](https://www.youtube.com/watch?v=_Zhf_iJMqwE)
- **concept** · [Autoscaling Elastic Kubernetes Infrastructure for Stateful... - Sanjay Pujare & Costin Manolache](https://www.youtube.com/watch?v=3cJIDvePywk). Explains how to autoscale elastic Kubernetes infrastructure for stateful workloads.
- **concept** · [Metrics at Full Throttle: Intro and Deep Dive Into Thanos - Saswata Mukherjee & Filip Petkovski](https://www.youtube.com/watch?v=2GokLB5_VfY). Introduction to Thanos plus a deep dive into its architecture and recent improvements.
- **concept** · [Bring Elastic and Resilient Multi-Tenancy to TiKV - Ping Yu & Shuning Chen, PingCAP](https://www.youtube.com/watch?v=rMKeBP-g8o0)
- **concept** · [Availability and Storage Autoscaling of Stateful Workloads on Kubernetes - Leila Vayghan](https://www.youtube.com/watch?v=a0aNdOUDqhA)
- **tutorial** · [Introduction to Vitess and Real World Usage - Arthur Schreiber, Github & Florent Poinsard](https://www.youtube.com/watch?v=C2DsT1_zK_4)

### 2023 · [KubeCon + CloudNativeCon NA 2023](../sources/PLj6h78yzYM2MYc0X1465RzF_7Cqf7bnqL.md)

- **case study** · [Zero-Downtime Live Migration of Stateful VMs on Kubernetes - Felicitas Pojtinger, Loophole Labs](https://www.youtube.com/watch?v=HrtX0JrjekE) — Loophole Labs
- **case study** · [Scale Your MySQL Database by Migrating to Vitess - Matt Lord & Deepthi Sigireddi, PlanetScale](https://www.youtube.com/watch?v=vvDhlv3zxWM) — PlanetScale
- **case study** · [Journey Through Time: Understanding Etcd Revisions and Resource Versions in... - Priyanka Saggu](https://www.youtube.com/watch?v=i7RCoEjAMOo)
- **concept** · [The Best Practice of Machine Learning Platform Storage Based on CubeFS - Leon Chang, OPPO](https://www.youtube.com/watch?v=T8IjKLU9DWw)
- **concept** · [Disaster Recovery with Very Large Postgres Databases - Gabriele Bartolini, EDB & Michelle Au, Google](https://www.youtube.com/watch?v=WGQq4MWzW6E)
- **concept** · [Cloud Native Storage:the CNCF Storage TAG, Projects, Technology... Raffaele Spazzoli & Alex Chircop](https://www.youtube.com/watch?v=pUF3Gg4ooXY)
- **concept** · [Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, VMware & Michelle Au, Google](https://www.youtube.com/watch?v=spyEgGcqwFs)
- **concept** · [Forging a Stronger Bond Between Etcd and Kubernetes - Marek Siarkowicz, Wenjia Zhang & James Blair](https://www.youtube.com/watch?v=6JYgBJAjpNQ). Maintainers describe work to tighten the integration between etcd and Kubernetes.
- **concept** · [Rook: Intro and Deep Dive with Ce... Travis Nielsen, Annette Clewett, Blaine Gardner & Dmitry Mishin](https://www.youtube.com/watch?v=z8MPuL6s6HY)
- **concept** · [Secrets of Running Etcd - Marek Siarkowicz, Google](https://www.youtube.com/watch?v=aJVMWcVZOPQ)
- **concept** · [The Kubernetes Storage Layer: Peeling the Onion Minus the Tears - Madhav Jivrajani, VMware](https://www.youtube.com/watch?v=TNNJFtfy7iU)
- **concept** · [Adventures in Data- Leaning on Kubernetes Storage to Run Hundreds of Real-Time Anal... Robert Hodges](https://www.youtube.com/watch?v=ogN_DOHJTIY)
- **concept** · [Data on Kubernetes Operator Maturity- Melissa Logan, Michelle Au, Robert Hodges & Gabriele Bartolini](https://www.youtube.com/watch?v=IQrBFYSSES4)
- **concept** · [SECURITY HUB UNCONFERENCE: STRIDE threat model for the vSphere CSI Driver](https://www.youtube.com/watch?v=1LIQFDc8CrQ). Unconference session applying the STRIDE threat model to the vSphere CSI driver.
- **tutorial** · [Tutorial: Mastering Etcd Observability: A Comprehensive Guide to M... Bogdan Kanivets & Vivek Patani](https://www.youtube.com/watch?v=GtAIwwJ5EJk)

### 2024 · [KubeCon + CloudNativeCon + Open Source Summit + AI_dev China 2024](../sources/PLj6h78yzYM2NcAGHRxgBHY8x3QTfnZQCv.md)

- **concept** · [The Challenges of Kubernetes Data Protection - Real Examples and Solutions... Wenkai Yin & Bruce Zou](https://www.youtube.com/watch?v=7uHYWtRi0-Q). Presents challenges of Kubernetes data protection with real examples and solutions, based on Velero.
- **concept** · [Beyond Statefulset: Containerize Your Enterprise Stateful Applications... - Mingshan Zhao & Vec Sun](https://www.youtube.com/watch?v=nCJAus3-6d8)
- **concept** · [JuiceFS CSI in Multi-Thousand Node Kubernetes Clusters for LLM Pre-Training - Weiwei Zhu](https://www.youtube.com/watch?v=DmzZHjl-vck)
- **concept** · [Deep Dive Into Windows CSI Driver HostProcess Containers - Andy Zhang (OSTC) & Weizhi Chen](https://www.youtube.com/watch?v=l8cGRq077gk)
- **concept** · [Building a High-Performance Time Series Database from Scratch:...- Aliaksandr Valialkin & Hui Wang](https://www.youtube.com/watch?v=uHu0OrniRSg)
- **concept** · [Power TiKV with in-Memory Engine | 使用内存引擎强化 TiKV - Chenjie Tang, PingCAP](https://www.youtube.com/watch?v=wXwsEu4AFqA)
- **concept** · [How to Manage Database Clusters Without a Dedicated Operator - Shanshan Ying, ApeCloud & Shun Ding](https://www.youtube.com/watch?v=i894E5o36EI)
- **concept** · [Time Series Database on Kubernetes: Efficient Management of Massive Internet of Vehi... - Vicky Lee](https://www.youtube.com/watch?v=uwpxWMqwNvQ)
- **concept** · [Project Lightning Talk: Explore Secure Artifacts Storage and Management with Harbor](https://www.youtube.com/watch?v=3mQJ43OXso8). Lightning talk on secure artifact storage and management with the Harbor registry.

### 2024 · [KubeCon + CloudNativeCon Europe 2024](../sources/PLj6h78yzYM2N8nw1YcqqKveySH6_0VnI0.md)

- **case study** · [Hacking Kubernetes to Migrate in-Tree Volumes to CSI - Baptiste Girard-Carrabin & Antoine Gaillard](https://www.youtube.com/watch?v=sVQtO55910I)
- **case study** · [Fantastic Ordinals and How to Avoid Them: Auto-Scaling Challenges in a Cloud Database](https://www.youtube.com/watch?v=AFoMsLMZKik). Describes auto-scaling challenges with StatefulSet ordinals when operating a cloud database.
- **case study** · [From UI to Storage: Unraveling the Magic of Thanos Query Processing](https://www.youtube.com/watch?v=ZGQIitaKoTM)
- **concept** · [Object Storage on Kubernetes? Completed It with Provider Ceph. - Conor Nolan & Richard Kovacs](https://www.youtube.com/watch?v=tZhDQpmzaS0)
- **concept** · [Unleash the Power of etcd: What Can an E[Xtensible]-etcd Bring? - Siyuan Zhang & Bogdan Kanivets](https://www.youtube.com/watch?v=VL9111ony2k)
- **concept** · [We Tested and Compared 6 Database Operators. The Results are In!](https://www.youtube.com/watch?v=l33pcnQ4cUQ)
- **concept** · [Kubernetes Data Protection WG Deep Dive - Dave Smith-Uchida, Veeam](https://www.youtube.com/watch?v=2rfMgYRNoPo). Deep dive into the Kubernetes Data Protection Working Group's goals and progress.
- **concept** · [Scaling Heights: Mastering Postgres Database Vertical Scalability... Gabriele Bartolini & Gari Singh](https://www.youtube.com/watch?v=LArl0VWxr3Y)
- **concept** · [Etcd 3.6 and Beyond - Wenjia Zhang, Marek Siarkowicz & Siyuan Zhang, Benjamin Wang](https://www.youtube.com/watch?v=b93U1ekv0Fc)
- **concept** · [Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, VMware & Jan Šafránek, Red Hat](https://www.youtube.com/watch?v=pnNTd4VlWFQ)
- **concept** · [CRD Vs Dedicated etcd as Storage Backend : Lessons from Taming High Churn Clusters](https://www.youtube.com/watch?v=o_LutIRlv-A)
- **concept** · [OCI as a Standard for ML Artifact Storage and Retrieval - Peyman Norouzi & Eric Koepfle, Bloomberg](https://www.youtube.com/watch?v=hGM5KQLzbYc)
- **concept** · [AI, Edge, and Storage Walk Into a Mongolian Mine - Reza Jelveh, SoftSage Solutions OU](https://www.youtube.com/watch?v=t7alW_Hjfj8)
- **concept** · [Accelerating Kubernetes Data Intensive APPs with Cloud Native Local Storage](https://www.youtube.com/watch?v=ttC8MeqTYII)
- **concept** · [Rook: Intro and Deep Dive with Ceph](https://www.youtube.com/watch?v=bL5Ay28KPOI)
- **concept** · [Vitess: Introduction, New Features and the Vinted User Story](https://www.youtube.com/watch?v=uRB-Qni_bCM)
- **concept** · [Cloud Native Storage: The CNCF Storage TAG Projects, Technology & Landscape](https://www.youtube.com/watch?v=MyhVUs69va0)
- **concept** · [CNCF Storage TAG and the Cloud Native Storage Landscape | TAG Lightning Talk](https://www.youtube.com/watch?v=Jpw5Yif0od0)

### 2024 · [KubeCon + CloudNativeCon India 2024](../sources/PLj6h78yzYM2P0vFbS4o1I0gRHSiXgLiEe.md)

- **case study** · [From Chaos to Control: Building Resilience with Effective Backup and Disaster Recov... - Yash Pimple](https://www.youtube.com/watch?v=Cr-yvnnYGv0)
- **concept** · [Rook: Intro and Deep Dive with Ceph Storage - Subham Rai, Yati Padia & Parth Arora, Deepika Upadhyay](https://www.youtube.com/watch?v=MIaRp-lUeo4)
- **concept** · [What's New with etcd, The Backbone of Kubernetes: Project Updates and New Features - Arka Saha](https://www.youtube.com/watch?v=H7nvOMrMGPU)
- **concept** · [Using vectordb for Data on S3 Bucket - Jiffin Tony Thottan, IBM](https://www.youtube.com/watch?v=-jAA-ba1KOI). Shows how to use a vector database with data stored in S3 buckets.
- **tutorial** · [Introduction to Vitess: Scalable Database for Modern Applications - Manan Gupta & Harshit Gangal](https://www.youtube.com/watch?v=PM213WqA-vg)

### 2024 · [KubeCon + CloudNativeCon NA 2024 - Salt Lake City](../sources/PLj6h78yzYM2Pw4mRw4S-1p_xLARMqPkA7.md)

- **case study** · [Vitess: Introduction, New Features & Running in Production- D. Sigireddi, D. Perkins, S. Vijayakumar](https://www.youtube.com/watch?v=MZXToqM8mds)
- **case study** · [Lightning Talk: Future-Proofing Kubernetes: Impact of Storage Version Migration and... N. Chaudhari](https://www.youtube.com/watch?v=oqv92TzphuE)
- **case study** · [How We Scale a Distributed SQL Database to 1 PB - Jinpeng Zhang, PingCAP](https://www.youtube.com/watch?v=c9eAU5DKR5c) — PingCAP
- **concept** · [Database DevOps: CD for Stateful Applications - Stephen Atwell & Christopher Crow](https://www.youtube.com/watch?v=oXrHyOrUwB8)
- **concept** · [Cooperative Scheduling for Stateful Systems - Michael Youssef & Zhantong Shang, LinkedIn](https://www.youtube.com/watch?v=jB2MI7ZKw40)
- **concept** · [Scaling and Safeguarding the Heart of Kubernetes: Deep Dive Into etcd - Panel](https://www.youtube.com/watch?v=q_HZo5Mu8Fk)
- **concept** · [Building Resilience: Effective Backup and Disaster Recovery for Vec... P. Navarathna, S. Subramanian](https://www.youtube.com/watch?v=kl32-01tXE4)
- **concept** · [AIStore as a Fast Tier Storage Solution: Enhancing Petascale Deep Learning... A. Gaikwad & A. Wilson](https://www.youtube.com/watch?v=N-d9cbROndg)
- **concept** · [When Life Gives You Containers, Make an Open Source RDS: A Kubernetes Love Story - Sergey Pronin](https://www.youtube.com/watch?v=0gSSmdNB-Zo). Describes building an open source RDS-like database-as-a-service on Kubernetes using operators.
- **concept** · [The Hard Truth About GitOps and Database Rollbacks - Rotem Tamir, Ariga](https://www.youtube.com/watch?v=jMJ0JSSUmd8)
- **concept** · [Kubernetes on Multisites – A Story About Stateful App, Hybrid Clouds, a... F. Coulombel, J. Šafránek](https://www.youtube.com/watch?v=BaLVmNYDxO8)
- **concept** · [Object Storage Is All You Need - Justin Cormack, Docker](https://www.youtube.com/watch?v=ei0wwTy6_G4)
- **concept** · [The Key Value of etcd Over Custom Resources: Scalability - Jef Spaleta, Isovalent at Cisco](https://www.youtube.com/watch?v=H3NYupSNMnA)
- **concept** · [Rook: Intro and Deep Dive with Ceph Storage - T. Nielsen, A. Clewett, B. Gardner, S. Rai](https://www.youtube.com/watch?v=qB5IQ9DOMbQ)
- **concept** · [Are Your Microservices Truly Scaling? A Framework for Unlocking the Stateful Backend - M. Penaroza](https://www.youtube.com/watch?v=mm5lR0CqY8I)
- **concept** · [Kubernetes (SIG Storage): What's Coming in Kubernetes Storage | Project Lightning Talk](https://www.youtube.com/watch?v=HcoZ6kX343c)
- **concept** · [Vitess: Arewefastyet: Benchmarking Vitess and Mentorship Stories | Project Lightning Talk](https://www.youtube.com/watch?v=ex3OJeftybM)
- **concept** · [Object, Block, or File Storage? Choosing the Right Cloud Storage to Integr... M. Becker, T. McDonald](https://www.youtube.com/watch?v=QQgmaHqKRyY)
- **concept** · [Kubernetes Data Protection WG Deep Dive - Dave Smith-Uchida, Veeam & Xing Yang, VMware by Broadcom](https://www.youtube.com/watch?v=5HgFYkhIoyM). Deep dive into the Kubernetes Data Protection Working Group's work and roadmap.
- **concept** · [TAG Storage: CNCF Storage TAG and the Cloud Native Storage Landscape | Project Lightning Talk](https://www.youtube.com/watch?v=rixA1F0Qk6w)
- **concept** · [SIG Auth & SIG Storage: Secret Guardians - (Secrets Store) CSI Driver and Sync Controller | PLT](https://www.youtube.com/watch?v=xbm92IqlEDE)
- **concept** · [Cloud Native Storage: The CNCF Storage TAG Projects, Technology... A. Chircop, R. Spazzoli, X. Yang](https://www.youtube.com/watch?v=DjePDGyEAvI)
- **concept** · [Kubernetes SIG Storage: Intro & Deep Dive - Michelle Au, Xing Yang & Hemant Kumar](https://www.youtube.com/watch?v=DkpQSCX6KqQ)
- **concept** · [Goodbye etcd! Running Kubernetes on Distributed PostgreSQL - Denis Magda, Yugabyte](https://www.youtube.com/watch?v=VdF1tKfDnQ0)

### 2025 · [KubeCon + CloudNativeCon China 2025 (Hong Kong)](../sources/PLj6h78yzYM2P1xtALqTcCmRAa6142uERl.md)

- **concept** · [Lightning Talk: Stateful Service Federation in Large-Scale Search, Ads, and R... Yang Song & Vec Sun](https://www.youtube.com/watch?v=JV_G34Jwr7M)
- **concept** · [Lightning Talk: Kata Confidential Containers Meet Persistent Stora... Andy Zhang & Archana Choudhary](https://www.youtube.com/watch?v=5QEVlyEQ5m8). Lightning talk on using persistent storage with Kata confidential containers.

### 2025 · [KubeCon + CloudNativeCon Europe 2025 - London](../sources/PLj6h78yzYM2MP0QhYFK8HOb8UqgbIkLMc.md)

- **case study** · [Vitess: Schema Changes at Scale - Rohit Nayak & Shlomi Noach, PlanetScale](https://www.youtube.com/watch?v=Zbi46yTlSVo) — PlanetScale
- **case study** · [Dancing With the Pods: Live Migration of a Database Fleet While Serving... Jayme Bird & Manish Gill](https://www.youtube.com/watch?v=ufY_JFPpzRI)
- **concept** · [Don't Let Your Kubernetes Cluster Go Wild: Ensuring Etcd Reli... Arka Saha & Chun-Hung (Henry) Tseng](https://www.youtube.com/watch?v=J93U9n_qxSI)
- **concept** · [Data Gravity and Kubernetes: Managing Large-Scale Data Ingest... Abhishek Bhattacharjee & Arya Soni](https://www.youtube.com/watch?v=4Pei4LMigQE). Discusses managing large-scale data ingest and data gravity challenges on Kubernetes.
- **concept** · [Stateful Connections in Kubernetes: The Scaling Secrets Nobody... André Mocke & Rodrigo Fior Kuntzer](https://www.youtube.com/watch?v=h1AyaAIf3HA)
- **concept** · [etcd V3.6.0 and etc... Benjamin Wang, Ivan Valdes Castillo, Siyuan Zhang, Arka Saha & Ciprian Hacman](https://www.youtube.com/watch?v=_xoDbpm-Qks)
- **concept** · [A Huge Cluster or Multi-Clusters? Identifying the Bottleneck - Paco Xu & Saiyam Pathak](https://www.youtube.com/watch?v=6l5zCt5QsdY). Analyzes bottlenecks to decide between one huge cluster and multiple clusters.
- **concept** · [Rook: Intro and... Travis Nielsen, Madhu Rajanna, Artem Torubarov, Deepika Upadhyay & Sebastien Han](https://www.youtube.com/watch?v=xGywrHPAMms)
- **concept** · [Cloud Native Storage and Data: The CNCF Storage TAG Projects, Te... Raffaele Spazzoli & Alex Chircop](https://www.youtube.com/watch?v=0GNjonLfCQA). Overview of the CNCF Storage TAG and its projects and cloud native storage and data topics.
- **concept** · [Enhancing Database Observability With OpenTelemetry - Marylia Gutierrez, Grafana Labs](https://www.youtube.com/watch?v=Rf9NceXXRuw)
- **concept** · [Unleashing the Power of Init Containers: Reducing Database Management To... Muhammad Junaid Muzammil](https://www.youtube.com/watch?v=nTmwmd4fcGI)
- **concept** · [The Future of Data on Kubernetes... Rob Strechay, Nimisha Mehta, Gabriele Bartolini & Brian Kaufman](https://www.youtube.com/watch?v=CI4rws1H-aM)
- **concept** · [Stateful Superpowers: Explore High Performa... Alex Chircop, Chris Milsted & Alex Reid, Lori Lorusso](https://www.youtube.com/watch?v=JtMYdR50-KU)
- **concept** · [Trust No One: Secure Storage With Confidential Containers - Aurélien Bombo, Microsoft](https://www.youtube.com/watch?v=etCmLttqJsQ)
- **concept** · [Project Lightning Talk: What's New in Kubernetes Storage - Xing Yang, Co-chair SIG Storage](https://www.youtube.com/watch?v=v_PzG81D33I)
- **concept** · [Project Lightning Talk: Empowering Data Protection for Stateful Applications on Kuberne... Mark Lavi](https://www.youtube.com/watch?v=6CXsWNOqYSw). Project lightning talk on data protection for stateful applications on Kubernetes.
- **concept** · [Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, VMware by Broadcom & Jan Šafránek, Red Hat](https://www.youtube.com/watch?v=X_xHC_Q5jGE)
- **concept** · [Project Lightning Talk: Vitess: Unlimited Database Scalability - Shlomi Noach, Maintainer](https://www.youtube.com/watch?v=ERztKTd-ckA)
- **concept** · [Kubernetes Backup Legitimized: CSI Changed Block Tracking Has Arrived- M. Lavi, C. Braganza, X. Yang](https://www.youtube.com/watch?v=U9qwxp7Uv08)
- **panel** · [Cortex: Insights, U... Friedrich Gonzalez, Daniel Sabsay, Charlie Le, Alolita Sharma & Daniel Blando](https://www.youtube.com/watch?v=3aUg2qxfoZU). Several Cortex maintainers and contributors discuss project insights and updates.

### 2025 · [KubeCon + CloudNativeCon India 2025](../sources/PLj6h78yzYM2MEQTMX_LIOK1hrePHxLD6U.md)

- **concept** · [SIG etcd Maintainer Track Talk - Arka Saha, VMware by Broadcom; Josh Berkus, Red Hat](https://www.youtube.com/watch?v=awxMf3AykQM)
- **concept** · [Inside Vitess: Building Resilient, Distributed Databases - Harshit Gangal, PlanetScale](https://www.youtube.com/watch?v=6QWRHln3VO8). Deep dive into Vitess architecture for resilient, distributed MySQL databases.
- **concept** · [Rook: Intro and Deep Dive Wi... Subham Rai, Nikhil Ladha, Rakshith R, Nitin Goyal & Deepika Upadhyay](https://www.youtube.com/watch?v=9c63Y5UCb-E). Introduction to Rook and a deep dive into its storage orchestration for Ceph on Kubernetes.

### 2025 · [KubeCon + CloudNativeCon Japan 2025 (Tokyo)](../sources/PLj6h78yzYM2PsNdcBGWR_mVN-SRLQl6KM.md)

- **concept** · [Lightning Talk: Providing Sufficient PVCs for Your StatefulSets: Creating New Volu... Kaoru Esashika](https://www.youtube.com/watch?v=-xqdoMinBek). A lightning talk on providing enough PVCs for StatefulSets by creating new volumes.
- **concept** · [Rook: Intro and Deep Dive With Ceph - Satoru Takeuchi, Cybozu, Inc.](https://www.youtube.com/watch?v=LmL2wyMWTXo)
- **concept** · [Dynamic Provisioning and Capacity-Aware Scheduling for Local Storage - Yuma Ogami, Cybozu, Inc.](https://www.youtube.com/watch?v=HXDIukPX6AY)

### 2025 · [KubeCon + CloudNativeCon North America 2025](../sources/PLj6h78yzYM2MLSW4tUDO2gs2pR5UpiD0C.md)

- **concept** · [Managing Data at Scale: Best Practices and Evolution of SIG-Apps - Maciej Szulik & Janet Kuo](https://www.youtube.com/watch?v=9xpp3wvoSDg). SIG-Apps maintainers cover how it has evolved and best practices for managing data and workloads at scale.
- **concept** · [Supercharge Cloud Native SQL Database With Object Storage: Scaling TiKV With S3 as... Jinpeng Zhang](https://www.youtube.com/watch?v=jDlAdMEMZgs)
- **concept** · [etcd V3.6 and Beyond... Siyuan Zhang, Justin Santa Barbara, Wei Fu, Arka Saha & Ivan Valdes Castillo](https://www.youtube.com/watch?v=tF7UOwhgetU)
- **concept** · [Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, Michelle Au, Hemant Kumar](https://www.youtube.com/watch?v=tGSEyEdh5ug)
- **concept** · [Under the Hood of Vitess: Database Engineered for Scale and Resilien... Matt Lord & Florent Poinsard](https://www.youtube.com/watch?v=2B0FB0A_c_Q). Deep dive into Vitess architecture and how it provides a scalable, resilient database layer on MySQL.
- **concept** · [The Next Decoupling: From Monolithic Cluster, To Control-Pl... Justin Santa Barbara & Ciprian Hacman](https://www.youtube.com/watch?v=7czd6oZV3CY). Argues for decoupling the monolithic cluster into separate control-plane components.
- **concept** · [Why Is My Query Slow? Real AI Use Cases With Vitess + Kubernete... Brett Warminski & Gourav Khanijoe](https://www.youtube.com/watch?v=qDBgHS2bE7s)
- **concept** · [Rook: Intro and Deep Dive With Ceph Storage - Blaine Gardner & Benamar Mekhissi, IBM](https://www.youtube.com/watch?v=w9JT4Gj5XtM)
- **concept** · [Routing Stateful AI Workloads in Kubernetes - Maroon Ayoub, IBM & Michey Mehta, Red Hat](../sources/videos/-C76naL3PRc.md). Explains why standard Kubernetes load balancing fails for stateful LLM inference and how llm-d's cache-aware routing fixes it, with benchmark data.
- **concept** · [Untangling CSI: Powering Persistent Storage for KubeVirt - Brenda McLaren & Chris Keller, Red Hat](https://www.youtube.com/watch?v=m97jWRWNv0o)
- **concept** · [Kubernetes and etcd: Common Pitfalls and How To Avoid Them - Arka Saha & Nabarun Pal, Broadcom](https://www.youtube.com/watch?v=wj9UQDcRSWA)
- **concept** · [Project Lightning Talk: Making Kubescape Storage Scale From Small and Mid-Size To... Ben Hirschberg](https://www.youtube.com/watch?v=0SxXulvdMMs). Lightning talk on making Kubescape storage scale from small to large clusters.
- **concept** · [Project Lightning Talk: Vitess: Unlimited Database Scalability - Matt Lord, Maintainer](https://www.youtube.com/watch?v=CSSnY3MFhPI)
- **concept** · [Project Lightning Talk: What's New In Kubernetes Storage - Xing Yang](https://www.youtube.com/watch?v=JhMwxRfi7Ho)
- **concept** · [Project Lightning Talk: CloudNativePG: Running Postgres The Kubernetes Way - Gabriele Bartolini](https://www.youtube.com/watch?v=pYwYwehQX3U)

### 2026 · [KubeCon + CloudNativeCon + OpenInfra Summit + PyTorch Conference China 2026](../sources/PLGcxfZT6qI-w.md)

- **concept** · [To Cache or Not to Cache? A Tiered KVCache Storage System for... Jingbin Zhang, Wang Cong & yun bai](https://www.youtube.com/watch?v=H2ULQz43ln8)
- **concept** · [Can Stateful AI Agents Scale To Zero? - Peng Li, Alibaba Cloud](https://www.youtube.com/watch?v=VWBQBVq3tF4)

### 2026 · [KubeCon + CloudNativeCon Europe 2026](../sources/PLj6h78yzYM2MXCOWSN9CqqID6OOvF7wxL.md)

- **case study** · [Preventing S3 Cost Storms: Applying Cortex’s Efficiency Lessons to I/O-Heav... A. Fishman-Lichterman](https://www.youtube.com/watch?v=7pFxk027sHw) — Cortex. Applies Cortex's lessons on preventing S3 cost spikes to I/O-heavy workloads.
- **concept** · [How Many Spark Applications Can Your Etcd Really Handle? - João Soares & João Azevedo, Feedzai](https://www.youtube.com/watch?v=jmz8c3oEmPY)
- **concept** · [Cloud Native Theater | Data on Kubernetes Day: KubeVirt Benchmar... Bhumitra Nagar & Dhruv Bhatnagar](https://www.youtube.com/watch?v=0s2mSPkE7dw). Presents KubeVirt benchmarking results and performance findings for running VMs on Kubernetes.
- **concept** · [Cloud Native Theater | Data on Kubernetes Day: From Billion... Victoriya Kalmanovich & Shahar Azulay](https://www.youtube.com/watch?v=G9Bt-7OHVBk)
- **concept** · [Cloud Native Theater | Data on Kubernetes Day: Tuning Elastic on Kube... Luuk Stolk and Artur Gromek](https://www.youtube.com/watch?v=LFuEq70lZdo)
- **concept** · [Cloud Native Theater | Data on Kubernetes Day: From PVC to Mount Point: Dissecting a... Vivek Singh](https://www.youtube.com/watch?v=MY-VaJVJmk0)
- **concept** · [Cloud Native Theater | Data on Kubernetes Day: From VMs to Ku... Gabriele Bartolini & Laurent Parodi](https://www.youtube.com/watch?v=m0LBKjlxrog)
- **concept** · [Project Lightning Talk: Run Your Data Layer In K8s With Vitess - Matt Lord, Maintainer](https://www.youtube.com/watch?v=podkclpdT9E)
- **concept** · [Project Lightning Talk: Let’s Deploy etcd Operator - Arka Saha, Maintainer](https://www.youtube.com/watch?v=FBV-fkNwyMU)
- **concept** · [The Symbiosis of Storage and Workloads: Longhorn for Hyperconverged Bl... Jinhong Kim & Jangseon Ryu](https://www.youtube.com/watch?v=qNxIebuifp8)
- **concept** · [Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, VMware by Broadcom & Jan Šafránek, Red Hat](https://www.youtube.com/watch?v=p17X_VnlpiY)
- **concept** · [Rook: Intro and Deep Dive With Ceph Storage - Artem Torubarov, Deepika Upadhyay & Niels de Vos](https://www.youtube.com/watch?v=ygE67l9b2Mc)
- **concept** · [etcd 3.6 Updates and 3.7 Roadmap - Arka Saha, Broadcom & Josh Berkus, Red Hat](https://www.youtube.com/watch?v=YK2Q0hz962o)
- **concept** · [Vitess: More Data, No Problems - Matt Lord & Rohit Nayak, PlanetScale](https://www.youtube.com/watch?v=u4T9PbsaxIU)

### 2026 · [KubeCon + CloudNativeCon India 2026](../sources/PLj6h78yzYM2PmaTdAzefPqjawTlop1lgG.md)

- **case study** · [Building a Self-Service Platform for Stateful AI Agents - Shuva Jyoti Kar, Cisco Systems](https://www.youtube.com/watch?v=1upZrTSUc7A) — Cisco. Cisco describes building a self-service platform for running stateful AI agents.
- **concept** · [When the Edge Can’t Afford a Third Node: A Storage Solution for Two-Node Kubernetes C... Parth Arora](https://www.youtube.com/watch?v=Cw8sFDdNu9Y)
- **concept** · [The Hidden Cost of ML Data Lifecycles in Kubernetes - Yashasvi Misra, Pure Storage](https://www.youtube.com/watch?v=a_yZgysIpFo)
- **concept** · [Project Lightning Talk: Vitess in Production: Powering Applications at Massive Sca... Harshit Gangal](https://www.youtube.com/watch?v=0xYpGQEmU40). Lightning talk on how Vitess powers MySQL-backed applications at massive scale.
- **concept** · [Sponsored Demo: Cloud Native AI: Model Management with Harbor & Velero - Dhruv Tyagi, Broadcom](https://www.youtube.com/watch?v=bDot6ur5U3Y)
- **concept** · [Rook: Intro and Deep Dive With Ceph Storage - Deepika U, Madhu R, Rewant S, Malay P & Pratik S](https://www.youtube.com/watch?v=uR3j_1mbxdY)
- **concept** · [Longhorn: What's New & What's Next for Cloud Native Persistent Storage - Divya Mohan, SUSE](https://www.youtube.com/watch?v=iW8rDK8syo4)
- **concept** · [etcd in 2026: Enhancements, V3.7 Roadmap... Lavish Pal, Arka Saha, Josh Berkus & Guna K Kambalimath](https://www.youtube.com/watch?v=BcLKvLD2D2Y)

### 2026 · [KubeCon + CloudNativeCon Japan 2026](../sources/PLH1zduub3WrE.md)

- **case study** · [Taming Billions of Rows: Data Lifecycle Management Lessons From a Cloud Native Database… R. Kadyrov](https://www.youtube.com/watch?v=32RGaUtPe5o). Lessons learned managing the data lifecycle of billions of rows in a cloud native database, reported from the speaker's own operating experience.
- **case study** · [Changing the Engine Mid-Flight: Zero-Downtime Ceph Upgrades - Cuong Nguyen, Viettel Group](https://www.youtube.com/watch?v=9Mr1y64ARtE) — Viettel Group. Viettel Group describes performing zero-downtime upgrades of its Ceph clusters.
- **case study** · [User Namespaces in Production: Enabling Root in Containers With RWX - Kohei Sugihara & Toru Komatsu](https://www.youtube.com/watch?v=5es7m1R7ZqY) — Preferred Networks. Describes running user namespaces in production to enable root inside containers with RWX storage.
- **concept** · [Is Your Kubernetes Disaster Recovery Actually Ready? - Saiyam Pathak & Saloni Narang](https://www.youtube.com/watch?v=21_7qv7J8GI). Discusses how to verify whether a Kubernetes disaster recovery setup is truly ready.
- **concept** · [Running Wasm Inside Your Storage Cluster With CSI and Gateway API - Ho Kim & SangJoon Park](https://www.youtube.com/watch?v=K6_KQm1lMn8)
- **concept** · [Rook: Intro and Deep Dive With Ceph - Satoru Takeuchi & Dan van der Ster](https://www.youtube.com/watch?v=blbLXigYIDI)
