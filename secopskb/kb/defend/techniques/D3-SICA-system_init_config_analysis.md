---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SICA"
d3fend_name: "System Init Config Analysis"
d3fend_ontology_id: "d3f:SystemInitConfigAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASystemInitConfigAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1037"
  - "T1037.004"
  - "T1037.005"
  - "T1547"
  - "T1547.001"
  - "T1562"
  - "T1562.009"
  - "T1574"
  - "T1574.011"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Analysis of any system process startup configuration.

## Workspace

- [[workspaces/defend/techniques/D3-SICA-system_init_config_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SICA-system_init_config_analysis-note]]

## Parent Technique

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Related ATT&CK Techniques

- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037004-rc-scripts|T1037.004: RC Scripts]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037005-startup-items|T1037.005: Startup Items]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
- [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562009-safe-mode-boot|T1562.009: Safe Mode Boot]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]

## Ontology Relationships

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

