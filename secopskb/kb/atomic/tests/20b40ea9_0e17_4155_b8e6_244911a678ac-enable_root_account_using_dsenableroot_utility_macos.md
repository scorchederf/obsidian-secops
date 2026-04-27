---
atomic_guid: "20b40ea9-0e17-4155-b8e6-244911a678ac"
title: "Enable root account using dsenableroot utility - MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.003"
attack_technique_name: "Valid Accounts: Local Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "20b40ea9-0e17-4155-b8e6-244911a678ac"
  - "Enable root account using dsenableroot utility - MacOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enable root account using dsenableroot utility - MacOS

After execution the current/new user will have root access

## Metadata

- Atomic GUID: 20b40ea9-0e17-4155-b8e6-244911a678ac
- Technique: T1078.003: Valid Accounts: Local Accounts
- Platforms: macos
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1078.003/T1078.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
dsenableroot #current user
dsenableroot -u art-tester -p art-tester -r art-root #new user
```

### Cleanup

```bash
dsenableroot -d #current user
dsenableroot -d -u art-tester -p art-tester #new user
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.yaml)
