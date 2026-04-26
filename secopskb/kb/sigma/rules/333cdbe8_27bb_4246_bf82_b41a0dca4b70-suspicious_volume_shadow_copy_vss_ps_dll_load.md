---
sigma_id: "333cdbe8-27bb-4246-bf82-b41a0dca4b70"
title: "Suspicious Volume Shadow Copy VSS_PS.dll Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_vss_ps_susp_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_vss_ps_susp_load.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "333cdbe8-27bb-4246-bf82-b41a0dca4b70"
  - "Suspicious Volume Shadow Copy VSS_PS.dll Load"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Volume Shadow Copy VSS_PS.dll Load

Detects the image load of vss_ps.dll by uncommon executables. This DLL is used by the Volume Shadow Copy Service (VSS) to manage shadow copies of files and volumes.
It is often abused by attackers to delete or manipulate shadow copies, which can hinder forensic investigations and data recovery efforts.
The fact that it is loaded by processes that are not typically associated with VSS operations can indicate suspicious activity.

## Metadata

- Rule ID: 333cdbe8-27bb-4246-bf82-b41a0dca4b70
- Status: test
- Level: high
- Author: Markus Neis, @markus_neis
- Date: 2021-07-07
- Modified: 2025-07-11
- Source Path: rules/windows/image_load/image_load_dll_vss_ps_susp_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \vss_ps.dll
filter_main_legit:
  Image|startswith: C:\Windows\
  Image|endswith:
  - \clussvc.exe
  - \dismhost.exe
  - \dllhost.exe
  - \inetsrv\appcmd.exe
  - \inetsrv\iissetup.exe
  - \msiexec.exe
  - \rundll32.exe
  - \searchindexer.exe
  - \srtasks.exe
  - \svchost.exe
  - \System32\SystemPropertiesAdvanced.exe
  - \taskhostw.exe
  - \thor.exe
  - \thor64.exe
  - \tiworker.exe
  - \vssvc.exe
  - \vssadmin.exe
  - \WmiPrvSE.exe
  - \wsmprovhost.exe
filter_main_update:
  CommandLine|startswith: C:\$WinREAgent\Scratch\
  CommandLine|contains: \dismhost.exe {
filter_main_image_null:
  Image: null
filter_optional_programfiles:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://www.virustotal.com/gui/file/ba88ca45589fae0139a40ca27738a8fc2dfbe1be5a64a9558f4e0f52b35c5add
- https://twitter.com/am0nsec/status/1412232114980982787

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_vss_ps_susp_load.yml)
