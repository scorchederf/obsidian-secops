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
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
d3fend_ids:
  - "D3-PSEP"
  - "D3-SAOR"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk (e.g., [[T1129-shared_modules|T1129: Shared Modules]]).

Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless executable code (ex: position-independent shellcode).(Citation: Introducing Donut)(Citation: S1 Custom Shellcode Tool)(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Mandiant BYOL) For example, the `Assembly.Load()` method executed by [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] may be abused to load raw code into the running process.(Citation: Microsoft AssemblyLoad)

Reflective code injection is very similar to [[T1055-process_injection|T1055: Process Injection]] except that the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk, while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Intezer ACBackdoor)(Citation: S1 Old Rat New Tricks)

## Workspace

- [[notes/attack/techniques/T1620-reflective_code_loading-note|Open workspace note]]

![[notes/attack/techniques/T1620-reflective_code_loading-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-PSEP-process_segment_execution_prevention|D3-PSEP: Process Segment Execution Prevention]]
- [[D3-SAOR-segment_address_offset_randomization|D3-SAOR: Segment Address Offset Randomization]]

## Tools

- [[powersploit|PowerSploit]]
- [[silenttrinity|SILENTTRINITY]]
- [[donut|Donut]]
- [[brute_ratel_c4|Brute Ratel C4]]

## Platforms

- Linux
- macOS
- Windows

