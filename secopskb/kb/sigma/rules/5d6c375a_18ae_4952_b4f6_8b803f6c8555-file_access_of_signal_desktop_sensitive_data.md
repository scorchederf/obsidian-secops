---
sigma_id: "5d6c375a-18ae-4952-b4f6-8b803f6c8555"
title: "File Access Of Signal Desktop Sensitive Data"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_signal_sensitive_config_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_signal_sensitive_config_access.yml"
build_date: "2026-04-26 14:14:25"
status: "experimental"
level: "medium"
logsource: "windows / security"
aliases:
  - "5d6c375a-18ae-4952-b4f6-8b803f6c8555"
  - "File Access Of Signal Desktop Sensitive Data"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Access Of Signal Desktop Sensitive Data

Detects access to Signal Desktop's sensitive data files: db.sqlite and config.json.
The db.sqlite file in Signal Desktop stores all locally saved messages in an encrypted SQLite database, while the config.json contains the decryption key needed to access that data.
Since the key is stored in plain text, a threat actor who gains access to both files can decrypt and read sensitive messages without needing the users credentials.
Currently the rule only covers the default Signal installation path in AppData\Roaming. Signal Portable installations may use different paths based on user configuration. Additional paths can be added to the selection as needed.

## Metadata

- Rule ID: 5d6c375a-18ae-4952-b4f6-8b803f6c8555
- Status: experimental
- Level: medium
- Author: Andreas Braathen (mnemonic.io)
- Date: 2025-10-19
- Source Path: rules/windows/builtin/security/win_security_signal_sensitive_config_access.yml

## Logsource

- definition: Requirements: System Access Control List (SACL) policy with attributes List folder/read data on Objects
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection:
  EventID: 4663
  ObjectType: File
  ObjectName|contains: \AppData\Roaming\Signal\
  ObjectName|endswith:
  - \config.json
  - \db.sqlite
filter_main_signal:
  ProcessName|endswith:
  - \signal-portable.exe
  - \signal.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely, but possible from AV or backup software accessing the files.

## References

- https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger/
- https://vmois.dev/query-signal-desktop-messages-sqlite/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_signal_sensitive_config_access.yml)
