---
mitre_id: "T1649"
mitre_name: "Steal or Forge Authentication Certificates"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7de1f7ac-5d0c-4c9c-8873-627202205331"
mitre_created: "2022-08-03T03:20:58.955Z"
mitre_modified: "2025-04-15T23:12:50.646Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1649/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Identity Provider"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-AVE"
  - "D3-CA"
  - "D3-CBAN"
  - "D3-CERO"
  - "D3-CF"
  - "D3-CM"
  - "D3-CP"
  - "D3-CQ"
  - "D3-DF"
  - "D3-FA"
  - "D3-FE"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-LFP"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RS"
  - "D3-SBV"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may steal or forge certificates used for authentication to access remote systems or resources. Digital certificates are often used to sign and encrypt messages and/or files. Certificates are also used as authentication material. For example, Entra ID device certificates and Active Directory Certificate Services (AD CS) certificates bind to an identity and can be used as credentials for domain accounts.(Citation: O365 Blog Azure AD Device IDs)(Citation: Microsoft AD CS Overview)

Authentication certificates can be both stolen and forged. For example, AD CS certificates can be stolen from encrypted storage (in the Registry or files)(Citation: APT29 Deep Look at Credential Roaming), misplaced certificate files (i.e. [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]), or directly from the Windows certificate store via various crypto APIs.(Citation: SpecterOps Certified Pre Owned)(Citation: GitHub CertStealer)(Citation: GitHub GhostPack Certificates) With appropriate enrollment rights, users and/or machines within a domain can also request and/or manually renew certificates from enterprise certificate authorities (CA). This enrollment process defines various settings and permissions associated with the certificate. Of note, the certificate’s extended key usage (EKU) values define signing, encryption, and authentication use cases, while the certificate’s subject alternative name (SAN) values define the certificate owner’s alternate names.(Citation: Medium Certified Pre Owned)

Abusing certificates for authentication credentials may enable other behaviors such as [[TA0008-lateral_movement|TA0008: Lateral Movement]]. Certificate-related misconfigurations may also enable opportunities for [[TA0004-privilege_escalation|TA0004: Privilege Escalation]], by way of allowing users to impersonate or assume privileged accounts or permissions via the identities (SANs) associated with a certificate. These abuses may also enable [[TA0003-persistence|TA0003: Persistence]] via stealing or forging certificates that can be used as [[T1078-valid_accounts|T1078: Valid Accounts]] for the duration of the certificate's validity, despite user password resets. Authentication certificates can also be stolen and forged for machine accounts.

Adversaries who have access to root (or subordinate) CA certificate private keys (or mechanisms protecting/managing these keys) may also establish [[TA0003-persistence|TA0003: Persistence]] by forging arbitrary authentication certificates for the victim domain (known as “golden” certificates).(Citation: Medium Certified Pre Owned) Adversaries may also target certificates and related services in order to access other forms of credentials, such as [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]] ticket-granting tickets (TGT) or NTLM plaintext.(Citation: Medium Certified Pre Owned)

## Workspace

- [[workspaces/attack/techniques/T1649-steal_or_forge_authentication_certificates-note|Open workspace note]]

![[workspaces/attack/techniques/T1649-steal_or_forge_authentication_certificates-note]]

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-CA-certificate_analysis|D3-CA: Certificate Analysis]]
- [[D3-CBAN-certificate-based_authentication|D3-CBAN: Certificate-based Authentication]]
- [[D3-CERO-certificate_rotation|D3-CERO: Certificate Rotation]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CP-certificate_pinning|D3-CP: Certificate Pinning]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SBV-service_binary_verification|D3-SBV: Service Binary Verification]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Mitigations

- [[M1015-active_directory_configuration|M1015: Active Directory Configuration]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1047-audit|M1047: Audit]]

## Tools

- [[mimikatz|Mimikatz (S0002)]]
- [[aadinternals|AADInternals (S0677)]]

## Platforms

- Windows
- Linux
- macOS
- Identity Provider

