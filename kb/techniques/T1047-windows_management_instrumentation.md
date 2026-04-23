---
mitre_id: "T1047"
mitre_name: "Windows Management Instrumentation"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--01a5a209-b94c-450b-b7f9-946497d91055"
mitre_created: "2017-05-31T21:30:44.329Z"
mitre_modified: "2025-10-24T17:48:19.670Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1047/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0002"
---

# T1047: Windows Management Instrumentation

Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems.(Citation: WMI 1-3) WMI is an administration feature that provides a uniform environment to access Windows system components.

The WMI service enables both local and remote access, though the latter is facilitated by [[T1021-remote_services|T1021: Remote Services]] such as [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]] and [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]].(Citation: WMI 1-3) Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and 5986 for HTTPS.(Citation: WMI 1-3) (Citation: Mandiant WMI)

An adversary can use WMI to interact with local and remote systems and use it as a means to execute various behaviors, such as gathering information for [[TA0007-discovery|TA0007: Discovery]] as well as [[TA0002-execution|TA0002: Execution]] of commands and payloads.(Citation: Mandiant WMI) For example, `wmic.exe` can be abused by an adversary to delete shadow copies with the command `wmic.exe Shadowcopy Delete` (i.e., [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]).(Citation: WMI 6)

**Note:** `wmic.exe` is deprecated as of January of 2024, with the WMIC feature being “disabled by default” on Windows 11+. WMIC will be removed from subsequent Windows releases and replaced by [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] as the primary WMI interface.(Citation: WMI 7,8) In addition to PowerShell and tools like `wbemtool.exe`, COM APIs can also be used to programmatically interact with WMI via C++, .NET, VBScript, etc.(Citation: WMI 7,8)

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Tools

- [[powersploit|PowerSploit]]
- [[koadic|Koadic]]
- [[impacket|Impacket]]
- [[empire|Empire]]
- [[poshc2|PoshC2]]
- [[crackmapexec|CrackMapExec]]
- [[silenttrinity|SILENTTRINITY]]
- [[brute_ratel_c4|Brute Ratel C4]]
- [[covenant|Covenant]]

## Platforms

- Windows

