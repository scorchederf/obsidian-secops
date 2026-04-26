---
sigma_id: "52cad028-0ff0-4854-8f67-d25dfcbc78b4"
title: "HTML Help HH.EXE Suspicious Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hh_html_help_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hh_html_help_susp_child_process.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "52cad028-0ff0-4854-8f67-d25dfcbc78b4"
  - "HTML Help HH.EXE Suspicious Child Process"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HTML Help HH.EXE Suspicious Child Process

Detects a suspicious child process of a Microsoft HTML Help (HH.exe)

## Metadata

- Rule ID: 52cad028-0ff0-4854-8f67-d25dfcbc78b4
- Status: test
- Level: high
- Author: Maxim Pavlunin, Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-04-01
- Modified: 2023-04-12
- Source Path: rules/windows/process_creation/proc_creation_win_hh_html_help_susp_child_process.yml

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
selection:
  ParentImage|endswith: \hh.exe
  Image|endswith:
  - \CertReq.exe
  - \CertUtil.exe
  - \cmd.exe
  - \cscript.exe
  - \installutil.exe
  - \MSbuild.exe
  - \MSHTA.EXE
  - \msiexec.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \schtasks.exe
  - \wmic.exe
  - \wscript.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/chm-badness-delivers-a-banking-trojan/
- https://github.com/elastic/protections-artifacts/commit/746086721fd385d9f5c6647cada1788db4aea95f#diff-27939090904026cc396b0b629c8e4314acd6f5dac40a676edbc87f4567b47eb7
- https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/
- https://www.zscaler.com/blogs/security-research/unintentional-leak-glimpse-attack-vectors-apt37

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hh_html_help_susp_child_process.yml)
