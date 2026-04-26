---
sigma_id: "e290b10b-1023-4452-a4a9-eb31a9013b3a"
title: "LOLBAS Data Exfiltration by DataSvcUtil.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_data_exfiltration_by_using_datasvcutil.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_data_exfiltration_by_using_datasvcutil.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e290b10b-1023-4452-a4a9-eb31a9013b3a"
  - "LOLBAS Data Exfiltration by DataSvcUtil.exe"
attack_technique_ids:
  - "T1567"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LOLBAS Data Exfiltration by DataSvcUtil.exe

Detects when a user performs data exfiltration by using DataSvcUtil.exe

## Metadata

- Rule ID: e290b10b-1023-4452-a4a9-eb31a9013b3a
- Status: test
- Level: medium
- Author: Ialle Teixeira @teixeira0xfffff, Austin Songer @austinsonger
- Date: 2021-09-30
- Modified: 2022-05-16
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_data_exfiltration_by_using_datasvcutil.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]

## Detection

```yaml
selection_cli:
  CommandLine|contains:
  - '/in:'
  - '/out:'
  - '/uri:'
selection_img:
- Image|endswith: \DataSvcUtil.exe
- OriginalFileName: DataSvcUtil.exe
condition: all of selection*
```

## False Positives

- DataSvcUtil.exe being used may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- DataSvcUtil.exe being executed from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://gist.github.com/teixeira0xfffff/837e5bfed0d1b0a29a7cb1e5dbdd9ca6
- https://learn.microsoft.com/en-us/previous-versions/dotnet/framework/data/wcf/wcf-data-service-client-utility-datasvcutil-exe
- https://learn.microsoft.com/en-us/previous-versions/dotnet/framework/data/wcf/generating-the-data-service-client-library-wcf-data-services
- https://learn.microsoft.com/en-us/previous-versions/dotnet/framework/data/wcf/how-to-add-a-data-service-reference-wcf-data-services
- https://lolbas-project.github.io/lolbas/Binaries/DataSvcUtil/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_data_exfiltration_by_using_datasvcutil.yml)
