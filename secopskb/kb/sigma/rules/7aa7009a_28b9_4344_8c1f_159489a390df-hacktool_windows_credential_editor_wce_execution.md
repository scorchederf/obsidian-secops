---
sigma_id: "7aa7009a-28b9-4344-8c1f-159489a390df"
title: "HackTool - Windows Credential Editor (WCE) Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_wce.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_wce.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "7aa7009a-28b9-4344-8c1f-159489a390df"
  - "HackTool - Windows Credential Editor (WCE) Execution"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Windows Credential Editor (WCE) Execution

Detects the use of Windows Credential Editor (WCE), a popular post-exploitation tool used to extract plaintext passwords, hash, PIN code and Kerberos tickets from memory.
It is often used by threat actors for credential dumping and lateral movement within compromised networks.

## Metadata

- Rule ID: 7aa7009a-28b9-4344-8c1f-159489a390df
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2019-12-31
- Modified: 2025-10-21
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_wce.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

### Software Tags

- S0005

## Detection

```yaml
selection_img:
  Image|endswith:
  - \WCE.exe
  - \WCE64.exe
selection_hash:
  Hashes|contains:
  - IMPHASH=136F0A8572C058A96436C82E541E4C41
  - IMPHASH=589657C64DDE88533186C39F82FA1F50
  - IMPHASH=6BFE09EFCB4FFDE061EBDBAFC4DB84CF
  - IMPHASH=7D490037BF450877E6D0287BDCFF8D2E
  - IMPHASH=8AB93B061287C79F3088C5BC7E7D97ED
  - IMPHASH=A53A02B997935FD8EEDCB5F7ABAB9B9F
  - IMPHASH=BA434A7A729EEC20E136CA4C32D6C740
  - IMPHASH=BD1D1547DA13C0FCB6C15E86217D5EB8
  - IMPHASH=E96A73C7BF33A464C510EDE582318BF2
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://www.ampliasecurity.com/research/windows-credentials-editor/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_wce.yml)
