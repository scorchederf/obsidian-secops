---
sigma_id: "411742ad-89b0-49cb-a7b0-3971b5c1e0a4"
title: "Locked Workstation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_workstation_was_locked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_workstation_was_locked.yml"
build_date: "2026-04-26 14:14:28"
status: "stable"
level: "informational"
logsource: "windows / security"
aliases:
  - "411742ad-89b0-49cb-a7b0-3971b5c1e0a4"
  - "Locked Workstation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Locked Workstation

Detects locked workstation session events that occur automatically after a standard period of inactivity.

## Metadata

- Rule ID: 411742ad-89b0-49cb-a7b0-3971b5c1e0a4
- Status: stable
- Level: informational
- Author: Alexandr Yampolskyi, SOC Prime
- Date: 2019-03-26
- Modified: 2023-12-11
- Source Path: rules/windows/builtin/security/win_security_workstation_was_locked.yml

## Logsource

- product: windows
- service: security

## Detection

```yaml
selection:
  EventID: 4800
condition: selection
```

## False Positives

- Likely

## References

- https://www.cisecurity.org/controls/cis-controls-list/
- https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf
- https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf
- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventID=4800

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_workstation_was_locked.yml)
