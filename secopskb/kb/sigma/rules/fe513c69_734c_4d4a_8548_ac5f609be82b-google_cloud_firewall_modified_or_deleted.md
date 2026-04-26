---
sigma_id: "fe513c69-734c-4d4a-8548-ac5f609be82b"
title: "Google Cloud Firewall Modified or Deleted"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_firewall_rule_modified_or_deleted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_firewall_rule_modified_or_deleted.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "fe513c69-734c-4d4a-8548-ac5f609be82b"
  - "Google Cloud Firewall Modified or Deleted"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Firewall Modified or Deleted

Detects  when a firewall rule is modified or deleted in Google Cloud Platform (GCP).

## Metadata

- Rule ID: fe513c69-734c-4d4a-8548-ac5f609be82b
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-13
- Modified: 2022-10-09
- Source Path: rules/cloud/gcp/audit/gcp_firewall_rule_modified_or_deleted.yml

## Logsource

- product: gcp
- service: gcp.audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  gcp.audit.method_name:
  - v*.Compute.Firewalls.Delete
  - v*.Compute.Firewalls.Patch
  - v*.Compute.Firewalls.Update
  - v*.Compute.Firewalls.Insert
condition: selection
```

## False Positives

- Firewall rules being modified or deleted may be performed by a system administrator. Verify that the firewall configuration change was expected.
- Exceptions can be added to this rule to filter expected behavior.

## References

- https://cloud.google.com/kubernetes-engine/docs/how-to/audit-logging
- https://developers.google.com/resources/api-libraries/documentation/compute/v1/java/latest/com/google/api/services/compute/Compute.Firewalls.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_firewall_rule_modified_or_deleted.yml)
