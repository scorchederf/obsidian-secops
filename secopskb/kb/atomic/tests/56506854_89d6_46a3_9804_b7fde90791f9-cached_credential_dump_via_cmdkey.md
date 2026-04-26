---
atomic_guid: "56506854-89d6-46a3-9804-b7fde90791f9"
title: "Cached Credential Dump via Cmdkey"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.005"
attack_technique_name: "OS Credential Dumping: Cached Domain Credentials"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.005/T1003.005.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "56506854-89d6-46a3-9804-b7fde90791f9"
  - "Cached Credential Dump via Cmdkey"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cached Credential Dump via Cmdkey

List credentials currently stored on the host via the built-in Windows utility cmdkey.exe
Credentials listed with Cmdkey only pertain to the current user
Passwords will not be displayed once they are stored
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey
https://www.peew.pw/blog/2017/11/26/exploring-cmdkey-an-edge-case-for-privilege-escalation

## Metadata

- Atomic GUID: 56506854-89d6-46a3-9804-b7fde90791f9
- Technique: T1003.005: OS Credential Dumping: Cached Domain Credentials
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1003.005/T1003.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.005]]

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
cmdkey /list
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.005/T1003.005.yaml)
