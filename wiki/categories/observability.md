---
title: "Observability"
summary: 567 talks (71 case studies) across 33 events; organizations include GitLab, Grafana Labs, Uber, Weaveworks, Lyft, Splunk.
tags: [category, observability]
generated: categories
---

# Observability

> 567 talks across 33 events, oldest first: 71 case studies where an organization reports its own experience, plus concept talks and tutorials.

Keywords: observability, opentelemetry, otel, prometheus, grafana, jaeger, tracing, distributed tracing, metrics, logging, logs, fluentd, fluent bit, loki, thanos, cortex, mimir, tempo, ebpf observability, monitoring, alerting, slo, profiling, pixie (edit under `categories:` in wiki.yaml).

## Over time

| Year | Talks | Case studies |
| --- | --- | --- |
| 2016 | 7 | 0 |
| 2017 | 30 | 1 |
| 2018 | 72 | 9 |
| 2019 | 67 | 7 |
| 2020 | 39 | 9 |
| 2021 | 48 | 5 |
| 2022 | 42 | 5 |
| 2023 | 60 | 7 |
| 2024 | 71 | 10 |
| 2025 | 76 | 6 |
| 2026 | 55 | 12 |

## Organizations with case studies

GitLab (3), Grafana Labs (3), Uber (2), Weaveworks (2), Lyft (2), Splunk (2), Intuit (2), JD.COM, Infobip, Branch Metrics, DigitalOcean, Planet, Spotify, Amgen, HashiCorp, Shopify, NVIDIA, Usabilla, Affirmed Networks, PingCAP, Alibaba, Calyptia, Itaú Unibanco, eBay, Honeycomb.io, Honeycomb, Heroku, Salesforce, A. Grabner, OpenTelemetry Network, Grafana, Red Hat, Google, Etsy, Bloomberg, Dash0, LinkedIn, Murphy Chen, Netflix, Cortex, Fluent Bit

## Talks by event

### 2016 · [KubeCon + CloudNativeCon North America 2016 (Seattle)](../sources/PLj6h78yzYM2PqgIGU1Qmi8nY7dqn9PCr4.md)

