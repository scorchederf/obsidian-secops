---
sigma_id: "af77cf95-c469-471c-b6a0-946c685c4798"
title: "Proxy Execution Via Wuauclt.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wuauclt_dll_loading.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wuauclt_dll_loading.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "af77cf95-c469-471c-b6a0-946c685c4798"
  - "Proxy Execution Via Wuauclt.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Proxy Execution Via Wuauclt.EXE

Detects the use of the Windows Update Client binary (wuauclt.exe) for proxy execution.

## Metadata

- Rule ID: af77cf95-c469-471c-b6a0-946c685c4798
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), Florian Roth (Nextron Systems), Sreeman, FPT.EagleEye Team
- Date: 2020-10-12
- Modified: 2023-11-11
- Source Path: rules/windows/process_creation/proc_creation_win_wuauclt_dll_loading.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \wuauclt.exe
- OriginalFileName: wuauclt.exe
selection_cli:
  CommandLine|contains|all:
  - UpdateDeploymentProvider
  - RunHandlerComServer
filter_main_generic:
  CommandLine|contains: ' /UpdateDeploymentProvider UpdateDeploymentProvider.dll '
filter_main_wuaueng:
  CommandLine|contains: ' wuaueng.dll '
filter_main_uus:
  CommandLine|contains:
  - :\Windows\UUS\Packages\Preview\amd64\updatedeploy.dll /ClassId
  - :\Windows\UUS\amd64\UpdateDeploy.dll /ClassId
filter_main_winsxs:
  CommandLine|contains|all:
  - :\Windows\WinSxS\
  - '\UpdateDeploy.dll /ClassId '
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://dtm.uk/wuauclt/
- https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wuauclt_dll_loading.yml)
