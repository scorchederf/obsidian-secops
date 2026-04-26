---
sigma_id: "234dc5df-40b5-49d1-bf53-0d44ce778eca"
title: "Payload Decoded and Decrypted via Built-in Utilities"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_payload_decoded_and_decrypted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_payload_decoded_and_decrypted.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "234dc5df-40b5-49d1-bf53-0d44ce778eca"
  - "Payload Decoded and Decrypted via Built-in Utilities"
attack_technique_ids:
  - "T1059"
  - "T1204"
  - "T1140"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Payload Decoded and Decrypted via Built-in Utilities

Detects when a built-in utility is used to decode and decrypt a payload after a macOS disk image (DMG) is executed. Malware authors may attempt to evade detection and trick users into executing malicious code by encoding and encrypting their payload and placing it in a disk image file. This behavior is consistent with adware or malware families such as Bundlore and Shlayer.

## Metadata

- Rule ID: 234dc5df-40b5-49d1-bf53-0d44ce778eca
- Status: test
- Level: medium
- Author: Tim Rauch (rule), Elastic (idea)
- Date: 2022-10-17
- Source Path: rules/macos/process_creation/proc_creation_macos_payload_decoded_and_decrypted.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1204-user_execution|T1204]]
- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

### Software Tags

- S0482
- S0402

## Detection

```yaml
selection:
  Image|endswith: /openssl
  CommandLine|contains|all:
  - /Volumes/
  - enc
  - -base64
  - ' -d '
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/elastic/protections-artifacts/commit/746086721fd385d9f5c6647cada1788db4aea95f#diff-5d42c3d772e04f1e8d0eb60f5233bc79def1ea73105a2d8822f44164f77ef823

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_payload_decoded_and_decrypted.yml)
