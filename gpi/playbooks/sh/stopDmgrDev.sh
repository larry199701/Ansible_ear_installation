#!/bin/sh

datetime=`date +%Y%m%d'_'%H%M%S`

. ~/larrytest/dmgr_addto_soap_client_props.sh


echo "stopping DMGR .... "
cd /opt/wasprofiles/Dmgr01/bin/
./stopManager.sh
RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Stop DMGR successful!
else
  echo Stop DMGR failed!
  exit 1
fi

. ~/larrytest/dmgr_remfrom_soap_client_props.sh

