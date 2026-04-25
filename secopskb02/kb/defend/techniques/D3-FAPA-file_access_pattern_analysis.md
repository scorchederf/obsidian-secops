---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-FAPA"
d3fend_name: "File Access Pattern Analysis"
d3fend_ontology_id: "d3f:FileAccessPatternAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AFileAccessPatternAnalysis/"
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

Analyzing the files accessed by a process to identify unauthorized activity.

## Workspace

- [[workspaces/defend/techniques/D3-FAPA-file_access_pattern_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-FAPA-file_access_pattern_analysis-note]]

## Parent Technique

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Knowledge Base Article

## How it works
File modifying malware such as wipers and ransomware are detected by identifying file access patterns that are associated with a malicious process. Examples of file access patterns include accessing a large number of files, accessing multiple file types, files being accessed located in multiple locations in a directory, and copying a file and encrypting the contents of that file into a copy.

## Considerations
Certain file access actions may not be statistically different from authorized activity.

## Ontology Relationships

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

