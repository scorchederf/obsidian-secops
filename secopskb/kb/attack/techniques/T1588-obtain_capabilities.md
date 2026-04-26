---
mitre_id: "T1588"
mitre_name: "Obtain Capabilities"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--ce0687a0-e692-4b77-964a-0784a8e54ff1"
mitre_created: "2020-10-01T01:56:24.776Z"
mitre_modified: "2025-10-24T17:49:24.545Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1588/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0042"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may buy and/or steal capabilities that can be used during targeting. Rather than developing their own capabilities in-house, adversaries may purchase, freely download, or steal them. Activities may include the acquisition of malware, software (including licenses), exploits, certificates, and information relating to vulnerabilities. Adversaries may obtain capabilities to support their operations throughout numerous phases of the adversary lifecycle.

In addition to downloading free malware, software, and exploits from the internet, adversaries may purchase these capabilities from third-party entities. Third-party entities can include technology companies that specialize in malware and exploits, criminal marketplaces, or from individuals.(Citation: NationsBuying)(Citation: PegasusCitizenLab)

In addition to purchasing capabilities, adversaries may steal capabilities from third-party entities (including other adversaries). This can include stealing software licenses, malware, SSL/TLS and code-signing certificates, or raiding closed databases of vulnerabilities or exploits.(Citation: DiginotarCompromise)

## Workspace

- [[workspaces/attack/techniques/T1588-obtain_capabilities-note|Open workspace note]]

