---
atomic_guid: "c1402f7b-67ca-43a8-b5f3-3143abedc01b"
title: "Search macOS Safari Cookies"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "c1402f7b-67ca-43a8-b5f3-3143abedc01b"
  - "Search macOS Safari Cookies"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Search macOS Safari Cookies

This test uses `grep` to search a macOS Safari binaryCookies file for specified values. This was used by CookieMiner malware.

Upon successful execution, MacOS shell will cd to `~/Libraries/Cookies` and grep for `Cookies.binarycookies`.

## Metadata

- Atomic GUID: c1402f7b-67ca-43a8-b5f3-3143abedc01b
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: macos
- Executor: sh
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Input Arguments

### search_string

- description: String to search Safari cookies to find.
- type: string
- default: coinbase

## Executor

- name: sh

### Command

```bash
cd ~/Library/Cookies
grep -q "#{search_string}" "Cookies.binarycookies"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
