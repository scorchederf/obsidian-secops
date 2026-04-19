---
id: T1602
name: Data from Configuration Repository
created: 2020-10-19 23:46:13.931000+00:00
modified: 2025-10-24 17:48:22.396000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[collection|Collection]]

Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories may also facilitate remote access and administration of devices.

Adversaries may target these repositories in order to collect large quantities of sensitive system administration data. Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data, much of which may align with adversary Discovery objectives.(Citation: US-CERT-TA18-106A)(Citation: US-CERT TA17-156A SNMP Abuse 2017)

## Subtechniques

### T1602.001: SNMP (MIB Dump)

^t1602001-snmp-(mib-dump)

**Parent Technique**
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]

**Tactic**
- [[collection|Collection]]

Adversaries may target the Management Information Base (MIB) to collect and/or mine valuable information in a network managed using Simple Network Management Protocol (SNMP).

The MIB is a configuration repository that stores variable information accessible via SNMP in the form of object identifiers (OID). Each OID identifies a variable that can be read or set and permits active management tasks, such as configuration changes, through remote modification of these variables. SNMP can give administrators great insight in their systems, such as, system information, description of hardware, physical location, and software packages(Citation: SANS Information Security Reading Room Securing SNMP Securing SNMP). The MIB may also contain device operational information, including running configuration, routing table, and interface details.

Adversaries may use SNMP queries to collect MIB content directly from SNMP-managed devices in order to collect network information that allows the adversary to build network maps and facilitate future targeted exploitation.(Citation: US-CERT-TA18-106A)(Citation: Cisco Blog Legacy Device Attacks) 

### T1602.002: Network Device Configuration Dump

^t1602002-network-device-configuration-dump

**Parent Technique**
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]

**Tactic**
- [[collection|Collection]]

Adversaries may access network configuration files to collect sensitive data about the device and the network. The network configuration is a file containing parameters that determine the operation of the device. The device typically stores an in-memory copy of the configuration while operating, and a separate configuration on non-volatile storage to load after device reset. Adversaries can inspect the configuration files to reveal information about the target network and its layout, the network device and its software, or identifying legitimate accounts and credentials for later use.

Adversaries can use common management tools and protocols, such as Simple Network Management Protocol (SNMP) and Smart Install (SMI), to access network configuration files.(Citation: US-CERT TA18-106A Network Infrastructure Devices 2018)(Citation: Cisco Blog Legacy Device Attacks) These tools may be used to query specific data from a configuration repository or configure the device to export the configuration for later analysis. 

## Mitigations

- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]
- [[M1037-filter_network_traffic|M1037: Filter Network Traffic]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1051-update_software|M1051: Update Software]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- Network Devices

