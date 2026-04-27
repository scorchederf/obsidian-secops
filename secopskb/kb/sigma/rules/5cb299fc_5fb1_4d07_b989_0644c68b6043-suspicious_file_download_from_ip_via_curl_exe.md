---
sigma_id: "5cb299fc-5fb1-4d07-b989-0644c68b6043"
title: "Suspicious File Download From IP Via Curl.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_curl_download_direct_ip_susp_extensions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_download_direct_ip_susp_extensions.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5cb299fc-5fb1-4d07-b989-0644c68b6043"
  - "Suspicious File Download From IP Via Curl.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious File Download From IP Via Curl.EXE

Detects potentially suspicious file downloads directly from IP addresses using curl.exe

## Metadata

- Rule ID: 5cb299fc-5fb1-4d07-b989-0644c68b6043
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-27
- Source Path: rules/windows/process_creation/proc_creation_win_curl_download_direct_ip_susp_extensions.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \curl.exe
- OriginalFileName: curl.exe
selection_ip:
  CommandLine|re: ://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
selection_http:
  CommandLine|contains: http
selection_flag:
  CommandLine|contains:
  - ' -O'
  - --remote-name
  - --output
selection_ext:
  CommandLine|endswith:
  - .bat
  - .bat"
  - .dat
  - .dat"
  - .dll
  - .dll"
  - .exe
  - .exe"
  - .gif
  - .gif"
  - .hta
  - .hta"
  - .jpeg
  - .jpeg"
  - .log
  - .log"
  - .msi
  - .msi"
  - .png
  - .png"
  - .ps1
  - .ps1"
  - .psm1
  - .psm1"
  - .vbe
  - .vbe"
  - .vbs
  - .vbs"
  - .bat'
  - .dat'
  - .dll'
  - .exe'
  - .gif'
  - .hta'
  - .jpeg'
  - .log'
  - .msi'
  - .png'
  - .ps1'
  - .psm1'
  - .vbe'
  - .vbs'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://labs.withsecure.com/publications/fin7-target-veeam-servers
- https://github.com/WithSecureLabs/iocs/blob/344203de742bb7e68bd56618f66d34be95a9f9fc/FIN7VEEAM/iocs.csv
- https://github.com/pr0xylife/IcedID/blob/8dd1e218460db4f750d955b4c65b2f918a1db906/icedID_09.28.2023.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_download_direct_ip_susp_extensions.yml)
