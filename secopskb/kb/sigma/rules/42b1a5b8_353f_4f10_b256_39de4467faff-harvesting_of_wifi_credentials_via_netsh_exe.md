---
sigma_id: "42b1a5b8-353f-4f10-b256-39de4467faff"
title: "Harvesting Of Wifi Credentials Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_wifi_credential_harvesting.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_wifi_credential_harvesting.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "42b1a5b8-353f-4f10-b256-39de4467faff"
  - "Harvesting Of Wifi Credentials Via Netsh.EXE"
attack_technique_ids:
  - "T1040"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Harvesting Of Wifi Credentials Via Netsh.EXE

Detect the harvesting of wifi credentials using netsh.exe

## Metadata

- Rule ID: 42b1a5b8-353f-4f10-b256-39de4467faff
- Status: test
- Level: medium
- Author: Andreas Hunkeler (@Karneades), oscd.community
- Date: 2020-04-20
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_wifi_credential_harvesting.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli:
  CommandLine|contains|all:
  - wlan
  - ' s'
  - ' p'
  - ' k'
  - =clear
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_wifi_credential_harvesting.yml)
