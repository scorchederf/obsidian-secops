---
sigma_id: "33efc23c-6ea2-4503-8cfe-bdf82ce8f705"
title: "Potential Persistence Via New AMSI Providers - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_amsi_providers.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_amsi_providers.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "33efc23c-6ea2-4503-8cfe-bdf82ce8f705"
  - "Potential Persistence Via New AMSI Providers - Registry"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via New AMSI Providers - Registry

Detects when an attacker adds a new AMSI provider via the Windows Registry to bypass AMSI (Antimalware Scan Interface) protections.
Attackers may add custom AMSI providers to persist on the system and evade detection by security software that relies on AMSI for scanning scripts and other content.
This technique is often used in conjunction with fileless malware and script-based attacks to maintain persistence while avoiding detection.

## Metadata

- Rule ID: 33efc23c-6ea2-4503-8cfe-bdf82ce8f705
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2025-10-26
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_amsi_providers.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains:
  - \SOFTWARE\Microsoft\AMSI\Providers\
  - \SOFTWARE\WOW6432Node\Microsoft\AMSI\Providers\
filter_optional_avast:
  Image:
  - C:\Program Files\Avast Software\Avast\RegSvr.exe
  - C:\Program Files\Avast Software\Avast\x86\RegSvr.exe
  TargetObject|contains: \{FB904E4E-D2C7-4C8D-8492-B620BB9896B1}
filter_optional_avg:
  Image:
  - C:\Program Files\AVG\Antivirus\RegSvr.exe
  - C:\Program Files\AVG\Antivirus\x86\RegSvr.exe
  TargetObject|contains: \{FB904E4E-D2C7-4C8D-8492-B620BB9896B1}
filter_optional_avira:
  Image: C:\Program Files\Avira\Endpoint Protection SDK\endpointprotection.exe
  TargetObject|contains: \{00000001-3DCC-4B48-A82E-E2071FE58E05}
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Legitimate security products adding their own AMSI providers. Filter these according to your environment.

## References

- https://persistence-info.github.io/Data/amsi.html
- https://github.com/gtworek/PSBits/blob/8d767892f3b17eefa4d0668f5d2df78e844f01d8/FakeAMSI/FakeAMSI.c

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_amsi_providers.yml)
