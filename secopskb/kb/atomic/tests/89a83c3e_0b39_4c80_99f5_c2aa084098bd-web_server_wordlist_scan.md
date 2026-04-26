---
atomic_guid: "89a83c3e-0b39-4c80-99f5-c2aa084098bd"
title: "Web Server Wordlist Scan"
framework: "atomic"
generated: "true"
attack_technique_id: "T1595.003"
attack_technique_name: "Active Scanning: Wordlist Scanning"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1595.003/T1595.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "89a83c3e-0b39-4c80-99f5-c2aa084098bd"
  - "Web Server Wordlist Scan"
platforms:
  - "windows"
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Web Server Wordlist Scan

This test will scan a target system with a wordlist of common directories and file paths.

## Metadata

- Atomic GUID: 89a83c3e-0b39-4c80-99f5-c2aa084098bd
- Technique: T1595.003: Active Scanning: Wordlist Scanning
- Platforms: windows, linux, macos
- Executor: powershell
- Source Path: atomics/T1595.003/T1595.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1595-active_scanning|T1595.003]]

## Input Arguments

### output_file

- description: File to output results to
- type: string
- default: $env:TMPDIR/wordlist_scan.txt

### request_timeout

- description: The timeout for each request (in seconds)
- type: integer
- default: 5

### target

- description: The target system to scan
- type: string
- default: http://localhost

### wordlist

- description: The wordlist to use for scanning
- type: path
- default: PathToAtomicsFolder/T1595.003/src/wordlist.txt

## Executor

- name: powershell

### Command

```powershell
Import-Module "PathToAtomicsFolder/T1595.003/src/WebServerScan.ps1"
Invoke-WordlistScan -Target "#{target}" -Wordlist "#{wordlist}" -Timeout "#{request_timeout}" -OutputFile "#{output_file}"
Write-Host "Scan complete. Results saved to: #{output_file}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1595.003/T1595.003.yaml)
