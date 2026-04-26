---
atomic_guid: "6581e4a7-42e3-43c5-a0d2-5a0d62f9702a"
title: "Registry artefact when application use webcam"
framework: "atomic"
generated: "true"
attack_technique_id: "T1125"
attack_technique_name: "Video Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1125/T1125.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "6581e4a7-42e3-43c5-a0d2-5a0d62f9702a"
  - "Registry artefact when application use webcam"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry artefact when application use webcam

[can-you-track-processes-accessing-the-camera-and-microphone](https://svch0st.medium.com/can-you-track-processes-accessing-the-camera-and-microphone-7e6885b37072)

## Metadata

- Atomic GUID: 6581e4a7-42e3-43c5-a0d2-5a0d62f9702a
- Technique: T1125: Video Capture
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1125/T1125.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1125-video_capture|T1125]]

## Executor

- name: command_prompt

### Command

```cmd
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam\NonPackaged\C:#Windows#Temp#atomic.exe /v LastUsedTimeStart /t REG_BINARY /d a273b6f07104d601 /f
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam\NonPackaged\C:#Windows#Temp#atomic.exe /v LastUsedTimeStop /t REG_BINARY /d 96ef514b7204d601 /f
```

### Cleanup

```cmd
reg DELETE HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam\NonPackaged\C:#Windows#Temp#atomic.exe /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1125/T1125.yaml)
