---
mitre_id: "TA0009"
mitre_name: "Collection"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--d108ce10-2419-4cf9-a774-46161d6c6cfe"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2024-09-05T18:27:09.070Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0009/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "collection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

The adversary is trying to gather data of interest to their goal.

Collection consists of techniques adversaries may use to gather information and the sources information is collected from that are relevant to following through on the adversary's objectives. Frequently, the next goal after collecting data is to either steal (exfiltrate) the data or to use the data to gain more information about the target environment. Common target sources include various drive types, browsers, audio, video, and email. Common collection methods include capturing screenshots and keyboard input.

## Workspace

- [[workspaces/attack/tactics/TA0009-collection-note|Open workspace note]]

![[workspaces/attack/tactics/TA0009-collection-note]]

## Related Techniques

- [[T1005-data_from_local_system|T1005: Data from Local System]]
- [[T1025-data_from_removable_media|T1025: Data from Removable Media]]
- [[T1039-data_from_network_shared_drive|T1039: Data from Network Shared Drive]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
    - [[T1056-input_capture#^t1056002-gui-input-capture|T1056.002: GUI Input Capture]]
    - [[T1056-input_capture#^t1056003-web-portal-capture|T1056.003: Web Portal Capture]]
    - [[T1056-input_capture#^t1056004-credential-api-hooking|T1056.004: Credential API Hooking]]
- [[T1074-data_staged|T1074: Data Staged]]
    - [[T1074-data_staged#^t1074001-local-data-staging|T1074.001: Local Data Staging]]
    - [[T1074-data_staged#^t1074002-remote-data-staging|T1074.002: Remote Data Staging]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1114-email_collection|T1114: Email Collection]]
    - [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
    - [[T1114-email_collection#^t1114002-remote-email-collection|T1114.002: Remote Email Collection]]
    - [[T1114-email_collection#^t1114003-email-forwarding-rule|T1114.003: Email Forwarding Rule]]
- [[T1115-clipboard_data|T1115: Clipboard Data]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1125-video_capture|T1125: Video Capture]]
- [[T1185-browser_session_hijacking|T1185: Browser Session Hijacking]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
    - [[T1213-data_from_information_repositories#^t1213001-confluence|T1213.001: Confluence]]
    - [[T1213-data_from_information_repositories#^t1213002-sharepoint|T1213.002: Sharepoint]]
    - [[T1213-data_from_information_repositories#^t1213003-code-repositories|T1213.003: Code Repositories]]
    - [[T1213-data_from_information_repositories#^t1213004-customer-relationship-management-software|T1213.004: Customer Relationship Management Software]]
    - [[T1213-data_from_information_repositories#^t1213005-messaging-applications|T1213.005: Messaging Applications]]
    - [[T1213-data_from_information_repositories#^t1213006-databases|T1213.006: Databases]]
- [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]
    - [[T1557-adversary-in-the-middle#^t1557002-arp-cache-poisoning|T1557.002: ARP Cache Poisoning]]
    - [[T1557-adversary-in-the-middle#^t1557003-dhcp-spoofing|T1557.003: DHCP Spoofing]]
    - [[T1557-adversary-in-the-middle#^t1557004-evil-twin|T1557.004: Evil Twin]]
- [[T1560-archive_collected_data|T1560: Archive Collected Data]]
    - [[T1560-archive_collected_data#^t1560001-archive-via-utility|T1560.001: Archive via Utility]]
    - [[T1560-archive_collected_data#^t1560002-archive-via-library|T1560.002: Archive via Library]]
    - [[T1560-archive_collected_data#^t1560003-archive-via-custom-method|T1560.003: Archive via Custom Method]]
- [[T1602-data_from_configuration_repository|T1602: Data from Configuration Repository]]
    - [[T1602-data_from_configuration_repository#^t1602001-snmp-(mib-dump)|T1602.001: SNMP (MIB Dump)]]
    - [[T1602-data_from_configuration_repository#^t1602002-network-device-configuration-dump|T1602.002: Network Device Configuration Dump]]

