---
sigma_id: "982e9f2d-1a85-4d5b-aea4-31f5e97c6555"
title: "Suspicious WebDav Client Execution Via Rundll32.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_webdav_client_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_webdav_client_susp_execution.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "982e9f2d-1a85-4d5b-aea4-31f5e97c6555"
  - "Suspicious WebDav Client Execution Via Rundll32.EXE"
attack_technique_ids:
  - "T1048.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious WebDav Client Execution Via Rundll32.EXE

Detects "svchost.exe" spawning "rundll32.exe" with command arguments like C:\windows\system32\davclnt.dll,DavSetCookie. This could be an indicator of exfiltration or use of WebDav to launch code (hosted on WebDav Server) or potentially a sign of exploitation of CVE-2023-23397

## Metadata

- Rule ID: 982e9f2d-1a85-4d5b-aea4-31f5e97c6555
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Florian Roth (Nextron Systems)
- Date: 2023-03-16
- Modified: 2023-09-18
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_webdav_client_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Detection

```yaml
selection:
  ParentImage|endswith: \svchost.exe
  ParentCommandLine|contains: -s WebClient
  Image|endswith: \rundll32.exe
  CommandLine|contains: C:\windows\system32\davclnt.dll,DavSetCookie
  CommandLine|re: ://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
filter_local_ips:
  CommandLine|contains:
  - ://10.
  - ://192.168.
  - ://172.16.
  - ://172.17.
  - ://172.18.
  - ://172.19.
  - ://172.20.
  - ://172.21.
  - ://172.22.
  - ://172.23.
  - ://172.24.
  - ://172.25.
  - ://172.26.
  - ://172.27.
  - ://172.28.
  - ://172.29.
  - ://172.30.
  - ://172.31.
  - ://127.
  - ://169.254.
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://twitter.com/aceresponder/status/1636116096506818562
- https://www.mdsec.co.uk/2023/03/exploiting-cve-2023-23397-microsoft-outlook-elevation-of-privilege-vulnerability/
- https://www.pwndefend.com/2023/03/15/the-long-game-persistent-hash-theft/
- https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/03/Figure-7-sample-webdav-process-create-event.png
- https://www.microsoft.com/en-us/security/blog/2023/03/24/guidance-for-investigating-attacks-using-cve-2023-23397/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_webdav_client_susp_execution.yml)
