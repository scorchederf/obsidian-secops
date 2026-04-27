---
atomic_guid: "9c3ad250-b185-4444-b5a9-d69218a10c95"
title: "using device audio capture commandlet"
framework: "atomic"
generated: "true"
attack_technique_id: "T1123"
attack_technique_name: "Audio Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1123/T1123.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "9c3ad250-b185-4444-b5a9-d69218a10c95"
  - "using device audio capture commandlet"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Uses AudioDeviceCmdlets to set the default recording device and simulate audio capture.
Module repo: [AudioDeviceCmdlets](https://github.com/frgnca/AudioDeviceCmdlets)

## ATT&CK Mapping

- [[kb/attack/techniques/T1123-audio_capture|T1123: Audio Capture]]

## Dependencies

AudioDeviceCmdlets module must be installed

### Prerequisite Check

```untitled
if (Get-Module -ListAvailable -Name AudioDeviceCmdlets) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```untitled
Install with: Install-Module -Name AudioDeviceCmdlets -Force"
```

## Executor

- name: powershell

### Command

```powershell
$mic = Get-AudioDevice -Recording
Set-AudioDevice -ID $mic.ID
Start-Sleep -Seconds 5
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1123/T1123.yaml)
