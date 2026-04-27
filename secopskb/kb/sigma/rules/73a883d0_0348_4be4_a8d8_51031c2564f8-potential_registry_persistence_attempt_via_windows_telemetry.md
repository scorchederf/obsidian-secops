---
sigma_id: "73a883d0-0348-4be4-a8d8-51031c2564f8"
title: "Potential Registry Persistence Attempt Via Windows Telemetry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_telemetry_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_telemetry_persistence.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "73a883d0-0348-4be4-a8d8-51031c2564f8"
  - "Potential Registry Persistence Attempt Via Windows Telemetry"
attack_technique_ids:
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential persistence behavior using the windows telemetry registry key.
Windows telemetry makes use of the binary CompatTelRunner.exe to run a variety of commands and perform the actual telemetry collections.
This binary was created to be easily extensible, and to that end, it relies on the registry to instruct on which commands to run.
The problem is, it will run any arbitrary command without restriction of location or type.

## Logsource

- category: registry_set
- definition: Requirements: Sysmon config that monitors \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\TelemetryController subkey of the HKLM hives
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\TelemetryController\
  TargetObject|endswith: \Command
  Details|contains:
  - .bat
  - .bin
  - .cmd
  - .dat
  - .dll
  - .exe
  - .hta
  - .jar
  - .js
  - .msi
  - .ps
  - .sh
  - .vb
filter_main_generic:
  Details|contains:
  - \system32\CompatTelRunner.exe
  - \system32\DeviceCensus.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.trustedsec.com/blog/abusing-windows-telemetry-for-persistence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_telemetry_persistence.yml)
