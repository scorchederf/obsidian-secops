---
atomic_guid: "0ad9ab92-c48c-4f08-9b20-9633277c4646"
title: "Headless Browser Accessing Mockbin"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.003"
attack_technique_name: "Hide Artifacts: Hidden Window"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.003/T1564.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "0ad9ab92-c48c-4f08-9b20-9633277c4646"
  - "Headless Browser Accessing Mockbin"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The following Atomic Red Team test leverages the Chrome headless browser to access a mockbin site. Create your own Mockbin.org site and replace the BIN in the inputs.
The default Mockbin ID forwards to google.com and you may view the details here https://mockbin.org/bin/f6b9a876-a826-4ac0-83b8-639d6ad516ec/view.
Reference: https://cert.gov.ua/article/5702579

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]

## Input Arguments

### bin_id

- description: Mockbin.org BIN ID
- type: string
- default: f6b9a876-a826-4ac0-83b8-639d6ad516ec

### browser

- description: Browser to use (msedge, chrome, firefox)
- type: string
- default: chrome

## Executor

- name: command_prompt

### Command

```cmd
start "" #{browser} --headless --disable-gpu https://mockbin.org/bin/#{bin_id}
```

### Cleanup

```cmd
taskkill /im #{browser} /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.003/T1564.003.yaml)
