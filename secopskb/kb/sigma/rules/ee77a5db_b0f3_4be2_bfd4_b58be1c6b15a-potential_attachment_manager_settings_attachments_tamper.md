---
sigma_id: "ee77a5db-b0f3-4be2-bfd4-b58be1c6b15a"
title: "Potential Attachment Manager Settings Attachments Tamper"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_policies_attachments_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_policies_attachments_tamper.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "ee77a5db-b0f3-4be2-bfd4-b58be1c6b15a"
  - "Potential Attachment Manager Settings Attachments Tamper"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Attachment Manager Settings Attachments Tamper

Detects tampering with attachment manager settings policies attachments (See reference for more information)

## Metadata

- Rule ID: ee77a5db-b0f3-4be2-bfd4-b58be1c6b15a
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-01
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_policies_attachments_tamper.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection_main:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Attachments\
selection_value_hide_zone_info:
  TargetObject|endswith: \HideZoneInfoOnProperties
  Details: DWORD (0x00000001)
selection_value_save_zone_info:
  TargetObject|endswith: \SaveZoneInformation
  Details: DWORD (0x00000002)
selection_value_scan_with_av:
  TargetObject|endswith: \ScanWithAntiVirus
  Details: DWORD (0x00000001)
condition: selection_main and 1 of selection_value_*
```

## False Positives

- Unlikely

## References

- https://support.microsoft.com/en-us/topic/information-about-the-attachment-manager-in-microsoft-windows-c48a4dcd-8de5-2af5-ee9b-cd795ae42738
- https://www.virustotal.com/gui/file/2bcd5702a7565952c44075ac6fb946c7780526640d1264f692c7664c02c68465

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_policies_attachments_tamper.yml)
