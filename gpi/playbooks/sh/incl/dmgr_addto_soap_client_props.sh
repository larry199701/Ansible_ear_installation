#!/bin/sh

datetime=`date +%Y%m%d'_'%H%M%S`


sed -i 's/^com.ibm.SOAP.loginUserid=.*/com.ibm.SOAP.loginUserid='$1'/' /opt/wasprofiles/Dmgr01/properties/soap.client.props
RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Before Stop DMGR, update loginUserid in soap.client.props successful!
else
  echo Before Stop DMGR, update loginUserid in soap.client.props failed!
  exit 1
fi

sed -i 's/^com.ibm.SOAP.loginPassword=.*/com.ibm.SOAP.loginPassword='$2'/g' /opt/wasprofiles/Dmgr01/properties/soap.client.props
RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Before Stop DMGR, update loginPassword in soap.client.props successful!
else
  echo Before Stop DMGR, loginPassword in soap.client.props failed!
  exit 1
fi
