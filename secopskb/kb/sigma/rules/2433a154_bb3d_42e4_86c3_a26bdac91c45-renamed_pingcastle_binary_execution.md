---
sigma_id: "2433a154-bb3d-42e4-86c3-a26bdac91c45"
title: "Renamed PingCastle Binary Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_pingcastle.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_pingcastle.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2433a154-bb3d-42e4-86c3-a26bdac91c45"
  - "Renamed PingCastle Binary Execution"
attack_technique_ids:
  - "T1059"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed PingCastle Binary Execution

Detects the execution of a renamed "PingCastle" binary based on the PE metadata fields.

## Metadata

- Rule ID: 2433a154-bb3d-42e4-86c3-a26bdac91c45
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), X__Junior (Nextron Systems)
- Date: 2024-01-11
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_pingcastle.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
- OriginalFileName:
  - PingCastleReporting.exe
  - PingCastleCloud.exe
  - PingCastle.exe
- CommandLine|contains:
  - --scanner aclcheck
  - --scanner antivirus
  - --scanner computerversion
  - --scanner foreignusers
  - --scanner laps_bitlocker
  - --scanner localadmin
  - --scanner nullsession
  - --scanner nullsession-trust
  - --scanner oxidbindings
  - --scanner remote
  - --scanner share
  - --scanner smb
  - --scanner smb3querynetwork
  - --scanner spooler
  - --scanner startup
  - --scanner zerologon
- CommandLine|contains: --no-enum-limit
- CommandLine|contains|all:
  - --healthcheck
  - --level Full
- CommandLine|contains|all:
  - --healthcheck
  - '--server '
filter_main_img:
  Image|endswith:
  - \PingCastleReporting.exe
  - \PingCastleCloud.exe
  - \PingCastle.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2023/10/30/netsupport-intrusion-results-in-domain-compromise/
- https://www.pingcastle.com/documentation/scanner/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_pingcastle.yml)
