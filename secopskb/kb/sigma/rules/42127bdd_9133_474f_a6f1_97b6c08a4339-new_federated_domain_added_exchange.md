---
sigma_id: "42127bdd-9133-474f-a6f1-97b6c08a4339"
title: "New Federated Domain Added - Exchange"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/m365/exchange/microsoft365_new_federated_domain_added_exchange.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/exchange/microsoft365_new_federated_domain_added_exchange.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "m365 / exchange"
aliases:
  - "42127bdd-9133-474f-a6f1-97b6c08a4339"
  - "New Federated Domain Added - Exchange"
attack_technique_ids:
  - "T1136.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Federated Domain Added - Exchange

Detects the addition of a new Federated Domain.

## Metadata

- Rule ID: 42127bdd-9133-474f-a6f1-97b6c08a4339
- Status: test
- Level: medium
- Author: Splunk Threat Research Team (original rule), '@ionsor (rule)'
- Date: 2022-02-08
- Source Path: rules/cloud/m365/exchange/microsoft365_new_federated_domain_added_exchange.yml

## Logsource

- product: m365
- service: exchange

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.003]]

## Detection

```yaml
selection:
  eventSource: Exchange
  eventName: Add-FederatedDomain
  status: success
condition: selection
```

## False Positives

- The creation of a new Federated domain is not necessarily malicious, however these events need to be followed closely, as it may indicate federated credential abuse or backdoor via federated identities at a similar or different cloud provider.

## References

- https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/wp-m-unc2452-2021-000343-01.pdf
- https://us-cert.cisa.gov/ncas/alerts/aa21-008a
- https://www.splunk.com/en_us/blog/security/a-golden-saml-journey-solarwinds-continued.html
- https://www.sygnia.co/golden-saml-advisory
- https://o365blog.com/post/aadbackdoor/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/m365/exchange/microsoft365_new_federated_domain_added_exchange.yml)
