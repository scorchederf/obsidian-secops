---
sigma_id: "c6fb44c6-71f5-49e6-9462-1425d328aee3"
title: "Powershell Base64 Encoded MpPreference Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_mppreference.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_mppreference.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c6fb44c6-71f5-49e6-9462-1425d328aee3"
  - "Powershell Base64 Encoded MpPreference Cmdlet"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects base64 encoded "MpPreference" PowerShell cmdlet code that tries to modifies or tamper with Windows Defender AV

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
- CommandLine|base64offset|contains:
  - 'Add-MpPreference '
  - 'Set-MpPreference '
  - 'add-mppreference '
  - 'set-mppreference '
- CommandLine|contains:
  - QQBkAGQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgA
  - EAZABkAC0ATQBwAFAAcgBlAGYAZQByAGUAbgBjAGUAIA
  - BAGQAZAAtAE0AcABQAHIAZQBmAGUAcgBlAG4AYwBlACAA
  - UwBlAHQALQBNAHAAUAByAGUAZgBlAHIAZQBuAGMAZQAgA
  - MAZQB0AC0ATQBwAFAAcgBlAGYAZQByAGUAbgBjAGUAIA
  - TAGUAdAAtAE0AcABQAHIAZQBmAGUAcgBlAG4AYwBlACAA
  - YQBkAGQALQBtAHAAcAByAGUAZgBlAHIAZQBuAGMAZQAgA
  - EAZABkAC0AbQBwAHAAcgBlAGYAZQByAGUAbgBjAGUAIA
  - hAGQAZAAtAG0AcABwAHIAZQBmAGUAcgBlAG4AYwBlACAA
  - cwBlAHQALQBtAHAAcAByAGUAZgBlAHIAZQBuAGMAZQAgA
  - MAZQB0AC0AbQBwAHAAcgBlAGYAZQByAGUAbgBjAGUAIA
  - zAGUAdAAtAG0AcABwAHIAZQBmAGUAcgBlAG4AYwBlACAA
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-endpoint/configure-process-opened-file-exclusions-microsoft-defender-antivirus
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://twitter.com/AdamTheAnalyst/status/1483497517119590403

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_mppreference.yml)
