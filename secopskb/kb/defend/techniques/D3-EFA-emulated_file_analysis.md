---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-EFA"
d3fend_name: "Emulated File Analysis"
d3fend_ontology_id: "d3f:EmulatedFileAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AEmulatedFileAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
attack_technique_ids:
  - "T1016"
  - "T1016.001"
  - "T1016.002"
  - "T1027"
  - "T1027.001"
  - "T1027.002"
  - "T1027.004"
  - "T1036"
  - "T1036.001"
  - "T1036.003"
  - "T1037"
  - "T1037.001"
  - "T1037.002"
  - "T1037.003"
  - "T1037.004"
  - "T1055"
  - "T1055.003"
  - "T1059"
  - "T1059.001"
  - "T1059.002"
  - "T1059.003"
  - "T1059.004"
  - "T1059.005"
  - "T1059.006"
  - "T1059.007"
  - "T1059.008"
  - "T1059.009"
  - "T1059.010"
  - "T1059.011"
  - "T1059.012"
  - "T1059.013"
  - "T1114"
  - "T1114.001"
  - "T1137"
  - "T1137.001"
  - "T1137.003"
  - "T1140"
  - "T1204"
  - "T1204.002"
  - "T1218"
  - "T1218.005"
  - "T1220"
  - "T1505"
  - "T1505.003"
  - "T1534"
  - "T1546"
  - "T1546.002"
  - "T1546.005"
  - "T1546.006"
  - "T1546.008"
  - "T1546.013"
  - "T1546.015"
  - "T1547"
  - "T1547.001"
  - "T1547.009"
  - "T1548"
  - "T1548.002"
  - "T1562"
  - "T1562.003"
  - "T1564"
  - "T1564.007"
  - "T1565"
  - "T1565.003"
  - "T1566"
  - "T1566.001"
  - "T1566.002"
  - "T1574"
  - "T1574.007"
  - "T1574.008"
  - "T1574.009"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Emulating instructions in a file looking for specific patterns.

## Workspace

- [[notes/defend/techniques/D3-EFA-emulated_file_analysis-note|Open workspace note]]

![[notes/defend/techniques/D3-EFA-emulated_file_analysis-note]]

## Parent Technique

- [[D3-FA-file_analysis|D3-FA: File Analysis]]

## Related ATT&CK Techniques

- [[T1016-system_network_configuration_discovery|T1016: System Network Configuration Discovery]]
- [[T1016-system_network_configuration_discovery#^t1016001-internet-connection-discovery|T1016.001: Internet Connection Discovery]]
- [[T1016-system_network_configuration_discovery#^t1016002-wi-fi-discovery|T1016.002: Wi-Fi Discovery]]
- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[T1027-obfuscated_files_or_information#^t1027001-binary-padding|T1027.001: Binary Padding]]
- [[T1027-obfuscated_files_or_information#^t1027002-software-packing|T1027.002: Software Packing]]
- [[T1027-obfuscated_files_or_information#^t1027004-compile-after-delivery|T1027.004: Compile After Delivery]]
- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading#^t1036001-invalid-code-signature|T1036.001: Invalid Code Signature]]
- [[T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]
- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037001-logon-script-(windows)|T1037.001: Logon Script (Windows)]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037002-login-hook|T1037.002: Login Hook]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037003-network-logon-script|T1037.003: Network Logon Script]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037004-rc-scripts|T1037.004: RC Scripts]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection#^t1055003-thread-execution-hijacking|T1055.003: Thread Execution Hijacking]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
- [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[T1059-command_and_scripting_interpreter#^t1059002-applescript|T1059.002: AppleScript]]
- [[T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]
- [[T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
- [[T1059-command_and_scripting_interpreter#^t1059006-python|T1059.006: Python]]
- [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]
- [[T1059-command_and_scripting_interpreter#^t1059008-network-device-cli|T1059.008: Network Device CLI]]
- [[T1059-command_and_scripting_interpreter#^t1059009-cloud-api|T1059.009: Cloud API]]
- [[T1059-command_and_scripting_interpreter#^t1059010-autohotkey-&-autoit|T1059.010: AutoHotKey & AutoIT]]
- [[T1059-command_and_scripting_interpreter#^t1059011-lua|T1059.011: Lua]]
- [[T1059-command_and_scripting_interpreter#^t1059012-hypervisor-cli|T1059.012: Hypervisor CLI]]
- [[T1059-command_and_scripting_interpreter#^t1059013-container-cli-api|T1059.013: Container CLI/API]]
- [[T1114-email_collection|T1114: Email Collection]]
- [[T1114-email_collection#^t1114001-local-email-collection|T1114.001: Local Email Collection]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup#^t1137001-office-template-macros|T1137.001: Office Template Macros]]
- [[T1137-office_application_startup#^t1137003-outlook-forms|T1137.003: Outlook Forms]]
- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]
- [[T1204-user_execution|T1204: User Execution]]
- [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]
- [[T1220-xsl_script_processing|T1220: XSL Script Processing]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
- [[T1534-internal_spearphishing|T1534: Internal Spearphishing]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546002-screensaver|T1546.002: Screensaver]]
- [[T1546-event_triggered_execution#^t1546005-trap|T1546.005: Trap]]
- [[T1546-event_triggered_execution#^t1546006-lc-load-dylib-addition|T1546.006: LC_LOAD_DYLIB Addition]]
- [[T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]
- [[T1546-event_triggered_execution#^t1546013-powershell-profile|T1546.013: PowerShell Profile]]
- [[T1546-event_triggered_execution#^t1546015-component-object-model-hijacking|T1546.015: Component Object Model Hijacking]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
- [[T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]
- [[T1547-boot_or_logon_autostart_execution#^t1547009-shortcut-modification|T1547.009: Shortcut Modification]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
- [[T1562-impair_defenses#^t1562003-impair-command-history-logging|T1562.003: Impair Command History Logging]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564007-vba-stomping|T1564.007: VBA Stomping]]
- [[T1565-data_manipulation|T1565: Data Manipulation]]
- [[T1565-data_manipulation#^t1565003-runtime-data-manipulation|T1565.003: Runtime Data Manipulation]]
- [[T1566-phishing|T1566: Phishing]]
- [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
- [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow#^t1574007-path-interception-by-path-environment-variable|T1574.007: Path Interception by PATH Environment Variable]]
- [[T1574-hijack_execution_flow#^t1574008-path-interception-by-search-order-hijacking|T1574.008: Path Interception by Search Order Hijacking]]
- [[T1574-hijack_execution_flow#^t1574009-path-interception-by-unquoted-path|T1574.009: Path Interception by Unquoted Path]]

## Ontology Relationships

- [[D3-FA-file_analysis|D3-FA: File Analysis]]

