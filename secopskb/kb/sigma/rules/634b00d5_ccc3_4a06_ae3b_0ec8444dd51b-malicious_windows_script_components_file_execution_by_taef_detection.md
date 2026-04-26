---
sigma_id: "634b00d5-ccc3-4a06-ae3b-0ec8444dd51b"
title: "Malicious Windows Script Components File Execution by TAEF Detection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "634b00d5-ccc3-4a06-ae3b-0ec8444dd51b"
  - "Malicious Windows Script Components File Execution by TAEF Detection"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Malicious Windows Script Components File Execution by TAEF Detection

Windows Test Authoring and Execution Framework (TAEF) framework allows you to run automation by executing tests files written on different languages (C, C#, Microsoft COM Scripting interfaces
Adversaries may execute malicious code (such as WSC file with VBScript, dll and so on) directly by running te.exe

## Metadata

- Rule ID: 634b00d5-ccc3-4a06-ae3b-0ec8444dd51b
- Status: test
- Level: low
- Author: Agro (@agro_sev) oscd.community
- Date: 2020-10-13
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
- Image|endswith: \te.exe
- ParentImage|endswith: \te.exe
- OriginalFileName: \te.exe
condition: selection
```

## False Positives

- It's not an uncommon to use te.exe directly to execute legal TAEF tests

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Te/
- https://twitter.com/pabraeken/status/993298228840992768
- https://learn.microsoft.com/en-us/windows-hardware/drivers/taef/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml)
