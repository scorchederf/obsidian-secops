---
sigma_id: "87261fb2-69d0-42fe-b9de-88c6b5f65a43"
title: "Atera Agent Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/msiinstaller/win_software_atera_rmm_agent_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_software_atera_rmm_agent_install.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / application"
aliases:
  - "87261fb2-69d0-42fe-b9de-88c6b5f65a43"
  - "Atera Agent Installation"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Atera Agent Installation

Detects successful installation of Atera Remote Monitoring & Management (RMM) agent as recently found to be used by Conti operators

## Metadata

- Rule ID: 87261fb2-69d0-42fe-b9de-88c6b5f65a43
- Status: test
- Level: high
- Author: Bhabesh Raj
- Date: 2021-09-01
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/application/msiinstaller/win_software_atera_rmm_agent_install.yml

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  EventID: 1033
  Provider_Name: MsiInstaller
  Message|contains: AteraAgent
condition: selection
```

## False Positives

- Legitimate Atera agent installation

## References

- https://www.advintel.io/post/secret-backdoor-behind-conti-ransomware-operation-introducing-atera-agent

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_software_atera_rmm_agent_install.yml)
