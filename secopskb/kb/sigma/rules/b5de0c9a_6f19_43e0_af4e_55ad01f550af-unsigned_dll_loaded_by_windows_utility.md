---
sigma_id: "b5de0c9a-6f19-43e0-af4e-55ad01f550af"
title: "Unsigned DLL Loaded by Windows Utility"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_susp_unsigned_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_unsigned_dll.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "b5de0c9a-6f19-43e0-af4e-55ad01f550af"
  - "Unsigned DLL Loaded by Windows Utility"
attack_technique_ids:
  - "T1218.011"
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unsigned DLL Loaded by Windows Utility

Detects windows utilities loading an unsigned or untrusted DLL.
Adversaries often abuse those programs to proxy execution of malicious code.

## Metadata

- Rule ID: b5de0c9a-6f19-43e0-af4e-55ad01f550af
- Status: test
- Level: medium
- Author: Swachchhanda Shrawan Poudel
- Date: 2024-02-28
- Modified: 2025-10-07
- Source Path: rules/windows/image_load/image_load_susp_unsigned_dll.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection:
  Image|endswith:
  - \InstallUtil.exe
  - \RegAsm.exe
  - \RegSvcs.exe
  - \regsvr32.exe
  - \rundll32.exe
filter_main_signed:
  Signed: 'true'
filter_main_sig_status:
  SignatureStatus:
  - errorChaining
  - errorCode_endpoint
  - errorExpired
  - trusted
  - Valid
filter_main_signed_null:
  Signed: null
filter_main_signed_empty:
  Signed:
  - ''
  - '-'
filter_main_sig_status_null:
  SignatureStatus: null
filter_main_sig_status_empty:
  SignatureStatus:
  - ''
  - '-'
filter_main_windows_installer:
  Image:
  - C:\Windows\SysWOW64\rundll32.exe
  - C:\Windows\System32\rundll32.exe
  ImageLoaded|startswith: C:\Windows\Installer\
  ImageLoaded|endswith:
  - .tmp-\Microsoft.Deployment.WindowsInstaller.dll
  - .tmp-\Avira.OE.Setup.CustomActions.dll
filter_main_assembly:
  Image|startswith:
  - C:\Windows\SysWOW64\
  - C:\Windows\System32\
  - C:\Windows\Microsoft.NET\Framework64
  Image|endswith: \RegAsm.exe
  ImageLoaded|endswith: .dll
  ImageLoaded|startswith: C:\Windows\assembly\NativeImages
filter_optional_klite_codec:
  Image:
  - C:\Windows\SysWOW64\regsvr32.exe
  - C:\Windows\System32\regsvr32.exe
  ImageLoaded|startswith:
  - C:\Program Files (x86)\K-Lite Codec Pack\
  - C:\Program Files\K-Lite Codec Pack\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://www.elastic.co/security-labs/Hunting-for-Suspicious-Windows-Libraries-for-Execution-and-Evasion
- https://akhere.hashnode.dev/hunting-unsigned-dlls-using-kql
- https://unit42.paloaltonetworks.com/unsigned-dlls/?web_view=true

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_unsigned_dll.yml)
