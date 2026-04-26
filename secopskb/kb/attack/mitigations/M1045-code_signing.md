---
mitre_id: "M1045"
mitre_name: "Code Signing"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--590777b3-b475-4c7c-aaf8-f4a73b140312"
mitre_created: "2019-06-11T17:01:25.405Z"
mitre_modified: "2024-12-10T18:52:40.747Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1045/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Code Signing is a security process that ensures the authenticity and integrity of software by digitally signing executables, scripts, and other code artifacts. It prevents untrusted or malicious code from executing by verifying the digital signatures against trusted sources. Code signing protects against tampering, impersonation, and distribution of unauthorized or malicious software, forming a critical defense against supply chain and software exploitation attacks. This mitigation can be implemented through the following measures:

Enforce Signed Code Execution:

- Implementation: Configure operating systems (e.g., Windows with AppLocker or Linux with Secure Boot) to allow only signed code to execute.
- Use Case: Prevent the execution of malicious PowerShell scripts by requiring all scripts to be signed with a trusted certificate.

Vendor-Signed Driver Enforcement:

- Implementation: Enable kernel-mode code signing to ensure that only drivers signed by trusted vendors can be loaded.
- Use Case: A malicious driver attempting to modify system memory fails to load because it lacks a valid signature.

Certificate Revocation Management:

- Implementation: Use Online Certificate Status Protocol (OCSP) or Certificate Revocation Lists (CRLs) to block certificates associated with compromised or deprecated code.
- Use Case: A compromised certificate used to sign a malicious update is revoked, preventing further execution of the software.

Third-Party Software Verification:

- Implementation: Require software from external vendors to be signed with valid certificates before deployment.
- Use Case: An organization only deploys signed and verified third-party software to prevent supply chain attacks.

Script Integrity in CI/CD Pipelines:

- Implementation: Integrate code signing into CI/CD pipelines to sign and verify code artifacts before production release.
- Use Case: A software company ensures that all production builds are signed, preventing tampered builds from reaching customers.

**Key Components of Code Signing**

- Digital Signature Verification: Verifies the authenticity of code by ensuring it was signed by a trusted entity.
- Certificate Management: Uses Public Key Infrastructure (PKI) to manage signing certificates and revocation lists.
- Enforced Policy for Unsigned Code: Prevents the execution of unsigned or untrusted binaries and scripts.
- Hash Integrity Check: Confirms that code has not been altered since signing by comparing cryptographic hashes.


## Workspace

- [[workspaces/attack/mitigations/M1045-code_signing-note|Open workspace note]]

![[workspaces/attack/mitigations/M1045-code_signing-note]]

## Mitigates Techniques

- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036001-invalid-code-signature|T1036.001: Invalid Code Signature]]
    - [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
    - [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
    - [[T1127-trusted_developer_utilities_proxy_execution#^t1127002-clickonce|T1127.002: ClickOnce]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204003-malicious-image|T1204.003: Malicious Image]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]
    - [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
    - [[T1505-server_software_component#^t1505004-iis-components|T1505.004: IIS Components]]
    - [[T1505-server_software_component#^t1505006-vsphere-installation-bundles|T1505.006: vSphere Installation Bundles]]
- [[T1525-implant_internal_image|T1525: Implant Internal Image]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546006-lc-load-dylib-addition|T1546.006: LC_LOAD_DYLIB Addition]]
    - [[T1546-event_triggered_execution#^t1546013-powershell-profile|T1546.013: PowerShell Profile]]
- [[T1554-compromise_host_software_binary|T1554: Compromise Host Software Binary]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
    - [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]]
    - [[T1601-modify_system_image#^t1601002-downgrade-system-image|T1601.002: Downgrade System Image]]

