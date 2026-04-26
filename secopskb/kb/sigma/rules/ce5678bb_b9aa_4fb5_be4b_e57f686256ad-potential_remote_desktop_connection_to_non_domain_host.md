---
sigma_id: "ce5678bb-b9aa-4fb5-be4b-e57f686256ad"
title: "Potential Remote Desktop Connection to Non-Domain Host"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/ntlm/win_susp_ntlm_rdp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ntlm/win_susp_ntlm_rdp.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / ntlm"
aliases:
  - "ce5678bb-b9aa-4fb5-be4b-e57f686256ad"
  - "Potential Remote Desktop Connection to Non-Domain Host"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Remote Desktop Connection to Non-Domain Host

Detects logons using NTLM to hosts that are potentially not part of the domain.

## Metadata

- Rule ID: ce5678bb-b9aa-4fb5-be4b-e57f686256ad
- Status: test
- Level: medium
- Author: James Pemberton
- Date: 2020-05-22
- Modified: 2021-11-27
- Source Path: rules/windows/builtin/ntlm/win_susp_ntlm_rdp.yml

## Logsource

- definition: Requires events from Microsoft-Windows-NTLM/Operational
- product: windows
- service: ntlm

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  EventID: 8001
  TargetName|startswith: TERMSRV
condition: selection
```

## False Positives

- Host connections to valid domains, exclude these.
- Host connections not using host FQDN.
- Host connections to external legitimate domains.

## References

- n/a

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ntlm/win_susp_ntlm_rdp.yml)
