---
sigma_id: "1f1d8209-636e-4c6c-a137-781cca8b82f9"
title: "WFP Filter Added via Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_wfp_filter_added.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_wfp_filter_added.yml"
build_date: "2026-04-26 14:14:39"
status: "experimental"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "1f1d8209-636e-4c6c-a137-781cca8b82f9"
  - "WFP Filter Added via Registry"
attack_technique_ids:
  - "T1562"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WFP Filter Added via Registry

Detects registry modifications that add Windows Filtering Platform (WFP) filters, which may be used to block security tools and EDR agents from reporting events.

## Metadata

- Rule ID: 1f1d8209-636e-4c6c-a137-781cca8b82f9
- Status: experimental
- Level: medium
- Author: Frack113
- Date: 2025-10-23
- Source Path: rules/windows/registry/registry_set/registry_set_susp_wfp_filter_added.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \BFE\Parameters\Policy\Persistent\Filter\
filter_main_svchost:
  Image:
  - C:\Windows\System32\svchost.exe
  - C:\Windows\SysWOW64\svchost.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/netero1010/EDRSilencer/blob/0e73a7037ec65c52894d8208e6f605a7da0a34a6/EDRSilencer.c
- https://www.huntress.com/blog/silencing-the-edr-silencers
- https://www.trendmicro.com/en_us/research/24/j/edrsilencer-disrupting-endpoint-security-solutions.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_wfp_filter_added.yml)
