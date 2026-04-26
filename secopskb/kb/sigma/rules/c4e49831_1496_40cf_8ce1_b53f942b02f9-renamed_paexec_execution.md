---
sigma_id: "c4e49831-1496-40cf-8ce1-b53f942b02f9"
title: "Renamed PAExec Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_paexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_paexec.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c4e49831-1496-40cf-8ce1-b53f942b02f9"
  - "Renamed PAExec Execution"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed PAExec Execution

Detects execution of renamed version of PAExec. Often used by attackers

## Metadata

- Rule ID: c4e49831-1496-40cf-8ce1-b53f942b02f9
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Jason Lynch
- Date: 2021-05-22
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_paexec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
- Description: PAExec Application
- OriginalFileName: PAExec.exe
- Product|contains: PAExec
- Hashes|contains:
  - IMPHASH=11D40A7B7876288F919AB819CC2D9802
  - IMPHASH=6444f8a34e99b8f7d9647de66aabe516
  - IMPHASH=dfd6aa3f7b2b1035b76b718f1ddc689f
  - IMPHASH=1a6cca4d5460b1710a12dea39e4a592c
filter_main_known_location:
- Image|endswith: \paexec.exe
- Image|startswith: C:\Windows\PAExec-
condition: selection and not 1 of filter_main_*
```

## False Positives

- Weird admins that rename their tools
- Software companies that bundle PAExec with their software and rename it, so that it is less embarrassing
- When executed with the "-s" flag. PAExec will copy itself to the "C:\Windows\" directory with a different name. Usually like this "PAExec-[XXXXX]-[ComputerName]"

## References

- https://www.poweradmin.com/paexec/
- https://summit.fireeye.com/content/dam/fireeye-www/summit/cds-2018/presentations/cds18-technical-s05-att&cking-fin7.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_paexec.yml)
