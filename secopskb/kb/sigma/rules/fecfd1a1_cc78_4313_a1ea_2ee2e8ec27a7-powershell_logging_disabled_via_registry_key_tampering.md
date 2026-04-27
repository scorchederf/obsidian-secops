---
sigma_id: "fecfd1a1-cc78-4313-a1ea-2ee2e8ec27a7"
title: "PowerShell Logging Disabled Via Registry Key Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_powershell_logging_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_logging_disabled.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "fecfd1a1-cc78-4313-a1ea-2ee2e8ec27a7"
  - "PowerShell Logging Disabled Via Registry Key Tampering"
attack_technique_ids:
  - "T1564.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects changes to the registry for the currently logged-in user. In order to disable PowerShell module logging, script block logging or transcription and script execution logging

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564001-hidden-files-and-directories|T1564.001: Hidden Files and Directories]]
- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Microsoft\Windows\PowerShell\
  - \Microsoft\PowerShellCore\
  TargetObject|endswith:
  - \ModuleLogging\EnableModuleLogging
  - \ScriptBlockLogging\EnableScriptBlockLogging
  - \ScriptBlockLogging\EnableScriptBlockInvocationLogging
  - \Transcription\EnableTranscripting
  - \Transcription\EnableInvocationHeader
  - \EnableScripts
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## Simulation

### Disable PowerShell Logging via Registry

- Atomic Test: [[kb/atomic/tests/95b25212_91a7_42ff_9613_124aca6845a8-windows_powershell_logging_disabled|95b25212-91a7-42ff-9613-124aca6845a8]]
- atomic_guid: 95b25212-91a7-42ff-9613-124aca6845a8
- name: Disable PowerShell Logging via Registry
- technique: T1112
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md#atomic-test-32---windows-powershell-logging-disabled

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_logging_disabled.yml)
