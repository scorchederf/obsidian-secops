---
sigma_id: "ab37a6ec-6068-432b-a64e-2c7bf95b1d22"
title: "Scripting/CommandLine Process Spawned Regsvr32"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_susp_parent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_parent.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ab37a6ec-6068-432b-a64e-2c7bf95b1d22"
  - "Scripting/CommandLine Process Spawned Regsvr32"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scripting/CommandLine Process Spawned Regsvr32

Detects various command line and scripting engines/processes such as "PowerShell", "Wscript", "Cmd", etc. spawning a "regsvr32" instance.

## Metadata

- Rule ID: ab37a6ec-6068-432b-a64e-2c7bf95b1d22
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-26
- Source Path: rules/windows/process_creation/proc_creation_win_regsvr32_susp_parent.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  Image|endswith: \regsvr32.exe
filter_main_rpcproxy:
  ParentImage: C:\Windows\System32\cmd.exe
  CommandLine|endswith: ' /s C:\Windows\System32\RpcProxy\RpcProxy.dll'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate ".bat", ".hta", ".ps1" or ".vbs" scripts leverage legitimately often. Apply additional filter and exclusions as necessary
- Some legitimate Windows services

## References

- https://web.archive.org/web/20171001085340/https://subt0x10.blogspot.com/2017/04/bypass-application-whitelisting-script.html
- https://app.any.run/tasks/34221348-072d-4b70-93f3-aa71f6ebecad/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_parent.yml)
