---
id: M1045
name: Code Signing
created: 2019-06-11 17:01:25.405000+00:00
modified: 2024-12-10 18:52:40.747000+00:00
type: course-of-action
---

# Code Signing

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


## Properties

- id: M1045
- name: Code Signing
- created: 2019-06-11 17:01:25.405000+00:00
- modified: 2024-12-10 18:52:40.747000+00:00
- type: course-of-action

## Mitigates Techniques

- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036001-invalid-code-signature|T1036.001: Invalid Code Signature]]
    - [[T1036-masquerading#^t1036005-match-legitimate-resource-name-or-location|T1036.005: Match Legitimate Resource Name or Location]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
    - [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
    - [[T1127-trusted_developer_utilities_proxy_execution#^t1127002-clickonce|T1127.002: ClickOnce]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204003-malicious-image|T1204.003: Malicious Image]]
- [[T1505-server_software_component|T1505: Server Software Component]]
    - [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]
    - [[T1505-server_software_component#^t1505002-transport-agent|T1505.002: Transport Agent]]
    - [[T1505-server_software_component#^t1505004-iis-components|T1505.004: IIS Components]]
    - [[T1505-server_software_component#^t1505006-vsphere-installation-bundles|T1505.006: vSphere Installation Bundles]]
- [[T1525-implant_internal_image|T1525: Implant Internal Image]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
    - [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
    - [[T1546-event_triggered_execution#^t1546006-lc-load-dylib-addition|T1546.006: LC_LOAD_DYLIB Addition]]
    - [[T1546-event_triggered_execution#^t1546013-powershell-profile|T1546.013: PowerShell Profile]]
- [[T1554-compromise_host_software_binary|T1554: Compromise Host Software Binary]]
- [[T1601-modify_system_image|T1601: Modify System Image]]
    - [[T1601-modify_system_image#^t1601001-patch-system-image|T1601.001: Patch System Image]]
    - [[T1601-modify_system_image#^t1601002-downgrade-system-image|T1601.002: Downgrade System Image]]

