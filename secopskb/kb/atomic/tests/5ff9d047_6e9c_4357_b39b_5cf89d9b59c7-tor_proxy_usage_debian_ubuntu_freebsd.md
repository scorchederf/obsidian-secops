---
atomic_guid: "5ff9d047-6e9c-4357-b39b-5cf89d9b59c7"
title: "Tor Proxy Usage - Debian/Ubuntu/FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1090.003"
attack_technique_name: "Proxy: Multi-hop Proxy"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.003/T1090.003.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "5ff9d047-6e9c-4357-b39b-5cf89d9b59c7"
  - "Tor Proxy Usage - Debian/Ubuntu/FreeBSD"
platforms:
  - "linux"
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
(which apt && sudo apt-get -y install tor) || (which pkg && pkg install -y tor)
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
[ "$(uname)" = 'FreeBSD' ] && sysrc tor_enable="YES" && service tor start || sudo systemctl start tor
```

### Cleanup

```bash
[ "$(uname)" = 'FreeBSD' ] && service tor stop && sysrc -x tor_enable || sudo systemctl stop tor
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.003/T1090.003.yaml)
