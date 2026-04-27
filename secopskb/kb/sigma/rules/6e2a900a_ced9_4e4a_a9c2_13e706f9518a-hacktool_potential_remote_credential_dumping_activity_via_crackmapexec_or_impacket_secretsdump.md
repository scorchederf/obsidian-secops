---
sigma_id: "6e2a900a-ced9-4e4a-a9c2-13e706f9518a"
title: "HackTool - Potential Remote Credential Dumping Activity Via CrackMapExec Or Impacket-Secretsdump"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_remote_cred_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_remote_cred_dump.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "6e2a900a-ced9-4e4a-a9c2-13e706f9518a"
  - "HackTool - Potential Remote Credential Dumping Activity Via CrackMapExec Or Impacket-Secretsdump"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects default filenames output from the execution of CrackMapExec and Impacket-secretsdump against an endpoint.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

## Detection

```yaml
selection:
  Image|endswith: \svchost.exe
  TargetFilename|re: \\Windows\\System32\\[a-zA-Z0-9]{8}\.tmp$
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Porchetta-Industries/CrackMapExec
- https://github.com/fortra/impacket/blob/ff8c200fd040b04d3b5ff05449646737f836235d/examples/secretsdump.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_remote_cred_dump.yml)
