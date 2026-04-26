---
sigma_id: "fadb84f0-4e84-4f6d-a1ce-9ef2bffb6ccd"
title: "Cloudflared Portable Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cloudflared_portable_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cloudflared_portable_execution.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "fadb84f0-4e84-4f6d-a1ce-9ef2bffb6ccd"
  - "Cloudflared Portable Execution"
attack_technique_ids:
  - "T1090.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cloudflared Portable Execution

Detects the execution of the "cloudflared" binary from a non standard location.

## Metadata

- Rule ID: fadb84f0-4e84-4f6d-a1ce-9ef2bffb6ccd
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-12-20
- Source Path: rules/windows/process_creation/proc_creation_win_cloudflared_portable_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090.001]]

## Detection

```yaml
selection:
  Image|endswith: \cloudflared.exe
filter_main_admin_location:
  Image|contains:
  - :\Program Files (x86)\cloudflared\
  - :\Program Files\cloudflared\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate usage of Cloudflared portable versions

## References

- https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/trycloudflare/
- https://github.com/cloudflare/cloudflared
- https://www.intrinsec.com/akira_ransomware/
- https://www.guidepointsecurity.com/blog/tunnel-vision-cloudflared-abused-in-the-wild/
- https://github.com/cloudflare/cloudflared/releases

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cloudflared_portable_execution.yml)
