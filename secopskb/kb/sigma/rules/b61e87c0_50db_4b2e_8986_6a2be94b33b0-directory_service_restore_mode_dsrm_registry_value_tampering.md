---
sigma_id: "b61e87c0-50db-4b2e-8986-6a2be94b33b0"
title: "Directory Service Restore Mode(DSRM) Registry Value Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_dsrm_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dsrm_tampering.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "b61e87c0-50db-4b2e-8986-6a2be94b33b0"
  - "Directory Service Restore Mode(DSRM) Registry Value Tampering"
attack_technique_ids:
  - "T1556"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Directory Service Restore Mode(DSRM) Registry Value Tampering

Detects changes to "DsrmAdminLogonBehavior" registry value.
During a Domain Controller (DC) promotion, administrators create a Directory Services Restore Mode (DSRM) local administrator account with a password that rarely changes. The DSRM account is an “Administrator” account that logs in with the DSRM mode when the server is booting up to restore AD backups or recover the server from a failure.
Attackers could abuse DSRM account to maintain their persistence and access to the organization's Active Directory.
If the "DsrmAdminLogonBehavior" value is set to "0", the administrator account can only be used if the DC starts in DSRM.
If the "DsrmAdminLogonBehavior" value is set to "1", the administrator account can only be used if the local AD DS service is stopped.
If the "DsrmAdminLogonBehavior" value is set to "2", the administrator account can always be used.

## Metadata

- Rule ID: b61e87c0-50db-4b2e-8986-6a2be94b33b0
- Status: test
- Level: high
- Author: Nischal Khadgi
- Date: 2024-07-11
- Source Path: rules/windows/registry/registry_set/registry_set_dsrm_tampering.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Control\Lsa\DsrmAdminLogonBehavior
filter_main_default_value:
  Details: DWORD (0x00000000)
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://adsecurity.org/?p=1785
- https://www.sentinelone.com/blog/detecting-dsrm-account-misconfigurations/
- https://book.hacktricks.xyz/windows-hardening/active-directory-methodology/dsrm-credentials

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dsrm_tampering.yml)
