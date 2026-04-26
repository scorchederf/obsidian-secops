---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-RS"
d3fend_name: "Restore Software"
d3fend_ontology_id: "d3f:RestoreSoftware"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ARestoreSoftware/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1014"
  - "T1056"
  - "T1056.003"
  - "T1072"
  - "T1127"
  - "T1127.001"
  - "T1137"
  - "T1137.006"
  - "T1176"
  - "T1176.001"
  - "T1176.002"
  - "T1195"
  - "T1195.001"
  - "T1195.002"
  - "T1212"
  - "T1218"
  - "T1218.014"
  - "T1490"
  - "T1497"
  - "T1497.003"
  - "T1505"
  - "T1505.001"
  - "T1505.004"
  - "T1542"
  - "T1542.001"
  - "T1542.002"
  - "T1542.003"
  - "T1542.004"
  - "T1546"
  - "T1546.011"
  - "T1547"
  - "T1547.008"
  - "T1554"
  - "T1564"
  - "T1564.006"
  - "T1574"
  - "T1574.005"
  - "T1574.010"
  - "T1649"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Restoring software to a host.

## Workspace

- [[workspaces/defend/techniques/D3-RS-restore_software-note|Open workspace note]]

![[workspaces/defend/techniques/D3-RS-restore_software-note]]

## Parent Technique

- [[D3-RO-restore_object|D3-RO: Restore Object]]

## Related ATT&CK Techniques

- [[T1014-rootkit|T1014: Rootkit]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056003-web-portal-capture|T1056.003: Web Portal Capture]]
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]
- [[T1127-trusted_developer_utilities_proxy_execution#^t1127001-msbuild|T1127.001: MSBuild]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
- [[T1137-office_application_startup#^t1137006-add-ins|T1137.006: Add-ins]]
- [[T1176-software_extensions|T1176: Software Extensions]]
- [[T1176-software_extensions#^t1176001-browser-extensions|T1176.001: Browser Extensions]]
- [[T1176-software_extensions#^t1176002-ide-extensions|T1176.002: IDE Extensions]]
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]
- [[T1195-supply_chain_compromise#^t1195001-compromise-software-dependencies-and-development-tools|T1195.001: Compromise Software Dependencies and Development Tools]]
- [[T1195-supply_chain_compromise#^t1195002-compromise-software-supply-chain|T1195.002: Compromise Software Supply Chain]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
- [[T1218-system_binary_proxy_execution#^t1218014-mmc|T1218.014: MMC]]
- [[T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]
- [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]
- [[T1497-virtualization_sandbox_evasion#^t1497003-time-based-checks|T1497.003: Time Based Checks]]
- [[T1505-server_software_component|T1505: Server Software Component]]
- [[T1505-server_software_component#^t1505001-sql-stored-procedures|T1505.001: SQL Stored Procedures]]
- [[T1505-server_software_component#^t1505004-iis-components|T1505.004: IIS Components]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
- [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]
- [[T1542-pre-os_boot#^t1542002-component-firmware|T1542.002: Component Firmware]]
- [[T1542-pre-os_boot#^t1542003-bootkit|T1542.003: Bootkit]]
- [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546011-application-shimming|T1546.011: Application Shimming]]
- [[T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]
- [[T1547-boot_or_logon_autostart_execution#^t1547008-lsass-driver|T1547.008: LSASS Driver]]
- [[T1554-compromise_host_software_binary|T1554: Compromise Host Software Binary]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
- [[T1564-hide_artifacts#^t1564006-run-virtual-instance|T1564.006: Run Virtual Instance]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow#^t1574005-executable-installer-file-permissions-weakness|T1574.005: Executable Installer File Permissions Weakness]]
- [[T1574-hijack_execution_flow#^t1574010-services-file-permissions-weakness|T1574.010: Services File Permissions Weakness]]
- [[T1649-steal_or_forge_authentication_certificates|T1649: Steal or Forge Authentication Certificates]]

## Ontology Relationships

- [[D3-RO-restore_object|D3-RO: Restore Object]]

