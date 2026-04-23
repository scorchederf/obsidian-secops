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
build_date: "2026-04-23 20:16:46"
build_source: "script"
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
---

# T1046: Network Service Discovery

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.(Citation: CISA AR21-126A FIVEHANDS May 2021)   

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as `dns-sd -B _ssh._tcp .`) to find other systems broadcasting the ssh service.(Citation: apple doco bonjour description)(Citation: macOS APT Activity Bradley)

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Tools

- [[pupy|Pupy]]
- [[koadic|Koadic]]
- [[empire|Empire]]
- [[poshc2|PoshC2]]
- [[nbtscan|NBTscan]]
- [[peirates|Peirates]]
- [[silenttrinity|SILENTTRINITY]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[frp|FRP]]

## Platforms

- Containers
- IaaS
- Linux
- macOS
- Network Devices
- Windows

