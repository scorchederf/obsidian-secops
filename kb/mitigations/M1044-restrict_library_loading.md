---
mitre_id: "M1044"
mitre_name: "Restrict Library Loading"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--e8242a33-481c-4891-af63-4cf3e4cf6aff"
mitre_created: "2019-06-11T17:00:01.740Z"
mitre_modified: "2024-12-18T20:22:48.602Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1044/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# M1044: Restrict Library Loading

Restricting library loading involves implementing security controls to ensure that only trusted and verified libraries (DLLs, shared objects, etc.) are loaded into processes. Adversaries often abuse Dynamic-Link Library (DLL) Injection, DLL Search Order Hijacking, or LD_PRELOAD mechanisms to execute malicious code by forcing the operating system to load untrusted libraries. This mitigation can be implemented through the following measures: 

Enforce Safe Library Loading Practices:

- Enable `SafeDLLSearchMode` on Windows.
- Restrict `LD_PRELOAD` and `LD_LIBRARY_PATH` usage on Linux systems.

Code Signing Enforcement:

- Require digital signatures for all libraries loaded into processes.
- Use tools like Signtool, and WDAC to enforce signed DLL execution.

Environment Hardening:

- Secure library paths and directories to prevent adversaries from placing rogue libraries.
- Monitor user-writable directories and system configurations for unauthorized changes.

Audit and Monitor Library Loading:

- Enable `Sysmon` on Windows to monitor for suspicious library loads.
- Use `auditd` on Linux to monitor shared library paths and configuration file changes.

Use Application Control Solutions:

- Implement AppLocker, WDAC, or SELinux to allow only trusted libraries.

*Tools for Implementation*

Windows-Specific Tools:

- AppLocker: Application whitelisting for DLLs.
- Windows Defender Application Control (WDAC): Restrict unauthorized library execution.
- Signtool: Verify and enforce code signing.
- Sysmon: Monitor DLL load events (Event ID 7).

Linux-Specific Tools:

- auditd: Monitor changes to library paths and critical files.
- SELinux/AppArmor: Define policies to restrict library loading.
- ldconfig and chattr: Secure LD configuration files and prevent unauthorized modifications.

Cross-Platform Solutions:

- Wazuh or OSSEC: File integrity monitoring for library changes.
- Tripwire: Detect and alert on unauthorized library modifications.

## Mitigates Techniques

- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
    - [[T1547-boot_or_logon_autostart_execution#^t1547008-lsass-driver|T1547.008: LSASS Driver]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
    - [[T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

