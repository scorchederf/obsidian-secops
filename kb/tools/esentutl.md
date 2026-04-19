---
id: S0404
name: esentutl
created: 2019-09-03 18:25:36.963000+00:00
modified: 2023-09-28 03:45:36.045000+00:00
type: tool
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

# esentutl

[esentutl](https://attack.mitre.org/software/S0404) is a command-line tool that provides database utilities for the Windows Extensible Storage Engine.(Citation: Microsoft Esentutl)

## Uses Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
    - [[T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]
- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1006-direct_volume_access|T1006: Direct Volume Access]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

