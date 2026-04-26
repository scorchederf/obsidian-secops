---
sigma_id: "dca8991c-cb16-4128-abf8-6b11e5cd156f"
title: "GitHub Repository Archive Status Changed"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_repository_archive_status_changed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_repository_archive_status_changed.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "low"
logsource: "github / audit"
aliases:
  - "dca8991c-cb16-4128-abf8-6b11e5cd156f"
  - "GitHub Repository Archive Status Changed"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# GitHub Repository Archive Status Changed

Detects when a GitHub repository is archived or unarchived, which may indicate unauthorized changes to repository status.

## Metadata

- Rule ID: dca8991c-cb16-4128-abf8-6b11e5cd156f
- Status: experimental
- Level: low
- Author: Ivan Saakov
- Date: 2025-10-18
- Source Path: rules/application/github/audit/github_repository_archive_status_changed.yml

## Logsource

- product: github
- service: audit

## Detection

```yaml
selection:
  action:
  - repo.archived
  - repo.unarchived
condition: selection
```

## False Positives

- Archiving or unarchiving a repository is often legitimate. Investigate this action to determine if it was authorized.

## References

- https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories
- https://www.sentinelone.com/blog/exploiting-repos-6-ways-threat-actors-abuse-github-other-devops-platforms
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/security-log-events

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_repository_archive_status_changed.yml)
