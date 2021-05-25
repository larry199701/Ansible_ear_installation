#!/bin/sh

datetime=`date +%Y%m%d'_'%H%M%S`

. ~/larrytest/dmgr_addto_soap_client_props.sh "$1" "$2"


echo "Deploying deployWeblink20EAR_QA .... "

/opt/wasprofiles/Dmgr01/bin/wsadmin.sh \
    -conntype SOAP \
    -port 8879 \
    -host qa-dmgr01.gpi.com \
    -lang jython -f ~/larrytest/deployWeblink20EAR_QA.py "$3"

RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Deploying Weblink20EAR_QA successful!
else
  echo Deploying Weblink20EAR_QA failed!
  exit 1
fi

. ~/larrytest/dmgr_remfrom_soap_client_props.sh "$1" "$2"

