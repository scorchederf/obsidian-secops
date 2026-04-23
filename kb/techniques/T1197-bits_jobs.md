---
mitre_id: "T1197"
mitre_name: "BITS Jobs"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--c8e87b83-edbb-48d4-9295-4974897525b7"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:49:22.711Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1197/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
  - "TA0003"
---

# T1197: BITS Jobs

Adversaries may abuse BITS jobs to persistently execute code and perform various background tasks. Windows Background Intelligent Transfer Service (BITS) is a low-bandwidth, asynchronous file transfer mechanism exposed through [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]] (COM).(Citation: Microsoft COM)(Citation: Microsoft BITS) BITS is commonly used by updaters, messengers, and other applications preferred to operate in the background (using available idle bandwidth) without interrupting other networked applications. File transfer tasks are implemented as BITS jobs, which contain a queue of one or more file operations.

The interface to create and manage BITS jobs is accessible through [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] and the [[bitsadmin|BITSAdmin]] tool.(Citation: Microsoft BITS)(Citation: Microsoft BITSAdmin)

Adversaries may abuse BITS to download (e.g. [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]), execute, and even clean up after running malicious code (e.g. [[T1070-indicator_removal|T1070: Indicator Removal]]). BITS tasks are self-contained in the BITS job database, without new files or registry modifications, and often permitted by host firewalls.(Citation: CTU BITS Malware June 2016)(Citation: Mondok Windows PiggyBack BITS May 2007)(Citation: Symantec BITS May 2007) BITS enabled execution may also enable persistence by creating long-standing jobs (the default maximum lifetime is 90 days and extendable) or invoking an arbitrary program when a job completes or errors (including after system reboots).(Citation: PaloAlto UBoatRAT Nov 2017)(Citation: CTU BITS Malware June 2016)

BITS upload functionalities can also be used to perform [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]].(Citation: CTU BITS Malware June 2016)

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0003-persistence|TA0003: Persistence]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]

## Tools

- [[bitsadmin|BITSAdmin]]

## Platforms

- Windows

