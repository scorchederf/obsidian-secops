---
sigma_id: "6f4191bb-912b-48a8-9ce7-682769541e6d"
title: "Suspicious Msiexec Execute Arbitrary DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msiexec_execute_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_execute_dll.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6f4191bb-912b-48a8-9ce7-682769541e6d"
  - "Suspicious Msiexec Execute Arbitrary DLL"
attack_technique_ids:
  - "T1218.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Msiexec Execute Arbitrary DLL

Adversaries may abuse msiexec.exe to proxy execution of malicious payloads.
Msiexec.exe is the command-line utility for the Windows Installer and is thus commonly associated with executing installation packages (.msi)

## Metadata

- Rule ID: 6f4191bb-912b-48a8-9ce7-682769541e6d
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-16
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_msiexec_execute_dll.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Detection

```yaml
selection:
  Image|endswith: \msiexec.exe
  CommandLine|contains|windash: ' -y'
filter_apple:
  CommandLine|contains:
  - \MsiExec.exe" /Y "C:\Program Files\Bonjour\mdnsNSP.dll
  - \MsiExec.exe" /Y "C:\Program Files (x86)\Bonjour\mdnsNSP.dll
  - \MsiExec.exe" /Y "C:\Program Files (x86)\Apple Software Update\ScriptingObjectModel.dll
  - \MsiExec.exe" /Y "C:\Program Files (x86)\Apple Software Update\SoftwareUpdateAdmin.dll
  - \MsiExec.exe" /Y "C:\Windows\CCM\
  - \MsiExec.exe" /Y C:\Windows\CCM\
  - \MsiExec.exe" -Y "C:\Program Files\Bonjour\mdnsNSP.dll
  - \MsiExec.exe" -Y "C:\Program Files (x86)\Bonjour\mdnsNSP.dll
  - \MsiExec.exe" -Y "C:\Program Files (x86)\Apple Software Update\ScriptingObjectModel.dll
  - \MsiExec.exe" -Y "C:\Program Files (x86)\Apple Software Update\SoftwareUpdateAdmin.dll
  - \MsiExec.exe" -Y "C:\Windows\CCM\
  - \MsiExec.exe" -Y C:\Windows\CCM\
condition: selection and not 1 of filter_*
```

## False Positives

- Legitimate script

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.007/T1218.007.md
- https://twitter.com/_st0pp3r_/status/1583914515996897281

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_execute_dll.yml)
