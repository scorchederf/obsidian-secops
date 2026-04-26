---
sigma_id: "77946e79-97f1-45a2-84b4-f37b5c0d8682"
title: "Suspicious Registry Modification From ADS Via Regini.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regini_ads.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regini_ads.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "77946e79-97f1-45a2-84b4-f37b5c0d8682"
  - "Suspicious Registry Modification From ADS Via Regini.EXE"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Registry Modification From ADS Via Regini.EXE

Detects the import of an alternate data stream with regini.exe, regini.exe can be used to modify registry keys.

## Metadata

- Rule ID: 77946e79-97f1-45a2-84b4-f37b5c0d8682
- Status: test
- Level: high
- Author: Eli Salem, Sander Wiebing, oscd.community
- Date: 2020-10-12
- Modified: 2023-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_regini_ads.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_img:
- Image|endswith: \regini.exe
- OriginalFileName: REGINI.EXE
selection_re:
  CommandLine|re: :[^ \\]
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Regini/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/regini

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regini_ads.yml)
