---
atomic_guid: "2169e8b0-2ee7-44cb-8a6e-d816a5db7d8a"
title: "Deploy 7-Zip Using Chocolatey"
framework: "atomic"
generated: "true"
attack_technique_id: "T1072"
attack_technique_name: "Software Deployment Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1072/T1072.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "2169e8b0-2ee7-44cb-8a6e-d816a5db7d8a"
  - "Deploy 7-Zip Using Chocolatey"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may use Chocolatey to remotely deploy the 7-Zip file archiver utility.

## ATT&CK Mapping

- [[kb/attack/techniques/T1072-software_deployment_tools|T1072: Software Deployment Tools]]

## Dependencies

Chocolatey must be installed to deploy 7-Zip.

### Prerequisite Check

```powershell
if (Test-Path "${env:ProgramFiles(x86)}\Chocolatey\choco.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Downloading Chocolatey installer
Invoke-WebRequest -Uri "https://chocolatey.org/install.ps1" -OutFile "chocolatey-install.ps1"
Write-Host Installing Chocolatey
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File chocolatey-install.ps1" -Wait
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
# Deploy 7-Zip using Chocolatey
choco install -y 7zip
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1072/T1072.yaml)
