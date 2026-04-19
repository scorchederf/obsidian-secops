---
id: T1083
name: File and Directory Discovery
created: 2017-05-31 21:31:04.710000+00:00
modified: 2025-10-24 17:49:00.036000+00:00
type: attack-pattern
x_mitre_version: 1.7
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Many command shell utilities can be used to obtain this information. Examples include <code>dir</code>, <code>tree</code>, <code>ls</code>, <code>find</code>, and <code>locate</code>.(Citation: Windows Commands JPCERT) Custom tools may also be used to gather file and directory information and interact with the [Native API](https://attack.mitre.org/techniques/T1106). Adversaries may also leverage a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008) on network devices to gather file and directory information (e.g. <code>dir</code>, <code>show flash</code>, and/or <code>nvram</code>).(Citation: US-CERT-TA18-106A)

Some files and directories may require elevated or specific user permissions to access.

## Properties

- id: T1083
- name: File and Directory Discovery
- created: 2017-05-31 21:31:04.710000+00:00
- modified: 2025-10-24 17:49:00.036000+00:00
- type: attack-pattern
- x_mitre_version: 1.7
- x_mitre_domains: enterprise-attack

## Platforms

- ESXi
- Linux
- macOS
- Network Devices
- Windows

## Tools

- [[S0106-cmd|S0106: cmd]]
- [[S0192-pupy|S0192: Pupy]]
- [[S0193-forfiles|S0193: Forfiles]]
- [[S0250-koadic|S0250: Koadic]]
- [[S0332-remcos|S0332: Remcos]]
- [[S0363-empire|S0363: Empire]]
- [[S0378-poshc2|S0378: PoshC2]]
- [[S0434-imminent_monitor|S0434: Imminent Monitor]]
- [[S0488-crackmapexec|S0488: CrackMapExec]]
- [[S0592-remoteutilities|S0592: RemoteUtilities]]
- [[S0633-sliver|S0633: Sliver]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]
- [[S1040-rclone|S1040: Rclone]]

