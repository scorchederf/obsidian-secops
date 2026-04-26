---
atomic_guid: "8a930abe-841c-4d4f-a877-72e9fe90b9ea"
title: "Enable Apple Remote Desktop Agent"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.005"
attack_technique_name: "Remote Services:VNC"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.005/T1021.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "8a930abe-841c-4d4f-a877-72e9fe90b9ea"
  - "Enable Apple Remote Desktop Agent"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enable Apple Remote Desktop Agent

ARD leverages a blend of protocols, including VNC to send the screen and control buffers and SSH for secure file transfer. 
Adversaries can abuse ARD to gain remote code execution and perform lateral movement.

References:  https://www.mandiant.com/resources/blog/leveraging-apple-remote-desktop-for-good-and-evil

## Metadata

- Atomic GUID: 8a930abe-841c-4d4f-a877-72e9fe90b9ea
- Technique: T1021.005: Remote Services:VNC
- Platforms: macos
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1021.005/T1021.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.005]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -activate -configure -allowAccessFor -allUsers -privs -all -quiet
```

### Cleanup

```bash
sudo /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -deactivate -stop -configure -privs -none -quiet
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.005/T1021.005.yaml)
