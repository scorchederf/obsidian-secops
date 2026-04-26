---
sigma_id: "fbc5e92f-3044-4e73-a5c6-1c4359b539de"
title: "PowerShell Script With File Hostname Resolving Capabilities"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_resolve_list_of_ip_from_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_resolve_list_of_ip_from_file.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "fbc5e92f-3044-4e73-a5c6-1c4359b539de"
  - "PowerShell Script With File Hostname Resolving Capabilities"
attack_technique_ids:
  - "T1020"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Script With File Hostname Resolving Capabilities

Detects PowerShell scripts that have capabilities to read files, loop through them and resolve DNS host entries.

## Metadata

- Rule ID: fbc5e92f-3044-4e73-a5c6-1c4359b539de
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-05
- Source Path: rules/windows/powershell/powershell_script/posh_ps_resolve_list_of_ip_from_file.yml

## Logsource

- category: ps_script
- definition: bade5735-5ab0-4aa7-a642-a11be0e40872
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1020-automated_exfiltration|T1020]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - 'Get-content '
  - foreach
  - '[System.Net.Dns]::GetHostEntry'
  - Out-File
condition: selection
```

## False Positives

- The same functionality can be implemented by admin scripts, correlate with name and creator

## References

- https://www.fortypoundhead.com/showcontent.asp?artid=24022
- https://labs.withsecure.com/publications/fin7-target-veeam-servers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_resolve_list_of_ip_from_file.yml)
