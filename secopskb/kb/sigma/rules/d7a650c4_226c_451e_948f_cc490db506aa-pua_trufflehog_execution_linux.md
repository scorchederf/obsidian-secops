---
sigma_id: "d7a650c4-226c-451e-948f-cc490db506aa"
title: "PUA - TruffleHog Execution - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_pua_trufflehog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_pua_trufflehog.yml"
build_date: "2026-04-26 14:14:30"
status: "experimental"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "d7a650c4-226c-451e-948f-cc490db506aa"
  - "PUA - TruffleHog Execution - Linux"
attack_technique_ids:
  - "T1083"
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - TruffleHog Execution - Linux

Detects execution of TruffleHog, a tool used to search for secrets in different platforms like Git, Jira, Slack, SharePoint, etc. that could be used maliciously.
While it is a legitimate tool, intended for use in CI pipelines and security assessments,
It was observed in the Shai-Hulud malware campaign targeting npm packages to steal sensitive information.

## Metadata

- Rule ID: d7a650c4-226c-451e-948f-cc490db506aa
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-09-24
- Source Path: rules/linux/process_creation/proc_creation_lnx_pua_trufflehog.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Detection

```yaml
selection_img:
  Image|endswith: /trufflehog
selection_cli_platform:
  CommandLine|contains:
  - ' docker --image '
  - ' Git '
  - ' GitHub '
  - ' Jira '
  - ' Slack '
  - ' Confluence '
  - ' SharePoint '
  - ' s3 '
  - ' gcs '
selection_cli_verified:
  CommandLine|contains: ' --results=verified'
condition: selection_img or all of selection_cli_*
```

## False Positives

- Legitimate use of TruffleHog by security teams or developers.

## References

- https://github.com/trufflesecurity/trufflehog
- https://www.getsafety.com/blog-posts/shai-hulud-npm-attack

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_pua_trufflehog.yml)
