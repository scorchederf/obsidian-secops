---
id: T1182
name: AppCert DLLs
created: 2018-01-16 16:13:52.465000+00:00
modified: 2025-10-24 17:48:44.956000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[privilege_escalation|Privilege Escalation]]

Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs Registry key under <code>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager</code> are loaded into every process that calls the ubiquitously used application programming interface (API) functions CreateProcess, CreateProcessAsUser, CreateProcessWithLoginW, CreateProcessWithTokenW, or WinExec. (Citation: Elastic Process Injection July 2017)

Similar to [Process Injection](https://attack.mitre.org/techniques/T1055), this value can be abused to obtain persistence and privilege escalation by causing a malicious DLL to be loaded and run in the context of separate processes on the computer.

## Platforms

- Windows

