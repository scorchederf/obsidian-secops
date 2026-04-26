---
sigma_id: "c4b890e5-8d8c-4496-8c66-c805753817cd"
title: "Potential Process Hollowing Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_tampering/proc_tampering_susp_process_hollowing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_tampering/proc_tampering_susp_process_hollowing.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_tampering"
aliases:
  - "c4b890e5-8d8c-4496-8c66-c805753817cd"
  - "Potential Process Hollowing Activity"
attack_technique_ids:
  - "T1055.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Process Hollowing Activity

Detects when a memory process image does not match the disk image, indicative of process hollowing.

## Metadata

- Rule ID: c4b890e5-8d8c-4496-8c66-c805753817cd
- Status: test
- Level: medium
- Author: Christopher Peacock '@securepeacock', SCYTHE '@scythe_io', Sittikorn S
- Date: 2022-01-25
- Modified: 2023-11-28
- Source Path: rules/windows/process_tampering/proc_tampering_susp_process_hollowing.yml

## Logsource

- category: process_tampering
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.012]]

## Detection

```yaml
selection:
  Type: Image is replaced
filter_main_generic:
  Image|contains:
  - :\Program Files (x86)
  - :\Program Files\
  - :\Windows\System32\wbem\WMIADAP.exe
  - :\Windows\SysWOW64\wbem\WMIADAP.exe
filter_optional_opera:
  Image|contains: \AppData\Local\Programs\Opera\
  Image|endswith: \opera.exe
filter_optional_edge:
  Image|endswith: \WindowsApps\MicrosoftEdge.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://twitter.com/SecurePeacock/status/1486054048390332423?s=20
- https://www.bleepingcomputer.com/news/microsoft/microsoft-sysmon-now-detects-malware-process-tampering-attempts/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_tampering/proc_tampering_susp_process_hollowing.yml)
