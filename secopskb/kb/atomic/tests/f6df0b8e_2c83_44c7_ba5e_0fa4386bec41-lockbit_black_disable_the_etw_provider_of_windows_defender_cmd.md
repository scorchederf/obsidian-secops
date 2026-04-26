---
atomic_guid: "f6df0b8e-2c83-44c7-ba5e-0fa4386bec41"
title: "LockBit Black - Disable the ETW Provider of Windows Defender -cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "f6df0b8e-2c83-44c7-ba5e-0fa4386bec41"
  - "LockBit Black - Disable the ETW Provider of Windows Defender -cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LockBit Black - Disable the ETW Provider of Windows Defender -cmd

An adversary can disable the ETW Provider of Windows Defender,
so nothing would be logged to Microsoft-Windows-Windows-Defender/Operational anymore.
https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a

## Metadata

- Atomic GUID: f6df0b8e-2c83-44c7-ba5e-0fa4386bec41
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Windows Defender/Operational" /v Enabled /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Windows Defender/Operational" /v Enabled /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
