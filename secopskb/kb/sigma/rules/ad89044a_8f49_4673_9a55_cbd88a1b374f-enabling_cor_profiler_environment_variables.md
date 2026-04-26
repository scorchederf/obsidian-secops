---
sigma_id: "ad89044a-8f49-4673-9a55-cbd88a1b374f"
title: "Enabling COR Profiler Environment Variables"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_enabling_cor_profiler_env_variables.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_enabling_cor_profiler_env_variables.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "ad89044a-8f49-4673-9a55-cbd88a1b374f"
  - "Enabling COR Profiler Environment Variables"
attack_technique_ids:
  - "T1574.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enabling COR Profiler Environment Variables

Detects .NET Framework CLR and .NET Core CLR "cor_enable_profiling" and "cor_profiler" variables being set and configured.

## Metadata

- Rule ID: ad89044a-8f49-4673-9a55-cbd88a1b374f
- Status: test
- Level: medium
- Author: Jose Rodriguez (@Cyb3rPandaH), OTR (Open Threat Research), Jimmy Bayne (@bohops)
- Date: 2020-09-10
- Modified: 2023-11-24
- Source Path: rules/windows/registry/registry_set/registry_set_enabling_cor_profiler_env_variables.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.012]]

## Detection

```yaml
selection_1:
  TargetObject|endswith:
  - \COR_ENABLE_PROFILING
  - \COR_PROFILER
  - \CORECLR_ENABLE_PROFILING
selection_2:
  TargetObject|contains: \CORECLR_PROFILER_PATH
condition: 1 of selection_*
```

## References

- https://twitter.com/jamieantisocial/status/1304520651248668673
- https://www.slideshare.net/JamieWilliams130/started-from-the-bottom-exploiting-data-sources-to-uncover-attck-behaviors
- https://www.sans.org/cyber-security-summit/archives
- https://learn.microsoft.com/en-us/dotnet/core/runtime-config/debugging-profiling

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_enabling_cor_profiler_env_variables.yml)
