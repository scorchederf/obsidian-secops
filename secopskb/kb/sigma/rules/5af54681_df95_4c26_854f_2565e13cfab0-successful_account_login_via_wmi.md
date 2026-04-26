---
sigma_id: "5af54681-df95-4c26-854f-2565e13cfab0"
title: "Successful Account Login Via WMI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/account_management/win_security_susp_wmi_login.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_wmi_login.yml"
build_date: "2026-04-26 14:14:35"
status: "stable"
level: "low"
logsource: "windows / security"
aliases:
  - "5af54681-df95-4c26-854f-2565e13cfab0"
  - "Successful Account Login Via WMI"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Successful Account Login Via WMI

Detects successful logon attempts performed with WMI

## Metadata

- Rule ID: 5af54681-df95-4c26-854f-2565e13cfab0
- Status: stable
- Level: low
- Author: Thomas Patzke
- Date: 2019-12-04
- Modified: 2024-01-17
- Source Path: rules/windows/builtin/security/account_management/win_security_susp_wmi_login.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection:
  EventID: 4624
  ProcessName|endswith: \WmiPrvSE.exe
condition: selection
```

## False Positives

- Monitoring tools
- Legitimate system administration

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/account_management/win_security_susp_wmi_login.yml)
