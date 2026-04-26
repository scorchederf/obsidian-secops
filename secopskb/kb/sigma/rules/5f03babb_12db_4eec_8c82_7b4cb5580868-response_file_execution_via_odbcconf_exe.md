---
sigma_id: "5f03babb-12db-4eec-8c82-7b4cb5580868"
title: "Response File Execution Via Odbcconf.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_odbcconf_response_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_response_file.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5f03babb-12db-4eec-8c82-7b4cb5580868"
  - "Response File Execution Via Odbcconf.EXE"
attack_technique_ids:
  - "T1218.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Response File Execution Via Odbcconf.EXE

Detects execution of "odbcconf" with the "-f" flag in order to load a response file which might contain a malicious action.

## Metadata

- Rule ID: 5f03babb-12db-4eec-8c82-7b4cb5580868
- Status: test
- Level: medium
- Author: Kirill Kiryanov, Beyu Denis, Daniil Yugoslavskiy, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-22
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_odbcconf_response_file.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.008]]

## Detection

```yaml
selection_img:
- Image|endswith: \odbcconf.exe
- OriginalFileName: odbcconf.exe
selection_cli:
  CommandLine|contains|windash: ' -f '
selection_rsp_ext:
  CommandLine|contains: .rsp
condition: all of selection_*
```

## False Positives

- The rule is looking for any usage of response file, which might generate false positive when this function is used legitimately. Investigate the contents of the ".rsp" file to determine if it is malicious and apply additional filters if necessary.

## References

- https://learn.microsoft.com/en-us/sql/odbc/odbcconf-exe?view=sql-server-ver16
- https://lolbas-project.github.io/lolbas/Binaries/Odbcconf/
- https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control
- https://www.hexacorn.com/blog/2020/08/23/odbcconf-lolbin-trifecta/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_odbcconf_response_file.yml)
