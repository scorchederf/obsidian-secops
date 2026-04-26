---
sigma_id: "04b45a8a-d11d-49e4-9acc-4a1b524407a5"
title: "DNS-over-HTTPS Enabled by Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_dns_over_https_enabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dns_over_https_enabled.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "04b45a8a-d11d-49e4-9acc-4a1b524407a5"
  - "DNS-over-HTTPS Enabled by Registry"
attack_technique_ids:
  - "T1140"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS-over-HTTPS Enabled by Registry

Detects when a user enables DNS-over-HTTPS.
This can be used to hide internet activity or be used to hide the process of exfiltrating data.
With this enabled organization will lose visibility into data such as query type, response and originating IP that are used to determine bad actors.

## Metadata

- Rule ID: 04b45a8a-d11d-49e4-9acc-4a1b524407a5
- Status: test
- Level: medium
- Author: Austin Songer
- Date: 2021-07-22
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_dns_over_https_enabled.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_edge:
  TargetObject|endswith: \SOFTWARE\Policies\Microsoft\Edge\BuiltInDnsClientEnabled
  Details: DWORD (0x00000001)
selection_chrome:
  TargetObject|endswith: \SOFTWARE\Google\Chrome\DnsOverHttpsMode
  Details: secure
selection_firefox:
  TargetObject|endswith: \SOFTWARE\Policies\Mozilla\Firefox\DNSOverHTTPS\Enabled
  Details: DWORD (0x00000001)
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://www.tenforums.com/tutorials/151318-how-enable-disable-dns-over-https-doh-microsoft-edge.html
- https://github.com/elastic/detection-rules/issues/1371
- https://chromeenterprise.google/policies/?policy=DnsOverHttpsMode
- https://admx.help/HKLM/Software/Policies/Mozilla/Firefox/DNSOverHTTPS

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dns_over_https_enabled.yml)
