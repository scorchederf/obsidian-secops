---
sigma_id: "771d1eb5-9587-4568-95fb-9ec44153a012"
title: "PUA - NSudo Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_nsudo.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nsudo.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "771d1eb5-9587-4568-95fb-9ec44153a012"
  - "PUA - NSudo Execution"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - NSudo Execution

Detects the use of NSudo tool for command execution

## Metadata

- Rule ID: 771d1eb5-9587-4568-95fb-9ec44153a012
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali
- Date: 2022-01-24
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_pua_nsudo.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0029

## Detection

```yaml
selection_img:
- Image|endswith:
  - \NSudo.exe
  - \NSudoLC.exe
  - \NSudoLG.exe
- OriginalFileName:
  - NSudo.exe
  - NSudoLC.exe
  - NSudoLG.exe
selection_cli:
  CommandLine|contains:
  - '-U:S '
  - '-U:T '
  - '-U:E '
  - '-P:E '
  - '-M:S '
  - '-M:H '
  - '-U=S '
  - '-U=T '
  - '-U=E '
  - '-P=E '
  - '-M=S '
  - '-M=H '
  - -ShowWindowMode:Hide
condition: all of selection_*
```

## False Positives

- Legitimate use by administrators

## References

- https://web.archive.org/web/20221019044836/https://nsudo.m2team.org/en-us/
- https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-windows/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nsudo.yml)
