---
atomic_guid: "49eb9404-5e0f-4031-a179-b40f7be385e3"
title: "PowerShell Invoke Known Malicious Cmdlets"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.001"
attack_technique_name: "Command and Scripting Interpreter: PowerShell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "49eb9404-5e0f-4031-a179-b40f7be385e3"
  - "PowerShell Invoke Known Malicious Cmdlets"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Invoke Known Malicious Cmdlets

Powershell execution of known Malicious PowerShell Cmdlets

## Metadata

- Atomic GUID: 49eb9404-5e0f-4031-a179-b40f7be385e3
- Technique: T1059.001: Command and Scripting Interpreter: PowerShell
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1059.001/T1059.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Input Arguments

### Malicious_cmdlets

- description: Known Malicious Cmdlets
- type: string
- default: "Add-Persistence", "Find-AVSignature", "Get-GPPAutologon", "Get-GPPPassword", "Get-HttpStatus", "Get-Keystrokes", "Get-SecurityPackages", "Get-TimedScreenshot", "Get-VaultCredential", "Get-VolumeShadowCopy", "Install-SSP", "Invoke-CredentialInjection", "Invoke-DllInjection", "Invoke-Mimikatz", "Invoke-NinjaCopy", "Invoke-Portscan", "Invoke-ReflectivePEInjection", "Invoke-ReverseDnsLookup", "Invoke-Shellcode", "Invoke-TokenManipulation", "Invoke-WmiCommand", "Mount-VolumeShadowCopy", "New-ElevatedPersistenceOption", "New-UserPersistenceOption", "New-VolumeShadowCopy", "Out-CompressedDll", "Out-EncodedCommand", "Out-EncryptedScript", "Out-Minidump", "PowerUp", "PowerView", "Remove-Comments", "Remove-VolumeShadowCopy", "Set-CriticalProcess", "Set-MasterBootRecord"


## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$malcmdlets = #{Malicious_cmdlets}
foreach ($cmdlets in $malcmdlets) {
    "function $cmdlets { Write-Host Pretending to invoke $cmdlets }"}
foreach ($cmdlets in $malcmdlets) {
    $cmdlets}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.001/T1059.001.yaml)
