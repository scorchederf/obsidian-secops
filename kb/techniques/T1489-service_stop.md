---
id: T1489
name: Service Stop
created: 2019-03-29 19:00:55.901000+00:00
modified: 2025-10-24 17:48:30.688000+00:00
type: attack-pattern
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

## Tactic

- [[impact|Impact]]

Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment.(Citation: Talos Olympic Destroyer 2018)(Citation: Novetta Blockbuster) 

Adversaries may accomplish this by disabling individual services of high importance to an organization, such as <code>MSExchangeIS</code>, which will make Exchange content inaccessible.(Citation: Novetta Blockbuster) In some cases, adversaries may stop or disable many or all services to render systems unusable.(Citation: Talos Olympic Destroyer 2018) Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct [Data Destruction](https://attack.mitre.org/techniques/T1485) or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486) on the data stores of services like Exchange and SQL Server, or on virtual machines hosted on ESXi infrastructure.(Citation: SecureWorks WannaCry Analysis)(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

Threat actors may also disable or stop service in cloud environments. For example, by leveraging the `DisableAPIServiceAccess` API in AWS, a threat actor may prevent the service from creating service-linked roles on new accounts in the AWS Organization.(Citation: Datadog Security Labs Cloud Persistence 2025)(Citation: AWS DisableAWSServiceAccess)

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

## Tools


