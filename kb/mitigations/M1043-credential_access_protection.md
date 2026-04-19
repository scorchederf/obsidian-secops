---
id: M1043
name: Credential Access Protection
created: 2019-06-11 16:47:12.859000+00:00
modified: 2024-12-10 18:55:27.646000+00:00
type: course-of-action
---

# Credential Access Protection

Credential Access Protection focuses on implementing measures to prevent adversaries from obtaining credentials, such as passwords, hashes, tokens, or keys, that could be used for unauthorized access. This involves restricting access to credential storage mechanisms, hardening configurations to block credential dumping methods, and using monitoring tools to detect suspicious credential-related activity. This mitigation can be implemented through the following measures:

Restrict Access to Credential Storage:

- Use Case: Prevent adversaries from accessing the SAM (Security Account Manager) database on Windows systems.
- Implementation: Enforce least privilege principles and restrict administrative access to credential stores such as `C:\Windows\System32\config\SAM`.

Use Credential Guard:

- Use Case: Isolate LSASS (Local Security Authority Subsystem Service) memory to prevent credential dumping.
- Implementation: Enable Windows Defender Credential Guard on enterprise endpoints to isolate secrets and protect them from unauthorized access.

Monitor for Credential Dumping Tools:

- Use Case: Detect and block known tools like Mimikatz or Windows Credential Editor.
- Implementation: Flag suspicious process behavior related to credential dumping.

Disable Cached Credentials:

- Use Case: Prevent adversaries from exploiting cached credentials on endpoints.
- Implementation: Configure group policy to reduce or eliminate the use of cached credentials (e.g., set Interactive logon: Number of previous logons to cache to 0).

Enable Secure Boot and Memory Protections:

- Use Case: Prevent memory-based attacks used to extract credentials.
- Implementation: Configure Secure Boot and enforce hardware-based security features like DEP (Data Execution Prevention) and ASLR (Address Space Layout Randomization).

## Mitigates Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547008-lsass-driver|T1547.008: LSASS Driver]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
    - [[T1558-steal_or_forge_kerberos_tickets#^t1558005-ccache-files|T1558.005: Ccache Files]]
- [[T1599-network_boundary_bridging|T1599: Network Boundary Bridging]]
    - [[T1599-network_boundary_bridging#^t1599001-network-address-translation-traversal|T1599.001: Network Address Translation Traversal]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
    - [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]]
    - [[T1601-modify_system_image#^t1601002-downgrade-system-image|T1601.002: Downgrade System Image]]

