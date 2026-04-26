---
sigma_id: "c615d676-f655-46b9-b913-78729021e5d7"
title: "Data Export From MSSQL Table Via BCP.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bcp_export_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcp_export_data.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c615d676-f655-46b9-b913-78729021e5d7"
  - "Data Export From MSSQL Table Via BCP.EXE"
attack_technique_ids:
  - "T1048"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Data Export From MSSQL Table Via BCP.EXE

Detects the execution of the BCP utility in order to export data from the database.
Attackers were seen saving their malware to a database column or table and then later extracting it via "bcp.exe" into a file.

## Metadata

- Rule ID: c615d676-f655-46b9-b913-78729021e5d7
- Status: test
- Level: medium
- Author: Omar Khaled (@beacon_exe), MahirAli Khan (in/mahiralikhan), Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-08-20
- Source Path: rules/windows/process_creation/proc_creation_win_bcp_export_data.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Detection

```yaml
selection_img:
- Image|endswith: \bcp.exe
- OriginalFileName: BCP.exe
selection_cli:
  CommandLine|contains:
  - ' out '
  - ' queryout '
condition: all of selection_*
```

## False Positives

- Legitimate data export operations.

## References

- https://docs.microsoft.com/en-us/sql/tools/bcp-utility
- https://asec.ahnlab.com/en/61000/
- https://asec.ahnlab.com/en/78944/
- https://www.huntress.com/blog/attacking-mssql-servers
- https://www.huntress.com/blog/attacking-mssql-servers-pt-ii
- https://news.sophos.com/en-us/2024/08/07/sophos-mdr-hunt-tracks-mimic-ransomware-campaign-against-organizations-in-india/
- https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcp_export_data.yml)
