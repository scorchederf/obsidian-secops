---
sigma_id: "f2485272-a156-4773-82d7-1d178bc4905b"
title: "Suspicious Service Installed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_service_installed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_service_installed.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "f2485272-a156-4773-82d7-1d178bc4905b"
  - "Suspicious Service Installed"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Service Installed

Detects installation of NalDrv or PROCEXP152 services via registry-keys to non-system32 folders.
Both services are used in the tool Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU (https://github.com/hfiref0x/KDU)

## Metadata

- Rule ID: f2485272-a156-4773-82d7-1d178bc4905b
- Status: test
- Level: medium
- Author: xknow (@xknow_infosec), xorxes (@xor_xes)
- Date: 2019-04-08
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_susp_service_installed.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject:
  - HKLM\System\CurrentControlSet\Services\NalDrv\ImagePath
  - HKLM\System\CurrentControlSet\Services\PROCEXP152\ImagePath
filter:
  Image|endswith:
  - \procexp64.exe
  - \procexp.exe
  - \procmon64.exe
  - \procmon.exe
  - \handle.exe
  - \handle64.exe
  Details|contains: \WINDOWS\system32\Drivers\PROCEXP152.SYS
condition: selection and not filter
```

## False Positives

- Other legimate tools using this service names and drivers. Note - clever attackers may easily bypass this detection by just renaming the services. Therefore just Medium-level and don't rely on it.

## References

- https://web.archive.org/web/20200419024230/https://blog.dylan.codes/evading-sysmon-and-windows-event-logging/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_service_installed.yml)
