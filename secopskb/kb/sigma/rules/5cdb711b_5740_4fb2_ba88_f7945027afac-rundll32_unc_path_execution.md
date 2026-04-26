---
sigma_id: "5cdb711b-5740-4fb2-ba88-f7945027afac"
title: "Rundll32 UNC Path Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_unc_path.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_unc_path.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5cdb711b-5740-4fb2-ba88-f7945027afac"
  - "Rundll32 UNC Path Execution"
attack_technique_ids:
  - "T1021.002"
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Rundll32 UNC Path Execution

Detects rundll32 execution where the DLL is located on a remote location (share)

## Metadata

- Rule ID: 5cdb711b-5740-4fb2-ba88-f7945027afac
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-10
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_unc_path.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
- CommandLine|contains: rundll32
selection_cli:
  CommandLine|contains: ' \\\\'
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.cybereason.com/blog/rundll32-the-infamous-proxy-for-executing-malicious-code

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_unc_path.yml)
