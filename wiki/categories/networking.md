---
title: "Networking"
summary: 659 talks (86 case studies) across 33 events; organizations include Lyft, Spotify, Google, HP, Datadog, Buoyant.
tags: [category, networking]
generated: categories
---

# Networking

> 659 talks across 33 events, oldest first: 86 case studies where an organization reports its own experience, plus concept talks and tutorials.

Keywords: networking, cni, cilium, calico, service mesh, istio, linkerd, envoy, gateway api, ingress, dns, coredns, load balancing, network policy, ebpf, multi-cluster networking (edit under `categories:` in wiki.yaml).

## Over time

| Year | Talks | Case studies |
| --- | --- | --- |
| 2016 | 4 | 0 |
| 2017 | 24 | 5 |
| 2018 | 86 | 12 |
| 2019 | 100 | 14 |
| 2020 | 55 | 5 |
| 2021 | 48 | 9 |
| 2022 | 46 | 4 |
| 2023 | 75 | 7 |
| 2024 | 104 | 15 |
| 2025 | 64 | 8 |
| 2026 | 53 | 7 |

## Organizations with case studies

Lyft (4), Spotify (3), Google (2), HP (2), Datadog (2), Buoyant (2), Airbnb (2), VMware (2), Concur, Monzo, Credit Karma, Booking.com, Form3, Heptio, Zachary Arnold & Austin Adams' employer, The Weather Company, IBM, ControlPlane, Inspur, Onefootball, Yahoo, Verizon, Yelp, Fred..., Fault, Cruise, H-E-B, Tencent, PingCAP, Alibaba, Salesforce, Absa Group, Niantic, Intuit, Amazon Web Services, Buoyant, Inc, DoorDash, Decathlon, eBay, EarnIn, Cash App, Microsoft, OpenTelemetry Network, Red Hat, NVIDIA, New York Times, Preferred, Meta, Careem, Feesh, Skyscanner

## Talks by event

### 2016 · [KubeCon + CloudNativeCon North America 2016 (Seattle)](../sources/PLj6h78yzYM2PqgIGU1Qmi8nY7dqn9PCr4.md)

