---
sigma_id: "234f9f48-904b-4736-a34c-55d23919e4b7"
title: "Google Cloud Re-identifies Sensitive Information"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_dlp_re_identifies_sensitive_information.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_dlp_re_identifies_sensitive_information.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "234f9f48-904b-4736-a34c-55d23919e4b7"
  - "Google Cloud Re-identifies Sensitive Information"
attack_technique_ids:
  - "T1565"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Re-identifies Sensitive Information

Identifies when sensitive information is re-identified in google Cloud.

## Metadata

- Rule ID: 234f9f48-904b-4736-a34c-55d23919e4b7
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-15
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_dlp_re_identifies_sensitive_information.yml

## Logsource

- product: gcp
- service: gcp.audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1565-data_manipulation|T1565]]

## Detection

```yaml
selection:
  gcp.audit.method_name: projects.content.reidentify
condition: selection
```

## False Positives

- Unknown

## References

- https://cloud.google.com/dlp/docs/reference/rest/v2/projects.content/reidentify

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_dlp_re_identifies_sensitive_information.yml)
