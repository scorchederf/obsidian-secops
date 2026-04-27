---
sigma_id: "e4d22291-f3d5-4b78-9a0c-a1fbaf32a6a4"
title: "Potentially Suspicious ODBC Driver Registered"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_odbc_driver_registered_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_odbc_driver_registered_susp.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e4d22291-f3d5-4b78-9a0c-a1fbaf32a6a4"
  - "Potentially Suspicious ODBC Driver Registered"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the registration of a new ODBC driver where the driver is located in a potentially suspicious location

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\ODBC\ODBCINST.INI\
  TargetObject|endswith:
  - \Driver
  - \Setup
  Details|contains:
  - :\PerfLogs\
  - :\ProgramData\
  - :\Temp\
  - :\Users\Public\
  - :\Windows\Registration\CRMLog
  - :\Windows\System32\com\dmp\
  - :\Windows\System32\FxsTmp\
  - :\Windows\System32\Microsoft\Crypto\RSA\MachineKeys\
  - :\Windows\System32\spool\drivers\color\
  - :\Windows\System32\spool\PRINTERS\
  - :\Windows\System32\spool\SERVERS\
  - :\Windows\System32\Tasks_Migrated\
  - :\Windows\System32\Tasks\Microsoft\Windows\SyncCenter\
  - :\Windows\SysWOW64\com\dmp\
  - :\Windows\SysWOW64\FxsTmp\
  - :\Windows\SysWOW64\Tasks\Microsoft\Windows\PLA\System\
  - :\Windows\SysWOW64\Tasks\Microsoft\Windows\SyncCenter\
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - :\Windows\Tracing\
  - \AppData\Local\Temp\
  - \AppData\Roaming\
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.hexacorn.com/blog/2020/08/23/odbcconf-lolbin-trifecta/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_odbc_driver_registered_susp.yml)
