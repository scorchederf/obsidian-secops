---
sigma_id: "b120b587-a4c2-4b94-875d-99c9807d6955"
title: "Credentials from Password Stores - Keychain"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_creds_from_keychain.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_creds_from_keychain.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "b120b587-a4c2-4b94-875d-99c9807d6955"
  - "Credentials from Password Stores - Keychain"
attack_technique_ids:
  - "T1555.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Credentials from Password Stores - Keychain

Detects passwords dumps from Keychain

## Metadata

- Rule ID: b120b587-a4c2-4b94-875d-99c9807d6955
- Status: test
- Level: medium
- Author: Tim Ismilyaev, oscd.community, Florian Roth (Nextron Systems)
- Date: 2020-10-19
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_creds_from_keychain.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.001]]

## Detection

```yaml
selection1:
  Image: /usr/bin/security
  CommandLine|contains:
  - find-certificate
  - ' export '
selection2:
  CommandLine|contains:
  - ' dump-keychain '
  - ' login-keychain '
condition: 1 of selection*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1555.001/T1555.001.md
- https://gist.github.com/Capybara/6228955

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_creds_from_keychain.yml)
