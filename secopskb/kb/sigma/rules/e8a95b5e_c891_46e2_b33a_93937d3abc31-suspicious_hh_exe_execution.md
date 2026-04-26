---
sigma_id: "e8a95b5e-c891-46e2-b33a-93937d3abc31"
title: "Suspicious HH.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hh_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hh_susp_execution.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e8a95b5e-c891-46e2-b33a-93937d3abc31"
  - "Suspicious HH.EXE Execution"
attack_technique_ids:
  - "T1047"
  - "T1059.001"
  - "T1059.003"
  - "T1059.005"
  - "T1059.007"
  - "T1218"
  - "T1218.001"
  - "T1218.010"
  - "T1218.011"
  - "T1566"
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious HH.EXE Execution

Detects a suspicious execution of a Microsoft HTML Help (HH.exe)

## Metadata

- Rule ID: e8a95b5e-c891-46e2-b33a-93937d3abc31
- Status: test
- Level: high
- Author: Maxim Pavlunin
- Date: 2020-04-01
- Modified: 2023-04-12
- Source Path: rules/windows/process_creation/proc_creation_win_hh_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.001]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]
- [[kb/attack/techniques/T1566-phishing|T1566]]
- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection_img:
- OriginalFileName: HH.exe
- Image|endswith: \hh.exe
selection_paths:
  CommandLine|contains:
  - .application
  - \AppData\Local\Temp\
  - \Content.Outlook\
  - \Downloads\
  - \Users\Public\
  - \Windows\Temp\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/chm-badness-delivers-a-banking-trojan/
- https://github.com/elastic/protections-artifacts/commit/746086721fd385d9f5c6647cada1788db4aea95f#diff-27939090904026cc396b0b629c8e4314acd6f5dac40a676edbc87f4567b47eb7
- https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/
- https://www.zscaler.com/blogs/security-research/unintentional-leak-glimpse-attack-vectors-apt37

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hh_susp_execution.yml)
