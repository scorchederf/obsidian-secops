---
atomic_guid: "0eeb68ce-e64c-4420-8d53-ad5bdc6f86d5"
title: "Windows - Display a simulated ransom note via Notepad (non-destructive)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1491.001"
attack_technique_name: "Defacement: Internal Defacement"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "0eeb68ce-e64c-4420-8d53-ad5bdc6f86d5"
  - "Windows - Display a simulated ransom note via Notepad (non-destructive)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows - Display a simulated ransom note via Notepad (non-destructive)

Creates a temporary ransom-note text file and opens it in Notepad to
simulate ransomware "note display" behavior without making destructive
changes. SAFE and non-destructive.

## Metadata

- Atomic GUID: 0eeb68ce-e64c-4420-8d53-ad5bdc6f86d5
- Technique: T1491.001: Defacement: Internal Defacement
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: command_prompt
- Source Path: atomics/T1491.001/T1491.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1491-defacement|T1491.001]]

## Input Arguments

### note_body

- description: The body of the ransom note (plain text)
- type: string
- default: Your files are SAFE. This is a TEST note for detection validation
by bak3n3k0. No data has been encrypted. This simulation exercises
detections for:
  - notepad.exe launched with a ransom-themed text file
  - creation of a ransom-themed text file in %TEMP%
NON-DESTRUCTIVE Atomic Red Team test.


### note_filename

- description: File name for the simulated ransom note
- type: string
- default: ART-T1491-ransom-note.txt

### note_title

- description: Title at the top of the ransom note
- type: string
- default: !!! READ_ME_NOW !!!

### pid_filename

- description: File name for storing Notepad PID
- type: string
- default: ART-T1491-notepad.pid

## Dependencies

Notepad must be present on the system

### Prerequisite Check

```cmd
where notepad
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$notePath = Join-Path $env:TEMP "#{note_filename}"
$pidPath  = Join-Path $env:TEMP "#{pid_filename}"

$Title = "#{note_title}"
$Body  = "#{note_body}"

$header  = $Title + "`r`n" + ('=' * $Title.Length) + "`r`n`r`n"
$content = $header + $Body

[System.IO.File]::WriteAllText($notePath, $content, [System.Text.Encoding]::UTF8)

$p = Start-Process notepad.exe -ArgumentList "`"$notePath`"" -PassThru
$p.Id | Out-File -FilePath $pidPath -Encoding ascii -Force
```

### Cleanup

```powershell
try {
  # 1. Kill all Notepad processes
  Get-Process notepad -ErrorAction SilentlyContinue |
    ForEach-Object {
      Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
    }

  # 2. Wait briefly for Windows to release file handles
  Start-Sleep -Seconds 1

  # 3. Force delete ransom note + PID file
  $notePath = Join-Path $env:TEMP "ART-T1491-ransom-note.txt"
  $pidPath  = Join-Path $env:TEMP "ART-T1491-notepad.pid"

  if (Test-Path $notePath) {
    Remove-Item $notePath -Force -ErrorAction Stop
  }
  if (Test-Path $pidPath) {
    Remove-Item $pidPath -Force -ErrorAction Stop
  }
}
catch {
  Write-Warning "Cleanup failed with error: $_"
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1491.001/T1491.001.yaml)
