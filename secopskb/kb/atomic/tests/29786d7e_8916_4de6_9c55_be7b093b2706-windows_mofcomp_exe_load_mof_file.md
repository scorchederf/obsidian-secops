---
atomic_guid: "29786d7e-8916-4de6-9c55-be7b093b2706"
title: "Windows MOFComp.exe Load MOF File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.003"
attack_technique_name: "Event Triggered Execution: Windows Management Instrumentation Event Subscription"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.003/T1546.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "29786d7e-8916-4de6-9c55-be7b093b2706"
  - "Windows MOFComp.exe Load MOF File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows MOFComp.exe Load MOF File

The following Atomic will utilize MOFComp.exe to load a local MOF file.
The Managed Object Format (MOF) compiler parses a file containing MOF statements and adds the classes and class instances defined in the file to the WMI repository. 
To query for the class:  gwmi __eventfilter -namespace root\subscription
A successful execution will add the class to WMI root namespace.
Reference: https://pentestlab.blog/2020/01/21/persistence-wmi-event-subscription/ and https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/.

## Metadata

- Atomic GUID: 29786d7e-8916-4de6-9c55-be7b093b2706
- Technique: T1546.003: Event Triggered Execution: Windows Management Instrumentation Event Subscription
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1546.003/T1546.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Input Arguments

### mof_file

- description: Local location MOF file
- type: string
- default: PathToAtomicsFolder\T1546.003\src\T1546.003.mof

### mofcomp_path

- description: Location of mofcomp.exe
- type: string
- default: c:\windows\system32\wbem\mofcomp.exe

## Dependencies

MofComp.exe must exist on disk at specified location (#{mofcomp_path})

### Prerequisite Check

```powershell
if (Test-Path "#{mofcomp_path}") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
Validate MOFComp.exe is on disk somewhere and update input argument.
```

MofComp.exe must exist on disk at specified location (#{mof_file})

### Prerequisite Check

```powershell
if (Test-Path "#{mof_file}") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{mof_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1546.003/src/T1546.003.mof" -OutFile "#{mof_file}"
```

## Executor

- name: powershell

### Command

```powershell
#{mofcomp_path} "#{mof_file}"
```

### Cleanup

```powershell
$EventConsumerToCleanup = Get-WmiObject -Namespace root/subscription -Class CommandLineEventConsumer -Filter "Name = 'AtomicRedTeam_consumer'"
$EventFilterToCleanup = Get-WmiObject -Namespace root/subscription -Class __EventFilter -Filter "Name = 'AtomicRedTeam_filter'"
$FilterConsumerBindingToCleanup = Get-WmiObject -Namespace root/subscription -Query "REFERENCES OF {$($EventConsumerToCleanup.__RELPATH)} WHERE ResultClass = __FilterToConsumerBinding" -ErrorAction SilentlyContinue
$FilterConsumerBindingToCleanup | Remove-WmiObject
$EventConsumerToCleanup | Remove-WmiObject
$EventFilterToCleanup | Remove-WmiObject
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.003/T1546.003.yaml)
