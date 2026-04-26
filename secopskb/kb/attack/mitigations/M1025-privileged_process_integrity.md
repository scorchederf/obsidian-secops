---
mitre_id: "M1025"
mitre_name: "Privileged Process Integrity"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--72dade3e-1cba-4182-b3b3-a77ca52f02a1"
mitre_created: "2019-06-06T21:08:58.465Z"
mitre_modified: "2024-12-18T18:51:02.792Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1025/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Privileged Process Integrity focuses on defending highly privileged processes (e.g., system services, antivirus, or authentication processes) from tampering, injection, or compromise by adversaries. These processes often interact with critical components, making them prime targets for techniques like code injection, privilege escalation, and process manipulation. This mitigation can be implemented through the following measures:

Protected Process Mechanisms:

- Enable RunAsPPL on Windows systems to protect LSASS and other critical processes.
- Use registry modifications to enforce protected process settings: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\RunAsPPL`

Anti-Injection and Memory Protection:

- Enable Control Flow Guard (CFG), DEP, and ASLR to protect against process memory tampering.
- Deploy endpoint protection tools that actively block process injection attempts.

Code Signing Validation:

- Implement policies for Windows Defender Application Control (WDAC) or AppLocker to enforce execution of signed binaries.
- Ensure critical processes are signed with valid certificates.

Access Controls:

- Use DACLs and MIC to limit which users and processes can interact with privileged processes.
- Disable unnecessary debugging capabilities for high-privileged processes.

Kernel-Level Protections:

- Ensure Kernel Patch Protection (PatchGuard) is enabled on Windows systems.
- Leverage SELinux or AppArmor on Linux to enforce kernel-level security policies.

*Tools for Implementation*

Protected Process Light (PPL):

- RunAsPPL (Windows)
- Windows Defender Credential Guard

Code Integrity and Signing:

- Windows Defender Application Control (WDAC)
- AppLocker
- SELinux/AppArmor (Linux)

Memory Protection:

- Control Flow Guard (CFG), Data Execution Prevention (DEP), ASLR

Process Isolation/Sandboxing:

- Firejail (Linux Sandbox)
- Windows Sandbox
- QEMU/KVM-based isolation

Kernel Protection:

- PatchGuard (Windows Kernel Patch Protection)
- SELinux (Mandatory Access Control for Linux)
- AppArmor

## Workspace

- [[workspaces/attack/mitigations/M1025-privileged_process_integrity-note|Open workspace note]]

![[workspaces/attack/mitigations/M1025-privileged_process_integrity-note]]

## Mitigates Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547002-authentication-package|T1547.002: Authentication Package]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547005-security-support-provider|T1547.005: Security Support Provider]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547008-lsass-driver|T1547.008: LSASS Driver]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
    - [[T1556-modify_authentication_process#^t1556001-domain-controller-authentication|T1556.001: Domain Controller Authentication]]

