---
sigma_id: "d353dac0-1b41-46c2-820c-d7d2561fc6ed"
title: "AWL Bypass with Winrm.vbs and Malicious WsmPty.xsl/WsmTxt.xsl - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "d353dac0-1b41-46c2-820c-d7d2561fc6ed"
  - "AWL Bypass with Winrm.vbs and Malicious WsmPty.xsl/WsmTxt.xsl - File"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWL Bypass with Winrm.vbs and Malicious WsmPty.xsl/WsmTxt.xsl - File

Detects execution of attacker-controlled WsmPty.xsl or WsmTxt.xsl via winrm.vbs and copied cscript.exe (can be renamed)

## Metadata

- Rule ID: d353dac0-1b41-46c2-820c-d7d2561fc6ed
- Status: test
- Level: medium
- Author: Julia Fomina, oscd.community
- Date: 2020-10-06
- Modified: 2022-11-28
- Source Path: rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
system_files:
  TargetFilename|endswith:
  - WsmPty.xsl
  - WsmTxt.xsl
in_system_folder:
  TargetFilename|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
condition: system_files and not in_system_folder
```

## False Positives

- Unlikely

## References

- https://posts.specterops.io/application-whitelisting-bypass-and-arbitrary-unsigned-code-execution-technique-in-winrm-vbs-c8c24fb40404

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_winrm_awl_bypass.yml)
