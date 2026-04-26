---
sigma_id: "cd71385d-fd9b-4691-9b98-2b1f7e508714"
title: "Lolbin Runexehelper Use As Proxy"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cd71385d-fd9b-4691-9b98-2b1f7e508714"
  - "Lolbin Runexehelper Use As Proxy"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Lolbin Runexehelper Use As Proxy

Detect usage of the "runexehelper.exe" binary as a proxy to launch other programs

## Metadata

- Rule ID: cd71385d-fd9b-4691-9b98-2b1f7e508714
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-29
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \runexehelper.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1206692239839289344
- https://lolbas-project.github.io/lolbas/Binaries/Runexehelper/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml)
