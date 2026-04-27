---
sigma_id: "602a1f13-c640-4d73-b053-be9a2fa58b96"
title: "HackTool - Powerup Write Hijack DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_powerup_dllhijacking.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_powerup_dllhijacking.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "602a1f13-c640-4d73-b053-be9a2fa58b96"
  - "HackTool - Powerup Write Hijack DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Powerup tool's Write Hijack DLL exploits DLL hijacking for privilege escalation.
In it's default mode, it builds a self deleting .bat file which executes malicious command.
The detection rule relies on creation of the malicious bat file (debug.bat by default).

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  TargetFilename|endswith: .bat
condition: selection
```

## False Positives

- Any powershell script that creates bat files

## References

- https://powersploit.readthedocs.io/en/latest/Privesc/Write-HijackDll/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_powerup_dllhijacking.yml)
