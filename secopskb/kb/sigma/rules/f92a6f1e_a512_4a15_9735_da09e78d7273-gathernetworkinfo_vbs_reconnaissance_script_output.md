---
sigma_id: "f92a6f1e-a512-4a15-9735-da09e78d7273"
title: "GatherNetworkInfo.VBS Reconnaissance Script Output"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_lolbin_gather_network_info_script_output.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_lolbin_gather_network_info_script_output.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "f92a6f1e-a512-4a15-9735-da09e78d7273"
  - "GatherNetworkInfo.VBS Reconnaissance Script Output"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# GatherNetworkInfo.VBS Reconnaissance Script Output

Detects creation of files which are the results of executing the built-in reconnaissance script "C:\Windows\System32\gatherNetworkInfo.vbs".

## Metadata

- Rule ID: f92a6f1e-a512-4a15-9735-da09e78d7273
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-08
- Source Path: rules/windows/file/file_event/file_event_win_lolbin_gather_network_info_script_output.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Windows\System32\config
  TargetFilename|endswith:
  - \Hotfixinfo.txt
  - \netiostate.txt
  - \sysportslog.txt
  - \VmSwitchLog.evtx
condition: selection
```

## False Positives

- Unknown

## References

- https://posts.slayerlabs.com/living-off-the-land/#gathernetworkinfovbs
- https://www.mandiant.com/resources/blog/trojanized-windows-installers-ukrainian-government

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_lolbin_gather_network_info_script_output.yml)
