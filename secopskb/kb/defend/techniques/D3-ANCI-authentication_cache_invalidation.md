---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ANCI"
d3fend_name: "Authentication Cache Invalidation"
d3fend_ontology_id: "d3f:AuthenticationCacheInvalidation"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AAuthenticationCacheInvalidation/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.003"
  - "T1003.005"
  - "T1003.008"
  - "T1098"
  - "T1098.001"
  - "T1110"
  - "T1110.001"
  - "T1110.002"
  - "T1110.003"
  - "T1134"
  - "T1134.001"
  - "T1134.002"
  - "T1134.003"
  - "T1528"
  - "T1539"
  - "T1550"
  - "T1550.001"
  - "T1550.004"
  - "T1552"
  - "T1552.001"
  - "T1552.002"
  - "T1552.003"
  - "T1552.004"
  - "T1552.005"
  - "T1552.006"
  - "T1552.007"
  - "T1552.008"
  - "T1558"
  - "T1558.001"
  - "T1558.002"
  - "T1558.003"
  - "T1558.004"
  - "T1558.005"
  - "T1606"
  - "T1606.001"
  - "T1606.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Removing tokens or credentials from an authentication cache to prevent further user associated account accesses.

## Workspace

- [[workspaces/defend/techniques/D3-ANCI-authentication_cache_invalidation-note|Open workspace note]]

![[workspaces/defend/techniques/D3-ANCI-authentication_cache_invalidation-note]]

## Parent Technique

- [[D3-CE-credential_eviction|D3-CE: Credential Eviction]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]
- [[T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]
- [[T1003-os_credential_dumping#^t1003008--etc-passwd-and--etc-shadow|T1003.008: /etc/passwd and /etc/shadow]]
- [[T1098-account_manipulation|T1098: Account Manipulation]]
- [[T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]
- [[T1110-brute_force#^t1110002-password-cracking|T1110.002: Password Cracking]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]
- [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]
- [[T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]]
- [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
- [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
- [[T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]
- [[T1552-unsecured_credentials#^t1552003-shell-history|T1552.003: Shell History]]
- [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]
- [[T1552-unsecured_credentials#^t1552005-cloud-instance-metadata-api|T1552.005: Cloud Instance Metadata API]]
- [[T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]
- [[T1552-unsecured_credentials#^t1552007-container-api|T1552.007: Container API]]
- [[T1552-unsecured_credentials#^t1552008-chat-messages|T1552.008: Chat Messages]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558002-silver-ticket|T1558.002: Silver Ticket]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558004-as-rep-roasting|T1558.004: AS-REP Roasting]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558005-ccache-files|T1558.005: Ccache Files]]
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]
- [[T1606-forge_web_credentials#^t1606001-web-cookies|T1606.001: Web Cookies]]
- [[T1606-forge_web_credentials#^t1606002-saml-tokens|T1606.002: SAML Tokens]]

## Knowledge Base Article

## How it works
Applications can locally cache user authentication credentials for certain server connections. An application may attempt to use the cached credential for a connection. If the cached credentials exist then the user will not be typically prompted for new credentials.


## Considerations
Are these cached credentials only on the local host? Can they be persisted to the remote server?

## Examples
Windows Credential Management API

## Ontology Relationships

- [[D3-CE-credential_eviction|D3-CE: Credential Eviction]]

