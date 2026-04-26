---
sigma_id: "fc028194-969d-4122-8abe-0470d5b8f12f"
title: "Access to Browser Login Data"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_access_to_browser_login_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_access_to_browser_login_data.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "fc028194-969d-4122-8abe-0470d5b8f12f"
  - "Access to Browser Login Data"
attack_technique_ids:
  - "T1555.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Access to Browser Login Data

Adversaries may acquire credentials from web browsers by reading files specific to the target browser.
Web browsers commonly save credentials such as website usernames and passwords so that they do not need to be entered manually in the future.
Web browsers typically store the credentials in an encrypted format within a credential store.

## Metadata

- Rule ID: fc028194-969d-4122-8abe-0470d5b8f12f
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-30
- Source Path: rules/windows/powershell/powershell_script/posh_ps_access_to_browser_login_data.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Detection

```yaml
selection_cmd:
  ScriptBlockText|contains|all:
  - Copy-Item
  - -Destination
selection_path:
  ScriptBlockText|contains:
  - \Opera Software\Opera Stable\Login Data
  - \Mozilla\Firefox\Profiles
  - \Microsoft\Edge\User Data\Default
  - \Google\Chrome\User Data\Default\Login Data
  - \Google\Chrome\User Data\Default\Login Data For Account
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555.003/T1555.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_access_to_browser_login_data.yml)
