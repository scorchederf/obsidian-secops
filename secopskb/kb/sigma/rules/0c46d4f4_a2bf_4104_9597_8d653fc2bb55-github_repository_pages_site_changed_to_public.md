---
sigma_id: "0c46d4f4-a2bf-4104-9597-8d653fc2bb55"
title: "GitHub Repository Pages Site Changed to Public"
framework: "sigma"
generated: "true"
source_path: "rules/application/github/audit/github_pages_site_changed_to_public.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_pages_site_changed_to_public.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "low"
logsource: "github / audit"
aliases:
  - "0c46d4f4-a2bf-4104-9597-8d653fc2bb55"
  - "GitHub Repository Pages Site Changed to Public"
attack_technique_ids:
  - "T1567.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# GitHub Repository Pages Site Changed to Public

Detects when a GitHub Pages site of a repository is made public. This usually is part of a publishing process but could indicate or lead to potential unauthorized exposure of sensitive information or code.

## Metadata

- Rule ID: 0c46d4f4-a2bf-4104-9597-8d653fc2bb55
- Status: experimental
- Level: low
- Author: Ivan Saakov
- Date: 2025-10-18
- Source Path: rules/application/github/audit/github_pages_site_changed_to_public.yml

## Logsource

- product: github
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.001]]

## Detection

```yaml
selection:
  action: repo.pages_public
condition: selection
```

## False Positives

- Legitimate publishing of repository pages by authorized users

## References

- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://www.sentinelone.com/blog/exploiting-repos-6-ways-threat-actors-abuse-github-other-devops-platforms
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/security-log-events

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/application/github/audit/github_pages_site_changed_to_public.yml)
