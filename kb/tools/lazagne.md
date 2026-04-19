---
id: S0349
name: LaZagne
created: 2019-01-30 16:44:59.887000+00:00
modified: 2024-04-04 03:49:27.035000+00:00
type: tool
x_mitre_version: 1.6
x_mitre_domains: enterprise-attack
---

# LaZagne

[LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018)

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
    - [[T1003-os_credential_dumping#^t1003004-lsa-secrets|T1003.004: LSA Secrets]]
    - [[T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]
    - [[T1003-os_credential_dumping#^t1003007-proc-filesystem|T1003.007: Proc Filesystem]]
    - [[T1003-os_credential_dumping#^t1003008--etc-passwd-and--etc-shadow|T1003.008: /etc/passwd and /etc/shadow]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555001-keychain|T1555.001: Keychain]]
    - [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
    - [[T1555-credentials_from_password_stores#^t1555004-windows-credential-manager|T1555.004: Windows Credential Manager]]

