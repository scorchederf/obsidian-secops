---
sigma_id: "5a2b21ee-6aaa-4234-ac9d-59a59edf90a1"
title: "Persistence Via New SIP Provider"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_sip_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_sip_persistence.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "5a2b21ee-6aaa-4234-ac9d-59a59edf90a1"
  - "Persistence Via New SIP Provider"
attack_technique_ids:
  - "T1553.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Persistence Via New SIP Provider

Detects when an attacker register a new SIP provider for persistence and defense evasion

## Metadata

- Rule ID: 5a2b21ee-6aaa-4234-ac9d-59a59edf90a1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_sip_persistence.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.003]]

## Detection

```yaml
selection_root:
  TargetObject|contains:
  - \SOFTWARE\Microsoft\Cryptography\Providers\
  - \SOFTWARE\Microsoft\Cryptography\OID\EncodingType
  - \SOFTWARE\WOW6432Node\Microsoft\Cryptography\Providers\
  - \SOFTWARE\WOW6432Node\Microsoft\Cryptography\OID\EncodingType
selection_dll:
  TargetObject|contains:
  - \Dll
  - \$DLL
filter:
  Details:
  - WINTRUST.DLL
  - mso.dll
filter_poqexec:
  Image: C:\Windows\System32\poqexec.exe
  TargetObject|contains: \CryptSIPDll
  Details: C:\Windows\System32\PsfSip.dll
condition: all of selection_* and not 1 of filter*
```

## False Positives

- Legitimate SIP being registered by the OS or different software.

## References

- https://persistence-info.github.io/Data/codesigning.html
- https://github.com/gtworek/PSBits/tree/master/SIP
- https://specterops.io/assets/resources/SpecterOps_Subverting_Trust_in_Windows.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_sip_persistence.yml)
