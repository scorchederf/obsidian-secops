---
mitre_id: "M1030"
mitre_name: "Network Segmentation"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--86598de0-b347-4928-9eb0-0acbfc21908c"
mitre_created: "2019-06-10T20:41:03.271Z"
mitre_modified: "2025-04-02T17:29:32.003Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1030/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise.

Effective network segmentation leverages a combination of physical boundaries, logical separation through VLANs, and access control policies enforced by network appliances like firewalls, routers, and cloud-based configurations. This mitigation can be implemented through the following measures:

Segment Critical Systems:

- Identify and group systems based on their function, sensitivity, and risk. Examples include payment systems, HR databases, production systems, and internet-facing servers.
- Use VLANs, firewalls, or routers to enforce logical separation.

Implement DMZ for Public-Facing Services:

- Host web servers, DNS servers, and email servers in a DMZ to limit their access to internal systems.
- Apply strict firewall rules to filter traffic between the DMZ and internal networks.

Use Cloud-Based Segmentation:

- In cloud environments, use VPCs, subnets, and security groups to isolate applications and enforce traffic rules.
- Apply AWS Transit Gateway or Azure VNet peering for controlled connectivity between cloud segments.

Apply Microsegmentation for Workloads:

- Use software-defined networking (SDN) tools to implement workload-level segmentation and prevent lateral movement.

Restrict Traffic with ACLs and Firewalls:

- Apply Access Control Lists (ACLs) to network devices to enforce "deny by default" policies.
- Use firewalls to restrict both north-south (external-internal) and east-west (internal-internal) traffic.

Monitor and Audit Segmented Networks:

- Regularly review firewall rules, ACLs, and segmentation policies.
- Monitor network flows for anomalies to ensure segmentation is effective.

Test Segmentation Effectiveness:

- Perform periodic penetration tests to verify that unauthorized access is blocked between network segments.

## Workspace

- [[workspaces/attack/mitigations/M1030-network_segmentation-note|Open workspace note]]

![[workspaces/attack/mitigations/M1030-network_segmentation-note]]

## Mitigates Techniques

- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
    - [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]
    - [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]
- [[T1040-network_sniffing|T1040: Network Sniffing]]
- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048001-exfiltration-over-symmetric-encrypted-non-c2-protocol|T1048.001: Exfiltration Over Symmetric Encrypted Non-C2 Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048002-exfiltration-over-asymmetric-encrypted-non-c2-protocol|T1048.002: Exfiltration Over Asymmetric Encrypted Non-C2 Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
    - [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
- [[T1133-external_remote_services|T1133: External Remote Services]]
- [[T1136-create_account|T1136: Create Account]]
- [[T1136-create_account|T1136: Create Account]]
    - [[T1136-create_account#^t1136002-domain-account|T1136.002: Domain Account]]
    - [[T1136-create_account#^t1136003-cloud-account|T1136.003: Cloud Account]]
- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[T1199-trusted_relationship|T1199: Trusted Relationship]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[T1489-service_stop|T1489: Service Stop]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552007-container-api|T1552.007: Container API]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
    - [[T1565-data_manipulation#^t1565003-runtime-data-manipulation|T1565.003: Runtime Data Manipulation]]
- [[T1571-non-standard_port|T1571: Non-Standard Port]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
    - [[T1602-data_from_configuration_repository#^t1602001-snmp-(mib-dump)|T1602.001: SNMP (MIB Dump)]]
    - [[T1602-data_from_configuration_repository#^t1602002-network-device-configuration-dump|T1602.002: Network Device Configuration Dump]]
- [[T1610-deploy_container|T1610: Deploy Container]]
- [[T1612-build_image_on_host|T1612: Build Image on Host]]
- [[T1613-container_and_resource_discovery|T1613: Container and Resource Discovery]]
- [[T1669-wi-fi_networks|T1669: Wi-Fi Networks]]

