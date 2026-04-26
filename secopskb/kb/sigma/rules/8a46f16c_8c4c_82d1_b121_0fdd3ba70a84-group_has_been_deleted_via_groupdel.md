---
sigma_id: "8a46f16c-8c4c-82d1-b121-0fdd3ba70a84"
title: "Group Has Been Deleted Via Groupdel"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_groupdel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_groupdel.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "8a46f16c-8c4c-82d1-b121-0fdd3ba70a84"
  - "Group Has Been Deleted Via Groupdel"
attack_technique_ids:
  - "T1531"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Group Has Been Deleted Via Groupdel

Detects execution of the "groupdel" binary. Which is used to delete a group. This is sometimes abused by threat actors in order to cover their tracks

## Metadata

- Rule ID: 8a46f16c-8c4c-82d1-b121-0fdd3ba70a84
- Status: test
- Level: medium
- Author: Tuan Le (NCSGroup)
- Date: 2022-12-26
- Source Path: rules/linux/process_creation/proc_creation_lnx_groupdel.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Detection

```yaml
selection:
  Image|endswith: /groupdel
condition: selection
```

## False Positives

- Legitimate administrator activities

## References

- https://linuxize.com/post/how-to-delete-group-in-linux/
- https://www.cyberciti.biz/faq/linux-remove-user-command/
- https://www.cybrary.it/blog/0p3n/linux-commands-used-attackers/
- https://linux.die.net/man/8/groupdel

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_groupdel.yml)
