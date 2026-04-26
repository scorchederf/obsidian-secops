---
atomic_guid: "9b7a7cfc-dd2e-43f5-a885-c0a3c270dd93"
title: "InstallUtil class constructor method call"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.004"
attack_technique_name: "Signed Binary Proxy Execution: InstallUtil"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.004/T1218.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "9b7a7cfc-dd2e-43f5-a885-c0a3c270dd93"
  - "InstallUtil class constructor method call"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# InstallUtil class constructor method call

Executes the installer assembly class constructor. Upon execution, version information will be displayed the .NET framework install utility.

## Metadata

- Atomic GUID: 9b7a7cfc-dd2e-43f5-a885-c0a3c270dd93
- Technique: T1218.004: Signed Binary Proxy Execution: InstallUtil
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1218.004/T1218.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.004]]

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

```text
if (Test-Path "#{test_harness}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
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

$CommandLine = "/logfile= /logtoconsole=false `"$InstallerAssemblyFullPath`""
$ExpectedOutput = 'Constructor_'

$TestArgs = @{
    OutputAssemblyDirectory = $InstallerAssemblyDir
    OutputAssemblyFileName = $InstallerAssemblyFileName
    InvocationMethod = '#{invocation_method}'
    CommandLine = $CommandLine
}

$ActualOutput = Invoke-BuildAndInvokeInstallUtilAssembly @TestArgs -MinimumViableAssembly

if ($ActualOutput -ne $ExpectedOutput) {
    throw @"
InstallUtil class constructor execution test failure. Installer assembly execution output did not match the expected output.
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
