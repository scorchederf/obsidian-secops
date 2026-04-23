---
mitre_id: "T1620"
mitre_name: "Reflective Code Loading"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4933e63b-9b77-476e-ab29-761bc5b7d15a"
mitre_created: "2021-10-05T01:15:06.293Z"
mitre_modified: "2025-10-24T17:48:44.030Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1620/"
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

# T1620: Reflective Code Loading

Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk (e.g., [[T1129-shared_modules|T1129: Shared Modules]]).

Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless executable code (ex: position-independent shellcode).(Citation: Introducing Donut)(Citation: S1 Custom Shellcode Tool)(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Mandiant BYOL) For example, the `Assembly.Load()` method executed by [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] may be abused to load raw code into the running process.(Citation: Microsoft AssemblyLoad)

Reflective code injection is very similar to [[T1055-process_injection|T1055: Process Injection]] except that the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk, while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Intezer ACBackdoor)(Citation: S1 Old Rat New Tricks)

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Tools

- [[powersploit|PowerSploit]]
- [[silenttrinity|SILENTTRINITY]]
- [[donut|Donut]]
- [[brute_ratel_c4|Brute Ratel C4]]

## Platforms

- Linux
- macOS
- Windows

