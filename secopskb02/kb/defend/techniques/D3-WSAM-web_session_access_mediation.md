---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-WSAM"
d3fend_name: "Web Session Access Mediation"
d3fend_ontology_id: "d3f:WebSessionAccessMediation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AWebSessionAccessMediation/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
  - "T1003.002"
  - "T1033"
  - "T1212"
  - "T1505"
  - "T1505.002"
  - "T1550"
  - "T1550.001"
  - "T1550.002"
  - "T1550.003"
  - "T1550.004"
  - "T1556"
  - "T1556.001"
  - "T1556.002"
  - "T1556.003"
  - "T1556.004"
  - "T1556.005"
  - "T1556.006"
  - "T1556.007"
  - "T1556.008"
  - "T1556.009"
  - "T1621"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Web session access mediation secures user sessions in web applications by employing robust authentication and integrity validation, along with adaptive threat mitigation techniques, to ensure that access to web resources is authorized and protected from session-related attacks.

## Workspace

- [[workspaces/defend/techniques/D3-WSAM-web_session_access_mediation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-WSAM-web_session_access_mediation-note]]

## Parent Technique

- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]

## Child Techniques

- [[D3-EBWSAM-endpoint-based_web_server_access_mediation|D3-EBWSAM: Endpoint-based Web Server Access Mediation]]
- [[D3-PBWSAM-proxy-based_web_server_access_mediation|D3-PBWSAM: Proxy-based Web Server Access Mediation]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]
- [[T1550-use_alternate_authentication_material#^t1550003-pass-the-ticket|T1550.003: Pass the Ticket]]
- [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process#^t1556001-domain-controller-authentication|T1556.001: Domain Controller Authentication]]
- [[T1556-modify_authentication_process#^t1556002-password-filter-dll|T1556.002: Password Filter DLL]]
- [[T1556-modify_authentication_process#^t1556003-pluggable-authentication-modules|T1556.003: Pluggable Authentication Modules]]
- [[T1556-modify_authentication_process#^t1556004-network-device-authentication|T1556.004: Network Device Authentication]]
- [[T1556-modify_authentication_process#^t1556005-reversible-encryption|T1556.005: Reversible Encryption]]
- [[T1556-modify_authentication_process#^t1556006-multi-factor-authentication|T1556.006: Multi-Factor Authentication]]
- [[T1556-modify_authentication_process#^t1556007-hybrid-identity|T1556.007: Hybrid Identity]]
- [[T1556-modify_authentication_process#^t1556008-network-provider-dll|T1556.008: Network Provider DLL]]
- [[T1556-modify_authentication_process#^t1556009-conditional-access-policies|T1556.009: Conditional Access Policies]]
- [[T1621-multi-factor_authentication_request_generation|T1621: Multi-Factor Authentication Request Generation]]

## Knowledge Base Article

## How it works

Web Session Access Mediation involves managing user access to web applications and services, ensuring secure and authorized sessions. This includes authenticating users, maintaining session integrity, and protecting against threats like session hijacking. Examples include accessing corporate intranets, SaaS applications, or online portals.

## Ontology Relationships

- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]

