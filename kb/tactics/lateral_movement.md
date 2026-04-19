---
id: x-mitre-tactic--7141578b-e50b-4dcc-bfa4-08a8dd689e9e
name: Lateral Movement
created: 2018-10-17 00:14:20.652000+00:00
modified: 2025-08-11 19:25:08.016000+00:00
type: x-mitre-tactic
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

# Lateral Movement

The adversary is trying to move through your environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Following through on their primary objective often requires exploring the network to find their target, then pivoting through multiple systems and accounts to gain access to it. Adversaries might install their own remote access tools to accomplish Lateral Movement or use legitimate credentials with native network and operating system tools, which may be stealthier. 

## Related Techniques

- [[T1017-application_deployment_software|T1017: Application Deployment Software]]
- [[T1021-remote_services|T1021: Remote Services]]
    - [[T1021-remote_services#^t1021001-remote-desktop-protocol|T1021.001: Remote Desktop Protocol]]
    - [[T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
    - [[T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]
    - [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]]
    - [[T1021-remote_services#^t1021005-vnc|T1021.005: VNC]]
    - [[T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]
    - [[T1021-remote_services#^t1021007-cloud-services|T1021.007: Cloud Services]]
    - [[T1021-remote_services#^t1021008-direct-cloud-vm-connections|T1021.008: Direct Cloud VM Connections]]
- [[T1028-windows_remote_management|T1028: Windows Remote Management]]
- [[T1051-shared_webroot|T1051: Shared Webroot]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1075-pass_the_hash|T1075: Pass the Hash]]
- [[T1076-remote_desktop_protocol|T1076: Remote Desktop Protocol]]
- [[T1077-windows_admin_shares|T1077: Windows Admin Shares]]
- [[T1080-taint_shared_content|T1080: Taint Shared Content]]
- [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]
- [[T1097-pass_the_ticket|T1097: Pass the Ticket]]
- [[T1175-component_object_model_and_distributed_com|T1175: Component Object Model and Distributed COM]]
- [[T1184-ssh_hijacking|T1184: SSH Hijacking]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1506-web_session_cookie|T1506: Web Session Cookie]]
- [[T1527-application_access_token|T1527: Application Access Token]]
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
