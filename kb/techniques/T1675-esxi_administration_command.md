---
mitre_id: "T1675"
mitre_name: "ESXi Administration Command"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--31e5011f-090e-45be-9bb6-17a1c5e8219b"
mitre_created: "2025-03-28T14:01:52.810Z"
mitre_modified: "2025-04-16T14:57:47.078Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1675/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
mitre_tactic_ids:
  - "TA0002"
---

# T1675: ESXi Administration Command

Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi virtual environment. Persistent background services on ESXi-hosted VMs, such as the VMware Tools Daemon Service, allow for remote management from the ESXi server. The tools daemon service runs as `vmtoolsd.exe` on Windows guest operating systems, `vmware-tools-daemon` on macOS, and `vmtoolsd ` on Linux.(Citation: Broadcom VMware Tools Services) 

Adversaries may leverage a variety of tools to execute commands on ESXi-hosted VMs – for example, by using the vSphere Web Services SDK to programmatically execute commands and scripts via APIs such as `StartProgramInGuest`, `ListProcessesInGuest`,  `ListFileInGuest`, and `InitiateFileTransferFromGuest`.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Broadcom Running Guest OS Operations) This may enable follow-on behaviors on the guest VMs, such as [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]], [[T1005-data_from_local_system|T1005: Data from Local System]], or [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]. 

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]

## Platforms

- ESXi

