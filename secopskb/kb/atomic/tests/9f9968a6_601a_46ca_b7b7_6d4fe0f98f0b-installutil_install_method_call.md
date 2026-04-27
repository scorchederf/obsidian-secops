---
atomic_guid: "9f9968a6-601a-46ca-b7b7-6d4fe0f98f0b"
title: "InstallUtil Install method call"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.004"
attack_technique_name: "Signed Binary Proxy Execution: InstallUtil"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.004/T1218.004.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "9f9968a6-601a-46ca-b7b7-6d4fe0f98f0b"
  - "InstallUtil Install method call"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes the Install Method. Upon execution, version information will be displayed the .NET framework install utility.

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218004-installutil|T1218.004: InstallUtil]]

## Input Arguments

### assembly_dir

- description: directory to drop the compiled installer assembly
- type: path
- default: $Env:TEMP\

### assembly_filename

- description: filename of the compiled installer assembly
- type: string
- default: T1218.004.dll

### invocation_method

- description: the type of InstallUtil invocation variant - Executable, InstallHelper, or CheckIfInstallable
- type: string
- default: Executable

### test_harness

- description: location of the test harness script - Invoke-BuildAndInvokeInstallUtilAssembly
- type: path
- default: PathToAtomicsFolder\T1218.004\src\InstallUtilTestHarness.ps1

## Dependencies

InstallUtil test harness script must be installed at specified location (#{test_harness})

### Prerequisite Check

```untitled
if (Test-Path "#{test_harness}") {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory (split-path "#{test_harness}") -ErrorAction ignore | Out-Null
Invoke-WebRequest 'https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1218.004/src/InstallUtilTestHarness.ps1' -OutFile "#{test_harness}"
```

## Executor

- name: powershell

### Command

```powershell
# Import the required test harness function, Invoke-BuildAndInvokeInstallUtilAssembly
. "#{test_harness}"

$InstallerAssemblyDir = "#{assembly_dir}"
$InstallerAssemblyFileName = "#{assembly_filename}"
$InstallerAssemblyFullPath = Join-Path -Path $InstallerAssemblyDir -ChildPath $InstallerAssemblyFileName

$CommandLine = "/logfile= /logtoconsole=false /installtype=notransaction /action=install `"$InstallerAssemblyFullPath`""
$ExpectedOutput = 'Constructor_Install_'

$TestArgs = @{
    OutputAssemblyDirectory = $InstallerAssemblyDir
    OutputAssemblyFileName = $InstallerAssemblyFileName
    InvocationMethod = '#{invocation_method}'
    CommandLine = $CommandLine
}

$ActualOutput = Invoke-BuildAndInvokeInstallUtilAssembly @TestArgs

if ($ActualOutput -ne $ExpectedOutput) {
    throw @"
InstallUtil Install method execution test failure. Installer assembly execution output did not match the expected output.
Expected: $ExpectedOutput
Actual: $ActualOutput
"@
}
```

### Cleanup

```powershell
$InstallerAssemblyDir = "#{assembly_dir}"
$InstallerAssemblyFileName = "#{assembly_filename}"
$InstallerAssemblyFullPath = Join-Path -Path $InstallerAssemblyDir -ChildPath $InstallerAssemblyFileName
Remove-Item -Path $InstallerAssemblyFullPath -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.004/T1218.004.yaml)
