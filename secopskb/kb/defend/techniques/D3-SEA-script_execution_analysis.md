---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SEA"
d3fend_name: "Script Execution Analysis"
d3fend_ontology_id: "d3f:ScriptExecutionAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AScriptExecutionAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Analyzing the execution of a script to detect unauthorized user activity.

## Workspace

- [[workspaces/defend/techniques/D3-SEA-script_execution_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SEA-script_execution_analysis-note]]

## Parent Technique

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Knowledge Base Article

## How it works
Software installed on the host system hooks into a scripting engine to intercept commands before they are executed and block commands if they are determined to be harmful. Pattern matching is used to identify unauthorized commands or in the case of script files, a hash of the file is compared against hashes of known unauthorized script files.

## Considerations
List of known unauthorized script files or regular expression patterns must be kept up to date to ensure detection of new threats.

## Ontology Relationships

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

