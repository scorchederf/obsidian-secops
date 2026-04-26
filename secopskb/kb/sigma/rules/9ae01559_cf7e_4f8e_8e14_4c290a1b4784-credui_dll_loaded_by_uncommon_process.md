---
sigma_id: "9ae01559-cf7e-4f8e-8e14-4c290a1b4784"
title: "CredUI.DLL Loaded By Uncommon Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_credui_uncommon_process_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_credui_uncommon_process_load.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "9ae01559-cf7e-4f8e-8e14-4c290a1b4784"
  - "CredUI.DLL Loaded By Uncommon Process"
attack_technique_ids:
  - "T1056.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CredUI.DLL Loaded By Uncommon Process

Detects loading of "credui.dll" and related DLLs by an uncommon process. Attackers might leverage this DLL for potential use of "CredUIPromptForCredentials" or "CredUnPackAuthenticationBufferW".

## Metadata

- Rule ID: 9ae01559-cf7e-4f8e-8e14-4c290a1b4784
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-10-20
- Modified: 2025-12-09
- Source Path: rules/windows/image_load/image_load_dll_credui_uncommon_process_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1056-input_capture|T1056.002]]

## Detection

```yaml
selection:
- ImageLoaded|endswith:
  - \credui.dll
  - \wincredui.dll
- OriginalFileName:
  - credui.dll
  - wincredui.dll
filter_main_generic:
  Image|startswith:
  - C:\Program Files (x86)\
  - C:\Program Files\
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\SystemApps\
filter_main_full:
  Image:
  - C:\Windows\explorer.exe
  - C:\Windows\ImmersiveControlPanel\SystemSettings.exe
  - C:\Windows\regedit.exe
filter_optional_opera:
  Image|endswith: \opera_autoupdate.exe
filter_optional_process_explorer:
  Image|endswith:
  - \procexp64.exe
  - \procexp.exe
filter_optional_teams:
  Image|startswith: C:\Users\
  Image|contains: \AppData\Local\Microsoft\Teams\
  Image|endswith: \Teams.exe
filter_optional_onedrive:
  Image|startswith: C:\Users\
  Image|contains: \AppData\Local\Microsoft\OneDrive\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Other legitimate processes loading those DLLs in your environment.

## References

- https://securitydatasets.com/notebooks/atomic/windows/credential_access/SDWIN-201020013208.html
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1056.002/T1056.002.md#atomic-test-2---powershell---prompt-user-for-password
- https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-creduipromptforcredentialsa
- https://github.com/S12cybersecurity/RDPCredentialStealer

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_credui_uncommon_process_load.yml)
