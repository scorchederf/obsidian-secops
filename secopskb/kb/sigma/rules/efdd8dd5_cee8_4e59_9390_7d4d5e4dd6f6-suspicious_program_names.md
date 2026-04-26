---
sigma_id: "efdd8dd5-cee8-4e59-9390-7d4d5e4dd6f6"
title: "Suspicious Program Names"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_progname.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_progname.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "efdd8dd5-cee8-4e59-9390-7d4d5e4dd6f6"
  - "Suspicious Program Names"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Program Names

Detects suspicious patterns in program names or folders that are often found in malicious samples or hacktools

## Metadata

- Rule ID: efdd8dd5-cee8-4e59-9390-7d4d5e4dd6f6
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-11
- Modified: 2023-03-22
- Source Path: rules/windows/process_creation/proc_creation_win_susp_progname.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_image:
- Image|contains:
  - \CVE-202
  - \CVE202
- Image|endswith:
  - \poc.exe
  - \artifact.exe
  - \artifact64.exe
  - \artifact_protected.exe
  - \artifact32.exe
  - \artifact32big.exe
  - obfuscated.exe
  - obfusc.exe
  - \meterpreter
selection_commandline:
  CommandLine|contains:
  - inject.ps1
  - Invoke-CVE
  - pupy.ps1
  - payload.ps1
  - beacon.ps1
  - PowerView.ps1
  - bypass.ps1
  - obfuscated.ps1
  - obfusc.ps1
  - obfus.ps1
  - obfs.ps1
  - evil.ps1
  - MiniDogz.ps1
  - _enc.ps1
  - \shell.ps1
  - \rshell.ps1
  - revshell.ps1
  - \av.ps1
  - \av_test.ps1
  - adrecon.ps1
  - mimikatz.ps1
  - \PowerUp_
  - powerup.ps1
  - \Temp\a.ps1
  - \Temp\p.ps1
  - \Temp\1.ps1
  - Hound.ps1
  - encode.ps1
  - powercat.ps1
condition: 1 of selection*
```

## False Positives

- Legitimate tools that accidentally match on the searched patterns

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1560.001/T1560.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_progname.yml)
