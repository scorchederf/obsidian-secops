---
sigma_id: "123e4e6d-b123-48f8-b261-7214938acaf0"
title: "Startup/Logon Script Added to Group Policy Object"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_group_policy_startup_script_added_to_gpo.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_group_policy_startup_script_added_to_gpo.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "123e4e6d-b123-48f8-b261-7214938acaf0"
  - "Startup/Logon Script Added to Group Policy Object"
attack_technique_ids:
  - "T1484.001"
  - "T1547"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Startup/Logon Script Added to Group Policy Object

Detects the modification of Group Policy Objects (GPO) to add a startup/logon script to users or computer objects.

## Metadata

- Rule ID: 123e4e6d-b123-48f8-b261-7214938acaf0
- Status: test
- Level: medium
- Author: Elastic, Josh Nickels, Marius Rothenbücher
- Date: 2024-09-06
- Source Path: rules/windows/builtin/security/win_security_susp_group_policy_startup_script_added_to_gpo.yml

## Logsource

- definition: The advanced audit policy setting "Object Access > Audit Detailed File Share" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification|T1484.001]]
- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Detection

```yaml
selection_eventid:
  EventID:
  - 5136
  - 5145
selection_attributes_main:
  AttributeLDAPDisplayName:
  - gPCMachineExtensionNames
  - gPCUserExtensionNames
  AttributeValue|contains: 42B5FAAE-6536-11D2-AE5A-0000F87571E3
selection_attributes_optional:
  AttributeValue|contains:
  - 40B6664F-4972-11D1-A7CA-0000F87571E3
  - 40B66650-4972-11D1-A7CA-0000F87571E3
selection_share:
  ShareName|endswith: \SYSVOL
  RelativeTargetName|endswith:
  - \scripts.ini
  - \psscripts.ini
  AccessList|contains: '%%4417'
condition: selection_eventid and (all of selection_attributes_* or selection_share)
```

## False Positives

- Legitimate execution by system administrators.

## References

- https://www.elastic.co/guide/en/security/current/startup-logon-script-added-to-group-policy-object.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_group_policy_startup_script_added_to_gpo.yml)
