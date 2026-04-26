---
mitre_id: "DC0083"
mitre_name: "Cloud Service Enumeration"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--8c826308-2760-492f-9e36-4f0f7e23bcac"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Cloud service enumeration involves listing or querying available cloud services in a cloud control plane. This activity is often performed to identify resources such as virtual machines, storage buckets, compute clusters, or other services within a cloud environment. Examples include API calls like `AWS ECS ListServices`, `Azure ListAllResources`, or `Google Cloud ListInstances`. Examples: 

AWS Cloud Service Enumeration: The adversary gathers details about existing ECS services to identify opportunities for privilege escalation or exfiltration.
- Azure Resource Enumeration: The adversary collects information about virtual machines, resource groups, and other Azure assets for reconnaissance purposes.
- Google Cloud Resource Enumeration: The attacker seeks to map the environment and find misconfigured or underutilized resources for exploitation.
- Office 365 Service Enumeration: The attacker may look for data repositories or collaboration tools to exfiltrate sensitive information.

## Workspace

- [[workspaces/attack/data-components/DC0083-cloud_service_enumeration-note|Open workspace note]]

![[workspaces/attack/data-components/DC0083-cloud_service_enumeration-note]]

