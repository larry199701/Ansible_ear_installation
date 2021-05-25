#!/bin/sh

cd /opt/wasprofiles/Dmgr01/bin/
./startManager.sh

RESULT=$?
if [ $RESULT -eq 0 ]; then
  echo Start DMGR successful!
else
  echo Start DMGR failed!
fi




