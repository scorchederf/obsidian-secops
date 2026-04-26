---
sigma_id: "f62176f3-8128-4faa-bf6c-83261322e5eb"
title: "Malicious PowerShell Keywords"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_malicious_keywords.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_malicious_keywords.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "f62176f3-8128-4faa-bf6c-83261322e5eb"
  - "Malicious PowerShell Keywords"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Malicious PowerShell Keywords

Detects keywords from well-known PowerShell exploitation frameworks

## Metadata

- Rule ID: f62176f3-8128-4faa-bf6c-83261322e5eb
- Status: test
- Level: medium
- Author: Sean Metcalf (source), Florian Roth (Nextron Systems)
- Date: 2017-03-05
- Modified: 2023-06-20
- Source Path: rules/windows/powershell/powershell_script/posh_ps_malicious_keywords.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - AdjustTokenPrivileges
  - IMAGE_NT_OPTIONAL_HDR64_MAGIC
  - Metasploit
  - Microsoft.Win32.UnsafeNativeMethods
  - Mimikatz
  - MiniDumpWriteDump
  - PAGE_EXECUTE_READ
  - ReadProcessMemory.Invoke
  - SE_PRIVILEGE_ENABLED
  - SECURITY_DELEGATION
  - TOKEN_ADJUST_PRIVILEGES
  - TOKEN_ALL_ACCESS
  - TOKEN_ASSIGN_PRIMARY
  - TOKEN_DUPLICATE
  - TOKEN_ELEVATION
  - TOKEN_IMPERSONATE
  - TOKEN_INFORMATION_CLASS
  - TOKEN_PRIVILEGES
  - TOKEN_QUERY
condition: selection
```

## False Positives

- Depending on the scripts, this rule might require some initial tuning to fit the environment

## References

- https://adsecurity.org/?p=2921

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_malicious_keywords.yml)
