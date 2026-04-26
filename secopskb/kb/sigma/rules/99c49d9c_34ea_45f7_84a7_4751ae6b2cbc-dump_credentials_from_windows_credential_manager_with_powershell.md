---
sigma_id: "99c49d9c-34ea-45f7-84a7-4751ae6b2cbc"
title: "Dump Credentials from Windows Credential Manager With PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_dump_password_windows_credential_manager.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_dump_password_windows_credential_manager.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "99c49d9c-34ea-45f7-84a7-4751ae6b2cbc"
  - "Dump Credentials from Windows Credential Manager With PowerShell"
attack_technique_ids:
  - "T1555"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Dump Credentials from Windows Credential Manager With PowerShell

Adversaries may search for common password storage locations to obtain user credentials.
Passwords are stored in several places on a system, depending on the operating system or application holding the credentials.

## Metadata

- Rule ID: 99c49d9c-34ea-45f7-84a7-4751ae6b2cbc
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-20
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_dump_password_windows_credential_manager.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555]]

## Detection

```yaml
selection_kiddie:
  ScriptBlockText|contains:
  - Get-PasswordVaultCredentials
  - Get-CredManCreds
selection_rename_Password:
  ScriptBlockText|contains|all:
  - New-Object
  - Windows.Security.Credentials.PasswordVault
selection_rename_credman:
  ScriptBlockText|contains|all:
  - New-Object
  - Microsoft.CSharp.CSharpCodeProvider
  - '[System.Runtime.InteropServices.RuntimeEnvironment]::GetRuntimeDirectory())'
  - Collections.ArrayList
  - System.CodeDom.Compiler.CompilerParameters
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555/T1555.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_dump_password_windows_credential_manager.yml)
