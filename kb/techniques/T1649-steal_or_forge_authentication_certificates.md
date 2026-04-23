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
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "Linux"
  - "macOS"
  - "Identity Provider"
mitre_tactic_ids:
  - "TA0006"
---

# T1649: Steal or Forge Authentication Certificates

Adversaries may steal or forge certificates used for authentication to access remote systems or resources. Digital certificates are often used to sign and encrypt messages and/or files. Certificates are also used as authentication material. For example, Entra ID device certificates and Active Directory Certificate Services (AD CS) certificates bind to an identity and can be used as credentials for domain accounts.(Citation: O365 Blog Azure AD Device IDs)(Citation: Microsoft AD CS Overview)

Authentication certificates can be both stolen and forged. For example, AD CS certificates can be stolen from encrypted storage (in the Registry or files)(Citation: APT29 Deep Look at Credential Roaming), misplaced certificate files (i.e. [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]), or directly from the Windows certificate store via various crypto APIs.(Citation: SpecterOps Certified Pre Owned)(Citation: GitHub CertStealer)(Citation: GitHub GhostPack Certificates) With appropriate enrollment rights, users and/or machines within a domain can also request and/or manually renew certificates from enterprise certificate authorities (CA). This enrollment process defines various settings and permissions associated with the certificate. Of note, the certificate’s extended key usage (EKU) values define signing, encryption, and authentication use cases, while the certificate’s subject alternative name (SAN) values define the certificate owner’s alternate names.(Citation: Medium Certified Pre Owned)

Abusing certificates for authentication credentials may enable other behaviors such as [[TA0008-lateral_movement|TA0008: Lateral Movement]]. Certificate-related misconfigurations may also enable opportunities for [[TA0004-privilege_escalation|TA0004: Privilege Escalation]], by way of allowing users to impersonate or assume privileged accounts or permissions via the identities (SANs) associated with a certificate. These abuses may also enable [[TA0003-persistence|TA0003: Persistence]] via stealing or forging certificates that can be used as [[T1078-valid_accounts|T1078: Valid Accounts]] for the duration of the certificate's validity, despite user password resets. Authentication certificates can also be stolen and forged for machine accounts.

Adversaries who have access to root (or subordinate) CA certificate private keys (or mechanisms protecting/managing these keys) may also establish [[TA0003-persistence|TA0003: Persistence]] by forging arbitrary authentication certificates for the victim domain (known as “golden” certificates).(Citation: Medium Certified Pre Owned) Adversaries may also target certificates and related services in order to access other forms of credentials, such as [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]] ticket-granting tickets (TGT) or NTLM plaintext.(Citation: Medium Certified Pre Owned)

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## Mitigations

- [[M1015-active_directory_configuration|M1015: Active Directory Configuration]]
- [[M1041-encrypt_sensitive_information|M1041: Encrypt Sensitive Information]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]
- [[M1047-audit|M1047: Audit]]

## Tools

- [[mimikatz|Mimikatz]]
- [[aadinternals|AADInternals]]

## Platforms

- Windows
- Linux
- macOS
- Identity Provider

