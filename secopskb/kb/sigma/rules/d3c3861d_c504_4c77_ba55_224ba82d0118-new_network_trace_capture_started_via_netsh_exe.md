---
sigma_id: "d3c3861d-c504-4c77-ba55-224ba82d0118"
title: "New Network Trace Capture Started Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_packet_capture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_packet_capture.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d3c3861d-c504-4c77-ba55-224ba82d0118"
  - "New Network Trace Capture Started Via Netsh.EXE"
attack_technique_ids:
  - "T1040"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Network Trace Capture Started Via Netsh.EXE

Detects the execution of netsh with the "trace" flag in order to start a network capture

## Metadata

- Rule ID: d3c3861d-c504-4c77-ba55-224ba82d0118
- Status: test
- Level: medium
- Author: Kutepov Anton, oscd.community
- Date: 2019-10-24
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_packet_capture.yml

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
  - trace
  - start
condition: all of selection_*
```

## False Positives

- Legitimate administration activity

## References

- https://blogs.msdn.microsoft.com/canberrapfe/2012/03/30/capture-a-network-trace-without-installing-anything-capture-a-network-trace-of-a-reboot/
- https://klausjochem.me/2016/02/03/netsh-the-cyber-attackers-tool-of-choice/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_packet_capture.yml)
