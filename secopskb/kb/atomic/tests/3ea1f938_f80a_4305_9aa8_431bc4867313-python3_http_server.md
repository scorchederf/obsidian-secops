---
atomic_guid: "3ea1f938-f80a-4305-9aa8-431bc4867313"
title: "Python3 http.server"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.003"
attack_technique_name: "Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "3ea1f938-f80a-4305-9aa8-431bc4867313"
  - "Python3 http.server"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Python3 http.server

An adversary may use the python3 standard library module http.server to exfiltrate data. This test checks if python3 is available and if so, creates a HTTP server on port 9090, captures the PID, sleeps for 10 seconds, then kills the PID and unsets the $PID variable.

## Metadata

- Atomic GUID: 3ea1f938-f80a-4305-9aa8-431bc4867313
- Technique: T1048.003: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1048.003/T1048.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Executor

- elevation_required: False
- name: sh

### Command

```bash
[ "$(uname)" = 'FreeBSD' ] && alias python3=python3.9
if [ $(which python3) ]; then cd /tmp; python3 -m http.server 9090 & PID=$!; sleep 10; kill $PID; unset PID; fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml)
