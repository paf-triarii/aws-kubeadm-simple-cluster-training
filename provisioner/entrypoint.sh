#!/bin/bash
ansible-playbook aws/ansible/infra/main.yaml
ansible-playbook aws/ansible/conf/main.yaml -i inventory.ini
# terraform_outputs=$(find $(pwd) -type d -name infra-provision*)
# cd ${terraform_outputs}/bsa-auto-infra
# terraform init
# terraform plan -var-file=envVariables --out tfplan
# terraform apply tfplan