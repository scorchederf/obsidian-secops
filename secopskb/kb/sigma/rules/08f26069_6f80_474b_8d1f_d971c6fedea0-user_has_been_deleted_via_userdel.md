---
sigma_id: "08f26069-6f80-474b-8d1f-d971c6fedea0"
title: "User Has Been Deleted Via Userdel"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_userdel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_userdel.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "08f26069-6f80-474b-8d1f-d971c6fedea0"
  - "User Has Been Deleted Via Userdel"
attack_technique_ids:
  - "T1531"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Has Been Deleted Via Userdel

Detects execution of the "userdel" binary. Which is used to delete a user account and related files. This is sometimes abused by threat actors in order to cover their tracks

## Metadata

- Rule ID: 08f26069-6f80-474b-8d1f-d971c6fedea0
- Status: test
- Level: medium
- Author: Tuan Le (NCSGroup)
- Date: 2022-12-26
- Source Path: rules/linux/process_creation/proc_creation_lnx_userdel.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Detection

```yaml
selection:
  Image|endswith: /userdel
condition: selection
```

## False Positives

- Legitimate administrator activities

## References

- https://linuxize.com/post/how-to-delete-group-in-linux/
- https://www.cyberciti.biz/faq/linux-remove-user-command/
- https://www.cybrary.it/blog/0p3n/linux-commands-used-attackers/
- https://linux.die.net/man/8/userdel

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_userdel.yml)
