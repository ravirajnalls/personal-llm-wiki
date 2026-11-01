---
title: Horizontal Pod Autoscaler case studies and implementations
summary: How the Kubernetes HPA decides replica counts, and how Deezer and Alibaba Cloud's EDAS extended it with custom metrics and KEDA.
tags: [kubernetes, autoscaling, hpa, keda, case-study]
updated: 2026-11-01
---

# Horizontal Pod Autoscaler case studies and implementations

> The Kubernetes HPA scales replicas by comparing a current metric to a target, and the two case studies here (Deezer, Alibaba Cloud EDAS) both went beyond CPU and memory: Deezer with a custom Node.js metric, Alibaba with KEDA.

## Summary

The Horizontal Pod Autoscaler (HPA) is the Kubernetes controller that adds or removes pod replicas based on a metric. Its core rule is a ratio between the desired and current metric value ([kubernetes.io](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#:~:text=From%20the%20most%20basic%20perspective%2C%20the%20HorizontalPodAutoscaler%20controller)).

Two real-world implementations show where the defaults fall short. Deezer built a Prometheus-based pipeline around a custom load metric ([infoq.com](https://www.infoq.com/news/2024/10/deezer-kubernetes-autoscaling#:~:text=Noting%20that%20scaling%20applications%20to%20the%20correct%20size)). Alibaba Cloud's EDAS platform standardized on KEDA ([cncf.io](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling/#:~:text=Posted%20on%20March%2030%2C%202021%20by%20Yan%20Xun%2C)).

Limits of coverage: the sources are one news write-up (InfoQ, 2024), one vendor blog (CNCF, 2021), the Kubernetes docs and one conference talk. They are not independent measurements.

## Key ideas

**CPU and memory can react too slowly.** Relying on CPU and memory can delay scaling during sudden traffic spikes, which is why KEDA or custom metrics are suggested for faster response ([infoq.com](https://www.infoq.com/news/2024/10/deezer-kubernetes-autoscaling#:~:text=Further%20emphasising%20the%20value%20of%20using%20custom%20metrics%2C)).

**Pick a metric that tracks real load.** Deezer found that event loop utilization (ELU, how busy a Node.js event loop is) represents server load better than CPU percentage ([infoq.com](https://www.infoq.com/news/2024/10/deezer-kubernetes-autoscaling#:~:text=Noting%20that%20scaling%20applications%20to%20the%20correct%20size)).

**Scale to zero is not native to the HPA.** Alibaba's team listed missing scale-to-zero as a gap, since many users want it when a microservice is not being consumed ([cncf.io](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling/#:~:text=No%20support%20for%20scale-to-zero%20Many%20users%20have%20the)). KEDA aims to cover this by supporting scale-to-zero ([cncf.io](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling/#:~:text=You%20could%20use%20Prometheus%20and%20use%20tools%2C%20such)).

## How it works

**The core calculation.** The controller compares desired and current metric values. For example, a current value of 200m against a desired 100m doubles the replica count ([kubernetes.io](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#:~:text=From%20the%20most%20basic%20perspective%2C%20the%20HorizontalPodAutoscaler%20controller)).

**Metric sources.** The HPA reads the resource metrics API for CPU and memory and a custom metrics API for others. Custom metrics are served through an adapter component ([▶ 28:22](https://www.youtube.com/watch?v=1xm_ccAYO90&t=1702s)). This is the 2018 design talk by Maciej Pytel and Solly Ross, so details may have changed since.

**Damping flapping.** When several recommendations arise, the controller can pick the highest within a configurable window, to avoid rapid downscaling ([kubernetes.io](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#:~:text=If%20multiple%20metrics%20are%20specified%20in%20a%20HorizontalPodAutoscaler%2C)). The `behavior` field sets this per HPA, for example a 300-second `scaleDown` stabilization window ([kubernetes.io](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#:~:text=The%20stabilization%20window%20is%20used%20to%20restrict%20the)).

**Case study: Deezer.** Deezer collects metrics with Prometheus and uses the Prometheus Adapter to expose them to Kubernetes. Its custom metric is ELU ([infoq.com](https://www.infoq.com/news/2024/10/deezer-kubernetes-autoscaling#:~:text=Noting%20that%20scaling%20applications%20to%20the%20correct%20size)). The team is now exploring KEDA for more flexibility ([infoq.com](https://www.infoq.com/news/2024/10/deezer-kubernetes-autoscaling#:~:text=While%20the%20custom%20metric-based%20autoscaling%20has%20proven%20beneficial%2C)).

**Case study: Alibaba Cloud EDAS.** EDAS required scale-to-zero out of the box. After evaluation, the team picked KEDA, which brings useful scalers ([cncf.io](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling/#:~:text=Base%20on%20the%20use%20cases%2C%20the%20EDAS%20team)). KEDA creates its own HPA objects, and the name length is limited to 63 characters ([cncf.io](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling/#:~:text=When%20creating%20KEDA%20HPA%2C%20the%20length%20of%20the)).

## Open questions

- Neither case study publishes before/after numbers such as replica counts, cost or latency in the text ingested here.
- Alibaba says it is working on AIOps-driven autoscaling decisions based on historical data, with no results reported ([cncf.io](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling/#:~:text=As%20the%20next%20step%2C%20Alibaba%20is%20actively%20working)).

## Disagreements

Deezer reports that custom-metric HPA scaling has been beneficial, yet is still looking at KEDA ([infoq.com](https://www.infoq.com/news/2024/10/deezer-kubernetes-autoscaling#:~:text=While%20the%20custom%20metric-based%20autoscaling%20has%20proven%20beneficial%2C)). Alibaba, by contrast, went all the way to KEDA ([cncf.io](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling/#:~:text=Posted%20on%20March%2030%2C%202021%20by%20Yan%20Xun%2C)). Alibaba also lists KEDA drawbacks: triggers cannot be disabled, which may cause trouble in production ([cncf.io](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling/#:~:text=When%20creating%20KEDA%20HPA%2C%20the%20length%20of%20the)).

## References

**Videos**

1. [Horizontal Pod Autoscaler Reloaded - Scale on Custom Metrics - Maciej Pytel & Solly Ross (CNCF [Cloud Native Computing Foundation])](https://www.youtube.com/watch?v=1xm_ccAYO90), cited at [28:22](https://www.youtube.com/watch?v=1xm_ccAYO90&t=1702s)

**Web**

1. [kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale)
2. [Deezer Optimizes Kubernetes Autoscaling with Custom Metrics ](https://www.infoq.com/news/2024/10/deezer-kubernetes-autoscaling) — infoq.com
3. [cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling](https://www.cncf.io/blog/2021/03/30/why-alibaba-cloud-uses-keda-for-application-autoscaling)
