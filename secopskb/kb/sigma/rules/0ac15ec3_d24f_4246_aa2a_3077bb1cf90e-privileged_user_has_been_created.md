---
sigma_id: "0ac15ec3-d24f-4246-aa2a-3077bb1cf90e"
title: "Privileged User Has Been Created"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_privileged_user_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_privileged_user_creation.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "0ac15ec3-d24f-4246-aa2a-3077bb1cf90e"
  - "Privileged User Has Been Created"
attack_technique_ids:
  - "T1136.001"
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Privileged User Has Been Created

Detects the addition of a new user to a privileged group such as "root" or "sudo"

## Metadata

- Rule ID: 0ac15ec3-d24f-4246-aa2a-3077bb1cf90e
- Status: test
- Level: high
- Author: Pawel Mazur
- Date: 2022-12-21
- Modified: 2025-01-21
- Source Path: rules/linux/builtin/lnx_privileged_user_creation.yml

## Logsource

- definition: /var/log/secure on REHL systems or /var/log/auth.log on debian like Systems needs to be collected in order for this detection to work
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection_new_user:
- new user
selection_uids_gids:
- GID=0,
- UID=0,
- GID=10,
- GID=27,
condition: all of selection_*
```

## False Positives

- Administrative activity

## References

- https://digital.nhs.uk/cyber-alerts/2018/cc-2825
- https://linux.die.net/man/8/useradd
- https://github.com/redcanaryco/atomic-red-team/blob/25acadc0b43a07125a8a5b599b28bbc1a91ffb06/atomics/T1136.001/T1136.001.md#atomic-test-5---create-a-new-user-in-linux-with-root-uid-and-gid

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_privileged_user_creation.yml)
