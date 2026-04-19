---
id: T1007
name: System Service Discovery
created: 2017-05-31 21:30:21.315000+00:00
modified: 2025-10-24 17:48:36.812000+00:00
type: attack-pattern
x_mitre_version: 1.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[discovery|Discovery]]

Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as <code>sc query</code>, <code>tasklist /svc</code>, <code>systemctl --type=service</code>, and <code>net start</code>. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.(Citation: Elastic Security Labs GOSAR 2024)(Citation: SentinelLabs macOS Malware 2021)(Citation: Splunk Linux Gormir 2024)(Citation: Aquasec Kinsing 2020)

Adversaries may use the information from [System Service Discovery](https://attack.mitre.org/techniques/T1007) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Platforms

- Linux
- macOS
- Windows

