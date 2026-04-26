---
sigma_id: "b5c7395f-e501-4a08-94d4-57fe7a9da9d2"
title: "Potential Binary Proxy Execution Via Cdb.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cdb_arbitrary_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cdb_arbitrary_command_execution.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b5c7395f-e501-4a08-94d4-57fe7a9da9d2"
  - "Potential Binary Proxy Execution Via Cdb.EXE"
attack_technique_ids:
  - "T1106"
  - "T1218"
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Binary Proxy Execution Via Cdb.EXE

Detects usage of "cdb.exe" to launch arbitrary processes or commands from a debugger script file

## Metadata

- Rule ID: b5c7395f-e501-4a08-94d4-57fe7a9da9d2
- Status: test
- Level: medium
- Author: Beyu Denis, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-10-26
- Modified: 2024-04-22
- Source Path: rules/windows/process_creation/proc_creation_win_cdb_arbitrary_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1106-native_api|T1106]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection_img:
- Image|endswith: \cdb.exe
- OriginalFileName: CDB.Exe
selection_cli:
  CommandLine|contains:
  - ' -c '
  - ' -cf '
condition: all of selection*
```

## False Positives

- Legitimate use of debugging tools

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Cdb/
- https://web.archive.org/web/20170715043507/http://www.exploit-monday.com/2016/08/windbg-cdb-shellcode-runner.html
- https://twitter.com/nas_bench/status/1534957360032120833

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cdb_arbitrary_command_execution.yml)
