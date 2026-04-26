---
mitre_id: "TA0040"
mitre_name: "Impact"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--5569339b-94c2-49ee-afb3-2222936582c8"
mitre_created: "2019-03-14T18:44:44.639Z"
mitre_modified: "2025-04-25T14:45:33.130Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0040/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "impact"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

The adversary is trying to manipulate, interrupt, or destroy your systems and data.
 
Impact consists of techniques that adversaries use to disrupt availability or compromise integrity by manipulating business and operational processes. Techniques used for impact can include destroying or tampering with data. In some cases, business processes can look fine, but may have been altered to benefit the adversaries’ goals. These techniques might be used by adversaries to follow through on their end goal or to provide cover for a confidentiality breach.

## Workspace

- [[workspaces/attack/tactics/TA0040-impact-note|Open workspace note]]

![[workspaces/attack/tactics/TA0040-impact-note]]

## Related Techniques

- [[T1485-data_destruction|T1485: Data Destruction]]
    - [[T1485-data_destruction#^t1485001-lifecycle-triggered-deletion|T1485.001: Lifecycle-Triggered Deletion]]
- [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]
- [[T1489-service_stop|T1489: Service Stop]]
- [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]
- [[T1491-defacement|T1491: Defacement]]
    - [[T1491-defacement#^t1491001-internal-defacement|T1491.001: Internal Defacement]]
    - [[T1491-defacement#^t1491002-external-defacement|T1491.002: External Defacement]]
- [[T1495-firmware_corruption|T1495: Firmware Corruption]]
- [[T1496-resource_hijacking|T1496: Resource Hijacking]]
    - [[T1496-resource_hijacking#^t1496001-compute-hijacking|T1496.001: Compute Hijacking]]
    - [[T1496-resource_hijacking#^t1496002-bandwidth-hijacking|T1496.002: Bandwidth Hijacking]]
    - [[T1496-resource_hijacking#^t1496003-sms-pumping|T1496.003: SMS Pumping]]
    - [[T1496-resource_hijacking#^t1496004-cloud-service-hijacking|T1496.004: Cloud Service Hijacking]]
- [[T1498-network_denial_of_service|T1498: Network Denial of Service]]
    - [[T1498-network_denial_of_service#^t1498001-direct-network-flood|T1498.001: Direct Network Flood]]
    - [[T1498-network_denial_of_service#^t1498002-reflection-amplification|T1498.002: Reflection Amplification]]
- [[T1499-endpoint_denial_of_service|T1499: Endpoint Denial of Service]]
    - [[T1499-endpoint_denial_of_service#^t1499001-os-exhaustion-flood|T1499.001: OS Exhaustion Flood]]
    - [[T1499-endpoint_denial_of_service#^t1499002-service-exhaustion-flood|T1499.002: Service Exhaustion Flood]]
    - [[T1499-endpoint_denial_of_service#^t1499003-application-exhaustion-flood|T1499.003: Application Exhaustion Flood]]
    - [[T1499-endpoint_denial_of_service#^t1499004-application-or-system-exploitation|T1499.004: Application or System Exploitation]]
- [[T1529-system_shutdown_reboot|T1529: System Shutdown/Reboot]]
- [[T1531-account_access_removal|T1531: Account Access Removal]]
- [[T1561-disk_wipe|T1561: Disk Wipe]]
    - [[T1561-disk_wipe#^t1561001-disk-content-wipe|T1561.001: Disk Content Wipe]]
    - [[T1561-disk_wipe#^t1561002-disk-structure-wipe|T1561.002: Disk Structure Wipe]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
    - [[T1565-data_manipulation#^t1565001-stored-data-manipulation|T1565.001: Stored Data Manipulation]]
    - [[T1565-data_manipulation#^t1565002-transmitted-data-manipulation|T1565.002: Transmitted Data Manipulation]]
    - [[T1565-data_manipulation#^t1565003-runtime-data-manipulation|T1565.003: Runtime Data Manipulation]]
- [[T1657-financial_theft|T1657: Financial Theft]]
- [[T1667-email_bombing|T1667: Email Bombing]]

