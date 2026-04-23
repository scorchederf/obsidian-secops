---
mitre_id: "S0358"
mitre_name: "Ruler"
mitre_type: "tool"
mitre_stix_id: "tool--90ac9266-68ce-46f2-b24f-5eb3b2a8ea38"
mitre_created: "2019-02-04T18:27:00.501Z"
mitre_modified: "2025-04-25T14:45:22.953Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0358/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_aliases:
  - "Ruler"
---

# Ruler

[Ruler](https://attack.mitre.org/software/S0358) is a tool to abuse Microsoft Exchange services. It is publicly available on GitHub and the tool is executed via the command line. The creators of [Ruler](https://attack.mitre.org/software/S0358) have also released a defensive tool, NotRuler, to detect its usage.(Citation: SensePost Ruler GitHub)(Citation: SensePost NotRuler)

## Uses Techniques

- [[T1087-account_discovery|T1087: Account Discovery]]
    - [[T1087-account_discovery#^t1087003-email-account|T1087.003: Email Account]]
- [[T1137-office_application_startup|T1137: Office Application Startup]]
    - [[T1137-office_application_startup#^t1137003-outlook-forms|T1137.003: Outlook Forms]]
    - [[T1137-office_application_startup#^t1137004-outlook-home-page|T1137.004: Outlook Home Page]]
    - [[T1137-office_application_startup#^t1137005-outlook-rules|T1137.005: Outlook Rules]]

