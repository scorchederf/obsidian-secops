---
sigma_id: "6004abd0-afa4-4557-ba90-49d172e0a299"
title: "Execute Pcwrun.EXE To Leverage Follina"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6004abd0-afa4-4557-ba90-49d172e0a299"
  - "Execute Pcwrun.EXE To Leverage Follina"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Execute Pcwrun.EXE To Leverage Follina

Detects indirect command execution via Program Compatibility Assistant "pcwrun.exe" leveraging the follina (CVE-2022-30190) vulnerability

## Metadata

- Rule ID: 6004abd0-afa4-4557-ba90-49d172e0a299
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-13
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \pcwrun.exe
  CommandLine|contains: ../
condition: selection
```

## False Positives

- Unlikely

## References

- https://twitter.com/nas_bench/status/1535663791362519040

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml)
