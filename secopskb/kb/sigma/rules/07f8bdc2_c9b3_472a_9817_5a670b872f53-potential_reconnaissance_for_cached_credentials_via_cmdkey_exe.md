---
sigma_id: "07f8bdc2-c9b3-472a-9817-5a670b872f53"
title: "Potential Reconnaissance For Cached Credentials Via Cmdkey.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "07f8bdc2-c9b3-472a-9817-5a670b872f53"
  - "Potential Reconnaissance For Cached Credentials Via Cmdkey.EXE"
attack_technique_ids:
  - "T1003.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Reconnaissance For Cached Credentials Via Cmdkey.EXE

Detects usage of cmdkey to look for cached credentials on the system

## Metadata

- Rule ID: 07f8bdc2-c9b3-472a-9817-5a670b872f53
- Status: test
- Level: high
- Author: jmallette, Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-01-16
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmdkey.exe
- OriginalFileName: cmdkey.exe
selection_cli:
  CommandLine|contains|windash: ' -l'
condition: all of selection*
```

## False Positives

- Legitimate administrative tasks

## Simulation

### Cached Credential Dump via Cmdkey

- atomic_guid: 56506854-89d6-46a3-9804-b7fde90791f9
- name: Cached Credential Dump via Cmdkey
- technique: T1003.005
- type: atomic-red-team

## References

- https://www.peew.pw/blog/2017/11/26/exploring-cmdkey-an-edge-case-for-privilege-escalation
- https://technet.microsoft.com/en-us/library/cc754243(v=ws.11).aspx
- https://github.com/redcanaryco/atomic-red-team/blob/b27a3cb25025161d49ac861cb216db68c46a3537/atomics/T1003.005/T1003.005.md#atomic-test-1---cached-credential-dump-via-cmdkey

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml)
