---
title: "VisualUiaVerifyNative.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/VisualUiaVerifyNative.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/VisualUiaVerifyNative.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "VisualUiaVerifyNative.exe"
functions:
  - "AWL Bypass"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# VisualUiaVerifyNative.exe

A Windows SDK binary for manual and automated testing of Microsoft UI Automation implementation and controls.

## Metadata

- Category: OtherMSBinaries
- Created: 2021-09-26
- Author: Jimmy (@bohops)
- Source Path: yml/OtherMSBinaries/VisualUiaVerifyNative.yml

## Paths

- `c:\Program Files (x86)\Windows Kits\10\bin\<version>\arm64\UIAVerify\VisualUiaVerifyNative.exe`
- `c:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\UIAVerify\VisualUiaVerifyNative.exe`
- `c:\Program Files (x86)\Windows Kits\10\bin\<version>\UIAVerify\VisualUiaVerifyNative.exe`

## Commands

### 1. AWL Bypass

Generate Serialized gadget and save to - `C:\Users\%USERNAME%\AppData\Roaminguiverify.config` before executing.

```cmd
VisualUiaVerifyNative.exe
```

- Use Case: Execute proxied payload with Microsoft signed binary to bypass WDAC policies
- Privileges: User
- Operating System: Windows 10 2004 (likely previous and newer versions as well)
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/6b34764215b0e97e32cbc4c6325fc933d2695c3a/rules/windows/process_creation/proc_creation_win_lolbin_visualuiaverifynative.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious

## Resources

- {'Link': 'https://bohops.com/2020/10/15/exploring-the-wdac-microsoft-recommended-block-rules-visualuiaverifynative/'}
- {'Link': 'https://github.com/MicrosoftDocs/windows-itpro-docs/commit/937db704b9148e9cee7c7010cad4d00ce9c4fdad'}

## Acknowledgements

- {'Person': 'Lee Christensen', 'Handle': '@tifkin'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/VisualUiaVerifyNative.yml)
