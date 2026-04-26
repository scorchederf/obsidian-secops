---
sigma_id: "aa7a3fce-bef5-4311-9cc1-5f04bb8c308c"
title: "Certificate Exported Via PowerShell - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_export_certificate.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_export_certificate.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "aa7a3fce-bef5-4311-9cc1-5f04bb8c308c"
  - "Certificate Exported Via PowerShell - ScriptBlock"
attack_technique_ids:
  - "T1552.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Certificate Exported Via PowerShell - ScriptBlock

Detects calls to cmdlets inside of PowerShell scripts that are used to export certificates from the local certificate store. Threat actors were seen abusing this to steal private keys from compromised machines.

## Metadata

- Rule ID: aa7a3fce-bef5-4311-9cc1-5f04bb8c308c
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2021-04-23
- Modified: 2023-05-18
- Source Path: rules/windows/powershell/powershell_script/posh_ps_export_certificate.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - Export-PfxCertificate
  - Export-Certificate
filter_optional_module_export:
  ScriptBlockText|contains: CmdletsToExport = @(
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Legitimate certificate exports by administrators. Additional filters might be required.

## References

- https://us-cert.cisa.gov/ncas/analysis-reports/ar21-112a
- https://learn.microsoft.com/en-us/powershell/module/pki/export-pfxcertificate?view=windowsserver2022-ps
- https://www.splunk.com/en_us/blog/security/breaking-the-chain-defending-against-certificate-services-abuse.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_export_certificate.yml)
