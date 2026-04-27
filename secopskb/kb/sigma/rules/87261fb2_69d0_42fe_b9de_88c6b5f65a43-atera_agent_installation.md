---
sigma_id: "87261fb2-69d0-42fe-b9de-88c6b5f65a43"
title: "Atera Agent Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/msiinstaller/win_software_atera_rmm_agent_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/msiinstaller/win_software_atera_rmm_agent_install.yml"
build_date: "2026-04-27 19:13:50"
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

Detects successful installation of Atera Remote Monitoring & Management (RMM) agent as recently found to be used by Conti operators

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools#^t1219002-remote-desktop-software|T1219.002: Remote Desktop Software]]

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
