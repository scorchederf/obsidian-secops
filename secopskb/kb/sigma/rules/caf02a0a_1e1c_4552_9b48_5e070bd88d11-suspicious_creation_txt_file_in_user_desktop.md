---
sigma_id: "caf02a0a-1e1c-4552-9b48-5e070bd88d11"
title: "Suspicious Creation TXT File in User Desktop"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_desktop_txt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_desktop_txt.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "caf02a0a-1e1c-4552-9b48-5e070bd88d11"
  - "Suspicious Creation TXT File in User Desktop"
attack_technique_ids:
  - "T1486"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Creation TXT File in User Desktop

Ransomware create txt file in the user Desktop

## Metadata

- Rule ID: caf02a0a-1e1c-4552-9b48-5e070bd88d11
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-26
- Source Path: rules/windows/file/file_event/file_event_win_susp_desktop_txt.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Detection

```yaml
selection:
  Image|endswith: \cmd.exe
  TargetFilename|contains|all:
  - \Users\
  - \Desktop\
  TargetFilename|endswith: .txt
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1486/T1486.md#atomic-test-5---purelocker-ransom-note

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_desktop_txt.yml)
