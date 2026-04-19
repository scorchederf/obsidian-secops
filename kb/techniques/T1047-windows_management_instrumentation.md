---
id: T1047
name: Windows Management Instrumentation
created: 2017-05-31 21:30:44.329000+00:00
modified: 2025-10-24 17:48:19.670000+00:00
type: attack-pattern
x_mitre_version: 1.6
x_mitre_domains: enterprise-attack
---

## Tactic

- [[execution|Execution]]

Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems.(Citation: WMI 1-3) WMI is an administration feature that provides a uniform environment to access Windows system components.

The WMI service enables both local and remote access, though the latter is facilitated by [Remote Services](https://attack.mitre.org/techniques/T1021) such as [Distributed Component Object Model](https://attack.mitre.org/techniques/T1021/003) and [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006).(Citation: WMI 1-3) Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and 5986 for HTTPS.(Citation: WMI 1-3) (Citation: Mandiant WMI)

An adversary can use WMI to interact with local and remote systems and use it as a means to execute various behaviors, such as gathering information for [Discovery](https://attack.mitre.org/tactics/TA0007) as well as [Execution](https://attack.mitre.org/tactics/TA0002) of commands and payloads.(Citation: Mandiant WMI) For example, `wmic.exe` can be abused by an adversary to delete shadow copies with the command `wmic.exe Shadowcopy Delete` (i.e., [Inhibit System Recovery](https://attack.mitre.org/techniques/T1490)).(Citation: WMI 6)

**Note:** `wmic.exe` is deprecated as of January of 2024, with the WMIC feature being “disabled by default” on Windows 11+. WMIC will be removed from subsequent Windows releases and replaced by [PowerShell](https://attack.mitre.org/techniques/T1059/001) as the primary WMI interface.(Citation: WMI 7,8) In addition to PowerShell and tools like `wbemtool.exe`, COM APIs can also be used to programmatically interact with WMI via C++, .NET, VBScript, etc.(Citation: WMI 7,8)

## Properties

- id: T1047
- name: Windows Management Instrumentation
- created: 2017-05-31 21:30:44.329000+00:00
- modified: 2025-10-24 17:48:19.670000+00:00
- type: attack-pattern
- x_mitre_version: 1.6
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1038-execution_prevention|M1038: Execution Prevention]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Platforms

- Windows

## Tools

- [[S0194-powersploit|S0194: PowerSploit]]
- [[S0250-koadic|S0250: Koadic]]
- [[S0357-impacket|S0357: Impacket]]
- [[S0363-empire|S0363: Empire]]
- [[S0378-poshc2|S0378: PoshC2]]
- [[S0488-crackmapexec|S0488: CrackMapExec]]
- [[S0692-silenttrinity|S0692: SILENTTRINITY]]
- [[S1063-brute_ratel_c4|S1063: Brute Ratel C4]]
- [[S1155-covenant|S1155: Covenant]]

