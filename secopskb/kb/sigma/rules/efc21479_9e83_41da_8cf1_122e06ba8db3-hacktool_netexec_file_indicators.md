---
sigma_id: "efc21479-9e83-41da-8cf1-122e06ba8db3"
title: "HackTool - NetExec File Indicators"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_netexec_file_indicators.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_netexec_file_indicators.yml"
build_date: "2026-04-26 17:03:19"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "efc21479-9e83-41da-8cf1-122e06ba8db3"
  - "HackTool - NetExec File Indicators"
attack_technique_ids:
  - "T1021.002"
  - "T1059.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - NetExec File Indicators

Detects file creation events indicating NetExec (nxc.exe) execution on the local machine.
NetExec is a PyInstaller-bundled binary that extracts its embedded data files to a "_MEI<random>" directory
under the Temp folder upon execution. Files dropped under the "\nxc\" sub-directory of that
extraction path are unique to NetExec and serve as reliable on-disk indicators of execution.
NetExec (formerly CrackMapExec) is a widely used post-exploitation and lateral movement tool used for
Active Directory enumeration, credential harvesting, and remote code execution.

## Metadata

- Rule ID: efc21479-9e83-41da-8cf1-122e06ba8db3
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-04-08
- Source Path: rules/windows/file/file_event/file_event_win_hktl_netexec_file_indicators.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]

## Detection

```yaml
selection:
- Image|contains: \nxc-windows-latest\
- TargetFilename|contains|all:
  - \Temp\_MEI
  - \nxc\data\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Pennyw0rth/NetExec
- https://www.netexec.wiki/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_netexec_file_indicators.yml)
