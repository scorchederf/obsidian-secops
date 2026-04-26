---
atomic_guid: "6c4ac96f-d4fa-44f4-83ca-56d8f4a55c02"
title: "Enable Local and Remote Symbolic Links via fsutil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222"
attack_technique_name: "File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222/T1222.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "6c4ac96f-d4fa-44f4-83ca-56d8f4a55c02"
  - "Enable Local and Remote Symbolic Links via fsutil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enable Local and Remote Symbolic Links via fsutil

Use fsutil to enable both ‘remote to local’ and ‘remote to remote’ symbolic links. This allows access to files from local shortcuts with local or remote paths.
[reference](https://symantec-enterprise-blogs.security.com/threat-intelligence/noberus-blackcat-alphv-rust-ransomware/)

## Metadata

- Atomic GUID: 6c4ac96f-d4fa-44f4-83ca-56d8f4a55c02
- Technique: T1222: File and Directory Permissions Modification
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1222/T1222.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
fsutil behavior set SymlinkEvaluation R2L:1
fsutil behavior set SymlinkEvaluation R2R:1
```

### Cleanup

```cmd
fsutil behavior set SymlinkEvaluation R2L:0
fsutil behavior set SymlinkEvaluation R2R:0
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222/T1222.yaml)
