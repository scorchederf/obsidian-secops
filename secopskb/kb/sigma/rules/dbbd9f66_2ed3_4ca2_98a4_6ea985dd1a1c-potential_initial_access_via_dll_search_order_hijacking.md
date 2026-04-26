---
sigma_id: "dbbd9f66-2ed3-4ca2-98a4-6ea985dd1a1c"
title: "Potential Initial Access via DLL Search Order Hijacking"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_initial_access_dll_search_order_hijacking.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_initial_access_dll_search_order_hijacking.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "dbbd9f66-2ed3-4ca2-98a4-6ea985dd1a1c"
  - "Potential Initial Access via DLL Search Order Hijacking"
attack_technique_ids:
  - "T1566"
  - "T1566.001"
  - "T1574"
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Initial Access via DLL Search Order Hijacking

Detects attempts to create a DLL file to a known desktop application dependencies folder such as Slack, Teams or OneDrive and by an unusual process. This may indicate an attempt to load a malicious module via DLL search order hijacking.

## Metadata

- Rule ID: dbbd9f66-2ed3-4ca2-98a4-6ea985dd1a1c
- Status: test
- Level: medium
- Author: Tim Rauch (rule), Elastic (idea)
- Date: 2022-10-21
- Source Path: rules/windows/file/file_event/file_event_win_initial_access_dll_search_order_hijacking.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566]]
- [[kb/attack/techniques/T1566-phishing|T1566.001]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \winword.exe
  - \excel.exe
  - \powerpnt.exe
  - \MSACCESS.EXE
  - \MSPUB.EXE
  - \fltldr.exe
  - \cmd.exe
  - \certutil.exe
  - \mshta.exe
  - \cscript.exe
  - \wscript.exe
  - \curl.exe
  - \powershell.exe
  - \pwsh.exe
  TargetFilename|endswith: .dll
  TargetFilename|contains|all:
  - \Users\
  - \AppData\
  TargetFilename|contains:
  - \Microsoft\OneDrive\
  - \Microsoft OneDrive\
  - \Microsoft\Teams\
  - \Local\slack\app-
  - \Local\Programs\Microsoft VS Code\
filter:
  Image|endswith: \cmd.exe
  TargetFilename|contains|all:
  - \Users\
  - \AppData\
  - \Microsoft\OneDrive\
  - \api-ms-win-core-
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/elastic/protections-artifacts/commit/746086721fd385d9f5c6647cada1788db4aea95f#diff-5d46dd4ac6866b4337ec126be8cee0e115467b3e8703794ba6f6df6432c806bc
- https://posts.specterops.io/automating-dll-hijack-discovery-81c4295904b0

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_initial_access_dll_search_order_hijacking.yml)
