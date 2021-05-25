#!/bin/sh
datetime=`date +%Y%m%d'_'%H%M%S`
_hostname=`hostname`

. ~/larrytest/was_addto_soap_client_props.sh

echo "stopping servers .... "

cd /opt/wasprofiles/Custom01/bin
./stopServer.sh wasAppServer010${_hostname: -1}
./stopServer.sh wasAppServer020${_hostname: -1}
./stopServer.sh wasAppServer030${_hostname: -1}
./stopServer.sh wasAppServer040${_hostname: -1}
./stopServer.sh wasAppServer050${_hostname: -1}
./stopServer.sh wasAppServer060${_hostname: -1}

echo "stopping Node .... "
cd /opt/wasprofiles/Custom01/bin
./stopNode.sh

RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Stop Node successful!
else
  echo Stop Node failed!
  exit 1
fi

. ~/larrytest/was_remfrom_soap_client_props.sh





: <<'COMMENT'
COMMENT
