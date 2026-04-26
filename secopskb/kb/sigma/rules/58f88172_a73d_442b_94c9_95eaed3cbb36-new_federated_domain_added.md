---
sigma_id: "58f88172-a73d-442b-94c9-95eaed3cbb36"
title: "New Federated Domain Added"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/audit/microsoft365_new_federated_domain_added_audit.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/audit/microsoft365_new_federated_domain_added_audit.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "m365 / audit"
aliases:
  - "58f88172-a73d-442b-94c9-95eaed3cbb36"
  - "New Federated Domain Added"
attack_technique_ids:
  - "T1484.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Federated Domain Added

Detects the addition of a new Federated Domain.

## Metadata

- Rule ID: 58f88172-a73d-442b-94c9-95eaed3cbb36
- Status: test
- Level: medium
- Author: Splunk Threat Research Team (original rule), Harjot Singh @cyb3rjy0t (sigma rule)
- Date: 2023-09-18
- Source Path: rules/cloud/m365/audit/microsoft365_new_federated_domain_added_audit.yml

## Logsource

- product: m365
- service: audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification|T1484.002]]

## Detection

```yaml
selection_domain:
  Operation|contains: domain
selection_operation:
  Operation|contains:
  - add
  - new
condition: all of selection_*
```

## False Positives

- The creation of a new Federated domain is not necessarily malicious, however these events need to be followed closely, as it may indicate federated credential abuse or backdoor via federated identities at a similar or different cloud provider.

## References

- https://research.splunk.com/cloud/e155876a-6048-11eb-ae93-0242ac130002/
- https://o365blog.com/post/aadbackdoor/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/audit/microsoft365_new_federated_domain_added_audit.yml)
