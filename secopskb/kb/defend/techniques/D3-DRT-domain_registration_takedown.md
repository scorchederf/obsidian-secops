---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DRT"
d3fend_name: "Domain Registration Takedown"
d3fend_ontology_id: "d3f:DomainRegistrationTakedown"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADomainRegistrationTakedown/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

The process of performing a takedown of the attacker's domain registration infrastructure.

## Workspace

- [[workspaces/defend/techniques/D3-DRT-domain_registration_takedown-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DRT-domain_registration_takedown-note]]

## Parent Technique

- [[D3-OE-object_eviction|D3-OE: Object Eviction]]

## Knowledge Base Article

## How it works

Most nameserver hosts and domain name registrars comply with internationally recognised standards and supply their services based on terms and conditions that provide users and organisations protection from abuse and trademark infringement. Performing a WHOIS query on the attacker's domain will provide a contact that can be notified in the case of abuse. Formal takedown processes should be initiated to suspend or disable the normal function of the domain name.

## Considerations

- Takedown notifications should clearly demonstrate (with evidence) that the nameserver or registrars Terms and Conditions have been breached.
- Takedown processes are notoriously slow and sometimes unsuccessful.
- Many government organisations will have takedown processes that should also be followed. They may use this for intelligence to assist other organisations suffering an attack.
- Top level domain registrars will have takedown processes that can be followed, as an escalation path, when the nameserver host and/or registrar have not responded or complied timeously or inline with the TLD expectations.

## Examples of Domain Registration Abuse

Attackers will create infrastructure from which to carry out their operations and this may include registering domain names to be used in the various attacks. Known misuse cases include:

- Registering domain names that are similar to the victim's. This is known as typosquatting or URL hijacking. Legitimate looking mails or URLs could be sent using this domain in phishing campaigns.
- Registring domain names that are used in C2 beacons.

## Ontology Relationships

- [[D3-OE-object_eviction|D3-OE: Object Eviction]]

