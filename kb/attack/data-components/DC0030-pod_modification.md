---
mitre_id: "DC0030"
mitre_name: "Pod Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--672b2ebd-4310-4efe-bf03-7ab005298a74"
mitre_created: "2021-10-20T15:05:19.272Z"
mitre_modified: "2025-10-21T15:10:28.402Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

# DC0030: Pod Modification

Changes made to a pod’s configuration or control data within a containerized cluster. This can include updating settings such as resource limits, environment variables, annotations, labels, or even the containers running within the pod. Pod modifications are often executed using commands like kubectl set, kubectl patch, or kubectl edit.

*Data Collection Measures:* 

- Kubernetes API Server Audit Logs:
    - Capture all API calls related to pod modification, such as PATCH, PUT, or UPDATE methods on v1/pods.
- Runtime Security Tools:
    - Tools like Falco, Sysdig, and Kube-bench can monitor pod modifications at runtime and alert on policy violations.
- Container Orchestration Logs:
    - Monitor events logged by Kubernetes itself (e.g., `kubectl logs -n kube-system kube-controller-manager`).
- SIEM and EDR Solutions:
    - Use SIEM platforms (e.g., Splunk) to aggregate API server logs and detect patterns of unauthorized or suspicious pod modifications.
    - Endpoint Detection and Response (EDR) tools configured with container visibility can monitor commands like `kubectl` set or `kubectl patch`.
- Host-Based Monitoring:
    - Collect and analyze logs for processes executing `kubectl` commands or interacting with Kubernetes configuration files (e.g., `.kube/config`).

## Workspace

- [[kb/notes/attack/data-components/dc0030-notes|Open workspace note]]

