---
atomic_guid: "44b68e11-9da2-4d45-a0d9-893dabd60f30"
title: "Data Encrypt Using DiskCryptor"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "44b68e11-9da2-4d45-a0d9-893dabd60f30"
  - "Data Encrypt Using DiskCryptor"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

DiskCryptor, an open source encryption utility, can be exploited by adversaries for encrypting all disk partitions, including system partitions. This tool was identified in a ransomware campaign, as reported on https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/. The documentation for DiskCryptor can be found at https://github.com/DavidXanatos/DiskCryptor. During the installation process, running dcrypt.exe starts the encryption console. It's important to note that a system reboot is necessary as part of the installation.

## ATT&CK Mapping

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]

## Input Arguments

### dcrypt_exe

- description: The dcrypt.exe executable from dcrypt_setup.exe
- type: path
- default: dcrypt.exe

## Dependencies

dcrypt_setup will be installed at specified location (#{dcrypt_exe})

### Prerequisite Check

```powershell
if (Test-Path "${env:ProgramFiles}/dcrypt/#{dcrypt_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Downloading DiskCryptor installer
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/DavidXanatos/DiskCryptor/releases/download/1.1.846.118/dcrypt_setup_1.1.846.118.exe" -OutFile      "PathToAtomicsFolder\..\ExternalPayloads\dcrypt_setup_1.1.846.118.exe"
Write-Host Install DiskCryptor
Start-Process "PathToAtomicsFolder\..\ExternalPayloads\dcrypt_setup_1.1.846.118.exe" -Wait -ArgumentList "/s"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
""%PROGRAMFILES%\dcrypt"\#{dcrypt_exe}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
