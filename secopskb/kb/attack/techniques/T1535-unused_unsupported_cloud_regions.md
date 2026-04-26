---
mitre_id: "T1535"
mitre_name: "Unused/Unsupported Cloud Regions"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--59bd0dec-f8b2-4b9a-9141-37a1e6899761"
mitre_created: "2019-09-04T14:35:04.617Z"
mitre_modified: "2025-10-24T17:48:49.853Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1535/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may create cloud instances in unused geographic service regions in order to evade detection. Access is usually obtained through compromising accounts used to manage cloud infrastructure.

Cloud service providers often provide infrastructure throughout the world in order to improve performance, provide redundancy, and allow customers to meet compliance requirements. Oftentimes, a customer will only use a subset of the available regions and may not actively monitor other regions. If an adversary creates resources in an unused region, they may be able to operate undetected.

A variation on this behavior takes advantage of differences in functionality across cloud regions. An adversary could utilize regions which do not support advanced detection services in order to avoid detection of their activity.

An example of adversary use of unused AWS regions is to mine cryptocurrency through [[T1496-resource_hijacking|T1496: Resource Hijacking]], which can cost organizations substantial amounts of money over time depending on the processing power used.(Citation: CloudSploit - Unused AWS Regions)

## Workspace

- [[workspaces/attack/techniques/T1535-unused_unsupported_cloud_regions-note|Open workspace note]]

![[workspaces/attack/techniques/T1535-unused_unsupported_cloud_regions-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Mitigations

- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- IaaS

