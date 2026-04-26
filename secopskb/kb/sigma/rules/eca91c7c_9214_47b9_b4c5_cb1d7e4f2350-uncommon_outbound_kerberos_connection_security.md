---
sigma_id: "eca91c7c-9214-47b9-b4c5-cb1d7e4f2350"
title: "Uncommon Outbound Kerberos Connection - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_outbound_kerberos_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_outbound_kerberos_connection.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "eca91c7c-9214-47b9-b4c5-cb1d7e4f2350"
  - "Uncommon Outbound Kerberos Connection - Security"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Outbound Kerberos Connection - Security

Detects uncommon outbound network activity via Kerberos default port indicating possible lateral movement or first stage PrivEsc via delegation.

## Metadata

- Rule ID: eca91c7c-9214-47b9-b4c5-cb1d7e4f2350
- Status: test
- Level: medium
- Author: Ilyas Ochkov, oscd.community
- Date: 2019-10-24
- Modified: 2024-03-15
- Source Path: rules/windows/builtin/security/win_security_susp_outbound_kerberos_connection.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection:
  EventID: 5156
  DestPort: 88
filter_main_lsass:
  Application|startswith:
  - \device\harddiskvolume
  - 'C:'
  Application|endswith: \Windows\System32\lsass.exe
filter_optional_chrome:
  Application|startswith:
  - \device\harddiskvolume
  - 'C:'
  Application|endswith:
  - \Program Files (x86)\Google\Chrome\Application\chrome.exe
  - \Program Files\Google\Chrome\Application\chrome.exe
filter_optional_firefox:
  Application|startswith:
  - \device\harddiskvolume
  - 'C:'
  Application|endswith:
  - \Program Files (x86)\Mozilla Firefox\firefox.exe
  - \Program Files\Mozilla Firefox\firefox.exe
filter_optional_tomcat:
  Application|endswith: \tomcat\bin\tomcat8.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Web Browsers and third party application might generate similar activity. An initial baseline is required.

## References

- https://github.com/GhostPack/Rubeus

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_outbound_kerberos_connection.yml)
