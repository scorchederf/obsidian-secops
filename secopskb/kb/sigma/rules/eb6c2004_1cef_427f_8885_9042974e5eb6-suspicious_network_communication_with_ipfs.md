---
sigma_id: "eb6c2004-1cef-427f-8885-9042974e5eb6"
title: "Suspicious Network Communication With IPFS"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_susp_ipfs_cred_harvest.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_susp_ipfs_cred_harvest.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "proxy"
aliases:
  - "eb6c2004-1cef-427f-8885-9042974e5eb6"
  - "Suspicious Network Communication With IPFS"
attack_technique_ids:
  - "T1056"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Network Communication With IPFS

Detects connections to interplanetary file system (IPFS) containing a user's email address which mirrors behaviours observed in recent phishing campaigns leveraging IPFS to host credential harvesting webpages.

## Metadata

- Rule ID: eb6c2004-1cef-427f-8885-9042974e5eb6
- Status: test
- Level: low
- Author: Gavin Knapp
- Date: 2023-03-16
- Source Path: rules/web/proxy_generic/proxy_susp_ipfs_cred_harvest.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1056-input_capture|T1056]]

## Detection

```yaml
selection:
  cs-uri|re: (?i)(ipfs\.io/|ipfs\.io\s).+\..+@.+\.[a-z]+
condition: selection
```

## False Positives

- Legitimate use of IPFS being used in the organisation. However the cs-uri regex looking for a user email will likely negate this.

## References

- https://blog.talosintelligence.com/ipfs-abuse/
- https://github.com/Cisco-Talos/IOCs/tree/80caca039988252fbb3f27a2e89c2f2917f582e0/2022/11
- https://isc.sans.edu/diary/IPFS%20phishing%20and%20the%20need%20for%20correctly%20set%20HTTP%20security%20headers/29638

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_susp_ipfs_cred_harvest.yml)
