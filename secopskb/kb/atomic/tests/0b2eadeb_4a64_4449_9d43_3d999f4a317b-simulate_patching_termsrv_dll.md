---
atomic_guid: "0b2eadeb-4a64-4449-9d43-3d999f4a317b"
title: "Simulate Patching termsrv.dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1505.005"
attack_technique_name: "Server Software Component: Terminal Services DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.005/T1505.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "0b2eadeb-4a64-4449-9d43-3d999f4a317b"
  - "Simulate Patching termsrv.dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Simulate Patching termsrv.dll

Simulates patching of termsrv.dll by making a benign change to the file and replacing it with the original afterwards.
Before we can make the modifications we need to take ownership of the file and grant ourselves the necessary permissions.

## Metadata

- Atomic GUID: 0b2eadeb-4a64-4449-9d43-3d999f4a317b
- Technique: T1505.005: Server Software Component: Terminal Services DLL
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1505.005/T1505.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1505-server_software_component|T1505.005]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$termsrvDll = "C:\Windows\System32\termsrv.dll"

$ACL = Get-Acl $termsrvDll
$permission = "Administrators","FullControl","Allow"
$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule $permission
$ACL.SetAccessRule($accessRule)
Set-Acl -Path $termsrvDll -AclObject $ACL

Copy-Item -Path "C:\Windows\System32\termsrv.dll" -Destination "C:\Windows\System32\termsrv_backup.dll" -ErrorAction Ignore
Add-Content -Path "C:\Windows\System32\termsrv.dll" -Value "`n" -NoNewline -ErrorAction Ignore
Move-Item -Path "C:\Windows\System32\termsrv_backup.dll" -Destination "C:\Windows\System32\termsrv.dll" -Force -ErrorAction Ignore
```

### Cleanup

```powershell
Move-Item -Path "C:\Windows\System32\termsrv_backup.dll" -Destination "C:\Windows\System32\termsrv.dll" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.005/T1505.005.yaml)
