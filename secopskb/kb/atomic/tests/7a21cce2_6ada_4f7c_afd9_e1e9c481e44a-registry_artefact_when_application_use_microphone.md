---
atomic_guid: "7a21cce2-6ada-4f7c-afd9-e1e9c481e44a"
title: "Registry artefact when application use microphone"
framework: "atomic"
generated: "true"
attack_technique_id: "T1123"
attack_technique_name: "Audio Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1123/T1123.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "7a21cce2-6ada-4f7c-afd9-e1e9c481e44a"
  - "Registry artefact when application use microphone"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry artefact when application use microphone

[can-you-track-processes-accessing-the-camera-and-microphone](https://svch0st.medium.com/can-you-track-processes-accessing-the-camera-and-microphone-7e6885b37072)

## Metadata

- Atomic GUID: 7a21cce2-6ada-4f7c-afd9-e1e9c481e44a
- Technique: T1123: Audio Capture
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1123/T1123.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1123-audio_capture|T1123]]

## Executor

- name: command_prompt

### Command

```commandprompt
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone\NonPackaged\C:#Windows#Temp#atomic.exe /v LastUsedTimeStart /t REG_BINARY /d a273b6f07104d601 /f
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone\NonPackaged\C:#Windows#Temp#atomic.exe /v LastUsedTimeStop /t REG_BINARY /d 96ef514b7204d601 /f
```

### Cleanup

```commandprompt
reg DELETE HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone\NonPackaged\C:#Windows#Temp#atomic.exe /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1123/T1123.yaml)
