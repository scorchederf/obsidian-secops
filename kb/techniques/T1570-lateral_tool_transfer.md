---
id: T1570
name: Lateral Tool Transfer
created: 2020-03-11 21:01:00.959000+00:00
modified: 2025-10-24 17:49:19.137000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[lateral_movement|Lateral Movement]]

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) to connected network shares or with authenticated connections via [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001).(Citation: Unit42 LockerGoga 2019)

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and [ftp](https://attack.mitre.org/software/S0095). In some cases, adversaries may be able to leverage [Web Service](https://attack.mitre.org/techniques/T1102)s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.(Citation: Dropbox Malware Sync)

## Properties

- id: T1570
- name: Lateral Tool Transfer
- created: 2020-03-11 21:01:00.959000+00:00
- modified: 2025-10-24 17:49:19.137000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

## Tools

- [[S0029-psexec|S0029: PsExec]]
- [[S0095-ftp|S0095: ftp]]
- [[S0106-cmd|S0106: cmd]]
- [[S0190-bitsadmin|S0190: BITSAdmin]]
- [[S0357-impacket|S0357: Impacket]]
- [[S0361-expand|S0361: Expand]]
- [[S0404-esentutl|S0404: esentutl]]

