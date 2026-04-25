---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DLIC"
d3fend_name: "Driver Load Integrity Checking"
d3fend_ontology_id: "d3f:DriverLoadIntegrityChecking"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADriverLoadIntegrityChecking/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Ensuring the integrity of drivers loaded during initialization of the operating system.

## Workspace

- [[workspaces/defend/techniques/D3-DLIC-driver_load_integrity_checking-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DLIC-driver_load_integrity_checking-note]]

## Parent Technique

- [[D3-PH-platform_hardening|D3-PH: Platform Hardening]]

## Knowledge Base Article

## How it works
This technique can be accomplished in a number of ways:

* A kernel level security agent installed on a host machine ensures that the driver associated with the agent is first in the initialization order. A dependent DLL associated with the driver is configured to be processed before other dependent DLLs and executes a number of operations to ensure the driver associated with the security agent is initialized first.

* Kernel components can be signed by a certificate obtained by a third party to verify the source of the component and whether it has been modified. When signed, the component will include a signature block implemented as a hash value of the component header and can also include a certificate chain. The signature and certificate data are typically added before the kernel component is distributed to the public.


## Considerations

* The private keys to sign certificates as reputable companies have been stolen in the past -- in cases such as where certificates from Adobe, Realtek, and JMicron have been used to sign malicious executables. (Source: https://resources.infosecinstitute.com/cybercrime-exploits-digital-certificates/#gref)

* Trusted Root Certificate Authorities have been compromised, yielding the ability to use the compromised keys to generate certificates with an arbitrary company name.

* It may not be difficult for an attacker to start an organization which can obtain a signed certificate.

* A root certificate authority (CA) whose certificate is trusted in the verification logic could generate incorrect certificates, if they are lax or have ulterior motives.

## Ontology Relationships

- [[D3-PH-platform_hardening|D3-PH: Platform Hardening]]

