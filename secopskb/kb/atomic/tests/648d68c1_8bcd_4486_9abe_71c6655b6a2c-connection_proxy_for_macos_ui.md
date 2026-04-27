---
atomic_guid: "648d68c1-8bcd-4486-9abe-71c6655b6a2c"
title: "Connection Proxy for macOS UI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1090.001"
attack_technique_name: "Proxy: Internal Proxy"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.001/T1090.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "648d68c1-8bcd-4486-9abe-71c6655b6a2c"
  - "Connection Proxy for macOS UI"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enable traffic redirection on macOS UI (not terminal).
The test will modify and enable the "Web Proxy" and "Secure Web Proxy" settings  in System Preferences => Network => Advanced => Proxies for the specified network interface.

Note that this test may conflict with pre-existing system configuration.

## ATT&CK Mapping

- [[kb/attack/techniques/T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]]

## Input Arguments

### interface

- description: Protocol to proxy (http or https)
- type: string
- default: Wi-Fi

### proxy_port

- description: Proxy server port
- type: integer
- default: 8080

### proxy_server

- description: Proxy server URL (host)
- type: url
- default: 127.0.0.1

## Executor

- name: sh

### Command

```bash
networksetup -setwebproxy #{interface} #{proxy_server} #{proxy_port}
networksetup -setsecurewebproxy #{interface} #{proxy_server} #{proxy_port}
```

### Cleanup

```bash
networksetup -setwebproxystate #{interface} off
networksetup -setsecurewebproxystate #{interface} off
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1090.001/T1090.001.yaml)
