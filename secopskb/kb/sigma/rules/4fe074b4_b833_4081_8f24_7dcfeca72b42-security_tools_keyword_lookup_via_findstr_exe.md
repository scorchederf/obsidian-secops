---
sigma_id: "4fe074b4-b833-4081-8f24-7dcfeca72b42"
title: "Security Tools Keyword Lookup Via Findstr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_security_keyword_lookup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_security_keyword_lookup.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4fe074b4-b833-4081-8f24-7dcfeca72b42"
  - "Security Tools Keyword Lookup Via Findstr.EXE"
attack_technique_ids:
  - "T1518.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Security Tools Keyword Lookup Via Findstr.EXE

Detects execution of "findstr" to search for common names of security tools. Attackers often pipe the results of recon commands such as "tasklist" or "whoami" to "findstr" in order to filter out the results.
This detection focuses on the keywords that the attacker might use as a filter.

## Metadata

- Rule ID: 4fe074b4-b833-4081-8f24-7dcfeca72b42
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2023-10-20
- Modified: 2023-11-14
- Source Path: rules/windows/process_creation/proc_creation_win_findstr_security_keyword_lookup.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \find.exe
  - \findstr.exe
- OriginalFileName:
  - FIND.EXE
  - FINDSTR.EXE
selection_cli:
  CommandLine|endswith:
  - ' avira'
  - ' avira"'
  - ' cb'
  - ' cb"'
  - ' cylance'
  - ' cylance"'
  - ' defender'
  - ' defender"'
  - ' kaspersky'
  - ' kaspersky"'
  - ' kes'
  - ' kes"'
  - ' mc'
  - ' mc"'
  - ' sec'
  - ' sec"'
  - ' sentinel'
  - ' sentinel"'
  - ' symantec'
  - ' symantec"'
  - ' virus'
  - ' virus"'
condition: all of selection_*
```

## False Positives

- Unknown

## Simulation

### Security Software Discovery

- atomic_guid: f92a380f-ced9-491f-b338-95a991418ce2
- name: Security Software Discovery
- technique: T1518.001
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/987e3ca988ae3cff4b9f6e388c139c05bf44bbb8/atomics/T1518.001/T1518.001.md#atomic-test-1---security-software-discovery
- https://www.microsoft.com/en-us/security/blog/2023/10/18/multiple-north-korean-threat-actors-exploiting-the-teamcity-cve-2023-42793-vulnerability/
- https://www.hhs.gov/sites/default/files/manage-engine-vulnerability-sector-alert-tlpclear.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_security_keyword_lookup.yml)
