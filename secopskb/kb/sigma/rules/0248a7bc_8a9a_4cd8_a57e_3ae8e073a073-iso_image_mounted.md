---
sigma_id: "0248a7bc-8a9a-4cd8-a57e-3ae8e073a073"
title: "ISO Image Mounted"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_iso_mount.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_iso_mount.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "0248a7bc-8a9a-4cd8-a57e-3ae8e073a073"
  - "ISO Image Mounted"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ISO Image Mounted

Detects the mount of an ISO image on an endpoint

## Metadata

- Rule ID: 0248a7bc-8a9a-4cd8-a57e-3ae8e073a073
- Status: test
- Level: medium
- Author: Syed Hasan (@syedhasan009)
- Date: 2021-05-29
- Modified: 2023-11-09
- Source Path: rules/windows/builtin/security/win_security_iso_mount.yml

## Logsource

- definition: The advanced audit policy setting "Object Access > Audit Removable Storage" must be configured for Success/Failure
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection:
  EventID: 4663
  ObjectServer: Security
  ObjectType: File
  ObjectName|startswith: \Device\CdRom
filter_main_generic:
  ObjectName:
  - \Device\CdRom0\autorun.ico
  - \Device\CdRom0\setup.exe
  - \Device\CdRom0\setup64.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Software installation ISO files

## References

- https://www.trendmicro.com/vinfo/hk-en/security/news/cybercrime-and-digital-threats/malicious-spam-campaign-uses-iso-image-files-to-deliver-lokibot-and-nanocore
- https://www.proofpoint.com/us/blog/threat-insight/threat-actor-profile-ta2719-uses-colorful-lures-deliver-rats-local-languages
- https://twitter.com/MsftSecIntel/status/1257324139515269121
- https://github.com/redcanaryco/atomic-red-team/blob/0f229c0e42bfe7ca736a14023836d65baa941ed2/atomics/T1553.005/T1553.005.md#atomic-test-1---mount-iso-image

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_iso_mount.yml)
