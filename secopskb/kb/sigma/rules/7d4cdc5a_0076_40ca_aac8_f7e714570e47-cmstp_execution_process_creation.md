---
sigma_id: "7d4cdc5a-0076-40ca-aac8-f7e714570e47"
title: "CMSTP Execution Process Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml"
build_date: "2026-04-26 17:03:18"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7d4cdc5a-0076-40ca-aac8-f7e714570e47"
  - "CMSTP Execution Process Creation"
attack_technique_ids:
  - "T1218.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# CMSTP Execution Process Creation

Detects various indicators of Microsoft Connection Manager Profile Installer execution

## Metadata

- Rule ID: 7d4cdc5a-0076-40ca-aac8-f7e714570e47
- Status: stable
- Level: high
- Author: Nik Seetharaman
- Date: 2018-07-16
- Modified: 2020-12-23
- Source Path: rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]

## Detection

```yaml
selection:
  ParentImage|endswith: \cmstp.exe
condition: selection
```

## False Positives

- Legitimate CMSTP use (unlikely in modern enterprise environments)

## References

- https://web.archive.org/web/20190720093911/http://www.endurant.io/cmstp/detecting-cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmstp_execution_by_creation.yml)
