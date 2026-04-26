---
mitre_id: "T1613"
mitre_name: "Container and Resource Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0470e792-32f8-46b0-a351-652bc35e9336"
mitre_created: "2021-03-31T14:26:00.848Z"
mitre_modified: "2025-10-24T17:48:20.661Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1613/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to discover containers and other resources that are available within a containers environment. Other resources may include images, deployments, pods, nodes, and other information such as the status of a cluster.

These resources can be viewed within web applications such as the Kubernetes dashboard or can be queried via the Docker and Kubernetes APIs.(Citation: Docker API)(Citation: Kubernetes API) In Docker, logs may leak information about the environment, such as the environment’s configuration, which services are available, and what cloud provider the victim may be utilizing. The discovery of these resources may inform an adversary’s next steps in the environment, such as how to perform lateral movement and which methods to utilize for execution. 

## Workspace

- [[workspaces/attack/techniques/T1613-container_and_resource_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1613-container_and_resource_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/ea2255df_d781_493b_9693_ac328f9afc3f-docker_container_and_resource_discovery|Docker Container and Resource Discovery (sh; containers)]]
- [[kb/atomic/tests/fc631702_3f03_4f2b_8d8a_6b3d055580a1-podman_container_and_resource_discovery|Podman Container and Resource Discovery (sh; containers)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]

## Tools

- [[peirates|Peirates (S0683)]]

## Platforms

- Containers

