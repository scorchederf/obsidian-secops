---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-TBA"
d3fend_name: "Token-based Authentication"
d3fend_ontology_id: "d3f:Token-basedAuthentication"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AToken-basedAuthentication/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1134"
  - "T1134.001"
  - "T1134.002"
  - "T1134.003"
  - "T1528"
  - "T1550"
  - "T1550.001"
  - "T1558"
  - "T1558.001"
  - "T1558.002"
  - "T1558.003"
  - "T1558.004"
  - "T1558.005"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Token-based authentication is an authentication protocol where users verify their identity in exchange for a unique access token. Users can then access the website, application, or resource for the life of the token without having to re-enter their credentials.

## Workspace

- [[workspaces/defend/techniques/D3-TBA-token-based_authentication-note|Open workspace note]]

![[workspaces/defend/techniques/D3-TBA-token-based_authentication-note]]

## Parent Technique

- [[D3-AA-agent_authentication|D3-AA: Agent Authentication]]

## Related ATT&CK Techniques

- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]
- [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]
- [[T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]]
- [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
- [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1558-steal_or_forge_kerberos_tickets|T1558: Steal or Forge Kerberos Tickets]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558001-golden-ticket|T1558.001: Golden Ticket]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558002-silver-ticket|T1558.002: Silver Ticket]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558003-kerberoasting|T1558.003: Kerberoasting]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558004-as-rep-roasting|T1558.004: AS-REP Roasting]]
- [[T1558-steal_or_forge_kerberos_tickets#^t1558005-ccache-files|T1558.005: Ccache Files]]

## Knowledge Base Article

## How it works

Token-based authentication starts with a user logging into a system, device or application, typically using a password or a security question. An authorization server validates that initial authentication and then issues an access token, which is a small piece of data that lets a client application make a secure call or signal to an API server. Once this initial token-based authentication protocol is completed, the token works like a stamped ticket: The user can continue to seamlessly access the relevant resources, without re-authenticating, for the duration of the token lifecycle. That lifecycle ends when the user logs out or quits an app — and can also be triggered by a set time-out protocol.

## Considerations:

While token-based authentication is undoubtedly a major step above traditional password-based authentication, the token is still considered a “bearer token” — that is, access is granted to whomever holds the token.

## Ontology Relationships

- [[D3-AA-agent_authentication|D3-AA: Agent Authentication]]

