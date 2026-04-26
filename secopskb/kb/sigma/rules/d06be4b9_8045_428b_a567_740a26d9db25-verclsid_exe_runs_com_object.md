---
sigma_id: "d06be4b9-8045-428b-a567-740a26d9db25"
title: "Verclsid.exe Runs COM Object"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d06be4b9-8045-428b-a567-740a26d9db25"
  - "Verclsid.exe Runs COM Object"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Verclsid.exe Runs COM Object

Detects when verclsid.exe is used to run COM object via GUID

## Metadata

- Rule ID: d06be4b9-8045-428b-a567-740a26d9db25
- Status: test
- Level: medium
- Author: Victor Sergeev, oscd.community
- Date: 2020-10-09
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \verclsid.exe
- OriginalFileName: verclsid.exe
selection_cli:
  CommandLine|contains|all:
  - /S
  - /C
filter_main_runtimebroker:
  ParentImage|endswith: C:\Windows\System32\RuntimeBroker.exe
  CommandLine|contains|all:
  - verclsid.exe" /S /C {
  - '} /I {'
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Verclsid/
- https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5
- https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_verclsid_runs_com.yml)
