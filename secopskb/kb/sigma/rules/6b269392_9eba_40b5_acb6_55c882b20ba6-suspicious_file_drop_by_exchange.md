---
sigma_id: "6b269392-9eba-40b5-acb6-55c882b20ba6"
title: "Suspicious File Drop by Exchange"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_exchange_webshell_drop_suspicious.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_exchange_webshell_drop_suspicious.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "6b269392-9eba-40b5-acb6-55c882b20ba6"
  - "Suspicious File Drop by Exchange"
attack_technique_ids:
  - "T1190"
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious File Drop by Exchange

Detects suspicious file type dropped by an Exchange component in IIS

## Metadata

- Rule ID: 6b269392-9eba-40b5-acb6-55c882b20ba6
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-10-04
- Source Path: rules/windows/file/file_event/file_event_win_exchange_webshell_drop_suspicious.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]
- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
selection:
  Image|endswith: \w3wp.exe
  CommandLine|contains: MSExchange
selection_types:
  TargetFilename|endswith:
  - .aspx
  - .asp
  - .ashx
  - .ps1
  - .bat
  - .exe
  - .dll
  - .vbs
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/09/30/analyzing-attacks-using-the-exchange-vulnerabilities-cve-2022-41040-and-cve-2022-41082/
- https://www.gteltsc.vn/blog/canh-bao-chien-dich-tan-cong-su-dung-lo-hong-zero-day-tren-microsoft-exchange-server-12714.html
- https://en.gteltsc.vn/blog/cap-nhat-nhe-ve-lo-hong-bao-mat-0day-microsoft-exchange-dang-duoc-su-dung-de-tan-cong-cac-to-chuc-tai-viet-nam-9685.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_exchange_webshell_drop_suspicious.yml)
