---
sigma_id: "b5aa7d60-c17e-4538-97de-09029d6cd76b"
title: "Suspicious Digital Signature Of AppX Package"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxpackaging_om/win_appxpackaging_om_sups_appx_signature.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxpackaging_om/win_appxpackaging_om_sups_appx_signature.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / appxpackaging-om"
aliases:
  - "b5aa7d60-c17e-4538-97de-09029d6cd76b"
  - "Suspicious Digital Signature Of AppX Package"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Digital Signature Of AppX Package

Detects execution of AppX packages with known suspicious or malicious signature

## Metadata

- Rule ID: b5aa7d60-c17e-4538-97de-09029d6cd76b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-16
- Source Path: rules/windows/builtin/appxpackaging_om/win_appxpackaging_om_sups_appx_signature.yml

## Logsource

- product: windows
- service: appxpackaging-om

## Detection

```yaml
selection:
  EventID: 157
  subjectName: CN=Foresee Consulting Inc., O=Foresee Consulting Inc., L=North York,
    S=Ontario, C=CA, SERIALNUMBER=1004913-1, OID.1.3.6.1.4.1.311.60.2.1.3=CA, OID.2.5.4.15=Private
    Organization
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research
- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxpackaging_om/win_appxpackaging_om_sups_appx_signature.yml)
