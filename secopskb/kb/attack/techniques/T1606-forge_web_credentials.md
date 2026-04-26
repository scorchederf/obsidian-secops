---
mitre_id: "T1606"
mitre_name: "Forge Web Credentials"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--94cb00a4-b295-4d06-aa2b-5653b9c1be9c"
mitre_created: "2020-12-17T02:13:46.247Z"
mitre_modified: "2025-10-24T17:49:07.201Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1606/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "SaaS"
  - "Windows"
  - "macOS"
  - "Linux"
  - "IaaS"
  - "Office Suite"
  - "Identity Provider"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-ANCI"
  - "D3-CCSA"
  - "D3-CH"
  - "D3-CR"
  - "D3-CRO"
  - "D3-CTS"
  - "D3-DUC"
  - "D3-MFA"
  - "D3-RIC"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access.

Adversaries may generate these credential materials in order to gain access to web resources. This differs from [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]], [[T1528-steal_application_access_token|T1528: Steal Application Access Token]], and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted from legitimate users.

The generation of web credentials often requires secret values, such as passwords, [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]], or other cryptographic seed values.(Citation: GitHub AWS-ADFS-Credential-Generator) Adversaries may also forge tokens by taking advantage of features such as the `AssumeRole` and `GetFederationToken` APIs in AWS, which allow users to request temporary security credentials (i.e., [[T1548-abuse_elevation_control_mechanism#^t1548005-temporary-elevated-cloud-access|T1548.005: Temporary Elevated Cloud Access]]), or the `zmprov gdpak` command in Zimbra, which generates a pre-authentication key that can be used to generate tokens for any user in the domain.(Citation: AWS Temporary Security Credentials)(Citation: Zimbra Preauth)

Once forged, adversaries may use these web credentials to access resources (ex: [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Pass The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)(Citation: Microsoft SolarWinds Customer Guidance)  

## Workspace

- [[workspaces/attack/techniques/T1606-forge_web_credentials-note|Open workspace note]]

![[workspaces/attack/techniques/T1606-forge_web_credentials-note]]

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-ANCI-authentication_cache_invalidation|D3-ANCI: Authentication Cache Invalidation]]
- [[D3-CCSA-credential_compromise_scope_analysis|D3-CCSA: Credential Compromise Scope Analysis]]
- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]
- [[D3-CR-credential_revocation|D3-CR: Credential Revocation]]
- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]
- [[D3-CTS-credential_transmission_scoping|D3-CTS: Credential Transmission Scoping]]
- [[D3-DUC-decoy_user_credential|D3-DUC: Decoy User Credential]]
- [[D3-MFA-multi-factor_authentication|D3-MFA: Multi-factor Authentication]]
- [[D3-RIC-reissue_credential|D3-RIC: Reissue Credential]]

## Subtechniques

### T1606.001: Web Cookies

^t1606001-web-cookies

Adversaries may forge web cookies that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate and authorize user access.

Adversaries may generate these cookies in order to gain access to web resources. This differs from [[T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]] and other similar behaviors in that the cookies are new and forged by the adversary, rather than stolen or intercepted from legitimate users. Most common web applications have standardized and documented cookie values that can be generated using provided tools or interfaces.(Citation: Pass The Cookie) The generation of web cookies often requires secret values, such as passwords, [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]], or other cryptographic seed values.

Once forged, adversaries may use these web cookies to access resources ([[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]]), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Volexity SolarWinds)(Citation: Pass The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)

### T1606.002: SAML Tokens

^t1606002-saml-tokens

An adversary may forge SAML tokens with any permissions claims and lifetimes if they possess a valid SAML token-signing certificate.(Citation: Microsoft SolarWinds Steps) The default lifetime of a SAML token is one hour, but the validity period can be specified in the `NotOnOrAfter` value of the `conditions ...` element in a token. This value can be changed using the `AccessTokenLifetime` in a `LifetimeTokenPolicy`.(Citation: Microsoft SAML Token Lifetimes) Forged SAML tokens enable adversaries to authenticate across services that use SAML 2.0 as an SSO (single sign-on) mechanism.(Citation: Cyberark Golden SAML)

An adversary may utilize [[T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]] to compromise an organization's token-signing certificate to create forged SAML tokens. If the adversary has sufficient permissions to establish a new federation trust with their own Active Directory Federation Services (AD FS) server, they may instead generate their own trusted token-signing certificate.(Citation: Microsoft SolarWinds Customer Guidance) This differs from [[T1528-steal_application_access_token|T1528: Steal Application Access Token]] and other similar behaviors in that the tokens are new and forged by the adversary, rather than stolen or intercepted from legitimate users.

An adversary may gain administrative Entra ID privileges if a SAML token is forged which claims to represent a highly privileged account. This may lead to [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]], which may bypass multi-factor and other authentication protection mechanisms.(Citation: Microsoft SolarWinds Customer Guidance)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1047-audit|M1047: Audit]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- SaaS
- Windows
- macOS
- Linux
- IaaS
- Office Suite
- Identity Provider

