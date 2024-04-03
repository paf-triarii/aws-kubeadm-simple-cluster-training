#!/bin/bash

ansible-playbook aws/ansible/main.yaml
terraform_outputs=$(find $(pwd) -type d -name infra-provision*)
cd ${terraform_outputs}/bsa-auto-infra
terraform init
terraform plan -var-file=envVariables --out tfplan
terraform apply tfplan