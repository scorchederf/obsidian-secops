---
sigma_id: "fc014922-5def-4da9-a0fc-28c973f41bfb"
title: "Execution DLL of Choice Using WAB.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "fc014922-5def-4da9-a0fc-28c973f41bfb"
  - "Execution DLL of Choice Using WAB.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execution DLL of Choice Using WAB.EXE

This rule detects that the path to the DLL written in the registry is different from the default one. Launched WAB.exe tries to load the DLL from Registry.

## Metadata

- Rule ID: fc014922-5def-4da9-a0fc-28c973f41bfb
- Status: test
- Level: high
- Author: oscd.community, Natalia Shornikova
- Date: 2020-10-13
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Software\Microsoft\WAB\DLLPath
filter:
  Details: '%CommonProgramFiles%\System\wab32.dll'
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/LOLBAS-Project/LOLBAS/blob/8283d8d91552213ded165fd36deb6cb9534cb443/yml/OSBinaries/Wab.yml
- https://twitter.com/Hexacorn/status/991447379864932352
- http://www.hexacorn.com/blog/2018/05/01/wab-exe-as-a-lolbin/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_wab_dllpath_reg_change.yml)
