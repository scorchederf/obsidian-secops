---
sigma_id: "16ab6143-510a-44e2-a615-bdb80b8317fc"
title: "Bitbucket Global SSH Settings Changed"
framework: "sigma"
generated: "true"
source_path: "rules/application/bitbucket/audit/bitbucket_audit_global_ssh_settings_change_detected.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_global_ssh_settings_change_detected.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "bitbucket / audit"
aliases:
  - "16ab6143-510a-44e2-a615-bdb80b8317fc"
  - "Bitbucket Global SSH Settings Changed"
attack_technique_ids:
  - "T1562.001"
  - "T1021.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bitbucket Global SSH Settings Changed

Detects Bitbucket global SSH access configuration changes.

## Metadata

- Rule ID: 16ab6143-510a-44e2-a615-bdb80b8317fc
- Status: test
- Level: medium
- Author: Muhammad Faisal (@faisalusuf)
- Date: 2024-02-25
- Source Path: rules/application/bitbucket/audit/bitbucket_audit_global_ssh_settings_change_detected.yml

## Logsource

- definition: Requirements: "Advance" log level is required to receive these audit events.
- product: bitbucket
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021.004]]

## Detection

```yaml
selection:
  auditType.category: Global administration
  auditType.action: SSH settings changed
condition: selection
```

## False Positives

- Legitimate user activity.

## References

- https://confluence.atlassian.com/bitbucketserver/audit-log-events-776640423.html
- https://confluence.atlassian.com/bitbucketserver/enable-ssh-access-to-git-repositories-776640358.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/bitbucket/audit/bitbucket_audit_global_ssh_settings_change_detected.yml)
