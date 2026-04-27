---
sigma_id: "a0a278fe-2c0e-4de2-ac3c-c68b08a9ba98"
title: "LSASS Access Detected via Attack Surface Reduction"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_asr_lsass_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_asr_lsass_access.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / windefend"
aliases:
  - "a0a278fe-2c0e-4de2-ac3c-c68b08a9ba98"
  - "LSASS Access Detected via Attack Surface Reduction"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# LSASS Access Detected via Attack Surface Reduction

Detects Access to LSASS Process

## Metadata

- Rule ID: a0a278fe-2c0e-4de2-ac3c-c68b08a9ba98
- Status: test
- Level: high
- Author: Markus Neis
- Date: 2018-08-26
- Modified: 2022-08-13
- Source Path: rules/windows/builtin/windefend/win_defender_asr_lsass_access.yml

## Logsource

- definition: Requirements:Enabled Block credential stealing from the Windows local security authority subsystem (lsass.exe) from Attack Surface Reduction (GUID: 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2)
- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  EventID: 1121
  Path|endswith: \lsass.exe
filter_thor:
  ProcessName|startswith: C:\Windows\Temp\asgard2-agent\
  ProcessName|endswith:
  - \thor64.exe
  - \thor.exe
filter_exact:
  ProcessName:
  - C:\Windows\System32\atiesrxx.exe
  - C:\Windows\System32\CompatTelRunner.exe
  - C:\Windows\System32\msiexec.exe
  - C:\Windows\System32\nvwmi64.exe
  - C:\Windows\System32\svchost.exe
  - C:\Windows\System32\Taskmgr.exe
  - C:\Windows\System32\wbem\WmiPrvSE.exe
  - C:\Windows\SysWOW64\msiexec.exe
filter_begins:
  ProcessName|startswith:
  - C:\Windows\System32\DriverStore\
  - C:\WINDOWS\Installer\
  - C:\Program Files\
  - C:\Program Files (x86)\
condition: selection and not 1 of filter_*
```

## False Positives

- Google Chrome GoogleUpdate.exe
- Some Taskmgr.exe related activity

## References

- https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_asr_lsass_access.yml)
