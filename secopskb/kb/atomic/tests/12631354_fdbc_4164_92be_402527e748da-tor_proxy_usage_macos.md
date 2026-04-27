---
atomic_guid: "12631354-fdbc-4164-92be-402527e748da"
title: "Tor Proxy Usage - MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1090.003"
attack_technique_name: "Proxy: Multi-hop Proxy"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.003/T1090.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "12631354-fdbc-4164-92be-402527e748da"
  - "Tor Proxy Usage - MacOS"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test is designed to launch the tor proxy service, which is what is utilized in the background by the Tor Browser and other applications with add-ons in order to provide onion routing functionality.
Upon successful execution, the tor proxy service will be launched.

## ATT&CK Mapping

- [[kb/attack/techniques/T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]

## Dependencies

Tor must be installed on the machine

### Prerequisite Check

```bash
if [ -x "$(command -v tor --version)" ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
if [ ! -x "$(command -v brew --version)" ]; then /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh keystroke return)"; fi
brew install tor
```

## Executor

- name: sh

### Command

```bash
osascript -e 'tell application "Terminal" to do script "tor"'
```

### Cleanup

```bash
killall tor > /dev/null 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.003/T1090.003.yaml)
