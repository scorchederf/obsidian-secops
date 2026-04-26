---
mitre_id: "M1046"
mitre_name: "Boot Integrity"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--7da0387c-ba92-4553-b291-b636ee42b2eb"
mitre_created: "2019-06-11T17:02:36.984Z"
mitre_modified: "2024-12-10T18:48:36.517Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1046/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Boot Integrity ensures that a system starts securely by verifying the integrity of its boot process, operating system, and associated components. This mitigation focuses on leveraging secure boot mechanisms, hardware-rooted trust, and runtime integrity checks to prevent tampering during the boot sequence. It is designed to thwart adversaries attempting to modify system firmware, bootloaders, or critical OS components. This mitigation can be implemented through the following measures:

Implementation of Secure Boot:

- Implementation: Enable UEFI Secure Boot on all systems and configure it to allow only signed bootloaders and operating systems.
- Use Case: An adversary attempts to replace the system’s bootloader with a malicious version to gain persistence. Secure Boot prevents the untrusted bootloader from executing, halting the attack.

Utilization of TPMs:

- Implementation: Configure systems to use TPM-based attestation for boot integrity, ensuring that any modification to the firmware, bootloader, or OS is detected.
- Use Case: A compromised firmware component alters the boot sequence. The TPM detects the change and triggers an alert, allowing the organization to respond before further damage.

Enable Bootloader Passwords:

- Implementation: Protect BIOS/UEFI settings with a strong password and limit physical access to devices.
- Use Case: An attacker with physical access attempts to disable Secure Boot or modify the boot sequence. The password prevents unauthorized changes.

Runtime Integrity Monitoring:

- Implementation: Deploy solutions to verify the integrity of critical files and processes after boot.
- Use Case: A malware infection modifies kernel modules post-boot. Runtime integrity monitoring detects the modification and prevents the malicious module from loading.

## Workspace

- [[workspaces/attack/mitigations/M1046-boot_integrity-note|Open workspace note]]

![[workspaces/attack/mitigations/M1046-boot_integrity-note]]

## Mitigates Techniques

- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]
    - [[T1195-supply_chain_compromise#^t1195003-compromise-hardware-supply-chain|T1195.003: Compromise Hardware Supply Chain]]
- [[T1495-firmware_corruption|T1495: Firmware Corruption]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505006-vsphere-installation-bundles|T1505.006: vSphere Installation Bundles]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
    - [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]
    - [[T1542-pre-os_boot#^t1542003-bootkit|T1542.003: Bootkit]]
    - [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]]
    - [[T1542-pre-os_boot#^t1542005-tftp-boot|T1542.005: TFTP Boot]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553006-code-signing-policy-modification|T1553.006: Code Signing Policy Modification]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
    - [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]]
    - [[T1601-modify_system_image#^t1601002-downgrade-system-image|T1601.002: Downgrade System Image]]

