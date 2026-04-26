---
atomic_guid: "53adbdfa-8200-490c-871c-d3b1ab3324b2"
title: "Install IIS Module using AppCmd.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1505.004"
attack_technique_name: "IIS Components"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.004/T1505.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "53adbdfa-8200-490c-871c-d3b1ab3324b2"
  - "Install IIS Module using AppCmd.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Install IIS Module using AppCmd.exe

The following Atomic will utilize AppCmd.exe to install a new IIS Module. IIS must be installed.
This atomic utilizes a DLL on disk, but to test further suspiciousness, compile and load [IIS-Raid](https://www.mdsec.co.uk/2020/02/iis-raid-backdooring-iis-using-native-modules/).
A successful execution will install a module into IIS using AppCmd.exe.
[Managing and installing Modules Reference](https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/iis-modules-overview#to-install-a-module-using-appcmdexe)
[IIS Modules](https://www.microsoft.com/en-us/security/blog/2022/12/12/iis-modules-the-evolution-of-web-shells-and-how-to-detect-them/)

## Metadata

- Atomic GUID: 53adbdfa-8200-490c-871c-d3b1ab3324b2
- Technique: T1505.004: IIS Components
- Platforms: windows
- Executor: command_prompt
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

- name: command_prompt

### Command

```cmd
%windir%\system32\inetsrv\appcmd.exe install module /name:#{module_name} /image:#{dll_path}
```

### Cleanup

```cmd
%windir%\system32\inetsrv\appcmd.exe uninstall module #{module_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1505.004/T1505.004.yaml)
