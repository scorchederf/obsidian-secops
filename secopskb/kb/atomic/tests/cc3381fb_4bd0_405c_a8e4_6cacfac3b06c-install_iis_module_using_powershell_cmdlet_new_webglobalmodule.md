---
atomic_guid: "cc3381fb-4bd0-405c-a8e4-6cacfac3b06c"
title: "Install IIS Module using PowerShell Cmdlet New-WebGlobalModule"
framework: "atomic"
generated: "true"
attack_technique_id: "T1505.004"
attack_technique_name: "IIS Components"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.004/T1505.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "cc3381fb-4bd0-405c-a8e4-6cacfac3b06c"
  - "Install IIS Module using PowerShell Cmdlet New-WebGlobalModule"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Install IIS Module using PowerShell Cmdlet New-WebGlobalModule

The following Atomic will utilize PowerShell Cmdlet New-WebGlobalModule to install a new IIS Module. IIS must be installed.
This atomic utilizes a DLL on disk, but to test further suspiciousness, compile and load [IIS-Raid](https://www.mdsec.co.uk/2020/02/iis-raid-backdooring-iis-using-native-modules/).
A successful execution will install a module into IIS using New-WebGlobalModule.
[Managing IIS Modules with PowerShell](https://learn.microsoft.com/en-us/powershell/module/webadministration/set-webglobalmodule?view=windowsserver2022-ps)
[IIS Modules](https://www.microsoft.com/en-us/security/blog/2022/12/12/iis-modules-the-evolution-of-web-shells-and-how-to-detect-them/)

## Metadata

- Atomic GUID: cc3381fb-4bd0-405c-a8e4-6cacfac3b06c
- Technique: T1505.004: IIS Components
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1505.004/T1505.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1505-server_software_component|T1505.004]]

## Input Arguments

### dll_path

- description: The path to the DLL to be loaded
- type: path
- default: %windir%\system32\inetsrv\defdoc.dll

### module_name

- description: The name of the IIS module
- type: string
- default: DefaultDocumentModule_Atomic

## Dependencies

IIS must be installed in order to add a module to IIS.

### Prerequisite Check

```powershell
$service = get-service w3svc -ErrorAction SilentlyContinue
if($service){ Write-Host "IIS installed on $env:computername" } else { Write-Host "IIS is not installed on $env:computername" }
```

### Get Prerequisite

```powershell
Install IIS to continue.
```

## Executor

- name: powershell

### Command

```powershell
New-WebGlobalModule -Name #{module_name} -Image #{dll_path}
```

### Cleanup

```powershell
Remove-WebGlobalModule -Name #{module_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.004/T1505.004.yaml)
