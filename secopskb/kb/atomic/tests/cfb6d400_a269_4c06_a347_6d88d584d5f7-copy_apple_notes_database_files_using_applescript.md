---
atomic_guid: "cfb6d400-a269-4c06-a347-6d88d584d5f7"
title: "Copy Apple Notes database files using AppleScript"
framework: "atomic"
generated: "true"
attack_technique_id: "T1005"
attack_technique_name: "Data from Local System"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1005/T1005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "cfb6d400-a269-4c06-a347-6d88d584d5f7"
  - "Copy Apple Notes database files using AppleScript"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy Apple Notes database files using AppleScript

This command will copy Apple Notes database files using AppleScript as seen in Atomic Stealer.

## Metadata

- Atomic GUID: cfb6d400-a269-4c06-a347-6d88d584d5f7
- Technique: T1005: Data from Local System
- Platforms: macos
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1005/T1005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Input Arguments

### destination_path

- description: Specify the path to copy the database files into.
- type: path
- default: /private/tmp

## Executor

- elevation_required: False
- name: sh

### Command

```bash
osascript -e 'tell application "Finder"' -e 'set destinationFolderPath to POSIX file "#{destination_path}"' -e 'set notesFolderPath to (path to home folder as text) & "Library:Group Containers:group.com.apple.notes:"' -e 'set notesFolder to folder notesFolderPath' -e 'set notesFiles to {file "NoteStore.sqlite", file "NoteStore.sqlite-shm", file "NoteStore.sqlite-wal"} of notesFolder' -e 'repeat with aFile in notesFiles' -e 'duplicate aFile to folder destinationFolderPath with replacing' -e 'end' -e 'end tell'
```

### Cleanup

```bash
rm "#{destination_path}/NoteStore.sqlite*"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1005/T1005.yaml)
