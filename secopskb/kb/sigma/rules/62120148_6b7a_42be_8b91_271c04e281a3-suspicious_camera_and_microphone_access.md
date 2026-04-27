---
sigma_id: "62120148-6b7a-42be-8b91-271c04e281a3"
title: "Suspicious Camera and Microphone Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_susp_mic_cam_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_mic_cam_access.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "62120148-6b7a-42be-8b91-271c04e281a3"
  - "Suspicious Camera and Microphone Access"
attack_technique_ids:
  - "T1125"
  - "T1123"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Processes accessing the camera and microphone from suspicious folder

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1125-video_capture|T1125: Video Capture]]
- [[kb/attack/techniques/T1123-audio_capture|T1123: Audio Capture]]

## Detection

```yaml
selection_1:
  TargetObject|contains|all:
  - \Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\
  - \NonPackaged
selection_2:
  TargetObject|contains:
  - microphone
  - webcam
selection_3:
  TargetObject|contains:
  - :#Windows#Temp#
  - :#$Recycle.bin#
  - :#Temp#
  - :#Users#Public#
  - :#Users#Default#
  - :#Users#Desktop#
condition: all of selection_*
```

## False Positives

- Unlikely, there could be conferencing software running from a Temp folder accessing the devices

## References

- https://medium.com/@7a616368/can-you-track-processes-accessing-the-camera-and-microphone-7e6885b37072

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_mic_cam_access.yml)
