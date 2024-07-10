#!/bin/bash

#export PATH="$PATH:/opt/mqm/bin"
#export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/mqm/lib:/opt/mqm/lib64"

cd /opt/team4codebucket/MQServer
./mqlicense.sh -accept

#for i in `echo 'MQSeriesRuntime-9.4.0-0.x86_64.rpm MQSeriesGSKit-9.4.0-0.x86_64.rpm MQSeriesSDK-9.4.0-0.x86_64.rpm MQSeriesClient-9.4.0-0.x86_64.rpm'`; do
#	echo "----------------------------------------"
#	echo $i
#	rpm -Kv $i
#	#rpm --prefix="/opt/team4codebucket/MQServer/mqm" -Uvh $i
#	rpm -Uvh $i
#done

rpm -Uvh MQSeriesRuntime-9.4.0-0.x86_64.rpm
rpm -Uvh MQSeriesGSKit-9.4.0-0.x86_64.rpm
rpm -Uvh MQSeriesSDK-9.4.0-0.x86_64.rpm
rpm -Uvh MQSeriesClient-9.4.0-0.x86_64.rpm