- **concept** · [Lightning Talk - Introducing CoreDNS Kubernetes Integration by John Belamaric, Infoblox](https://www.youtube.com/watch?v=oKmir1aiSR8)
- **concept** · [Kubernetes Ingress: Your Router, Your Rules by Gerred Dillon, Deis](https://www.youtube.com/watch?v=Syw2PzRudIM)
- **concept** · [Navigating the Container Jungle by Casey Davenport, Tigera](https://www.youtube.com/watch?v=9fKDoCB5mHQ). Tigera's Casey Davenport gives an overview of container networking options and how to choose among them.
- **panel** · [Kubernetes Networking Panel: Collaborate on the Spec, Compete on Execution](https://www.youtube.com/watch?v=iVZeGA3kW08)

### 2017 · [KubeCon + CloudNativeCon Europe 2017 (Berlin)](../sources/PLj6h78yzYM2PAavlbv0iZkod4IVh_iGqV.md)

- **case study** · [Switching From External Load Balancing to consul & ingress [I] - Dan Wilson, Concur](https://www.youtube.com/watch?v=gsf__yuWCF8) — Concur
- **case study** · [When Failure is Not an Option: Processing Real Money at Monzo with Kubernetes and Linkerd [I]](https://www.youtube.com/watch?v=wBgBwNZo_EE) — Monzo
- **concept** · [Life of a Packet [I] - Michael Rubin, Google](https://www.youtube.com/watch?v=0Omvgd7Hg1I). Traces how a packet travels through Kubernetes networking.
- **concept** · [K8SNIff - End-to-End Encryption Till the Pod [A] - Sebastian Scheele & Jason Murray, Loodse GmbH](https://www.youtube.com/watch?v=3nNIyaJ1gBs). Describes K8SNIff, an approach for end-to-end encryption all the way to the pod.
- **concept** · [IPVS for Scaled Private Cloud Load Balancing [I] - Kimberly Messimer, Comcast VIPER](https://www.youtube.com/watch?v=KJ-A8LYriGI)

### 2017 · [KubeCon + CloudNativeCon North America 2017 (Austin)](../sources/PLj6h78yzYM2P-3-xqvmWaZbbI1sW-ulZb.md)

- **case study** · [The Mechanics of Deploying Envoy at Lyft - Matt Klein, Lyft](https://www.youtube.com/watch?v=IeJDjq-COjk) — Lyft
- **case study** · [Bottoms-Up Adoption of a Microservices Workflow Using Kubernetes & Envoy - Rafael Schloming](https://www.youtube.com/watch?v=GfrPVlRx5Gk)
- **case study** · [From Monolith to Microservices with Kubernetes and Linkerd - Mason Jones, Credit Karma](https://www.youtube.com/watch?v=PoGUI74TimM) — Credit Karma
- **concept** · [Istio: Weaving the Service Mesh [I] - Shriram Rajagopalan, IBM & Louis Ryan, Google](https://www.youtube.com/watch?v=WFEllbmRI8U)
- **concept** · [Microservices, Service Mesh, and CI/CD Pipelines: Making It All Work Together [I] - Brian Redmond](https://www.youtube.com/watch?v=UbLG_qUyCgM)
- **concept** · [Ask Your Proxy, It Knows Everything - Blake Mizerany, Backplane](https://www.youtube.com/watch?v=43wFJBRTHG0). Explores querying a proxy to learn about traffic and system behavior.
- **concept** · [The Service Mesh: Past, Present, and Future [B] - William Morgan, Buoyant](https://www.youtube.com/watch?v=2trOvMUuLkk). William Morgan traces the service mesh's past, present, and future.
- **concept** · [Microservices Patterns with NGINX Proxy in an Istio Services Mesh [I] - A.J. Hunyady, NGINX Inc](https://www.youtube.com/watch?v=hr-euazYG88)
- **concept** · [Securing Cluster Networking with Network Policies - Ahmet Balkan, Google](https://www.youtube.com/watch?v=3gGpMmYeEO8). Explains how to use Kubernetes Network Policies to secure cluster networking.
- **concept** · [The Easy--Don't Drive Yourself Crazy--Way to Kubernetes Networking [B] - Gerard Hickey](https://www.youtube.com/watch?v=H5Zl_kDOwBU)
- **concept** · [Istio: Sailing to a Secure Services Mesh [I] - Spike Curtis, Tigera & Dan Berg, IBM](https://www.youtube.com/watch?v=HMofcmTD444)
- **concept** · [Kubernetes Ingress Controller with Apache Traffic Server [I] - Mrunmayi Dhume, Oath (Yahoo)](https://www.youtube.com/watch?v=v_VMLkt4mTA)
- **concept** · [Linkerd Salon - Hosted by William Morgan, Buoyant](https://www.youtube.com/watch?v=wH9N8kbPbJ0)
- **concept** · [Setting Sail with Istio [B] - Lachlan Evenson, Microsoft](https://www.youtube.com/watch?v=wq1nlJNvy1w)
- **concept** · [Reliable Application Roll Out and Operations with Istio [B] - Lin Sun, IBM & Mandar Jog, Google](https://www.youtube.com/watch?v=8fbBnpCXP5k). Shows how to use Istio for reliable application rollouts and operations.
- **concept** · [Enable your Microservices with Advanced Resiliency and Fault Tolerance Leveraging Istio](https://www.youtube.com/watch?v=j0M3KFB1C1o)
- **concept** · [Istio’s Mixer: Policy Enforcement with Custom Adapters - Limin Wang, Google & Torin Sandall, Styra](https://www.youtube.com/watch?v=czZLXUqzd24)
- **concept** · [CNI, CRI, and OCI - Oh My! [I] - Elsie Phillips & Paul Burt, CoreOS](https://www.youtube.com/watch?v=1FEBOXpTI0M). Explains how the CNI, CRI and OCI standards relate and what each does in the container ecosystem.
- **panel** · [Panel: Ask Me Anything: Microservices and Service Mesh [B] - Moderated by Jason McGee, IBM](https://www.youtube.com/watch?v=22oL0j8mh9w). Moderated ask-me-anything panel on microservices and service mesh.

### 2018 · [KubeCon + CloudNativeCon China 2018 (Shanghai)](../sources/PLj6h78yzYM2OK087kzLgc4jTPVbZjuNfs.md)

- **case study** · [Experiences From Running Istio in a K8s Production Environment - Line Moseng & Johnny Horvi](https://www.youtube.com/watch?v=5qrR01n9JyY). Speakers share their experiences running Istio in a Kubernetes production environment.
- **case study** · [Istio in Production: Real Customers, Real Solutions - Craig Box, Google](https://www.youtube.com/watch?v=cV6JFq8XNZQ) — Google
- **case study** · [How HP Uses Istio to Manage Network Traffic - Xi He & Zhoujian Zhang, HP](https://www.youtube.com/watch?v=C5fi1gOdryg) — HP
- **concept** · [Extending Istio - Develop a New Mixer Adapter for Your Monitoring - Wen Tao Zhang & Yang Yang](https://www.youtube.com/watch?v=qqmY2WdKkgw)
- **concept** · [Modern Service Networking With Consul Connect, Envoy and Kubernetes - Nic Jackson, HashiCorp](https://www.youtube.com/watch?v=vt1Gk1jWfbc)
- **concept** · [Container Networking Untangling Services Meshes and SDNs - Gregory Elkinbard, GSE Software](https://www.youtube.com/watch?v=FxxHDHhMdGA)
- **concept** · [Comprehensive Performance Benchmark on Various Well-Known CNI Plugins - Giri Kuncoro & Vijay Dhama](https://www.youtube.com/watch?v=6DvLOXsHwd4). Benchmarks the performance of various well-known CNI plugins.
- **concept** · [Istio Certificate Management Through Vault - Lei Tang & Yonggang Liu, Google](https://www.youtube.com/watch?v=U4AJTEnUdkU)
- **concept** · [Network QoS Support for Kubernetes Applications - Jun Du, Huawei](https://www.youtube.com/watch?v=3A1FtjnUd7c). Presents design for network quality-of-service support for Kubernetes applications.
- **concept** · [Intro: CoreDNS - Yong Tang, Infoblox](https://www.youtube.com/watch?v=0VQzo6CWVCU). Introduces CoreDNS and its plugin-based design.
- **concept** · [Deep Dive: CoreDNS - Yong Tang, Infoblox](https://www.youtube.com/watch?v=Yj0cj2oymqY)
- **concept** · [Navigating the Service Mesh Ecosystem - George Miranda, Buoyant, Inc. & Diogenes Rittori, Pivotal](https://www.youtube.com/watch?v=FqorOTQsEGE)
- **concept** · [Handling Edge Cloud Network Using “KubeEdgeBus” - Yulin Sun & Weijin Xu, Huawei](https://www.youtube.com/watch?v=6R2T5Nvv72w). Presents KubeEdgeBus, a messaging approach for edge cloud networking in KubeEdge.
- **concept** · [Mesher: The Practice of a Production-Level Service Mesh - Xiaoliang Tian, Huawei](https://www.youtube.com/watch?v=K3qWoMoz2Mw)

### 2018 · [KubeCon + CloudNativeCon Europe 2018 (Copenhagen)](../sources/PLj6h78yzYM2N8GdbjmhVU65KYm_68qBmo.md)

- **case study** · [Introducing Envoy-Based Service Mesh at Booking.com - Ivan Kruglov, Booking.com](https://www.youtube.com/watch?v=Pus2ytdEfrQ) — Booking.com
- **case study** · [Evolving Systems Design: From Unreliable rpc to Resilience with Linkerd - Edward Wilde, Form3](https://www.youtube.com/watch?v=2EqkvPqk7JU) — Form3. Form3 describes how its systems design evolved from unreliable RPC to resilience using Linkerd.
- **case study** · [How We Built Contour, and What You Can Learn From Our Experience - Dave Cheney, Heptio](https://www.youtube.com/watch?v=4usXJE0EwHo) — Heptio. Heptio's Dave Cheney shares the experience and lessons from building the Contour ingress controller.
- **case study** · [Achieving High Security at Scale with Microservices - Zachary Arnold & Austin Adams](https://www.youtube.com/watch?v=1YCIOEW5nGw) — Zachary Arnold & Austin Adams' employer. Speakers describe how they achieved high security across a large microservices deployment in their own organization.
- **case study** · [Istio - The Weather Company's Journey - Nick Nellis & Fabio Oliveira, IBM (Any Skill Level)](https://www.youtube.com/watch?v=0fKi3NeCsSE) — The Weather Company, IBM. The Weather Company (IBM) shares its journey adopting Istio service mesh in production.
- **case study** · [From Kubelet to Istio: Kubernetes Network Security Demystified - Andrew Martin, ControlPlane](https://www.youtube.com/watch?v=Uocf67aD5QQ) — ControlPlane
- **concept** · [Low-Overhead Tracing Using eBPF for Observability into Kubernetes Apps and Services - Gaurav Gupta](https://www.youtube.com/watch?v=ug3lYZdN0Bk)
- **concept** · [Performance and Scale @ Istio Service Mesh - Fawad Khaliq, Laurent Demailly & Surya V Duggirala](https://www.youtube.com/watch?v=G4F5aRFEXnU)
- **concept** · [Building Hybrid Clouds with Istio - Allan Naim, Google & Rohit Agarwalla, Cisco](https://www.youtube.com/watch?v=bLJL53UIcqI)
- **concept** · [Replacing NGINX with Envoy in a Traffic Control System - Mark McBride, Turbine Labs, Inc](https://www.youtube.com/watch?v=MO_0bwcNEZY)
- **concept** · [The Untapped Power of Services - L7 Load Balancing Without a Service Mesh - Damien Lespiau](https://www.youtube.com/watch?v=PQnTBUr174M)
- **concept** · [Envoy Project Intro – Matt Klein & Jose Nino, Lyft (Any Skill Level)](https://www.youtube.com/watch?v=RUPgiHqUAZg)
- **concept** · [gRPC Load Balancing on Kubernetes - Jan Tattermusch, Google (Intermediate Skill Level)](https://www.youtube.com/watch?v=F2znfxn_5Hg)
- **concept** · [Cloud Native Networking for Containers in AWS using CNI Plugins - Anirudh Aithal](https://www.youtube.com/watch?v=tsc17ZuV5iU)
- **concept** · [The “Silk” Road: Building a CNI Plugin from Scratch - Usha Ramachandran & Angela Chin](https://www.youtube.com/watch?v=RdpDvpA--nw)
- **concept** · [Kubernetes and the CNI: Where We Are and What's Next - Casey Callendrello, CoreOS](https://www.youtube.com/watch?v=Vn6KYkNevBQ)
- **concept** · [Multicluster Ingress Powered by Kubernetes Cluster Registry - Greg Harmon & Nikhil Jindal](https://www.youtube.com/watch?v=nCON0U2dZ_w)
- **concept** · [Understand and Troubleshoot the “Magic” of Kubernetes Networking - Minhan Xia & Rohit Ramkumar](https://www.youtube.com/watch?v=knIJEzTd3kc)
- **concept** · [Lightning Talk: Istio by Example - Josef Adersberger, QAware (Beginner Skill Level)](https://www.youtube.com/watch?v=LYeAgVaJrm0)
- **concept** · [Extending Istio Service Mesh w/Envoy v2 APIs - Dmitri Chtchourov & Tim Swanson](https://www.youtube.com/watch?v=yq-c3H1Cd1A)
- **concept** · [CoreDNS Intro – Miek Gieben, Google (Any Skill Level)](https://www.youtube.com/watch?v=ZFEa2pDpvws)
- **concept** · [Observability and Debugging Cloud-Native Apps using Linkerd & Conduit - Franziska von der Goltz](https://www.youtube.com/watch?v=RC_9ywj0yz8)
- **concept** · [Envoy Internals Deep Dive - Matt Klein, Lyft (Advanced Skill Level)](https://www.youtube.com/watch?v=gQF23Vw0keg)
- **concept** · [GitOps for Istio - Manage Istio Config like Code - Varun Talwar & Alexis Richardson](https://www.youtube.com/watch?v=VkKMf23ZokY)
- **concept** · [How a Service Mesh Helped Us Build Production Cloud-Native Services - Israel Sotomayor](https://www.youtube.com/watch?v=VoYAtCVz3Ig)
- **concept** · [How to Get a Service Mesh Into Prod without Getting Fired - William Morgan, Buoyant, Inc](https://www.youtube.com/watch?v=XA1aGpYzpYg)
- **concept** · [Observing and Troubleshooting your Microservices with Istio - Isaiah Snell-feikema & Douglas Reid](https://www.youtube.com/watch?v=TSEqxsctXVc)
- **concept** · [Accelerating Envoy with the Linux Kernel - Thomas Graf, Covalent (Advanced Skill Level)](https://www.youtube.com/watch?v=ER9eIXL2_14)
- **concept** · [Istio Tells me my Service has Slow Response Time, Now What? - Endre Sara & Enlin Xu](https://www.youtube.com/watch?v=ZF-_LN9XYiQ)
- **concept** · [Canary Deploys with Kubernetes, Istio and Envoy - Jason Yee, Datadog (Beginner Skill Level)](https://www.youtube.com/watch?v=MGLDRKiXNf0)
- **concept** · [Envoy Project Intro – Matt Klein & Jose Nino, Lyft (Any Skill Level)](https://www.youtube.com/watch?v=WJBn5QZDnDo)
- **concept** · [Linkerd Deep Dive – George Miranda & Thomas Rampelberg (Intermediate Skill Level)](https://www.youtube.com/watch?v=j0Kosjecx70)
- **concept** · [Envoy Deep Dive – Matt Klein, Lyft (Intermediate Skill Level)](https://www.youtube.com/watch?v=odRR94jhNbU)
- **concept** · [Istio Multi-Cluster Mesh Expansion BOF - Sven Mawson, Google (Any Skill Level)](https://www.youtube.com/watch?v=_seY39zvgA4)
- **concept** · [CoreDNS Deep Dive – Miek Gieben, Google (Intermediate Skill Level)](https://www.youtube.com/watch?v=ZnW3k6m5AY8)
- **concept** · [Practical and Useful Latency Analysis using Istio and OpenCensus - Varun Talwar](https://www.youtube.com/watch?v=ME-EhOKqFOY)
- **concept** · [Linkerd Intro – Andrew Seigner, Buoyant.io, & George Miranda (Any Skill Level)](https://www.youtube.com/watch?v=cxrlgVJO5YE)
- **tutorial** · [Introduction to Istio Configuration - Joy Zhang, Google (Beginner Skill Level)](https://www.youtube.com/watch?v=x1Tyw8dFKjI)
- **tutorial** · [CNI Intro – Bryan Boreham, Weaveworks, & Casey Callendrello, CoreOS (Any Skill Level)](https://www.youtube.com/watch?v=7CeYAIlUY6s). Introductory session on the Container Network Interface and how CNI plugins work.
- **panel** · [Panel Discussion: Ask Us Anything: Microservices and Service Mesh - Moderated by Jason McGee](https://www.youtube.com/watch?v=uWi-Fe4Rzhg)

### 2018 · [KubeCon + CloudNativeCon North America 2018 (Seattle)](../sources/PLj6h78yzYM2PZf9eA7bhWnIh_mK1vyOfU.md)

- **case study** · [Lightning Talk: Optimizing Kubernetes Networking at Datadog - Laurent Bernaille, Datadog](https://www.youtube.com/watch?v=F7xDGtN6lB8) — Datadog
- **case study** · [Instrumenting and Scaling Cloud-Native Databases with Envoy - Daniel Hochman, Lyft](https://www.youtube.com/watch?v=1e2_Ljxe0Sg) — Lyft. Lyft shows how it uses Envoy to instrument and scale its cloud-native databases.
- **case study** · [The Telco Networking Journey to Cloud Native: The Good, Bad, and Ugly - Heather Kirksey](https://www.youtube.com/watch?v=BkH83WuO2KQ)
- **concept** · [Lightning Talk: CoreDNS Over gRPC: Reliable Service Discovery for Kubernetes - Yong Tang](https://www.youtube.com/watch?v=xd6T2ZEy6y4)
- **concept** · [Lightning Talk: PID Autoscaling Strava's Linkerd Service Mesh Using Prometheus Data - J Evans](https://www.youtube.com/watch?v=sOku2TMZC3k)
- **concept** · [Intro: Network Service Mesh BoF - Ed Warnick, Cisco & Frederick F. Kautz IV, Red Hat](https://www.youtube.com/watch?v=YeAKtUFaqQ0)
- **concept** · [Deep Dive: Envoy - Matt Klein & Constance Caramanolis, Lyft](https://www.youtube.com/watch?v=eQMTf1G7x8U)
- **concept** · [Intro: Envoy - Matt Klein & Constance Caramanolis, Lyft](https://www.youtube.com/watch?v=P719qI2h2yY)
- **concept** · [Linkerd 2.0, Now with Extra Prometheus - Andrew Seigner, Buoyant & Frederic Branczyk, CoreOS](https://www.youtube.com/watch?v=bnDWApsH36Y)
- **concept** · [Intro: CoreDNS - Yong Tang, MobileIron, Inc & Cricket Liu, Infoblox](https://www.youtube.com/watch?v=hopDaALR8uQ)
- **concept** · [Athenz with Istio: Single Access Control Model in Cloud Infrastructures - Tatsuya Yano](https://www.youtube.com/watch?v=jhutgE6NwsM)
- **concept** · [Securing Application Telemetry & Tracing with SPIFFE and Envoy - Sabree Blackmon, Docker](https://www.youtube.com/watch?v=_OzG4PHihSk)
- **concept** · [Deep Dive: Linkerd - Oliver Gould, Buoyant](https://www.youtube.com/watch?v=8EtH0ymXpvw). Deep dive into how the Linkerd service mesh is designed and works.
- **concept** · [Understanding CoreDNS in Kubernetes - John Belamaric, Google & Cricket Liu, Francois Tur, Infoblox](https://www.youtube.com/watch?v=qRiLmLACYSY)
- **concept** · [Implementing Least Privilege Security and Networking with BPF on Kubernetes - Arvind Soni, Covalent](https://www.youtube.com/watch?v=3F_XNbhjgxY). Shows how to implement least-privilege security and networking on Kubernetes with BPF.
- **concept** · [Navigating Workload Identity in Kubernetes - Michael Danese, Google & Spike Curtis, Tigera](https://www.youtube.com/watch?v=7N1PFdCEFE8). Explains approaches to giving Kubernetes workloads verifiable identity and how they compare.
- **concept** · [Deep Dive: CNI - Bryan Boreham, Weaveworks & Dan Williams, Red Hat](https://www.youtube.com/watch?v=VCrTDqfxuJM)
- **concept** · [eBPF Powered Distributed Kubernetes Performance Analysis - Lorenzo Fontana, InfluxData](https://www.youtube.com/watch?v=GkMltybVHkU)
- **concept** · [Deep Dive: Network Service Mesh BoF - Ed Warnicke, Cisco & Frederick F. Kautz IV, Red Hat](https://www.youtube.com/watch?v=SGi9LS870rk)
- **concept** · [Multi-Cloud Ingress LB: Gimbal Use Case in Actapio and Yahoo... - Hirotaka Ichikawa & Ryutaro Inoue](https://www.youtube.com/watch?v=It4RdxpAnEU)
- **concept** · [Istio - The Packet's-Eye View - Matt Turner, Tetrate](https://www.youtube.com/watch?v=zJnYuFsLHfY)
- **concept** · [Reducing Mean-Time-to-Detection of Incidents with an Envoy Service Mesh - Constance Caramanolis](https://www.youtube.com/watch?v=q_psmHeXaGI)
- **concept** · [Performance Testing Ingress for Internet-Scale Workloads - Alexander Brand, Heptio](https://www.youtube.com/watch?v=eeRDOL2m07M)
- **concept** · [Deep Dive: CoreDNS - Michael Grosser, Okkur Labs & John Belamaric, Google](https://www.youtube.com/watch?v=LIoC6aC--jQ)
- **concept** · [Is Istio the Most Next Gen Next Gen Firewall Ever Created? - John Morello, Twistlock](https://www.youtube.com/watch?v=H4wkdwlL8ZA)
- **concept** · [Game Server Networking with Envoy - Christopher M Luciano, IBM](https://www.youtube.com/watch?v=tSQDOYozl1E)
- **concept** · [Switching the Engine (DNS) in Kubernetes: Benchmarks ... - Michael Grosser & Jake Sanders](https://www.youtube.com/watch?v=Il-yzqBrUdo)
- **concept** · [Intro: Linkerd – William Morgan, Buoyant with William King & Ivan Sim & Sebastian Tiedtke](https://www.youtube.com/watch?v=5kktb9rsNts). Introduction to the Linkerd service mesh project and its design.
- **concept** · [Evolution of Integration and Microservices with Service Mesh and Ballerina - Christian Posta](https://www.youtube.com/watch?v=rRrJKM0BAAo)
- **tutorial** · [Tutorial: Using Istio - Lee Calcote & Girish Ranganathan, SolarWinds](https://www.youtube.com/watch?v=jlHLZqS7Vek)
- **tutorial** · [Container Networking From Scratch - Kristen Jacobs, Oracle](https://www.youtube.com/watch?v=6v_BDHIgOY8). Builds container networking from scratch to explain how it works.
- **panel** · [Panel Discussion: Ask Us Anything: Microservices and Service Mesh – Moderated by Jason McGee](https://www.youtube.com/watch?v=cqAj28nyr9E)

### 2019 · [KubeCon + CloudNativeCon China 2019 (Shanghai)](../sources/PLj6h78yzYM2Njj5PvNc4Mtcril2YyR95d.md)

- **case study** · [Lightning Talk: How We Use Istio and OPA for Authorization - Lin Tao, HP](https://www.youtube.com/watch?v=ctr2bVmzGpk) — HP
- **case study** · [Open Source Networking Technology in Inspur Cloud - Yanjun Li, Inspur](https://www.youtube.com/watch?v=9FqYPlndf78) — Inspur. Inspur describes using open source networking technology in its own cloud.
- **concept** · [Intro: Network Service Mesh (NSM) - Frederick Kautz, Doc.ai & Nikolay Nikolaev, VMware](https://www.youtube.com/watch?v=4kHu9Nq-41o). Introduces Network Service Mesh and its approach to Kubernetes networking.
- **concept** · [Intro + Deep Dive: CoreDNS - Yong Tang, MobileIron](https://www.youtube.com/watch?v=tMseoUn_inE)
- **concept** · [Observability in Service Mesh Powered by Envoy and Apache SkyWalking - Sheng Wu & Lizan Zhou](https://www.youtube.com/watch?v=tERm39ju9ew)
- **concept** · [Intro: Envoy - Lizan Zhou, Tetrate](https://www.youtube.com/watch?v=4dPL756cJj4). Introduction to the Envoy proxy project.
- **concept** · [How SPIFFE Helps Istio in Service Mesh Federation - Yonggang Liu & Wencheng Lu, Google](https://www.youtube.com/watch?v=SCBksDnA2rU)
- **concept** · [Istio Performance and Best Practices in Large Scale... Guang Ya Liu & Chun Lin Yang](https://www.youtube.com/watch?v=wzQtNaE15KI)
- **concept** · [Cloud Native Load Balancing From Scratch - Fangyuan Li, VMware](https://www.youtube.com/watch?v=48gg58FyxDg). Builds a cloud native load balancer from scratch.
- **concept** · [Running Resilient Workloads with Istio - Matt Turner, Tetrate](https://www.youtube.com/watch?v=_nBZQS4bPbQ)
- **concept** · [Upgrading Your Service Mesh to Linkerd 2 - Tilen Faganel, Open Credo ltd.](https://www.youtube.com/watch?v=DnEdeSbq5s4)
- **concept** · [Using Istio to Manage the Cross-Regional & Cross-Cluster... Xi Ning Wang & Xiaozhong Liu](https://www.youtube.com/watch?v=OCWqpv0IzaE)
- **concept** · [Enhancing Envoy: Certificate Handling at the Edge - Brian Redbeard & Bill Decoste, Red Hat](https://www.youtube.com/watch?v=oCl6h_XB2gs)
- **concept** · [Network Observability with Envoy - Nic Jackson, HashiCorp](https://www.youtube.com/watch?v=usSyncnsl4A)
- **concept** · [Efficient and Flexible Virtual Machine Networking Through eBPF - Jason Wang, Red Hat](https://www.youtube.com/watch?v=DWY_zIkob6o)
- **concept** · [Debugging with eBPF on Arm Platforms - Leo Yan, Linaro](https://www.youtube.com/watch?v=y3p4i8zXbns)
- **concept** · [IngressRoute: A Path Towards a Better Ingress Object for Kubernetes - David Cheney, VMware](https://www.youtube.com/watch?v=PvqmL5MygaM)
- **concept** · [AIOps: Anomaly Detection with Prometheus and Istio - Marcel Hild, Red Hat](https://www.youtube.com/watch?v=D09x0eR4vu4)
- **concept** · [Manage Multi-tenant ML Workloads Using Istio - Wencheng Lu & Limin Wang, Google](https://www.youtube.com/watch?v=_5HoYiKeQbk)

### 2019 · [KubeCon + CloudNativeCon Europe 2019 (Barcelona)](../sources/PLj6h78yzYM2PpmMAnvpvsnR4c27wJePh3.md)

- **case study** · [JustFootball’s Journey to gRPC + Linkerd in Production - Ben Lambert, & Kevin Lingerfelt](https://www.youtube.com/watch?v=AxPfa7Mp_WY)
- **case study** · [5 Simple Steps To Simplifying Your Compliance Journey With a Service Mesh – Granville Schmidt](https://www.youtube.com/watch?v=BGqWrdfZEMM)
- **case study** · [Istio on Knative Lessons Learned: How Istio is Fit for Serverless Platform - Ying Chun Guo](https://www.youtube.com/watch?v=DN7chnOM0g0)
- **case study** · [Scaling Edge Operations at Onefootball with Ambassador: From 0 to 6000 rps - Jonathan Juares Beber](https://www.youtube.com/watch?v=07RvO4AChHE) — Onefootball. Onefootball scaled its edge operations with Ambassador from zero to 6000 requests per second.
- **case study** · [Kubernetes Networking at Scale - Laurent Bernaille, Datadog & Bowei Du, Google](https://www.youtube.com/watch?v=MvoImel5qfc) — Datadog, Google
- **concept** · [Lightning Talk: Using Istio's Mixer for Network Request Caching - Zach Arnold, Ygrene Energy Fund](https://www.youtube.com/watch?v=x1SomOy431I)
- **concept** · [Lightning Talk: Back to the Future with eBPF - Beatriz Martínez Rubio, IBM](https://www.youtube.com/watch?v=AQNz_16CaiI). Lightning talk looking at eBPF and how it connects past and future technologies.
- **concept** · [Istio, We Have a Problem! Understanding and Fixing Bugs with a Service-Mesh - David Gageot, Google](https://www.youtube.com/watch?v=9CQ0PMiOGhg). Shows techniques for understanding and fixing bugs using a service mesh like Istio.
- **concept** · [Intro: Network Service Mesh (NSM) - Frederick Kautz, Doc.ai & Ed Warnicke, Cisco](https://www.youtube.com/watch?v=eLTjXdtlMzA)
- **concept** · [Using eBPF to Bring Kubernetes-Aware Security to the Linux Kernel - Dan Wendlandt, Isovalent](https://www.youtube.com/watch?v=7PXQB-1U380). Describes using eBPF to give the Linux kernel Kubernetes-aware security enforcement.
- **concept** · [Envoy SDS: Fortifying Istio Security - Yonggang Liu & Quanjie Lin, Google](https://www.youtube.com/watch?v=QlQyqCaTOh0)
- **concept** · [Intro: Linkerd - William Morgan, Buoyant](https://www.youtube.com/watch?v=Z3nfLI3z0hc)
- **concept** · [Istio New Workload Identity Provision Pipeline Based on Envoy SDS - Quanjie Lin & Diem Vu, Google](https://www.youtube.com/watch?v=NiiZOszksGU)
- **concept** · [What WePay Learned From Processing Billions of Dollars on GKE Using Linkerd - Mohsen Rezaei, WePay](https://www.youtube.com/watch?v=ph_NqGNHdhM)
- **concept** · [Extending Envoy with WebAssembly - John Plevyak & Dhi Aurrahman, Tetrate](https://www.youtube.com/watch?v=XdWmm_mtVXI)
- **concept** · [Intro: CoreDNS - Daniel Garcia, Infoblox & Michael Grosser, Okkur Labs](https://www.youtube.com/watch?v=erfYbXzQ05k)
- **concept** · [Democratizing Service Mesh on Kubernetes - Gabe Monroy, Microsoft & CNCF Board Member](https://www.youtube.com/watch?v=gDLD8gyd7J8)
- **concept** · [Istio Multi-Cluster Service Mesh Patterns Explained - Daniel Berg & Ram Vennam, IBM](https://www.youtube.com/watch?v=-zsThiLvYos). Explains Istio multi-cluster service mesh deployment patterns.
- **concept** · [Intro: Envoy - Lizan Zhou, Tetrate](https://www.youtube.com/watch?v=vsGFiOHoMYk)
- **concept** · [Zero Trust Service Mesh with Calico, SPIRE, and Envoy - Shaun Crampton & Evan Gilman](https://www.youtube.com/watch?v=rKOEYoINdOE)
- **concept** · [Building an Edge Control Plane with Kubernetes and Envoy - Flynn, Datawire](https://www.youtube.com/watch?v=aFbxDWteQl8)
- **concept** · [Deep Dive: CoreDNS - Yong Tang, MobileIron & John Belamaric, Google](https://www.youtube.com/watch?v=yHXGtFTOQmY)
- **concept** · [Benefits of a Service Mesh When Integrating Kubernetes with Legacy Services - Stephan Fudeus](https://www.youtube.com/watch?v=vQ2IktsMlgQ)
- **concept** · [Co-Evolution of Kubernetes and GCP Networking - Purvi Desai & Tim Hockin, Google](https://www.youtube.com/watch?v=eBKouNho5t4)
- **concept** · [gRPC load balancing and Service Mesh - Vishal Powar, Google](https://www.youtube.com/watch?v=FuXnfGHUZcU)
- **concept** · [Reinventing Networking: A Deep Dive into Istio's Multicluster Gateways - Steve Dake, Independent](https://www.youtube.com/watch?v=-t2BfT59zJA). A deep dive into how Istio's multicluster gateways work and how they reshape networking.
- **concept** · [Deep Dive: Network Service Mesh (NSM) - Nikolay Nikolaev, VMware & Frederick Kautz, Doc.ai](https://www.youtube.com/watch?v=AWHkn_dqAUA). Deep dive into the architecture of Network Service Mesh.
- **concept** · [Cross-Cluster Calls Made Easy with Istio 1.1 - Matt Turner, Tetrate](https://www.youtube.com/watch?v=FiMSr-fOFKU)
- **concept** · [Networking the Service Mesh Proxy: Where We Are, Where We’re Going - Tim Swanson & John Joyce, Cisco](https://www.youtube.com/watch?v=rUB-IBZcBwY)
- **concept** · [Deep Dive: Linkerd - Oliver Gould, Buoyant](https://www.youtube.com/watch?v=E-zuggDfv0A)
- **concept** · [Deep Dive: Envoy - Lizan Zhou, Tetrate](https://www.youtube.com/watch?v=spzfupads2o)
- **concept** · [High Performance Networking with Kubevirt - Doug Smith, Red Hat & Abdul Halim, Intel](https://www.youtube.com/watch?v=dhQ51C4F8WE)
- **concept** · [Unblocking the Release Train with Istio Traffic Management - Dave Shepherd & Pierre Meunier](https://www.youtube.com/watch?v=jJdhec4Yufo)
- **concept** · [Autoscaling Multi-Cluster Observability with Thanos and Linkerd - Andrew Seigner & Frederic Branczyk](https://www.youtube.com/watch?v=qTxunwzYO0g)
- **concept** · [Kubernetes Networking: How to Write a CNI Plugin From Scratch - Eran Yanay, Twistlock](https://www.youtube.com/watch?v=zmYxdtFzK6s)
- **concept** · [Ingress V2 and Multicluster Services - Rohit Ramkumar & Bowei Du, Google](https://www.youtube.com/watch?v=Ne9UJL6irXY)
- **concept** · [Transparent Chaos Testing with Envoy , Cilium and BPF - Thomas Graf, Isovalent](https://www.youtube.com/watch?v=gPvl2NDIWzY)
- **concept** · [Network Flow Monitoring in Kubernetes with Contiv/VPP CNI and Elastic Stack - Rastislav Szabo](https://www.youtube.com/watch?v=GYee7igCmDs)
- **panel** · [Panel Discussion: Ask Us Anything: Microservices and Service Mesh](https://www.youtube.com/watch?v=101xw1RN3t4). Ask-us-anything panel on microservices and service mesh.

### 2019 · [KubeCon + CloudNativeCon North America 2019 (San Diego)](../sources/PLj6h78yzYM2NDs-iu8WU5fMxINxHXlien.md)

- **case study** · [Running Istio and Kubernetes On-prem at Yahoo Scale - Suresh Visvanathan & Mrunmayi Dhume, Verizon](https://www.youtube.com/watch?v=fEaVU1i-fOQ) — Yahoo, Verizon
- **case study** · [Envoy on Fire: A Practical Look at Debugging a Service Mesh - Lita Cho & Ryan Cox, Lyft](https://www.youtube.com/watch?v=6jnzo8QXyDk) — Lyft. Lyft shares how it debugs Envoy and its service mesh in production.
- **case study** · [How Yelp Moved Security From the App to the Mesh with Envoy and OPA - Daniel Popescu & Ben Plotnick](https://www.youtube.com/watch?v=Z6aN3Smt-9M) — Yelp
- **case study** · [From Brownfield to Greenfield: Istio Service Mesh Journey at Fred... Shriram Rajagopalan & Lixun Qi](https://www.youtube.com/watch?v=Rako7zKXquU) — Fred...
- **case study** · [There's a Bug in My Service Mesh! What Do You Do When the Mesh is At Fault? - Ana Calin & Risha Mars](https://www.youtube.com/watch?v=n24jPIty-pg) — Fault
- **case study** · [Cruise’s Self-Driving Networking Journey - Bernard Van De Walle & Jon Yucel, Cruise](https://www.youtube.com/watch?v=EaCUFOehNnY) — Cruise
- **case study** · [How Spotify Migrated Ingress HTTP Systems to Envoy - Erica Manno & Vladimir Shakhov, Spotify](https://www.youtube.com/watch?v=I_oa8l0j-yM) — Spotify
- **concept** · [Lightning Talk: Is Your Kubernetes Cluster's DNS Working? - Jonathan Perry, Flowmill](https://www.youtube.com/watch?v=thBCB7YeZ2g)
- **concept** · [Porting Envoy to Windows; A Progress Report - Yechiel Kalmenson & William A. Rowe, Jr., Pivotal](https://www.youtube.com/watch?v=FGBBeyZ-p1k)
- **concept** · [Enforcing Automatic mTLS With Linkerd and OPA Gatekeeper - Ivan Sim, Buoyant & Rita Zhang, Microsoft](https://www.youtube.com/watch?v=gMaGVHnvNfs)
- **concept** · [Rethinking the K8s DNS for the Modern Enterprise - Deepa Kalani & Venil Noronha, VMware](https://www.youtube.com/watch?v=fLx78pSYFvw)
- **concept** · [Understanding and Troubleshooting the eBPF Datapath in Cilium - Nathan Sweet, DigitalOcean](https://www.youtube.com/watch?v=Kmm8Hl57WDU)
- **concept** · [Intro to gRPC - Jayant Kolhe & Eric Anderson, Google](https://www.youtube.com/watch?v=3Kkj6vAW5a4). Introduces gRPC, covering its design and how to use it.
- **concept** · [Intro: Linkerd - William Morgan, Buoyant](https://www.youtube.com/watch?v=guHZ7U7ZoWc)
- **concept** · [How the Department of Defense Moved to Kubernetes and Istio - Nicolas Chaillan](https://www.youtube.com/watch?v=YjZ4AZ7hRM0)
- **concept** · [Service Mesh: There and Back Again - Hema Lee & Cody Vandermyn, Nordstrom](https://www.youtube.com/watch?v=sq8nsjuJqO4)
- **concept** · [Supercharge Your Microservices CI/CD with Service Mesh and Kubernetes - Brian Redmond, Microsoft](https://www.youtube.com/watch?v=SMoaem3UBag)
- **concept** · [Evolving the Kubernetes Ingress APIs to GA and Beyond - Christopher M Luciano, IBM & Bowei Du](https://www.youtube.com/watch?v=cduG0FrjdJA)
- **concept** · [Life Outside the Cluster: Adding Virtual Machines to an Envoy Servic... Megan O'Keefe & Ameer Abbas,](https://www.youtube.com/watch?v=0B8maYcjq_c). Shows how to add virtual machines to an Envoy-based service mesh.
- **concept** · [Liberating Kubernetes From Kube-proxy and Iptables - Martynas Pumputis, Cilium](https://www.youtube.com/watch?v=bIRwSIwNHC0)
- **concept** · [Advanced Model Inferencing Leveraging KNative, Istio & Kubeflow Serving - Animesh Singh & Clive Cox](https://www.youtube.com/watch?v=YaGASyU88dQ)
- **concept** · [Deep Dive: CNI - Bryan Boreham, Weaveworks & Dan Williams, Red Hat](https://www.youtube.com/watch?v=zChkx-AB5Xc)
- **concept** · [CoreDNS Deep Dive - John Belamaric, Google](https://www.youtube.com/watch?v=VfobOJ91A5Y)
- **concept** · [Take Envoy Beyond a K8s Service Mesh - to Legacy Bare Metal & VMs + More - Steve Sloka & Steven Wong](https://www.youtube.com/watch?v=jzla7xdqtwM)
- **concept** · [Five Cool Things You Can Do with Network Service ... Ed Warnicke, Nikolay Nikolaev & Frederick Kautz](https://www.youtube.com/watch?v=-SeHk0qJMBs). Demonstrates five things you can do with Network Service Mesh.
- **concept** · [Enforcing Service Mesh Structure using OPA Gatekeeper - Sandeep Parikh, Google](https://www.youtube.com/watch?v=90RHTBinAFU). Shows how to enforce service mesh structure and configuration with OPA Gatekeeper.
- **concept** · [Walk-through: Debugging an RBAC Problem in Istio (But Without the Swearing) - Matt Turner](https://www.youtube.com/watch?v=Rc_MM99wbYo)
- **concept** · [Networking Optimizations for Multi-Node Deep Learning on Kubernetes - Rajat Chopra & Erez Cohen](https://www.youtube.com/watch?v=CL71kbZ72iU)
- **concept** · [Networking Optimizations for Multi-Node Deep Learning on Kubernetes - Rajat Chopra & Erez Cohen](https://www.youtube.com/watch?v=UIyLFDHNgFc)
- **concept** · [CoreDNS: Beyond the Basics - Cricket Liu, Infoblox & John Belamaric, Google](https://www.youtube.com/watch?v=ym1uWYzxpEE)
- **concept** · [Building a Dev/Test Loop for a Kubernetes Edge Gateway with Envoy Proxy - Flynn, Datawire](https://www.youtube.com/watch?v=_HTIEcOm3SA)
- **concept** · [Bringing the Envoy Service Mesh to Mobile - Jose Nino & Michael Schore, Lyft](https://www.youtube.com/watch?v=NYb_nVWkP-I)
- **concept** · [Envoy Overview and Maintainer Q&A - Harvey Tuch; Lizan Zhou; Stephan Zuercher & Snow Pettersen](https://www.youtube.com/watch?v=tlj-rjyHG4A)
- **concept** · [How Container Networking Affects Database Performance - Tyler Duzan & Vadim Tkachenko, Percona](https://www.youtube.com/watch?v=EXqEzZPm4I0)
- **concept** · [Stitching a Service Mesh Across Hundreds of Discrete Networks - Jason Webb & Anil Attuluri, Intuit](https://www.youtube.com/watch?v=EWyNbBn1vns)
- **concept** · [Low Latency Multi-cluster Kubernetes Networking in AWS - Paul Fisher, Lyft](https://www.youtube.com/watch?v=Mj5zgbC6YDI)
- **concept** · [Deep Dive: Linkerd - Oliver Gould, Buoyant](https://www.youtube.com/watch?v=NqjRqe0J98U)
- **concept** · [OpenFaaS Cloud + Linkerd: A Secure, Multi-Tenant Serverless Platform - Charles Pretzer & Alex Ellis](https://www.youtube.com/watch?v=sD7hCwq3Gw0)
- **tutorial** · [Service Discovery With Hybrid and Multi-Cloud: Introduction to CoreDNS - Yong Tang, MobileIron](https://www.youtube.com/watch?v=vvVmx0EDdkw)
- **tutorial** · [Introduction to CNI, the Container Network Interface Project - Bryan Boreham & Dan Williams](https://www.youtube.com/watch?v=YjjrQiJOyME)
- **tutorial** · [Tutorial: Service Mesh for the Developer Workflow - Christian Posta & Nic Jackson](https://www.youtube.com/watch?v=uC2O36QKUlc)
- **panel** · [Panel: Is Service Mesh Ready for Edge-Native Applications?](https://www.youtube.com/watch?v=H1osUImcvrQ)

### 2020 · [KubeCon + CloudNativeCon Europe 2020 - Virtual](../sources/PLj6h78yzYM2O1wlsM-Ma-RYhfT5LKq0XC.md)

- **case study** · [Booting 5 K8s Clusters on Every Git Push: How Linkerd Leveled Up Its CI - Andrew Seigner, Buoyant](https://www.youtube.com/watch?v=2MkqFCXtZfI) — Buoyant. Buoyant explains how Linkerd's CI now boots five Kubernetes clusters on every git push.
- **case study** · [Migrating Transactions Worth Billions of $ to Service Mesh With N... Mahendra Kariya & Shishir Joshi](https://www.youtube.com/watch?v=OY0CxiKbX2o)
- **case study** · [Multi-cluster Made Reasonable: Envoy Service Mesh Control Plane - Ashley Kasim & Paul Fisher, Lyft](https://www.youtube.com/watch?v=7aMgS1uRU5s) — Lyft. Lyft describes the Envoy-based control plane it built to run its service mesh across multiple clusters.
- **concept** · [Making Envoy Contributions Feasible for Everyone - Yaroslav Skopets, Tetrate.io](https://www.youtube.com/watch?v=mJAYHHKmLhU)
- **concept** · [Hacking on Network Service Mesh Dataplane for a True Multi-c... Aleksandra Kowalska & Jaroslaw Lukow](https://www.youtube.com/watch?v=zzDAAMC7214)
- **concept** · [Envoy, Take the Wheel: Real-time Adaptive Circuit Breaking - Tony Allen, Lyft](https://www.youtube.com/watch?v=CQvmSXlnyeQ)
- **concept** · [Building the Cloud Native Telco with Network Service Mesh - Ivana Atanasova & Radoslav Dimitrov](https://www.youtube.com/watch?v=zPKCZxHrERU)
- **concept** · [Kubernetes DNS Horror Stories (And How to Avoid Them) - Laurent Bernaille, Datadog](https://www.youtube.com/watch?v=Yq-SVNa_W5E)
- **concept** · [Deep Dive: Linkerd - Zahari Dichev, Buoyant](https://www.youtube.com/watch?v=GJVzSqYrflc)
- **concept** · [Designing a gRPC Interface for Kernel Tracing with eBPF - Leonardo Di Donato, Sysdig](https://www.youtube.com/watch?v=kjOJfNDPVSo)
- **concept** · [eBPF and Kubernetes: Little Helper Minions for Scaling Microservices - Daniel Borkmann, Cilium](https://www.youtube.com/watch?v=99jUcLt3rSk). Explains how eBPF and Cilium help scale Kubernetes microservices networking.
- **concept** · [Multicloud Vitess over Network Service Mesh - Tim Swanson, Cisco & John Watson, PlanetScale](https://www.youtube.com/watch?v=NulLc7DxXg8)
- **concept** · [Ingress on the Rails: Use Community Tools to Automate Ingress Provisioning - Alastair Firth, Camunda](https://www.youtube.com/watch?v=Y7-X-htiVw0)
- **concept** · [Deep-Dive: Packet-level Debugging of Bridged and Non-bridged CNI Plugins - Jay Vyas & Sedef Savas](https://www.youtube.com/watch?v=RQNy1PHd5_A)
- **concept** · [The Past, Present, and Future of Cloud Native API Gateways - Daniel Bryant, Datawire](https://www.youtube.com/watch?v=1mBp8uxImO8). Traces the history, current state and future of cloud native API gateways.
- **concept** · [Service Mesh and Serverless Chatbots with Linkerd, K8s and OpenFaas - Sergio Méndez](https://www.youtube.com/watch?v=bNoeI_Wi-R0)
- **concept** · [What You Didn’t Know About Ingress Controllers’ Performance - Mikko Ylinen & Ismo Puustinen, Intel](https://www.youtube.com/watch?v=6Dqon7Fs7kg). Examines the performance characteristics of ingress controllers.
- **concept** · [Scaling Kubernetes Networking Beyond 100k Endpoints - Rob Scott & Minhan Xia, Google](https://www.youtube.com/watch?v=a6SfbeM06Qo)
- **concept** · [Episode IV: A New Network Service Mesh - Frederick Kautz, Doc.ai & Nikolay Nikolaev, VMware](https://www.youtube.com/watch?v=STxfzYMwIEs)
- **concept** · [CoreDNS for Hybrid and Multi-cloud - Yong Tang, MobileIron](https://www.youtube.com/watch?v=7ZQgIECUEwg). Explains using CoreDNS for DNS across hybrid and multi-cloud environments.
- **concept** · [Automating Load Balancing and Fault Tolerance via Predictive Analysis - Steven Rosenberg, Red Hat](https://www.youtube.com/watch?v=RgksePRWr6k)
- **concept** · [Deep Dive: CNI - Bryan Boreham, Weaveworks & Bruce Ma, Ant Financial](https://www.youtube.com/watch?v=0tbnXX7jXdg). A deep dive into the Container Network Interface specification and how it works.
- **concept** · [Building a Distributed API Gateway with a Service Mesh - Rei Shimizu & Cynthia Coan](https://www.youtube.com/watch?v=YeK34lItg2Q)
- **concept** · [Mutual TLS Adoption Made Simple, Safe and Secure - Lizan Zhou, Tetrate & Jianfei Hu, Google](../sources/videos/-20SUP6IWUs.md). Maintainers explain why mutual TLS is hard to adopt and how Istio API improvements make adoption simpler and safer.
- **concept** · [Intro: Linkerd - William Morgan, Buoyant](https://www.youtube.com/watch?v=PxRAis8afAU)
- **concept** · [Sponsor Demo: HAProxy Technologies - Benchmarking 5 Popular Ingress Controllers](https://www.youtube.com/watch?v=cv14e6OQQ6E)
- **concept** · [Hubble - eBPF Based Observability for Kubernetes - Sebastian Wicki, Isovalent](https://www.youtube.com/watch?v=8WCbGSCyDSo). Introduces Hubble, eBPF-based observability for Kubernetes.
- **concept** · [Kubernetes Networking Intro and Deep-Dive - Bowei Du & Tim Hockin, Google](https://www.youtube.com/watch?v=tq9ng_Nz9j8)
- **concept** · [Network Service Mesh to Address Cloud Native 5G Telco Networking... Roshini Ratnam & Anders Franzen](https://www.youtube.com/watch?v=uV-GtLv2AJc)
- **concept** · [Mesh in a Mesh: A Model for Stronger Multi-tenancy of Kubernetes Wo... Nitish Malhotra & Akash Baid](https://www.youtube.com/watch?v=7XMgtfey5YI). Proposes a mesh-in-a-mesh model for stronger multi-tenancy of Kubernetes workloads.
- **tutorial** · [Tutorial: Communication Is Key - Understanding Kubernetes Networking - Jeff Poole, Vivint Smart Home](https://www.youtube.com/watch?v=InZVNuKY5GY)
- **tutorial** · [BoF: Introduction to Contour, A High Performance Multitenant Ingress... Michael Michael & Nick Young](https://www.youtube.com/watch?v=MK6BoBoj-Zg)
- **tutorial** · [Introduction to CNI, the Container Network Interface Project - Casey Callendrello & Bryan Boreham](https://www.youtube.com/watch?v=YWXucnygGmY)
- **panel** · [Panel: Ask Me Anything About Service Mesh](https://www.youtube.com/watch?v=3BOfbgbHDY0). A panel taking audience questions about service mesh.

### 2020 · [KubeCon + CloudNativeCon North America 2020 - Virtual](../sources/PLj6h78yzYM2Pn8RxfLh2qrXBDftr6Qjut.md)

- **case study** · [How H-E-B Curbside Adopted Linkerd During a Pandemic - Justin Turner & Garrett Griffin, H-E-B](https://www.youtube.com/watch?v=DN-HPeqXnlo) — H-E-B
- **case study** · [High Performance Networking for Distributed DL Training in Production K8s - Nivedita Viswanath](https://www.youtube.com/watch?v=GjqpXpah5NE)
- **concept** · [Taking Envoy Beyond C++ with WebAssembly - Idit Levine & Yuval Kohavi, Solo.io](https://www.youtube.com/watch?v=qZqN9PYzxPY)
- **concept** · [Scalable and Multitenant Networking in XDP and Kubernetes Operators - Sherif Abdelwahab & Ying Xiong](https://www.youtube.com/watch?v=gptklnLaqMA)
- **concept** · [Inside Kubernetes Ingress - Dominik Tornow, Cisco](https://www.youtube.com/watch?v=2fZrnx2FRMs). Deep dive into how Kubernetes Ingress works internally.
- **concept** · [Extending Service Mesh to the Edge - Stephen Wong, OPNFV Clover](https://www.youtube.com/watch?v=OHDKH6z22Dw)
- **concept** · [Enhancing K8s Networking with SmartNICs - Dave Cremins, Intel](https://www.youtube.com/watch?v=mJ3nM4lKTO4)
- **concept** · [Proxyless Service Mesh with gRPC - Menghan Li, Google](https://www.youtube.com/watch?v=MZzzbUQ_NiQ)
- **concept** · [Overview and State of Linkerd - William Morgan & Tarun Pothulapati, Buoyant, Inc.](https://www.youtube.com/watch?v=9XlEIURv_3M). Overview and state of the Linkerd project, with recent changes.
- **concept** · [Multi-Cluster is Easier Than You Think with Linkerd and Ambassador - Thomas Rampelberg, Buoyant](https://www.youtube.com/watch?v=pf_Io5qnPWk)
- **concept** · [Kubernetes SIG-Network: Intro and Deep-Dive - Tim Hockin & Bowei Du, Google & Rich Renner](https://www.youtube.com/watch?v=3w-AX4OIdwg). Intro and deep dive into Kubernetes SIG-Network and its current work.
- **concept** · [Service Discovery with CoreDNS Plugins in Golang - Yong Tang, Mobileiron & John Belamaric, Google](https://www.youtube.com/watch?v=PtG0xlh5eSs)
- **concept** · [Safely Deploying a 100K line Envoy YAML Configuration to Production - Lisa Lu & Jyoti Mahapatra](https://www.youtube.com/watch?v=FvT86JaQkcc)
- **concept** · [All You Can Eat Networking. Kubernetes Goodness for the Hungriest Workloads - Aloys Augustin](https://www.youtube.com/watch?v=tPnqFx32rW4)
- **concept** · [Service Mesh Specifications and Why They Matter in Your Deployment - Lee Calcote & Kush Trivedi](https://www.youtube.com/watch?v=4XvtQdjWxUQ). Explains service mesh specifications and why they matter for deployments.
- **concept** · [Empowering Cloud Native Networking with Arm Ecosystem - Trevor Tao & HanYu Ding, Arm](https://www.youtube.com/watch?v=gTE-je4aIRI)
- **concept** · [Contour, A High Performance Multitenant Ingress Controller for Kubernetes - Michael Michael](https://www.youtube.com/watch?v=2Gcf3Rs6q4o). Explains how Contour provides a high-performance multitenant ingress controller for Kubernetes.
- **concept** · [Cloud Native & SD-WAN: Improving K8s Application Experience Over SD-WAN - Alberto Rodriguez-Natal](https://www.youtube.com/watch?v=-sWVNFk6tCo). Explains how to improve Kubernetes application experience over SD-WAN networks.
- **concept** · [Build Your Own Envoy Control Plane - Steve Sloka, VMware](https://www.youtube.com/watch?v=qAuq4cKEG_E)
- **concept** · [Envoy Q&A - Matt Klein, Lyft & Harvey Tuch, Google](https://www.youtube.com/watch?v=RT3qYMG8mxU)
- **panel** · [Panel: Tales from the Edge: Is the Edge More Important Than the Service Mesh? - Matt Klein](https://www.youtube.com/watch?v=YD5UHbNTud4)

### 2021 · [KubeCon + CloudNativeCon + Open Source Summit China 2021](../sources/PLj6h78yzYM2PjmJ9A98QCXnMsmONhU--t.md)

- **case study** · [Online Video upgrades resilience from SC Circuit Breaker to Service Mesh - Xu Shiyu & Zhang Chaomeng](https://www.youtube.com/watch?v=K16sFwAjwus)
- **case study** · [Envoy Mesh Acceleration: From Iptables to Fully BPF - Xiyao Zhang & Xu Liu, Tencent](https://www.youtube.com/watch?v=tzNh1CXXY-0) — Tencent
- **case study** · [Creating a Unified Network Plane across Kubernetes with Kube-OVN - Cheng Chen, PingCAP](https://www.youtube.com/watch?v=2x_O-IYr-uY) — PingCAP. PingCAP shows how it created a unified network plane across Kubernetes clusters using Kube-OVN.
- **case study** · [Best Practice: DNS Failure Observability and Diagnosis in Kubernetes - Yuning Xie, Alibaba](https://www.youtube.com/watch?v=1EjLM_GCWKU) — Alibaba. Alibaba shares its best practices for observing and diagnosing DNS failures in its Kubernetes clusters.
- **concept** · [Zero Trust Network Turnkey Solution to Support Zero Trust Service Mesh - Hongjun Ni & Pan Zhang](https://www.youtube.com/watch?v=f52CA__zm7s)
- **concept** · [Solving the Service Mesh Adopter’s Dilemma - Anita Ihuman, Layer5](https://www.youtube.com/watch?v=7RIvUS3aFZQ). Discusses barriers to service mesh adoption and ways to address the adopter's dilemma.
- **concept** · [RDMA Programming Using Rust Async - Pu Wang, China](https://www.youtube.com/watch?v=1kMwnqvuxqs). Shows how to program RDMA using Rust async.
- **concept** · [Overview of CNI 1.0.0 and preview of CNI 2.0 - Bruce Ma, Ant Financial & Bingshen Wang, Alibaba](https://www.youtube.com/watch?v=612xICa_qEg). Overview of CNI 1.0.0 and a preview of the planned CNI 2.0.
- **concept** · [Monitor mesh for edge clusters - Liye Pang, Inspur & Huailong Zhang, Intel](https://www.youtube.com/watch?v=-guZplBR51I). Presents a monitoring mesh design for observing edge clusters.
- **concept** · [Extension and expansion of Service Mesh in edge computing scenarios - Wang Jiezhang, Huawei](https://www.youtube.com/watch?v=XolekApWHfE)
- **concept** · [CNCF TAG Network and Service Mesh Working Group - Lee Calcote, Ed Warnicke & Ken Owens](https://www.youtube.com/watch?v=sipjphPVKNY)
- **concept** · [C++ Workflow: Task-based Parallel Computing and Asynchronous Networking Engine - Yingxin Li, Tencent](https://www.youtube.com/watch?v=suBMGtPAI7Y)
- **tutorial** · [BPF: Introduction, Programming Tips and Tricks - Wenbo Zhang, PingCAP](https://www.youtube.com/watch?v=-YUkeIUWz58). Introduction to BPF with programming tips and tricks.

### 2021 · [KubeCon + CloudNativeCon Europe 2021](../sources/PLj6h78yzYM2MqBm19mRz9SYLsw4kfQBrC.md)

- **case study** · [Operationalizing Kubernetes Sidecars in Production at Salesforce - Mayank Kumar, Salesforce](https://www.youtube.com/watch?v=8D4XDPnRkr0) — Salesforce. Salesforce shares how it operates Kubernetes sidecars in production and the lessons learned.
- **concept** · [Linkerd vs. COVID-19: Addressing the global Pandemic with a Service Mesh - William Morgan, CEO](https://www.youtube.com/watch?v=S-7XbbJMonM)
- **concept** · [xDS in gRPC for Service Mesh - Megan Yahya, Google LLC](https://www.youtube.com/watch?v=cGJXkZ7jiDk)
- **concept** · [Towards CNI v2.0 - Casey Callendrello, Red Hat](https://www.youtube.com/watch?v=h9QYbaJzBe0)
- **concept** · [Overview and State of Linkerd - William Morgan & Matei David, Buoyant, Inc.](https://www.youtube.com/watch?v=ATUkfUwbBvo). Overview and project update on the Linkerd service mesh and its state and direction.
- **concept** · [Gateway API: A New Set of Kubernetes APIs for Advanced Traffic Routing - Harry Bagdi & Rob Scott](https://www.youtube.com/watch?v=lCRuzWFJBO0)
- **concept** · [Turning Your Cloud Native Apps Inside Out With a Service Mesh - Adam Zwickey & Liam White, Tetrate](https://www.youtube.com/watch?v=eLxx8WjmEdk)
- **concept** · [Seamless multi-cluster Communication and Observability with Linkerd - Max Körbächer, Liquid Reply](https://www.youtube.com/watch?v=X70Tb54Y-o4)
- **concept** · [Inside Kubernetes Networking - Dominik Tornow, Cisco](https://www.youtube.com/watch?v=kgYcl6bXqMg)
- **concept** · [How to Break your Kubernetes Cluster with Networking - Thomas Graf, Isovalent](https://www.youtube.com/watch?v=7qUDyQQ52Uk). Explains ways networking can break a Kubernetes cluster.
- **concept** · [Cert-Manager Beyond Ingress – Exploring the Variety of Use Cases - Matthew Bates, Jetstack](https://www.youtube.com/watch?v=wEW2kVKxgss)
- **concept** · [CoreDNS Deep Dive: Building Custom Plugins - Yong Tang, Ivanti](https://www.youtube.com/watch?v=ZffZzGbjy1k)
- **concept** · [Contour, a High Performance Multitenant Ingress Controller for Kubernetes - Steve Sloka, VMware](https://www.youtube.com/watch?v=PBIbQ4PBXBA)
- **concept** · [Sponsored Session: HAProxy Technologies - Benchmarking 5 Popular Ingress Controllers](https://www.youtube.com/watch?v=Mf7Y_u3QQ5I)
- **concept** · [Sponsored Session: Google Cloud - Multi-cluster, Blue-green Traffic Splitting with the Gateway API](https://www.youtube.com/watch?v=vs8YrjdRJJU)
- **tutorial** · [Kubernetes Advanced Networking Testing with KIND - Antonio Ojea, RedHat](../sources/videos/-18U84TS75o.md). Antonio Ojea shows how KIND implements networking with Docker and how to use it for advanced Kubernetes network testing.
- **tutorial** · [eBPF on the Rise - Getting Started - Quentin Monnet, Isovalent](https://www.youtube.com/watch?v=cABk-6Sdb20)
- **panel** · [Panel Discussion: Cloud Native Networking State of the Union](https://www.youtube.com/watch?v=pLInEuPnWv4)

### 2021 · [KubeCon + CloudNativeCon North America 2021](../sources/PLj6h78yzYM2Nd1U4RMhv7v88fdiFqeYAP.md)

- **case study** · [Cloud Native Global Load Balancer for Kubernetes - Yury Tsarev & Zak Anderson, Absa Group](https://www.youtube.com/watch?v=-lkKZRdv81A) — Absa Group. Absa Group presents its cloud native global load balancer for Kubernetes, k8gb, and its use in multi-cluster setups.
- **case study** · [Migrating to Service Mesh at Scale to Support Billions of $ Transactions - Imre Nagi & Giri Kuncoro](https://www.youtube.com/watch?v=OE1Qujq51nM)
- **case study** · [Building a Multi Cluster/Env Service Mesh at Airbnb - Weibo He & Stephen Chan, Airbnb](https://www.youtube.com/watch?v=1D8lg36ZNHs) — Airbnb. Airbnb describes how it built its multi-cluster, multi-environment service mesh.
- **case study** · [Context Aware Traffic Routing for Stateful Services using Envoy - Renana Yacobi & Piaw Na, Niantic](https://www.youtube.com/watch?v=0W7aYTjtVwM) — Niantic. Niantic describes using Envoy for context-aware traffic routing of its stateful services.
- **concept** · [Contour, a High Performance Multitenant Ingress Controller for Kubernetes - Steve Sloka & Alex Xu](https://www.youtube.com/watch?v=xLlexJbAQxM)
- **concept** · [Real-time Kubernetes: How Entain Australia 10x'd throughput with Linkerd - Steve Gray](https://www.youtube.com/watch?v=PKhQXjb6cB4)
- **concept** · [How to Improve Your Kubernetes Experience with Service Mesh... Maksim Chudnovskii & Igor Gustomyasov](https://www.youtube.com/watch?v=TfDgsEHA1Yo)
- **concept** · [Cloud Native Superpowers with eBPF - Liz Rice, Isovalent](https://www.youtube.com/watch?v=KY5qujcujfI)
- **concept** · [Calico/VPP: Using Calico’s Pluggable Dataplanes for Fun and Fast N... Aloys Augustin & Chris Tomkins](https://www.youtube.com/watch?v=9zBu4Zcf__c). Shows how Calico's pluggable dataplanes, including VPP, deliver faster networking.
- **concept** · [Beyond the Hype: Cloud Native eBPF - Frederic Branczyk, Polar Signals](https://www.youtube.com/watch?v=2rdNCn_JXYk). Looks past the hype to explain what eBPF offers cloud native systems in practice.
- **concept** · [Storage and Networking: Rook on Multus - Sébastien Han & Rohan Gupta, Red Hat](https://www.youtube.com/watch?v=zIS5qaG_HRw)
- **concept** · [Service Mesh using Envoy on Windows - S. Nanopoulos, P. Balasubramanian, K. Subramanian, N Jackson](https://www.youtube.com/watch?v=ggvaAbjx4jo)
- **concept** · [Deep Dive CoreDNS - Yong Tang, Ivanti Inc.; Miek Gieben, Independent; John Belamaric, Google](https://www.youtube.com/watch?v=tk1ZGU0P4U4)
- **concept** · [Overview and State of Linkerd - Oliver Gould, Buoyant](https://www.youtube.com/watch?v=9qA_iRpYj2w). Linkerd's creator gives an overview and the current state of the project.
- **concept** · [gRPC Proxyless Service Mesh with Security - Sanjay M Pujare, Google](https://www.youtube.com/watch?v=cSxHGt7tc88)
- **concept** · [Envoy Maintainer Q&A - Lizan Zhou, Tetrate](https://www.youtube.com/watch?v=KfEz3hlgyw4)
- **concept** · [Beyond printf & tcpdump: Debugging Kubernetes Networking with eBPF - Martynas Pumputis & Aditi Ghag](https://www.youtube.com/watch?v=vqx-hLYfCYE)

### 2022 · [KubeCon + CloudNativeCon Europe 2022](../sources/PLj6h78yzYM2MCEgkd8zH0vJWF7jdQ-GRR.md)

- **case study** · [Service Mesh at Scale: How Xbox Cloud Gaming Secures 22k Pods with Linkerd - Christopher Voss](https://www.youtube.com/watch?v=Mh0Wqu3v8h0)
- **case study** · [Automated Progressive Delivery Using GitOps and Service Mesh - Yasen Simeonov & Henrik Blixt, Intuit](https://www.youtube.com/watch?v=5Ko-CnP2qhA) — Intuit. Intuit shows how it automates progressive delivery with GitOps and a service mesh.
- **concept** · [How Linkerd Helped bink Partner up with Barclays - Mark Swarbrick, bink](https://www.youtube.com/watch?v=clICN5FXyNE)
- **concept** · [CNCF TAG Network and Service Mesh Working Group Deep-Dive - Lee Calcote, Ken Owens, Ed Warnicke,](https://www.youtube.com/watch?v=ofZyEMTwBwA)
- **concept** · [Composability is to Software as Compounding Interest is to Finance - Bill Mulligan, Isovalent](https://www.youtube.com/watch?v=25aVkm89ZT8). Argues that composability in software compounds value like interest in finance, using cloud native examples.
- **concept** · ["My CNI Plugin Did… What?!": Debugging CNI with Style & Aplomb - Douglas Smith & Daniel Mellado Area](https://www.youtube.com/watch?v=WSO-AFo7dEg)
- **concept** · [Better Bandwidth Management with eBPF - Daniel Borkmann & Christopher M. Luciano, Isovalent](https://www.youtube.com/watch?v=QTSS6ktK8hY)
- **concept** · [Logs Told Us It Was DNS, It Felt Like DNS, It Had To Be DNS, I... Laurent Bernaille & Elijah Andrews](https://www.youtube.com/watch?v=NunyPkN0n3c)
- **concept** · [Lightning Talk: Locating and Debugging Failures with Linkerd... Alejandro Pedraza & Edidiong Asikpo](https://www.youtube.com/watch?v=E13a_CDGRV4)
- **concept** · [Lightning Talk: Tell Your SD-WAN About Your Service Mesh External Services! - Alberto Rodriguez](https://www.youtube.com/watch?v=c1R3RS29x30)
- **concept** · [A Guided Tour of Cilium Service Mesh - Liz Rice, Isovalent](https://www.youtube.com/watch?v=e10kDBEsZw4)
- **concept** · [Simplifying Service Mesh Operations with Flux and Flagger - Mitch Connors & Stefan Prodan](https://www.youtube.com/watch?v=1rJYsdLgJGA). Shows how Flux and Flagger can be combined to simplify operating a service mesh through GitOps and progressive delivery.
- **concept** · [CoreDNS: Intro and Deep Dive - John Belamaric, Google & Yong Tang, Ivanti, Inc](https://www.youtube.com/watch?v=rNlSgYZoIYs)
- **concept** · [Contour Ingress Intro and Deep Dive - Nick Young, Orlin Vasilev & Nigel Brown, VMware](https://www.youtube.com/watch?v=nSc0te3QQ0o)
- **concept** · [Overview and State of Linkerd - Matei David, Buoyant, Inc.](https://www.youtube.com/watch?v=9ksMUVhSW_k). Overview of Linkerd and its current state, with recent changes and plans.
- **concept** · [Three Surprising K8s Networking “Features” and How to Defend Against Them - James Cleverley-Prance](https://www.youtube.com/watch?v=7iwnwbbmxqQ). Covers three surprising Kubernetes networking behaviors and how to defend against them.
- **concept** · [Full Mesh Encryption in Kubernetes with WireGuard and Calico - Peter Kelly, Tigera](https://www.youtube.com/watch?v=G_jcvYMRUhc)
- **concept** · [Gateway API: Beta to GA - Rob Scott, Google & Nick Young, VMware](https://www.youtube.com/watch?v=YPiuicxC8UU)
- **concept** · [Reproducing Production Issues in your CI Pipeline Using eBPF - Matthew LeRay & Omid Azizi](https://www.youtube.com/watch?v=_RQLY4KXXG8)
- **concept** · [Multi-cluster Failover Using Linkerd - Charles Pretzer, Buoyant, Inc.](https://www.youtube.com/watch?v=ieQ5eqd49BQ)
- **tutorial** · [Kubernetes Networking 101 - Randy Abernethy, RX-M LLC](https://www.youtube.com/watch?v=cUGXu2tiZMc)
- **tutorial** · [Cloud-Native Building Blocks: An Interactive Envoy Proxy Workshop - Adam Sayah & Jim Barton, Solo.io](https://www.youtube.com/watch?v=SNM-wnyRR8U)
- **tutorial** · [Emissary + Linkerd: A Guide to End-to-end Encryption for your Cluster - Flynn & Jason Morgan](https://www.youtube.com/watch?v=3NCAUtW0sck). A guide to setting up end-to-end encryption in a cluster using Emissary ingress together with Linkerd.
- **panel** · [Linkerd End User Panel: Case Studies from Production](https://www.youtube.com/watch?v=_DbZ6SFdY1g)
- **keynote** · [Cilium: Welcome, Vision and Updates - Thomas Graf & Liz Rice, Isovalent; Laurent Bernaille, Datadog](https://www.youtube.com/watch?v=oXpGYrbmnwQ)

### 2022 · [KubeCon + CloudNativeCon North America 2022](../sources/PLj6h78yzYM2O5aNpRM71NQyx3WUe1xpTn.md)

- **case study** · [Building Multi-Tenant Routing And Scaling With Envoy - Yiming Peng, Amazon Web Services, Inc.](https://www.youtube.com/watch?v=6-akjOASvxc) — Amazon Web Services. AWS describes building multi-tenant routing and scaling with Envoy.
- **case study** · [What We Learned From the Gateway API: Designing Linkerd’s New Policy CRD - Matei David, Buoyant, Inc](https://www.youtube.com/watch?v=okZq5yOB9Wc) — Buoyant, Inc
- **concept** · [100Gbit/S Clusters With Cilium: Building Tomorrows Networking- Daniel Borkmann & Nikolay Aleksandrov](https://www.youtube.com/watch?v=Kvdh78TURck)
- **concept** · [Resize Your Pods In-Place With Deterministic eBPF Triggers - Pablo Chico de Guzman & Vinay Kulkarni](https://www.youtube.com/watch?v=jjfa1cVJLwc)
- **concept** · [Remote Control Planes With Konnectivity; What, Why And How? - Jussi Nummelin & Rastislav Szabo](https://www.youtube.com/watch?v=0yltsB3Cbr4). Explains what Konnectivity is and how to use it to run control planes remote from worker nodes.
- **concept** · [Five Ways With a CNI: Understanding Kubernetes Networking For Performance..-Stig Telfer & Erez Cohen](https://www.youtube.com/watch?v=m6o-KYF_s5E)
- **concept** · [Whose Packet Is It Anyway? Life of a Packet Through a Service Mesh - Kevin Leimkuhler & Doug Jordan](https://www.youtube.com/watch?v=TJM7juAD8B0)
- **concept** · [Exiting Ingress With the Gateway API - Rob Scott, Google & Shane Utt, Kong, Inc.](https://www.youtube.com/watch?v=sTQv4QOC-TI)
- **concept** · [Using the EBPF Superpowers To Generate Kubernetes Security... Mauricio Vásquez Bernal & Alban Crequy](https://www.youtube.com/watch?v=3dysej_Ydcw). Shows how eBPF tooling can observe workloads to automatically generate Kubernetes security policies.
- **concept** · [Emissary + Linkerd Resilience Patterns: Rate Limits, Retries & Timeouts - Flynn & Daniel Bryant](https://www.youtube.com/watch?v=hOGPz1DJqb8)
- **concept** · [CoreDNS Intro And Deep Dive - Yong Tang, Ivanti](https://www.youtube.com/watch?v=6TkrrZLxQeo). Intro and deep dive into CoreDNS and its plugin architecture.
- **concept** · [Kubernetes Networking Infrastructure...- D Daly & N Jain, N Bitar, Moshe Levi, Vytautas Valancius](https://www.youtube.com/watch?v=L2lcPoGZLgc)
- **concept** · [Dynamically Testing Individual Microservice Releases In Production - Matt Turner, Tetrate](https://www.youtube.com/watch?v=2xvs5QFbheU). Shows how to dynamically test individual microservice releases in production.
- **concept** · [One API To Rule Them All? What the Gateway API Means For Service Meshes - Keith Mattix & John Howard](https://www.youtube.com/watch?v=vYGP5XdP2TA)
- **concept** · [Cilium Updates, News And Roadmap- Thomas Graf, Bill Mulligan Liz Rice, Purvi Desai, Chandan Aggarwal](https://www.youtube.com/watch?v=WxZr35Eyqxk)
- **concept** · [Istio Today and Tomorrow: Sidecars and Beyond - Mitch Conners, Google & Lin Sun, Solo.io](https://www.youtube.com/watch?v=bKNngrE4cc8)
- **concept** · [Decentralized Routing For a Sharded Application On Service Mesh - Vinay Gonuguntla & Pankaj Sikka](https://www.youtube.com/watch?v=cmTRWEcSEZM)
- **concept** · [Overview And State Of Linkerd - Alex Leong, Buoyant](https://www.youtube.com/watch?v=BufQKvH6K1Q)
- **concept** · [Lightning Talk: Securing Envoy: Catching Vulnerabilities With Continuous Fuzz Testing - Teju Nareddy](https://www.youtube.com/watch?v=2wM1Ks23DZU). Lightning talk on using continuous fuzz testing to catch vulnerabilities in Envoy.
- **concept** · [Envoy Maintainer Q+A - Matt Klein, Lyft](https://www.youtube.com/watch?v=Z5BTM5Z7Dw0)
- **tutorial** · [Flagger, Linkerd, And Gateway API: Oh My! - Jason Morgan, Buoyant & Sanskar Jaiswal, Weaveworks](https://www.youtube.com/watch?v=9Ag45POgnKw). Shows how Flagger, Linkerd and the Gateway API work together for progressive delivery.

### 2023 · [KubeCon + CloudNativeCon + Open Source Summit China 2023](../sources/PLj6h78yzYM2OJcjIuAsbbhXAaDrAnuKRB.md)

- **case study** · [Live CNI Migration in Production Environments - Yike Wang and Yanzhao Li, VMware](https://www.youtube.com/watch?v=y75WrvuYt-Y) — VMware
- **concept** · [Building Proxy with New Asynchronous I/O API: Exploring Envoy's Io_uring In... Hejie Xu & Zhihao Xie](https://www.youtube.com/watch?v=dYs1sn-HsrY)
- **concept** · [The Service Mesh Exploration of China Mobile Cloud - Haiwen Zhang, China Mobile](https://www.youtube.com/watch?v=y08jvtXfXH8)
- **concept** · [Service Mesh Is on the Way to Witness the... - Huailong Zhang, Zhonghu Xu, Pei Fei, Xi Ning Wang](https://www.youtube.com/watch?v=jv-DeuXtCJ4)
- **concept** · [Rethink About Service Mesh Load Balancing - Zhonghu Xu, Huawei](https://www.youtube.com/watch?v=oMz1sbCd6-Q)
- **concept** · [CNI-Agnostic Network Performance Accelerator with eBPF - Mengxin Liu, Alauda & Yizhou Xu, Intel](https://www.youtube.com/watch?v=gPmDp4KoxPk)
- **concept** · [Cross-Cluster Traffic Orchestration with eBPF - Xiaohui Zhang, Flomesh & Zhen Chang, Huawei Cloud](https://www.youtube.com/watch?v=e4GA5e-C7n0)
- **concept** · [Envoy Gateway: The API Gateway in the Cloud Native Era - Xunzhuo Liu, Tencent & Huabing Zhao](https://www.youtube.com/watch?v=XBsDe9stMcg)
- **concept** · [Next Hop of Istio After Graduation - Zhonghu Xu, Huawei](https://www.youtube.com/watch?v=n6wWtQTsbC0)
- **concept** · [Scaling up and Scaling Out Networking, Observability, and Security... - Bill Mulligan & Jaff Cheng](https://www.youtube.com/watch?v=l4Fe2YdtfvU)
- **concept** · [Just Buzz or Real Byte? eBPF in Cloud Native - Bill Mulligan, Isovalent](https://www.youtube.com/watch?v=UnERQrBXg1s)
- **concept** · [Detailed Parse and Reproduce Response Flags of Istio Access Log Based on Productio... Chaomeng Zhang](https://www.youtube.com/watch?v=jh6H3uPE8sY)

### 2023 · [KubeCon + CloudNativeCon Europe 2023](../sources/PLj6h78yzYM2PyrvCoOii4rAopBswfz1p7.md)

- **case study** · [Operate Multi-Tenancy Service Mesh with ArgoCD in Production - Lin Sun & Faseela K](https://www.youtube.com/watch?v=w3d8gxGpaNQ)
- **case study** · [Multi-Cluster Observability with Service Mesh - That Is a Lot of Moving Parts!? - Ryota Sawada](https://www.youtube.com/watch?v=6KTzE3LppDg). The speaker shares their experience operating multi-cluster observability across a service mesh and the complexity involved.
- **concept** · [Emissary-Ingress: Self-Service APIs and the Kubernetes Gateway API - Lance Austin & Flynn](https://www.youtube.com/watch?v=piDYmZObh_M)
- **concept** · [Envoy Gateway Update - Alice Wasko, Ambassador Labs & Arko Dasgupta, Tetrate](https://www.youtube.com/watch?v=4vnJxt9sVho). Project update on Envoy Gateway covering recent progress and plans.
- **concept** · [Gateway API Project Update - Nick Young, Isovalent & Rob Scott, Google](https://www.youtube.com/watch?v=zIKNTGTzT1o)
- **concept** · [Life Without Sidecars - Is eBPF's Promise Too Good to Be True? - Zahari Dichev, Buoyant](https://www.youtube.com/watch?v=onQuRBy5rgo)
- **concept** · [Cilium Updates, News, Roadmap, and in the Wild - Liz Rice, Andy Allred, Richard Hartmann](https://www.youtube.com/watch?v=RdAO_Kxe6tE)
- **concept** · [Past, Present, & Future of eBPF in Cloud Native Observability - Frederic Branczyk & Natalie Serrino](https://www.youtube.com/watch?v=pb_eAVAWq2o)
- **concept** · [Verifiable GitHub Actions with eBPF - Jose Donizetti, Aqua](https://www.youtube.com/watch?v=6vNt9JMU9p4). Shows how to verify GitHub Actions runs using eBPF.
- **concept** · [Overview and State of Linkerd - Matei David, Buoyant, Inc.](https://www.youtube.com/watch?v=YaJD-cvbD8o)
- **concept** · [Automated Cloud-Native Incident Response with Kubernetes and Service Mesh - M Turner & F Beltramini](https://www.youtube.com/watch?v=vor-xiV25xM)
- **concept** · [The RPC Revolution: Getting the Most Out of gRPC - Richard Belleville & Kevin Nilson, Google](https://www.youtube.com/watch?v=9dBMPrwtGAQ). Google's gRPC maintainers explain how to get more out of gRPC through its features and best practices.
- **concept** · [Create Istio Filters with Any Programming Language - Angel De Miguel Meana & Rafael Fernandez Lopez](https://www.youtube.com/watch?v=_y3f18gf4FA)
- **concept** · [Beyond Gateway API: Building a Cloud Agnostic Gateway Controller- Michael Larsen & Martin Villumsen](https://www.youtube.com/watch?v=o7Q7S2qn0LI)
- **concept** · [Future of Istio - Sidecar, Sidecarless or Both? - Neeraj Poddar, Solo.io](https://www.youtube.com/watch?v=OSD3sftzSO0)
- **concept** · [SIG Network: Intro and Updates - Antonio Ojea Garcia, Google; Surya Seetharaman, Red Hat; Shane Utt](https://www.youtube.com/watch?v=0uPEFcWn-_o). SIG Network introduces itself and gives updates on its recent work and roadmap.
- **concept** · [🦝 The Top 10 List of Istio Security Risks and Mitigation Strategies - José Carlos Chávez, Tetrate](https://www.youtube.com/watch?v=aCCm9VowNSs)
- **concept** · [The Next Log4jshell?! Preparing for CVEs with eBPF! - Natalia Reka Ivanko & John Fastabend](https://www.youtube.com/watch?v=u8HKg5pENj4)
- **concept** · [Agones + Quilkin: Kubernetes Game Server Orchestration and UDP Service Mesh - Mark Mandel](https://www.youtube.com/watch?v=RHOHkIYdrqw)
- **concept** · [Developing a Mental Model of Istio: From Kubernetes to Sidecars...- Aaron Birkland & Nina Polshakova](https://www.youtube.com/watch?v=0xCsMfPVZ6M). Builds a mental model of how Istio works by relating its sidecar-based mesh to underlying Kubernetes primitives.
- **concept** · [Effortless Open Source Observability with Cilium, Prometheus... - Raymond de Jong & Anna Kapuścińska](https://www.youtube.com/watch?v=l3zY7wHUkBA)
- **concept** · [Surviving Day 2 - How to Troubleshoot Kubernetes Networking - Thomas Graf, Isovalent](https://www.youtube.com/watch?v=920BZXvQpVs). Covers approaches to troubleshooting Kubernetes networking in day 2 operations.
- **concept** · [Keeping It Simple: Cilium Networking for Multicloud Kubernetes - Liz Rice, Isovalent](https://www.youtube.com/watch?v=fJiuqRY5Oi4)
- **concept** · [Scale the Internet with DNS: A CoreDNS Deep Dive - Yong Tang, Ivanti](https://www.youtube.com/watch?v=bfUzLOFwns8)
- **concept** · [Exiting Ingress 201: A Primer on Extension Mechanisms in Gateway API- Sunjay Bhatia & Daneyon Hansen](https://www.youtube.com/watch?v=7P55G8GsYRs). Primer on the extension mechanisms Gateway API offers beyond what Ingress supported.
- **tutorial** · [Tutorial: Getting Familiar with Security Observability Using eBPF &Cilium Tetragon - Holmes & Cooley](https://www.youtube.com/watch?v=kTGU-Nc2Db0)
- **tutorial** · [Tutorial: Measure Twice, Cut Once: Dive Into Network Foundations the Right Way! - Wijay & Skrzypek](https://www.youtube.com/watch?v=3BLwRDh9JgA). A hands-on tutorial on network fundamentals for Kubernetes.
- **tutorial** · [eBPF 201: Supercharging Your eBPF Dev Process for Cloud Native Apps - Sanjeev Rampal & Donald Hunter](https://www.youtube.com/watch?v=9vUJhbqf4eo). Intermediate eBPF session on speeding up the eBPF development process for cloud native apps.
- **tutorial** · [Kubernetes Networking 101: An Overview of Popular Networking Options - Goutam Verma](https://www.youtube.com/watch?v=wUah5rHCp3M)

### 2023 · [KubeCon + CloudNativeCon NA 2023](../sources/PLj6h78yzYM2MYc0X1465RzF_7Cqf7bnqL.md)

- **case study** · [A Practical Guide to eBPF Licensing: Or How I Learned to Stop Worryin... Jef Spaleta & Bill Mulligan](https://www.youtube.com/watch?v=cxyDEdzNdH8)
- **case study** · [Five Years of Cloud Native Rust - Alex Leong, Buoyant](https://www.youtube.com/watch?v=9Ro-LN2SmhY) — Buoyant. Buoyant reflects on five years of building the Linkerd data plane in Rust and the lessons learned.
- **case study** · [Service Mesh Journey at DoorDash: The Good, the Bad, and the Ugly - Hochuen Wong, DoorDash](https://www.youtube.com/watch?v=I6E_7f40YP0) — DoorDash
- **case study** · [Cilium: From Service Mesh to Kubernetes and... James McShane, Hemanth Malla, Liz Rice & Thomas Graf](https://www.youtube.com/watch?v=b-3AyOBBRU4)
- **concept** · [Network Policy API: Intro and Project... Andrew Stoycos, Surya Seetharaman, Dan Winship & Yang Ding](https://www.youtube.com/watch?v=lYWW3KogPTg)
- **concept** · [Service Mesh Battle Scars: Technology, Timing, and Tradeoffs - Panel](https://www.youtube.com/watch?v=fOZ2jCechns)
- **concept** · [High Performance, Low Latency Networking for Edge & Telco](https://www.youtube.com/watch?v=hXAcaLOh2Uw)
- **concept** · [Take It to the Edge: Creating a Globally Distributed Ingress with Istio & K8gb - Jimmi Dyson, D2iQ](https://www.youtube.com/watch?v=4qJDkw5YGqM). Shows how to build a globally distributed ingress with Istio and k8gb.
- **concept** · [Service via BGP with Metallb and Calico - Evangelista Tragni & Francesco Grimaldi, Desotech SRL](https://www.youtube.com/watch?v=boOP5EzZUAk)
- **concept** · [Demystifying Service Mesh: Separating Hype from Practicality - Brian Redmond & Ally Ford, Microsoft](https://www.youtube.com/watch?v=yNsV9uqskMk)
- **concept** · [When Is a Secure Connection Not Encrypted? and Other Stories - Liz Rice, Isovalent](https://www.youtube.com/watch?v=5U9h4E0H5RA). Liz Rice explains when secure connections are not actually encrypted and the pitfalls of how encryption is applied in Kubernetes networking.
- **concept** · [Collecting Low-Level Metrics with eBPF - Mauricio Vásquez Bernal, Microsoft](https://www.youtube.com/watch?v=_ft3iTw5uv8)
- **concept** · [CoreDNS Plugins: A Deep Dive - Yong Tang, Ivanti & John Belamaric, Google](https://www.youtube.com/watch?v=-L9_MLmnKfs). Deep dive into how CoreDNS plugins work and are built.
- **concept** · [Envoy Maintainer Q&A - Alyssa Wilk, Josh Marantz, Greg Greenway, Yan Avlasov](https://www.youtube.com/watch?v=M0n9mN8o-yw)
- **concept** · [Emissary-Ingress: Self-Service APIs and the Kubernetes Gateway API - Hamzah Qudsi & Flynn](https://www.youtube.com/watch?v=UKc01HZasWc)
- **concept** · [Gateway API: The Most Collaborative API in Kubernetes History Is GA - Rob Scott & Nick Young](https://www.youtube.com/watch?v=V3Vu_FWb4l4)
- **concept** · [Turning up Performance to 11: Cilium, NetKit Devices, and Going Big with TCP - Daniel Borkmann](https://www.youtube.com/watch?v=AVEBcZc0YsQ). Explains Cilium performance improvements using netkit devices and big TCP.
- **concept** · [Modern Load Balancing, Improving Application's Resource Availability... Antonio Ojea & Gerrit DeWitt](https://www.youtube.com/watch?v=NlO4uhhQiRw)
- **concept** · [eBPF for Observability: Data Overload Panacea or Pain...](https://www.youtube.com/watch?v=3wyfGmUNPE8). Examines whether eBPF-based observability solves or worsens data overload.
- **concept** · [Apply the Can Opener of Enlightenment: Lifting the Lid off Kubernetes Networking - Joe Thompson](https://www.youtube.com/watch?v=OQxHmTP232A)
- **concept** · [Service Proxy, API Gateway, Service Mesh: What’s the Difference? W... Ahmet Soormally & Carol Cheung](https://www.youtube.com/watch?v=YDgkH8KOeHU)
- **concept** · [Linkerd for the Enterprise: VM Support, Flat Networks, Gateway API, and More - William Morgan](https://www.youtube.com/watch?v=gKh1nWtxGTQ)
- **concept** · [Survive eBPF Deployment with Bpfd - Andrew Stoycos, Red Hat & Shane Utt, Kong](https://www.youtube.com/watch?v=8pXBbFzH_tQ). Presents bpfd for safely deploying and managing eBPF programs in Kubernetes.
- **concept** · [Istio: The Past, Present and Future of the Project and Community - Louis Ryan & John Howard](https://www.youtube.com/watch?v=vu18vpTxX0g)
- **concept** · [Flavors of Certificates in Service Mesh: The Whys and Hows! - Iris Ding & Faseela Kundattil](https://www.youtube.com/watch?v=1aYVoQNo3qc). Explains the different kinds of certificates used in service mesh and how and why they are configured.
- **concept** · [Paint the Picture! - Detecting Suspicious Data Patterns in E... Natalia Reka Ivanko & John Fastabend](../sources/videos/-2FykHaqvlg.md). Shows how Tetragon uses eBPF and kTLS to detect suspicious data patterns in encrypted traffic.
- **concept** · [Under the Hood: Exploring Istio's Lock Contention and Its Impact o... Raghav Grover & Timothy Ehlers](https://www.youtube.com/watch?v=HFduMmPcKqI)
- **concept** · [Untangling Your Service Mesh with Feature Gates - Niranjan Shankar, Microsoft](https://www.youtube.com/watch?v=BuChyhnmHeA)
- **concept** · [Scaling Kubernetes Networking to 1k, 5k, ... 100k Nodes!? - Marcel Zięba & Dorde Lapcevic](https://www.youtube.com/watch?v=VWGB-NW800Y)
- **concept** · [eBPF + Wasm: Lightweight Observability on Steroids - Michael Yuan & Yusheng Zheng](https://www.youtube.com/watch?v=cZk0Jsi4N5Y)
- **concept** · [gRPC Tapping Filter with Hardware Accelerated in Service Mesh - Yizhou Xu & Devan Nair](https://www.youtube.com/watch?v=2qbMEZzbSyY). Shows how a gRPC tapping filter can be hardware accelerated in a service mesh.
- **concept** · [Make Underlay CNI to Be Powerful and Simple - Lan Weizhou & Qiuping Dai, Daocloud](https://www.youtube.com/watch?v=KqfzkOGObCQ)
- **concept** · [A Wind of Change for Threat Detection - Melissa Kilby, Apple](https://www.youtube.com/watch?v=1y1m9Vz93Yo). Describes changes and new directions in threat detection, focused on Falco and runtime security.
- **tutorial** · [Tutorial: Demystifying Cilium: Learn How to Build an eBPF CNI Plugin from Scratch - Adam Sayah](https://www.youtube.com/watch?v=3cqCmtg-TOo). Hands-on tutorial building an eBPF-based CNI plugin from scratch to understand how Cilium works.

### 2024 · [KubeCon + CloudNativeCon + Open Source Summit + AI_dev China 2024](../sources/PLj6h78yzYM2NcAGHRxgBHY8x3QTfnZQCv.md)

- **case study** · [Understanding the Buzz Around Cilium: Introduction and in Production at... - Bo Kang Li & Liyi Huang](https://www.youtube.com/watch?v=SAmFvxW-lOw)
- **concept** · [Best Practice: Karmada & Istio Improve Workload & Traffic Resilience of Production... Chaomeng Zhang](https://www.youtube.com/watch?v=cfY0RWzM6CM)
- **concept** · [How Does KubeEdge Build the Tunnel Which Is Secure, Trusted, and Adapta...- Wei Hu & Clement Richard](https://www.youtube.com/watch?v=-elXR50jgKk). Describes how KubeEdge builds a secure, trusted and adaptable tunnel between cloud and edge.
- **concept** · [Model Service Mesh: A New Paradigm for Large-Scale AI Model Servic...- Xi Ning Wang & Huailong Zhang](https://www.youtube.com/watch?v=Yz1IDRe_eJg)
- **concept** · [Unlocking LLM Performance with EBPF: Optimizing Training and Inference Pipelines - Yang Xiang](https://www.youtube.com/watch?v=Pb1QhYGCCdI)
- **concept** · [Gateway API and Beyond: Introducing Envoy Gateway's Gateway API Extensions - Huabing Zhao, Tetrate](https://www.youtube.com/watch?v=qH2byF7SDO8)
- **concept** · [Revolutionizing Service Mesh with Kernel-Native Sidecarless Architecture - Xin Liu](https://www.youtube.com/watch?v=vZUwOGCnKQU)
- **concept** · [Unified Management, Continuity, Compliance in Multi-Clouds with Service Mesh - Kebe Liu, DaoCloud](https://www.youtube.com/watch?v=b-codkDu344)
- **concept** · [Redefining Service Mesh: Leveraging EBPF to Optimize Istio Ambient Architecture and... - Yuxing Zeng](https://www.youtube.com/watch?v=0YRZa-R33IE). Shows how eBPF can optimize Istio Ambient mesh architecture.
- **concept** · [What Is the Future of Service Mesh? Sidecar or Sidecarless - Zhonghu Xu, Huawei](https://www.youtube.com/watch?v=8jiLbWLKkMU). Compares sidecar and sidecarless service mesh architectures and where service mesh is heading.
- **concept** · [A New Choice for Istio Data Plane: Architectural Innovation for a Brand-New Performan...- Zhonghu Xu](https://www.youtube.com/watch?v=WtGR48h_MEs)
- **concept** · [Multi-Cluster Networking and Service Discovery Leveraging NRI - LingMing Xia & Di Xu](https://www.youtube.com/watch?v=Bu3aN8rR0Ek)
- **concept** · [Implementing Seamless Connectivity and Service Governance in Multi Kubernetes Clu... - Xiaohui Zhang](https://www.youtube.com/watch?v=9IAZyWk6BI4). Describes approaches to seamless connectivity and service governance across multiple Kubernetes clusters.
- **concept** · [Project Lightning Talk: Telemetry API and Open Telemetry: the answer of istio monitoring?](https://www.youtube.com/watch?v=k9JD_sDdLqo)
- **concept** · [Project Lightning Talk: A Deep Dive into Cilium Gateway API: The Future of Ingress Traffic Routing](https://www.youtube.com/watch?v=H3LFb4Q7Hbw)
- **panel** · [Istio and Modern API Gateways: Navigating the Future of Service Meshes - Panel Discussion](https://www.youtube.com/watch?v=6t-oJQOPaBM). A panel on the future of service meshes and their relationship with API gateways.

### 2024 · [KubeCon + CloudNativeCon Europe 2024](../sources/PLj6h78yzYM2N8nw1YcqqKveySH6_0VnI0.md)

- **case study** · [Assessing Service Mesh's Net Worth: A Pragmatic Onboarding - Adrien Gillard, Decathlon](https://www.youtube.com/watch?v=5quqbj8npRo) — Decathlon. Decathlon assesses the value of a service mesh and describes its pragmatic onboarding approach.
- **case study** · [No 'Soup' for You! Enforcing Network Policies for Host Processes via eBPF - Vinay Kulkarni, eBay](https://www.youtube.com/watch?v=AWAf3H4Qwq8) — eBay. eBay describes enforcing network policies on host processes with eBPF in its own infrastructure.
- **case study** · [Reducing Cross-Zone Egress at Spotify with Custom gRPC Load Balancing](https://www.youtube.com/watch?v=8E5zVdEfwi0) — Spotify. Spotify reduced cross-zone egress costs by implementing custom gRPC load balancing.
- **concept** · [Istio Project Update - Mitch Connors, Aviatrix & Zhonghu Xu, Huawei](https://www.youtube.com/watch?v=oxM6iqiV-Ts)
- **concept** · [eBPF’s Abilities and Limitations: The Truth - Liz Rice & John Fastabend, Isovalent](https://www.youtube.com/watch?v=tClsqnZMN6I)
- **concept** · [At the Intersection of Cilium CNI and Service Mesh - Who Has the Right of Way? - Christine Kim](https://www.youtube.com/watch?v=ZykwwHt5hYY)
- **concept** · [Next-Level Security: Implementing MTLS in Istio Multi-Cluster Environments Using SPIRE](https://www.youtube.com/watch?v=83jOYMnmWWY). Explains implementing mTLS across Istio multi-cluster environments using SPIRE for identity.
- **concept** · [Scaling Service Mesh: Self Service Beyond 300 Clusters - Sumit Mathur & Sushanth Kamath A, Intuit](https://www.youtube.com/watch?v=Iz9_FDEKF5M)
- **concept** · [Cilium ClusterMesh in Action: Strengthening Security Across Distributed Kubernetes Clusters](https://www.youtube.com/watch?v=MSqI-gBiCrc)
- **concept** · [CNI: Recap and Update - Casey Callendrello, Isovalent & Tomofumi Hayashi, Red Hat](https://www.youtube.com/watch?v=V7xyWeXBDWg)
- **concept** · [Bringing SPIFFE to Linkerd for Mesh Expansion - Zahari Dichev, Buoyant](https://www.youtube.com/watch?v=ZLCJW--J6s0)
- **concept** · [Unlock Energy Consumption in the Cloud with eBPF - Leonard Pahlke](https://www.youtube.com/watch?v=lW9pZoKRJVs)
- **concept** · [Gateway API: Beyond GA - Mattia Lavacca, Kong; Surya Seetharaman, Nick Young, Lior Lieberman](https://www.youtube.com/watch?v=LITg6TvctjM)
- **concept** · [Stop Leaking Kubernetes Service Information via DNS! - John Belamaric, Google & Yong Tang, Ivanti](https://www.youtube.com/watch?v=Nfc4CiLUxUU)
- **concept** · [Network Policy: The Future of Network Policy with AdminNetworkPolicy](https://www.youtube.com/watch?v=riSv0g-TNtI)
- **concept** · [The Rustvolution: How Rust Is the Future of Cloud Native - Flynn, Buoyant](https://www.youtube.com/watch?v=2q3RLffSvEc). Argues that Rust is the future of cloud native software, drawing on the Linkerd data plane's design.
- **concept** · [Ingress-Nginx and 2024 Plans - Marco Ebert, Giant Swarm & James Strong, Isovalent](https://www.youtube.com/watch?v=8qaU9SX-IdI). Ingress-NGINX maintainers outline project status and plans for 2024.
- **concept** · [Fast and Efficient Log Processing with Wasm and eBPF - Michael Yuan, Second State](https://www.youtube.com/watch?v=4u7nUpZxr3g). Shows how Wasm and eBPF can be combined for fast, efficient log processing.
- **concept** · [What not to do when you're updating Istio in a critical environm... David de Lucca & Guilherme Saijo](https://www.youtube.com/watch?v=hjddDoV83Co)
- **concept** · [Troubleshooting Hidden Performance and Costs in Network Traffic Across Multiple AZs with eBPF](https://www.youtube.com/watch?v=CF0vAWhxKU4)
- **concept** · [Linkerd Project Update: VM Support, Ingress, Security on the Edge, and Rust](https://www.youtube.com/watch?v=N76X9N_y7j8)
- **concept** · [CoreDNS Plugins: A Deep Dive - John Belamaric, Google & Yong Tang, Ivanti](https://www.youtube.com/watch?v=Rtl3MXdSkzk)
- **concept** · [Simplifying Multi-Cluster and Multi-Cloud Deployments with Cilium - Liz Rice, Isovalent](https://www.youtube.com/watch?v=qbB3TEiOb24)
- **concept** · [How Many Network Policies Can I Create? - Nadia Pinaeva, Red Hat & Shaun Crampton, Tigera](https://www.youtube.com/watch?v=2YDQFv0aRCQ). Examines how many network policies a cluster can handle and how different CNIs scale.
- **concept** · [Persistence Pays Off: The Path to Session Persistence in Gateway API](https://www.youtube.com/watch?v=5uoHQNkJC10). Explains how session persistence is being designed in Gateway API.
- **concept** · [Comparing Sidecar-Less Service Mesh from Cilium and Istio - Christian Posta, Solo.io](https://www.youtube.com/watch?v=91oylZSoYzM). Compares the sidecar-less service mesh approaches of Cilium and Istio.
- **concept** · [A Cilium Introduction: Back to Bee-Sics - Nico Vibert & Dan Finneran, Isovalent](https://www.youtube.com/watch?v=KZzNm5ntRbo)
- **concept** · [The gRPCRoute to Success: Idiomatically Routing and Balancing...- Richard Belleville & Arko Dasgupta](https://www.youtube.com/watch?v=8cXm-TtkGd0). Explains how GRPCRoute in Gateway API routes and balances gRPC traffic idiomatically.
- **concept** · [Sustainable Computing: Measuring Application Energy Consumption in Kubernetes Environments with K...](https://www.youtube.com/watch?v=7_a9mCTcxkk). Shows how to measure application energy consumption in Kubernetes environments.
- **concept** · [What’s New in Kuma: Advanced Service Mesh Capabilities | Project Lightning Talk](https://www.youtube.com/watch?v=wHIbrOoU5EY)
- **concept** · [Future of Service Mesh is Sidecar-less with Istio Ambient Mesh | Project Lightning Talk](https://www.youtube.com/watch?v=Oh5jFS5bL3M)
- **concept** · [K8gb: Reliable Global Service Load Balancing without vendor lock-in | Project Lightning Talk](https://www.youtube.com/watch?v=MsQ0E7SYNPo)
- **concept** · [Lightning Talk: Help! My Envoy Sidecar Is Consuming 8GBs of Memory! - Krzysztof Słonka, Kong](https://www.youtube.com/watch?v=ikOw8WubgHE)
- **concept** · [Dealing with eBPF’s Observability Data Deluge - Anna Kapuścińska, Isovalent](https://www.youtube.com/watch?v=yWB8n_e4N14)
- **concept** · [Cilium: Connecting, Observing, and Securing Service Mesh and Beyond with eBPF - Panel](https://www.youtube.com/watch?v=wq1TxZw1AaY)
- **tutorial** · [Tutorial: Simpler Than Making a Fraisier Cake: Building, Running, and Observing Your First eBPF...](https://www.youtube.com/watch?v=lpopvZ67l6I)
- **tutorial** · [Tutorial: From CNI Zero to CNI Hero: A Kubernetes Networking Tutorial Using CNI](https://www.youtube.com/watch?v=YumoKGhuZ2o)
- **tutorial** · [Tutorial: Configuring Your Service Mesh with Gateway API - Mike Morris, Microsoft & Flynn, Buoyant](https://www.youtube.com/watch?v=UMGRp0fGk3o)

### 2024 · [KubeCon + CloudNativeCon India 2024](../sources/PLj6h78yzYM2P0vFbS4o1I0gRHSiXgLiEe.md)

- **case study** · [Pick Cilium! Lessons Learned From Writing 20+ Cloud Native Case Studies about Cilium](https://www.youtube.com/watch?v=AlqYDsARSo8)
- **case study** · [From Bottleneck to Breakthrough: EarnIn's Network Evolution with Link... K. Trivedi & S. Chakraborty](https://www.youtube.com/watch?v=8QPbI25lw0g) — EarnIn. EarnIn recounts how its network evolved by adopting Linkerd.
- **case study** · [A Debugging Journey from CoreDNS to Coreutils - Akhil Mohan & Humble Devassy Chirammal, VMware](https://www.youtube.com/watch?v=_7P61ojiCKk) — VMware
- **case study** · [Stay Ahead of Disruptions : Experience Robust DNS Failover for API Ga... G. Yadav & V. K. M. Vadrevu](https://www.youtube.com/watch?v=1NJAJkYHoUM). Speakers describe building robust DNS failover for API gateways to stay available through disruptions.
- **concept** · [Lightning Talk: Non-Intrusive Multi-Tenant Auth & Authz with Istio, OAuth2Pr... - Adarsh Kumar Singh](https://www.youtube.com/watch?v=QTgiQ2I0ZwE)
- **concept** · [Invoking Serverless Functions via gRPC Service Mesh - K. Jayaprakasam, S. Sridharan & R. Belleville](https://www.youtube.com/watch?v=07HWxUEPJ_o). Shows how to invoke serverless functions through a gRPC service mesh.
- **concept** · [A Deep Dive Into the Current Runtime Security Landscape - Ankur Kothiwal, CERN](https://www.youtube.com/watch?v=1euSNC0ObNk). Survey of the current runtime security tooling landscape for cloud native workloads.
- **concept** · [Contributing to Istio : View from an LFX Mentee's Eyes - Adil Mohamed M P, Independent](https://www.youtube.com/watch?v=JpOzPFHBH0w)
- **concept** · [Cilium: Connecting, Observing, and Securing Kubernetes and Beyond with eBPF - B. Mulligan & N. Bisht](https://www.youtube.com/watch?v=0ZnxpVkBxpo). Overview of Cilium for connecting, observing and securing Kubernetes with eBPF.

### 2024 · [KubeCon + CloudNativeCon NA 2024 - Salt Lake City](../sources/PLj6h78yzYM2Pw4mRw4S-1p_xLARMqPkA7.md)

- **case study** · [Cash App's Journey Into a Multi-Cluster Ecosystem - Rachel Sheikh, Cash App](https://www.youtube.com/watch?v=9TSNOVJ6BEY) — Cash App. Cash App shares its journey to a multi-cluster Kubernetes ecosystem.
- **case study** · [How to Move from Ingress to Gateway API with Minimal Hassle - Keith Mattix, Microsoft](https://www.youtube.com/watch?v=dyye6L6aKkA) — Microsoft
- **case study** · [Understanding How OpenTelemetry Network Uses eBPF for Network Observab... S.R. Shrivastava, J. Perry](https://www.youtube.com/watch?v=Ljf671BSu2g) — OpenTelemetry Network
- **case study** · [From Observability to Enforcement: Lessons Learned Implementing eBPF R... A. Kapuścińska, K. Kourtis](https://www.youtube.com/watch?v=Hw469I5GKmY)
- **case study** · [Thousands of Gamers, One Kubernetes Network - Surya Seetharaman, Red Hat & Girish Moodalbail](https://www.youtube.com/watch?v=76tfwAvDWX8) — Red Hat, NVIDIA. Red Hat and partner engineers show how one Kubernetes network was built to serve thousands of gamers.
- **case study** · [Accelerating Adoption: What’s New in Envoy Gateway and Why It Matters | Project Lightning Talk](https://www.youtube.com/watch?v=y6O220qbmXc)
- **case study** · [Kubernetes at Scale: Practical Solutions for Enhanced CNI and Kubelet P... H. Santana, B.G. da Silva](https://www.youtube.com/watch?v=tKoxI-k7cu8)
- **concept** · [Solving the Kubernetes Networking API Rubik's Cube - D. Smith, S. Seetharaman, S. Utt, L. Lieberman](https://www.youtube.com/watch?v=S5QsqEb8wec)
- **concept** · [Understanding Kubernetes Networking in 30 Minutes - Ricardo Katz & James Strong](https://www.youtube.com/watch?v=Mj04QOqAaJ8)
- **concept** · [Cilium: Connecting, Observing, and Securing Kubernetes and Beyond with eBPF - Panel](https://www.youtube.com/watch?v=xJ_Jiv7y6N0)
- **concept** · [Life of a Packet: Ambient Edition - John Howard, Solo.io & Keith Mattix, Microsoft](https://www.youtube.com/watch?v=5IJwd9X5Yk8). Follows a packet through Istio ambient mesh to show how traffic flows.
- **concept** · [Extending the Gateway API: The Power and Challenges of Policies - Kate Osborn, NGINX](https://www.youtube.com/watch?v=haeVAmhihT4)
- **concept** · [Cilium, eBPF, WireGuard: Can We Tame the Network Encryption Performanc... D. Borkmann, A. Protopopov](https://www.youtube.com/watch?v=oXhNVj80Z8A)
- **concept** · [Optimizing Load Balancing and Autoscaling for Large Language Model (LLM) Inference on Kub... D. Gray](https://www.youtube.com/watch?v=TSEGAh1bs4A)
- **concept** · [Can Your Kubernetes Network Handle the Heat? Building Resilience wit... L. Lieberman, S. Seetharaman](https://www.youtube.com/watch?v=2oTtpRpv3M8). Explores how to build resilience into Kubernetes networking so it can withstand failures and stress.
- **concept** · [All Your Routes Are Ready, More or Less - Dave Protasowski](https://www.youtube.com/watch?v=6eMplLH3NIw). Explains how route readiness is determined and why it is eventually consistent in the networking layer.
- **concept** · [DNS Deep Dive in Kubernetes with CoreDNS - Jingming Guo, Airbnb](https://www.youtube.com/watch?v=lAUmdIGP_fE)
- **concept** · [Gateway API: What's New, What's Next? - C. Kim, N. Young, M. Lavacca, G. Cassolato](https://www.youtube.com/watch?v=reGxuaM7XBs)
- **concept** · [What Istio Got Wrong: Learnings from the Last Seven Years of Service Mesh - C. Posta, L. Ryan](https://www.youtube.com/watch?v=XW10IpsTmH8)
- **concept** · [Shopify’s Open Source Approach to Network Monitoring with eBPF, Vector... S. Rabenhorst, M. Franklin](https://www.youtube.com/watch?v=FpVjdaRVmA4)
- **concept** · [Powering Automatic Authorization in Envoy Through Live Traffic Inspection - Dom Del Nano](https://www.youtube.com/watch?v=_d5ff8QTmX4)
- **concept** · [CoreDNS Plugins: A Deep Dive - John Belamaric, Google & Yong Tang, Ivanti](https://www.youtube.com/watch?v=av2duJhlaTw)
- **concept** · [Testing Kubernetes Without Kubernetes: A Networking Deep Dive - John Howard, Solo.io](../sources/videos/-Dp7fAxXuwI.md). John Howard shows how to test Kubernetes networking components without a real cluster for faster, easier-to-debug tests.
- **concept** · [With Great Flexibility Comes Great Complexity: Inspect Your Gateway API... M. Lavacca, G. Ghildiyal](https://www.youtube.com/watch?v=kbTVzAhtHKs)
- **concept** · [Inspektor Gadget: eBPF for Observability, Made Easy and Approachable | Project Lightning Talk](https://www.youtube.com/watch?v=_nR1cHhBth8)
- **concept** · [OpenTelemetry: The Future of Network Monitoring eBPF for Low-Level Insights | Project Lightning Talk](https://www.youtube.com/watch?v=LSAl0qVWXKQ)
- **concept** · [k8gb: Global Load Balancing, the Kubernetes Way | Project Lightning Talk](https://www.youtube.com/watch?v=vCzl15AIoU0)
- **concept** · [Linkerd: Adding Federated Services to Linkerd - Design Considerations and Debates | PLT](https://www.youtube.com/watch?v=qXrmhlXP4tw)
- **concept** · [Istio: Why Choose Istio in 2025 | Project Lightning Talk](https://www.youtube.com/watch?v=boU_yVSLrbY)
- **concept** · [Kuma: What’s New in Kuma? | Project Lightning Talk](https://www.youtube.com/watch?v=52A593Kxo8Y). Lightning talk on what is new in the Kuma service mesh.
- **concept** · [Seeing Double? Implementing Multicast with eBPF and Cilium - Louis DeLosSantos, Isovalent at Cisco](https://www.youtube.com/watch?v=fX7LL0cIX40)
- **concept** · [CNI Updates and Direction! - Michael Zappa, Microsoft & Lionel Jouin, Ericsson](https://www.youtube.com/watch?v=sWQ6Vonzkr0)
- **concept** · [Mish-Mesh: Abusing the Service Mesh to Compromise Kubernetes Environments - H. Ben-Sasson, N. Ohfeld](https://www.youtube.com/watch?v=iMQR_l0ZvWU)
- **concept** · [Seccomp and eBPF; What’s the Difference? Why Do I Need to Know? - Natalia Reka Ivanko, Duffie Cooley](https://www.youtube.com/watch?v=o5MdGMFcj1M)
- **concept** · [Harnessing the Power of Envoy Proxy for Building an LLM Gateway - Idit Levine, Solo.io](https://www.youtube.com/watch?v=w9rOcy2tGr4)
- **concept** · [One Gateway API to Rule Them All (and in the Cluster Configure Them) - Flynn, Buoyant](https://www.youtube.com/watch?v=sRHjg6bGfug)
- **concept** · [Linkerd Update: Egress, Rate Limiting, Federated Services, and more  William Morgan, Linkerd](https://www.youtube.com/watch?v=aOt62I2bkxk)
- **tutorial** · [Kubernetes Multi-Cluster Networking 101 - Niranjan Shankar, Microsoft & Ram Vennam, Solo.io](https://www.youtube.com/watch?v=cpkKinqdwqA)
- **tutorial** · [Tutorial: No Mess Rollouts with Gateway API: Leveraging Gateway API and... N. Polshakova, L. Gadban](https://www.youtube.com/watch?v=H67jKACtPHs)
- **tutorial** · [Tutorial: A Mad Scientist's Guide to Automating CNI with Generative AI - Doug Smith, Red Hat, Inc](https://www.youtube.com/watch?v=tEVoXKtymIA)
- **tutorial** · [Tutorial: Live with Gateway API V1.2 - Flynn, Buoyant & Mike Morris, Microsoft](https://www.youtube.com/watch?v=asbtOWQosxI)

### 2025 · [KubeCon + CloudNativeCon China 2025 (Hong Kong)](../sources/PLj6h78yzYM2P1xtALqTcCmRAa6142uERl.md)

- **concept** · [Revolutionizing Sidecarless Service Mesh With eBPF - Zhonghu Xu & Muyang Tian, Huawei](https://www.youtube.com/watch?v=kZuewTKKcQY)
- **concept** · [Guardians of the Gateway: Keeping Chaos Out of Your Cloud Highway - Sayan Mondal & Jintao Zhang](https://www.youtube.com/watch?v=6V-2xKUCV7A). Shows how to apply chaos engineering to gateways to test the resilience of cloud traffic paths.
- **concept** · [Project Lightning Talk: Practical Extension of eBPF Usability in KubeCon - Lizhencheng, Maintainer](https://www.youtube.com/watch?v=c9AQ2kVTcuc)
- **concept** · [Lightning Talk: Best Practices for Upgrading Service Mesh Seamlessly - Hang Yin & Zhencheng Lee](https://www.youtube.com/watch?v=iqL0AEw2b_c)
- **concept** · [Simplifying the Networking and Security Stack With Cilium, Hubble, and Tet... Liyi Huang & Kaixi Fan](https://www.youtube.com/watch?v=cKPW67D7X10)

### 2025 · [KubeCon + CloudNativeCon Europe 2025 - London](../sources/PLj6h78yzYM2MP0QhYFK8HOb8UqgbIkLMc.md)

- **case study** · [How We Moved Spotify To a Proxyless gRPC Service Mesh - Erik Lindblad & Erica Manno, Spotify](https://www.youtube.com/watch?v=2_ECK6v_yXc) — Spotify. Spotify explains how it migrated to a proxyless gRPC service mesh.
- **case study** · [Journey at the New York Times: Is Sidecar-Less Service Mesh Disappearing I... Lin Sun & Ahmed Bebars](https://www.youtube.com/watch?v=9U3WMez9q74) — New York Times. The New York Times shares its service mesh journey and evaluates whether sidecar-less mesh is replacing sidecars.
- **case study** · [Expanding eBPF’s Reach: From Batteries-Included Auto-Instrumentation To E2E Observab... Dom Del Nano](https://www.youtube.com/watch?v=I236sjooftw)
- **concept** · [Using eBPF for Non-invasive, Performant, Instant Network Monitoring - Mario Macías & Marc Tudurí](https://www.youtube.com/watch?v=HV3Nb_wUro4)
- **concept** · [Emissary-ingress: Version 4 and the Road Ahead - Flynn, Buoyant](https://www.youtube.com/watch?v=7U6nAxUxG6c). Covers Emissary-ingress version 4 and the project's future direction.
- **concept** · [Linkerd Update: Gateway API, Client-Specific Policy, Federated Services, Multicluster... Alex Leong](https://www.youtube.com/watch?v=aYGGnDDGX-Q)
- **concept** · [Redesigning Ingress: Docker’s Transition To the Next-Gen Gate... Kateryna Nezdolii & Ryan Hristovski](https://www.youtube.com/watch?v=Ea5OuNjpi9M)
- **concept** · [Istio: The Past, Present and Future of the Project and Communi... Lin Sun, Louis Ryan & Raymond Wong](https://www.youtube.com/watch?v=poBOYc_EkpA)
- **concept** · [Securing the Gateway: A Deep Dive Into Envoy Gateway's Advanced Security Pol... Huabing (Robin) Zhao](https://www.youtube.com/watch?v=x8wEo6ZDT1g)
- **concept** · [Debugging Envoy Tunnels: A Deep Dive - Carlos Sanchez & Alexandra Stoica, Adobe](https://www.youtube.com/watch?v=vrG5tBDsdd0)
- **concept** · [eBPF and Wasm: Unifying Userspace Extensions With Bpftime - Yusheng Zheng, eunomia-bpf](https://www.youtube.com/watch?v=W5C0O7vk78o)
- **concept** · [What's New in gRPC - Kevin Nilson, Google](https://www.youtube.com/watch?v=0qNOZpdW870). An update on new features and developments in the gRPC project.
- **concept** · [Scalable DNS With CoreDNS Plugins: A Deep Dive - Yong Tang, Ivanti & John Belamaric, Google](https://www.youtube.com/watch?v=W3f5Ks0j2Q8)
- **concept** · [How To Gateway With Ingress - 140 Days InGate - Marco Ebert & James Strong](https://www.youtube.com/watch?v=zTLbnstVjHc)
- **concept** · [Simplifying the Networking and Secur... Bill Mulligan, Anna Kapuścińska, Bowei Du & Amir Kheirkhahan](https://www.youtube.com/watch?v=kYT7KV_Cijs)
- **concept** · [Museum of Weird Bugs: Our Favorites From 8 Years of Service Mesh Debugging - Alex Leong, Buoyant](https://www.youtube.com/watch?v=Kcjh0-hXwWw)
- **concept** · [Making the Leap: What Gateway API Needs To Support Ingress-NGINX Users - Rob Scott & James Strong](https://www.youtube.com/watch?v=EeegJKZ_4g0)
- **concept** · [Uncharted Waters: Dynamic Resource Allocation for Networking - Miguel Duarte Barroso & Lionel Jouin](https://www.youtube.com/watch?v=PgCaIyeRn6Y)
- **concept** · [Project Lightning Talk: Kepler Project Updates - Sunyanan Choochotkaew, Maintainer](https://www.youtube.com/watch?v=0FrmlwV9D0Y). Lightning talk on recent updates to the Kepler energy-monitoring project.
- **concept** · [Project Lightning Talk: API Management in the CRD World: What Linkerd Has Learned - Phil Henderson](https://www.youtube.com/watch?v=5CyAZBUH1f8). Lightning talk on what Linkerd learned about managing APIs in a world of CRDs.
- **concept** · [Project Lightning Talk: What's New in Istio? - Mitch Connors, Maintainer](https://www.youtube.com/watch?v=B7lpXPZPFoI)
- **concept** · [Project Lightning Talk: What’s New in Kuma: Advanced Service Mesh Capabilities - Marcin Skalski](https://www.youtube.com/watch?v=rRExAhVI1nU)
- **concept** · [Lightning Talk: Extending Envoy With WebAssembly - Yuki Ito, newmo, Inc.](https://www.youtube.com/watch?v=bOhaJV3_7X4)
- **concept** · [C.A.L.L.I.N.G. Now I'm Calling You, Calling You Now - Mario Macías & Terra Tauri, Grafana Labs](https://www.youtube.com/watch?v=2BIhTXQd0CI). Grafana Labs speakers explain an observability approach that builds on OpenTelemetry and eBPF instrumentation.

### 2025 · [KubeCon + CloudNativeCon India 2025](../sources/PLj6h78yzYM2MEQTMX_LIOK1hrePHxLD6U.md)

- **concept** · [Back To the Basics - Service Mesh Fundamentals - Kannan Jayaprakasam & Pawan Bhardwaj, Google](https://www.youtube.com/watch?v=2EbwEYWiz74). Explains service mesh fundamentals and why and how to use one.
- **concept** · [Unlocking the Power of Kuma Service Mesh: Enhancing Reliability and D... Deepak Verma & Arpit Mishra](https://www.youtube.com/watch?v=W98f23NjodU)
- **concept** · [Effortless, Standardised Homelab Observability With eBPF - Goutham Veeramachaneni, Grafana Labs](https://www.youtube.com/watch?v=CzTdtlqcFhQ)
- **concept** · [Guard Your Network With Kyverno and Envoy - Sanskar Gurdasani & Swastik Gour](https://www.youtube.com/watch?v=XMtVHDTXD6c)
- **concept** · [High-Performance Cloud Networking With Calico and Vec... Shatakshi Mishra & Abed Mohammad Kamaluddin](https://www.youtube.com/watch?v=hPL4SWU894A)
- **concept** · [Enhancing DNS Reliability in Kubernetes With Node Local DN... Sanjay Kumar K K R & Priyanshi Agrawal](https://www.youtube.com/watch?v=ueMe_LLxfVI)
- **concept** · [Auto-instrumentation for GPU Performance Using eBPF - Annanay Agarwal, Grafana Labs](https://www.youtube.com/watch?v=eEBAFyLB9Zg)

### 2025 · [KubeCon + CloudNativeCon Japan 2025 (Tokyo)](../sources/PLj6h78yzYM2PsNdcBGWR_mVN-SRLQl6KM.md)

- **case study** · [BGP Peering Patterns for Kubernetes Networking at Preferred Networks - Sho Shimizu & Yutaro Hayakawa](https://www.youtube.com/watch?v=n7_I4zu6f_M) — Preferred
- **case study** · [From Moon Prism Power To eBPF Super Saiyan: A Guide To Cloud Native Se... Carla Gaggini & Kenta Tada](https://www.youtube.com/watch?v=SqD8jNJGweU)
- **concept** · [Access AI Models Anywhere: Scaling AI Traffic With Envoy AI Gateway - Dan Sun & Takeshi Yoneda](https://www.youtube.com/watch?v=xk1HsvVHMtA)
- **concept** · [Lightning Talk: Enhanced Service Redirection: eBPF Ensures the High Availability of N... Weizhou Lan](https://www.youtube.com/watch?v=D7N4FoeGxSc)
- **concept** · [Envoy Gateway Policies: Unlocking the Full Power of Envoy Proxy for API Gateways - Huabing Zhao](https://www.youtube.com/watch?v=_454exrrbMM)
- **concept** · [Project Lightning Talk: Understanding Cilium's eBPF kube-proxy Replacement for High... Yusuke Suzuki](https://www.youtube.com/watch?v=d62JtUt9Qts)
- **concept** · [Full Lifecycle API Management in Kubernetes With Envoy and WebAssem... Brandon Kang & Mostafa Radwan](https://www.youtube.com/watch?v=McMBwWPlYTE)

### 2025 · [KubeCon + CloudNativeCon North America 2025](../sources/PLj6h78yzYM2MLSW4tUDO2gs2pR5UpiD0C.md)

- **case study** · [Fast and the Furious: CICD Pipeline for eBPF Programs at Meta S... Theophilus Benson & Prankur Gupta](https://www.youtube.com/watch?v=wXuykaYSFCQ) — Meta
- **case study** · [TikTok's IPv6 Journey To Cilium: Pitfalls and Lessons Learned - Giri Kuncoro & Joseph Pallamidessi](https://www.youtube.com/watch?v=y0qlhiKtDGo)
- **case study** · [GAMMA in Action: How Careem Migrated To Istio Without Downtime - Suren Raju & Sergey Marunich](https://www.youtube.com/watch?v=igJXmbwMYAc) — Careem
- **concept** · [Fix First, Investigate Later: When an eBPF Rollout Brought Down Our... Zain Malik & Grzegorz Głąb](https://www.youtube.com/watch?v=J-Zx64mJzVk)
- **concept** · [Scaling and Securing CoreDNS: Performance and Resilience - Yong Tang & John Belamaric](https://www.youtube.com/watch?v=RodoZHYEXTY)
- **concept** · [Diagnosing Application Performance With EBPF, Pyroscope, and Kubernetes - Liam Mackie](https://www.youtube.com/watch?v=RrlF7OzCojE)
- **concept** · [Istio Project Updates: AI Inference, Ambient Multicluster & Default Deny - Keith Mattix, Microsoft](https://www.youtube.com/watch?v=vdCMLZ-4vUo)
- **concept** · [Gateway API: Table Stakes - Shane Utt, Candace Holman, Mike Morris, Lior Lieberman & Kellen Swain](https://www.youtube.com/watch?v=RWFDjA6ZeWc)
- **concept** · [Navigating the AI/ML Networking Maze in Kubernetes: Lessons From the Trenches - Antonio Ojea, Google](https://www.youtube.com/watch?v=liHY_dy-W0w)
- **concept** · [Beyond the Cloud(s): Falco’s Ascent in Performance and... Leonardo Grasso & Leonardo Di Giovanna](https://www.youtube.com/watch?v=5JoNk7_Sors). Falco project update on performance improvements and new capabilities.
- **concept** · [10 Years of Cilium: Connecting, Securing... Bill Mulligan, Paul Arah, Neha Aggarwal, Satish Krishnan](https://www.youtube.com/watch?v=mCKwX74xIs4)
- **concept** · [Routing Stateful AI Workloads in Kubernetes - Maroon Ayoub, IBM & Michey Mehta, Red Hat](../sources/videos/-C76naL3PRc.md). Explains why standard Kubernetes load balancing fails for stateful LLM inference and how llm-d's cache-aware routing fixes it, with benchmark data.
- **concept** · [QEMU in the Fast Lane: Accelerating KubeVirt Networking With... Daniel Borkmann & Anton Protopopov](https://www.youtube.com/watch?v=3X0X4az_E_4). Shows how to speed up KubeVirt networking by accelerating the QEMU data path with eBPF.
- **concept** · [On-Prem Load Balancing Reimagined: Serving 20 Million QPS With Gateway API and Envoy... Isaac Wilson](https://www.youtube.com/watch?v=kHChbblwVwk)
- **concept** · [Return of the Mesh: Gateway API's Epic Quest for Unity - Henrik Rexed, Dynatrace](https://www.youtube.com/watch?v=tgs6Wq5UlBs)
- **concept** · [Project Lightning Talk: Introducing k8gb: Kubernetes Native Global Load Balancing Mad... Yury Tsarev](https://www.youtube.com/watch?v=4rpPTWIV5DA). Lightning talk introducing k8gb, a Kubernetes-native global server load balancing project.
- **concept** · [Project Lightning Talk: Linkerd, mTLS, and Bungled Bundles - Flynn, Technical Evangelist](https://www.youtube.com/watch?v=PpV8tAbBvsU)
- **concept** · [Project Lightning Talk: Istio: Set Sailing With Istio Without Sidecars - Lin Sun](https://www.youtube.com/watch?v=SwB7W8g9r6I)
- **concept** · [Project Lightning Talk: OVN-Kubernetes: Scalable, Production-Grade Networking... Surya Seetharaman](https://www.youtube.com/watch?v=5SP7RS_DnIE). Project lightning talk on OVN-Kubernetes as a scalable, production-grade networking implementation for Kubernetes.
- **tutorial** · [Lightning Talk: Know Before You Go! Speedrun Intro To Gateway API - Christine Kim](https://www.youtube.com/watch?v=Cd0hGGydUGo)
- **tutorial** · [Don't Panic! A Beginner's Guide To K8s Debugging - Ivan Porta & Phil Henderson, Buoyant](https://www.youtube.com/watch?v=2fRRYcugOh4). Beginner's guide to debugging problems in Kubernetes clusters.

### 2026 · [KubeCon + CloudNativeCon + OpenInfra Summit + PyTorch Conference China 2026](../sources/PLGcxfZT6qI-w.md)

- **concept** · [Non-Invasive AI Agent Observability With OBI - Haibin Zhang, Alibaba Cloud & Endre Sara, Causely](https://www.youtube.com/watch?v=AWPjeQBZ9Eo). Shows non-invasive observability of AI agents using OpenTelemetry eBPF instrumentation (OBI).
- **concept** · [10 Years of Cilium: Connecting, Securing, and Simplifying the... Liyi Huang, Tingjin Ye & Yashi Su](https://www.youtube.com/watch?v=pg2ZXH9rAqE)
- **concept** · [Behind the Scenes of Building a Gateway API Dataplane... Norwin Schnyder & Huabing (Robin) Zhao](https://www.youtube.com/watch?v=1pF7IKAzr3U). Behind-the-scenes look at designing and building a Gateway API dataplane.

### 2026 · [KubeCon + CloudNativeCon Europe 2026](../sources/PLj6h78yzYM2MXCOWSN9CqqID6OOvF7wxL.md)

- **case study** · [An Immersive and Visual Journey Into Kubernetes Networking - Benoit Entzmann, Feesh](https://www.youtube.com/watch?v=Xtjpdy8OmQQ) — Feesh
- **case study** · [From NLB Sprawl To Mesh Efficiency: How Skyscanner Handles 60M Reque... John Clark & Steven Thwaites](https://www.youtube.com/watch?v=2ZvvGdHfknM) — Skyscanner. Skyscanner describes moving from NLB sprawl to a mesh to handle 60M requests efficiently.
- **case study** · [Gateway API: Bridging the Gap from Ingress to the Future - Panel](https://www.youtube.com/watch?v=_4JkNbuA2Gg)
- **concept** · [Cloud Native Theater | Istio Day: The Good, The Ugly, and The Bad... Alfonso Ming and Jorge Turrado](https://www.youtube.com/watch?v=ToKv7JntLvY)
- **concept** · [Cloud Native Theater | Istio Day: Running State of the Art Inference... Jackie Maertens and Nili Guy](https://www.youtube.com/watch?v=dr03NZmau5g)
- **concept** · [Cloud Native Theater | Istio Day: Zero-Downtime Migration from ingress-nginx to Isti... Joe Abellard](https://www.youtube.com/watch?v=wix_PfQ61jY)
- **concept** · [Cloud Native Theater | EnvoyCon: External Processing, Internal Leverage: MCP Tool Calls... Jens Kat](https://www.youtube.com/watch?v=4XciSKk-Rek). Shows how Envoy external processing can be used to handle MCP tool calls.
- **concept** · [Cloud Native Theater | EnvoyCon: The Future of AI Traffic: What's New in Envoy AI Tra... Xiaolin Lin](https://www.youtube.com/watch?v=7OkSrMBirmc). Presents new features and the direction of Envoy AI Gateway for managing AI traffic.
- **concept** · [Cloud Native Theater | EnvoyCon: Inside Spotify’s Envoy Architecture: What We Le... Leonardo da Mata](https://www.youtube.com/watch?v=CAn22mnA6kE)
- **concept** · [Cloud Native Theater | EnvoyCon: The Next Generation of Envoy Extensibility: Dynami... Rohit Agrawal](https://www.youtube.com/watch?v=ScMu2-ILhvg)
- **concept** · [Cloud Native Theater | EnvoyCon: From ingress-nginx to Envoy Gateway at Zapier: The... Kalen Wessel](https://www.youtube.com/watch?v=kIj2U13VZJY)
- **concept** · [Project Lightning Talk: Envoy Today: What’s New In Managing Cloud-Native And AI Workl... Karol Szwaj](https://www.youtube.com/watch?v=g3CHzGl2zS0)
- **concept** · [Project Lightning Talk: Optimize Sidecarless Service Mesh With A Brand-New Rust-Base... Zengzeng Yao](https://www.youtube.com/watch?v=knX673N1jKM)
- **concept** · [Project Lightning Talk: MCP Routing In Linkerd - Flynn, Technical Evangelist](https://www.youtube.com/watch?v=tb8rSQz1MGE)
- **concept** · [Envoy in the Era of Agentic Workloads - Yan Avlasov, Google & Erica Hughberg, Tetrate](https://www.youtube.com/watch?v=HvX4nGkhfZw)
- **concept** · [Project Lightning Talk: Translating Ebpf Into Business Value: Lessons From The Cili... Bill Mulligan](https://www.youtube.com/watch?v=J4jHq2ExjJo)
- **concept** · [Tailor Made: Dynamic Fine-Grained Authorization for API Traffic - Erica Hughberg & Andres Aguiar](https://www.youtube.com/watch?v=A1FXOwUmA6M). Shows dynamic fine-grained authorization for API traffic at the gateway.
- **concept** · [Navigating the Gateway API Maze: 40+ Implementations, 55+ Features... Beka Modebadze & Christine Kim](https://www.youtube.com/watch?v=aBoqH0wf4Yk)
- **concept** · [Signed, Sealed, Delivered: Why Reverse Proxies Outperform VPNs - Peter O'Neill & Boris Kurktchiev](https://www.youtube.com/watch?v=0tq06AAdKWQ). Argues that reverse proxies outperform VPNs for secure access and explains why.
- **concept** · [Evolution or Revolution: Istio as the Network Platform for Cloud Nat... Mitch Connors & Daniel Grimm](https://www.youtube.com/watch?v=4K6s5y8HoBc). Considers whether Istio's evolution is evolutionary or revolutionary as a cloud native network platform.
- **concept** · [Hacking GPU Observability: eBPF & Ephemeral Containers in Action on Kubernetes - Brandon Kang](https://www.youtube.com/watch?v=mkH38O3wLog)
- **concept** · [BoF | Beyond Nginx Ingress: Higress as the K8s Gateway for the AI Era](https://www.youtube.com/watch?v=FURcBVNuK0U)
- **concept** · [Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF - Zahari Dichev](https://www.youtube.com/watch?v=J61kV92bSt0)
- **concept** · [Agentic Networking: Securing AI Agents on Kubernetes - Haiyan Meng, Google & Evaline Ju, IBM](https://www.youtube.com/watch?v=KXmPxmNN0fc)
- **concept** · [Linkerd: Reliable Production in an AI/MCP World - William Morgan, Buoyant](https://www.youtube.com/watch?v=jPWsMZFpihA)
- **concept** · [Rust Vs. Go: Building a Container Network Stack From Scratch - Matt Heon & Shivang K Raghuvanshi](https://www.youtube.com/watch?v=05wBWDa8W-g). Compares Rust and Go for building a container network stack from scratch.
- **concept** · [Real-World Supply-Chain Security - Alex Leong, Buoyant](https://www.youtube.com/watch?v=1Pd28J4kpN8). Covers practical supply-chain security measures and threats, from the Buoyant perspective.
- **concept** · [Not Yet Another Envoy Implementation - Exploring Kgateway To Write Your Own GatewayA... Ricardo Katz](https://www.youtube.com/watch?v=9VqzQgin6vk). Explores using kgateway to build your own Gateway API implementation.
- **concept** · [Building the Next Generation of Multi-Cluster with Gateway API - Mike Morris & Alan Grosskurth](https://www.youtube.com/watch?v=oRbdcHgHPbo)
- **concept** · [10 Years of Cilium: Connecting, Securing, and Simplifying the... Bill M, Paul A, Marcelo M & Neha A](https://www.youtube.com/watch?v=EN_77SkK5jg)
- **concept** · [When DNS Blinks: Scaling and Hardening CoreDNS in Critical Cloud Infra... Yong Tang & John Belamaric](https://www.youtube.com/watch?v=9UIPskZ07dY). Covers how to scale and harden CoreDNS for critical cloud infrastructure.
- **concept** · [SIG Network: The State of Networking for AI on Ku... David M, Haiyan M, Bowei D & Kellen S & Nadia P](https://www.youtube.com/watch?v=DO1PVnly9cU)
- **concept** · [Istio's Ambient Mesh: The Real Cost of Sidecar-less Tracing - Mofesola Babalola & Hannah Olukoye](https://www.youtube.com/watch?v=wI9a3GuJw7U)
- **concept** · [DNS Tracing & Metrics Via eBPF in OpenTelemetry- Endre Sara, Causely & Nikola Grcevski, Grafana Labs](https://www.youtube.com/watch?v=YMqSK6uBhxU)
- **tutorial** · [Tutorial: Attack Defense: Leverage eBPF To Reveal Attack Flows... Constanze R, Markus G & Teodor P](https://www.youtube.com/watch?v=VA-ne25QX9g)
- **panel** · [Cloud Native Theater | Istio Day: Panel: Horrors and Successes of Running Istio in Production](https://www.youtube.com/watch?v=-Z9zvo6leRY). Istio Day panel on the horrors and successes of running Istio in production.

### 2026 · [KubeCon + CloudNativeCon India 2026](../sources/PLj6h78yzYM2PmaTdAzefPqjawTlop1lgG.md)

- **case study** · [Zero Trust for Fintech: Building Secure Banking Infrastructure Wit... Prasta Maha & Herbert Sianturi](https://www.youtube.com/watch?v=3zr_smC81Ec). Describes building secure zero-trust banking infrastructure for fintech on cloud native tooling.
- **concept** · [Service Networking Within Air-Gapped Environments: Deployment Strategies and Operat... Anirban Nandi](https://www.youtube.com/watch?v=Zvg2JWvc_oY)
- **concept** · [When Kubeflow Fights Cilium: Debugging 60% Idle GPUs... Ramkumar Nagaraj & Bingi Narasimha Karthik](https://www.youtube.com/watch?v=BG9XGouyM9c)

### 2026 · [KubeCon + CloudNativeCon Japan 2026](../sources/PLH1zduub3WrE.md)

- **case study** · [The Road To Cilium: Migrating 150+ Kubernetes Clusters at Airbnb - Yifei Sun, Airbnb](https://www.youtube.com/watch?v=LX4YZeqXWck) — Airbnb
- **case study** · [Runtime Security at Scale With EBPF: Hybrid Detection and Root Cause… Y. Krishna Kota & R. Waghare](https://www.youtube.com/watch?v=wpIoiYAwMmA)
- **case study** · [I Tested 7 So You Only Need 1: Your First Gateway API Migration in 5 Minutes - Hoon Jo](https://www.youtube.com/watch?v=lne3bX2FOnA)
- **concept** · [Beyond Wasm: How Dynamic Modules Let You Extend Envoy Proxy in Go, Rust, or… R. Agrawal & T. Yoneda](https://www.youtube.com/watch?v=qvSrzTC7RL8)
- **concept** · [Dynamic Modules in Envoy Gateway: API Design, Safety, and Operability - K. Kimura & H. (Robin) Zhao](https://www.youtube.com/watch?v=j7zSa_XiGzE)
- **concept** · [A Practical, Research‑Backed Introduction To Cloud‑Native Kernel‑Bypass Networking - K. Yasukata](https://www.youtube.com/watch?v=3T44otf6d_k). A research-backed introduction to kernel-bypass networking in cloud-native environments.
- **concept** · [Running Wasm Inside Your Storage Cluster With CSI and Gateway API - Ho Kim & SangJoon Park](https://www.youtube.com/watch?v=K6_KQm1lMn8)
- **concept** · [Detecting Compromised CI With eBPF and Cilium Tetragon - Liz Rice, Isovalent at Cisco](https://www.youtube.com/watch?v=IbitBG6bbsM)
- **concept** · [A Decade of Cilium Around the World - Liz Rice, Isovalent at Cisco & Hiroki Hanada, Cybozu, Inc.](https://www.youtube.com/watch?v=TrXfYqUKjeI)
- **concept** · [Beyond Power and Magic: Forging Stable eBPF Tools for the Post-Demon King Era - K. Tada & C. Gaggini](https://www.youtube.com/watch?v=v7VRjJa2mO8)

### 2026 · [Sneak Peek: KubeCon + CloudNativeCon North America 2026](../sources/PLHklxv-Cu3dQ.md)

- **other** · [Meet William Morgan - Speaker at KubeCon + CloudNativeCon North America](https://www.youtube.com/watch?v=-qbCNPXF0ps). A short sneak-peek promo introducing speaker William Morgan for KubeCon North America.
