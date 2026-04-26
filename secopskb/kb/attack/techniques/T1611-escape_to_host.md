---
mitre_id: "T1611"
mitre_name: "Escape to Host"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4a5b7ade-8bb5-4853-84ed-23f262002665"
mitre_created: "2021-03-30T17:38:34.277Z"
mitre_modified: "2025-10-24T17:48:44.317Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1611/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "Containers"
  - "ESXi"
mitre_tactic_ids:
  - "TA0004"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may break out of a container or virtualized environment to gain access to the underlying host. This can allow an adversary access to other containerized or virtualized resources from the host level or to the host itself. In principle, containerized / virtualized resources should provide a clear separation of application functionality and be isolated from the host environment.(Citation: Docker Overview)

There are multiple ways an adversary may escape from a container to a host environment. Examples include creating a container configured to mount the host’s filesystem using the bind parameter, which allows the adversary to drop payloads and execute control utilities such as cron on the host; utilizing a privileged container to run commands or load a malicious kernel module on the underlying host; or abusing system calls such as `unshare` and `keyctl` to escalate privileges and steal secrets.(Citation: Docker Bind Mounts)(Citation: Trend Micro Privileged Container)(Citation: Intezer Doki July 20)(Citation: Container Escape)(Citation: Crowdstrike Kubernetes Container Escape)(Citation: Keyctl-unmask)

Additionally, an adversary may be able to exploit a compromised container with a mounted container management socket, such as `docker.sock`, to break out of the container via a [[T1609-container_administration_command|T1609: Container Administration Command]].(Citation: Container Escape) Adversaries may also escape via [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]], such as exploiting vulnerabilities in global symbolic links in order to access the root directory of a host machine.(Citation: Windows Server Containers Are Open)

In ESXi environments, an adversary may exploit a vulnerability in order to escape from a virtual machine into the hypervisor.(Citation: Broadcom VMSA-2025-004)

Gaining access to the host may provide the adversary with the opportunity to achieve follow-on objectives, such as establishing persistence, moving laterally within the environment, accessing other containers or virtual machines running on the host, or setting up a command and control channel on the host.

## Workspace

- [[workspaces/attack/techniques/T1611-escape_to_host-note|Open workspace note]]

![[workspaces/attack/techniques/T1611-escape_to_host-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/0b2f9520_a17a_4671_9dba_3bd034099fff-deploy_container_using_nsenter_container_escape|Deploy container using nsenter container escape (sh; containers)]]
- [[kb/atomic/tests/39fab1bc_fcb9_406f_bc2e_fe03e42ff0e4-privilege_escalation_via_docker_volume_mapping|Privilege Escalation via Docker Volume Mapping (sh; containers)]]
- [[kb/atomic/tests/6c499943_b098_4bc6_8d38_0956fc182984-mount_host_filesystem_to_escape_privileged_docker_container|Mount host filesystem to escape privileged Docker container (sh; containers)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0004-privilege_escalation|TA0004: Privilege Escalation]]

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1048-application_isolation_and_sandboxing|M1048: Application Isolation and Sandboxing]]
- [[M1051-update_software|M1051: Update Software]]

## Tools

- [[peirates|Peirates (S0683)]]

## Platforms

- Windows
- Linux
- Containers
- ESXi

