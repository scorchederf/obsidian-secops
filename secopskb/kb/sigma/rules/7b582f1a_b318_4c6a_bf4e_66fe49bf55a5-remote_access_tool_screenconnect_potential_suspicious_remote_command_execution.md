---
sigma_id: "7b582f1a-b318-4c6a-bf4e-66fe49bf55a5"
title: "Remote Access Tool - ScreenConnect Potential Suspicious Remote Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_remote_execution_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_remote_execution_susp.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7b582f1a-b318-4c6a-bf4e-66fe49bf55a5"
  - "Remote Access Tool - ScreenConnect Potential Suspicious Remote Command Execution"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - ScreenConnect Potential Suspicious Remote Command Execution

Detects potentially suspicious child processes launched via the ScreenConnect client service.

## Metadata

- Rule ID: 7b582f1a-b318-4c6a-bf4e-66fe49bf55a5
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems), @Kostastsale
- Date: 2022-02-25
- Modified: 2024-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_remote_execution_susp.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  ParentCommandLine|contains|all:
  - :\Windows\TEMP\ScreenConnect\
  - run.cmd
  Image|endswith:
  - \bitsadmin.exe
  - \cmd.exe
  - \curl.exe
  - \dllhost.exe
  - \net.exe
  - \nltest.exe
  - \powershell.exe
  - \pwsh.exe
  - \rundll32.exe
  - \wevtutil.exe
condition: selection
```

## False Positives

- If the script being executed make use of any of the utilities mentioned in the detection then they should filtered out or allowed.

## References

- https://www.mandiant.com/resources/telegram-malware-iranian-espionage
- https://docs.connectwise.com/ConnectWise_Control_Documentation/Get_started/Host_client/View_menu/Backstage_mode
- https://www.huntress.com/blog/slashandgrab-screen-connect-post-exploitation-in-the-wild-cve-2024-1709-cve-2024-1708
- https://www.trendmicro.com/en_us/research/24/b/threat-actor-groups-including-black-basta-are-exploiting-recent-.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_screenconnect_remote_execution_susp.yml)
