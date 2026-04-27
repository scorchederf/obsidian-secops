---
sigma_id: "37c1333a-a0db-48be-b64b-7393b2386e3b"
title: "Hacktool Execution - PE Metadata"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_execution_via_pe_metadata.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_execution_via_pe_metadata.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "37c1333a-a0db-48be-b64b-7393b2386e3b"
  - "Hacktool Execution - PE Metadata"
attack_technique_ids:
  - "T1588.002"
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of different Windows based hacktools via PE metadata (company, product, etc.) even if the files have been renamed

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities#^t1588002-tool|T1588.002: Tool]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

## Detection

```yaml
selection:
  Company: Cube0x0
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/cube0x0
- https://www.virustotal.com/gui/search/metadata%253ACube0x0/files

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_execution_via_pe_metadata.yml)
