#!/bin/sh

datetime=`date +%Y%m%d'_'%H%M%S`

. ~/larrytest/dmgr_addto_soap_client_props.sh "$1" "$2"


echo "unDeploy PAOServiceWAS85EAR .... "

/opt/wasprofiles/Dmgr01/bin/wsadmin.sh \
    -conntype SOAP \
    -port 8879 \
    -host dev-dmgr01.gpi.com \
    -lang jython -f ~/larrytest/unDeployPAOServiceWAS85EAR_Dev.py "$3"

RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Undeploying PAOServiceWAS85EAR successful!
else
  echo Undeploying PAOServiceWAS85EAR failed!
  exit 1
fi

. ~/larrytest/dmgr_remfrom_soap_client_props.sh "$1" "$2"

