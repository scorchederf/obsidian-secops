---
sigma_id: "97b9ce1e-c5ab-11ea-87d0-0242ac130003"
title: "PSExec and WMI Process Creations Block"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_asr_psexec_wmi.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_asr_psexec_wmi.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / windefend"
aliases:
  - "97b9ce1e-c5ab-11ea-87d0-0242ac130003"
  - "PSExec and WMI Process Creations Block"
attack_technique_ids:
  - "T1047"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PSExec and WMI Process Creations Block

Detects blocking of process creations originating from PSExec and WMI commands

## Metadata

- Rule ID: 97b9ce1e-c5ab-11ea-87d0-0242ac130003
- Status: test
- Level: high
- Author: Bhabesh Raj
- Date: 2020-07-14
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/windefend/win_defender_asr_psexec_wmi.yml

## Logsource

- definition: Requirements:Enabled Block process creations originating from PSExec and WMI commands from Attack Surface Reduction (GUID: d1e49aac-8f56-4280-b9ba-993a6d77406c)
- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  EventID: 1121
  ProcessName|endswith:
  - \wmiprvse.exe
  - \psexesvc.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-process-creations-originating-from-psexec-and-wmi-commands
- https://twitter.com/duff22b/status/1280166329660497920

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_asr_psexec_wmi.yml)
