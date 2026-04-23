---
mitre_id: "T1018"
mitre_name: "Remote System Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--e358d692-23c0-4a31-9eb6-ecc13a8d7735"
mitre_created: "2017-05-31T21:30:28.187Z"
mitre_modified: "2025-10-24T17:49:31.319Z"
mitre_version: "3.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1018/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Network Devices"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
---

# T1018: Remote System Discovery

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as  [[ping|Ping]], `net view` using [[net|Net]], or, on ESXi servers, `esxcli network diag ping`.

Adversaries may also analyze data from local host files (ex: `C:\Windows\System32\Drivers\etc\hosts` or `/etc/hosts`) or other passive means (such as local [[arp|Arp]] cache entries) in order to discover the presence of remote systems in an environment.

Adversaries may also target discovery of network infrastructure as well as leverage [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands on network devices to gather detailed information about systems within a network (e.g. `show cdp neighbors`, `show arp`).(Citation: US-CERT-TA18-106A)(Citation: CISA AR21-126A FIVEHANDS May 2021)  


## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[net|Net]]
- [[ping|Ping]]
- [[arp|Arp]]
- [[nltest|Nltest]]
- [[crackmapexec|CrackMapExec]]
- [[bloodhound|BloodHound]]
- [[adfind|AdFind]]
- [[nbtscan|NBTscan]]
- [[roadtools|ROADTools]]
- [[silenttrinity|SILENTTRINITY]]

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

