---
mitre_id: "DC0091"
mitre_name: "Container Enumeration"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--91b3ed33-d1b5-4c4b-a896-76c55eb3cfd8"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
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

"Container Enumeration" data component captures events and actions related to listing and identifying active or available containers within a containerized environment. This includes information about running, stopped, or configured containers, such as their names, IDs, statuses, or associated images. Monitoring this activity is crucial for detecting unauthorized discovery or reconnaissance efforts. Examples: 

- Docker Example: `docker ps`, `docker ps -a`
- Kubernetes Example: `kubectl get pods`, `kubectl get deployments`
- Cloud Container Services Example
    - AWS ECS: API Call: ListTasks or ListContainers
    - Azure Kubernetes Service: API Call: List pod or container instances.
    - Google Kubernetes Engine (GKE): API Call: Retrieve deployments and their associated containers.

## Workspace

- [[workspaces/attack/data-components/DC0091-container_enumeration-note|Open workspace note]]

![[workspaces/attack/data-components/DC0091-container_enumeration-note]]

