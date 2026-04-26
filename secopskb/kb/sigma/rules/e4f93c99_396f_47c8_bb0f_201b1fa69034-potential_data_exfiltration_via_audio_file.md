---
sigma_id: "e4f93c99-396f-47c8-bb0f-201b1fa69034"
title: "Potential Data Exfiltration Via Audio File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_audio_exfiltration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_audio_exfiltration.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "e4f93c99-396f-47c8-bb0f-201b1fa69034"
  - "Potential Data Exfiltration Via Audio File"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Data Exfiltration Via Audio File

Detects potential exfiltration attempt via audio file using PowerShell

## Metadata

- Rule ID: e4f93c99-396f-47c8-bb0f-201b1fa69034
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-16
- Source Path: rules/windows/powershell/powershell_script/posh_ps_audio_exfiltration.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## Detection

```yaml
selection_main:
  ScriptBlockText|contains|all:
  - '[System.Math]::'
  - '[IO.FileMode]::'
  - BinaryWriter
selection_header_wav:
  ScriptBlockText|contains|all:
  - '0x52'
  - '0x49'
  - '0x46'
  - '0x57'
  - '0x41'
  - '0x56'
  - '0x45'
  - '0xAC'
condition: selection_main and 1 of selection_header_*
```

## False Positives

- Unknown

## References

- https://github.com/gtworek/PSBits/blob/e97cbbb173b31cbc4d37244d3412de0a114dacfb/NoDLP/bin2wav.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_audio_exfiltration.yml)
