---
sigma_id: "9a4ccd1a-3526-4d99-b980-9f9c5d3a6ff3"
title: "Potential Credential Dumping Via WER"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_werfault_lsass_shtinkering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_werfault_lsass_shtinkering.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9a4ccd1a-3526-4d99-b980-9f9c5d3a6ff3"
  - "Potential Credential Dumping Via WER"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Credential Dumping Via WER

Detects potential credential dumping via Windows Error Reporting LSASS Shtinkering technique which uses the Windows Error Reporting to dump lsass

## Metadata

- Rule ID: 9a4ccd1a-3526-4d99-b980-9f9c5d3a6ff3
- Status: test
- Level: high
- Author: @pbssubhash , Nasreddine Bencherchali
- Date: 2022-12-08
- Modified: 2022-12-09
- Source Path: rules/windows/process_creation/proc_creation_win_werfault_lsass_shtinkering.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \Werfault.exe
- OriginalFileName: WerFault.exe
selection_cli:
  ParentUser|contains:
  - AUTHORI
  - AUTORI
  User|contains:
  - AUTHORI
  - AUTORI
  CommandLine|contains|all:
  - ' -u -p '
  - ' -ip '
  - ' -s '
filter_lsass:
  ParentImage: C:\Windows\System32\lsass.exe
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Windows Error Reporting might produce similar behavior. In that case, check the PID associated with the "-p" parameter in the CommandLine.

## References

- https://github.com/deepinstinct/Lsass-Shtinkering
- https://media.defcon.org/DEF%20CON%2030/DEF%20CON%2030%20presentations/Asaf%20Gilboa%20-%20LSASS%20Shtinkering%20Abusing%20Windows%20Error%20Reporting%20to%20Dump%20LSASS.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_werfault_lsass_shtinkering.yml)
