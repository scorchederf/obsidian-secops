---
sigma_id: "470ec5fa-7b4e-4071-b200-4c753100f49b"
title: "Failed Code Integrity Checks"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_codeintegrity_check_failure.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_codeintegrity_check_failure.yml"
build_date: "2026-04-26 14:14:25"
status: "stable"
level: "informational"
logsource: "windows / security"
aliases:
  - "470ec5fa-7b4e-4071-b200-4c753100f49b"
  - "Failed Code Integrity Checks"
attack_technique_ids:
  - "T1027.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Failed Code Integrity Checks

Detects code integrity failures such as missing page hashes or corrupted drivers due unauthorized modification. This could be a sign of tampered binaries.

## Metadata

- Rule ID: 470ec5fa-7b4e-4071-b200-4c753100f49b
- Status: stable
- Level: informational
- Author: Thomas Patzke
- Date: 2019-12-03
- Modified: 2025-01-19
- Source Path: rules/windows/builtin/security/win_security_codeintegrity_check_failure.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.001]]

## Detection

```yaml
selection:
  EventID:
  - 5038
  - 6281
filter_optional_crowdstrike:
  param1|contains:
  - \CSFalconServiceUninstallTool_
  - \Program Files\CrowdStrike\
  - \System32\drivers\CrowdStrike\
  - \Windows\System32\ScriptControl64_
filter_optional_sophos:
  param1|contains: \Program Files\Sophos\
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Disk device errors

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-5038
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-6281

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_codeintegrity_check_failure.yml)
