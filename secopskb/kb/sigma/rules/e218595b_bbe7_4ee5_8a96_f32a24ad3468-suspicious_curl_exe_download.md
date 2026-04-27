---
sigma_id: "e218595b-bbe7-4ee5-8a96-f32a24ad3468"
title: "Suspicious Curl.EXE Download"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_curl_susp_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_susp_download.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e218595b-bbe7-4ee5-8a96-f32a24ad3468"
  - "Suspicious Curl.EXE Download"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious curl process start on Windows and outputs the requested document to a local file

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detection

```yaml
selection_curl:
- Image|endswith: \curl.exe
- Product: The curl executable
selection_susp_locations:
  CommandLine|contains:
  - '%AppData%'
  - '%Public%'
  - '%Temp%'
  - '%tmp%'
  - \AppData\
  - \Desktop\
  - \Temp\
  - \Users\Public\
  - C:\PerfLogs\
  - C:\ProgramData\
  - C:\Windows\Temp\
selection_susp_extensions:
  CommandLine|endswith:
  - .dll
  - .gif
  - .jpeg
  - .jpg
  - .png
  - .temp
  - .tmp
  - .txt
  - .vbe
  - .vbs
filter_optional_git_windows:
  ParentImage: C:\Program Files\Git\usr\bin\sh.exe
  Image: C:\Program Files\Git\mingw64\bin\curl.exe
  CommandLine|contains|all:
  - '--silent --show-error --output '
  - gfw-httpget-
  - AppData
condition: selection_curl and 1 of selection_susp_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## Simulation

### Curl Download File

- Atomic Test: [[kb/atomic/tests/2b080b99_0deb_4d51_af0f_833d37c4ca6a-curl_download_file|2b080b99-0deb-4d51-af0f-833d37c4ca6a]]
- atomic_guid: 2b080b99-0deb-4d51-af0f-833d37c4ca6a
- name: Curl Download File
- technique: T1105
- type: atomic-red-team

## References

- https://twitter.com/max_mal_/status/1542461200797163522
- https://web.archive.org/web/20200128160046/https://twitter.com/reegun21/status/1222093798009790464
- https://github.com/pr0xylife/Qakbot/blob/4f0795d79dabee5bc9dd69f17a626b48852e7869/Qakbot_AA_23.06.2022.txt
- https://www.volexity.com/blog/2022/07/28/sharptongue-deploys-clever-mail-stealing-browser-extension-sharpext/
- https://github.com/redcanaryco/atomic-red-team/blob/0f229c0e42bfe7ca736a14023836d65baa941ed2/atomics/T1105/T1105.md#atomic-test-18---curl-download-file

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_susp_download.yml)
