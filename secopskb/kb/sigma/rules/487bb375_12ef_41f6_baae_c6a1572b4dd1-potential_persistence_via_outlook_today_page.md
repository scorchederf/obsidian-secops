---
sigma_id: "487bb375-12ef-41f6-baae-c6a1572b4dd1"
title: "Potential Persistence Via Outlook Today Page"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_outlook_todaypage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_outlook_todaypage.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "487bb375-12ef-41f6-baae-c6a1572b4dd1"
  - "Potential Persistence Via Outlook Today Page"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via Outlook Today Page

Detects potential persistence activity via outlook today page.
An attacker can set a custom page to execute arbitrary code and link to it via the registry values "URL" and "UserDefinedUrl".

## Metadata

- Rule ID: 487bb375-12ef-41f6-baae-c6a1572b4dd1
- Status: test
- Level: high
- Author: Tobias Michalski (Nextron Systems), David Bertho (@dbertho) & Eirik Sveen (@0xSV1), Storebrand
- Date: 2021-06-10
- Modified: 2024-08-07
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_outlook_todaypage.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_main:
  TargetObject|contains|all:
  - Software\Microsoft\Office\
  - \Outlook\Today\
selection_value_stamp:
  TargetObject|endswith: \Stamp
  Details: DWORD (0x00000001)
selection_value_url:
  TargetObject|endswith:
  - \URL
  - \UserDefinedUrl
filter_main_office:
  Image|startswith:
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\
  - C:\Program Files\Common Files\Microsoft Shared\ClickToRun\Updates\
  Image|endswith: \OfficeClickToRun.exe
condition: selection_main and 1 of selection_value_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=74
- https://trustedsec.com/blog/specula-turning-outlook-into-a-c2-with-one-registry-change

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_outlook_todaypage.yml)
