---
sigma_id: "8b9606c9-28be-4a38-b146-0e313cc232c1"
title: "Potential Ransomware Activity Using LegalNotice Message"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_legalnotice_susp_message.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_legalnotice_susp_message.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "8b9606c9-28be-4a38-b146-0e313cc232c1"
  - "Potential Ransomware Activity Using LegalNotice Message"
attack_technique_ids:
  - "T1491.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Ransomware Activity Using LegalNotice Message

Detect changes to the "LegalNoticeCaption" or "LegalNoticeText" registry values where the message set contains keywords often used in ransomware ransom messages

## Metadata

- Rule ID: 8b9606c9-28be-4a38-b146-0e313cc232c1
- Status: test
- Level: high
- Author: frack113
- Date: 2022-12-11
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_legalnotice_susp_message.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1491-defacement|T1491.001]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LegalNoticeCaption
  - \SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LegalNoticeText
  Details|contains:
  - encrypted
  - Unlock-Password
  - paying
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/5c1e6f1b4fafd01c8d1ece85f510160fc1275fbf/atomics/T1491.001/T1491.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_legalnotice_susp_message.yml)
