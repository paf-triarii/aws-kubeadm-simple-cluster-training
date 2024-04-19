#!/bin/bash
ansible-playbook aws/ansible/infra/main.yaml -u ${ANSIBLE_USER_LOCAL} ${VERBOSITY}
# ansible-playbook aws/ansible/conf/main.yaml -i inventory.ini -u ${ANSIBLE_USER_REMOTE} ${VERBOSITY}