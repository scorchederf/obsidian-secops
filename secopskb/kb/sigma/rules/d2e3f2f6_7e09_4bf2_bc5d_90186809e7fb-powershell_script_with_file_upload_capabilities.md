---
sigma_id: "d2e3f2f6-7e09-4bf2-bc5d-90186809e7fb"
title: "PowerShell Script With File Upload Capabilities"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_script_with_upload_capabilities.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_script_with_upload_capabilities.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "d2e3f2f6-7e09-4bf2-bc5d-90186809e7fb"
  - "PowerShell Script With File Upload Capabilities"
attack_technique_ids:
  - "T1020"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Script With File Upload Capabilities

Detects PowerShell scripts leveraging the "Invoke-WebRequest" cmdlet to send data via either "PUT" or "POST" method.

## Metadata

- Rule ID: d2e3f2f6-7e09-4bf2-bc5d-90186809e7fb
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-07
- Modified: 2025-07-18
- Source Path: rules/windows/powershell/powershell_script/posh_ps_script_with_upload_capabilities.yml

## Logsource

- category: ps_script
- definition: bade5735-5ab0-4aa7-a642-a11be0e40872
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1020-automated_exfiltration|T1020]]

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains:
  - Invoke-RestMethod
  - Invoke-WebRequest
  - 'irm '
  - 'iwr '
selection_flag:
  ScriptBlockText|contains:
  - -Method "POST"
  - -Method "PUT"
  - -Method POST
  - -Method PUT
  - -Method 'POST'
  - -Method 'PUT'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1020/T1020.md
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.4

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_script_with_upload_capabilities.yml)
