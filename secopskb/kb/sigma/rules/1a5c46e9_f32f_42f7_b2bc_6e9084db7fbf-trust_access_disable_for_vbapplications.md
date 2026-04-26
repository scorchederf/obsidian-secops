---
sigma_id: "1a5c46e9-f32f-42f7-b2bc-6e9084db7fbf"
title: "Trust Access Disable For VBApplications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_access_vbom_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_access_vbom_tamper.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "1a5c46e9-f32f-42f7-b2bc-6e9084db7fbf"
  - "Trust Access Disable For VBApplications"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Trust Access Disable For VBApplications

Detects registry changes to Microsoft Office "AccessVBOM" to a value of "1" which disables trust access for VBA on the victim machine and lets attackers execute malicious macros without any Microsoft Office warnings.

## Metadata

- Rule ID: 1a5c46e9-f32f-42f7-b2bc-6e9084db7fbf
- Status: test
- Level: high
- Author: Trent Liffick (@tliffick), Nasreddine Bencherchali (Nextron Systems)
- Date: 2020-05-22
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_office_access_vbom_tamper.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Security\AccessVBOM
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unlikely

## References

- https://twitter.com/inversecos/status/1494174785621819397
- https://www.mcafee.com/blogs/other-blogs/mcafee-labs/zloader-with-a-new-infection-technique/
- https://securelist.com/scarcruft-surveilling-north-korean-defectors-and-human-rights-activists/105074/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_access_vbom_tamper.yml)
