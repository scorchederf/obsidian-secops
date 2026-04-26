---
sigma_id: "d67572a0-e2ec-45d6-b8db-c100d14b8ef2"
title: "NetNTLM Downgrade Attack - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_net_ntlm_downgrade.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_net_ntlm_downgrade.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "d67572a0-e2ec-45d6-b8db-c100d14b8ef2"
  - "NetNTLM Downgrade Attack - Registry"
attack_technique_ids:
  - "T1562.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# NetNTLM Downgrade Attack - Registry

Detects NetNTLM downgrade attack

## Metadata

- Rule ID: d67572a0-e2ec-45d6-b8db-c100d14b8ef2
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), wagga, Nasreddine Bencherchali (Splunk STRT)
- Date: 2018-03-20
- Modified: 2024-12-03
- Source Path: rules/windows/registry/registry_event/registry_event_net_ntlm_downgrade.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_regkey:
  TargetObject|contains|all:
  - SYSTEM\
  - ControlSet
  - \Control\Lsa
selection_value_lmcompatibilitylevel:
  TargetObject|endswith: \lmcompatibilitylevel
  Details:
  - DWORD (0x00000000)
  - DWORD (0x00000001)
  - DWORD (0x00000002)
selection_value_ntlmminclientsec:
  TargetObject|endswith: \NtlmMinClientSec
  Details:
  - DWORD (0x00000000)
  - DWORD (0x00000010)
  - DWORD (0x00000020)
  - DWORD (0x00000030)
selection_value_restrictsendingntlmtraffic:
  TargetObject|endswith: \RestrictSendingNTLMTraffic
condition: selection_regkey and 1 of selection_value_*
```

## False Positives

- Services or tools that set the values to more restrictive values

## References

- https://web.archive.org/web/20171113231705/https://www.optiv.com/blog/post-exploitation-using-netntlm-downgrade-attacks
- https://www.ultimatewindowssecurity.com/wiki/page.aspx?spid=NSrpcservers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_net_ntlm_downgrade.yml)
