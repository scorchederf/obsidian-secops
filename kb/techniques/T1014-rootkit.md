---
mitre_id: "T1014"
mitre_name: "Rootkit"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0f20e3cb-245b-4a61-8a91-2d93f7cb0e9b"
mitre_created: "2017-05-31T21:30:26.496Z"
mitre_modified: "2025-10-24T17:48:24.032Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1014/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
---

# T1014: Rootkit

Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information. (Citation: Symantec Windows Rootkits) 

Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor or [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]. (Citation: Wikipedia Rootkit) Rootkits have been seen for Windows, Linux, and Mac OS X systems. (Citation: CrowdStrike Linux Rootkit) (Citation: BlackHat Mac OSX Rootkit)

Rootkits that reside or modify boot sectors are known as [[T1542-pre-os_boot#^t1542003-bootkit|T1542.003: Bootkit]]s and specifically target the boot process of the operating system.

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Tools

- [[htran|HTRAN]]

## Platforms

- Linux
- macOS
- Windows

