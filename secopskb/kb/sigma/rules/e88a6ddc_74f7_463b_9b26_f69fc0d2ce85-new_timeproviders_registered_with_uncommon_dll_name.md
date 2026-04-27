---
sigma_id: "e88a6ddc-74f7-463b-9b26-f69fc0d2ce85"
title: "New TimeProviders Registered With Uncommon DLL Name"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_timeproviders_dllname.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_timeproviders_dllname.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e88a6ddc-74f7-463b-9b26-f69fc0d2ce85"
  - "New TimeProviders Registered With Uncommon DLL Name"
attack_technique_ids:
  - "T1547.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects processes setting a new DLL in DllName in under HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProvider.
Adversaries may abuse time providers to execute DLLs when the system boots.
The Windows Time service (W32Time) enables time synchronization across and within domains.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547003-time-providers|T1547.003: Time Providers]]

## Detection

```yaml
selection:
  TargetObject|contains: \Services\W32Time\TimeProviders
  TargetObject|endswith: \DllName
filter_main_w32time:
  Details:
  - '%SystemRoot%\System32\vmictimeprovider.dll'
  - '%systemroot%\system32\w32time.dll'
  - C:\Windows\SYSTEM32\w32time.DLL
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.003/T1547.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_timeproviders_dllname.yml)
