---
atomic_guid: "c7a0bb71-70ce-4a53-b115-881f241b795b"
title: "using Quicktime Player"
framework: "atomic"
generated: "true"
attack_technique_id: "T1123"
attack_technique_name: "Audio Capture"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1123/T1123.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "c7a0bb71-70ce-4a53-b115-881f241b795b"
  - "using Quicktime Player"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# using Quicktime Player

Use AppleScript to get Quicktime Player to record an audio file from the default microphone.

Should create a non-empty m4a file with sound from the microphone.

- requires Automation permissions but no additional microphone permissions
- saves file in /tmp by default. Other locations likely to require more permissions.

## Metadata

- Atomic GUID: c7a0bb71-70ce-4a53-b115-881f241b795b
- Technique: T1123: Audio Capture
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1123/T1123.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1123-audio_capture|T1123]]

## Input Arguments

### audiofile

- description: Location of the recorded audio file
- type: path
- default: /tmp/T1123.m4a

### duration

- description: Length of recording to make in seconds
- type: integer
- default: 5

### filename

- description: Location of the script
- type: path
- default: PathToAtomicsFolder/T1123/src/T1123.sh

## Executor

- name: sh

### Command

```bash
sh #{filename} #{audiofile} #{duration}
```

### Cleanup

```bash
if test -w #{audiofile}; then
  rm #{audiofile}
fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1123/T1123.yaml)
