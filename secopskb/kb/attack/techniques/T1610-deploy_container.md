---
mitre_id: "T1610"
mitre_name: "Deploy Container"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--56e0d8b8-3e25-49dd-9050-3aa252f5aa92"
mitre_created: "2021-03-29T16:51:26.020Z"
mitre_modified: "2025-10-24T17:48:49.017Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1610/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
mitre_tactic_ids:
  - "TA0005"
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may deploy a container into an environment to facilitate execution or evade defenses. In some cases, adversaries may deploy a new container to execute processes associated with a particular image or deployment, such as processes that execute or download malware. In others, an adversary may deploy a new container configured without network rules, user limitations, etc. to bypass existing defenses within the environment. In Kubernetes environments, an adversary may attempt to deploy a privileged or vulnerable container into a specific node in order to [[T1611-escape_to_host|T1611: Escape to Host]] and access other containers running on the node. (Citation: AppSecco Kubernetes Namespace Breakout 2020)

Containers can be deployed by various means, such as via Docker's `create` and `start` APIs or via a web application such as the Kubernetes dashboard or Kubeflow. (Citation: Docker Containers API)(Citation: Kubernetes Dashboard)(Citation: Kubeflow Pipelines) In Kubernetes environments, containers may be deployed through workloads such as ReplicaSets or DaemonSets, which can allow containers to be deployed across multiple nodes.(Citation: Kubernetes Workload Management) Adversaries may deploy containers based on retrieved or built malicious images or from benign images that download and execute malicious payloads at runtime.(Citation: Aqua Build Images on Hosts)

## Workspace

- [[workspaces/attack/techniques/T1610-deploy_container-note|Open workspace note]]

![[workspaces/attack/techniques/T1610-deploy_container-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]
- [[M1047-audit|M1047: Audit]]

## Tools

- [[peirates|Peirates (S0683)]]

## Platforms

- Containers

