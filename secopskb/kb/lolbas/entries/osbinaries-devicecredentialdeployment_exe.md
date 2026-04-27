---
title: "DeviceCredentialDeployment.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/DeviceCredentialDeployment.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/DeviceCredentialDeployment.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "DeviceCredentialDeployment.exe"
functions:
  - "Conceal"
attack_technique_ids:
  - "T1564"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Device Credential Deployment

## Paths

- `C:\Windows\System32\DeviceCredentialDeployment.exe`

## Commands

### 1. Conceal

Grab the console window handle and set it to hidden

```cmd
DeviceCredentialDeployment
```

- Use Case: Can be used to stealthily run a console application (e.g. cmd.exe) in the background
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564: Hide Artifacts]]

## Detections

- IOC: DeviceCredentialDeployment.exe should not be run on a normal workstation
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff5102832031425f6eed011dd3a2e62653008c94/rules/windows/process_creation/proc_creation_win_lolbin_device_credential_deployment.yml

## Acknowledgements

- {'Person': 'Elliot Killick', 'Handle': '@elliotkillick'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/DeviceCredentialDeployment.yml)
