---
id: T1014
name: Rootkit
created: 2017-05-31 21:30:26.496000+00:00
modified: 2025-10-24 17:48:24.032000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[defense_evasion|Defense Evasion]]

Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information. (Citation: Symantec Windows Rootkits) 

Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor or [System Firmware](https://attack.mitre.org/techniques/T1542/001). (Citation: Wikipedia Rootkit) Rootkits have been seen for Windows, Linux, and Mac OS X systems. (Citation: CrowdStrike Linux Rootkit) (Citation: BlackHat Mac OSX Rootkit)

Rootkits that reside or modify boot sectors are known as [Bootkit](https://attack.mitre.org/techniques/T1542/003)s and specifically target the boot process of the operating system.

## Platforms

- Linux
- macOS
- Windows

## Tools

- [[htran|HTRAN]]

