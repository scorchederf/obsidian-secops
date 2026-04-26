---
sigma_id: "af4c4609-5755-42fe-8075-4effb49f5d44"
title: "Microsoft Excel Add-In Loaded From Uncommon Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_office_excel_xll_susp_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_excel_xll_susp_load.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "af4c4609-5755-42fe-8075-4effb49f5d44"
  - "Microsoft Excel Add-In Loaded From Uncommon Location"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Microsoft Excel Add-In Loaded From Uncommon Location

Detects Microsoft Excel loading an Add-In (.xll) file from an uncommon location

## Metadata

- Rule ID: af4c4609-5755-42fe-8075-4effb49f5d44
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-12
- Source Path: rules/windows/image_load/image_load_office_excel_xll_susp_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection:
  Image|endswith: \excel.exe
  ImageLoaded|contains:
  - \Desktop\
  - \Downloads\
  - \Perflogs\
  - \Temp\
  - \Users\Public\
  - \Windows\Tasks\
  ImageLoaded|endswith: .xll
condition: selection
```

## False Positives

- Some tuning might be required to allow or remove certain locations used by the rule if you consider them as safe locations

## References

- https://www.mandiant.com/resources/blog/lnk-between-browsers
- https://wazuh.com/blog/detecting-xll-files-used-for-dropping-fin7-jssloader-with-wazuh/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_excel_xll_susp_load.yml)
