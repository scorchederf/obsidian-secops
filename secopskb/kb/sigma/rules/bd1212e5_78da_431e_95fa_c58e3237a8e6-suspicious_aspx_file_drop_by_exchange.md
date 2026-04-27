---
sigma_id: "bd1212e5-78da-431e-95fa-c58e3237a8e6"
title: "Suspicious ASPX File Drop by Exchange"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_exchange_webshell_drop.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_exchange_webshell_drop.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "bd1212e5-78da-431e-95fa-c58e3237a8e6"
  - "Suspicious ASPX File Drop by Exchange"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious ASPX File Drop by Exchange

Detects suspicious file type dropped by an Exchange component in IIS into a suspicious folder

## Metadata

- Rule ID: bd1212e5-78da-431e-95fa-c58e3237a8e6
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), MSTI (query, idea)
- Date: 2022-10-01
- Source Path: rules/windows/file/file_event/file_event_win_exchange_webshell_drop.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
selection:
  Image|endswith: \w3wp.exe
  CommandLine|contains: MSExchange
  TargetFilename|contains:
  - FrontEnd\HttpProxy\
  - \inetpub\wwwroot\aspnet_client\
selection_types:
  TargetFilename|endswith:
  - .aspx
  - .asp
  - .ashx
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/09/30/analyzing-attacks-using-the-exchange-vulnerabilities-cve-2022-41040-and-cve-2022-41082/
- https://www.gteltsc.vn/blog/canh-bao-chien-dich-tan-cong-su-dung-lo-hong-zero-day-tren-microsoft-exchange-server-12714.html
- https://en.gteltsc.vn/blog/cap-nhat-nhe-ve-lo-hong-bao-mat-0day-microsoft-exchange-dang-duoc-su-dung-de-tan-cong-cac-to-chuc-tai-viet-nam-9685.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_exchange_webshell_drop.yml)
