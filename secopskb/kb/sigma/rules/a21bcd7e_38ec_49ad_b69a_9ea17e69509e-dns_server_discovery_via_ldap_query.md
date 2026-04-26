---
sigma_id: "a21bcd7e-38ec-49ad-b69a-9ea17e69509e"
title: "DNS Server Discovery Via LDAP Query"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_dns_server_discovery_via_ldap_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_dns_server_discovery_via_ldap_query.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "windows / dns_query"
aliases:
  - "a21bcd7e-38ec-49ad-b69a-9ea17e69509e"
  - "DNS Server Discovery Via LDAP Query"
attack_technique_ids:
  - "T1482"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Server Discovery Via LDAP Query

Detects DNS server discovery via LDAP query requests from uncommon applications

## Metadata

- Rule ID: a21bcd7e-38ec-49ad-b69a-9ea17e69509e
- Status: test
- Level: low
- Author: frack113
- Date: 2022-08-20
- Modified: 2023-09-18
- Source Path: rules/windows/dns_query/dns_query_win_dns_server_discovery_via_ldap_query.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Detection

```yaml
selection:
  QueryName|startswith: _ldap.
filter_main_generic:
  Image|contains:
  - :\Program Files\
  - :\Program Files (x86)\
  - :\Windows\
filter_main_defender:
  Image|contains: :\ProgramData\Microsoft\Windows Defender\Platform\
  Image|endswith: \MsMpEng.exe
filter_main_unknown:
  Image: <unknown process>
filter_optional_azure:
  Image|startswith: C:\WindowsAzure\GuestAgent
filter_main_null:
  Image: null
filter_optional_browsers:
  Image|endswith:
  - \chrome.exe
  - \firefox.exe
  - \opera.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Likely

## References

- https://github.com/redcanaryco/atomic-red-team/blob/980f3f83fd81f37c1ca9c02dccfd1c3d9f9d0841/atomics/T1016/T1016.md#atomic-test-9---dns-server-discovery-using-nslookup
- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/7fcdce70-5205-44d6-9c3a-260e616a2f04

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_dns_server_discovery_via_ldap_query.yml)
