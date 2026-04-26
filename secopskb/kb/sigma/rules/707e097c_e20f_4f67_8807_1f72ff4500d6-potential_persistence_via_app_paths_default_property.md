---
sigma_id: "707e097c-e20f-4f67-8807-1f72ff4500d6"
title: "Potential Persistence Via App Paths Default Property"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "707e097c-e20f-4f67-8807-1f72ff4500d6"
  - "Potential Persistence Via App Paths Default Property"
attack_technique_ids:
  - "T1546.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via App Paths Default Property

Detects changes to the "Default" property for keys located in the \Software\Microsoft\Windows\CurrentVersion\App Paths\ registry. Which might be used as a method of persistence
The entries found under App Paths are used primarily for the following purposes.
First, to map an application's executable file name to that file's fully qualified path.
Second, to prepend information to the PATH environment variable on a per-application, per-process basis.

## Metadata

- Rule ID: 707e097c-e20f-4f67-8807-1f72ff4500d6
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-10
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.012]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths
  TargetObject|endswith:
  - (Default)
  - Path
  Details|contains:
  - \Users\Public
  - \AppData\Local\Temp\
  - \Windows\Temp\
  - \Desktop\
  - \Downloads\
  - '%temp%'
  - '%tmp%'
  - iex
  - Invoke-
  - rundll32
  - regsvr32
  - mshta
  - cscript
  - wscript
  - .bat
  - .hta
  - .dll
  - .ps1
condition: selection
```

## False Positives

- Legitimate applications registering their binary from on of the suspicious locations mentioned above (tune it)

## References

- https://www.hexacorn.com/blog/2013/01/19/beyond-good-ol-run-key-part-3/
- https://learn.microsoft.com/en-us/windows/win32/shell/app-registration

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_app_paths.yml)
