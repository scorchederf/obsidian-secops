---
mitre_id: "T1480"
mitre_name: "Execution Guardrails"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--853c4192-4311-43e1-bfbb-b11b14911852"
mitre_created: "2019-01-31T02:10:08.261Z"
mitre_modified: "2025-10-24T17:49:03.764Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1480/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "ESXi"
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0005"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign.(Citation: FireEye Kevin Mandia Guardrails) Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.(Citation: FireEye Outlook Dec 2019)

Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]. While use of [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]] may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.

Adversaries may identify and block certain user-agents to evade defenses and narrow the scope of their attack to victims and platforms on which it will be most effective. A user-agent self-identifies data such as a user's software application, operating system, vendor, and version. Adversaries may check user-agents for operating system identification and then only serve malware for the exploitable software while ignoring all other operating systems.(Citation: Trellix-Qakbot)

## Workspace

- [[workspaces/attack/techniques/T1480-execution_guardrails-note|Open workspace note]]

![[workspaces/attack/techniques/T1480-execution_guardrails-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## Subtechniques

### T1480.001: Environmental Keying

^t1480001-environmental-keying

Adversaries may environmentally key payloads or other features of malware to evade defenses and constraint execution to a specific target environment. Environmental keying uses cryptography to constrain execution or actions based on adversary supplied environment specific conditions that are expected to be present on the target. Environmental keying is an implementation of [[T1480-execution_guardrails|T1480: Execution Guardrails]] that utilizes cryptographic techniques for deriving encryption/decryption keys from specific types of values in a given computing environment.(Citation: EK Clueless Agents)

Values can be derived from target-specific elements and used to generate a decryption key for an encrypted payload. Target-specific values can be derived from specific network shares, physical devices, software/software versions, files, joined AD domains, system time, and local/external IP addresses.(Citation: Kaspersky Gauss Whitepaper)(Citation: Proofpoint Router Malvertising)(Citation: EK Impeding Malware Analysis)(Citation: Environmental Keyed HTA)(Citation: Ebowla: Genetic Malware) By generating the decryption keys from target-specific environmental values, environmental keying can make sandbox detection, anti-virus detection, crowdsourcing of information, and reverse engineering difficult.(Citation: Kaspersky Gauss Whitepaper)(Citation: Ebowla: Genetic Malware) These difficulties can slow down the incident response process and help adversaries hide their tactics, techniques, and procedures (TTPs).

Similar to [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]], adversaries may use environmental keying to help protect their TTPs and evade detection. Environmental keying may be used to deliver an encrypted payload to the target that will use target-specific values to decrypt the payload before execution.(Citation: Kaspersky Gauss Whitepaper)(Citation: EK Impeding Malware Analysis)(Citation: Environmental Keyed HTA)(Citation: Ebowla: Genetic Malware)(Citation: Demiguise Guardrail Router Logo) By utilizing target-specific values to decrypt the payload the adversary can avoid packaging the decryption key with the payload or sending it over a potentially monitored network connection. Depending on the technique for gathering target-specific values, reverse engineering of the encrypted payload can be exceptionally difficult.(Citation: Kaspersky Gauss Whitepaper) This can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within.

Like other [[T1480-execution_guardrails|T1480: Execution Guardrails]], environmental keying can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This activity is distinct from typical [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]. While use of [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]] may involve checking for known sandbox values and continuing with execution only if there is no match, the use of environmental keying will involve checking for an expected target-specific value that must match for decryption and subsequent execution to be successful.

### T1480.002: Mutual Exclusion

^t1480002-mutual-exclusion

Adversaries may constrain execution or actions based on the presence of a mutex associated with malware. A mutex is a locking mechanism used to synchronize access to a resource. Only one thread or process can acquire a mutex at a given time.(Citation: Microsoft Mutexes)

While local mutexes only exist within a given process, allowing multiple threads to synchronize access to a resource, system mutexes can be used to synchronize the activities of multiple processes.(Citation: Microsoft Mutexes) By creating a unique system mutex associated with a particular malware, adversaries can verify whether or not a system has already been compromised.(Citation: Sans Mutexes 2012)

In Linux environments, malware may instead attempt to acquire a lock on a mutex file. If the malware is able to acquire the lock, it continues to execute; if it fails, it exits to avoid creating a second instance of itself.(Citation: Intezer RedXOR 2021)(Citation: Deep Instinct BPFDoor 2023)

Mutex names may be hard-coded or dynamically generated using a predictable algorithm.(Citation: ICS Mutexes 2015)

## Mitigations

- [[M1055-do_not_mitigate|M1055: Do Not Mitigate]]

## Platforms

- ESXi
- Linux
- macOS
- Windows

