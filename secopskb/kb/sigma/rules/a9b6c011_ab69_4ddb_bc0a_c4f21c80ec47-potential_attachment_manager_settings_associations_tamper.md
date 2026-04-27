---
sigma_id: "a9b6c011-ab69-4ddb-bc0a-c4f21c80ec47"
title: "Potential Attachment Manager Settings Associations Tamper"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_policies_associations_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_policies_associations_tamper.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "a9b6c011-ab69-4ddb-bc0a-c4f21c80ec47"
  - "Potential Attachment Manager Settings Associations Tamper"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Attachment Manager Settings Associations Tamper

Detects tampering with attachment manager settings policies associations to lower the default file type risks (See reference for more information)

## Metadata

- Rule ID: a9b6c011-ab69-4ddb-bc0a-c4f21c80ec47
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-01
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_policies_associations_tamper.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection_main:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Associations\
selection_value_default_file_type_rsik:
  TargetObject|endswith: \DefaultFileTypeRisk
  Details: DWORD (0x00006152)
selection_value_low_risk_filetypes:
  TargetObject|endswith: \LowRiskFileTypes
  Details|contains:
  - .zip;
  - .rar;
  - .exe;
  - .bat;
  - .com;
  - .cmd;
  - .reg;
  - .msi;
  - .htm;
  - .html;
condition: selection_main and 1 of selection_value_*
```

## False Positives

- Unlikely

## References

- https://support.microsoft.com/en-us/topic/information-about-the-attachment-manager-in-microsoft-windows-c48a4dcd-8de5-2af5-ee9b-cd795ae42738
- https://www.virustotal.com/gui/file/2bcd5702a7565952c44075ac6fb946c7780526640d1264f692c7664c02c68465

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_policies_associations_tamper.yml)
