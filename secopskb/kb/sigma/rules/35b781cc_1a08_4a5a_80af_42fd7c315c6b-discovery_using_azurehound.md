---
sigma_id: "35b781cc-1a08-4a5a-80af-42fd7c315c6b"
title: "Discovery Using AzureHound"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/signin_logs/azure_ad_azurehound_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_azurehound_discovery.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "azure / signinlogs"
aliases:
  - "35b781cc-1a08-4a5a-80af-42fd7c315c6b"
  - "Discovery Using AzureHound"
attack_technique_ids:
  - "T1087.004"
  - "T1526"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects AzureHound (A BloodHound data collector for Microsoft Azure) activity via the default User-Agent that is used during its operation after successful authentication.

## Logsource

- product: azure
- service: signinlogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery#^t1087004-cloud-account|T1087.004: Cloud Account]]
- [[kb/attack/techniques/T1526-cloud_service_discovery|T1526: Cloud Service Discovery]]

## Detection

```yaml
selection:
  userAgent|contains: azurehound
  ResultType: 0
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/BloodHoundAD/AzureHound

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/signin_logs/azure_ad_azurehound_discovery.yml)
