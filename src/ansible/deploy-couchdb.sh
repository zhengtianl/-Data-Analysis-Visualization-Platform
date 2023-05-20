#!/bin/bash

. ~/unimelb-comp90024-2023-grp-42-openrc.sh; ansible-playbook --ask-become-pass deploy-couchdb.yaml -i inventory/hosts