---
mitre_id: "DC0037"
mitre_name: "Pod Enumeration"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--07688e40-a7fa-4436-937f-1216674341a0"
mitre_created: "2021-10-20T15:05:19.272Z"
mitre_modified: "2025-10-21T15:14:40.544Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Extracting a list of running or existing pods within a containerized cluster environment. Pods are the smallest deployable units in a Kubernetes cluster and typically represent an application or workload. Enumeration of pods provides insight into the structure and state of applications running in the cluster, such as the names of pods, their namespaces, and their associated metadata.

*Data Collection Measures:*

- Kubernetes API Server Audit Logs:
    - Enable Audit Logging in Kubernetes to capture API requests, such as GET `/api/v1/pods`.
- Container Runtime Logs:
    - Collect runtime-level logs from tools like CRI-O, containerd, or Docker, which might show relevant API calls for pod enumeration.
- EDR and SIEM:
    - Endpoint Detection and Response (EDR) tools, if configured with cluster-level visibility, can monitor user commands like `kubectl get pods`.
    - SIEM platforms (e.g., Splunk) can ingest Kubernetes API logs to detect enumeration patterns.
- Host-Based Monitoring:
    - Monitor processes and commands executed on nodes where `kubectl` is installed using tools like auditd, Sysmon for Linux, or kernel modules.

## Workspace

- [[workspaces/attack/data-components/DC0037-pod_enumeration-note|Open workspace note]]

![[workspaces/attack/data-components/DC0037-pod_enumeration-note]]

