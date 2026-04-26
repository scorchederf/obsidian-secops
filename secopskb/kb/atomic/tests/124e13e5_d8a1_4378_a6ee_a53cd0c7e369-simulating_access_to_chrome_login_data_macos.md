---
atomic_guid: "124e13e5-d8a1-4378-a6ee-a53cd0c7e369"
title: "Simulating Access to Chrome Login Data - MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "124e13e5-d8a1-4378-a6ee-a53cd0c7e369"
  - "Simulating Access to Chrome Login Data - MacOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Simulating Access to Chrome Login Data - MacOS

This test locates the Login Data files used by Chrome to store encrypted credentials, then copies them to the temp directory for later exfil. 
Once the files are exfiltrated, malware like CookieMiner could be used to perform credential extraction. 
See https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/ .

## Metadata

- Atomic GUID: 124e13e5-d8a1-4378-a6ee-a53cd0c7e369
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Executor

- name: sh

### Command

```sh
cp ~/Library/"Application Support/Google/Chrome/Default/Login Data" "/tmp/T1555.003_Login Data"
cp ~/Library/"Application Support/Google/Chrome/Default/Login Data For Account" "/tmp/T1555.003_Login Data For Account"
```

### Cleanup

```sh
rm "/tmp/T1555.003_Login Data" >/dev/null 2>&1
rm "/tmp/T1555.003_Login Data For Account" >/dev/null 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
