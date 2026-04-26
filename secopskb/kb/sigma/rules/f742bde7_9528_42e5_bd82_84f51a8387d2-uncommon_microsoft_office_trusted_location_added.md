---
sigma_id: "f742bde7-9528-42e5-bd82-84f51a8387d2"
title: "Uncommon Microsoft Office Trusted Location Added"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_trusted_location_uncommon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_trusted_location_uncommon.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "f742bde7-9528-42e5-bd82-84f51a8387d2"
  - "Uncommon Microsoft Office Trusted Location Added"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Uncommon Microsoft Office Trusted Location Added

Detects changes to registry keys related to "Trusted Location" of Microsoft Office where the path is set to something uncommon. Attackers might add additional trusted locations to avoid macro security restrictions.

## Metadata

- Rule ID: f742bde7-9528-42e5-bd82-84f51a8387d2
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-21
- Modified: 2023-09-29
- Source Path: rules/windows/registry/registry_set/registry_set_office_trusted_location_uncommon.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|contains: Security\Trusted Locations\Location
  TargetObject|endswith: \Path
filter_exclude_known_paths:
  Details|contains:
  - '%APPDATA%\Microsoft\Templates'
  - '%%APPDATA%%\Microsoft\Templates'
  - '%APPDATA%\Microsoft\Word\Startup'
  - '%%APPDATA%%\Microsoft\Word\Startup'
  - :\Program Files (x86)\Microsoft Office\root\Templates\
  - :\Program Files\Microsoft Office (x86)\Templates
  - :\Program Files\Microsoft Office\root\Templates\
  - :\Program Files\Microsoft Office\Templates\
filter_main_office_click_to_run:
  Image|contains: :\Program Files\Common Files\Microsoft Shared\ClickToRun\
  Image|endswith: \OfficeClickToRun.exe
filter_main_office_apps:
  Image|contains:
  - :\Program Files\Microsoft Office\
  - :\Program Files (x86)\Microsoft Office\
condition: selection and not 1 of filter_main_* and not 1 of filter_exclude_*
```

## False Positives

- Other unknown legitimate or custom paths need to be filtered to avoid false positives

## References

- Internal Research
- https://admx.help/?Category=Office2016&Policy=excel16.Office.Microsoft.Policies.Windows::L_TrustedLoc01

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_trusted_location_uncommon.yml)