- **concept** · [Logging for Containers by Eduardo Silva, Treasure Data](https://www.youtube.com/watch?v=395iaisdZEY). Covers approaches and tools for collecting and managing logs from containers.
- **concept** · [You’re Monitoring Kubernetes Wrong by Loris Degioanni, Sysdig](https://www.youtube.com/watch?v=agbBy1Aduew)
- **concept** · [Monitoring MySQL and MongoDB with Prometheus by Vadim Tkachenko, Percona](https://www.youtube.com/watch?v=19c_gNQT2dM). Shows how to monitor MySQL and MongoDB with Prometheus.
- **concept** · [Weave Cortex: Horizontally Scalable, Multitenant Prometheus as a Service by Tom Wilkie, Weaveworks](https://www.youtube.com/watch?v=9Uctgnazfwk). Presents Cortex, a horizontally scalable multitenant Prometheus as a service.
- **concept** · [Prometheus Is Good for Your Small Startup by Ignacio P. Carretero, ShuttleCloud](https://www.youtube.com/watch?v=veohecVHtBU)
- **concept** · [Chronix as Long Term Storage for Prometheus by Moritz Kammerer, QAware GmbH](https://www.youtube.com/watch?v=4fhXSgRmLHM). Presents Chronix as a long-term storage backend for Prometheus.
- **concept** · [Beyond Nagios: Modern Monitoring of Bronze-Age Applications with Prometheus by Ben Kochie](https://www.youtube.com/watch?v=ebfEhfJBEJ8)

### 2017 · [KubeCon + CloudNativeCon Europe 2017 (Berlin)](../sources/PLj6h78yzYM2PAavlbv0iZkod4IVh_iGqV.md)

- **concept** · [Lightning Talk: The Top 5 Kubernetes Metrics to Monitor - Jorge Salamero Sanz, Sysdig](https://www.youtube.com/watch?v=dgkUVggy4ec)
- **concept** · [Lightning Talk: Flexible Logging Pipelines with Fluentd and Kubernetes - Jakob Karalus, codecentric](https://www.youtube.com/watch?v=FABYwvizXOQ)
- **concept** · [Integrating Long-Term Storage with Prometheus [A] - Julius Volz, Prometheus](https://www.youtube.com/watch?v=MuHkckZg5L0)
- **concept** · [Kubernetes-Defined Monitoring [I] - Gianluca Borello, Sysdig](https://www.youtube.com/watch?v=ncSn3_9bfIQ)
- **concept** · [The Patterns of Distributed Logging and Containers [I] - Satoshi Tagomori, Treasure Data, Inc.](https://www.youtube.com/watch?v=TIg9Yi2eGqM)
- **concept** · [Grafana is Not Enough: DIY User Interfaces for Prometheus [I] - David Kaltschmidt, Weaveworks](https://www.youtube.com/watch?v=bfSMDERvkZY)
- **concept** · [Understanding and Extending Prometheus AlertManager [I] - Lee Calcote, SolarWinds](https://www.youtube.com/watch?v=jpb6fLQOgn4)
- **concept** · [Alerting in Cloud Native Environments [I] - Fabian Reinartz, CoreOS](https://www.youtube.com/watch?v=cR9Fp6hwTLE)
- **concept** · [Counting with Prometheus [I] - Brian Brazil, Robust Perception](https://www.youtube.com/watch?v=67Ulrq6DxwA). Brian Brazil explains how counting and counters work in Prometheus.
- **concept** · [OpenTracing and Containers: Depth, Breadth, and the Future of Tracing [I] - Priyanka Sharma](https://www.youtube.com/watch?v=CUjTw7k_0RQ)
- **concept** · [Operational and Business Insights from Tracing Distributed Microservices [I]](https://www.youtube.com/watch?v=dmMWaTZE5gQ)
- **concept** · [Loki: An OpenSource Zipkin / Prometheus Mashup, Written in Go [I] - Tom Wilkie, Weaveworks](https://www.youtube.com/watch?v=Bmzx-5uExPM)
- **concept** · [OpenTracing Isn't Just Tracing: Measure Twice, Instrument Once [B] - Priyanka Sharma & Ted Young](https://www.youtube.com/watch?v=NyySNe6Rr_g)
- **concept** · [360° Monitoring of Your Services [I] - Philipp Krenn, Elastic](https://www.youtube.com/watch?v=4TLJOc1EeI8). Overview of monitoring services end to end with the Elastic stack.
- **concept** · [Audit in Kubernetes Now, and in the Future [B] - Maciej Szulik, Red Hat](https://www.youtube.com/watch?v=4SXjS69X8pg). Covers how Kubernetes auditing works and where it is headed.
- **concept** · [Behind the Iron Curtain: Getting Metrics From the Browser into Prometheus [I] - Tom Wilkie](https://www.youtube.com/watch?v=5S-0bJAtpMc). Shows how to get metrics from the browser into Prometheus.
- **concept** · [Ops for Developers - Monitor Your Java Application with Prometheus [I] - Alexander Schwartz](https://www.youtube.com/watch?v=Zgka3GFjqjA)
- **concept** · [Monitor My Socks: Using Prometheus in a Polyglot Open Source Microservices](https://www.youtube.com/watch?v=U_nQObcAxSk)
- **concept** · [Configuring Prometheus for High Performance [A] - Björn Rabenstein, SoundCloud Ltd.](https://www.youtube.com/watch?v=hPC60ldCGm8)
- **concept** · [Prometheus: The Unsung Heroes [I] - Alejandro Ramirez, Swisscom Directories AG](https://www.youtube.com/watch?v=lo0Y1QyGh0k)

### 2017 · [KubeCon + CloudNativeCon North America 2017 (Austin)](../sources/PLj6h78yzYM2P-3-xqvmWaZbbI1sW-ulZb.md)

- **case study** · [Would You Like Some Tracing With Your Monitoring? - Yuri Shkuro, Uber Technologies](https://www.youtube.com/watch?v=1NDq86kbvbU) — Uber. Uber explains how it combines distributed tracing with monitoring, drawing on its experience building Jaeger.
- **concept** · [“If you Don’t Monitor your Infrastructure, you Don’t Own it!” Regain Control Thanks to Prometheus](https://www.youtube.com/watch?v=MNc3046o-Og)
- **concept** · [Fluentd and Distributed Logging [I] - Masahiro Nakagawa, Treasure Data](https://www.youtube.com/watch?v=XZMGCQ96C80)
- **concept** · [Full Stack Visibility with Elastic: Logs, Metrics and Traces - Carlos Pérez-Aradros, Elastic](https://www.youtube.com/watch?v=SzX5tTY-vPM)
- **concept** · [Unified Monitoring of Containers and Microservices [I] - Nishant Sahay, Wipro Limited](https://www.youtube.com/watch?v=YBVipwfH5cQ)
- **concept** · [Ask Your Proxy, It Knows Everything - Blake Mizerany, Backplane](https://www.youtube.com/watch?v=43wFJBRTHG0). Explores querying a proxy to learn about traffic and system behavior.
- **concept** · [Running Mixed Workloads on Kubernetes at the Institute for Health Metrics and Evaluation](https://www.youtube.com/watch?v=JfIJiK7QrC8)
- **concept** · [Monitoring Kubernetes: Follow the Data [B] - Ilan Rabinovitch, Datadog](https://www.youtube.com/watch?v=XYWI2sf7A14)
- **tutorial** · [Cloud Native Logging 101 [B] - Eduardo Silva, Treasure Data](https://www.youtube.com/watch?v=szN_e9VZ8ZA)
- **tutorial** · [A Practical Guide to Prometheus for App Developers [B] - Ilya Dmitrichenko, Weaveworks](../sources/videos/-7fO99IiTpY.md). Practical guide for app developers on using Prometheus, with PromQL examples and remote read/write.

### 2018 · [KubeCon + CloudNativeCon China 2018 (Shanghai)](../sources/PLj6h78yzYM2OK087kzLgc4jTPVbZjuNfs.md)

- **case study** · [Kube-Liveboard: Make Your Cluster Visible - Xinkun Xu, JD.COM](https://www.youtube.com/watch?v=-MqK6dmd84E) — JD.COM. JD.COM presents Kube-Liveboard, a tool it built to make its Kubernetes clusters visible.
- **case study** · [Canary Deployment With Prometheus - Andrey Markelov, Infobip](https://www.youtube.com/watch?v=3s2_UCeWeJg) — Infobip. Infobip shows how it runs canary deployments using Prometheus metrics.
- **concept** · [Extending Istio - Develop a New Mixer Adapter for Your Monitoring - Wen Tao Zhang & Yang Yang](https://www.youtube.com/watch?v=qqmY2WdKkgw)
- **concept** · [Intro: Prometheus – Richard "RichiH" Hartmann, SpaceNet & Ben "SuperQ" Kochie, GitLab](https://www.youtube.com/watch?v=LSzyP_xfFRg)
- **concept** · [Intro: Jaeger - Prithvi Raj Venkat Raj & Won Jun Jang, Uber](https://www.youtube.com/watch?v=HoNSs6bz_1I)
- **concept** · [Deep Dive: Prometheus – Richard "RichiH" Hartmann, SpaceNet & Ben "SuperQ" Kochie, GitLab](https://www.youtube.com/watch?v=z-g-hUnl9YU)
- **concept** · [Intro: Fluentd - Eduardo Silva & Masahiro Nakagawa, Treasure Data](https://www.youtube.com/watch?v=NEGEy6mruR0)
- **concept** · [Deep Dive: Fluent Bit - Eduardo Silva & Masahiro Nakagawa, Treasure Data](https://www.youtube.com/watch?v=v46iUnAcKbA)
- **concept** · [Deep Dive: Jaeger - Prithvi Raj Venkat Raj & Won Jun Jang, Uber](https://www.youtube.com/watch?v=B5v4UvO2hCs)
- **concept** · [Production Cluster Monitoring and Remediation for High Reliability - Shijun Qian & YingKe Liu](https://www.youtube.com/watch?v=MVJiWtNC3SM)
- **concept** · [Seamless Integration - Take Kubernetes into your Existing Monitoring Stack - Shaojun Ding, IBM](https://www.youtube.com/watch?v=9Ax-vbGgbJ4). Describes how to integrate Kubernetes into an existing monitoring stack.
- **tutorial** · [Getting Started With Logging in Kubernetes - Eduardo Silva, Treasure Data](https://www.youtube.com/watch?v=XoudmP9a2zc)

### 2018 · [KubeCon + CloudNativeCon Europe 2018 (Copenhagen)](../sources/PLj6h78yzYM2N8GdbjmhVU65KYm_68qBmo.md)

- **case study** · [How We Used Jaeger and Prometheus to Deliver Lightning-Fast User Queries - Bryan Boreham](https://www.youtube.com/watch?v=qg0ENOdP1Lo)
- **case study** · [Lightning Talk: What I Wish I’d Known about Fluentd with Kubernetes - Bryan Boreham, Weaveworks](https://www.youtube.com/watch?v=BQuBnXp31ZA) — Weaveworks
- **case study** · [Feeding Realworld Data into Prometheus Microservice Apps on Kubernetes - Burkhard Noltensmeier](https://www.youtube.com/watch?v=1rwBeDVdjyY). Shows how real-world data was fed into Prometheus for monitoring microservice applications running on Kubernetes.
- **case study** · [Federated Prometheus Monitoring at Scale - Nandhakumar Venkatachalam & LungChih Tung](https://www.youtube.com/watch?v=Zm43VM7nKdU)
- **concept** · [Low-Overhead Tracing Using eBPF for Observability into Kubernetes Apps and Services - Gaurav Gupta](https://www.youtube.com/watch?v=ug3lYZdN0Bk)
- **concept** · [Scalable Monitoring Using Prometheus with Apache Spark - Diane Feddema & Zak Hassan, Red Hat Inc](https://www.youtube.com/watch?v=oNBpZFhL94s)
- **concept** · [How to Export Prometheus Metrics from Just About Anything - Matt Layher, DigitalOcean](https://www.youtube.com/watch?v=Zk09Mbu0YQk)
- **concept** · [Prometheus for Devs - Hubert Ströbitzer, Freelancer (Beginner Skill Level)](https://www.youtube.com/watch?v=ZHCSmYvA_sg)
- **concept** · [Prometheus Project Intro – Julius Volz, Prometheus (Any Skill Level)](https://www.youtube.com/watch?v=sYMTY-SciUQ)
- **concept** · [Jaeger Project Intro - Juraci Kröhling, Red Hat (Any Skill Level)](https://www.youtube.com/watch?v=D7XakRQaEk0)
- **concept** · [What's Up With All The Different Container Runtimes? - Ricardo Aravena, Branch Metrics](https://www.youtube.com/watch?v=lHv0LVEIPk8)
- **concept** · [A Survey of the OSS Tracing Ecosystem - Ben Sigelman & Ted Young, LightStep (Beginner Skill Level)](https://www.youtube.com/watch?v=-zLPPYYH_F8). A beginner survey of the open source tracing ecosystem and its projects.
- **concept** · [Reveal Your Deepest Kubernetes Metrics - Bob Cotton, Freshtracks.io](https://www.youtube.com/watch?v=1oJXMdVi0mM). Explains how to surface deeper Kubernetes metrics using Prometheus-based tooling.
- **concept** · [TSDB: The Past, Present and the Future - Goutham Veeramachaneni, IIT Hyderabad](https://www.youtube.com/watch?v=0UvKEHFNu4Q). Covers the history, current state and future of the Prometheus TSDB.
- **concept** · [Pod Anomaly Detection and Eviction using Prometheus Metrics - David Benque & Cedric Lamoriniere](https://www.youtube.com/watch?v=HIB_haT1z5M)
- **concept** · [Autoscale your Kubernetes Workload with Prometheus - Frederic Branczyk, CoreOS](https://www.youtube.com/watch?v=VQFoc0ukCvI)
- **concept** · [Who Shot the Cluster? - Audit Logging in Kubernetes - Marian Lobur & Mik Vyatskov, Google](https://www.youtube.com/watch?v=gDZxQBo-Zdc)
- **concept** · [Managing Kubernetes: What You Need to Know About Day 2 - Craig Tracey, Heptio](https://www.youtube.com/watch?v=0TBelL8UBQU). Covers what to know about managing Kubernetes in day 2 operations.
- **concept** · [Fluentd Project Intro – Eduardo Silva & Masahiro Nakagawa, Treasure Data](https://www.youtube.com/watch?v=BtGOTIkxnGE)
- **concept** · [Prometheus Deep Dive – Julius Volz, Prometheus, & Max Inden, Red Hat (Intermediate Skill Level)](https://www.youtube.com/watch?v=UAAT0tRmXP8)
- **concept** · [Jaeger Project Deep Dive - Juraci Kröhling, Red Hat (Intermediate Skill Level)](https://www.youtube.com/watch?v=tFZAHWl8y_I)
- **concept** · [Observability and Debugging Cloud-Native Apps using Linkerd & Conduit - Franziska von der Goltz](https://www.youtube.com/watch?v=RC_9ywj0yz8)
- **concept** · [Horizontal Pod Autoscaler Reloaded - Scale on Custom Metrics - Maciej Pytel & Solly Ross](https://www.youtube.com/watch?v=1xm_ccAYO90). Explains how the Horizontal Pod Autoscaler can scale workloads on custom metrics via the Kubernetes metrics APIs.
- **concept** · [Monitoring: Follow the Data from the Darkest Corners - Piotr Szczesniak & Frederic Branczyk](https://www.youtube.com/watch?v=FAqwXX3Zt9s)
- **concept** · [Fluentd Deep Dive – Eduardo Silva & Masahiro Nakagawa, Treasure Data](https://www.youtube.com/watch?v=TqW-b60AiNk)
- **concept** · [Declarative Multi-Cluster Monitoring with Prometheus - Matthias Loibl, Loodse & Frederic Branczyk](https://www.youtube.com/watch?v=IpGfmmJ2hcw)
- **concept** · [Integrating Prometheus and InfluxDB - Paul Dix, InfluxData (Intermediate Skill Level)](https://www.youtube.com/watch?v=6UjVX-RTFmo). Explains how Prometheus and InfluxDB can be integrated for long-term storage and querying of metrics.
- **concept** · [Beyond OpenTracing - Allison Richardet, Asteris, LLC (Intermediate Skill Level)](https://www.youtube.com/watch?v=5uGGgMn2iq4). Discusses the future of tracing beyond OpenTracing.
- **concept** · [Lightning Talk: TSDB: The Engine behind Prometheus - Goutham Veeramachaneni, IIT Hyderabad](https://www.youtube.com/watch?v=_529xDFDzI0)
- **tutorial** · [Getting Started with Logging in Kubernetes - Eduardo Silva, Treasure Data (Any Skill Level)](https://www.youtube.com/watch?v=7qL5wkAaSh4). Introduces getting started with logging in Kubernetes.
- **tutorial** · [Building a Kubernetes Scheduler using Custom Metrics - Mateo Burillo, Sysdig](https://www.youtube.com/watch?v=4TaHQgG9wEg). Walks through building a custom Kubernetes scheduler driven by custom metrics.

### 2018 · [KubeCon + CloudNativeCon North America 2018 (Seattle)](../sources/PLj6h78yzYM2PZf9eA7bhWnIh_mK1vyOfU.md)

- **case study** · [Kubernetes and The GitOps Face-Off - Ricardo Aravena & Javeria Khan, Branch Metrics](https://www.youtube.com/watch?v=9qGqx_jdxQg) — Branch Metrics. Branch Metrics compares GitOps approaches on Kubernetes based on its own experience.
- **case study** · [Adopting Prometheus the Hard Way - Tim Simmons, DigitalOcean](https://www.youtube.com/watch?v=LmXWLNd2FTA) — DigitalOcean
- **case study** · [Instrumenting and Scaling Cloud-Native Databases with Envoy - Daniel Hochman, Lyft](https://www.youtube.com/watch?v=1e2_Ljxe0Sg) — Lyft. Lyft shows how it uses Envoy to instrument and scale its cloud-native databases.
- **concept** · [Lightning Talk: Labels in Prometheus Alerts: Think Twice Before Using Them - Elena Morozova](https://www.youtube.com/watch?v=F7zNv6qhYO4)
- **concept** · [Lightning Talk: Monitoring Kubernetes with BPF and Prometheus - Jonathan Perry, Flowtune](https://www.youtube.com/watch?v=mVEsTywBg7E)
- **concept** · [Lightning Talk: PID Autoscaling Strava's Linkerd Service Mesh Using Prometheus Data - J Evans](https://www.youtube.com/watch?v=sOku2TMZC3k)
- **concept** · [Three Pillars, Zero Answers: We Need to Rethink Observability - Ben Sigelman, LightStep](https://www.youtube.com/watch?v=EJV_CgiqlOE)
- **concept** · [Observability is the Key Tenet of Running a Multi-Tenant K8s Environment - Thom McCann](https://www.youtube.com/watch?v=mBE3Mjo9RRg)
- **concept** · [Water, Water, Everywhere: Making Kubernetes Audit Logs Potable - Kate Kuchin, Heptio](https://www.youtube.com/watch?v=7dJiagat4FI). Explains how to make Kubernetes audit logs usable by configuring and processing them.
- **concept** · [Linkerd 2.0, Now with Extra Prometheus - Andrew Seigner, Buoyant & Frederic Branczyk, CoreOS](https://www.youtube.com/watch?v=bnDWApsH36Y)
- **concept** · [Intro: Fluentd - Eduardo Silva & Masahiro Nakagawa, Treasure Data](https://www.youtube.com/watch?v=6Lfrh3pw1rM). Introduction to the Fluentd project and how it collects and routes logs.
- **concept** · [Intro: Prometheus – Richard "RichiH" Hartmann, SpaceNet & Frederic Branczyk, CoreOS](https://www.youtube.com/watch?v=MUb2WX4RgJI)
- **concept** · [Monitor the World: Meaningful Metrics for Containerized Apps & Clusters - Nicholas Turner & Nic Cope](https://www.youtube.com/watch?v=HYDojVW9YtU)
- **concept** · [Cortex - Infinitely Scalable Prometheus - Bryan Boreham, Weaveworks](https://www.youtube.com/watch?v=iyN40FsRQEo)
- **concept** · [Deep Dive: Prometheus – Richard "RichiH" Hartmann, SpaceNet & Frederic Branczyk, CoreOS](https://www.youtube.com/watch?v=EkPkGJvh4Jg)
- **concept** · [Securing Application Telemetry & Tracing with SPIFFE and Envoy - Sabree Blackmon, Docker](https://www.youtube.com/watch?v=_OzG4PHihSk)
- **concept** · [Deep Dive: Linkerd - Oliver Gould, Buoyant](https://www.youtube.com/watch?v=8EtH0ymXpvw). Deep dive into how the Linkerd service mesh is designed and works.
- **concept** · [Intro: Jaeger - Yuri Shkuro, Uber & Pavol Loffay, Red Hat](https://www.youtube.com/watch?v=WRntQsUajow)
- **concept** · [Predictive Application Scaling with Prometheus and ML - Chris Dutra, Schireson](https://www.youtube.com/watch?v=xcK--dJn55g)
- **concept** · [Trace Driven Development: Unifying Testing and Observability - Ted Young, LightStep](https://www.youtube.com/watch?v=NU-fTr-udZg)
- **concept** · [Got a Need for Speed? Accelerate Your Prometheus Dashboard Using... - Shilla Saebi & James Ranson](https://www.youtube.com/watch?v=ZO7nrX20iT0)
- **concept** · [Deep Dive: Jaeger - Pavol Loffay, Red Hat & Yuri Shkuro, Uber](https://www.youtube.com/watch?v=i8JttH6DJxo)
- **concept** · [Understanding Microservices with Distributed Tracing - Lita Cho, Lyft](https://www.youtube.com/watch?v=eWFFczgz69c)
- **concept** · [Unified Observability in Kubernetes and Beyond with OpenCensus - Morgan McLean & Jaana Burcu Dogan](https://www.youtube.com/watch?v=wL6UxIar_Gk)
- **concept** · [Sharded And Federated Prometheus Servers to Monitor Distributed Databases - Jun Li & Viswa Vutharkar](https://www.youtube.com/watch?v=YVj_aqUbpYs)
- **concept** · [Distributed Tracing in Serverless Systems - Nitzan Shapira, Epsagon](https://www.youtube.com/watch?v=RHpenniI7zw)
- **concept** · [Collecting Operational Metrics for a Cluster with 5,000 Namespaces - Rob Szumski & Chance Zibolski](https://www.youtube.com/watch?v=JHmWRBWPKog)
- **concept** · [On the OSS Path to Full Observability with Grafana - David Kaltschmidt, Grafana Labs](https://www.youtube.com/watch?v=U7C5SpRtK74)
- **concept** · [Deep Dive: Fluent Bit - Eduardo Silva & Masahiro Nakagawa, Treasure Data](https://www.youtube.com/watch?v=OB-IKl_PbzU)

### 2019 · [KubeCon + CloudNativeCon China 2019 (Shanghai)](../sources/PLj6h78yzYM2Njj5PvNc4Mtcril2YyR95d.md)

- **case study** · [Real World Architecture - Building a Global Cross-Cloud Monitoring...  Dominic Green & Yifan Zhao](https://www.youtube.com/watch?v=UUtAGyGN7Sk)
- **concept** · [Community Data is Not Community Metrics - Brian Proffitt, Red Hat](https://www.youtube.com/watch?v=u9zP6HEnvIw)
- **concept** · [Network Visibility in Hybrid and Multi Clouds - Suresh Kumar Anaparti & Harikrishna Patnala](https://www.youtube.com/watch?v=5F7fAoASrYY). Covers how to get network visibility across hybrid and multi-cloud environments.
- **concept** · [Observability in Service Mesh Powered by Envoy and Apache SkyWalking - Sheng Wu & Lizan Zhou](https://www.youtube.com/watch?v=tERm39ju9ew)
- **concept** · [High Available + Scalable Prometheus with Thanos in Alibaba - Guo'an Qin, Alibaba & Tao Li, Alibaba](https://www.youtube.com/watch?v=ZS6zMksfipc)
- **concept** · [OpenTelemetry: Overview & Backwards Compatibility of OpenTracing + OpenCensus - Steve Flanders](https://www.youtube.com/watch?v=CqgAMMb4k7o)
- **concept** · [Deep Dive: Jaeger – Steve Flanders, Omnition](https://www.youtube.com/watch?v=A4iqTcqO4wg). Deep dive into Jaeger distributed tracing.
- **concept** · [Network Observability with Envoy - Nic Jackson, HashiCorp](https://www.youtube.com/watch?v=usSyncnsl4A)
- **concept** · [Fluentd: A Complete Logging Ecosystem for Kubernetes - Masahiro Nakagawa & Yuta Iwama](https://www.youtube.com/watch?v=XNJwWEo5wik)
- **concept** · [Anomaly Detection for Cloud Native Storage - Seiya Takei & Xing Yang](https://www.youtube.com/watch?v=7TK9TgqITE0). Explores detecting anomalies in cloud native storage systems.
- **concept** · [AIOps: Anomaly Detection with Prometheus and Istio - Marcel Hild, Red Hat](https://www.youtube.com/watch?v=D09x0eR4vu4)
- **concept** · [Enable Serverless Metrics in Apache OpenWhisk on Kubernetes with Prometheus - Ying Chun Guo, IBM](https://www.youtube.com/watch?v=GyXHonYHzis)
- **concept** · [Intro: Falco - Kaizhe Huang, Sysdig](https://www.youtube.com/watch?v=5q2WoTvA__8). Introduction to the Falco runtime security project.

### 2019 · [KubeCon + CloudNativeCon Europe 2019 (Barcelona)](../sources/PLj6h78yzYM2PpmMAnvpvsnR4c27wJePh3.md)

- **case study** · [From New Cluster to Insight. Deploying Monitoring and Logging to Kubernetes - Eddie Zaneski](https://www.youtube.com/watch?v=sR3jxSXY7A4)
- **case study** · [M3 and Prometheus, Monitoring at Planet Scale for Everyone - Rob Skillington, Uber](https://www.youtube.com/watch?v=EFutyuIpFXQ) — Planet, Uber
- **concept** · [Lightning Talk: Back to the Future with eBPF - Beatriz Martínez Rubio, IBM](https://www.youtube.com/watch?v=AQNz_16CaiI). Lightning talk looking at eBPF and how it connects past and future technologies.
- **concept** · [Using K8s Audit Logs to Secure Your Cluster - Mark Stemm, Sysdig](https://www.youtube.com/watch?v=h0h9QWhGFS4)
- **concept** · [Istio, We Have a Problem! Understanding and Fixing Bugs with a Service-Mesh - David Gageot, Google](https://www.youtube.com/watch?v=9CQ0PMiOGhg). Shows techniques for understanding and fixing bugs using a service mesh like Istio.
- **concept** · [Intro: Fluentd - Masahiro Nakagawa, ARM Treasure Data](https://www.youtube.com/watch?v=L3LYItZ7IXI)
- **concept** · [Intro: Cortex - Tom Wilkie, Grafana Labs & Bryan Boreham, Weaveworks](https://www.youtube.com/watch?v=_7Wnta-3-W0)
- **concept** · [OpenTelemetry: Backwards Compatibility with... - Ben Sigelman, Bogdan Drutu & Spiros Xanthos](https://www.youtube.com/watch?v=mvWwSkBq9sY)
- **concept** · [Deep Dive Fluent Bit: Logging & Stream Processing - Eduardo Silva, ARM Treasure Data](https://www.youtube.com/watch?v=xKbVBUMnJH0)
- **concept** · [Fluent Bit: Extending Your Logging Pipeline with Go - Warren Fernandes & Jason Keene, Pivotal](https://www.youtube.com/watch?v=oL6WovwwxrY)
- **concept** · [Tracing is More Than Traces: The Insights in Trace Aggregates - Daniela Miao, LightStep](https://www.youtube.com/watch?v=mzTTYzIzzkk)
- **concept** · [What's the Performance Overhead? Answering the Biggest Question in Tracing - Gabriela Soria](https://www.youtube.com/watch?v=8GjwYU2MbgM). Examines the performance overhead that tracing adds to applications.
- **concept** · [Deep Dive: Cortex - Tom Wilkie, Grafana Labs & Bryan Boreham, Weaveworks](https://www.youtube.com/watch?v=mYyFT4ChHio)
- **concept** · [Deep Dive: Kubernetes Metric APIs using Prometheus - Matthias Loibl & Sergiusz Urbaniak, Red Hat](https://www.youtube.com/watch?v=cIoOAbzhR7k)
- **concept** · [Fool-Proof Kubernetes Dashboards for Sleep-Deprived Oncalls - David Kaltschmidt, Grafana Labs](https://www.youtube.com/watch?v=YE2aQFiMGfY)
- **concept** · [Grafana Loki: Like Prometheus, But for logs. - Tom Wilkie, Grafana Labs](https://www.youtube.com/watch?v=CQiawXlgabQ)
- **concept** · [Intro + Deep Dive: Jaeger - Juraci Paixão Kröhling, Red Hat & Prithvi Raj, Uber](https://www.youtube.com/watch?v=Edy2vd7bh5U)
- **concept** · [Intro + Deep Dive: Prometheus - Julius Volz, Prometheus & Richard Hartmann, SpaceNet](https://www.youtube.com/watch?v=9GMWvFcQjYI). Intro and deep dive on how Prometheus works and its recent developments.
- **concept** · [Monitoring Service Architecture and Health with BPF - Jonathan Perry, Flowmill, Inc.](https://www.youtube.com/watch?v=J2NWvh3lgJI)
- **concept** · [Network Observability with IPFIX, Prometheus and Elastic Stack - Rastislav Szabo](https://www.youtube.com/watch?v=sj7pmz5sutE)
- **concept** · [Deploy, Scale and Extend Jaeger - Louis-Etienne Dorval, Ticketmaster](https://www.youtube.com/watch?v=JloanFIc-ms)
- **concept** · [Autoscaling Multi-Cluster Observability with Thanos and Linkerd - Andrew Seigner & Frederic Branczyk](https://www.youtube.com/watch?v=qTxunwzYO0g)
- **concept** · [Network Flow Monitoring in Kubernetes with Contiv/VPP CNI and Elastic Stack - Rastislav Szabo](https://www.youtube.com/watch?v=GYee7igCmDs)
- **panel** · [OpenTelemetry: Panel Discussion and Q&A - Ben Sigelman, Morgan McClean & Bogdan Drutu](https://www.youtube.com/watch?v=IdYZphA5S7s)
- **panel** · [Panel Discussion: Metrics that Matter: How to Forge More Diverse, Inclusive Communities](https://www.youtube.com/watch?v=PCQc6T94RE4)

### 2019 · [KubeCon + CloudNativeCon North America 2019 (San Diego)](../sources/PLj6h78yzYM2NDs-iu8WU5fMxINxHXlien.md)

- **case study** · [Lightning Talk: How the Observability Team at Spotify Radically Decreased... Lauren Muhlhauser](https://www.youtube.com/watch?v=AA8e5v43AcU) — Spotify. Spotify's observability team describes how it radically decreased observability costs or usage.
- **case study** · [From Issue to PR Merged: A Fluentd “Tail” - Jordan Hamel, Amgen](https://www.youtube.com/watch?v=P1ONBKIxz7w) — Amgen
- **case study** · [Envoy on Fire: A Practical Look at Debugging a Service Mesh - Lita Cho & Ryan Cox, Lyft](https://www.youtube.com/watch?v=6jnzo8QXyDk) — Lyft. Lyft shares how it debugs Envoy and its service mesh in production.
- **case study** · [The Great Cardinality Disasters of Our Time - Bryan Boreham, Weaveworks & Chris Marchbanks, Splunk](https://www.youtube.com/watch?v=6f9z9JSNOGk) — Weaveworks, Splunk. Weaveworks and Splunk engineers recount real Prometheus high-cardinality disasters and lessons learned.
- **concept** · [Lightning Talk: Easily Observing Operators - Lili Cosic, Red Hat](https://www.youtube.com/watch?v=-ioN-apfQFc). A lightning talk on how to easily observe Kubernetes operators.
- **concept** · [Jaeger Intro - Yuri Shkuro, Uber Technologies & Pavol Loffay, Red Hat](https://www.youtube.com/watch?v=cXoTja7BvSA)
- **concept** · [Making the Most Out of Kubernetes Audit Logs - Laurent Bernaille & Robert Boll, Datadog](https://www.youtube.com/watch?v=raJRLmGb9Is)
- **concept** · [Fluentd: Cloud Native Logging - Yuta Iwama, Arm Treasure Data & Masahiro Nakagawa, Arm Treasure Data](https://www.youtube.com/watch?v=wyRK26s34M0)
- **concept** · [No-Nonsense Observability Improvement - Cory Watson, SignalFx](https://www.youtube.com/watch?v=HmKAjIlImcU)
- **concept** · [Blazin’ Fast PromQL - Tom Wilkie, Grafana Labs](https://www.youtube.com/watch?v=yYgdZyeBOck)
- **concept** · [Kubernetes SIG Instrumentation - Intro - Frederic Branczyk, Red Hat & Piotr Szczesniak, Google](https://www.youtube.com/watch?v=0MBQzO_6T1s). Introduces Kubernetes SIG Instrumentation, its scope and its work.
- **concept** · [Fine Grained Mesh Metrics for Better Visibility With Native Performance - Mandar Jog & Kuat Yessenov](https://www.youtube.com/watch?v=I-3oHb6lqdU)
- **concept** · [Exporting Kubernetes Event Objects for Better Observability - Mustafa Akın & Ahmet Şeker, Atlassian](https://www.youtube.com/watch?v=_s0o_xAF3Pg)
- **concept** · [Doing Things Prometheus Can’t Do with Prometheus - Tim Simmons, DigitalOcean](https://www.youtube.com/watch?v=hV8mtZSlJ-w)
- **concept** · [Debugging Live Applications the Kubernetes Way: From a Sidecar - Joe Elliott, Grafana Labs](https://www.youtube.com/watch?v=yNTc2-i9arg)
- **concept** · [Prometheus Deep Dive - Ben Kochie, GitLab](https://www.youtube.com/watch?v=Me-kZi4xkEs)
- **concept** · [Thanos Deep Dive: Inside a Distributed Monitoring System - Bartlomiej Plotka & Frederic Branczyk](https://www.youtube.com/watch?v=qQN0N14HXPM)
- **concept** · [Intro: Prometheus - Matt Layher, Fastly & Ganesh Vernekar, Grafana Labs](https://www.youtube.com/watch?v=mC6Zt5Ga9UQ)
- **concept** · [OpenTelemetry: The First R... Morgan McLean, Tristan Sloughter, Sergey Kanzhelev & Chris Kleinknecht](https://www.youtube.com/watch?v=CoLaCKQUkKw)
- **concept** · [Deep Linking Metrics and Traces with OpenTelemetry, OpenMetrics and M3 - Rob Skillington](https://www.youtube.com/watch?v=TzNZIEvhAdA)
- **concept** · [Fluent Bit: Logging and Data Processing on the Edge - Eduardo Silva & Masoud Koleini](https://www.youtube.com/watch?v=2C5Kh3dWKeA). Explains how Fluent Bit handles logging and data processing in edge environments.
- **concept** · [How to Include Latency in SLO-based Alerting - Björn Rabenstein, Grafana Labs](https://www.youtube.com/watch?v=X99X-VDzxnw)
- **concept** · [Jaeger Deep Dive - Yuri Shkuro, Uber Technologies & Pavol Loffay, Red Hat](https://www.youtube.com/watch?v=zb0fdU6c0KU)
- **concept** · [Doing Things Prometheus Can’t Do with Prometheus - Tim Simmons, DigitalOcean](https://www.youtube.com/watch?v=pRmnh8lgjsU)
- **concept** · [Every way we DDoSed our Cortex - Goutham Veeramachaneni, Grafana Labs](https://www.youtube.com/watch?v=VuE5aDHDexU)
- **concept** · [Shipping Metrics From the Edge - Matthias Loibl, Red Hat](https://www.youtube.com/watch?v=FrcfxkbJH20)
- **tutorial** · [Intro to Thanos: Scale Your Prometheus Monitoring With Ease - Lucas Serven & Dominic Green](https://www.youtube.com/watch?v=m0JgWlTc60Q)
- **tutorial** · [Cortex 101: Horizontally Scalable Long Term Storage for Prometheus - Chris Marchbanks, Splunk](https://www.youtube.com/watch?v=f8GmbH0U_kI)
- **tutorial** · [Beyond Getting Started: Using OpenTelemetry to Its Full Potential - Sergey Kanzhelev & Morgan McLean](https://www.youtube.com/watch?v=FlghuHDlQdM)

### 2020 · [KubeCon + CloudNativeCon Europe 2020 - Virtual](../sources/PLj6h78yzYM2O1wlsM-Ma-RYhfT5LKq0XC.md)

- **case study** · [Observability at Scale: Running OpenTelemetry Across an Enterprise - Jonah Back & Kranti Vikram](https://www.youtube.com/watch?v=Dswj-nPy_Fs)
- **case study** · [Scaling Prometheus: How We Got Some Thanos Into Cortex - Thor Hansen, HashiCorp & Marco Pracucci](https://www.youtube.com/watch?v=Z5OJzRogAS4) — HashiCorp
- **case study** · [Migrating to OpenTelemetry From a Custom Distributed Tracing Pipeline - Francis Bogsanyi, Shopify](https://www.youtube.com/watch?v=-SplF2iZ5_E) — Shopify. Shopify describes migrating from a custom distributed tracing pipeline to OpenTelemetry.
- **case study** · [Monitoring GPUs at Scale for AI/ML and HPC Clusters - Bharti L Agrawal, NVIDIA](https://www.youtube.com/watch?v=X5gn_bgxJiw) — NVIDIA
- **case study** · [Stateless Fluentd with Kafka - Steven McDonald, Usabilla](https://www.youtube.com/watch?v=0G9lUnBBM6c) — Usabilla. Usabilla describes running a stateless Fluentd logging pipeline with Kafka.
- **concept** · [Jaeger Intro - Yuri Shkuro, Uber](https://www.youtube.com/watch?v=UNqilb9_zwY)
- **concept** · [Designing a gRPC Interface for Kernel Tracing with eBPF - Leonardo Di Donato, Sysdig](https://www.youtube.com/watch?v=kjOJfNDPVSo)
- **concept** · [Do The Math: Auto-Scaling Applications with Kubernetes - Antoine Hamon, Nephely](https://www.youtube.com/watch?v=6RZNx58GKsg). Explains the math behind autoscaling applications on Kubernetes.
- **concept** · [Jaeger Deep Dive - Pavol Loffay, Red Hat](https://www.youtube.com/watch?v=BWtNelj_XUc)
- **concept** · [Prometheus Deep Dive - Goutham Veeramachaneni, Grafana Labs & Bartłomiej Płotka, Red Hat](https://www.youtube.com/watch?v=Xx16tAoqw70)
- **concept** · [OpenTelemetry Agent and Collector: Telemetry Built-in Into All S... Steve Flanders & Trask Stalnaker](https://www.youtube.com/watch?v=cHiFSprUqa0)
- **concept** · [Make Prometheus Use Less Memory and Restart Faster - Ganesh Vernekar, Grafana Labs](https://www.youtube.com/watch?v=suMhZfg9Cuk)
- **concept** · [Enabling E2E Observability via Open Source in 5G Telco CNFs - Tamas Zsiros & Henrik Saavedra Persson](https://www.youtube.com/watch?v=ZxIesjrP5b0)
- **concept** · [Better Histograms for Prometheus - Björn Rabenstein, Grafana Labs](https://www.youtube.com/watch?v=HG7uzON-IDM)
- **concept** · [Turn It Up to a Million: Ingesting Millions of Metrics with Thanos Receive - Lucas Servén Marín](https://www.youtube.com/watch?v=5MJqdJq41Ms). Explains how Thanos Receive ingests millions of metrics at scale.
- **concept** · [Thanos: Cheap, Simple and Scalable Prometheus - Giedrius Statkevičius & Matthias Loibl](https://www.youtube.com/watch?v=Wroo1n5GWwg)
- **concept** · [Predictable Performance Through Prometheus and Topology Aware Schedu... Killian Muldoon & Tom Golway](https://www.youtube.com/watch?v=WU0nYicYanQ)
- **concept** · [Sponsor Demo: Elastic - Elastic and Kubernetes: From Orchestration to Observability](https://www.youtube.com/watch?v=Ton6V03Ufgc)
- **concept** · [Advanced Logging with Fluent Bit - Eduardo Silva, Arm Treasure Data & Wesley Pettit, Amazon](https://www.youtube.com/watch?v=F73MgV_c2MM)
- **concept** · [Prometheus Introduction - Julius Volz, Prometheus](https://www.youtube.com/watch?v=PzFUwBflXYc)
- **concept** · [Hubble - eBPF Based Observability for Kubernetes - Sebastian Wicki, Isovalent](https://www.youtube.com/watch?v=8WCbGSCyDSo). Introduces Hubble, eBPF-based observability for Kubernetes.
- **concept** · [OpenTelemetry Auto-Instrumentation Deep Dive - Carlos Alberto Cortez & Alex Boten, LightStep](https://www.youtube.com/watch?v=1DxMHqYIvkQ). Deep dive into how OpenTelemetry auto-instrumentation works.
- **tutorial** · [Tracing is For Everyone: Tracing User Events with GraphQL and OpenTelemetry - Nina Stawski, Splunk](https://www.youtube.com/watch?v=8Ldp9w8wm-U). Shows how to trace user events using GraphQL and OpenTelemetry.

### 2020 · [KubeCon + CloudNativeCon North America 2020 - Virtual](../sources/PLj6h78yzYM2Pn8RxfLh2qrXBDftr6Qjut.md)

- **case study** · [Observability Brings Clarity in 5G World - Yamini Sridaran & Praveen George, Affirmed Networks](https://www.youtube.com/watch?v=85qJvhMkOO0) — Affirmed Networks. Affirmed Networks describes how it applies observability to run its 5G network workloads.
- **case study** · [An SLO-Driven Approach to Enhance Kubernetes Cluster Reliability - Qian Ding & Cong Chen](https://www.youtube.com/watch?v=2IfYBwfA80I). Speakers describe an SLO-driven approach to improving the reliability of their Kubernetes clusters.
- **case study** · [Improved TiKV Observability: How We Trace Events under Nanoseconds Latency- Wish Shi & Zhenchi Zhong](https://www.youtube.com/watch?v=50ExGNo1vao) — PingCAP. PingCAP engineers describe how they improved TiKV observability to trace events at nanosecond latency.
- **case study** · [Sponsored Lightning Talk: Why You Need Observability to Adopt Kubernetes at Scale - Shreyans Parekh](https://www.youtube.com/watch?v=euzWPNBSumA)
- **concept** · [Observing Cloud Native Observables with the New SIG Observability - Bartlomiej Płotka, Red Hat](https://www.youtube.com/watch?v=Yg9XByetXsI)
- **concept** · [A New Approach to Logging as a Stack: Fluent Bit + PostgreSQL (FPS) - Jonathan Gonzalez, EDB](https://www.youtube.com/watch?v=pJtma71yAOg)
- **concept** · [Overview and State of Linkerd - William Morgan & Tarun Pothulapati, Buoyant, Inc.](https://www.youtube.com/watch?v=9XlEIURv_3M). Overview and state of the Linkerd project, with recent changes.
- **concept** · [Kubernetes and Logging: Do It Right - Eduardo Silva, Arm Treasure Data](https://www.youtube.com/watch?v=3kIRn6ImIRc). Best practices for implementing logging in Kubernetes using Fluent Bit and related tools.
- **concept** · [Jaeger Deep Dive - Yuri Shkuro, Facebook, Pavol Loffay, Red Hat & Annanay Agarwal, Grafana Labs](https://www.youtube.com/watch?v=dv77X0PSW00)
- **concept** · [Absorbing Thanos Infinite Powers for Multi-Cluster Telemetry - Bartlomiej Płotka](https://www.youtube.com/watch?v=6Nx2BFyr7qQ). Explains how Thanos enables multi-cluster telemetry on top of Prometheus.
- **concept** · [A High-Schooler’s Guide to Kubernetes Network Observability - Drew Ripberger, Nirmata](https://www.youtube.com/watch?v=YqXyMuaZAh4)
- **concept** · [Logging: Fluentd & Fluent Bit - Eduardo Silva & Masahiro Nakagawa, Treasure Data](https://www.youtube.com/watch?v=Af4MtRs4w6g)
- **concept** · [Evolution of Metric Monitoring and Alerting: Upgrade Your Prometheus Today - Bartlomiej Płotka](https://www.youtube.com/watch?v=HpWJg7qZLEY)
- **concept** · [Sponsored Session: AppDynamics - Path to Kubernetes Observability - Jeffrey Holmes, AppDynamics](https://www.youtube.com/watch?v=G7MwSNePLxM)
- **tutorial** · [Intro to Scaling Prometheus with Cortex - Tom Wilkie, Grafana Labs & Ken Haines, Microsoft](https://www.youtube.com/watch?v=oHGoZd-9jWA)
- **tutorial** · [Getting Started with Jaeger - Joe Elliott, Grafana Labs](https://www.youtube.com/watch?v=aMZoUIG-mgY)

### 2021 · [KubeCon + CloudNativeCon + Open Source Summit China 2021](../sources/PLj6h78yzYM2PjmJ9A98QCXnMsmONhU--t.md)

- **case study** · [Best Practice: DNS Failure Observability and Diagnosis in Kubernetes - Yuning Xie, Alibaba](https://www.youtube.com/watch?v=1EjLM_GCWKU) — Alibaba. Alibaba shares its best practices for observing and diagnosing DNS failures in its Kubernetes clusters.
- **concept** · [OSS Project Health Metrics for Gitee Projects - Yehui Wang, Huawei & Georg Link, Bitergia](https://www.youtube.com/watch?v=Z1bzcIejacA)
- **concept** · [On the Need for Metrics to Engage with Open Source Communities - Willem Jiang & Daniel Izquierdo](https://www.youtube.com/watch?v=MXEdzKcpFX4)
- **concept** · [Monitor mesh for edge clusters - Liye Pang, Inspur & Huailong Zhang, Intel](https://www.youtube.com/watch?v=-guZplBR51I). Presents a monitoring mesh design for observing edge clusters.
- **concept** · [Intelligent Analysis on Cloud Infrastructure With AIOps - Ethan Gao, Intel & Pang Liye, Inspur](https://www.youtube.com/watch?v=3aYsp3XjzYw). Describes using AIOps for intelligent analysis of cloud infrastructure.
- **concept** · [Deep Dive Into Profilers: How CPU Profilers Measure Your Application's Performance - Shuang Chen](https://www.youtube.com/watch?v=663AxWUsv7A). Deep dive into how CPU profilers measure application performance.
- **tutorial** · [BPF: Introduction, Programming Tips and Tricks - Wenbo Zhang, PingCAP](https://www.youtube.com/watch?v=-YUkeIUWz58). Introduction to BPF with programming tips and tricks.

### 2021 · [KubeCon + CloudNativeCon Europe 2021](../sources/PLj6h78yzYM2MqBm19mRz9SYLsw4kfQBrC.md)

- **case study** · [How We are Dealing with Metrics at Scale on GitLab.com - Andrew Newdigate, GitLab](https://www.youtube.com/watch?v=6sfr2IGJQXk) — GitLab. GitLab explains how it handles metrics at scale on GitLab.com.
- **case study** · [Building a Community: How Cortex Went from a Vendor Project to a Community - Goutham Veeramachaneni](https://www.youtube.com/watch?v=ng7rpcKvpyQ)
- **case study** · [Better Scalability & More Isolation? The Cortex “Shuffle Sharding” Story - Tom Wilkie, Grafana Labs](https://www.youtube.com/watch?v=1OVpogSKxyI) — Grafana Labs. Grafana Labs tells how shuffle sharding in Cortex improved scalability and tenant isolation.
- **case study** · [High Throughput with Low Resource Usage: A Logging Journey - Eduardo Silva, Calyptia](https://www.youtube.com/watch?v=jaTRWxrcUl8) — Calyptia
- **concept** · [COVID Tracker - Testing & Contact Tracing: How Ireland is Battling COVID-19 - Gar Mac Críosta](https://www.youtube.com/watch?v=sN-lriKyU-Q)
- **concept** · [Prometheus – What it is, What is New, and What is Coming - Richard Hartmann & Julien Pivotto](https://www.youtube.com/watch?v=UsxIDNNIwa0)
- **concept** · [Petabyte Scale Logging with Fluentd and Fluent Bit: A Use Case From... Hanzel Jesheen & Anurag Gupta](https://www.youtube.com/watch?v=OuKm2SiwnGM)
- **concept** · [CNCF SIG Observability Updates - Bartlomiej Płotka, Richard Hartmann & Simone Ferlin](https://www.youtube.com/watch?v=fxscFF7Jwk8)
- **concept** · [Graduated Project Lightning Talk: Fluent Bit - Eduardo Silva, Calyptia](https://www.youtube.com/watch?v=hUik04JYCyo)
- **concept** · [Thanos: Easier Than Ever to Scale Prometheus and Make It Highly Ava... G. Statkevičius & P. Saraswat](https://www.youtube.com/watch?v=mtwwUqeIHAw)
- **concept** · [Log Support in OpenTelemetry - Steve Flanders, Splunk](https://www.youtube.com/watch?v=ypq-nXh38Zk)
- **concept** · [Seamless multi-cluster Communication and Observability with Linkerd - Max Körbächer, Liquid Reply](https://www.youtube.com/watch?v=X70Tb54Y-o4)
- **concept** · [When Prometheus Can’t Take the Load Anymore - Liron Cohen, Riskified](https://www.youtube.com/watch?v=parm7--PQIE)
- **concept** · [Intro and Deep Dive: Kubernetes SIG Instrumentation - Frederic Branczyk, Polar Signals](https://www.youtube.com/watch?v=4yTdJph2Knk). Introduction and deep dive into Kubernetes SIG Instrumentation and its work.
- **concept** · [Jaeger Intro and Deep Dive - Prithvi Raj, Uber & Joe Elliott, Grafana Labs](https://www.youtube.com/watch?v=VDGr79WX11I)
- **concept** · [Cortex: Multi-tenant Scalable Prometheus - Bryan Boreham, Weaveworks & Jacob Tlisi, Grafana Labs](https://www.youtube.com/watch?v=VPBKNfRRytg)
- **concept** · [Graduated Project Lightning Talk: Using Trace Data for Monitoring & Alerting of Appl... Albert Teoh](https://www.youtube.com/watch?v=EaIqBoiRivs)
- **concept** · [Sponsored Session: Salesforce - Using Sloop for Monitoring Highly Available Services](https://www.youtube.com/watch?v=geUT1MoBZF4)
- **concept** · [Sponsored Session: New Relic - Flexible, Open and Easy Observability for Developers](https://www.youtube.com/watch?v=oO4IBm_leRU)
- **concept** · [Sponsored Session: Elastic - Autoscaled K8s Observability with the Elastic Operator](https://www.youtube.com/watch?v=v2mavow40PM)
- **concept** · [Sponsored Session: Dynatrace - Extending OpenTelemetry to Observability](https://www.youtube.com/watch?v=mcCO97AFLus)
- **keynote** · [Cloud Native: The Building Blocks for the Human Experience - Priyanka Sharma & Zain Asgar](https://www.youtube.com/watch?v=2cW8_h98sn8). Keynote on how cloud native technologies underpin the human experience.

### 2021 · [KubeCon + CloudNativeCon North America 2021](../sources/PLj6h78yzYM2Nd1U4RMhv7v88fdiFqeYAP.md)

- **concept** · [Building Prometheus Metrics Support in OpenTelemetry - Alolita Sharma, Amazon](https://www.youtube.com/watch?v=7WV5GMFXaV4). Describes how Prometheus metrics support is being built into OpenTelemetry.
- **concept** · [Cortex: Intro and Production Tips - Bryan Boreham, Grafana Labs & Alvin Lin, Amazon Web Services](https://www.youtube.com/watch?v=zNE_kGcUGuI)
- **concept** · [Conprof - Profiling in the cloud-native era - Matthias Loibl, Polar Signals & Kemal Akkoyun, Red Hat](https://www.youtube.com/watch?v=ficc6_6RYQk)
- **concept** · [Evolving Prometheus for More Use Cases - Bartek Plotka, Red Hat & Chris Marchbanks, Grafana Labs](https://www.youtube.com/watch?v=5R6Fy21MXVE). Maintainers discuss how Prometheus is evolving to cover more use cases.
- **concept** · [What You Need to Know About OpenMetrics - Richard Hartmann, Grafana Labs](https://www.youtube.com/watch?v=MMfmNpoYAec)
- **concept** · [The Prometheus Conformance Program - Richard Hartmann, Grafana Labs](https://www.youtube.com/watch?v=N_OkWRC-xQU)
- **concept** · [Observe with Rust: OpenTelemetry and Tremor - Gary White Jr., Wayfair](https://www.youtube.com/watch?v=RI9cy8OJQmY)
- **concept** · [Beyond the Hype: Cloud Native eBPF - Frederic Branczyk, Polar Signals](https://www.youtube.com/watch?v=2rdNCn_JXYk). Looks past the hype to explain what eBPF offers cloud native systems in practice.
- **concept** · [OpenTelemetry Collector Deployment Patterns - Juraci Paixão Kröhling, Red Hat](https://www.youtube.com/watch?v=WhRrwSHDBFs)
- **concept** · [Effortless Profiling on Kubernetes - Eden Federman, Verizon](https://www.youtube.com/watch?v=VPN-q2rjhxc)
- **concept** · [TAG Observability Update - Matt Young, Everquote & Alolita Sharma, Amazon](https://www.youtube.com/watch?v=Qw1ndSMdqtA)
- **concept** · [Thanos: Highly Available, Pluggable, Long Term Metric Storage for Everyone!- Wiard van Rij, Fullstaq](https://www.youtube.com/watch?v=VG_TtLg84ME)
- **concept** · [Stream vs. Batch: Leveraging M3 and Thanos for Real-Time Aggregation - Gibbs Cullen, Chronosphere](https://www.youtube.com/watch?v=so_017-skv0)
- **concept** · [Fluentd and Fluent Bit - Eduardo Silva, Calyptia](https://www.youtube.com/watch?v=J0dq3rZoLNs)
- **concept** · [Correlating Signals in Opentelemetry: Benefits, Stories, and the Road... Morgan McLean & Jaana Dogan](https://www.youtube.com/watch?v=lQG6UKpTs6M)
- **concept** · [Jaeger: Intro and Deep Dive - Jonah Kowall, Logz.io](https://www.youtube.com/watch?v=Wyrcik2XbgE)
- **concept** · [Native Instrumentation for Open Source Software with OpenTelemetry - Ted Young & Ludmila Molkova](https://www.youtube.com/watch?v=6UqCo32vdeI). Argues for open source libraries to ship native OpenTelemetry instrumentation and explains how to do it.
- **panel** · [Cloud Native and Kubernetes Observability Panel: The State of Union](https://www.youtube.com/watch?v=5_YecRaB6ww). Panel on the state of cloud native and Kubernetes observability.
- **keynote** · [EmpowerUs, sponsored by Chronosphere](https://www.youtube.com/watch?v=0ulTbE9nK2Q). A Chronosphere-sponsored EmpowerUs session at KubeCon North America 2021.

### 2022 · [KubeCon + CloudNativeCon Europe 2022](../sources/PLj6h78yzYM2MCEgkd8zH0vJWF7jdQ-GRR.md)

- **case study** · [From Monitoring to Observability: Left Shift your SLOs with Chaos - Michael Friedrich, GitLab](https://www.youtube.com/watch?v=BkREMg8adaI) — GitLab
- **case study** · [Kubernetes Everywhere: Lessons Learned From Going Multi-Cloud - Niko Smeds, Grafana Labs](https://www.youtube.com/watch?v=ZY5h8Atc14A) — Grafana Labs
- **concept** · [gRPC For Microservices: Service-mesh and Observability - Sanjay Pujare & Wenbo Zhu‎, Google](https://www.youtube.com/watch?v=y2lKORewzJA)
- **concept** · [Build a Cloud Native Logging Pipeline on the Edge with Fluentbit Operator - Feynman Zhou, QingCloud](https://www.youtube.com/watch?v=D_nyUhO8Y7Q)
- **concept** · [OpenTelemetry: The Road Ahead + Meet the Co... Morgan McLean, Alolita Sharma, Ted Young, Daniel Dyla](https://www.youtube.com/watch?v=2uuqGuKpyQ8). OpenTelemetry maintainers present the project's roadmap and meet the community.
- **concept** · [Logs Told Us It Was DNS, It Felt Like DNS, It Had To Be DNS, I... Laurent Bernaille & Elijah Andrews](https://www.youtube.com/watch?v=NunyPkN0n3c)
- **concept** · [Metrics as a First-Class Citizen in the E2E Testing Landscape - Matej Gera & Jéssica Lins, Red Hat](https://www.youtube.com/watch?v=jFm3WBtFhv4)
- **concept** · [Lightning Talk: Thank you Keptn Obvious! Making SLOs observable with Prometheus a... Andreas Grabner](https://www.youtube.com/watch?v=5NDozsGMWIg). Lightning talk showing how Keptn makes SLOs observable with Prometheus.
- **concept** · [Prometheus Intro and Deep Dive - Julius Volz, Björn Rabenstein, Matthias Rampke](https://www.youtube.com/watch?v=eM3RXdK1yys)
- **concept** · [The Soul of a New Command: Adding ‘Events’ to kubectl - Bryan Boreham, Grafana Labs](https://www.youtube.com/watch?v=YI1ZuN-OHNw)
- **concept** · [Autoscaling Elasticsearch for Logs on Kubernetes - Radu Gheorghe & Ciprian Hacman](https://www.youtube.com/watch?v=ONGqk3xXRTw)
- **concept** · [Why, How to, and Issues: Tail-Based Sampling in the OpenTelemetry Collector - Reese Lee, New Relic](https://www.youtube.com/watch?v=l4PeclHKl7I)
- **concept** · [Prometheus Sparse High-Resolution Histograms in Action - Ganesh Vernekar, Grafana Labs](https://www.youtube.com/watch?v=T2GvcYNth9U)
- **concept** · [Alerting in the Prometheus Ecosystem: The Past, Present and Future - Josue (Josh) Abreu](https://www.youtube.com/watch?v=9AX8u-bt4J8). Reviews the history, current state and future of alerting in the Prometheus ecosystem.
- **concept** · [Better Reliability Through Observability and Experimentation - Julie Gunderson & Kerim Satirli](https://www.youtube.com/watch?v=DeewkVL3RWI)
- **concept** · [OpenTelemetry: The Vision, Reality, and How to Get Started - Dotan Horovits, Logz.io](https://www.youtube.com/watch?v=qE1ggEmvz2Y)
- **concept** · [Operating Prometheus in a Serverless World - Colin Douch, Cloudflare](https://www.youtube.com/watch?v=Zln_Kvv7hxY)
- **concept** · [Jaeger: Present and Future - Pavol Loffay, Red Hat & Jonah Kowall, Logz.io](https://www.youtube.com/watch?v=NWQD_uCGP6k)
- **concept** · [Fluent Bit: Logs, OpenMetrics, and OpenTelemetry all-in-one - Eduardo Silva & Anurag Gupta, Calyptia](https://www.youtube.com/watch?v=TciIQVve2V0)
- **concept** · [How Attackers Use Exposed Prometheus Server to Exploit... David de Torres Huerta & Miguel Hernández](https://www.youtube.com/watch?v=5cbbm_L6n7w). Demonstrates how attackers exploit exposed Prometheus servers to compromise Kubernetes environments.
- **concept** · [Story of Correlation: Integrating Thanos Metrics with Observabi... Bartłomiej Płotka & Kemal Akkoyun](https://www.youtube.com/watch?v=rWFb01GW0mQ)
- **tutorial** · [Intro to Kubernetes, GitOps, and Observability Hands-On Tutorial - Joaquin Rodriguez & Tiffany Wang](https://www.youtube.com/watch?v=WKvogzTg2iM)
- **other** · [What Is the CNCF TAG Observability and How You Can Join Our Effort!](https://www.youtube.com/watch?v=50s0XrD-ZEQ). Overview of CNCF TAG Observability and how to get involved.

### 2022 · [KubeCon + CloudNativeCon North America 2022](../sources/PLj6h78yzYM2O5aNpRM71NQyx3WUe1xpTn.md)

- **case study** · [DoorDash’s Journey From StatsD To Prometheus With 10 Million Metrics/Second - Emma Wang & Ben Raskin](https://www.youtube.com/watch?v=xkEGmPF0kCQ)
- **case study** · [Customer Centric Observability: How Intuit Reduced Time To Detect... - Vinit Samel & Nagaraja Tantry](https://www.youtube.com/watch?v=b6m4Kk1z-24) — Intuit
- **case study** · [Tamland: How GitLab.Com Uses Long-Term Monitoring Data For Capacity Forecasting. - Andrew Newdigate](https://www.youtube.com/watch?v=Aa5IT3PWLO0) — GitLab. GitLab shows how Tamland uses long-term monitoring data to forecast capacity for GitLab.com.
- **concept** · [Jaeger: The Future with OpenTelemetry and Metrics- Jonah Kowall, Logz.io & Joe Elliott, Grafana Labs](https://www.youtube.com/watch?v=i18XQVg0Ad8)
- **concept** · [SLO-Based Observability For All Kubernetes Cluster Components - Matthias Loibl & Nadine Vehling](https://www.youtube.com/watch?v=AC38JtXXE50). Shows SLO-based observability for all Kubernetes cluster components.
- **concept** · [Running the Observability As a Service For Your Teams With Thanos - Ben Ye & Bartłomiej Płotka](https://www.youtube.com/watch?v=I4Mfyfd_4M8)
- **concept** · [Fluent Bit V2.0: Unifying Open Standards For Logs, Metrics & Traces - Eduardo Silva & Anurag Gupta](https://www.youtube.com/watch?v=avzx7MNpB_w)
- **concept** · [Tips And Tricks To Successfully Migrate From Jaeger To OpenTelemetry - Vineeth Pothulapati](https://www.youtube.com/watch?v=6Vnuu2oVEMA). Gives tips and tricks for migrating from Jaeger instrumentation and backends to OpenTelemetry.
- **concept** · [Stateless Collectors For Stateful Data: Scaling Prometheus As a Node Agent - Danny Clark, Google](https://www.youtube.com/watch?v=yk2aaAyxgKw)
- **concept** · [Observability In ArgoCD/Rollouts Using Streaming ML For Reducing MTTR - Vigith Maurice & A Kalamkar](https://www.youtube.com/watch?v=-YGS1hmd60E). Shows using streaming ML on ArgoCD/Rollouts observability data to reduce MTTR.
- **concept** · [Prometheus - Intro, Deep Dive, And Open Q+A - Goutham Veeramachaneni & Ganesh Vernekar, Grafana Labs](https://www.youtube.com/watch?v=45n_Nf5xhaw). Prometheus intro and deep dive with open Q&A.
- **concept** · [2022 Observability TAG Update - Alolita Sharma, Apple & Matt Young, TAG Observability](https://www.youtube.com/watch?v=LwRYD8uS7pk)
- **concept** · [Current State and the Future of Cortex - Alvin Lin & Alan Protasio, Amazon Web Services](https://www.youtube.com/watch?v=u1SfBAGWHgQ)
- **concept** · [Keptn Beyond 1.0: Sailing into the...-Thomas Schuetz & Andi Grabner, Brad McCoy, Ana Medina](https://www.youtube.com/watch?v=6bAfrMhdQdQ). Project update on Keptn after 1.0 and its roadmap.
- **concept** · [When the Logs Just Don’t Cut It: Root-Causing Incidents Without Re-Deploying Prod- Phillip Kuznetsov](https://www.youtube.com/watch?v=QCABjMm5JpA)
- **concept** · [OpenMetrics; the State Of 1.X And the Plans For 2.0 - Richard Hartmann, Grafana Labs](https://www.youtube.com/watch?v=8zyoYFFiIdI). Covers the state of OpenMetrics 1.x and plans for 2.0.
- **concept** · [Unified Chaos Injection And SLO Validation... - Srinivasan Parthasarathy & Shubham Chaudhary](https://www.youtube.com/watch?v=aeTCYm1x-co)
- **concept** · [Lightning Talk: Metrics, How To Measure What Is Going On In Your Community - Peter O'Neill, Styra](https://www.youtube.com/watch?v=kgGW82pgT8M)
- **panel** · [OpenTelemetry: Meet the Community, Build the Roadmap - Morgan, Daniel, Ted, Alolita](https://www.youtube.com/watch?v=7mYNLafiaOk). OpenTelemetry maintainers meet the community and discuss the roadmap.

### 2023 · [KubeCon + CloudNativeCon + Open Source Summit China 2023](../sources/PLj6h78yzYM2OJcjIuAsbbhXAaDrAnuKRB.md)

- **concept** · [Build a High Performance Remote Storage for Prometheus with Unlimited Time Series - Yang Xiang](https://www.youtube.com/watch?v=7pQZyYEz1l4). Presents a high performance remote storage design for Prometheus with unlimited time series.
- **concept** · [Prometheus Intro and Deep Dive - Richard Hartmann, Grafana Labs](https://www.youtube.com/watch?v=t3YFv20Ulnc)
- **concept** · [SIG Instrumentation: Intro, Deep Dive and Recent... - Mengjiao Liu & Shivanshu Raj Shrivastava](https://www.youtube.com/watch?v=5RSQUyqok2s). Intro and deep dive on SIG Instrumentation and its recent work.
- **concept** · [Revolutionizing Kubernetes Logging: Structured Logs for Enhanced Monitoring - Naman Lakhwani, VMware](https://www.youtube.com/watch?v=MO8EroNA-5I)
- **concept** · [Scaling up and Scaling Out Networking, Observability, and Security... - Bill Mulligan & Jaff Cheng](https://www.youtube.com/watch?v=l4Fe2YdtfvU)
- **concept** · [Balancing Cost and Quality in OpenTelemetry: An Evaluation of Sampling Policies - Zhu Jiekun, Quwan](https://www.youtube.com/watch?v=hDLQi6HeW0k)
- **concept** · [Enabling Zero Code Observability for Financial Applications Using WebAssembly - Casey Li](https://www.youtube.com/watch?v=AWxV9TW6ncI). Shows how WebAssembly enables zero-code observability for financial applications.
- **concept** · [Multi-Cluster Alerting: A Kubernetes-Native Approach - Junot Xiang & Wanjun Lei, QingCloud](https://www.youtube.com/watch?v=JXBTsj-rJ3k)
- **tutorial** · [Tutorial: A Hitchhiker's Guide to CNCF/OSS Observability So... Matthias Haeussler & Tiffany Jernigan](https://www.youtube.com/watch?v=XEa92rVChno)

### 2023 · [KubeCon + CloudNativeCon Europe 2023](../sources/PLj6h78yzYM2PyrvCoOii4rAopBswfz1p7.md)

- **case study** · [Hazardous Defaults: Managing Cardinality and Performance for Your Lo... Derek Cavanaugh & Sara Moore](https://www.youtube.com/watch?v=A1YgG0yz68Q). Discusses managing cardinality and performance pitfalls from hazardous defaults in logging and observability setups.
- **case study** · [Multi-Cluster Observability with Service Mesh - That Is a Lot of Moving Parts!? - Ryota Sawada](https://www.youtube.com/watch?v=6KTzE3LppDg). The speaker shares their experience operating multi-cluster observability across a service mesh and the complexity involved.
- **case study** · [Show Me the Metrics: How a Huge Bank Does Observability with Multi-Tenancy... - Inacio & Costa](https://www.youtube.com/watch?v=8eeKVGQowDI) — Itaú Unibanco. A large bank describes running multi-tenant metrics observability at scale for its own teams.
- **case study** · [Continuous Profiling Your Production Kubernetes Deployments Running a... Vijay Samuel & Nick Pordash](https://www.youtube.com/watch?v=6TqzXj1I8aw) — eBay. Describes how continuous profiling was run on production Kubernetes deployments at scale.
- **case study** · [Intuit’s Customer Centric Observability Journey Using AIOps - Vigith Maurice & Amit Kalamkar, Intuit](https://www.youtube.com/watch?v=D-eQxDBbx48) — Intuit
- **concept** · [Using OpenTelemetry for Application Security, with a Real Life Example - Ron Vider, Oxeye](https://www.youtube.com/watch?v=hz3ncpPKzUs)
- **concept** · [Prometheus Updates and Deep Dive - Kemal Akkoyun, Polar Signals & Bryan Boreham, Grafana Labs](https://www.youtube.com/watch?v=qQpehBEOakY)
- **concept** · [Combat Maintainer Burnout with Proactive Metrics - Sophia Vargas, Google](https://www.youtube.com/watch?v=C2Zn2tqsU6I)
- **concept** · [Observability with Fluent Bit: Logs, Metrics & Traces - Eduardo Silva & Anurag Gupta, Calyptia](https://www.youtube.com/watch?v=PP8vlQBRtts)
- **concept** · [Jaeger: The Future with OpenTelemetry and Metrics - Pavol Loffay, Red Hat & Jonah Kowall, Aiven](https://www.youtube.com/watch?v=-J8tEDi1WFE). Project update on Jaeger's future direction with OpenTelemetry and metrics support.
- **concept** · [Past, Present, & Future of eBPF in Cloud Native Observability - Frederic Branczyk & Natalie Serrino](https://www.youtube.com/watch?v=pb_eAVAWq2o)
- **concept** · [Understand Systems with OpenTelemetry: A Hybrid Telemetry Data Backend - Ran Xu & Xiaochun Yang](https://www.youtube.com/watch?v=Zo9HVe2KUo4)
- **concept** · [Emergent Load Testing: Rules for Organized Chaos - Nicole van der Hoeven, Grafana Labs](https://www.youtube.com/watch?v=YhHX2ULmnOo)
- **concept** · [Kubernetes Defensive Monitoring with Prometheus - David de Torres Huerta & Mirco De Zorzi, Sysdig](https://www.youtube.com/watch?v=Ammf8oJhPkY)
- **concept** · [OpenTelemetry: Using Unified Semantics to Drive Insights + Project... - Morgan, Alolita, Daniel, Ted](https://www.youtube.com/watch?v=dFKpbfGJVxI)
- **concept** · [Revamping Kubernetes with Contextual and Structured Logging, a Deep Dive - Shivanshu Shrivastava](https://www.youtube.com/watch?v=njoyvh07i4s)
- **concept** · [The RPC Revolution: Getting the Most Out of gRPC - Richard Belleville & Kevin Nilson, Google](https://www.youtube.com/watch?v=9dBMPrwtGAQ). Google's gRPC maintainers explain how to get more out of gRPC through its features and best practices.
- **concept** · [What Could Go Wrong with a GraphQL Query and Can OpenTelemetry Help?- Sonja Chevre & Ahmet Soormally](https://www.youtube.com/watch?v=IkEUJjRBCbo)
- **concept** · [Connected Observability Pipelines in the OpenTelemetry Collector - Dan Jaglowski, observIQ](https://www.youtube.com/watch?v=uPpZ23iu6kI)
- **concept** · [Effortless Open Source Observability with Cilium, Prometheus... - Raymond de Jong & Anna Kapuścińska](https://www.youtube.com/watch?v=l3zY7wHUkBA)
- **concept** · [Metrics at Full Throttle: Intro and Deep Dive Into Thanos - Saswata Mukherjee & Filip Petkovski](https://www.youtube.com/watch?v=2GokLB5_VfY). Introduction to Thanos plus a deep dive into its architecture and recent improvements.
- **concept** · [Cortex: How to Run a Rock Solid Multi-Tenant Prometheus - Friedrich Gonzalez, Adobe & Alan Protasio](https://www.youtube.com/watch?v=Pl5hEoRPLJU)
- **tutorial** · [OTel Me About Metrics: A Metrics 101 Crash Course - Reese Lee, New Relic](https://www.youtube.com/watch?v=QDEpOV1kiio)
- **tutorial** · [Tutorial: Getting Familiar with Security Observability Using eBPF &Cilium Tetragon - Holmes & Cooley](https://www.youtube.com/watch?v=kTGU-Nc2Db0)
- **tutorial** · [Tutorial: Building an Open Source Observability Stack - Troisi, Mehta & Nguyen, Kolbitsch](https://www.youtube.com/watch?v=0XwwCp1NQyQ). Hands-on tutorial building an open source observability stack.
- **tutorial** · [Tutorial: Exploring the Power of OpenTelemetry on..- Loffay, Bongartz & Oliveira Sa, Neumann, Pathak](https://www.youtube.com/watch?v=XvPsdjNrpKo)
- **panel** · [Defining A Common Observability Query Language and Other Observabili... Alolita Sharma & Matt Young](https://www.youtube.com/watch?v=9mchgI3mr_8). Discussion of defining a common observability query language and other observability topics.

### 2023 · [KubeCon + CloudNativeCon NA 2023](../sources/PLj6h78yzYM2MYc0X1465RzF_7Cqf7bnqL.md)

- **case study** · [Journey to Becoming an OpenTelemetry Approver - Jamie Danielson, Honeycomb.io](https://www.youtube.com/watch?v=onAwzVlRxtI) — Honeycomb.io
- **case study** · [How and Why You Should Adopt and Expose OSS Interfaces Like Otel... - Daniel Hrabovcak & Shishi Chen](https://www.youtube.com/watch?v=D71fK2MFreI)
- **concept** · [Observability in the Cloud Native Era - Why Is It Still so Hard?](https://www.youtube.com/watch?v=rs-5SYlCj80)
- **concept** · [Build in Observability While Developing - Jamie Danielson, Honeycomb.io](https://www.youtube.com/watch?v=TXO_d594Ri8)
- **concept** · [E2E Observability for Connected Vehicle Service via Distributed Tracing - Kota Endo & Masanori Itoh](https://www.youtube.com/watch?v=qEU7xamQxYQ)
- **concept** · [Collecting Low-Level Metrics with eBPF - Mauricio Vásquez Bernal, Microsoft](https://www.youtube.com/watch?v=_ft3iTw5uv8)
- **concept** · [All You Need to Know About Prometheus in 2023: Decade of Monitoring - Julien Pivotto & Ben Kochie](https://www.youtube.com/watch?v=xoaQ9RIDqfs)
- **concept** · [Fluent Bit: Telemetry Agent - Eduardo Silva, Calyptia](https://www.youtube.com/watch?v=TYUrYMZ1tvg)
- **concept** · [Observability TAG Updates: Enhancing Kubernetes Observability and Query Language Standardization](https://www.youtube.com/watch?v=kRTmUr-4yIc)
- **concept** · [eBPF for Observability: Data Overload Panacea or Pain...](https://www.youtube.com/watch?v=3wyfGmUNPE8). Examines whether eBPF-based observability solves or worsens data overload.
- **concept** · [Introducing Logs in OpenTelemetry: What It Unlocks and How to Use It - Morgan McLean & Dan Jaglowski](https://www.youtube.com/watch?v=a1KZwfLr2PQ)
- **concept** · [Logging Deep Dive and Best Practices - Eduardo Silva, Calyptia](https://www.youtube.com/watch?v=1dQd2seQrkA). Deep dive into logging architecture and best practices for cloud native environments.
- **concept** · [Remote Control for Observability Using the Open Agent Management Prot... Jacob Aronoff & Andy Keller](https://www.youtube.com/watch?v=t550FzDi054)
- **concept** · [OpenTelemetry: What's Next? Logs, Profiles... Morgan McLean, Ted Young, Alolita Sharma & Daniel Dyla](https://www.youtube.com/watch?v=OEGgmTNfYsU)
- **concept** · [Jaeger the Future with OpenTelemetry and Metrics - Pavol Loffay, Red Hat](https://www.youtube.com/watch?v=vR6HkNpi8Os)
- **concept** · [Paint the Picture! - Detecting Suspicious Data Patterns in E... Natalia Reka Ivanko & John Fastabend](../sources/videos/-2FykHaqvlg.md). Shows how Tetragon uses eBPF and kTLS to detect suspicious data patterns in encrypted traffic.
- **concept** · [OpenTelemetry Tracing for Monoliths - Phillip Carter, Honeycomb](https://www.youtube.com/watch?v=kzXT0WlTBpw)
- **concept** · [Thanos Unleashed: Mastering the Challenges of Production-Scale Metrics - Joel Verezhak, Open Systems](https://www.youtube.com/watch?v=Q3qOZ7SEgcM)
- **concept** · [eBPF + Wasm: Lightweight Observability on Steroids - Michael Yuan & Yusheng Zheng](https://www.youtube.com/watch?v=cZk0Jsi4N5Y)
- **concept** · [gRPC Tapping Filter with Hardware Accelerated in Service Mesh - Yizhou Xu & Devan Nair](https://www.youtube.com/watch?v=2qbMEZzbSyY). Shows how a gRPC tapping filter can be hardware accelerated in a service mesh.
- **tutorial** · [A Practical Guide to Debugging Browser Performance with OpenTelemetry - Purvi Kanal, Honeycomb](https://www.youtube.com/watch?v=0J1z599tmfY). Practical guide to debugging browser performance using OpenTelemetry.
- **tutorial** · [Tutorial: Exploring the Power of Metrics Collection with OpenTelemetry on Kubernetes...](https://www.youtube.com/watch?v=hsI7mCJ0JSE)
- **tutorial** · [Tutorial: Mastering Etcd Observability: A Comprehensive Guide to M... Bogdan Kanivets & Vivek Patani](https://www.youtube.com/watch?v=GtAIwwJ5EJk)
- **tutorial** · [Tutorial: OpenTelemetry 101: Let's Instrument! - Paige Cruz, Chronosphere](https://www.youtube.com/watch?v=CB2nEcnBBcE)

### 2024 · [KubeCon + CloudNativeCon + Open Source Summit + AI_dev China 2024](../sources/PLj6h78yzYM2NcAGHRxgBHY8x3QTfnZQCv.md)

- **concept** · [OpAMP: Scaling OpenTelemetry with Flexibility - Husni Alhamdani & Herbert Sianturi](https://www.youtube.com/watch?v=F8ZR26X3Ib4)
- **concept** · [Observability Supercharger: Build the Traffic Topology Map for Millio...- Sheng Wei & Teck Chuan Lim](https://www.youtube.com/watch?v=FmDcO3EqhMA)
- **concept** · [KubeSkoop: Deal with the Complexity of Network Issues and Monitoring... - Yutong Li & Bingshen Wang](https://www.youtube.com/watch?v=DnOkHQx92hE)
- **concept** · [Kelemetry: Global Control Plane Tracing for Kubernetes - Wei Shao & Jonathan Chan, ByteDance](https://www.youtube.com/watch?v=G5O8SpN-UJ4)
- **concept** · [Implement Auto Instrumentation Under GraalVM Static Compilation on OTel Java Agent - Zihao Rao](https://www.youtube.com/watch?v=NXO4nvsahtU)
- **concept** · [Beyond the Basics: Towards Making Thanos Production-Ready - Benjamin Huo & Junhao Zhang](https://www.youtube.com/watch?v=sTXYJTypdTk)
- **concept** · [OpenTelemetry Amplified: Full Observability with EBPF-Enabled Distributed... - Kai Liu & Wanqi Yang](https://www.youtube.com/watch?v=uGj_QwdvIlA)
- **concept** · [OpenTelemetry Community Update | OpenTelemetry社区更新 - Zihao Rao, Huxing Zhang & Wanqi Yang, Jared Tan](https://www.youtube.com/watch?v=4UFXBy12VZc). OpenTelemetry community update on recent progress and roadmap.
- **concept** · [Scorecard: Assessments Made Easy | Scorecard：让开源项目评估更轻松 - Ram Iyengar, Cloud Foundry Foundation](https://www.youtube.com/watch?v=88jdTmvnGVs). Introduces OpenSSF Scorecard for easily assessing the security posture of open source projects.
- **concept** · [Lightning Talk: How Prometheus AI Agent Helps Build Interactive Monitoring?  - Zhihao Liu, Quwan](https://www.youtube.com/watch?v=v-LHviDYYmk)
- **concept** · [Project Lightning Talk: Telemetry API and Open Telemetry: the answer of istio monitoring?](https://www.youtube.com/watch?v=k9JD_sDdLqo)
- **concept** · [Project Lightning Talk: Adaptive Tracing Propagation with OpenTelemetry: Navigating Protocol Div...](https://www.youtube.com/watch?v=17sPjWV35YU). Lightning talk on adaptive tracing propagation with OpenTelemetry across divergent protocols.

### 2024 · [KubeCon + CloudNativeCon Europe 2024](../sources/PLj6h78yzYM2N8nw1YcqqKveySH6_0VnI0.md)

- **case study** · [From RUM to Front-End Observability with OpenTelemetry - Purvi Kanal, Honeycomb](https://www.youtube.com/watch?v=l2_wsvv-Rhs) — Honeycomb
- **case study** · [From UI to Storage: Unraveling the Magic of Thanos Query Processing](https://www.youtube.com/watch?v=ZGQIitaKoTM)
- **concept** · [Prometheus Update from the Maintainers - Bryan Boreham, Grafana Labs & Simon Pasquier, Red Hat](https://www.youtube.com/watch?v=D0jE4BSzX3Y)
- **concept** · [Observable Feature Rollouts with OpenTelemetry and OpenFeature - Daniel Dyla & Michael Beemer](https://www.youtube.com/watch?v=euYhIn4leW0)
- **concept** · [Fluent Bit v3: Unified Layer for Logs, Metrics and Traces - Eduardo Silva, Calyptia](https://www.youtube.com/watch?v=4SqDRokC7ac). Introduces Fluent Bit v3 as a unified layer for logs, metrics and traces.
- **concept** · [Thanos’ Infinity Stones and How You Can Operate Them! - Saswata Mukherjee & Daniel Mohr, Red Hat](https://www.youtube.com/watch?v=e8kvX6mRlyE)
- **concept** · [Observability TAG: A Review and the Rise of Gen-AI Observability](https://www.youtube.com/watch?v=YluNsK0hgrw)
- **concept** · [Leverage Contextual and Structured Logging in K8s for Enhanced Monitoring](https://www.youtube.com/watch?v=qdZA_TpIK68)
- **concept** · [Prometheus and OpenTelemetry: Better Together - Adriana Villela & Reese Lee](https://www.youtube.com/watch?v=LJd1pJ0k28g)
- **concept** · [Fast and Efficient Log Processing with Wasm and eBPF - Michael Yuan, Second State](https://www.youtube.com/watch?v=4u7nUpZxr3g). Shows how Wasm and eBPF can be combined for fast, efficient log processing.
- **concept** · [Intelligent Observability: The Foundation for Operating Smarter in the Age of AI - Alolita Sharma](https://www.youtube.com/watch?v=8sQo493lOiE). Explains intelligent observability as a foundation for operating smarter in the age of AI.
- **concept** · [Distributed Tracing with Jaeger and OpenTelemetry - Pavol Loffay, Red Hat & Jonah Kowall, Aiven](https://www.youtube.com/watch?v=WNfesi_T0Bs)
- **concept** · [Disintegrated Telemetry: The Pains of Monitoring Asynchronous Workflows - Johannes Tax, Grafana Labs](https://www.youtube.com/watch?v=GvF1ivr7RlA)
- **concept** · [Monitoring Kubernetes and Cloud Spend with OpenCost | Project Lightning Talk](https://www.youtube.com/watch?v=OQzZcHXL_7o)
- **concept** · [OpenTelemetry for OSS! | Project Lightning Talk](https://www.youtube.com/watch?v=yjVCOhxJH-0)
- **concept** · [A little bit of pixie dust: Evolving the on-premise experience with Tinkerbell | Project Lightnin...](https://www.youtube.com/watch?v=IoCB5MK3GEU)
- **concept** · [Crossplane Observability &Traceability for Effective Multi-Cloud... - Katharina Sick & Viktor Farcic](https://www.youtube.com/watch?v=R2NBPX2x9n4)
- **concept** · [Dealing with eBPF’s Observability Data Deluge - Anna Kapuścińska, Isovalent](https://www.youtube.com/watch?v=yWB8n_e4N14)
- **concept** · [Cortex Intro: Multi-Tenant Scalable Prometheus - Ben Ye & Friedrich Gonzalez](https://www.youtube.com/watch?v=by538PPSPQ0)
- **tutorial** · [Tutorial: Exploring the Power of Distributed Tracing with OpenTelemetry on Kubernetes](https://www.youtube.com/watch?v=nwy0I6vdtEE)
- **panel** · [OpenTelemetry: Project Updates, Next Steps, and AMA](https://www.youtube.com/watch?v=wQ3ntXP8SSw)

### 2024 · [KubeCon + CloudNativeCon India 2024](../sources/PLj6h78yzYM2P0vFbS4o1I0gRHSiXgLiEe.md)

- **case study** · [From Three Pillars to More with OpenTelemetry - Steve Flanders, Splunk](https://www.youtube.com/watch?v=WG8NA0J_YLo) — Splunk
- **concept** · [Lightning Talk: From Creation to Termination: Your Pod's Digital Footprint - Subha Seenivasan](https://www.youtube.com/watch?v=8uJLO8JkhIM). Lightning talk tracing a pod's lifecycle and the footprint it leaves from creation to termination.
- **concept** · [Tying OpenFeature and OpenTelemetry for Automated Rollouts of New S... Pranay Prateek & Ekansh Gupta](https://www.youtube.com/watch?v=8hi-qixOYNc). Shows how to combine OpenFeature and OpenTelemetry to automate rollouts of new features.
- **concept** · [Cilium: Connecting, Observing, and Securing Kubernetes and Beyond with eBPF - B. Mulligan & N. Bisht](https://www.youtube.com/watch?v=0ZnxpVkBxpo). Overview of Cilium for connecting, observing and securing Kubernetes with eBPF.
- **concept** · [WebAssembly Profiling with Pprof and Wzprof - Rajiv Ranjan Singh & Naman Lakhwani](https://www.youtube.com/watch?v=LaQZVxOixGY)
- **tutorial** · [Unleashing Observability: Enabling Distributed Tracing in gRPC... - Purnesh Dixit & Sourabh Singh](https://www.youtube.com/watch?v=6d5rJHT-Gv4). Shows how to enable distributed tracing in gRPC services with OpenTelemetry.

### 2024 · [KubeCon + CloudNativeCon NA 2024 - Salt Lake City](../sources/PLj6h78yzYM2Pw4mRw4S-1p_xLARMqPkA7.md)

- **case study** · [Lessons Learned Adopting OpenTelemetry at Scale - Alex Arnell, Heroku / Salesforce](https://www.youtube.com/watch?v=5iM8n3uCo_U) — Heroku, Salesforce. Heroku/Salesforce shares lessons learned adopting OpenTelemetry at scale.
- **case study** · [How We Made OpenTelemetry Be Our Fitness Tracker for Your CI/CD Pipelines! - N. Woerner, A. Grabner](https://www.youtube.com/watch?v=IRNyf_MLHDw) — A. Grabner
- **case study** · [Understanding How OpenTelemetry Network Uses eBPF for Network Observab... S.R. Shrivastava, J. Perry](https://www.youtube.com/watch?v=Ljf671BSu2g) — OpenTelemetry Network
- **case study** · [From Observability to Enforcement: Lessons Learned Implementing eBPF R... A. Kapuścińska, K. Kourtis](https://www.youtube.com/watch?v=Hw469I5GKmY)
- **case study** · [Watching the Watchers: How We Do Continuous Reliability at Grafana Labs - Nicole van der Hoeven](https://www.youtube.com/watch?v=pCxmwvqTklo) — Grafana
- **case study** · [From Observability to Performance - Nadia Pinaeva, Red Hat & Antonio Ojea, Google](https://www.youtube.com/watch?v=uYo2O3jbJLk) — Red Hat, Google
- **case study** · [OpenTelemetry: The OpenTelemetry Hero’s Journey: Working with Open Source Observability | PLT](https://www.youtube.com/watch?v=WO0wJGnLg7c)
- **concept** · [Mastering OpenTelemetry Collector Configuration - Steve Flanders, Cisco](https://www.youtube.com/watch?v=vzJpDNfA5xU)
- **concept** · [Low-Overhead, Zero-Instrumentation, Continuous Profiling for OpenTelemetry - Christos Kalkanis](https://www.youtube.com/watch?v=WtNDLgdIn24)
- **concept** · [Cognitive and Self-Adaptive System for Effective Distributed-Tracing in Appl... M. Tandon, A. Gusain](https://www.youtube.com/watch?v=9V_iLfYsScY). Proposes a cognitive, self-adaptive approach to distributed tracing in applications.
- **concept** · [Fluent Bit: Better Pipelines for Observability - Eduardo Silva, Chronosphere](https://www.youtube.com/watch?v=XCaA6eXsztE)
- **concept** · [Cortex Intro: Multi-Tenant Scalable Prometheus - Charlie Le, Apple & Daniel Blando, Amazon](https://www.youtube.com/watch?v=OGAEWCoM6Tw)
- **concept** · [Celebrating Prometheus 3.0: A Deep Dive with the Maintainers - Richard Hartman & Josh Abreu](https://www.youtube.com/watch?v=9ROvfBqpdu4). Prometheus maintainers walk through the features and changes in the Prometheus 3.0 release.
- **concept** · [Observability TAG Round-up and What’s New for AI Observability - Alolita Sharma & Chris Larsen](https://www.youtube.com/watch?v=xFrB0HHQZms)
- **concept** · [OpenTelemetry Project Update - A. Sharma, J. Paixão Kröhling, T. Young, M. Mclean, D. Dyla](https://www.youtube.com/watch?v=rX7gKt4QlTk)
- **concept** · [Distributed Tracing with Jaeger and OpenTelemetry - Jonah Kowall, Paessler & Pavol Loffay, Red Hat](https://www.youtube.com/watch?v=J2mXmwK3uss)
- **concept** · [Unifying Observability: Correlating Metrics, Traces, and Logs with Exemplars an... K.P. Simha, C. Le](https://www.youtube.com/watch?v=zYF1JIZmpI4)
- **concept** · [Unlocking Cost Savings & New Possibilities: Your Guide to Prometheus Remote W... C. Styan, B. Płotka](https://www.youtube.com/watch?v=o5HpeMtpsTg)
- **concept** · [Optimizing LLM Performance in Kubernetes with OpenTelemetry - Ashok Chandrasekar & Liudmila Molkova](https://www.youtube.com/watch?v=6rdeFACyyYg). Shows how to use OpenTelemetry to observe and optimize LLM performance on Kubernetes.
- **concept** · [Choose Your Own Adventure: The Observability Odyssey - Whitney Lee & Viktor Farcic](https://www.youtube.com/watch?v=R3CFETvCBFU)
- **concept** · [Shopify’s Open Source Approach to Network Monitoring with eBPF, Vector... S. Rabenhorst, M. Franklin](https://www.youtube.com/watch?v=FpVjdaRVmA4)
- **concept** · [Supercharge Your Kubernetes Autoscaling with Custom Metrics - V. Krishna Samudrala, S. Akinapally](https://www.youtube.com/watch?v=LrL9tRnAH0M)
- **concept** · [Thanos: Intro and Updates - Ben Ye, Amazon Web Services](https://www.youtube.com/watch?v=SR2sG4wno-s)
- **concept** · [Service Profiling Based Management and Scheduling in K8- Jia Deng, Cong Xu & Mingmeng Luo, Bytedance](https://www.youtube.com/watch?v=nbc5acJv9r0)
- **concept** · [Jaeger: Distributed Tracing with Jaeger and OpenTelemetry | Project Lightning Talk](https://www.youtube.com/watch?v=xpN0fuWEmX8)
- **concept** · [OpenTelemetry: OpenTelemetry in Five Minutes | Project Lightning Talk](https://www.youtube.com/watch?v=l8xiNOCIdLY)
- **concept** · [Prometheus: Celebrating Prometheus 3.0: All You Need To Know! | Project Lightning Talk](https://www.youtube.com/watch?v=jcDtB150inI)
- **concept** · [Inspektor Gadget: eBPF for Observability, Made Easy and Approachable | Project Lightning Talk](https://www.youtube.com/watch?v=_nR1cHhBth8)
- **concept** · [OpenTelemetry: The Future of Network Monitoring eBPF for Low-Level Insights | Project Lightning Talk](https://www.youtube.com/watch?v=LSAl0qVWXKQ)
- **concept** · [Using OpenTelemetry for Deep Observability Within Messaging Queues - S.R. Shrivastava, E. Gupta](https://www.youtube.com/watch?v=IuOurlfAYhI)
- **concept** · [Lightning Talk: Minimizing Data Loss Within the OpenTelemetry (OTel) Collector - Alex Kats](https://www.youtube.com/watch?v=xxRkfVXdy9E)
- **tutorial** · [Tutorial: OpenTelemetry Hands-on - Automatic and Manual Instrumentatio... T. Angerstein, T. Jernigan](https://www.youtube.com/watch?v=8CKgAyenEjo). Hands-on tutorial covering automatic and manual instrumentation with OpenTelemetry.

### 2025 · [KubeCon + CloudNativeCon China 2025 (Hong Kong)](../sources/PLj6h78yzYM2P1xtALqTcCmRAa6142uERl.md)

- **concept** · [Antipatterns in Observability: Lessons Learned and How OpenTelemetry Solves Them - Steve Flanders](https://www.youtube.com/watch?v=2xX3Fx_WVSo). Covers common observability antipatterns and how OpenTelemetry addresses them.
- **concept** · [Advancing Observability With Compile-Time Auto-Instrumentation in G... Liu Ziming & Przemek Delewski](https://www.youtube.com/watch?v=xEsVOhBdlZY)
- **concept** · [OpenTelemetry Project Update - Zihao Rao, Hui Wang & Jared Tan](https://www.youtube.com/watch?v=W9ynhEWKmdA)
- **concept** · [Unified Observability in GRPC: Metrics and Tracing Using OpenTelemetry Plugin - Purnesh Dixit](https://www.youtube.com/watch?v=_Fr10UoFI7Y)
- **concept** · [China Mobile's Panji Platform: Observability Practices and Implementations... Jing Shang & Casey Li](https://www.youtube.com/watch?v=zN1j4EpVwjY)

### 2025 · [KubeCon + CloudNativeCon Europe 2025 - London](../sources/PLj6h78yzYM2MP0QhYFK8HOb8UqgbIkLMc.md)

- **case study** · [How To Adopt OpenTelemetry in an Enterprise Where Incumbent Vendor Tools Reign Supre... Chris Weldon](https://www.youtube.com/watch?v=JqRXqk-1CLo)
- **case study** · [Pushing the Limits of Prometheus at Etsy - Chris Leavoy, Etsy & Bryan Boreham, Grafana Labs](https://www.youtube.com/watch?v=IWrd-pSojqg) — Etsy, Grafana Labs
- **concept** · [Fluent Bit v4: A Decade of Innovation and What’s Next - Leonardo Alminana, Chronosphere](https://www.youtube.com/watch?v=Ae2-LNHtUr8)
- **concept** · [Evolving OpenID Connect and Observability in Keycloak - Ryan Emerson & Takashi Norimatsu](https://www.youtube.com/watch?v=bC4xbBJs0CA)
- **concept** · [The State of Prometheus and OpenTelemetry Interoperability - Arthur Sens & Juraj Michálek](https://www.youtube.com/watch?v=JFS0lSfHtMI)
- **concept** · [The Missing Metrics: Measuring Memory Interference in Cloud Native Systems - Jonathan Perry](https://www.youtube.com/watch?v=nXdGXdxmWNQ)
- **concept** · [How To Supercharge AI/ML Observability With OpenTelemetry and Fluent Bit - Celalettin Calis](https://www.youtube.com/watch?v=DVFQ20OrEFk)
- **concept** · [Using eBPF for Non-invasive, Performant, Instant Network Monitoring - Mario Macías & Marc Tudurí](https://www.youtube.com/watch?v=HV3Nb_wUro4)
- **concept** · [From the Observability TAG: Designing a Common Query... lolita Sharma, Pereira Braga & Chris Larsen](https://www.youtube.com/watch?v=1iWD14xvBQA). Observability TAG presents work on designing a common query language across telemetry signals.
- **concept** · [How To Rename Metrics Without Impacting Somebody’s Observabili... Bartłomiej Płotka & Arianna Vespri](https://www.youtube.com/watch?v=Rw4c7lmdyFs)
- **concept** · [Prometheus Deep Dive: What’s New in v3.0 and Beyond - Saswata Mukherjee & Fiona Liao](https://www.youtube.com/watch?v=KS_rGWazTio)
- **concept** · [OpenTelemetry Project Update](https://www.youtube.com/watch?v=nclJn1KEjis)
- **concept** · [Jaeger V2: OpenTelemetry at the Core of Modern Distributed Tracing - Jonah Kowall, Paessler](https://www.youtube.com/watch?v=_3fpZA-DqDU)
- **concept** · [Standardizing CI/CD Observability With OpenTelemetry: Insights Fr... Dotan Horovits & Adriel Perkins](https://www.youtube.com/watch?v=IvIgsHS5MDk)
- **concept** · [Logs, Metrics, Traces and Mayhem: An Interactive Observability Adventure... Jay Clifford & Tom Glenn](https://www.youtube.com/watch?v=D8r5j_R9QsA)
- **concept** · [How Green Is My OpenTelemetry Collector? - Nancy Chauhan, Student & Adriana Villela, Dynatrace](https://www.youtube.com/watch?v=ea2CKLX5vEs)
- **concept** · [An Exemplary Path: Leveraging EBPFs and OpenTelemetry To Aut... Charlie Le & Kruthika Prasanna Simha](https://www.youtube.com/watch?v=u-eUO3rIQV4)
- **concept** · [Asimov's Zeroth Law of Robotics: Observability for AI - Nicole van der Hoeven, Grafana Labs](https://www.youtube.com/watch?v=x6EKTCAWtn8)
- **concept** · [Deep Dive To AI Agent Observability - Guangya Liu, IBM & Karthik Kalyanaraman, Langtrace AI](https://www.youtube.com/watch?v=1B9WZ6H0cn4). Deep dive into observability for AI agents.
- **concept** · [Enhancing Database Observability With OpenTelemetry - Marylia Gutierrez, Grafana Labs](https://www.youtube.com/watch?v=Rf9NceXXRuw)
- **concept** · [First Day Foresight: Anomaly Detection for Observability - Prashant Gupta & Kruthika Prasanna Simha](https://www.youtube.com/watch?v=jiT7kGqcpR4)
- **concept** · [Project Lightning Talk: Perses Update - Augustin Husson, Maintainer](https://www.youtube.com/watch?v=81SMpKgJb3k). Maintainer update on the Perses dashboard project.
- **concept** · [Project Lightning Talk: Prometheus 3.0 Speedrun - Ben Kochie, Maintainer](https://www.youtube.com/watch?v=NRL-bSYVi7Q)
- **concept** · [Optimizing Metrics Collection & Serving When Autoscaling LLM Workloads - Vincent Hou & Jiří Kremser](https://www.youtube.com/watch?v=lefjb4Vnd8k)
- **concept** · [Observability Pipeline Query Languages: Present and the Future - Jacek Migdal, Quesma](https://www.youtube.com/watch?v=iiI91sUMtdg)
- **concept** · [Limitless Possibilities, Consistent Design: Crafting Dashboards... Nicolas Takashi & Antoine Thébaud](https://www.youtube.com/watch?v=7h70Olo5Uzk). Discusses crafting consistent, flexible observability dashboards.
- **concept** · [OTel Sucks (But Also Rocks!) - Juraci Paixão Kröhling, OllyGarden & Daniel Dyla, Dynatrace](https://www.youtube.com/watch?v=QzStkLbA7Qk)
- **concept** · [OTel Me How To Get My Open Source Community Taken Seriously: Lessons... Reese Lee & Adriana Villela](https://www.youtube.com/watch?v=Hdrf5QosFTw)
- **concept** · [Lightning Talk: Observability Diet: Your 5-Step Plan To Trim the Data Fat - Pranay Prateek, SigNoz](https://www.youtube.com/watch?v=xE3iMfib2LA)
- **concept** · [Taming 50 Billion Time Series: Operating Global-Scale Prometheus Dep... Orcun Berkem & Alan Protasio](https://www.youtube.com/watch?v=OqLpKJwKZlk)
- **concept** · [Where’s All My Memory Gone? Mapping K8s Memory Metrics To Physical Resources - Mahé Tardy](https://www.youtube.com/watch?v=zLHdgl2qxbg)
- **concept** · [C.A.L.L.I.N.G. Now I'm Calling You, Calling You Now - Mario Macías & Terra Tauri, Grafana Labs](https://www.youtube.com/watch?v=2BIhTXQd0CI). Grafana Labs speakers explain an observability approach that builds on OpenTelemetry and eBPF instrumentation.
- **tutorial** · [Learning Kubernetes Through the Lens of Metrics - Priyanka Saggu & Mario Jason Braganza](https://www.youtube.com/watch?v=95NNuV-SUdg). Teaches Kubernetes concepts by exploring them through metrics.
- **tutorial** · [Project Lightning Talk: Quick Intro to CI/CD Observability with OpenTelemetry - Dotan Horovits](https://www.youtube.com/watch?v=vpMHv-56gsk)
- **panel** · [Cortex: Insights, U... Friedrich Gonzalez, Daniel Sabsay, Charlie Le, Alolita Sharma & Daniel Blando](https://www.youtube.com/watch?v=3aUg2qxfoZU). Several Cortex maintainers and contributors discuss project insights and updates.

### 2025 · [KubeCon + CloudNativeCon India 2025](../sources/PLj6h78yzYM2MEQTMX_LIOK1hrePHxLD6U.md)

- **case study** · [Observability at Scale With Monitoring as Code... Vipin GopalaKrishnapillai & Saiabhinay Bommakanti](https://www.youtube.com/watch?v=3nHnGjTmgNk). Presents practicing observability at scale through monitoring-as-code, based on the speakers' organization's own approach.
- **concept** · [Project Lightning Talk: OTel 2025: The Latest Milestones and What’s Next - Steve Flanders](https://www.youtube.com/watch?v=5DOj91l20bw). Project update on OpenTelemetry's recent milestones and what comes next.
- **concept** · [Effortless, Standardised Homelab Observability With eBPF - Goutham Veeramachaneni, Grafana Labs](https://www.youtube.com/watch?v=CzTdtlqcFhQ)
- **concept** · [Unlocking Kubernetes Observability: Secure, Tenant-Cen... Bingi Narasimha Karthik & Ramkumar Nagaraj](https://www.youtube.com/watch?v=gI40zpbES5w)
- **concept** · [Building a Scalable Observability Platform for Edge Compute Nodes - Naveen Kumar S P & Karthik A](https://www.youtube.com/watch?v=z5ef-4fS5xs)
- **concept** · [Auto-instrumentation for GPU Performance Using eBPF - Annanay Agarwal, Grafana Labs](https://www.youtube.com/watch?v=eEBAFyLB9Zg)

### 2025 · [KubeCon + CloudNativeCon Japan 2025 (Tokyo)](../sources/PLj6h78yzYM2PsNdcBGWR_mVN-SRLQl6KM.md)

- **concept** · [Never Underestimate Memory Architecture - Bryan Boreham, Grafana Labs](https://www.youtube.com/watch?v=C6aBa1vnYT4)
- **concept** · [Prometheus 3.0 and the New Governance: Setting the Project up for the Next Decade - Josue Abreu](https://www.youtube.com/watch?v=DTDp7tw0rgw)
- **concept** · [Lightning Talk: Practical Monitoring for Knative Serving - Kazuki Higashiguchi, Autify](https://www.youtube.com/watch?v=GXlnSqYGHyA)
- **concept** · [Debugging OpenTelemetry: Ensuring Your Observability Signals Are Spot On - Kasper Borg Nissen, Dash0](https://www.youtube.com/watch?v=k6PSX8I-IJY)
- **concept** · [Project Lightning Talk: OTel 2025: The Latest Milestones and What’s Next - Greg Leffler, Contributor](https://www.youtube.com/watch?v=GvRHPpa5Unc)
- **concept** · [The Future of Prometheus Exposition Format - Arthur Sens, Grafana Labs](https://www.youtube.com/watch?v=pRFUFJIAluk)
- **concept** · [Green OpenTelemetry: Have Your Cake and Eat It Too - Adriana Villela, Dynatrace](https://www.youtube.com/watch?v=XNLC3TVB868)

### 2025 · [KubeCon + CloudNativeCon North America 2025](../sources/PLj6h78yzYM2MLSW4tUDO2gs2pR5UpiD0C.md)

- **case study** · [Building Scalable End-to-end Latency Metrics From Distributed Trace - Kusha Maharshi, Bloomberg](https://www.youtube.com/watch?v=6xxqm9LIhoU) — Bloomberg. Bloomberg describes building scalable end-to-end latency metrics from distributed traces.
- **case study** · [Designing for Observability: From Noise To Insight - Andrea Chomiak, Dash0](https://www.youtube.com/watch?v=KGPX3-xasK8) — Dash0
- **case study** · [Making Application Rollouts Observable, Actionable and Boring - Vasudev Bongale, LinkedIn](https://www.youtube.com/watch?v=8QS3hmsDjNE) — LinkedIn. LinkedIn shows how it made application rollouts observable, actionable and boring.
- **concept** · [Prometheus Intro, Deep Dive, and Open Q+A - Owen Williams, Grafana Labs & David Ashpole, Google](https://www.youtube.com/watch?v=81pbYzd6sNI). Introduction and deep dive into Prometheus with an open Q&A from maintainers.
- **concept** · [From Panic To Peace: Making K8s Controller Observability Suck Less - Cat Morris & Derik Evangelista](https://www.youtube.com/watch?v=1P76Roya9oQ). Shows ways to make Kubernetes controllers easier to observe and debug.
- **concept** · [Debugging Your Cluster When It’s on Fire - Nikola Grcevski, Grafana Labs & Tyler Yahn, Splunk](https://www.youtube.com/watch?v=Jy0d9QXZXrQ)
- **concept** · [The Future of Debugging Is No Debugging: Observability Is Dead - Jeremy Adams, Neo4j](https://www.youtube.com/watch?v=nBka0VrCWpE)
- **concept** · [Lightning Talk: Summarizing the Noise: LLM Observability With Open Data Hub, VLLM... Twinkll Sisodia](https://www.youtube.com/watch?v=QFH8nfWt8Es)
- **concept** · [Lightning Talk: Tracing the Untraceable: OpenTelemetry for ‘Vibe-Coded’ LLM Apps - Pranay Prateek](https://www.youtube.com/watch?v=dprArlELOBU)
- **concept** · [OpenTelemetry Logs Driving a Major Shift: Events, Richer Data, and Smarter Semantics - Robert Pająk](https://www.youtube.com/watch?v=-j6bHtUV3IA). Explains how OpenTelemetry logs are shifting toward events, richer data and better semantics.
- **concept** · [Fluent Bit: Smarter Telemetry Routing, Faster Pipelines - Eduardo Silva, Chronosphere](https://www.youtube.com/watch?v=40gHwYn0bo4). Covers Fluent Bit features for smarter telemetry routing and faster pipelines.
- **concept** · [Where’s My Pod? End-to-End Tracing for Kubernetes With OpenTelemetry - Artem Tkachuk & JP Phillips](https://www.youtube.com/watch?v=Dn0gvU2Czno)
- **concept** · [Retrofitting OTEL Collectors & Prometheus - How To Overcome Scale... Vijay Samuel & Sandeep Raveesh](https://www.youtube.com/watch?v=O5GdShQJCgE)
- **concept** · [OpenTelemetry: Unpacking 2025, Charti... Alolita Sharma, Morgan McLean, Josh Suereth & Austin Parker](https://www.youtube.com/watch?v=RRX_L1ZjMco)
- **concept** · [UX Research Report: Prometheus and OTel's Resource Attributes. - Victoria Nduka & Amy Super](https://www.youtube.com/watch?v=cSLXIAc020A)
- **concept** · [Zero-Downtime Telemetry: Hot Reloading OpenTelemetry Collector Pipel... Amir Jakoby & Shiran Melamed](https://www.youtube.com/watch?v=ngm1mHVfcgY)
- **concept** · [Observing Dark Matter With OpenTelemetry - Sam Alipio & Mario Macías, Grafana Labs](https://www.youtube.com/watch?v=pfBw4g1LdAM)
- **concept** · [Integrating Data Center Observability Into Cloud Native Envi... Pedro Célestin & Julia Furst Morgado](https://www.youtube.com/watch?v=TsNfSKppiPU)
- **concept** · [Project Lightning Talk: Fluent Bit - Eduardo Silva, Maintainer](https://www.youtube.com/watch?v=6m0vgUeYkNc). A maintainer lightning talk on Fluent Bit project updates.
- **concept** · [Confidential Observability on Kubernetes: Protecting Telemetry End-to-End- Jitendra Singh, Microsoft](https://www.youtube.com/watch?v=ZVM8azeTHAU)
- **tutorial** · [Who Wants To Secure Clusters ? - Henrik Rexed & Simon Reisinger, Dynatrace](https://www.youtube.com/watch?v=8UXgIHSh8K0). Walkthrough of securing Kubernetes clusters.
- **tutorial** · [OTel+K8s= ❤️: An Introduction To OpenTelemetry for Kubernetes... Christos Markou & Jacob Aronoff](https://www.youtube.com/watch?v=cCGNs7nyutU)
- **panel** · [Beyond the Dashboard: Modern Observability... Danielle C, Whitney L, Stevie C, Khallai T & Payal B](https://www.youtube.com/watch?v=46qRFcv_FDY). Panel discussing modern observability beyond dashboards.

### 2026 · [Keynotes - KubeCon + CloudNativeCon Japan 2026](../sources/PLOZCGaPFoeIM.md)

- **concept** · [OpenTelemetry Celebrates Graduation and the Next Era of Agentic... - Alolita Sharma & Ted Young](https://www.youtube.com/watch?v=W3WSCDURjvg)

### 2026 · [KubeCon + CloudNativeCon + OpenInfra Summit + PyTorch Conference China 2026](../sources/PLGcxfZT6qI-w.md)

- **case study** · [End-to-End Observability for LLM Inference: From Token To GPU - Jared Tan, Murphy Chen & Nicole Li](https://www.youtube.com/watch?v=K6doiHgBabk) — Murphy Chen
- **concept** · [Why Your TTFT Lies: Diagnosing PD-Disaggregated LLM Inference with Minimal... Nicole Li & Kebe Liu](https://www.youtube.com/watch?v=5rWtmHfYUCA). Explains how to diagnose time-to-first-token in prefill/decode-disaggregated LLM inference.
- **concept** · [Non-Invasive AI Agent Observability With OBI - Haibin Zhang, Alibaba Cloud & Endre Sara, Causely](https://www.youtube.com/watch?v=AWPjeQBZ9Eo). Shows non-invasive observability of AI agents using OpenTelemetry eBPF instrumentation (OBI).

### 2026 · [KubeCon + CloudNativeCon Europe 2026](../sources/PLj6h78yzYM2MXCOWSN9CqqID6OOvF7wxL.md)

- **case study** · [From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat R... Willem Berroubache](https://www.youtube.com/watch?v=XiNsfhUxO2Y)
- **case study** · [Is the Agent in the Room with Us Right Now? - Nick Rutigliano & Andrew Halaney, Netflix](https://www.youtube.com/watch?v=-rwTJebNC10) — Netflix. Netflix engineers share their own experience with AI agents operating in their environment and the challenges of knowing what agents are doing.
- **case study** · [Fluent Bit V5: Pushing the Limits of Observability at Scale - Eduardo Silva](https://www.youtube.com/watch?v=w1pj0Lz1mW4)
- **case study** · [How Manual OTel Instrumentation Saves More Than Just Money - Juliano Costa & Yuri Oliveira](https://www.youtube.com/watch?v=13Lyvy48Y6A). Argues that manual OTel instrumentation reduces observability cost and more, based on the speakers' own experience.
- **case study** · [Accelerating Thanos at Scale: Faster and Cheaper Queries With Parquet - Giedrius Statkevičius](https://www.youtube.com/watch?v=PySEmqtrvL8)
- **case study** · [Preventing S3 Cost Storms: Applying Cortex’s Efficiency Lessons to I/O-Heav... A. Fishman-Lichterman](https://www.youtube.com/watch?v=7pFxk027sHw) — Cortex. Applies Cortex's lessons on preventing S3 cost spikes to I/O-heavy workloads.
- **concept** · [We Deleted Our Observability Stack and Rebuilt It With OTEL: 12 Engine... Yash Sharma & Kunju Perath](https://www.youtube.com/watch?v=Z0oum6Eh1is)
- **concept** · [Project Lightning Talk: Fluent Bit V5 - Eduardo Silva, Maintainer](https://www.youtube.com/watch?v=BwpXIkXOLOU)
- **concept** · [Discover Cortex: High Scalability Metrics in 2026 - Friedrich Gonzalez & Charlie Le, Apple](https://www.youtube.com/watch?v=PCeS4YLKTwg)
- **concept** · [CRI-O: Faster Pulls, Better Metrics, and a Future Beyond Images - Sohan Kunkerkar & Ayato Tokubi](https://www.youtube.com/watch?v=en2oz2BWHW8)
- **concept** · [Prometheus V3 One Year In: OpenMetrics 2.0 and More! - Jan Fajerski & Bartłomiej Płotka](https://www.youtube.com/watch?v=6vE9b6StC0g). A Prometheus project update one year after V3, covering OpenMetrics 2.0.
- **concept** · [The Fourth Pillar Arrives: OpenTelemetry Profiling Alpha in A... Felix Geisendörfer & Florian Lehner](https://www.youtube.com/watch?v=TKp2snmgvtQ)
- **concept** · [Cutting Metrics Traffic, Cutting Costs: The AZ-Aware Observ...  Iris Dyrmishi & Rodrigo Fior Kuntzer](https://www.youtube.com/watch?v=ycnDgULCHTA)
- **concept** · [18 Bluetooth Controllers Walk into a Bar: Observability & R... Simon Schrottner & Manuel Timelthaler](https://www.youtube.com/watch?v=Y9agHID8Ml4)
- **concept** · [Hacking GPU Observability: eBPF & Ephemeral Containers in Action on Kubernetes - Brandon Kang](https://www.youtube.com/watch?v=mkH38O3wLog)
- **concept** · [Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF - Zahari Dichev](https://www.youtube.com/watch?v=J61kV92bSt0)
- **concept** · [The Missing Half of Performance Profiling: Understanding Memory in Cloud Native Syste... Dom Delnano](https://www.youtube.com/watch?v=rTkrS46meSM)
- **concept** · [OpenTelemetry Collector SIG: Project Updates - Jade G, Dmitrii A, Alex B, Evan B & Antoine T](https://www.youtube.com/watch?v=0zwLl8QGOdM). Project updates from the OpenTelemetry Collector SIG.
- **concept** · [Observing Chaos: Real-Time Monitoring of AI-Driven Kubernetes Destr... Josh Halley & Ricardo Aravena](https://www.youtube.com/watch?v=KOM-PQNpcjk)
- **concept** · [Jaeger V2: The Maintainers' Guide To OpenTelemetry-Native Tracing - Pavol Loffay, Red Hat](https://www.youtube.com/watch?v=gH_JzIXFshI)
- **concept** · [OpenTelemetry Project Update and 'Ask the Experts' - Pablo B, Juraci P, Marylia G & Severin N](https://www.youtube.com/watch?v=mvSGusgcVuw)
- **concept** · [OpenTelemetry Logs Driving a Major Shift: Events, Richer Data, and Smarter Semantics - Robert Pająk](https://www.youtube.com/watch?v=aoEe2FDnnDk)
- **concept** · [Enriching Telemetry Signals Through Lookups in the OTel Collector - João Duarte, Elastic](https://www.youtube.com/watch?v=OVffupWFEtw)
- **concept** · [GenAI Observability: Keeping GenAI Honest Without Oversharing - Liudmila Molkova, Grafana Labs](https://www.youtube.com/watch?v=Q4E9GDAslIk)
- **concept** · [Retroactive Sampling with OpenTelemetry: Cut 90% Distributed Traci... Roman Khavronenko & Zhu Jiekun](https://www.youtube.com/watch?v=ehKzt_kGEeM)
- **concept** · [Smoothed and Anchored Rate Calculation in PromQL - Björn Rabenstein, Grafana Labs](https://www.youtube.com/watch?v=iN5vQjDuiWc)
- **concept** · [Istio's Ambient Mesh: The Real Cost of Sidecar-less Tracing - Mofesola Babalola & Hannah Olukoye](https://www.youtube.com/watch?v=wI9a3GuJw7U)
- **concept** · [DNS Tracing & Metrics Via eBPF in OpenTelemetry- Endre Sara, Causely & Nikola Grcevski, Grafana Labs](https://www.youtube.com/watch?v=YMqSK6uBhxU)
- **tutorial** · [Hello World, Meet the Spanimals: Observability for Beginners - Tiffany Jernigan & Matthias Haeussler](https://www.youtube.com/watch?v=_bLAN_mzxIs)
- **tutorial** · [Tutorial: Full-Stack Observability on a Budget: A Guide to Strategic Sampling and Da... Pavol Loffay](https://www.youtube.com/watch?v=2iW0DMZqMMA). A hands-on guide to reducing observability costs through strategic sampling and data reduction.
- **tutorial** · [When OTTL Goes Off the Rails: Debugging Transformations wit... Edmo Vamerlatti Costa & Tyler Helmuth](https://www.youtube.com/watch?v=465RlwgsNHg). Shows how to debug OpenTelemetry OTTL transformations that misbehave.

### 2026 · [KubeCon + CloudNativeCon India 2026](../sources/PLj6h78yzYM2PmaTdAzefPqjawTlop1lgG.md)

- **case study** · [Who Watches the Watchers? From Closed Observability To... Aditi Gupta, Madhu Patel & Sandeep Kanabar](https://www.youtube.com/watch?v=nYxLSHljwxQ)
- **concept** · [Patients as Time-Series: High-Stakes Clinical Alerting With Ope... Seema Saharan & Aakanksha Saharan](https://www.youtube.com/watch?v=Vn5OkBWVV5o)
- **concept** · [Offline but Not Blind: Observability in Air-Gapped Kubernetes Environment - Manoj Sardana](https://www.youtube.com/watch?v=Ith_TOa85Lw)
- **concept** · [The Invisible Tax: How Data Format Conversions Drive up Telemetry Pipeline Costs - Cijo Thomas](https://www.youtube.com/watch?v=A-94_ip0IFo). Explains how data format conversions in telemetry pipelines add hidden cost.
- **concept** · [The Lean Observability Stack: Quick and Native Telemetry for Service... Arpitha Srivathsa Malavalli](https://www.youtube.com/watch?v=UEuQ56hZhpc)
- **concept** · [When Kafka Goes Cloud Native: Observability That Actually Works! - Roopadharsini K & Mary Vinothini](https://www.youtube.com/watch?v=vZXJfJtgEQc)
- **concept** · [What Did My Agent Do? Observability and Accountability for AI Agents - Ishan Jain, Grafana Labs](https://www.youtube.com/watch?v=Bx_BU7dGyiI)
- **panel** · [Observability 2.0: Shifting Left From Reactive Mon... Kokilavani K, RK Gupta, Sivakumar K & Suresh K](../sources/videos/-Fr26VOeX4E.md). Panel with Intuit, Atlassian and Cloudera practitioners on the shift from traditional monitoring to LLM-assisted 'observability 2.0'.

### 2026 · [KubeCon + CloudNativeCon Japan 2026](../sources/PLH1zduub3WrE.md)

- **case study** · [Repurposing OpenTelemetry Traces as Test Data: Breaking the Cost Barrier in System… Y. Fujikane](https://www.youtube.com/watch?v=68VhjKfv7KQ). Describes reusing OpenTelemetry traces as test data to lower the cost of system testing.
- **case study** · [From Statsd To OpenTelemetry: Atlassian's Metrics Platform Migration… I. Grace Endozo & F. Vazirnia](https://www.youtube.com/watch?v=Qhtq9IuBKxg)
- **case study** · [From Tool Calls To Context Fabric: Building AI-Native Observability for… D. Choudhary & D. Kapur](https://www.youtube.com/watch?v=svCz4PBg0Uk)
- **case study** · [Lessons From Five+ Years of Fluent Bit: Building a Global-Scale Observability Agent - Hiroshi Hatake](https://www.youtube.com/watch?v=68nH0PMLAhk) — Fluent Bit. Hiroshi Hatake shares lessons from more than five years of building and operating Fluent Bit as a global-scale observability agent.
- **concept** · [One Binary, Two Ecosystems: Embedding Prometheus Exporters With OCB - Kyle Eckhart & Arthur Sens](https://www.youtube.com/watch?v=SbtH6iIt1DQ)
- **concept** · [OTel Meets Wasm: Rethinking OpenTelemetry Collector Extensibility - Kotaro Inoue & Tsuzuki Tsuchiya](https://www.youtube.com/watch?v=zvdaQXDRRXQ)
- **concept** · [Designing for High-cardinality Metrics - Walther Lee & Aleksandr Krivoshchekov, Reddit](https://www.youtube.com/watch?v=wI_nKRNjdxo)
- **concept** · [Standardizing Industrial IoT Observability With OpenTelemetry - Alolita Sharma, Apple](https://www.youtube.com/watch?v=AMDE02bLCpY). Shows how OpenTelemetry can standardize observability for industrial IoT systems.
- **concept** · [⚡Lightning Talk: Learning Kubernetes From Logs: Building a Foundation for Future… K. Ishii](https://www.youtube.com/watch?v=JUgkesGAtlw)
- **concept** · [Project Lightning Talk: Spiderpool Unlocks Fine-Grained RDMA Observability for AI Inference - W. Lan](https://www.youtube.com/watch?v=l2jx6aGz4Rc)
- **concept** · [Project Lightning Talk: New Frontiers for OpenTelemetry - A Roadmap for the Future - Ted Young](https://www.youtube.com/watch?v=E-JoSRNq6hg)
- **concept** · [Vulnerability Response for Large Open Source Projects - Jo Guerreiro & Charline Voinot, Grafana Labs](https://www.youtube.com/watch?v=UFQVGdcAb6A)
