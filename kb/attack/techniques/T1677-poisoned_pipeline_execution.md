---
mitre_id: "T1677"
mitre_name: "Poisoned Pipeline Execution"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--7655ac3b-dfde-49c5-a967-242856174434"
mitre_created: "2025-05-22T20:01:16.611Z"
mitre_modified: "2025-10-21T02:38:29.636Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1677/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "SaaS"
mitre_tactic_ids:
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

# T1677: Poisoned Pipeline Execution

Adversaries may manipulate continuous integration / continuous development (CI/CD) processes by injecting malicious code into the build process. There are several mechanisms for poisoning pipelines: 

* In a <b>Direct Pipeline Execution</b> scenario, the threat actor directly modifies the CI configuration file (e.g., `gitlab-ci.yml` in GitLab). They may include a command to exfiltrate credentials leveraged in the build process to a remote server, or to export them as a workflow artifact.(Citation: Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025)(Citation: OWASP CICD-SEC-4)
* In an <b>Indirect Pipeline Execution</b> scenario, the threat actor injects malicious code into files referenced by the CI configuration file. These may include makefiles, scripts, unit tests, and linters.(Citation: OWASP CICD-SEC-4)
* In a <b>Public Pipeline Execution</b> scenario, the threat actor does not have direct access to the repository but instead creates a malicious pull request from a fork that triggers a part of the CI/CD pipeline. For example, in GitHub Actions, the `pull_request_target` trigger allows workflows running from forked repositories to access secrets.  If this trigger is combined with an explicit pull request checkout and a location for a threat actor to insert malicious code (e.g., an `npm build` command), a threat actor may be able to leak pipeline credentials.(Citation: Unit 42 Palo Alto GitHub Actions Supply Chain Attack 2025)(Citation: GitHub Security Lab GitHub Actions Security 2021) Similarly, threat actors may craft pull requests with malicious inputs (such as branch names) if the build pipeline treats those inputs as trusted.(Citation: Wiz Ultralytics AI Library Hijack 2024)(Citation: Synactiv Hijacking GitHub Runners)(Citation: GitHub Security Labs GitHub Actions Security Part 2 2021) Finally, if a pipeline leverages a self-hosted runner, a threat actor may be able to execute arbitrary code on a host inside the organization’s network.(Citation: John Stawinski PyTorch Supply Chain Attack 2024)

By poisoning CI/CD pipelines, threat actors may be able to gain access to credentials, laterally move to additional hosts, or input malicious components to be shipped further down the pipeline (i.e., [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]). 

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- SaaS

## Workspace

- [[kb/notes/attack/techniques/t1677-notes|Open workspace note]]

