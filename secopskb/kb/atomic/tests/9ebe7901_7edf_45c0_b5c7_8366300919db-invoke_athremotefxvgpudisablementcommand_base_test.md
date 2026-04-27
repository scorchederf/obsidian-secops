---
atomic_guid: "9ebe7901-7edf-45c0-b5c7-8366300919db"
title: "Invoke-ATHRemoteFXvGPUDisablementCommand base test"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218"
attack_technique_name: "Signed Binary Proxy Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "9ebe7901-7edf-45c0-b5c7-8366300919db"
  - "Invoke-ATHRemoteFXvGPUDisablementCommand base test"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

RemoteFXvGPUDisablement.exe is an abusable, signed PowerShell host executable that was introduced in Windows 10 and Server 2019 (OS Build 17763.1339).

One of the PowerShell functions called by RemoteFXvGPUDisablement.exe is Get-VMRemoteFXPhysicalVideoAdapter, a part of the Hyper-V module. This atomic test influences RemoteFXvGPUDisablement.exe to execute custom PowerShell code by using a technique referred to as "PowerShell module load-order hijacking" where a module containing, in this case, an implementation of the Get-VMRemoteFXPhysicalVideoAdapter is loaded first by way of introducing a temporary module into the first directory listed in the %PSModulePath% environment variable or within a user-specified module directory outside of %PSModulePath%. Upon execution the temporary module is deleted.

Invoke-ATHRemoteFXvGPUDisablementCommand is used in this test to demonstrate how a PowerShell host executable can be directed to user-supplied PowerShell code without needing to supply anything at the command-line. PowerShell code execution is triggered when supplying the "Disable" argument to RemoteFXvGPUDisablement.exe.

The Invoke-ATHRemoteFXvGPUDisablementCommand function outputs all relevant execution-related artifacts.

Reference: https://github.com/redcanaryco/AtomicTestHarnesses/blob/master/TestHarnesses/T1218_SignedBinaryProxyExecution/InvokeRemoteFXvGPUDisablementCommand.ps1

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Input Arguments

### module_name

- description: Specifies a temporary module name to use. If -ModuleName is not supplied, a 16-character random temporary module name is used. A PowerShell module can have any name. Because Get-VMRemoteFXPhysicalVideoAdapter abuses module load order, a module name must be specified.
- type: string
- default: foo

### module_path

- description: Specifies an alternate, non-default PowerShell module path for RemoteFXvGPUDisablement.exe. If -ModulePath is not specified, the first entry in %PSModulePath% will be used. Typically, this is %USERPROFILE%\Documents\WindowsPowerShell\Modules.
- type: string
- default: $PWD

## Dependencies

The AtomicTestHarnesses module must be installed and Invoke-ATHRemoteFXvGPUDisablementCommand must be exported in the module.

### Prerequisite Check

```untitled
$RequiredModule = Get-Module -Name AtomicTestHarnesses -ListAvailable
if (-not $RequiredModule) {exit 1}
if (-not $RequiredModule.ExportedCommands['Invoke-ATHRemoteFXvGPUDisablementCommand']) {exit 1} else {exit 0}
```

### Get Prerequisite

```untitled
Install-Module -Name AtomicTestHarnesses -Scope CurrentUser -Force
```

## Executor

- name: powershell

### Command

```powershell
Invoke-ATHRemoteFXvGPUDisablementCommand -ModuleName #{module_name} -ModulePath #{module_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218/T1218.yaml)
