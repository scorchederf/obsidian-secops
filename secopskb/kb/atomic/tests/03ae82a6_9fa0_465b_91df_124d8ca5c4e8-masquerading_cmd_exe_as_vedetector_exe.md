---
atomic_guid: "03ae82a6-9fa0-465b-91df-124d8ca5c4e8"
title: "Masquerading cmd.exe as VEDetector.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.005"
attack_technique_name: "Masquerading: Match Legitimate Name or Location"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.005/T1036.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "03ae82a6-9fa0-465b-91df-124d8ca5c4e8"
  - "Masquerading cmd.exe as VEDetector.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Masquerading cmd.exe as VEDetector.exe

This test simulates an adversary renaming cmd.exe to VEDetector.exe to masquerade as a legitimate application.
The test copies cmd.exe, renames it to VEDetector.exe, adds a registry run key for persistence, and executes the renamed binary.
This technique may be used to evade detection by mimicking legitimate software names or locations.

**Expected Output:**
- A new process named VEDetector.exe appears in the process list, but its behavior matches cmd.exe.
- SIEM/EDR systems may detect this as suspicious process activity (e.g., Sysmon Event ID 1 for process creation, or Event ID 13 for registry modifications).
- Registry modification in HKLM:\Software\Microsoft\Windows\CurrentVersion\Run may trigger persistence alerts in XDR platforms.

**References:**
- [MITRE ATT&CK T1036.005](https://attack.mitre.org/techniques/T1036/005/)
- [Sysmon Process Creation](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## Metadata

- Atomic GUID: 03ae82a6-9fa0-465b-91df-124d8ca5c4e8
- Technique: T1036.005: Masquerading: Match Legitimate Name or Location
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1036.005/T1036.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Input Arguments

### source_file

- description: Path to the source cmd.exe file
- type: Path
- default: $env:SystemRoot\System32\cmd.exe

### ved_path

- description: Directory path where VEDetector.exe will be created
- type: Path
- default: $env:TEMP

## Dependencies

The source cmd.exe file must exist on the system.

### Prerequisite Check

```powershell
if (Test-Path "#{source_file}") { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "[-] Source file not found: #{source_file}. Ensure cmd.exe exists in the specified path."
exit 1
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
# Copy and rename cmd.exe to VEDetector.exe
Copy-Item -Path "#{source_file}" -Destination "#{ved_path}\VEDetector.exe" -Force

# Create registry run key for persistence
New-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "VEDetector" -Value "#{ved_path}\VEDetector.exe" -PropertyType String -Force

# Start the renamed process
Start-Process -FilePath "#{ved_path}\VEDetector.exe"

Start-Sleep -Seconds 5
```

### Cleanup

```powershell
# Remove registry key
Remove-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "VEDetector" -ErrorAction SilentlyContinue

# Stop the process
Stop-Process -Name "VEDetector" -Force -ErrorAction SilentlyContinue

# Remove the file
Remove-Item -Path "#{ved_path}\VEDetector.exe" -Force -ErrorAction SilentlyContinue

Write-Host "[+] Cleaned up VEDetector artifacts"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.005/T1036.005.yaml)
