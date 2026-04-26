---
sigma_id: "9e716b33-63b2-46da-86a4-bd3c3b9b5dfb"
title: "Certificate Exported Via PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_export_certificate.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_export_certificate.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9e716b33-63b2-46da-86a4-bd3c3b9b5dfb"
  - "Certificate Exported Via PowerShell"
attack_technique_ids:
  - "T1552.004"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Certificate Exported Via PowerShell

Detects calls to cmdlets that are used to export certificates from the local certificate store. Threat actors were seen abusing this to steal private keys from compromised machines.

## Metadata

- Rule ID: 9e716b33-63b2-46da-86a4-bd3c3b9b5dfb
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-18
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_export_certificate.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - 'Export-PfxCertificate '
  - 'Export-Certificate '
condition: selection
```

## False Positives

- Legitimate certificate exports by administrators. Additional filters might be required.

## References

- https://us-cert.cisa.gov/ncas/analysis-reports/ar21-112a
- https://learn.microsoft.com/en-us/powershell/module/pki/export-pfxcertificate?view=windowsserver2022-ps
- https://www.splunk.com/en_us/blog/security/breaking-the-chain-defending-against-certificate-services-abuse.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_export_certificate.yml)
