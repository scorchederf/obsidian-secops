---
sigma_id: "3b4b232a-af90-427c-a22f-30b0c0837b95"
title: "CMSTP Execution Process Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_cmstp_execution_by_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_cmstp_execution_by_access.yml"
build_date: "2026-04-26 14:14:21"
status: "stable"
level: "high"
logsource: "windows / process_access"
aliases:
  - "3b4b232a-af90-427c-a22f-30b0c0837b95"
  - "CMSTP Execution Process Access"
attack_technique_ids:
  - "T1218.003"
  - "T1559.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CMSTP Execution Process Access

Detects various indicators of Microsoft Connection Manager Profile Installer execution

## Metadata

- Rule ID: 3b4b232a-af90-427c-a22f-30b0c0837b95
- Status: stable
- Level: high
- Author: Nik Seetharaman
- Date: 2018-07-16
- Modified: 2021-06-27
- Source Path: rules/windows/process_access/proc_access_win_cmstp_execution_by_access.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.003]]
- [[kb/attack/techniques/T1559-inter-process_communication|T1559.001]]

## Detection

```yaml
selection:
  CallTrace|contains: cmlua.dll
condition: selection
```

## False Positives

- Legitimate CMSTP use (unlikely in modern enterprise environments)

## References

- https://web.archive.org/web/20190720093911/http://www.endurant.io/cmstp/detecting-cmstp-enabled-code-execution-and-uac-bypass-with-sysmon/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_cmstp_execution_by_access.yml)
