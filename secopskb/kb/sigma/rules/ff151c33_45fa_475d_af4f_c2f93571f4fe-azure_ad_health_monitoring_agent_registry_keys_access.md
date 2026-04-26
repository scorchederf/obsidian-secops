---
sigma_id: "ff151c33-45fa-475d-af4f-c2f93571f4fe"
title: "Azure AD Health Monitoring Agent Registry Keys Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_aadhealth_mon_agent_regkey_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_aadhealth_mon_agent_regkey_access.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "ff151c33-45fa-475d-af4f-c2f93571f4fe"
  - "Azure AD Health Monitoring Agent Registry Keys Access"
attack_technique_ids:
  - "T1012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure AD Health Monitoring Agent Registry Keys Access

This detection uses Windows security events to detect suspicious access attempts to the registry key of Azure AD Health monitoring agent.
This detection requires an access control entry (ACE) on the system access control list (SACL) of the following securable object HKLM\SOFTWARE\Microsoft\Microsoft Online\Reporting\MonitoringAgent.

## Metadata

- Rule ID: ff151c33-45fa-475d-af4f-c2f93571f4fe
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
- Date: 2021-08-26
- Modified: 2022-10-09
- Source Path: rules/windows/builtin/security/win_security_aadhealth_mon_agent_regkey_access.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1012-query_registry|T1012]]

## Detection

```yaml
selection:
  EventID:
  - 4656
  - 4663
  ObjectType: Key
  ObjectName: \REGISTRY\MACHINE\SOFTWARE\Microsoft\Microsoft Online\Reporting\MonitoringAgent
filter:
  ProcessName|contains:
  - Microsoft.Identity.Health.Adfs.DiagnosticsAgent.exe
  - Microsoft.Identity.Health.Adfs.InsightsService.exe
  - Microsoft.Identity.Health.Adfs.MonitoringAgent.Startup.exe
  - Microsoft.Identity.Health.Adfs.PshSurrogate.exe
  - Microsoft.Identity.Health.Common.Clients.ResourceMonitor.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://o365blog.com/post/hybridhealthagent/
- https://github.com/OTRF/Set-AuditRule/blob/c3dec5443414231714d850565d364ca73475ade5/rules/registry/aad_connect_health_monitoring_agent.yml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_aadhealth_mon_agent_regkey_access.yml)
