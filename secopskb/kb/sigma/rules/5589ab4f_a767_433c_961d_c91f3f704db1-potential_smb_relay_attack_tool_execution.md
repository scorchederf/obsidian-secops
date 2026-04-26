---
sigma_id: "5589ab4f-a767-433c-961d-c91f3f704db1"
title: "Potential SMB Relay Attack Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_relay_attacks_tools.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_relay_attacks_tools.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "5589ab4f-a767-433c-961d-c91f3f704db1"
  - "Potential SMB Relay Attack Tool Execution"
attack_technique_ids:
  - "T1557.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential SMB Relay Attack Tool Execution

Detects different hacktools used for relay attacks on Windows for privilege escalation

## Metadata

- Rule ID: 5589ab4f-a767-433c-961d-c91f3f704db1
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-07-24
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_relay_attacks_tools.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557.001]]

## Detection

```yaml
selection_pe:
  Image|contains:
  - PetitPotam
  - RottenPotato
  - HotPotato
  - JuicyPotato
  - \just_dce_
  - Juicy Potato
  - \temp\rot.exe
  - \Potato.exe
  - \SpoolSample.exe
  - \Responder.exe
  - \smbrelayx
  - \ntlmrelayx
  - \LocalPotato
selection_script:
  CommandLine|contains:
  - Invoke-Tater
  - ' smbrelay'
  - ' ntlmrelay'
  - 'cme smb '
  - ' /ntlm:NTLMhash '
  - Invoke-PetitPotam
  - '.exe -t * -p '
selection_juicypotato_enum:
  CommandLine|contains: .exe -c "{
  CommandLine|endswith: '}" -z'
filter_hotpotatoes:
  Image|contains:
  - HotPotatoes6
  - HotPotatoes7
  - 'HotPotatoes '
condition: 1 of selection_* and not 1 of filter_*
```

## False Positives

- Legitimate files with these rare hacktool names

## References

- https://foxglovesecurity.com/2016/09/26/rotten-potato-privilege-escalation-from-service-accounts-to-system/
- https://pentestlab.blog/2017/04/13/hot-potato/
- https://github.com/ohpe/juicy-potato
- https://hunter2.gitbook.io/darthsidious/other/war-stories/domain-admin-in-30-minutes
- https://hunter2.gitbook.io/darthsidious/execution/responder-with-ntlm-relay-and-empire
- https://www.localpotato.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_relay_attacks_tools.yml)
