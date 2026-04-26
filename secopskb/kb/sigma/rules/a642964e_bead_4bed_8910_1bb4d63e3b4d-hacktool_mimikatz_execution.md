---
sigma_id: "a642964e-bead-4bed-8910-1bb4d63e3b4d"
title: "HackTool - Mimikatz Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_mimikatz_command_line.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_mimikatz_command_line.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a642964e-bead-4bed-8910-1bb4d63e3b4d"
  - "HackTool - Mimikatz Execution"
attack_technique_ids:
  - "T1003.001"
  - "T1003.002"
  - "T1003.004"
  - "T1003.005"
  - "T1003.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Mimikatz Execution

Detection well-known mimikatz command line arguments

## Metadata

- Rule ID: a642964e-bead-4bed-8910-1bb4d63e3b4d
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, oscd.community, David ANDRE (additional keywords), Tim Shelton
- Date: 2019-10-22
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_mimikatz_command_line.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.005]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.006]]

## Detection

```yaml
selection_tools_name:
  CommandLine|contains:
  - DumpCreds
  - mimikatz
selection_function_names:
  CommandLine|contains:
  - ::aadcookie
  - ::detours
  - ::memssp
  - ::mflt
  - ::ncroutemon
  - ::ngcsign
  - ::printnightmare
  - ::skeleton
  - ::preshutdown
  - ::mstsc
  - ::multirdp
selection_module_names:
  CommandLine|contains:
  - 'rpc::'
  - 'token::'
  - 'crypto::'
  - 'dpapi::'
  - 'sekurlsa::'
  - 'kerberos::'
  - 'lsadump::'
  - 'privilege::'
  - 'process::'
  - 'vault::'
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment
- https://tools.thehacker.recipes/mimikatz/modules

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_mimikatz_command_line.yml)
