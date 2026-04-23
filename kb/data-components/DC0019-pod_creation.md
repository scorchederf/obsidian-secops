---
mitre_id: "DC0019"
mitre_name: "Pod Creation"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--5263cb33-08cc-4a68-820f-004e1e400d76"
mitre_created: "2021-10-20T15:05:19.272Z"
mitre_modified: "2025-10-21T15:14:37.749Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# DC0019: Pod Creation

The initial deployment or instantiation of a new pod in a containerized environment. This includes creating a pod manually, through orchestration tools (Kubernetes), or via Infrastructure-as-Code (IaC) configurations. A Pod is the smallest deployable unit in Kubernetes, typically containing one or more containers. Creation methods include:
- Direct pod deployment (`kubectl run`, `kubectl apply`)
- Automated deployment via CI/CD pipelines (e.g., ArgoCD, Jenkins, GitOps)
- Infrastructure-as-Code (IaC) templates (e.g., Terraform, Helm Charts)
- API-based deployments via Kubernetes control plane (create_pod API calls)
- Pods can be ephemeral (short-lived) or persistent (part of a StatefulSet or Deployment).

*Data Collection Measures:*

- Kubernetes Audit Logs
    - Captures all API requests, including pod `create` events.
- Kube-api server Logs	
    - Monitors API calls related to pod deployments and modifications. Related Events: `PodSandboxChanged`, `SyncLoop`, `Created pod`
- Container Runtime Logs	
    - Logs from CRI-O, containerd, or Docker capture pod creation events. Related Events: `container start`, `container create`
- Cloud Provider Logs	
    - GKE, EKS, AKS logs provide insights into Kubernetes API interactions.
- SIEM & Log Aggregation	
    - Integrates Kubernetes logs into SIEM solutions.
- EDR/XDR Solutions	
    - Monitors container-based activity for anomalous pod creations.

