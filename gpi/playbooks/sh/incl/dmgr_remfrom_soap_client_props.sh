#!/bin/sh

datetime=`date +%Y%m%d'_'%H%M%S`

sed 's/com.ibm.SOAP.loginUserid='$1'/com.ibm.SOAP.loginUserid=/g' /opt/wasprofiles/Dmgr01/properties/soap.client.props > /tmp/soap.client.props
RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo After Stop DMGR, copy to /tmp/soap.client.props Successful
else
  echo After Stop DMGR, copy to /tmp/soap.client.props failed!
  exit 1
fi

sed 's/com.ibm.SOAP.loginPassword='$2'/com.ibm.SOAP.loginPassword=/g' /tmp/soap.client.props > /opt/wasprofiles/Dmgr01/properties/soap.client.props
RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo After Stop DMGR, copy to /opt/wasprofiles/Dmgr01/properties/soap.client.props Successful
else
  echo After Stop DMGR, copy to /opt/wasprofiles/Dmgr01/properties/soap.client.props failed!
  exit 1
fi
