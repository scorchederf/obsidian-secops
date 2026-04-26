---
sigma_id: "45e112d0-7759-4c2a-aa36-9f8fb79d3393"
title: "IE Change Domain Zone"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_change_security_zones.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_change_security_zones.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "45e112d0-7759-4c2a-aa36-9f8fb79d3393"
  - "IE Change Domain Zone"
attack_technique_ids:
  - "T1137"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# IE Change Domain Zone

Hides the file extension through modification of the registry

## Metadata

- Rule ID: 45e112d0-7759-4c2a-aa36-9f8fb79d3393
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-22
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_change_security_zones.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137]]

## Detection

```yaml
selection_domains:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\
filter:
  Details:
  - DWORD (0x00000000)
  - DWORD (0x00000001)
  - (Empty)
condition: selection_domains and not filter
```

## False Positives

- Administrative scripts

## Simulation

### Add Domain to Trusted Sites Zone

- atomic_guid: cf447677-5a4e-4937-a82c-e47d254afd57
- name: Add Domain to Trusted Sites Zone
- technique: T1112
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1112/T1112.md#atomic-test-4---add-domain-to-trusted-sites-zone
- https://learn.microsoft.com/en-us/troubleshoot/developer/browsers/security-privacy/ie-security-zones-registry-entries

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_change_security_zones.yml)
