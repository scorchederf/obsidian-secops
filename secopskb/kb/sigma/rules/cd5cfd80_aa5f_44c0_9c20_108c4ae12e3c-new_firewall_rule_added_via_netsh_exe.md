---
sigma_id: "cd5cfd80-aa5f-44c0-9c20-108c4ae12e3c"
title: "New Firewall Rule Added Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_fw_add_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_add_rule.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cd5cfd80-aa5f-44c0-9c20-108c4ae12e3c"
  - "New Firewall Rule Added Via Netsh.EXE"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Firewall Rule Added Via Netsh.EXE

Detects the addition of a new rule to the Windows firewall via netsh

## Metadata

- Rule ID: cd5cfd80-aa5f-44c0-9c20-108c4ae12e3c
- Status: test
- Level: medium
- Author: Markus Neis, Sander Wiebing
- Date: 2019-01-29
- Modified: 2023-02-10
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_fw_add_rule.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

### Software Tags

- S0246

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli:
  CommandLine|contains|all:
  - ' firewall '
  - ' add '
filter_optional_dropbox:
  CommandLine|contains:
  - advfirewall firewall add rule name=Dropbox dir=in action=allow "program=?:\Program
    Files (x86)\Dropbox\Client\Dropbox.exe" enable=yes profile=Any
  - advfirewall firewall add rule name=Dropbox dir=in action=allow "program=?:\Program
    Files\Dropbox\Client\Dropbox.exe" enable=yes profile=Any
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate administration activity
- Software installations

## References

- https://web.archive.org/web/20190508165435/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_add_rule.yml)
