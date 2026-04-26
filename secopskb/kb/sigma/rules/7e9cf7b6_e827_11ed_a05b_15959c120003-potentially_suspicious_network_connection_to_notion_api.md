---
sigma_id: "7e9cf7b6-e827-11ed-a05b-15959c120003"
title: "Potentially Suspicious Network Connection To Notion API"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_notion_api_susp_communication.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_notion_api_susp_communication.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "low"
logsource: "windows / network_connection"
aliases:
  - "7e9cf7b6-e827-11ed-a05b-15959c120003"
  - "Potentially Suspicious Network Connection To Notion API"
attack_technique_ids:
  - "T1102"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Network Connection To Notion API

Detects a non-browser process communicating with the Notion API. This could indicate potential use of a covert C2 channel such as "OffensiveNotion C2"

## Metadata

- Rule ID: 7e9cf7b6-e827-11ed-a05b-15959c120003
- Status: test
- Level: low
- Author: Gavin Knapp
- Date: 2023-05-03
- Source Path: rules/windows/network_connection/net_connection_win_domain_notion_api_susp_communication.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1102-web_service|T1102]]

## Detection

```yaml
selection:
  DestinationHostname|contains: api.notion.com
filter_main_notion:
  Image|endswith: \AppData\Local\Programs\Notion\Notion.exe
filter_main_brave:
  Image|endswith: \brave.exe
filter_main_chrome:
  Image:
  - C:\Program Files\Google\Chrome\Application\chrome.exe
  - C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
filter_main_firefox:
  Image:
  - C:\Program Files\Mozilla Firefox\firefox.exe
  - C:\Program Files (x86)\Mozilla Firefox\firefox.exe
filter_main_ie:
  Image:
  - C:\Program Files (x86)\Internet Explorer\iexplore.exe
  - C:\Program Files\Internet Explorer\iexplore.exe
filter_main_maxthon:
  Image|endswith: \maxthon.exe
filter_main_edge_1:
- Image|startswith: C:\Program Files (x86)\Microsoft\EdgeWebView\Application\
- Image|endswith: \WindowsApps\MicrosoftEdge.exe
- Image:
  - C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
  - C:\Program Files\Microsoft\Edge\Application\msedge.exe
filter_main_edge_2:
  Image|startswith:
  - C:\Program Files (x86)\Microsoft\EdgeCore\
  - C:\Program Files\Microsoft\EdgeCore\
  Image|endswith:
  - \msedge.exe
  - \msedgewebview2.exe
filter_main_opera:
  Image|endswith: \opera.exe
filter_main_safari:
  Image|endswith: \safari.exe
filter_main_seamonkey:
  Image|endswith: \seamonkey.exe
filter_main_vivaldi:
  Image|endswith: \vivaldi.exe
filter_main_whale:
  Image|endswith: \whale.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate applications communicating with the "api.notion.com" endpoint that are not already in the exclusion list. The desktop and browser applications do not appear to be using the API by default unless integrations are configured.

## References

- https://github.com/mttaggart/OffensiveNotion
- https://medium.com/@huskyhacks.mk/we-put-a-c2-in-your-notetaking-app-offensivenotion-3e933bace332

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_notion_api_susp_communication.yml)
