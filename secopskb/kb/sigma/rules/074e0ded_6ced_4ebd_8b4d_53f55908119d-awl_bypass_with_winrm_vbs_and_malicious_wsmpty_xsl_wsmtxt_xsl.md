---
sigma_id: "074e0ded-6ced-4ebd-8b4d-53f55908119d"
title: "AWL Bypass with Winrm.vbs and Malicious WsmPty.xsl/WsmTxt.xsl"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "074e0ded-6ced-4ebd-8b4d-53f55908119d"
  - "AWL Bypass with Winrm.vbs and Malicious WsmPty.xsl/WsmTxt.xsl"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AWL Bypass with Winrm.vbs and Malicious WsmPty.xsl/WsmTxt.xsl

Detects execution of attacker-controlled WsmPty.xsl or WsmTxt.xsl via winrm.vbs and copied cscript.exe (can be renamed)

## Metadata

- Rule ID: 074e0ded-6ced-4ebd-8b4d-53f55908119d
- Status: test
- Level: medium
- Author: Julia Fomina, oscd.community
- Date: 2020-10-06
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
contains_format_pretty_arg:
  CommandLine|contains:
  - format:pretty
  - format:"pretty"
  - format:"text"
  - format:text
image_from_system_folder:
  Image|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
contains_winrm:
  CommandLine|contains: winrm
condition: contains_winrm and (contains_format_pretty_arg and not image_from_system_folder)
```

## False Positives

- Unlikely

## References

- https://posts.specterops.io/application-whitelisting-bypass-and-arbitrary-unsigned-code-execution-technique-in-winrm-vbs-c8c24fb40404

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrm_awl_bypass.yml)
