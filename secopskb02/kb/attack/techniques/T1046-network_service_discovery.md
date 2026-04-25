---
mitre_id: "T1046"
mitre_name: "Network Service Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e3a12395-188d-4051-9a16-ea8e14d07b88"
mitre_created: "2017-05-31T21:30:43.915Z"
mitre_modified: "2025-10-24T17:49:31.494Z"
mitre_version: "3.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1046/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Containers"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.(Citation: CISA AR21-126A FIVEHANDS May 2021)   

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as `dns-sd -B _ssh._tcp .`) to find other systems broadcasting the ssh service.(Citation: apple doco bonjour description)(Citation: macOS APT Activity Bradley)

## Workspace

- [[workspaces/attack/techniques/T1046-network_service_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1046-network_service_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Tools

- [[pupy|Pupy (S0192)]]
- [[koadic|Koadic (S0250)]]
- [[empire|Empire (S0363)]]
- [[poshc2|PoshC2 (S0378)]]
- [[nbtscan|NBTscan (S0590)]]
- [[peirates|Peirates (S0683)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]
- [[brute_ratel_c4|Brute Ratel C4 (S1063)]]
- [[frp|FRP (S1144)]]

## Platforms

- Containers
- IaaS
- Linux
- macOS
- Network Devices
- Windows

