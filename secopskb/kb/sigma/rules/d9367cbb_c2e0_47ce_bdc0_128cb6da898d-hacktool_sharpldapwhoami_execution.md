---
sigma_id: "d9367cbb-c2e0-47ce-bdc0-128cb6da898d"
title: "HackTool - SharpLdapWhoami Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpldapwhoami.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpldapwhoami.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d9367cbb-c2e0-47ce-bdc0-128cb6da898d"
  - "HackTool - SharpLdapWhoami Execution"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - SharpLdapWhoami Execution

Detects SharpLdapWhoami, a whoami alternative that queries the LDAP service on a domain controller

## Metadata

- Rule ID: d9367cbb-c2e0-47ce-bdc0-128cb6da898d
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-29
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharpldapwhoami.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection_name:
  Image|endswith: \SharpLdapWhoami.exe
selection_pe:
- OriginalFileName|contains: SharpLdapWhoami
- Product: SharpLdapWhoami
selection_flags1:
  CommandLine|endswith:
  - ' /method:ntlm'
  - ' /method:kerb'
  - ' /method:nego'
  - ' /m:nego'
  - ' /m:ntlm'
  - ' /m:kerb'
condition: 1 of selection*
```

## False Positives

- Programs that use the same command line flags

## References

- https://github.com/bugch3ck/SharpLdapWhoami

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpldapwhoami.yml)
