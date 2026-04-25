---
mitre_id: "T1012"
mitre_name: "Query Registry"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c32f7008-9fea-41f7-8366-5eb9b74bd896"
mitre_created: "2017-05-31T21:30:25.584Z"
mitre_modified: "2025-10-24T17:49:20.660Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1012/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
d3fend_ids:
  - "D3-DI"
  - "D3-RD"
  - "D3-SCA"
  - "D3-SCF"
  - "D3-SCP"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security.(Citation: Wikipedia Windows Registry) Information can easily be queried using the [[reg|Reg]] utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from [[T1012-query_registry|T1012: Query Registry]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Workspace

- [[notes/attack/techniques/T1012-query_registry-note|Open workspace note]]

![[notes/attack/techniques/T1012-query_registry-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-DI-data_inventory|D3-DI: Data Inventory]]
- [[D3-RD-restore_database|D3-RD: Restore Database]]
- [[D3-SCA-system_call_analysis|D3-SCA: System Call Analysis]]
- [[D3-SCF-system_call_filtering|D3-SCF: System Call Filtering]]
- [[D3-SCP-system_configuration_permissions|D3-SCP: System Configuration Permissions]]

## Tools

- [[reg|Reg]]
- [[powersploit|PowerSploit]]
- [[silenttrinity|SILENTTRINITY]]
- [[pcshare|PcShare]]

## Platforms

- Windows

