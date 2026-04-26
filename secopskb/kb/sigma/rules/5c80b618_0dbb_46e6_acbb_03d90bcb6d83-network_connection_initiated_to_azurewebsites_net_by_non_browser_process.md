---
sigma_id: "5c80b618-0dbb-46e6-acbb-03d90bcb6d83"
title: "Network Connection Initiated To AzureWebsites.NET By Non-Browser Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_azurewebsites.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_azurewebsites.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "5c80b618-0dbb-46e6-acbb-03d90bcb6d83"
  - "Network Connection Initiated To AzureWebsites.NET By Non-Browser Process"
attack_technique_ids:
  - "T1102"
  - "T1102.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Connection Initiated To AzureWebsites.NET By Non-Browser Process

Detects an initiated network connection by a non browser process on the system to "azurewebsites.net". The latter was often used by threat actors as a malware hosting and exfiltration site.

## Metadata

- Rule ID: 5c80b618-0dbb-46e6-acbb-03d90bcb6d83
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-06-24
- Modified: 2024-07-16
- Source Path: rules/windows/network_connection/net_connection_win_domain_azurewebsites.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1102-web_service|T1102]]
- [[kb/attack/techniques/T1102-web_service|T1102.001]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationHostname|endswith: azurewebsites.net
filter_main_chrome:
  Image:
  - C:\Program Files\Google\Chrome\Application\chrome.exe
  - C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
filter_main_chrome_appdata:
  Image|startswith: C:\Users\
  Image|endswith: \AppData\Local\Google\Chrome\Application\chrome.exe
filter_main_firefox:
  Image:
  - C:\Program Files\Mozilla Firefox\firefox.exe
  - C:\Program Files (x86)\Mozilla Firefox\firefox.exe
filter_main_firefox_appdata:
  Image|startswith: C:\Users\
  Image|endswith: \AppData\Local\Mozilla Firefox\firefox.exe
filter_main_ie:
  Image:
  - C:\Program Files (x86)\Internet Explorer\iexplore.exe
  - C:\Program Files\Internet Explorer\iexplore.exe
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
filter_main_safari:
  Image|contains:
  - C:\Program Files (x86)\Safari\
  - C:\Program Files\Safari\
  Image|endswith: \safari.exe
filter_main_defender:
  Image|contains:
  - C:\Program Files\Windows Defender Advanced Threat Protection\
  - C:\Program Files\Windows Defender\
  - C:\ProgramData\Microsoft\Windows Defender\Platform\
  Image|endswith:
  - \MsMpEng.exe
  - \MsSense.exe
filter_main_prtg:
  Image|endswith:
  - C:\Program Files (x86)\PRTG Network Monitor\PRTG Probe.exe
  - C:\Program Files\PRTG Network Monitor\PRTG Probe.exe
filter_main_brave:
  Image|startswith: C:\Program Files\BraveSoftware\
  Image|endswith: \brave.exe
filter_main_maxthon:
  Image|contains: \AppData\Local\Maxthon\
  Image|endswith: \maxthon.exe
filter_main_opera:
  Image|contains: \AppData\Local\Programs\Opera\
  Image|endswith: \opera.exe
filter_main_seamonkey:
  Image|startswith:
  - C:\Program Files\SeaMonkey\
  - C:\Program Files (x86)\SeaMonkey\
  Image|endswith: \seamonkey.exe
filter_main_vivaldi:
  Image|contains: \AppData\Local\Vivaldi\
  Image|endswith: \vivaldi.exe
filter_main_whale:
  Image|startswith:
  - C:\Program Files\Naver\Naver Whale\
  - C:\Program Files (x86)\Naver\Naver Whale\
  Image|endswith: \whale.exe
filter_main_whaterfox:
  Image|startswith:
  - C:\Program Files\Waterfox\
  - C:\Program Files (x86)\Waterfox\
  Image|endswith: \Waterfox.exe
filter_main_slimbrowser:
  Image|startswith:
  - C:\Program Files\SlimBrowser\
  - C:\Program Files (x86)\SlimBrowser\
  Image|endswith: \slimbrowser.exe
filter_main_flock:
  Image|contains: \AppData\Local\Flock\
  Image|endswith: \Flock.exe
filter_main_phoebe:
  Image|contains: \AppData\Local\Phoebe\
  Image|endswith: \Phoebe.exe
filter_main_falkon:
  Image|startswith:
  - C:\Program Files\Falkon\
  - C:\Program Files (x86)\Falkon\
  Image|endswith: \falkon.exe
filter_main_qtweb:
  Image|startswith:
  - C:\Program Files (x86)\QtWeb\
  - C:\Program Files\QtWeb\
  Image|endswith: \QtWeb.exe
filter_main_avant:
  Image|startswith:
  - C:\Program Files (x86)\Avant Browser\
  - C:\Program Files\Avant Browser\
  Image|endswith: \avant.exe
filter_main_discord:
  Image|contains: \AppData\Local\Discord\
  Image|endswith: \Discord.exe
filter_main_null:
  Image: null
filter_main_empty:
  Image: ''
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.sentinelone.com/labs/wip26-espionage-threat-actors-abuse-cloud-infrastructure-in-targeted-telco-attacks/
- https://symantec-enterprise-blogs.security.com/threat-intelligence/harvester-new-apt-attacks-asia
- https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/higaisa-or-winnti-apt-41-backdoors-old-and-new/
- https://intezer.com/blog/research/how-we-escaped-docker-in-azure-functions/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_azurewebsites.yml)
