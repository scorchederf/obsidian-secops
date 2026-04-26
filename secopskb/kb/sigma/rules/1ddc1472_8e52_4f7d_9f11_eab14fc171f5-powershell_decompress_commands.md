---
sigma_id: "1ddc1472-8e52-4f7d-9f11-eab14fc171f5"
title: "PowerShell Decompress Commands"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_decompress_commands.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_decompress_commands.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "informational"
logsource: "windows / ps_module"
aliases:
  - "1ddc1472-8e52-4f7d-9f11-eab14fc171f5"
  - "PowerShell Decompress Commands"
attack_technique_ids:
  - "T1140"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Decompress Commands

A General detection for specific decompress commands in PowerShell logs. This could be an adversary decompressing files.

## Metadata

- Rule ID: 1ddc1472-8e52-4f7d-9f11-eab14fc171f5
- Status: test
- Level: informational
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-05-02
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_module/posh_pm_decompress_commands.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Detection

```yaml
selection_4103:
  Payload|contains: Expand-Archive
condition: selection_4103
```

## False Positives

- Unknown

## References

- https://github.com/OTRF/detection-hackathon-apt29/issues/8
- https://github.com/OTRF/ThreatHunter-Playbook/blob/2d4257f630f4c9770f78d0c1df059f891ffc3fec/docs/evals/apt29/detections/4.A.3_09F29912-8E93-461E-9E89-3F06F6763383.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_decompress_commands.yml)
