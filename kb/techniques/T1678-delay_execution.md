---
mitre_id: "T1678"
mitre_name: "Delay Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--a1df809c-7d0e-459f-8fe5-25474bab770b"
mitre_created: "2025-09-24T18:03:15.021Z"
mitre_modified: "2025-10-21T23:58:09.956Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1678/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
---

# T1678: Delay Execution

Adversaries may employ various time-based methods to evade detection and analysis. These techniques often exploit system clocks, delays, or timing mechanisms to obscure malicious activity, blend in with benign activity, and avoid scrutiny. Adversaries can perform this behavior within virtualization/sandbox environments or natively on host systems. 

Adversaries may utilize programmatic `sleep` commands or native system scheduling functionality, for example [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]. Benign commands or other operations may also be used to delay malware execution or ensure prior commands have had time to execute properly. Loops or otherwise needless repetitions of commands, such as `ping`, may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments.(Citation: Revil Independence Day)(Citation: Netskope Nitol) Another variation, commonly referred to as API hammering, involves making various calls to Native API functions in order to delay execution (while also potentially overloading analysis environments with junk data).(Citation: Joe Sec Nymaim)(Citation: Joe Sec Trickbot)

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Platforms

- Linux
- macOS
- Windows

