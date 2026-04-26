---
sigma_id: "c7a74c80-ba5a-486e-9974-ab9e682bc5e4"
title: "File With Uncommon Extension Created By An Office Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_susp_file_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_susp_file_extension.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "c7a74c80-ba5a-486e-9974-ab9e682bc5e4"
  - "File With Uncommon Extension Created By An Office Application"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File With Uncommon Extension Created By An Office Application

Detects the creation of files with an executable or script extension by an Office application.

## Metadata

- Rule ID: c7a74c80-ba5a-486e-9974-ab9e682bc5e4
- Status: test
- Level: high
- Author: Vadim Khrykov (ThreatIntel), Cyb3rEng (Rule), Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-08-23
- Modified: 2025-10-17
- Source Path: rules/windows/file/file_event/file_event_win_office_susp_file_extension.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection1:
  Image|endswith:
  - \excel.exe
  - \msaccess.exe
  - \mspub.exe
  - \powerpnt.exe
  - \visio.exe
  - \winword.exe
selection2:
  TargetFilename|endswith:
  - .bat
  - .cmd
  - .com
  - .dll
  - .exe
  - .hta
  - .ocx
  - .proj
  - .ps1
  - .scf
  - .scr
  - .sys
  - .vbe
  - .vbs
  - .wsf
  - .wsh
filter_main_localassembly:
  TargetFilename|contains: \AppData\Local\assembly\tmp\
  TargetFilename|endswith: .dll
filter_optional_webservicecache:
  TargetFilename|contains|all:
  - C:\Users\
  - \AppData\Local\Microsoft\Office\
  - \WebServiceCache\AllUsers
  TargetFilename|endswith: .com
filter_optional_webex:
  Image|endswith: \winword.exe
  TargetFilename|contains: \AppData\Local\Temp\webexdelta\
  TargetFilename|endswith:
  - .dll
  - .exe
filter_optional_backstageinappnavcache:
  TargetFilename|contains|all:
  - C:\Users\
  - \AppData\Local\Microsoft\Office\
  - \BackstageInAppNavCache\
  TargetFilename|endswith: .com
condition: all of selection* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/
- https://github.com/vadim-hunter/Detection-Ideas-Rules/blob/02bcbfc2bfb8b4da601bb30de0344ae453aa1afe/Threat%20Intelligence/The%20DFIR%20Report/20210329_Sodinokibi_(aka_REvil)_Ransomware.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_susp_file_extension.yml)
