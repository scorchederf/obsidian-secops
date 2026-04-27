---
sigma_id: "7a4d9232-92fc-404d-8ce1-4c92e7caf539"
title: "HackTool - Stracciatella Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_stracciatella_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_stracciatella_execution.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7a4d9232-92fc-404d-8ce1-4c92e7caf539"
  - "HackTool - Stracciatella Execution"
attack_technique_ids:
  - "T1059"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Stracciatella which executes a Powershell runspace from within C# (aka SharpPick technique) with AMSI, ETW and Script Block Logging disabled based on PE metadata characteristics.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
- Image|endswith: \Stracciatella.exe
- OriginalFileName: Stracciatella.exe
- Description: Stracciatella
- Hashes|contains:
  - SHA256=9d25e61ec1527e2a69d7c2a4e3fe2fe15890710c198a66a9f25d99fdf6c7b956
  - SHA256=fd16609bd9830c63b9413671678bb159b89c357d21942ddbb6b93add808d121a
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/mgeeky/Stracciatella

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_stracciatella_execution.yml)
