---
title: "Project Lightning Talk: kcp: Scaling The Kubernetes Control Plane For The Multi-Clust... Jan Willies"
video: -GJgzn3pyvM
kind: concept
orgs: []
topics: ["kcp", "multi-tenancy", "control plane", "crds", "kubernetes api", "workspaces"]
---

# Project Lightning Talk: kcp: Scaling The Kubernetes Control Plane For The Multi-Clust... Jan Willies

concept · 5:14 · [Watch on YouTube](https://www.youtube.com/watch?v=-GJgzn3pyvM)

Playlists: [KubeCon + CloudNativeCon Europe 2026](../PLj6h78yzYM2MXCOWSN9CqqID6OOvF7wxL.md), [KubeCon + CloudNativeCon Europe 2026 - Project Lightning Talks](../PLj6h78yzYM2MAvQHOQsuMVA-LRuR7A_d1.md)

> Lightning talk introducing kcp, a horizontally scalable lightweight Kubernetes-style control plane that gives isolated API experiences without full clusters.

Topics: `kcp`, `multi-tenancy`, `control plane`, `crds`, `kubernetes api`, `workspaces`

## Transcript

[▶ 0:00](https://www.youtube.com/watch?v=-GJgzn3pyvM&t=0s) Hi, my name is Jan Viegas. I work for a company called Accenture and today I'll be presenting about the KCP project. So, basically the problem [clears throat] statement in Kubernetes is a bit and I'm sure many of you have been there already. When I want something in Kubernetes a space for me, myself, the team, I either have something called a namespace and have projects around the namespace who promise me to do like namespace on steroids to have a isolated account at Kubernetes or I get the full Kubernetes cluster experience via an isolated

[▶ 0:44](https://www.youtube.com/watch?v=-GJgzn3pyvM&t=44s) own tenant. And while a namespace is very quick to provision, a full Kubernetes cluster with if additionally have some opinion about it is from like even from a managed cloud provider half an hour to an hour so it's very heavy as an account and it shouldn't be heavy. So, being coming back to the roots here, what if we have both of that? So, we have a lightweight Kubernetes API and still have the full isolated experience. >> [clears throat] >> So, basically true isolation without the infrastructure backing it. And

[▶ 1:29](https://www.youtube.com/watch?v=-GJgzn3pyvM&t=89s) a vanilla Kubernetes cluster has around 80 built-in resources last time I checked and for a use case where you are working with extending Kubernetes and like doubling down on CRDs, that is a lot and a lot of stuff you don't need for that. So, basically have a bit of a lightweight API server which which can be provisioned in seconds. So, that exactly is the KCP project. KCP is an open source horizontally scalable control plane for Kubernetes like APIs and that provides isolated Kubernetes endpoints. And an endpoint in

[▶ 2:12](https://www.youtube.com/watch?v=-GJgzn3pyvM&t=132s) in KCP is called a workspace and what you get with a workspace is basically a full-blown Kubernetes API without all the workload and infrastructure stuff. So, there are no nodes, no pods, no deployments, nothing like that. And inside a workspace you are cluster admin. So, you are basically in your in your own account and you can do whatever you want. And KCP serves as the as the housing around it. So, when you create a workspace it's up there in in literally a second and it allows you to do to um well, yeah, to control everything, not

[▶ 2:56](https://www.youtube.com/watch?v=-GJgzn3pyvM&t=176s) just the non-namespace stuff on the just the namespace stuff. And since it's a Kubernetes like API you can use all the familiar tools to access it like kubectl, helm, basically everything which is based on client go. Oops. So, it's a single binary. It's it's in go written and it's compiled to a single binary. So, you can just run it on on your laptop or on on a managed service or of course on Kubernetes as well to play around with it but it is also can be deployed as a global control plane with multi-region support with many caching layers

[▶ 3:39](https://www.youtube.com/watch?v=-GJgzn3pyvM&t=219s) and aggregate APIs um based on the on the deployment infrastructure. And what really shines about KCP is the mechanism to deal with CRDs. So, I'm not sure [clears throat] how many of you have run into the issue when upgrading a CRD from V1 alpha 1 to V alpha 2 and there's a breaking change in between and you thought ah well, I'll just have a different API version and that's sure is enough. Well, not in Kubernetes but KCP solves exactly this problem. So, you get mechanism for dealing with different different CRDs and different CRD versions. For example, version upgrades

[▶ 4:23](https://www.youtube.com/watch?v=-GJgzn3pyvM&t=263s) or the controllers who are backing that. Basically, what you can do is have the V1 alpha 1 served by a different controller than the V1 alpha 2. You can also have a different name for your API which you export in in KCP than in the different in the backing cluster. So, if that's spiked your attention, then there's more on KCP on this conference. Um Yeah, the first one is is rightly going into the CVE which we discovered. So, um but the other ones on Wednesday they go deeper into the project themselves. And that's it. Thank you very much.

[▶ 5:10](https://www.youtube.com/watch?v=-GJgzn3pyvM&t=310s) >> Awesome. Thank you. >> [applause]
