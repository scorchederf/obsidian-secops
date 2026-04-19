---
id: T1606
name: Forge Web Credentials
created: 2020-12-17 02:13:46.247000+00:00
modified: 2025-10-24 17:49:07.201000+00:00
type: attack-pattern
x_mitre_version: 1.5
x_mitre_domains: enterprise-attack
---

## Tactic

- [[credential_access|Credential Access]]

Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access.

Adversaries may generate these credential materials in order to gain access to web resources. This differs from [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539), [Steal Application Access Token](https://attack.mitre.org/techniques/T1528), and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted from legitimate users.

The generation of web credentials often requires secret values, such as passwords, [Private Keys](https://attack.mitre.org/techniques/T1552/004), or other cryptographic seed values.(Citation: GitHub AWS-ADFS-Credential-Generator) Adversaries may also forge tokens by taking advantage of features such as the `AssumeRole` and `GetFederationToken` APIs in AWS, which allow users to request temporary security credentials (i.e., [Temporary Elevated Cloud Access](https://attack.mitre.org/techniques/T1548/005)), or the `zmprov gdpak` command in Zimbra, which generates a pre-authentication key that can be used to generate tokens for any user in the domain.(Citation: AWS Temporary Security Credentials)(Citation: Zimbra Preauth)

Once forged, adversaries may use these web credentials to access resources (ex: [Use Alternate Authentication Material](https://attack.mitre.org/techniques/T1550)), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Pass The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)(Citation: Microsoft SolarWinds Customer Guidance)  

## Subtechniques

### T1606.001: Web Cookies
^t1606001-web-cookies

**Parent Technique**
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]

**Tactic**
- [[credential_access|Credential Access]]

Adversaries may forge web cookies that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate and authorize user access.

Adversaries may generate these cookies in order to gain access to web resources. This differs from [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539) and other similar behaviors in that the cookies are new and forged by the adversary, rather than stolen or intercepted from legitimate users. Most common web applications have standardized and documented cookie values that can be generated using provided tools or interfaces.(Citation: Pass The Cookie) The generation of web cookies often requires secret values, such as passwords, [Private Keys](https://attack.mitre.org/techniques/T1552/004), or other cryptographic seed values.

Once forged, adversaries may use these web cookies to access resources ([Web Session Cookie](https://attack.mitre.org/techniques/T1550/004)), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Volexity SolarWinds)(Citation: Pass The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)

#### Properties

- id: T1606.001
- name: Web Cookies
- created: 2020-12-17 02:14:34.178000+00:00
- modified: 2025-10-24 17:49:04.036000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1606.002: SAML Tokens
^t1606002-saml-tokens

**Parent Technique**
- [[T1606-forge_web_credentials|T1606: Forge Web Credentials]]

**Tactic**
- [[credential_access|Credential Access]]

An adversary may forge SAML tokens with any permissions claims and lifetimes if they possess a valid SAML token-signing certificate.(Citation: Microsoft SolarWinds Steps) The default lifetime of a SAML token is one hour, but the validity period can be specified in the <code>NotOnOrAfter</code> value of the <code>conditions ...</code> element in a token. This value can be changed using the <code>AccessTokenLifetime</code> in a <code>LifetimeTokenPolicy</code>.(Citation: Microsoft SAML Token Lifetimes) Forged SAML tokens enable adversaries to authenticate across services that use SAML 2.0 as an SSO (single sign-on) mechanism.(Citation: Cyberark Golden SAML)

An adversary may utilize [Private Keys](https://attack.mitre.org/techniques/T1552/004) to compromise an organization's token-signing certificate to create forged SAML tokens. If the adversary has sufficient permissions to establish a new federation trust with their own Active Directory Federation Services (AD FS) server, they may instead generate their own trusted token-signing certificate.(Citation: Microsoft SolarWinds Customer Guidance) This differs from [Steal Application Access Token](https://attack.mitre.org/techniques/T1528) and other similar behaviors in that the tokens are new and forged by the adversary, rather than stolen or intercepted from legitimate users.

An adversary may gain administrative Entra ID privileges if a SAML token is forged which claims to represent a highly privileged account. This may lead to [Use Alternate Authentication Material](https://attack.mitre.org/techniques/T1550), which may bypass multi-factor and other authentication protection mechanisms.(Citation: Microsoft SolarWinds Customer Guidance)

#### Properties

- id: T1606.002
- name: SAML Tokens
- created: 2020-12-17 15:24:12.240000+00:00
- modified: 2025-10-24 17:48:30.302000+00:00
- type: attack-pattern
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

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

