---
mitre_id: "T1542"
mitre_name: "Pre-OS Boot"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7f0ca133-88c4-40c6-a62f-b3083a7fbc2e"
mitre_created: "2019-11-13T14:44:49.439Z"
mitre_modified: "2025-10-24T17:49:01.466Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1542/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Network Devices"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0005"
  - "TA0003"
d3fend_ids:
  - "D3-APCA"
  - "D3-AVE"
  - "D3-BA"
  - "D3-CSPP"
  - "D3-FBA"
  - "D3-FEMC"
  - "D3-FV"
  - "D3-NTCD"
  - "D3-NTF"
  - "D3-NTSA"
  - "D3-PHDURA"
  - "D3-PMAD"
  - "D3-RS"
  - "D3-RTSD"
  - "D3-SFV"
  - "D3-SU"
  - "D3-SWI"
  - "D3-UGLPA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting process of a computer, firmware and various startup services are loaded before the operating system. These programs control flow of execution before the operating system takes control.(Citation: Wikipedia Booting)

Adversaries may overwrite data in boot drivers or firmware such as BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) to persist on systems at a layer below the operating system. This can be particularly difficult to detect as malware at this level will not be detected by host software-based defenses.

## Workspace

- [[workspaces/attack/techniques/T1542-pre-os_boot-note|Open workspace note]]

![[workspaces/attack/techniques/T1542-pre-os_boot-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]
- [[TA0003-persistence|TA0003: Persistence]]

## D3FEND

- [[D3-APCA-application_protocol_command_analysis|D3-APCA: Application Protocol Command Analysis]]
- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-BA-bootloader_authentication|D3-BA: Bootloader Authentication]]
- [[D3-CSPP-client-server_payload_profiling|D3-CSPP: Client-server Payload Profiling]]
- [[D3-FBA-firmware_behavior_analysis|D3-FBA: Firmware Behavior Analysis]]
- [[D3-FEMC-firmware_embedded_monitoring_code|D3-FEMC: Firmware Embedded Monitoring Code]]
- [[D3-FV-firmware_verification|D3-FV: Firmware Verification]]
- [[D3-NTCD-network_traffic_community_deviation|D3-NTCD: Network Traffic Community Deviation]]
- [[D3-NTF-network_traffic_filtering|D3-NTF: Network Traffic Filtering]]
- [[D3-NTSA-network_traffic_signature_analysis|D3-NTSA: Network Traffic Signature Analysis]]
- [[D3-PHDURA-per_host_download-upload_ratio_analysis|D3-PHDURA: Per Host Download-Upload Ratio Analysis]]
- [[D3-PMAD-protocol_metadata_anomaly_detection|D3-PMAD: Protocol Metadata Anomaly Detection]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-RTSD-remote_terminal_session_detection|D3-RTSD: Remote Terminal Session Detection]]
- [[D3-SFV-system_firmware_verification|D3-SFV: System Firmware Verification]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]

## Subtechniques

### T1542.001: System Firmware

^t1542001-system-firmware

Adversaries may modify system firmware to persist on systems.The BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) or Extensible Firmware Interface (EFI) are examples of system firmware that operate as the software interface between the operating system and hardware of a computer.(Citation: Wikipedia BIOS)(Citation: Wikipedia UEFI)(Citation: About UEFI)

System firmware like BIOS and (U)EFI underly the functionality of a computer and may be modified by an adversary to perform or assist in malicious activity. Capabilities exist to overwrite the system firmware, which may give sophisticated adversaries a means to install malicious firmware updates as a means of persistence on a system that may be difficult to detect.

### T1542.002: Component Firmware

^t1542002-component-firmware

Adversaries may modify component firmware to persist on systems. Some adversaries may employ sophisticated means to compromise computer components and install malicious firmware that will execute adversary code outside of the operating system and main system firmware or BIOS. This technique may be similar to [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]] but conducted upon other system components/devices that may not have the same capability or level of integrity checking.

Malicious component firmware could provide both a persistent level of access to systems despite potential typical failures to maintain access and hard disk re-images, as well as a way to evade host software-based defenses and integrity checks.

### T1542.003: Bootkit

^t1542003-bootkit

Adversaries may use bootkits to persist on systems. A bootkit is a malware variant that modifies the boot sectors of a hard drive, allowing malicious code to execute before a computer's operating system has loaded. Bootkits reside at a layer below the operating system and may make it difficult to perform full remediation unless an organization suspects one was used and can act accordingly.

In BIOS systems, a bootkit may modify the Master Boot Record (MBR) and/or Volume Boot Record (VBR).(Citation: Mandiant M Trends 2016) The MBR is the section of disk that is first loaded after completing hardware initialization by the BIOS. It is the location of the boot loader. An adversary who has raw access to the boot drive may overwrite this area, diverting execution during startup from the normal boot loader to adversary code.(Citation: Lau 2011)

The MBR passes control of the boot process to the VBR. Similar to the case of MBR, an adversary who has raw access to the boot drive may overwrite the VBR to divert execution during startup to adversary code.

In UEFI (Unified Extensible Firmware Interface) systems, a bootkit may instead create or modify files in the EFI system partition (ESP). The ESP is a partition on data storage used by devices containing UEFI that allows the system to boot the OS and other utilities used by the system. An adversary can use the newly created or patched files in the ESP to run malicious kernel code.(Citation: Microsoft Security)(Citation: welivesecurity)

### T1542.004: ROMMONkit

^t1542004-rommonkit

Adversaries may abuse the ROM Monitor (ROMMON) by loading an unauthorized firmware with adversary code to provide persistent access and manipulate device behavior that is difficult to detect. (Citation: Cisco Synful Knock Evolution)(Citation: Cisco Blog Legacy Device Attacks)


ROMMON is a Cisco network device firmware that functions as a boot loader, boot image, or boot helper to initialize hardware and software when the platform is powered on or reset. Similar to [[T1542-pre-os_boot#^t1542005-tftp-boot|T1542.005: TFTP Boot]], an adversary may upgrade the ROMMON image locally or remotely (for example, through TFTP) with adversary code and restart the device in order to overwrite the existing ROMMON image. This provides adversaries with the means to update the ROMMON to gain persistence on a system in a way that may be difficult to detect.

### T1542.005: TFTP Boot

^t1542005-tftp-boot

Adversaries may abuse netbooting to load an unauthorized network device operating system from a Trivial File Transfer Protocol (TFTP) server. TFTP boot (netbooting) is commonly used by network administrators to load configuration-controlled network device images from a centralized management server. Netbooting is one option in the boot sequence and can be used to centralize, manage, and control device images.

Adversaries may manipulate the configuration on the network device specifying use of a malicious TFTP server, which may be used in conjunction with [[T1601-modify_system_image|T1601: Modify System Image]] to load a modified image on device startup or reset. The unauthorized image allows adversaries to modify device configuration, add malicious capabilities to the device, and introduce backdoors to maintain control of the network device while minimizing detection through use of a standard functionality. This technique is similar to [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]] and may result in the network device running a modified image. (Citation: Cisco Blog Legacy Device Attacks)

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1035-limit_access_to_resource_over_network|M1035: Limit Access to Resource Over Network]]
- [[M1046-boot_integrity|M1046: Boot Integrity]]
- [[M1047-audit|M1047: Audit]]
- [[M1051-update_software|M1051: Update Software]]

## Platforms

- Linux
- Network Devices
- Windows
- macOS

