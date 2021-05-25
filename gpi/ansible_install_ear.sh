#ansible-doc -l
#ansible all -i inventory --list-hosts
#ansible devdmgr -i inventory -m ping
#ansible dev -i inventory -m command -a "id"
#ansible dev -i inventory -m command -a "env"
#ansible dev -i inventory -m shell -a "env"
#ansible dev -i inventory -m copy -a 'content="Copied here by Ansible Larry\n" dest=~/larry_test.txt'
#ansible -i inventory dev -m setup -a 'filter=ansible_kernel'
#ansible-playbook --syntax-check playbooks/test.yml
#ansible-playbook -i inventory -C playbooks/simple.yml    	
#ansible-playbook -i inventory --step playbooks/simple.yml
#ansible-playbook -i inventory playbooks/simple.yml
#ansible-playbook -i inventory playbooks/xslttest.yml
#ansible-playbook -i inventory playbooks/stopServers.yml
#ansible-playbook -i inventory playbooks/startServers.yml
#ansible-playbook -i inventory playbooks/deployWeblink2Utility.yml







#ansible-playbook -i inventory playbooks/deployWeblink20_EAR_Dev.yml
#ansible-playbook -i inventory playbooks/deployWeblink20_EAR_QA.yml

#ansible-playbook -i inventory playbooks/deployWeblink20_47981_EAR_Dev.yml
#ansible-playbook -i inventory playbooks/deployWeblink20_47981_EAR_QA.yml

#ansible-playbook -i inventory playbooks/deployPAOServiceWAS85EAR_Dev.yml
ansible-playbook -i inventory playbooks/deployPAOServiceWAS85EAR_QA.yml















