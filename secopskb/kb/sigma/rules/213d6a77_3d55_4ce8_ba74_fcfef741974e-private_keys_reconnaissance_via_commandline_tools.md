---
sigma_id: "213d6a77-3d55-4ce8-ba74-fcfef741974e"
title: "Private Keys Reconnaissance Via CommandLine Tools"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_private_keys_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_private_keys_recon.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "213d6a77-3d55-4ce8-ba74-fcfef741974e"
  - "Private Keys Reconnaissance Via CommandLine Tools"
attack_technique_ids:
  - "T1552.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Private Keys Reconnaissance Via CommandLine Tools

Adversaries may search for private key certificate files on compromised systems for insecurely stored credential

## Metadata

- Rule ID: 213d6a77-3d55-4ce8-ba74-fcfef741974e
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-07-20
- Modified: 2023-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_susp_private_keys_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

## Detection

```yaml
selection_cmd_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cmd_cli:
  CommandLine|contains: 'dir '
selection_pwsh_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_pwsh_cli:
  CommandLine|contains: 'Get-ChildItem '
selection_findstr:
- Image|endswith: \findstr.exe
- OriginalFileName: FINDSTR.EXE
selection_ext:
  CommandLine|contains:
  - .key
  - .pgp
  - .gpg
  - .ppk
  - .p12
  - .pem
  - .pfx
  - .cer
  - .p7b
  - .asc
condition: selection_ext and (all of selection_cmd_* or all of selection_pwsh_* or
  selection_findstr)
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.004/T1552.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_private_keys_recon.yml)
