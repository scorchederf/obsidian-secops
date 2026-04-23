---
mitre_id: "T1609"
mitre_name: "Container Administration Command"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7b50a1d3-4ca7-45d1-989d-a6503f04bfe1"
mitre_created: "2021-03-29T16:39:26.183Z"
mitre_modified: "2025-10-24T17:48:59.945Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1609/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
mitre_tactic_ids:
  - "TA0002"
---

# T1609: Container Administration Command

Adversaries may abuse a container administration service to execute commands within a container. A container administration service such as the Docker daemon, the Kubernetes API server, or the kubelet may allow remote management of containers within an environment.(Citation: Docker Daemon CLI)(Citation: Kubernetes API)(Citation: Kubernetes Kubelet)

In Docker, adversaries may specify an entrypoint during container deployment that executes a script or command, or they may use a command such as `docker exec` to execute a command within a running container.(Citation: Docker Entrypoint)(Citation: Docker Exec) In Kubernetes, if an adversary has sufficient permissions, they may gain remote execution in a container in the cluster via interaction with the Kubernetes API server, the kubelet, or by running a command such as `kubectl exec`.(Citation: Kubectl Exec Get Shell)

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Tools

- [[peirates|Peirates]]

## Platforms

- Containers

