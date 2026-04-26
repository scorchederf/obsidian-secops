---
sigma_id: "baecf8fb-edbf-429f-9ade-31fc3f22b970"
title: "Office Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_office.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_office.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "baecf8fb-edbf-429f-9ade-31fc3f22b970"
  - "Office Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Office Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: baecf8fb-edbf-429f-9ade-31fc3f22b970
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2025-10-17
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_office.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection_office_root:
  TargetObject|contains:
  - \Software\Wow6432Node\Microsoft\Office
  - \Software\Microsoft\Office
selection_office_details:
  TargetObject|contains:
  - \Word\Addins
  - \PowerPoint\Addins
  - \Outlook\Addins
  - \Onenote\Addins
  - \Excel\Addins
  - \Access\Addins
  - test\Special\Perf
filter_main_empty:
  Details: (Empty)
filter_main_known_addins:
  Image|startswith:
  - C:\Program Files\Microsoft Office\
  - C:\Program Files (x86)\Microsoft Office\
  - C:\Windows\System32\msiexec.exe
  - C:\Windows\System32\regsvr32.exe
  TargetObject|contains:
  - \Excel\Addins\AdHocReportingExcelClientLib.AdHocReportingExcelClientAddIn.1\
  - \Excel\Addins\ExcelPlugInShell.PowerMapConnect\
  - \Excel\Addins\NativeShim\
  - \Excel\Addins\NativeShim.InquireConnector.1\
  - \Excel\Addins\PowerPivotExcelClientAddIn.NativeEntry.1\
  - \Outlook\AddIns\AccessAddin.DC\
  - \Outlook\AddIns\ColleagueImport.ColleagueImportAddin\
  - \Outlook\AddIns\EvernoteCC.EvernoteContactConnector\
  - \Outlook\AddIns\EvernoteOLRD.Connect\
  - \Outlook\Addins\Microsoft.VbaAddinForOutlook.1\
  - \Outlook\Addins\OcOffice.OcForms\
  - \Outlook\Addins\\OneNote.OutlookAddin
  - \Outlook\Addins\OscAddin.Connect\
  - \Outlook\Addins\OutlookChangeNotifier.Connect\
  - \Outlook\Addins\UCAddin.LyncAddin.1
  - \Outlook\Addins\UCAddin.UCAddin.1
  - \Outlook\Addins\UmOutlookAddin.FormRegionAddin\
  - AddinTakeNotesService\FriendlyName
filter_main_officeclicktorun:
  Image|startswith:
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\Updates\
  Image|endswith: \OfficeClickToRun.exe
filter_optional_avg:
  Image:
  - C:\Program Files\AVG\Antivirus\RegSvr.exe
  - C:\Program Files\AVG\Antivirus\x86\RegSvr.exe
  TargetObject|contains: \Microsoft\Office\Outlook\Addins\Antivirus.AsOutExt\
filter_optional_avast:
  Image:
  - C:\Program Files\Avast Software\Avast\RegSvr.exe
  - C:\Program Files\Avast Software\Avast\x86\RegSvr.exe
  TargetObject|contains: \Microsoft\Office\Outlook\Addins\Avast.AsOutExt\
condition: all of selection_office_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_office.yml)
