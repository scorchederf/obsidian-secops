---
mitre_id: "TA0002"
mitre_name: "Execution"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--4ca45d45-df4d-4613-8980-bac22d278fa5"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2025-04-25T14:45:32.769Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0002/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "execution"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

The adversary is trying to run malicious code.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system. Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data. For example, an adversary might use a remote access tool to run a PowerShell script that does Remote System Discovery. 

## Workspace

- [[workspaces/attack/tactics/TA0002-execution-note|Open workspace note]]

![[workspaces/attack/tactics/TA0002-execution-note]]

## Related Techniques

- [[T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053002-at|T1053.002: At]]
    - [[T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
    - [[T1053-scheduled_task_job#^t1053006-systemd-timers|T1053.006: Systemd Timers]]
    - [[T1053-scheduled_task_job#^t1053007-container-orchestration-job|T1053.007: Container Orchestration Job]]
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
- [[T1072-software_deployment_tools|T1072: Software Deployment Tools]]
- [[T1106-native_api|T1106: Native API]]
- [[T1129-shared_modules|T1129: Shared Modules]]
- [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204001-malicious-link|T1204.001: Malicious Link]]
    - [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]
    - [[T1204-user_execution#^t1204003-malicious-image|T1204.003: Malicious Image]]
    - [[T1204-user_execution#^t1204004-malicious-copy-and-paste|T1204.004: Malicious Copy and Paste]]
    - [[T1204-user_execution#^t1204005-malicious-library|T1204.005: Malicious Library]]
- [[T1559-inter-process_communication|T1559: Inter-Process Communication]]
    - [[T1559-inter-process_communication#^t1559001-component-object-model|T1559.001: Component Object Model]]
    - [[T1559-inter-process_communication#^t1559002-dynamic-data-exchange|T1559.002: Dynamic Data Exchange]]
    - [[T1559-inter-process_communication#^t1559003-xpc-services|T1559.003: XPC Services]]
- [[T1569-system_services|T1569: System Services]]
    - [[T1569-system_services#^t1569001-launchctl|T1569.001: Launchctl]]
    - [[T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
    - [[T1569-system_services#^t1569003-systemctl|T1569.003: Systemctl]]
- [[T1609-container_administration_command|T1609: Container Administration Command]]
- [[T1610-deploy_container|T1610: Deploy Container]]
- [[T1648-serverless_execution|T1648: Serverless Execution]]
- [[T1651-cloud_administration_command|T1651: Cloud Administration Command]]
- [[T1674-input_injection|T1674: Input Injection]]
- [[T1675-esxi_administration_command|T1675: ESXi Administration Command]]
- [[T1677-poisoned_pipeline_execution|T1677: Poisoned Pipeline Execution]]

