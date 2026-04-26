---
sigma_id: "e83e8899-c9b2-483b-b355-5decc942b959"
title: "Interesting Service Enumeration Via Sc.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_query_interesting_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_query_interesting_services.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "e83e8899-c9b2-483b-b355-5decc942b959"
  - "Interesting Service Enumeration Via Sc.EXE"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Interesting Service Enumeration Via Sc.EXE

Detects the enumeration and query of interesting and in some cases sensitive services on the system via "sc.exe".
Attackers often try to enumerate the services currently running on a system in order to find different attack vectors.

## Metadata

- Rule ID: e83e8899-c9b2-483b-b355-5decc942b959
- Status: test
- Level: low
- Author: Swachchhanda Shrawan Poudel
- Date: 2024-02-12
- Source Path: rules/windows/process_creation/proc_creation_win_sc_query_interesting_services.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection_img:
- Image|endswith: \sc.exe
- OriginalFileName: sc.exe
selection_cli:
  CommandLine|contains: query
selection_cmd:
  CommandLine|contains: termservice
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.n00py.io/2021/05/dumping-plaintext-rdp-credentials-from-svchost-exe/
- https://pentestlab.blog/tag/svchost/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_query_interesting_services.yml)
