---
mitre_id: "S0349"
mitre_name: "LaZagne"
mitre_type: "tool"
mitre_stix_id: "tool--b76b2d94-60e4-4107-a903-4a3a7622fb3b"
mitre_created: "2019-01-30T16:44:59.887Z"
mitre_modified: "2024-04-04T03:49:27.035Z"
mitre_version: "1.6"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0349/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_aliases:
  - "LaZagne"
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
- [[T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
    - [[T1555-credentials_from_password_stores#^t1555001-keychain|T1555.001: Keychain]]
    - [[T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
    - [[T1555-credentials_from_password_stores#^t1555004-windows-credential-manager|T1555.004: Windows Credential Manager]]

