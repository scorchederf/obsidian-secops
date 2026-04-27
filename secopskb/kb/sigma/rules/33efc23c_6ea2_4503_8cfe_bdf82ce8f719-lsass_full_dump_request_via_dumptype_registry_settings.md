---
sigma_id: "33efc23c-6ea2-4503-8cfe-bdf82ce8f719"
title: "Lsass Full Dump Request Via DumpType Registry Settings"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_lsass_usermode_dumping.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_lsass_usermode_dumping.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "33efc23c-6ea2-4503-8cfe-bdf82ce8f719"
  - "Lsass Full Dump Request Via DumpType Registry Settings"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the setting of the "DumpType" registry value to "2" which stands for a "Full Dump". Technique such as LSASS Shtinkering requires this value to be "2" in order to dump LSASS.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\DumpType
  - \SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps\lsass.exe\DumpType
  Details: DWORD (0x00000002)
condition: selection
```

## False Positives

- Legitimate application that needs to do a full dump of their process

## References

- https://github.com/deepinstinct/Lsass-Shtinkering
- https://learn.microsoft.com/en-us/windows/win32/wer/collecting-user-mode-dumps
- https://media.defcon.org/DEF%20CON%2030/DEF%20CON%2030%20presentations/Asaf%20Gilboa%20-%20LSASS%20Shtinkering%20Abusing%20Windows%20Error%20Reporting%20to%20Dump%20LSASS.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_lsass_usermode_dumping.yml)
