---
sigma_id: "6f535e01-ca1f-40be-ab8d-45b19c0c8b7f"
title: "Import LDAP Data Interchange Format File Via Ldifde.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "6f535e01-ca1f-40be-ab8d-45b19c0c8b7f"
  - "Import LDAP Data Interchange Format File Via Ldifde.EXE"
attack_technique_ids:
  - "T1218"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Import LDAP Data Interchange Format File Via Ldifde.EXE

Detects the execution of "Ldifde.exe" with the import flag "-i". The can be abused to include HTTP-based arguments which will allow the arbitrary download of files from a remote server.

## Metadata

- Rule ID: 6f535e01-ca1f-40be-ab8d-45b19c0c8b7f
- Status: test
- Level: medium
- Author: @gott_cyber
- Date: 2022-09-02
- Modified: 2023-03-14
- Source Path: rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
- Image|endswith: \ldifde.exe
- OriginalFileName: ldifde.exe
selection_cli:
  CommandLine|contains|all:
  - -i
  - -f
condition: all of selection_*
```

## False Positives

- Since the content of the files are unknown, false positives are expected

## References

- https://twitter.com/0gtweet/status/1564968845726580736
- https://strontic.github.io/xcyclopedia/library/ldifde.exe-979DE101F5059CEC1D2C56967CA2BAC0.html
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731033(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ldifde_file_load.yml)
