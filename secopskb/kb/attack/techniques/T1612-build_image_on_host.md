---
mitre_id: "T1612"
mitre_name: "Build Image on Host"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--800f9819-7007-4540-a520-40e655876800"
mitre_created: "2021-03-30T17:54:03.944Z"
mitre_modified: "2025-10-24T17:49:01.646Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1612/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may build a container image directly on a host to bypass defenses that monitor for the retrieval of malicious images from a public registry. A remote `build` request may be sent to the Docker API that includes a Dockerfile that pulls a vanilla base image, such as alpine, from a public or local registry and then builds a custom image upon it.(Citation: Docker Build Image)

An adversary may take advantage of that `build` API to build a custom image on the host that includes malware downloaded from their C2 server, and then they may utilize [[T1610-deploy_container|T1610: Deploy Container]] using that custom image.(Citation: Aqua Build Images on Hosts)(Citation: Aqua Security Cloud Native Threat Report June 2021) If the base image is pulled from a public registry, defenses will likely not detect the image as malicious since it’s a vanilla image. If the base image already resides in a local registry, the pull may be considered even less suspicious since the image is already in the environment. 

## Workspace

- [[notes/attack/techniques/T1612-build_image_on_host-note|Open workspace note]]

![[notes/attack/techniques/T1612-build_image_on_host-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- Containers

