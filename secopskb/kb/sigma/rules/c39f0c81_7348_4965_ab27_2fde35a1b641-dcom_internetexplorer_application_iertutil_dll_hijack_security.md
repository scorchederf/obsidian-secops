---
sigma_id: "c39f0c81-7348-4965-ab27-2fde35a1b641"
title: "DCOM InternetExplorer.Application Iertutil DLL Hijack - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_dcom_iertutil_dll_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dcom_iertutil_dll_hijack.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "c39f0c81-7348-4965-ab27-2fde35a1b641"
  - "DCOM InternetExplorer.Application Iertutil DLL Hijack - Security"
attack_technique_ids:
  - "T1021.002"
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DCOM InternetExplorer.Application Iertutil DLL Hijack - Security

Detects a threat actor creating a file named `iertutil.dll` in the `C:\Program Files\Internet Explorer\` directory over the network for a DCOM InternetExplorer DLL Hijack scenario.

## Metadata

- Rule ID: c39f0c81-7348-4965-ab27-2fde35a1b641
- Status: test
- Level: high
- Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR)
- Date: 2020-10-12
- Modified: 2022-11-26
- Source Path: rules/windows/builtin/security/win_security_dcom_iertutil_dll_hijack.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Detection

```yaml
selection:
  EventID: 5145
  RelativeTargetName|endswith: \Internet Explorer\iertutil.dll
filter:
  SubjectUserName|endswith: $
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/201009-RemoteDCOMIErtUtilDLLHijack/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_dcom_iertutil_dll_hijack.yml)
