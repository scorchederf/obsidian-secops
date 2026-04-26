---
atomic_guid: "f650456b-bd49-4bc1-ae9d-271b5b9581e7"
title: "Hide Files Through Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.001"
attack_technique_name: "Hide Artifacts: Hidden Files and Directories"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "f650456b-bd49-4bc1-ae9d-271b5b9581e7"
  - "Hide Files Through Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hide Files Through Registry

Disable Show Hidden files switch in registry. This technique was abused by several malware to hide their files from normal user.
See how this trojan abuses this technique - https://www.sophos.com/en-us/threat-center/threat-analyses/viruses-and-spyware/W32~Tiotua-P/detailed-analysis.aspx

## Metadata

- Atomic GUID: f650456b-bd49-4bc1-ae9d-271b5b9581e7
- Technique: T1564.001: Hide Artifacts: Hidden Files and Directories
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1564.001/T1564.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v ShowSuperHidden /t REG_DWORD /d 0 /f
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v Hidden /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v ShowSuperHidden /f >nul 2>&1
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v Hidden /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.001/T1564.001.yaml)
