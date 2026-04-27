---
atomic_guid: "84113186-ed3c-4d0d-8a3c-8980c86c1f4a"
title: "Dump Credential Manager using keymgr.dll and rundll32.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003"
attack_technique_name: "OS Credential Dumping"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "84113186-ed3c-4d0d-8a3c-8980c86c1f4a"
  - "Dump Credential Manager using keymgr.dll and rundll32.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test executes the exported function `KRShowKeyMgr` located in `keymgr.dll` using `rundll32.exe`. It opens a window that allows to export stored Windows credentials from the credential manager to a file (`.crd` by default). The file can then be retrieved and imported on an attacker-controlled computer to list the credentials get the passwords. The only limitation is that it requires a CTRL+ALT+DELETE input from the attacker, which can be achieve multiple ways (e.g. a custom implant with remote control capabilities, enabling RDP, etc.).
Reference: https://twitter.com/0gtweet/status/1415671356239216653

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

## Executor

- name: powershell

### Command

```powershell
rundll32.exe keymgr,KRShowKeyMgr
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml)
