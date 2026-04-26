---
sigma_id: "36d88494-1d43-4dc0-b3fa-35c8fea0ca9d"
title: "HackTool - CreateMiniDump Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_createminidump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_createminidump.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "36d88494-1d43-4dc0-b3fa-35c8fea0ca9d"
  - "HackTool - CreateMiniDump Execution"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - CreateMiniDump Execution

Detects the use of CreateMiniDump hack tool used to dump the LSASS process memory for credential extraction on the attacker's machine

## Metadata

- Rule ID: 36d88494-1d43-4dc0-b3fa-35c8fea0ca9d
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-12-22
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_createminidump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
- Image|endswith: \CreateMiniDump.exe
- Hashes|contains: IMPHASH=4a07f944a83e8a7c2525efa35dd30e2f
condition: selection
```

## False Positives

- Unknown

## References

- https://ired.team/offensive-security/credential-access-and-credential-dumping/dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_createminidump.yml)
