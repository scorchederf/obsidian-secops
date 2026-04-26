---
mitre_id: "T1489"
mitre_name: "Service Stop"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--20fb2507-d71c-455d-9b6d-6104461cf26b"
mitre_created: "2019-03-29T19:00:55.901Z"
mitre_modified: "2025-10-24T17:48:30.688Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1489/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "IaaS"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0040"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment.(Citation: Talos Olympic Destroyer 2018)(Citation: Novetta Blockbuster) 

Adversaries may accomplish this by disabling individual services of high importance to an organization, such as `MSExchangeIS`, which will make Exchange content inaccessible.(Citation: Novetta Blockbuster) In some cases, adversaries may stop or disable many or all services to render systems unusable.(Citation: Talos Olympic Destroyer 2018) Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct [[T1485-data_destruction|T1485: Data Destruction]] or [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]] on the data stores of services like Exchange and SQL Server, or on virtual machines hosted on ESXi infrastructure.(Citation: SecureWorks WannaCry Analysis)(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

Threat actors may also disable or stop service in cloud environments. For example, by leveraging the `DisableAPIServiceAccess` API in AWS, a threat actor may prevent the service from creating service-linked roles on new accounts in the AWS Organization.(Citation: Datadog Security Labs Cloud Persistence 2025)(Citation: AWS DisableAWSServiceAccess)

## Workspace

- [[workspaces/attack/techniques/T1489-service_stop-note|Open workspace note]]

![[workspaces/attack/techniques/T1489-service_stop-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/220457c1_1c9f_4c2e_afe6_9598926222c1-delete_all_scheduled_tasks|Delete All Scheduled Tasks (high; windows / process_creation)]]
- [[kb/sigma/rules/9ac94dc8_9042_493c_ba45_3b5e7c86b980-disable_important_scheduled_task|Disable Important Scheduled Task (high; windows / process_creation)]]
- [[kb/sigma/rules/9e3cb244_bdb8_4632_8c90_6079c8f4f16d-important_scheduled_task_deleted|Important Scheduled Task Deleted (high; windows / taskscheduler)]]
- [[kb/sigma/rules/ce72ef99_22f1_43d4_8695_419dcb5d9330-suspicious_windows_service_tampering|Suspicious Windows Service Tampering (high; windows / process_creation)]]
- [[kb/sigma/rules/dbc1f800_0fe0_4bc0_9c66_292c2abe3f78-delete_important_scheduled_task|Delete Important Scheduled Task (high; windows / process_creation)]]

### Atomic Tests

- [[kb/atomic/tests/08b4718f_a8bf_4bb5_a552_294fc5178fea-linux_stop_service_by_killing_process_using_pkill|Linux - Stop service by killing process using pkill (sh; linux)]]
- [[kb/atomic/tests/21dfb440_830d_4c86_a3e5_2a491d5a8d04-windows_stop_service_using_service_controller|Windows - Stop service using Service Controller (command_prompt; windows)]]
- [[kb/atomic/tests/332f4c76_7e96_41a6_8cc2_7361c49db8be-linux_stop_service_by_killing_process_using_kill|Linux - Stop service by killing process using kill (sh; linux)]]
- [[kb/atomic/tests/41274289_ec9c_4213_bea4_e43c4aa57954-windows_stop_service_using_net_exe|Windows - Stop service using net.exe (command_prompt; windows)]]
- [[kb/atomic/tests/42e3a5bd_1e45_427f_aa08_2a65fa29a820-linux_stop_service_using_systemctl|Linux - Stop service using systemctl (sh; linux)]]
- [[kb/atomic/tests/6e76f56f_2373_4a6c_a63f_98b7b72761f1-abuse_of_linux_magic_system_request_key_for_send_a_sigterm_to_all_processes|Abuse of linux magic system request key for Send a SIGTERM to all processes (bash; linux)]]
- [[kb/atomic/tests/e5d95be6_02ee_4ff1_aebe_cf86013b6189-linux_stop_service_by_killing_process_using_killall|Linux - Stop service by killing process using killall (sh; linux)]]
- [[kb/atomic/tests/f3191b84_c38b_400b_867e_3a217a27795f-windows_stop_service_by_killing_process|Windows - Stop service by killing process (command_prompt; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1024-restrict_registry_permissions|M1024: Restrict Registry Permissions]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1060-out-of-band_communications_channel|M1060: Out-of-Band Communications Channel]]

## Platforms

- ESXi
- IaaS
- Linux
- macOS
- Windows

