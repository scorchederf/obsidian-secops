---
sigma_id: "573df571-a223-43bc-846e-3f98da481eca"
title: "Creation Of a Suspicious ADS File Outside a Browser Download"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_stream_hash/create_stream_hash_creation_internet_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_creation_internet_file.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / create_stream_hash"
aliases:
  - "573df571-a223-43bc-846e-3f98da481eca"
  - "Creation Of a Suspicious ADS File Outside a Browser Download"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Creation Of a Suspicious ADS File Outside a Browser Download

Detects the creation of a suspicious ADS (Alternate Data Stream) file by software other than browsers

## Metadata

- Rule ID: 573df571-a223-43bc-846e-3f98da481eca
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-10-22
- Modified: 2023-06-12
- Source Path: rules/windows/create_stream_hash/create_stream_hash_creation_internet_file.yml

## Logsource

- category: create_stream_hash
- product: windows

## Detection

```yaml
selection:
  Contents|startswith: '[ZoneTransfer]  ZoneId=3'
  TargetFilename|endswith: :Zone.Identifier
  TargetFilename|contains:
  - .exe
  - .scr
  - .bat
  - .cmd
  - .docx
  - .hta
  - .jse
  - .lnk
  - .pptx
  - .ps
  - .reg
  - .sct
  - .vb
  - .wsc
  - .wsf
  - .xlsx
filter_optional_brave:
  Image|endswith: \brave.exe
filter_optional_chrome:
  Image:
  - C:\Program Files\Google\Chrome\Application\chrome.exe
  - C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
filter_optional_firefox:
  Image:
  - C:\Program Files\Mozilla Firefox\firefox.exe
  - C:\Program Files (x86)\Mozilla Firefox\firefox.exe
filter_optional_ie:
  Image:
  - C:\Program Files (x86)\Internet Explorer\iexplore.exe
  - C:\Program Files\Internet Explorer\iexplore.exe
filter_optional_maxthon:
  Image|endswith: \maxthon.exe
filter_optional_edge_1:
- Image|startswith: C:\Program Files (x86)\Microsoft\EdgeWebView\Application\
- Image|endswith: \WindowsApps\MicrosoftEdge.exe
- Image:
  - C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
  - C:\Program Files\Microsoft\Edge\Application\msedge.exe
filter_optional_edge_2:
  Image|startswith:
  - C:\Program Files (x86)\Microsoft\EdgeCore\
  - C:\Program Files\Microsoft\EdgeCore\
  Image|endswith:
  - \msedge.exe
  - \msedgewebview2.exe
filter_optional_opera:
  Image|endswith: \opera.exe
filter_optional_safari:
  Image|endswith: \safari.exe
filter_optional_seamonkey:
  Image|endswith: \seamonkey.exe
filter_optional_vivaldi:
  Image|endswith: \vivaldi.exe
filter_optional_whale:
  Image|endswith: \whale.exe
filter_optional_snipping_tool:
  Image|startswith: C:\Program Files\WindowsApps\Microsoft.ScreenSketch_
  Image|endswith: \SnippingTool\SnippingTool.exe
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains|all:
  - \AppData\Local\Packages\Microsoft.ScreenSketch_
  - '\TempState\Screenshot '
  TargetFilename|endswith: .png:Zone.Identifier
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Other legitimate browsers not currently included in the filter (please add them)
- Legitimate downloads via scripting or command-line tools (Investigate to determine if it's legitimate)

## References

- https://www.bleepingcomputer.com/news/security/exploited-windows-zero-day-lets-javascript-files-bypass-security-warnings/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_creation_internet_file.yml)