![[workspaces/attack/techniques/T1588-obtain_capabilities-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Sigma Rules

- [[kb/sigma/rules/24e3e58a_646b_4b50_adef_02ef935b9fc8-hacktool_execution_imphash|Hacktool Execution - Imphash (critical; windows / process_creation)]]
- [[kb/sigma/rules/36aa86ca_fd9d_4456_814e_d3b1b8e1e0bb-relevant_clamav_message|Relevant ClamAV Message (high; linux / clamav)]]
- [[kb/sigma/rules/37c1333a_a0db_48be_b64b_7393b2386e3b-hacktool_execution_pe_metadata|Hacktool Execution - PE Metadata (high; windows / process_creation)]]
- [[kb/sigma/rules/78bc5783_81d9_4d73_ac97_59f6db4f72a8-relevant_anti_virus_signature_keywords_in_application_log|Relevant Anti-Virus Signature Keywords In Application Log (high; windows / application)]]
- [[kb/sigma/rules/8023f872_3f1d_4301_a384_801889917ab4-usage_of_renamed_sysinternals_tools_registryset|Usage of Renamed Sysinternals Tools - RegistrySet (high; windows / registry_set)]]
- [[kb/sigma/rules/c9a88268_0047_4824_ba6e_4d81ce0b907c-antivirus_relevant_file_paths_alerts|Antivirus Relevant File Paths Alerts (high; antivirus)]]
- [[kb/sigma/rules/cd764533_2e07_40d6_a718_cfeec7f2da7f-renamed_sysinternals_debugview_execution|Renamed SysInternals DebugView Execution (high; windows / process_creation)]]
- [[kb/sigma/rules/f50f3c09_557d_492d_81db_9064a8d4e211-suspicious_execution_of_renamed_sysinternals_tools_registry|Suspicious Execution Of Renamed Sysinternals Tools - Registry (high; windows / registry_set)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0042-resource_development|TA0042: Resource Development]]

## Subtechniques

### T1588.001: Malware

^t1588001-malware

Adversaries may buy, steal, or download malware that can be used during targeting. Malicious software can include payloads, droppers, post-compromise tools, backdoors, packers, and C2 protocols. Adversaries may acquire malware to support their operations, obtaining a means for maintaining control of remote machines, evading defenses, and executing post-compromise behaviors.

In addition to downloading free malware from the internet, adversaries may purchase these capabilities from third-party entities. Third-party entities can include technology companies that specialize in malware development, criminal marketplaces (including Malware-as-a-Service, or MaaS), or from individuals. In addition to purchasing malware, adversaries may steal and repurpose malware from third-party entities (including other adversaries).

### T1588.002: Tool

^t1588002-tool

Adversaries may buy, steal, or download software tools that can be used during targeting. Tools can be open or closed source, free or commercial. A tool can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [[psexec|PsExec (S0029)]]). 

Adversaries may obtain tools to support their operations, including to support execution of post-compromise behaviors. Tools may also be leveraged for testing – for example, evaluating malware against commercial antivirus or endpoint detection and response (EDR) applications.(Citation: Forescout Conti Leaks 2022)(Citation: Sentinel Labs Top Tier Target 2025)

Tool acquisition may involve the procurement of commercial software licenses, including for red teaming tools such as Cobalt Strike. In addition to freely downloading or purchasing software, adversaries may steal software and/or software licenses from third-party entities (including other adversaries). Threat actors may also crack trial versions of software.(Citation: Recorded Future Beacon 2019)

### T1588.003: Code Signing Certificates

^t1588003-code-signing-certificates

Adversaries may buy and/or steal code signing certificates that can be used during targeting. Code signing is the process of digitally signing executables and scripts to confirm the software author and guarantee that the code has not been altered or corrupted. Code signing provides a level of authenticity for a program from the developer and a guarantee that the program has not been tampered with.(Citation: Wikipedia Code Signing) Users and/or security tools may trust a signed piece of code more than an unsigned piece of code even if they don't know who issued the certificate or who the author is.

Prior to [[T1553-subvert_trust_controls#^t1553002-code-signing|T1553.002: Code Signing]], adversaries may purchase or steal code signing certificates for use in operations. The purchase of code signing certificates may be done using a front organization or using information stolen from a previously compromised entity that allows the adversary to validate to a certificate provider as that entity. Adversaries may also steal code signing materials directly from a compromised third-party.

### T1588.004: Digital Certificates

^t1588004-digital-certificates

Adversaries may buy and/or steal SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are designed to instill trust. They include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's contents are correct. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate with its owner.

Adversaries may purchase or steal SSL/TLS certificates to further their operations, such as encrypting C2 traffic (ex: [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]] with [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]) or even enabling [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]] if the certificate is trusted or otherwise added to the root of trust (i.e. [[T1553-subvert_trust_controls#^t1553004-install-root-certificate|T1553.004: Install Root Certificate]]). The purchase of digital certificates may be done using a front organization or using information stolen from a previously compromised entity that allows the adversary to validate to a certificate provider as that entity. Adversaries may also steal certificate materials directly from a compromised third-party, including from certificate authorities.(Citation: DiginotarCompromise) Adversaries may register or hijack domains that they will later purchase an SSL/TLS certificate for.

Certificate authorities exist that allow adversaries to acquire SSL/TLS certificates, such as domain validation certificates, for free.(Citation: Let's Encrypt FAQ)

After obtaining a digital certificate, an adversary may then install that certificate (see [[T1608-stage_capabilities#^t1608003-install-digital-certificate|T1608.003: Install Digital Certificate]]) on infrastructure under their control.

### T1588.005: Exploits

^t1588005-exploits

Adversaries may buy, steal, or download exploits that can be used during targeting. An exploit takes advantage of a bug or vulnerability in order to cause unintended or unanticipated behavior to occur on computer hardware or software. Rather than developing their own exploits, an adversary may find/modify exploits from online or purchase them from exploit vendors.(Citation: Exploit Database)(Citation: TempertonDarkHotel)(Citation: NationsBuying)

In addition to downloading free exploits from the internet, adversaries may purchase exploits from third-party entities. Third-party entities can include technology companies that specialize in exploit development, criminal marketplaces (including exploit kits), or from individuals.(Citation: PegasusCitizenLab)(Citation: Wired SandCat Oct 2019) In addition to purchasing exploits, adversaries may steal and repurpose exploits from third-party entities (including other adversaries).(Citation: TempertonDarkHotel)

An adversary may monitor exploit provider forums to understand the state of existing, as well as newly discovered, exploits. There is usually a delay between when an exploit is discovered and when it is made public. An adversary may target the systems of those known to conduct exploit research and development in order to gain that knowledge for use during a subsequent operation.

Adversaries may use exploits during various phases of the adversary lifecycle (i.e. [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]], [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]], [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]], [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]], [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]], [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]], and [[T1499-endpoint_denial_of_service#^t1499004-application-or-system-exploitation|T1499.004: Application or System Exploitation]]).

### T1588.006: Vulnerabilities

^t1588006-vulnerabilities

Adversaries may acquire information about vulnerabilities that can be used during targeting. A vulnerability is a weakness in computer hardware or software that can, potentially, be exploited by an adversary to cause unintended or unanticipated behavior to occur. Adversaries may find vulnerability information by searching open databases or gaining access to closed vulnerability databases.(Citation: National Vulnerability Database)

An adversary may monitor vulnerability disclosures/databases to understand the state of existing, as well as newly discovered, vulnerabilities. There is usually a delay between when a vulnerability is discovered and when it is made public. An adversary may target the systems of those known to conduct vulnerability research (including commercial vendors). Knowledge of a vulnerability may cause an adversary to search for an existing exploit (i.e. [[T1588-obtain_capabilities#^t1588005-exploits|T1588.005: Exploits]]) or to attempt to develop one themselves (i.e. [[T1587-develop_capabilities#^t1587004-exploits|T1587.004: Exploits]]).

### T1588.007: Artificial Intelligence

^t1588007-artificial-intelligence

Adversaries may obtain access to generative artificial intelligence tools, such as large language models (LLMs), to aid various techniques during targeting. These tools may be used to inform, bolster, and enable a variety of malicious tasks, including conducting [[TA0043-reconnaissance|TA0043: Reconnaissance]], creating basic scripts, assisting social engineering, and even developing payloads.(Citation: MSFT-AI) 

For example, by utilizing a publicly available LLM an adversary is essentially outsourcing or automating certain tasks to the tool. Using AI, the adversary may draft and generate content in a variety of written languages to be used in [[T1566-phishing|T1566: Phishing]]/[[T1598-phishing_for_information|T1598: Phishing for Information]] campaigns. The same publicly available tool may further enable vulnerability or other offensive research supporting [[T1587-develop_capabilities|T1587: Develop Capabilities]]. AI tools may also automate technical tasks by generating, refining, or otherwise enhancing (e.g., [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]) malicious scripts and payloads.(Citation: OpenAI-CTI) Finally, AI-generated text, images, audio, and video may be used for fraud, [[T1656-impersonation|T1656: Impersonation]], and other malicious activities.(Citation: Google-Vishing24)(Citation: IC3-AI24)(Citation: WSJ-Vishing-AI24)


## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

