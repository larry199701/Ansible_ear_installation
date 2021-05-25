
ansible-playbook -i inventory playbooks/stopServersDev.yml
ansible-playbook -i inventory playbooks/stopDmgrDev.yml
ansible-playbook -i inventory playbooks/startDmgrDev.yml
ansible-playbook -i inventory playbooks/startServersDev.yml

