---
id: T1046
name: Network Service Discovery
created: 2017-05-31 21:30:43.915000+00:00
modified: 2025-10-24 17:49:31.494000+00:00
type: attack-pattern
x_mitre_version: 3.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system.(Citation: CISA AR21-126A FIVEHANDS May 2021)   

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as <code>dns-sd -B _ssh._tcp .</code>) to find other systems broadcasting the ssh service.(Citation: apple doco bonjour description)(Citation: macOS APT Activity Bradley)

## Properties

- id: T1046
- name: Network Service Discovery
- created: 2017-05-31 21:30:43.915000+00:00
- modified: 2025-10-24 17:49:31.494000+00:00
- type: attack-pattern
- x_mitre_version: 3.2
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Containers
- IaaS
- Linux
- macOS
- Network Devices
- Windows

## Tools

- [[S0192-pupy|S0192: Pupy]]
- [[S0250-koadic|S0250: Koadic]]
- [[S0363-empire|S0363: Empire]]
- [[S0378-poshc2|S0378: PoshC2]]
- [[S0590-nbtscan|S0590: NBTscan]]
- [[S0683-peirates|S0683: Peirates]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]
- [[S1063-brute_ratel_c4|S1063: Brute Ratel C4]]
- [[S1144-frp|S1144: FRP]]

