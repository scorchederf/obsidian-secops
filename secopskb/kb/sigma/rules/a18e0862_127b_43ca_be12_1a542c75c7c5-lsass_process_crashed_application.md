---
sigma_id: "a18e0862-127b-43ca-be12-1a542c75c7c5"
title: "LSASS Process Crashed - Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/application_error/win_application_error_lsass_crash.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/application_error/win_application_error_lsass_crash.yml"
build_date: "2026-04-27 19:13:52"
status: "experimental"
level: "high"
logsource: "windows / application"
aliases:
  - "a18e0862-127b-43ca-be12-1a542c75c7c5"
  - "LSASS Process Crashed - Application"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Windows error reporting events where the process that crashed is LSASS (Local Security Authority Subsystem Service).
This could be the cause of a provoked crash by techniques such as Lsass-Shtinkering to dump credentials.

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
  Provider_Name: Application Error
  EventID: 1000
  AppName: lsass.exe
  ExceptionCode: c0000001
condition: selection
```

## False Positives

- Rare legitimate crashing of the lsass process

## References

- https://github.com/deepinstinct/Lsass-Shtinkering
- https://media.defcon.org/DEF%20CON%2030/DEF%20CON%2030%20presentations/Asaf%20Gilboa%20-%20LSASS%20Shtinkering%20Abusing%20Windows%20Error%20Reporting%20to%20Dump%20LSASS.pdf
- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/application_error/win_application_error_lsass_crash.yml)
