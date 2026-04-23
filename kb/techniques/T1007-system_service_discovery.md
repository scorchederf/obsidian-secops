---
mitre_id: "T1007"
mitre_name: "System Service Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--322bad5a-1c49-4d23-ab79-76d641794afa"
mitre_created: "2017-05-31T21:30:21.315Z"
mitre_modified: "2025-10-24T17:48:36.812Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1007/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
---

# T1007: System Service Discovery

Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as `sc query`, `tasklist /svc`, `systemctl --type=service`, and `net start`. Adversaries may also gather information about schedule tasks via commands such as `schtasks` on Windows or `crontab -l` on Linux and macOS.(Citation: Elastic Security Labs GOSAR 2024)(Citation: SentinelLabs macOS Malware 2021)(Citation: Splunk Linux Gormir 2024)(Citation: Aquasec Kinsing 2020)

Adversaries may use the information from [[T1007-system_service_discovery|T1007: System Service Discovery]] during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[net|Net]]
- [[tasklist|Tasklist]]
- [[poshc2|PoshC2]]
- [[silenttrinity|SILENTTRINITY]]

## Platforms

- Linux
- macOS
- Windows

