---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-TB"
d3fend_name: "Token Binding"
d3fend_ontology_id: "d3f:TokenBinding"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ATokenBinding/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Token binding is a security mechanism used to enhance the protection of tokens, such as cookies or OAuth tokens, by binding them to a specific connection.

## Workspace

- [[notes/defend/techniques/D3-TB-token_binding-note|Open workspace note]]

![[notes/defend/techniques/D3-TB-token_binding-note]]

## Parent Technique

- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]

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

When issuing a security token to a client that supports Token Binding, a server includes the client's Token Binding ID (or its cryptographic hash) in the token. Later on, when a client presents a security token containing a Token Binding ID, the server verifies that the ID in the token matches the ID of the Token Binding established with the client. In the case of a mismatch, the server rejects the token.

## Considerations

- While industry participation in the standards process is widespread, browser support remains limited.
- In practice, token-binding implementations are tied to Transport Security Layer (TLS).

## See Also

- dbr:Token_Binding

## Ontology Relationships

- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]

