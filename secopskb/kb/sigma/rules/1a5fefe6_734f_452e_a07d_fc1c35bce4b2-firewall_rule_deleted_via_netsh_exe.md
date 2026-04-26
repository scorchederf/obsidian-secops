---
sigma_id: "1a5fefe6-734f-452e-a07d-fc1c35bce4b2"
title: "Firewall Rule Deleted Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_fw_delete_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_delete_rule.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1a5fefe6-734f-452e-a07d-fc1c35bce4b2"
  - "Firewall Rule Deleted Via Netsh.EXE"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Firewall Rule Deleted Via Netsh.EXE

Detects the removal of a port or application rule in the Windows Firewall configuration using netsh

## Metadata

- Rule ID: 1a5fefe6-734f-452e-a07d-fc1c35bce4b2
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-14
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_fw_delete_rule.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli:
  CommandLine|contains|all:
  - firewall
  - 'delete '
filter_optional_dropbox:
  ParentImage|endswith: \Dropbox.exe
  CommandLine|contains: name=Dropbox
filter_optional_avast:
  ParentImage|endswith: \instup.exe
  CommandLine|contains: advfirewall firewall delete rule name="Avast Antivirus Admin
    Client"
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate administration activity
- Software installations and removal

## References

- https://app.any.run/tasks/8bbd5b4c-b82d-4e6d-a3ea-d454594a37cc/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_delete_rule.yml)
