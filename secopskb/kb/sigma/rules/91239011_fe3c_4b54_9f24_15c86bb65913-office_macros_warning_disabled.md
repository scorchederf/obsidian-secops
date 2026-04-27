---
sigma_id: "91239011-fe3c-4b54-9f24-15c86bb65913"
title: "Office Macros Warning Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_vba_warnings_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_vba_warnings_tamper.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "91239011-fe3c-4b54-9f24-15c86bb65913"
  - "Office Macros Warning Disabled"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects registry changes to Microsoft Office "VBAWarning" to a value of "1" which enables the execution of all macros, whether signed or unsigned.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Security\VBAWarnings
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_vba_warnings_tamper.yml)
