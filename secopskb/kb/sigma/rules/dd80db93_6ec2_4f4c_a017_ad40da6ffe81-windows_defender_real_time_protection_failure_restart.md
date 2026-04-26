---
sigma_id: "dd80db93-6ec2-4f4c-a017-ad40da6ffe81"
title: "Windows Defender Real-Time Protection Failure/Restart"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/windefend/win_defender_real_time_protection_errors.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_real_time_protection_errors.yml"
build_date: "2026-04-26 14:14:40"
status: "stable"
level: "medium"
logsource: "windows / windefend"
aliases:
  - "dd80db93-6ec2-4f4c-a017-ad40da6ffe81"
  - "Windows Defender Real-Time Protection Failure/Restart"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Real-Time Protection Failure/Restart

Detects issues with Windows Defender Real-Time Protection features

## Metadata

- Rule ID: dd80db93-6ec2-4f4c-a017-ad40da6ffe81
- Status: stable
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Christopher Peacock '@securepeacock' (Update)
- Date: 2023-03-28
- Modified: 2023-05-05
- Source Path: rules/windows/builtin/windefend/win_defender_real_time_protection_errors.yml

## Logsource

- product: windows
- service: windefend

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  EventID:
  - 3002
  - 3007
filter_optional_network_inspection:
  Feature_Name: '%%886'
  Reason:
  - '%%892'
  - '%%858'
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Some crashes can occur sometimes and the event doesn't provide enough information to tune out these cases. Manual exception is required

## References

- Internal Research
- https://www.microsoft.com/en-us/security/blog/2023/04/11/guidance-for-investigating-attacks-using-cve-2022-21894-the-blacklotus-campaign/
- https://gist.github.com/nasbench/33732d6705cbdc712fae356f07666346

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_real_time_protection_errors.yml)
