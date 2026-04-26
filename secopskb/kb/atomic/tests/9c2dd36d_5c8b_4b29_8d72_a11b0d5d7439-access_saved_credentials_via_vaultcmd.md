---
atomic_guid: "9c2dd36d-5c8b-4b29-8d72-a11b0d5d7439"
title: "Access Saved Credentials via VaultCmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.004"
attack_technique_name: "Credentials from Password Stores: Windows Credential Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.004/T1555.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "9c2dd36d-5c8b-4b29-8d72-a11b0d5d7439"
  - "Access Saved Credentials via VaultCmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Access Saved Credentials via VaultCmd

List credentials currently stored in Windows Credential Manager via the native Windows utility vaultcmd.exe
Credential Manager stores credentials for signing into websites, applications, and/or devices that request authentication through NTLM or Kerberos
https://blog.malwarebytes.com/101/2016/01/the-windows-vaults/
https://medium.com/threatpunter/detecting-adversary-tradecraft-with-image-load-event-logging-and-eql-8de93338c16

## Metadata

- Atomic GUID: 9c2dd36d-5c8b-4b29-8d72-a11b0d5d7439
- Technique: T1555.004: Credentials from Password Stores: Windows Credential Manager
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1555.004/T1555.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.004]]

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
vaultcmd /listcreds:"Windows Credentials"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.004/T1555.004.yaml)
