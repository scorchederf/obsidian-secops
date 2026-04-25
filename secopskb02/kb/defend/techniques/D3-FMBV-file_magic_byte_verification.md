---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-FMBV"
d3fend_name: "File Magic Byte Verification"
d3fend_ontology_id: "d3f:FileMagicByteVerification"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AFileMagicByteVerification/"
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

Utilizing the magic number to verify the file

## Workspace

- [[workspaces/defend/techniques/D3-FMBV-file_magic_byte_verification-note|Open workspace note]]

![[workspaces/defend/techniques/D3-FMBV-file_magic_byte_verification-note]]

## Parent Technique

- [[D3-FMVV-file_metadata_value_verification|D3-FMVV: File Metadata Value Verification]]

## Knowledge Base Article

## How it works

Many file formats use magic numbers to identify a file format or protocol. Verifying that the magic number matches the expected value of its declared format is a simple way of verifying the file format.

## Ontology Relationships

- [[D3-FMVV-file_metadata_value_verification|D3-FMVV: File Metadata Value Verification]]

