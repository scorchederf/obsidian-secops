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
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
---

# T1012: Query Registry

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security.(Citation: Wikipedia Windows Registry) Information can easily be queried using the [[reg|Reg]] utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from [[T1012-query_registry|T1012: Query Registry]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[reg|Reg]]
- [[powersploit|PowerSploit]]
- [[silenttrinity|SILENTTRINITY]]
- [[pcshare|PcShare]]

## Platforms

- Windows

