---
mitre_id: "TA0008"
mitre_name: "Lateral Movement"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--7141578b-e50b-4dcc-bfa4-08a8dd689e9e"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2025-08-11T19:25:08.016Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0008/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "lateral-movement"
---

# TA0008: Lateral Movement

The adversary is trying to move through your environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Following through on their primary objective often requires exploring the network to find their target, then pivoting through multiple systems and accounts to gain access to it. Adversaries might install their own remote access tools to accomplish Lateral Movement or use legitimate credentials with native network and operating system tools, which may be stealthier. 

## Related Techniques

- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
    - [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
    - [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]
    - [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]]
    - [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]
    - [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]
    - [[T1021-remote_services#^t1021007-cloud-services|T1021.007: Cloud Services]]
    - [[T1021-remote_services#^t1021008-direct-cloud-vm-connections|T1021.008: Direct Cloud VM Connections]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1080-taint_shared_content|T1080: Taint Shared Content]]
- [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
    - [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
    - [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
    - [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563001-ssh-hijacking|T1563.001: SSH Hijacking]]
    - [[T1563-remote_service_session_hijacking#^t1563002-rdp-hijacking|T1563.002: RDP Hijacking]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

## Workspace

- [[kb/notes/attack/tactics/ta0008-notes|Open workspace note]]

