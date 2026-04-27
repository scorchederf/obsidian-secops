---
mitre_id: "T1040"
mitre_name: "Network Sniffing"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3257eb21-f9a7-4430-8de1-d8b6e288f529"
mitre_created: "2017-05-31T21:30:41.399Z"
mitre_modified: "2025-10-24T17:48:36.910Z"
mitre_version: "1.7"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1040/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
  - "Network Devices"
  - "IaaS"
mitre_tactic_ids:
  - "TA0006"
  - "TA0007"
d3fend_ids:
  - "D3-DNSTA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may passively sniff network traffic to capture information about an environment, including authentication material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol. Techniques for name service resolution poisoning, such as [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]], can also be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.

Network sniffing may reveal configuration details, such as running services, version numbers, and other network characteristics (e.g. IP addresses, hostnames, VLAN IDs) necessary for subsequent [[TA0008-lateral_movement|TA0008: Lateral Movement]] and/or [[TA0005-defense_evasion|TA0005: Defense Evasion]] activities. Adversaries may likely also utilize network sniffing during [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]] (AiTM) to passively gain additional knowledge about the environment.

In cloud-based environments, adversaries may still be able to use traffic mirroring services to sniff network traffic from virtual machines. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to.(Citation: AWS Traffic Mirroring)(Citation: GCP Packet Mirroring)(Citation: Azure Virtual Network TAP) Often, much of this traffic will be in cleartext due to the use of TLS termination at the load balancer level to reduce the strain of encrypting and decrypting traffic.(Citation: Rhino Security Labs AWS VPC Traffic Mirroring)(Citation: SpecterOps AWS Traffic Mirroring) The adversary can then use exfiltration techniques such as Transfer Data to Cloud Account in order to access the sniffed traffic.(Citation: Rhino Security Labs AWS VPC Traffic Mirroring)

On network devices, adversaries may perform network captures using [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]] commands such as `monitor capture`.(Citation: US-CERT-TA18-106A)(Citation: capture_embedded_packet_on_software)

## Workspace

- [[workspaces/attack/techniques/T1040-network_sniffing-note|Open workspace note]]

![[workspaces/attack/techniques/T1040-network_sniffing-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2020-11-002-local_network_sniffing|CAR-2020-11-002: Local Network Sniffing]]

### Atomic Tests

- [[kb/atomic/tests/10c710c9_9104_4d5f_8829_5b65391e2a29-packet_capture_linux_socket_af_packet_sock_raw_with_sudo|Packet Capture Linux socket AF_PACKET,SOCK_RAW with sudo (bash; linux)]]
- [[kb/atomic/tests/515575ab_d213_42b1_aa64_ef6a2dd4641b-packet_capture_linux_socket_af_inet_sock_packet_udp_with_sudo|Packet Capture Linux socket AF_INET,SOCK_PACKET,UDP with sudo (bash; linux)]]
- [[kb/atomic/tests/7a0895f0_84c1_4adf_8491_a21510b1d4c1-packet_capture_linux_socket_af_inet_sock_raw_tcp_with_sudo|Packet Capture Linux socket AF_INET,SOCK_RAW,TCP with sudo (bash; linux)]]
- [[kb/atomic/tests/7fe741f7_b265_4951_a7c7_320889083b3e-packet_capture_linux_using_tshark_or_tcpdump|Packet Capture Linux using tshark or tcpdump (bash; linux)]]
- [[kb/atomic/tests/855fb8b4_b8ab_4785_ae77_09f5df7bff55-windows_internal_pktmon_set_filter|Windows Internal pktmon set filter (command_prompt; windows)]]
- [[kb/atomic/tests/9c15a7de_de14_46c3_bc2a_6d94130986ae-powershell_network_sniffing|PowerShell Network Sniffing (powershell; windows)]]
- [[kb/atomic/tests/9d04efee_eff5_4240_b8d2_07792b873608-packet_capture_macos_using_tcpdump_or_tshark|Packet Capture macOS using tcpdump or tshark (bash; macos)]]
- [[kb/atomic/tests/a3a0d4c9_c068_4563_a08d_583bd05b884c-filtered_packet_capture_freebsd_using_dev_bpfn_with_sudo|Filtered Packet Capture FreeBSD using /dev/bpfN with sudo (sh; linux)]]
- [[kb/atomic/tests/a5b2f6a0_24b4_493e_9590_c699f75723ca-packet_capture_windows_command_prompt|Packet Capture Windows Command Prompt (command_prompt; windows)]]
- [[kb/atomic/tests/b1cbdf8b_6078_48f5_a890_11ea19d7f8e9-packet_capture_linux_socket_af_packet_sock_raw_with_bpf_filter_for_udp_with_sudo|Packet Capture Linux socket AF_PACKET,SOCK_RAW with BPF filter for UDP with sudo (bash; linux)]]
- 6 more in the generated source index

### LOLBAS Entries

- [[kb/lolbas/entries/osbinaries-pktmon_exe|Pktmon.exe (Reconnaissance)]]
- [[kb/lolbas/entries/othermsbinaries-nmcap_exe|Nmcap.exe (Reconnaissance)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]
- [[TA0007-discovery|TA0007: Discovery]]

## D3FEND

- [[D3-DNSTA-dns_traffic_analysis|D3-DNSTA: DNS Traffic Analysis]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]

## Tools
- [[empire|Empire (S0363)]]
- [[impacket|Impacket (S0357)]]
- [[nbtscan|NBTscan (S0590)]]
- [[poshc2|PoshC2 (S0378)]]
- [[responder|Responder (S0174)]]


## Platforms

- Linux
- macOS
- Windows
- Network Devices
- IaaS

