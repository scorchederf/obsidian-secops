---
sigma_id: "9d15044a-7cfe-4d23-8085-6ebc11df7685"
title: "Potential Persistence Via Visual Studio Tools for Office"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_office_vsto.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_office_vsto.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "9d15044a-7cfe-4d23-8085-6ebc11df7685"
  - "Potential Persistence Via Visual Studio Tools for Office"
attack_technique_ids:
  - "T1137.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Visual Studio Tools for Office

Detects persistence via Visual Studio Tools for Office (VSTO) add-ins in Office applications.

## Metadata

- Rule ID: 9d15044a-7cfe-4d23-8085-6ebc11df7685
- Status: test
- Level: medium
- Author: Bhabesh Raj
- Date: 2021-01-10
- Modified: 2025-10-07
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_office_vsto.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137.006]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Software\Microsoft\Office\Outlook\Addins\
  - \Software\Microsoft\Office\Word\Addins\
  - \Software\Microsoft\Office\Excel\Addins\
  - \Software\Microsoft\Office\Powerpoint\Addins\
  - \Software\Microsoft\VSTO\Security\Inclusion\
filter_main_system:
  Image:
  - C:\Windows\System32\msiexec.exe
  - C:\Windows\SysWOW64\msiexec.exe
  - C:\Windows\System32\regsvr32.exe
  - C:\Windows\SysWOW64\regsvr32.exe
filter_main_office_click_to_run:
  Image|startswith:
  - C:\Program Files\Common Files (x86)\Microsoft Shared\ClickToRun\
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\
  Image|endswith: \OfficeClickToRun.exe
filter_main_integrator:
  Image:
  - C:\Program Files (x86)\Microsoft Office\root\integration\integrator.exe
  - C:\Program Files\Microsoft Office\root\integration\integrator.exe
filter_main_office_apps:
  Image|startswith:
  - C:\Program Files\Microsoft Office\OFFICE
  - C:\Program Files (x86)\Microsoft Office\OFFICE
  - C:\Program Files\Microsoft Office\Root\OFFICE
  - C:\Program Files (x86)\Microsoft Office\Root\OFFICE
  Image|endswith:
  - \excel.exe
  - \Integrator.exe
  - \outlook.exe
  - \powerpnt.exe
  - \Teams.exe
  - \visio.exe
  - \winword.exe
filter_optional_avg:
  Image:
  - C:\Program Files\AVG\Antivirus\RegSvr.exe
  - C:\Program Files (x86)\AVG\Antivirus\RegSvr.exe
  TargetObject|contains: \Microsoft\Office\Outlook\Addins\Antivirus.AsOutExt\
filter_optional_avast:
  Image:
  - C:\Program Files\Avast Software\Avast\RegSvr.exe
  - C:\Program Files (x86)\Avast Software\Avast\RegSvr.exe
  TargetObject|contains: \Microsoft\Office\Outlook\Addins\Avast.AsOutExt\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate Addin Installation

## References

- https://twitter.com/_vivami/status/1347925307643355138
- https://vanmieghem.io/stealth-outlook-persistence/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_office_vsto.yml)
