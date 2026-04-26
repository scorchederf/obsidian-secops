---
sigma_id: "6f7e1c10-2dc9-4312-adb6-9574ff09a5c8"
title: "Cisco Duo Successful MFA Authentication Via Bypass Code"
framework: "sigma"
generated: "true"
source_path: "rules/identity/cisco_duo/cisco_duo_mfa_bypass_via_bypass_code.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/identity/cisco_duo/cisco_duo_mfa_bypass_via_bypass_code.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "cisco / duo"
aliases:
  - "6f7e1c10-2dc9-4312-adb6-9574ff09a5c8"
  - "Cisco Duo Successful MFA Authentication Via Bypass Code"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco Duo Successful MFA Authentication Via Bypass Code

Detects when a successful MFA authentication occurs due to the use of a bypass code.
A bypass code is a temporary passcode created by an administrator for a specific user to access a Duo-protected application. These are generally used as "backup codes," so that enrolled users who are having problems with their mobile devices (e.g., mobile service is disrupted, the device is lost or stolen, etc.) or who temporarily can't use their enrolled devices (on a plane without mobile data services) can still access their Duo-protected systems.

## Metadata

- Rule ID: 6f7e1c10-2dc9-4312-adb6-9574ff09a5c8
- Status: test
- Level: medium
- Author: Nikita Khalimonenkov
- Date: 2024-04-17
- Source Path: rules/identity/cisco_duo/cisco_duo_mfa_bypass_via_bypass_code.yml

## Logsource

- product: cisco
- service: duo

## Detection

```yaml
selection:
  event_type: authentication
  reason: bypass_user
condition: selection
```

## False Positives

- Legitimate user that was assigned on purpose to a bypass group

## References

- https://duo.com/docs/adminapi#logs
- https://help.duo.com/s/article/6327?language=en_US

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/identity/cisco_duo/cisco_duo_mfa_bypass_via_bypass_code.yml)
