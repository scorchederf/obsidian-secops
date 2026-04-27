---
sigma_id: "8289bf8c-4aca-4f5a-9db3-dc3d7afe5c10"
title: "Unsigned Binary Loaded From Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security_mitigations/win_security_mitigations_unsigned_dll_from_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security_mitigations/win_security_mitigations_unsigned_dll_from_susp_location.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / security-mitigations"
aliases:
  - "8289bf8c-4aca-4f5a-9db3-dc3d7afe5c10"
  - "Unsigned Binary Loaded From Suspicious Location"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Code Integrity (CI) engine blocking processes from loading unsigned DLLs residing in suspicious locations

## Logsource

- product: windows
- service: security-mitigations

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  EventID:
  - 11
  - 12
  ImageName|contains:
  - \Users\Public\
  - \PerfLogs\
  - \Desktop\
  - \Downloads\
  - \AppData\Local\Temp\
  - C:\Windows\TEMP\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/nasbench/EVTX-ETW-Resources/blob/45fd5be71a51aa518b1b36d4e1f36af498084e27/ETWEventsList/CSV/Windows11/21H2/W11_21H2_Pro_20220719_22000.795/Providers/Microsoft-Windows-Security-Mitigations.csv

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security_mitigations/win_security_mitigations_unsigned_dll_from_susp_location.yml)
