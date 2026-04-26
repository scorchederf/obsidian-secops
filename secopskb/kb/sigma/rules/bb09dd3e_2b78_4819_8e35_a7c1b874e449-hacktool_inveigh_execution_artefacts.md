---
sigma_id: "bb09dd3e-2b78-4819-8e35-a7c1b874e449"
title: "HackTool - Inveigh Execution Artefacts"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_inveigh_artefacts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_inveigh_artefacts.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "critical"
logsource: "windows / file_event"
aliases:
  - "bb09dd3e-2b78-4819-8e35-a7c1b874e449"
  - "HackTool - Inveigh Execution Artefacts"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Inveigh Execution Artefacts

Detects the presence and execution of Inveigh via dropped artefacts

## Metadata

- Rule ID: bb09dd3e-2b78-4819-8e35-a7c1b874e449
- Status: test
- Level: critical
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-24
- Modified: 2024-06-27
- Source Path: rules/windows/file/file_event/file_event_win_hktl_inveigh_artefacts.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \Inveigh-Log.txt
  - \Inveigh-Cleartext.txt
  - \Inveigh-NTLMv1Users.txt
  - \Inveigh-NTLMv2Users.txt
  - \Inveigh-NTLMv1.txt
  - \Inveigh-NTLMv2.txt
  - \Inveigh-FormInput.txt
  - \Inveigh.dll
  - \Inveigh.exe
  - \Inveigh.ps1
  - \Inveigh-Relay.ps1
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/Kevin-Robertson/Inveigh/blob/29d9e3c3a625b3033cdaf4683efaafadcecb9007/Inveigh/Support/Output.cs
- https://github.com/Kevin-Robertson/Inveigh/blob/29d9e3c3a625b3033cdaf4683efaafadcecb9007/Inveigh/Support/Control.cs
- https://thedfirreport.com/2020/11/23/pysa-mespinoza-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_inveigh_artefacts.yml)
