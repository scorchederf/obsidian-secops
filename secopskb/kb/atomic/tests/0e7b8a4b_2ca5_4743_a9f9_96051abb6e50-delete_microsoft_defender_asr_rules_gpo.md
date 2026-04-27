---
atomic_guid: "0e7b8a4b-2ca5-4743-a9f9-96051abb6e50"
title: "Delete Microsoft Defender ASR Rules - GPO"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "0e7b8a4b-2ca5-4743-a9f9-96051abb6e50"
  - "Delete Microsoft Defender ASR Rules - GPO"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Delete Microsoft Defender ASR Rules - GPO

This test simulates the deletion of the ASR rules loaded by Microsoft Defender using the registry. Depending on the deployment, rules can be pushed either using GPO or InTune, This test simulates a GPO-based rules deployment.

## Metadata

- Atomic GUID: 0e7b8a4b-2ca5-4743-a9f9-96051abb6e50
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\ASR\Rules"

if (-not (Test-Path $registryPath)) {
    New-Item -Path $registryPath -Force
    Write-Host "Registry key created: $registryPath"
}

$newValueName = "36190899-1602-49e8-8b27-eb1d0a1ce869"
$newValueData = "1"
New-ItemProperty -Path $registryPath -Name $newValueName -PropertyType String -Value $newValueData -Force
Write-Host "Registry value created: $newValueName with data $newValueData"

Remove-ItemProperty -Path $registryPath -Name $newValueName
Write-Host "Registry value deleted: $newValueName"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
