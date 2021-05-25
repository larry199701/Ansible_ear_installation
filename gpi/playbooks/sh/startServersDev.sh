#!/bin/sh
_hostname=`hostname`

. ~/larrytest/was_addto_soap_client_props.sh

cd /opt/wasprofiles/Custom01/bin
#./syncNode.sh dev-dmgr01.gpi.com 8879
RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Synchronizing Node successful!
else
  echo Synchronizing Node failed!
  exit 1
fi

. ~/larrytest/was_remfrom_soap_client_props.sh

./startNode.sh
RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Start Node successful!
else
  echo Start Node failed!
fi

echo "starting servers .... "

./startServer.sh wasAppServer010${_hostname: -1}
./startServer.sh wasAppServer020${_hostname: -1}
./startServer.sh wasAppServer030${_hostname: -1}
./startServer.sh wasAppServer040${_hostname: -1}
./startServer.sh wasAppServer050${_hostname: -1}
./startServer.sh wasAppServer060${_hostname: -1}

