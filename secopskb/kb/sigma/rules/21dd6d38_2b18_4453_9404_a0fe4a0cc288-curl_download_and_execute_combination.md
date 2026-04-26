---
sigma_id: "21dd6d38-2b18-4453-9404-a0fe4a0cc288"
title: "Curl Download And Execute Combination"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_curl_download_exec_combo.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_curl_download_exec_combo.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "21dd6d38-2b18-4453-9404-a0fe4a0cc288"
  - "Curl Download And Execute Combination"
attack_technique_ids:
  - "T1218"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Curl Download And Execute Combination

Adversaries can use curl to download payloads remotely and execute them. Curl is included by default in Windows 10 build 17063 and later.

## Metadata

- Rule ID: 21dd6d38-2b18-4453-9404-a0fe4a0cc288
- Status: test
- Level: high
- Author: Sreeman, Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-01-13
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_curl_download_exec_combo.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  CommandLine|contains|windash: ' -c '
  CommandLine|contains|all:
  - 'curl '
  - http
  - -o
  - '&'
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/@reegun/curl-exe-is-the-new-rundll32-exe-lolbin-3f79c5f35983

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_curl_download_exec_combo.yml)
