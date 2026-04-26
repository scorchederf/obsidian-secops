---
sigma_id: "65236ec7-ace0-4f0c-82fd-737b04fd4dcb"
title: "EVTX Created In Uncommon Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_create_evtx_non_common_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_create_evtx_non_common_locations.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "65236ec7-ace0-4f0c-82fd-737b04fd4dcb"
  - "EVTX Created In Uncommon Location"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# EVTX Created In Uncommon Location

Detects the creation of new files with the ".evtx" extension in non-common or non-standard location.
This could indicate tampering with default EVTX locations in order to evade security controls or simply exfiltration of event log to search for sensitive information within.
Note that backup software and legitimate administrator might perform similar actions during troubleshooting.

## Metadata

- Rule ID: 65236ec7-ace0-4f0c-82fd-737b04fd4dcb
- Status: test
- Level: medium
- Author: D3F7A5105
- Date: 2023-01-02
- Modified: 2024-03-26
- Source Path: rules/windows/file/file_event/file_event_win_create_evtx_non_common_locations.yml

## Logsource

- category: file_event
- definition: Requirements: The ".evtx" extension should be monitored via a Sysmon configuration. Example: <TargetFilename condition="end with">.evtx<TargetFilename>
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection:
  TargetFilename|endswith: .evtx
filter_main_path:
  TargetFilename|startswith: C:\Windows\System32\winevt\Logs\
filter_main_baseimage:
  TargetFilename|startswith: C:\ProgramData\Microsoft\Windows\Containers\BaseImages\
  TargetFilename|endswith: \Windows\System32\winevt\Logs\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Administrator or backup activity
- An unknown bug seems to trigger the Windows "svchost" process to drop EVTX files in the "C:\Windows\Temp" directory in the form "<log_name">_<uuid>.evtx". See https://superuser.com/questions/1371229/low-disk-space-after-filling-up-c-windows-temp-with-evtx-and-txt-files

## References

- https://learn.microsoft.com/en-us/windows/win32/eventlog/eventlog-key

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_create_evtx_non_common_locations.yml)
