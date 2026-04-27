---
atomic_guid: "8a930abe-841c-4d4f-a877-72e9fe90b9ea"
title: "Enable Apple Remote Desktop Agent"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.005"
attack_technique_name: "Remote Services:VNC"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.005/T1021.005.yaml"
build_date: "2026-04-27 19:12:25"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

ARD leverages a blend of protocols, including VNC to send the screen and control buffers and SSH for secure file transfer. 
Adversaries can abuse ARD to gain remote code execution and perform lateral movement.

References:  https://www.mandiant.com/resources/blog/leveraging-apple-remote-desktop-for-good-and-evil

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]

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
