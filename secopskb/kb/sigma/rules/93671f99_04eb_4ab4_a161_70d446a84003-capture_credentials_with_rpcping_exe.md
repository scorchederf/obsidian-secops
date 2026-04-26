---
sigma_id: "93671f99-04eb-4ab4-a161-70d446a84003"
title: "Capture Credentials with Rpcping.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rpcping_credential_capture.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rpcping_credential_capture.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "93671f99-04eb-4ab4-a161-70d446a84003"
  - "Capture Credentials with Rpcping.exe"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Capture Credentials with Rpcping.exe

Detects using Rpcping.exe to send a RPC test connection to the target server (-s) and force the NTLM hash to be sent in the process.

## Metadata

- Rule ID: 93671f99-04eb-4ab4-a161-70d446a84003
- Status: test
- Level: medium
- Author: Julia Fomina, oscd.community
- Date: 2020-10-09
- Modified: 2025-10-31
- Source Path: rules/windows/process_creation/proc_creation_win_rpcping_credential_capture.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection_main_img:
- Image|endswith: \RpcPing.exe
- OriginalFileName: \RpcPing.exe
selection_main_flag:
  CommandLine|contains|windash: -s
selection_cli_ntlm:
  CommandLine|contains|windash: -u
  CommandLine|contains: NTLM
selection_cli_ncacn:
  CommandLine|contains|windash: -t
  CommandLine|contains: ncacn_np
condition: all of selection_main_* and 1 of selection_cli_*
```

## False Positives

- Unlikely

## References

- https://lolbas-project.github.io/lolbas/Binaries/Rpcping/
- https://twitter.com/vysecurity/status/974806438316072960
- https://twitter.com/vysecurity/status/873181705024266241
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh875578(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rpcping_credential_capture.yml)
