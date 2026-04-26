---
atomic_guid: "2d7c471a-e887-4b78-b0dc-b0df1f2e0658"
title: "Malicious User Agents - Nix"
framework: "atomic"
generated: "true"
attack_technique_id: "T1071.001"
attack_technique_name: "Application Layer Protocol: Web Protocols"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.001/T1071.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "2d7c471a-e887-4b78-b0dc-b0df1f2e0658"
  - "Malicious User Agents - Nix"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Malicious User Agents - Nix

This test simulates an infected host beaconing to command and control.
Inspired by APTSimulator - https://github.com/NextronSystems/APTSimulator/blob/master/test-sets/command-and-control/malicious-user-agents.bat

## Metadata

- Atomic GUID: 2d7c471a-e887-4b78-b0dc-b0df1f2e0658
- Technique: T1071.001: Application Layer Protocol: Web Protocols
- Platforms: linux, macos
- Executor: sh
- Source Path: atomics/T1071.001/T1071.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Input Arguments

### domain

- description: Default domain to simulate against
- type: string
- default: www.google.com

## Executor

- name: sh

### Command

```sh
curl -s -A "HttpBrowser/1.0" -m3 #{domain}
curl -s -A "Wget/1.9+cvs-stable (Red Hat modified)" -m3 #{domain}
curl -s -A "Opera/8.81 (Windows NT 6.0; U; en)" -m3 #{domain}
curl -s -A "*<|>*" -m3 #{domain}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1071.001/T1071.001.yaml)
