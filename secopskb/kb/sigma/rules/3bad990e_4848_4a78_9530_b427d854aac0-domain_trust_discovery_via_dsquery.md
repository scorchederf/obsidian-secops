---
sigma_id: "3bad990e-4848-4a78-9530-b427d854aac0"
title: "Domain Trust Discovery Via Dsquery"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dsquery_domain_trust_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dsquery_domain_trust_discovery.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3bad990e-4848-4a78-9530-b427d854aac0"
  - "Domain Trust Discovery Via Dsquery"
attack_technique_ids:
  - "T1482"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Domain Trust Discovery Via Dsquery

Detects execution of "dsquery.exe" for domain trust discovery

## Metadata

- Rule ID: 3bad990e-4848-4a78-9530-b427d854aac0
- Status: test
- Level: medium
- Author: E.M. Anhaus, Tony Lambert, oscd.community, omkar72
- Date: 2019-10-24
- Modified: 2023-02-02
- Source Path: rules/windows/process_creation/proc_creation_win_dsquery_domain_trust_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Detection

```yaml
selection_img:
- Image|endswith: \dsquery.exe
- OriginalFileName: dsquery.exe
selection_cli:
  CommandLine|contains: trustedDomain
condition: all of selection_*
```

## False Positives

- Legitimate use of the utilities by legitimate user for legitimate reason

## Simulation

### Windows - Discover domain trusts with dsquery

- atomic_guid: 4700a710-c821-4e17-a3ec-9e4c81d6845f
- name: Windows - Discover domain trusts with dsquery
- technique: T1482
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1482/T1482.md
- https://posts.specterops.io/an-introduction-to-manual-active-directory-querying-with-dsquery-and-ldapsearch-84943c13d7eb?gi=41b97a644843

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dsquery_domain_trust_discovery.yml)
