---
sigma_id: "2569ed8c-1147-498a-9b8c-2ad3656b10ed"
title: "Potential Renamed Rundll32 Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_rundll32_dllregisterserver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_rundll32_dllregisterserver.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2569ed8c-1147-498a-9b8c-2ad3656b10ed"
  - "Potential Renamed Rundll32 Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Renamed Rundll32 Execution

Detects when 'DllRegisterServer' is called in the commandline and the image is not rundll32. This could mean that the 'rundll32' utility has been renamed in order to avoid detection

## Metadata

- Rule ID: 2569ed8c-1147-498a-9b8c-2ad3656b10ed
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-22
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_rundll32_dllregisterserver.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains: DllRegisterServer
filter:
  Image|endswith: \rundll32.exe
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://twitter.com/swisscom_csirt/status/1331634525722521602?s=20
- https://app.any.run/tasks/f74c5157-8508-4ac6-9805-d63fe7b0d399/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_rundll32_dllregisterserver.yml)
