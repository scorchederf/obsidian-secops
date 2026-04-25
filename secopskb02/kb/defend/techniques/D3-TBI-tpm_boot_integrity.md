---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-TBI"
d3fend_name: "TPM Boot Integrity"
d3fend_ontology_id: "d3f:TPMBootIntegrity"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ATPMBootIntegrity/"
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

Assuring the integrity of a platform by demonstrating that the boot process starts from a trusted combination of hardware and software and continues until the operating system has fully booted and applications are running.  Sometimes called Static Root of Trust Measurement (STRM).

## Workspace

- [[workspaces/defend/techniques/D3-TBI-tpm_boot_integrity-note|Open workspace note]]

![[workspaces/defend/techniques/D3-TBI-tpm_boot_integrity-note]]

## Parent Technique

- [[D3-PH-platform_hardening|D3-PH: Platform Hardening]]

## Knowledge Base Article

## How it works
During the boot process, the BIOS boot block (which with this defense enabled, is the Core Root of Trust for Measurement) measures boot components (firmware, ROM). The TPM hashes those measurements and stores the hashes in Platform Configuration Registers (PCRs).  Upon a subsequent boot, these hashes are provided to a verifier which compares the stored measurements to the new boot measurements. Integrity of the boot components is assured if they match.

Attestation of the secure boot occurs when a verifying entity requests a Quote which is a concatenation of the requested PCR values, hashed and signed by the TPM's unique RSA key.  The TPM signature is trusted because the private key is stored securely in hardware and never leaves the TPM.

## Considerations

* The TPM does not perform the follow-on actions of acting on the PCR value information, it just provides the PCR stored information.
* The current version of TPM is 2.0.; most existing implementations use TPM 1.2.

## Citations
[1] [TPM 2.0 Library](https://trustedcomputinggroup.org/resource/tpm-library-specification/)
[2] [TCG Trusted Attestation Protocol (TAP) Use Cases for TPM Families 1.2 and 2.0 and DICE](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TNC_TAP_Use_Cases_v1r0p35_published.pdf)

## Ontology Relationships

- [[D3-PH-platform_hardening|D3-PH: Platform Hardening]]

