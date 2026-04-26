---
sigma_id: "0250638a-2b28-4541-86fc-ea4c558fa0c6"
title: "Suspicious Browser Child Process - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_susp_browser_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_browser_child_process.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "0250638a-2b28-4541-86fc-ea4c558fa0c6"
  - "Suspicious Browser Child Process - MacOS"
attack_technique_ids:
  - "T1189"
  - "T1203"
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Browser Child Process - MacOS

Detects suspicious child processes spawned from browsers. This could be a result of a potential web browser exploitation.

## Metadata

- Rule ID: 0250638a-2b28-4541-86fc-ea4c558fa0c6
- Status: test
- Level: medium
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-04-05
- Source Path: rules/macos/process_creation/proc_creation_macos_susp_browser_child_process.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1189-drive-by_compromise|T1189]]
- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  ParentImage|contains:
  - com.apple.WebKit.WebContent
  - firefox
  - Google Chrome Helper
  - Google Chrome
  - Microsoft Edge
  - Opera
  - Safari
  - Tor Browser
  Image|endswith:
  - /bash
  - /curl
  - /dash
  - /ksh
  - /osascript
  - /perl
  - /php
  - /pwsh
  - /python
  - /sh
  - /tcsh
  - /wget
  - /zsh
filter_main_generic:
  CommandLine|contains: --defaults-torrc
filter_main_ms_autoupdate:
  CommandLine|contains: /Library/Application Support/Microsoft/MAU*/Microsoft AutoUpdate.app/Contents/MacOS/msupdate
filter_main_chrome:
  ParentImage|contains:
  - Google Chrome Helper
  - Google Chrome
  CommandLine|contains:
  - /Volumes/Google Chrome/Google Chrome.app/Contents/Frameworks/*/Resources/install.sh
  - /Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/*/Resources/keystone_promote_preflight.sh
  - /Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/*/Resources/keystone_promote_postflight.sh
filter_main_ms_edge:
  ParentImage|contains: Microsoft Edge
  CommandLine|contains:
  - IOPlatformExpertDevice
  - hw.model
filter_main_chromerecovery:
  ParentImage|contains:
  - Google Chrome Helper
  - Google Chrome
  CommandLine|contains|all:
  - /Users/
  - /Library/Application Support/Google/Chrome/recovery/
  - /ChromeRecovery
filter_optional_null:
  CommandLine: null
filter_optional_empty:
  CommandLine: ''
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate browser install, update and recovery scripts

## References

- https://fr.slideshare.net/codeblue_jp/cb19-recent-apt-attack-on-crypto-exchange-employees-by-heungsoo-kang
- https://github.com/elastic/detection-rules/blob/4312d8c9583be524578a14fe6295c3370b9a9307/rules/macos/execution_initial_access_suspicious_browser_childproc.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_browser_child_process.yml)
