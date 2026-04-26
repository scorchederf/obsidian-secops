---
sigma_id: "d3bf399f-b0cf-4250-8bb4-dfc192ab81dc"
title: "Ie4uinit Lolbin Use From Invalid Path"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d3bf399f-b0cf-4250-8bb4-dfc192ab81dc"
  - "Ie4uinit Lolbin Use From Invalid Path"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Ie4uinit Lolbin Use From Invalid Path

Detect use of ie4uinit.exe to execute commands from a specially prepared ie4uinit.inf file from a directory other than the usual directories

## Metadata

- Rule ID: d3bf399f-b0cf-4250-8bb4-dfc192ab81dc
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-05-07
- Modified: 2022-05-16
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
lolbin:
- Image|endswith: \ie4uinit.exe
- OriginalFileName: IE4UINIT.EXE
filter_correct:
  CurrentDirectory:
  - c:\windows\system32\
  - c:\windows\sysWOW64\
filter_missing:
  CurrentDirectory: null
condition: lolbin and not 1 of filter_*
```

## False Positives

- ViberPC updater calls this binary with the following commandline "ie4uinit.exe -ClearIconCache"

## References

- https://lolbas-project.github.io/lolbas/Binaries/Ie4uinit/
- https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_ie4uinit.yml)
