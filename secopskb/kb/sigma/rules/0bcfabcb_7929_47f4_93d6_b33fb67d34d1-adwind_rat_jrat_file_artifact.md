---
sigma_id: "0bcfabcb-7929-47f4-93d6-b33fb67d34d1"
title: "Adwind RAT / JRAT File Artifact"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_mal_adwind.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_mal_adwind.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "0bcfabcb-7929-47f4-93d6-b33fb67d34d1"
  - "Adwind RAT / JRAT File Artifact"
attack_technique_ids:
  - "T1059.005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Adwind RAT / JRAT File Artifact

Detects javaw.exe in AppData folder as used by Adwind / JRAT

## Metadata

- Rule ID: 0bcfabcb-7929-47f4-93d6-b33fb67d34d1
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Tom Ueltschi, Jonhnathan Ribeiro, oscd.community
- Date: 2017-11-10
- Modified: 2022-12-02
- Source Path: rules/windows/file/file_event/file_event_win_mal_adwind.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection:
- TargetFilename|contains|all:
  - \AppData\Roaming\Oracle\bin\java
  - .exe
- TargetFilename|contains|all:
  - \Retrive
  - .vbs
condition: selection
```

## References

- https://www.hybrid-analysis.com/sample/ba86fa0d4b6af2db0656a88b1dd29f36fe362473ae8ad04255c4e52f214a541c?environmentId=100
- https://www.first.org/resources/papers/conf2017/Advanced-Incident-Detection-and-Threat-Hunting-using-Sysmon-and-Splunk.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_mal_adwind.yml)
