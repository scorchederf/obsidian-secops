---
sigma_id: "c15e99a3-c474-48ab-b9a7-84549a7a9d16"
title: "Remote Thread Creation Ttdinject.exe Proxy"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / create_remote_thread"
aliases:
  - "c15e99a3-c474-48ab-b9a7-84549a7a9d16"
  - "Remote Thread Creation Ttdinject.exe Proxy"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remote Thread Creation Ttdinject.exe Proxy

Detects a remote thread creation of Ttdinject.exe used as proxy

## Metadata

- Rule ID: c15e99a3-c474-48ab-b9a7-84549a7a9d16
- Status: test
- Level: high
- Author: frack113
- Date: 2022-05-16
- Modified: 2022-06-02
- Source Path: rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
  SourceImage|endswith: \ttdinject.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Ttdinject/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_ttdinjec.yml)
