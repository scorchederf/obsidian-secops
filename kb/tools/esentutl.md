---
mitre_id: "S0404"
mitre_name: "esentutl"
mitre_type: "tool"
mitre_stix_id: "tool--c256da91-6dd5-40b2-beeb-ee3b22ab3d27"
mitre_created: "2019-09-03T18:25:36.963Z"
mitre_modified: "2023-09-28T03:45:36.045Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0404/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_aliases:
  - "esentutl"
  - "esentutl.exe"
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

