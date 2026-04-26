---
sigma_id: "f37aba28-a9e6-4045-882c-d5004043b337"
title: "Potential Arbitrary File Download Via Cmdl32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmdl32_arbitrary_file_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmdl32_arbitrary_file_download.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f37aba28-a9e6-4045-882c-d5004043b337"
  - "Potential Arbitrary File Download Via Cmdl32.EXE"
attack_technique_ids:
  - "T1218"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Arbitrary File Download Via Cmdl32.EXE

Detects execution of Cmdl32 with the "/vpn" and "/lan" flags.
Attackers can abuse this utility in order to download arbitrary files via a configuration file.
Inspect the location and the content of the file passed as an argument in order to determine if it is suspicious.

## Metadata

- Rule ID: f37aba28-a9e6-4045-882c-d5004043b337
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-03
- Modified: 2024-04-22
- Source Path: rules/windows/process_creation/proc_creation_win_cmdl32_arbitrary_file_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmdl32.exe
- OriginalFileName: CMDL32.EXE
selection_cli:
  CommandLine|contains|all:
  - /vpn
  - /lan
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Cmdl32/
- https://twitter.com/SwiftOnSecurity/status/1455897435063074824
- https://github.com/LOLBAS-Project/LOLBAS/pull/151

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmdl32_arbitrary_file_download.yml)
