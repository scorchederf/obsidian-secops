---
sigma_id: "8cd538a4-62d5-4e83-810b-12d41e428d6e"
title: "Processes Accessing the Microphone and Webcam"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_camera_microphone_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_camera_microphone_access.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "8cd538a4-62d5-4e83-810b-12d41e428d6e"
  - "Processes Accessing the Microphone and Webcam"
attack_technique_ids:
  - "T1123"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Processes Accessing the Microphone and Webcam

Potential adversaries accessing the microphone and webcam in an endpoint.

## Metadata

- Rule ID: 8cd538a4-62d5-4e83-810b-12d41e428d6e
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-06-07
- Modified: 2021-11-27
- Source Path: rules/windows/builtin/security/win_security_camera_microphone_access.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1123-audio_capture|T1123]]

## Detection

```yaml
selection:
  EventID:
  - 4657
  - 4656
  - 4663
  ObjectName|contains:
  - \SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone\NonPackaged
  - \SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam\NonPackaged
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/duzvik/status/1269671601852813320
- https://medium.com/@7a616368/can-you-track-processes-accessing-the-camera-and-microphone-7e6885b37072

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_camera_microphone_access.yml)
