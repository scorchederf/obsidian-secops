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
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-SEA: Script Execution Analysis

Analyzing the execution of a script to detect unauthorized user activity.

## Parent Technique

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Knowledge Base Article

## How it works
Software installed on the host system hooks into a scripting engine to intercept commands before they are executed and block commands if they are determined to be harmful. Pattern matching is used to identify unauthorized commands or in the case of script files, a hash of the file is compared against hashes of known unauthorized script files.

## Considerations
List of known unauthorized script files or regular expression patterns must be kept up to date to ensure detection of new threats.

## Ontology Relationships

- [[D3-PA-process_analysis|D3-PA: Process Analysis]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-sea-notes|Open workspace note]]

