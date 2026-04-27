---
sigma_id: "c67fc22a-0be5-4b4f-aad5-2b32c4b69523"
title: "Symlink Etc Passwd"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_symlink_etc_passwd.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_symlink_etc_passwd.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "c67fc22a-0be5-4b4f-aad5-2b32c4b69523"
  - "Symlink Etc Passwd"
attack_technique_ids:
  - "T1204.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Symlink Etc Passwd

Detects suspicious command lines that look as if they would create symbolic links to /etc/passwd

## Metadata

- Rule ID: c67fc22a-0be5-4b4f-aad5-2b32c4b69523
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-04-05
- Modified: 2021-11-27
- Source Path: rules/linux/builtin/lnx_symlink_etc_passwd.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.001]]

## Detection

```yaml
keywords:
- ln -s -f /etc/passwd
- ln -s /etc/passwd
condition: keywords
```

## False Positives

- Unknown

## References

- https://www.qualys.com/2021/05/04/21nails/21nails.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_symlink_etc_passwd.yml)
