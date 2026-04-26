---
sigma_id: "3037d961-21e9-4732-b27a-637bcc7bf539"
title: "Suspicious High IntegrityLevel Conhost Legacy Option"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_conhost_legacy_option.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_legacy_option.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "informational"
logsource: "windows / process_creation"
aliases:
  - "3037d961-21e9-4732-b27a-637bcc7bf539"
  - "Suspicious High IntegrityLevel Conhost Legacy Option"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious High IntegrityLevel Conhost Legacy Option

ForceV1 asks for information directly from the kernel space. Conhost connects to the console application. High IntegrityLevel means the process is running with elevated privileges, such as an Administrator context.

## Metadata

- Rule ID: 3037d961-21e9-4732-b27a-637bcc7bf539
- Status: test
- Level: informational
- Author: frack113
- Date: 2022-12-09
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_conhost_legacy_option.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  IntegrityLevel:
  - High
  - S-1-16-12288
  CommandLine|contains|all:
  - conhost.exe
  - '0xffffffff'
  - -ForceV1
condition: selection
```

## False Positives

- Very Likely, including launching cmd.exe via Run As Administrator

## References

- https://cybercryptosec.medium.com/covid-19-cyber-infection-c615ead7c29
- https://thedfirreport.com/2022/04/04/stolen-images-campaign-ends-in-conti-ransomware/
- https://learn.microsoft.com/en-us/windows/win32/secauthz/mandatory-integrity-control

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_legacy_option.yml)
