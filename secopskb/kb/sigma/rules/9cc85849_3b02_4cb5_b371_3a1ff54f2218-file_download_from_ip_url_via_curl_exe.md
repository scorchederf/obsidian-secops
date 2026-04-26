---
sigma_id: "9cc85849-3b02-4cb5-b371-3a1ff54f2218"
title: "File Download From IP URL Via Curl.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_curl_download_direct_ip_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_download_direct_ip_exec.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9cc85849-3b02-4cb5-b371-3a1ff54f2218"
  - "File Download From IP URL Via Curl.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Download From IP URL Via Curl.EXE

Detects file downloads directly from IP address URL using curl.exe

## Metadata

- Rule ID: 9cc85849-3b02-4cb5-b371-3a1ff54f2218
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-10-18
- Source Path: rules/windows/process_creation/proc_creation_win_curl_download_direct_ip_exec.yml

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
filter_main_ext:
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
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://labs.withsecure.com/publications/fin7-target-veeam-servers
- https://github.com/WithSecureLabs/iocs/blob/344203de742bb7e68bd56618f66d34be95a9f9fc/FIN7VEEAM/iocs.csv
- https://github.com/pr0xylife/IcedID/blob/8dd1e218460db4f750d955b4c65b2f918a1db906/icedID_09.28.2023.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_download_direct_ip_exec.yml)
