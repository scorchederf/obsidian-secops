---
sigma_id: "1f7025a6-e747-4130-aac4-961eb47015f1"
title: "HackTool - DiagTrackEoP Default Named Pipe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/pipe_created/pipe_created_hktl_diagtrack_eop.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_diagtrack_eop.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "critical"
logsource: "windows / pipe_created"
aliases:
  - "1f7025a6-e747-4130-aac4-961eb47015f1"
  - "HackTool - DiagTrackEoP Default Named Pipe"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - DiagTrackEoP Default Named Pipe

Detects creation of default named pipe used by the DiagTrackEoP POC, a tool that abuses "SeImpersonate" privilege.

## Metadata

- Rule ID: 1f7025a6-e747-4130-aac4-961eb47015f1
- Status: test
- Level: critical
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-03
- Modified: 2023-08-07
- Source Path: rules/windows/pipe_created/pipe_created_hktl_diagtrack_eop.yml

## Logsource

- category: pipe_created
- definition: Note that you have to configure logging for Named Pipe Events in Sysmon config (Event ID 17 and Event ID 18). The basic configuration is in popular sysmon configuration (https://github.com/SwiftOnSecurity/sysmon-config), but it is worth verifying. You can also use other repo, e.g. https://github.com/Neo23x0/sysmon-config, https://github.com/olafhartong/sysmon-modular. How to test detection? You can check powershell script from this site https://svch0st.medium.com/guide-to-named-pipes-and-hunting-for-cobalt-strike-pipes-dc46b2c5f575
- product: windows

## Detection

```yaml
selection:
  PipeName|contains: thisispipe
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/Wh04m1001/DiagTrackEoP/blob/3a2fc99c9700623eb7dc7d4b5f314fd9ce5ef51f/main.cpp#L22

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/pipe_created/pipe_created_hktl_diagtrack_eop.yml)
