Summary: IBM MQ REST API and Console
Name: MQSeriesWeb
Version: 9.4.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesRuntime = 9.4.0-0
Requires: MQSeriesJava = 9.4.0-0
Requires: MQSeriesJRE = 9.4.0-0
Requires: MQSeriesServer = 9.4.0-0
%define _source_filedigest_algorithm md5
%define _binary_filedigest_algorithm md5
%define _source_payload w7.lzdio
%define _binary_payload w7.lzdio
%global __strip /bin/true
%global _rpmdir /build/jslot0/p940_P/inst.images/amd64_linux_2/images/
%global _tmppath /build/jslot0/p940_P/obj/amd64_linux_2/install/unix/linux_2/trial
%define _unpackaged_files_terminate_build 0
BuildRoot: /build/jslot0/p940_P/obj/amd64_linux_2/ship

%description
IBM MQ for Linux for x86_64 
5724-H72 
This package provides an IBM WebSphere Liberty Profile for running the IBM MQ administrative REST API and Console.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/web
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/web/etc
install -d $RPM_BUILD_ROOT/opt/mqm/web/mq
install -d $RPM_BUILD_ROOT/opt/mqm/web/mq/etc
install -d $RPM_BUILD_ROOT/opt/mqm/web/mq/samp
install -d $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration
install -d $RPM_BUILD_ROOT/opt/mqm/web/mq/libs
install -d $RPM_BUILD_ROOT/opt/mqm/web/mq/apps
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_WebUI-9.4.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_WebUI-9.4.0.mqtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_WebUI-9.4.0.mqtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/samp/configuration/basic_registry.xml $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration/basic_registry.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration/basic_registry.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/samp/configuration/ldap_registry.xml $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration/ldap_registry.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration/ldap_registry.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/samp/configuration/no_security.xml $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration/no_security.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration/no_security.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/samp/configuration/local_os_registry.xml $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration/local_os_registry.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/samp/configuration/local_os_registry.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/etc/mqweb.xml $RPM_BUILD_ROOT/opt/mqm/web/mq/etc/mqweb.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/etc/mqweb.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/libs/com.ibm.mq.rest.utils.jar $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.mq.rest.utils.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.mq.rest.utils.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/libs/com.ibm.mq.restapi.common.jar $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.mq.restapi.common.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.mq.restapi.common.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/libs/org.json.jar $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/org.json.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/org.json.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/apps/com.ibm.mq.webconsole.ear $RPM_BUILD_ROOT/opt/mqm/web/mq/apps/com.ibm.mq.webconsole.ear
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/apps/com.ibm.mq.webconsole.ear
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/apps/com.ibm.mq.rest.ear $RPM_BUILD_ROOT/opt/mqm/web/mq/apps/com.ibm.mq.rest.ear
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/apps/com.ibm.mq.rest.ear
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/libs/com.ibm.wmqfte.cmdline.jar $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.wmqfte.cmdline.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.wmqfte.cmdline.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/libs/com.ibm.wmqfte.common.jar $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.wmqfte.common.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.wmqfte.common.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq/libs/com.ibm.wmqfte.exitroutines.api.jar $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.wmqfte.exitroutines.api.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq/libs/com.ibm.wmqfte.exitroutines.api.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/etc/server.env $RPM_BUILD_ROOT/opt/mqm/web/etc/server.env
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/etc/server.env
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/web/mq_wlp.tar.gz $RPM_BUILD_ROOT/opt/mqm/web/mq_wlp.tar.gz
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/web/mq_wlp.tar.gz
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqwlpver $RPM_BUILD_ROOT/opt/mqm/bin/amqwlpver
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqwlpver
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqweb $RPM_BUILD_ROOT/opt/mqm/bin/dspmqweb
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqweb
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqweb $RPM_BUILD_ROOT/opt/mqm/bin/setmqweb
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/setmqweb
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/strmqweb $RPM_BUILD_ROOT/opt/mqm/bin/strmqweb
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/strmqweb
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqweb $RPM_BUILD_ROOT/opt/mqm/bin/endmqweb
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/endmqweb

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(550,mqm,mqm) "/opt/mqm/web"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(550,mqm,mqm) "/opt/mqm/web/etc"
%dir %attr(550,mqm,mqm) "/opt/mqm/web/mq"
%dir %attr(550,mqm,mqm) "/opt/mqm/web/mq/etc"
%dir %attr(550,mqm,mqm) "/opt/mqm/web/mq/samp"
%dir %attr(550,mqm,mqm) "/opt/mqm/web/mq/samp/configuration"
%dir %attr(550,mqm,mqm) "/opt/mqm/web/mq/libs"
%dir %attr(550,mqm,mqm) "/opt/mqm/web/mq/apps"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_WebUI-9.4.0.mqtag"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/samp/configuration/basic_registry.xml"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/samp/configuration/ldap_registry.xml"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/samp/configuration/no_security.xml"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/samp/configuration/local_os_registry.xml"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/etc/mqweb.xml"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/libs/com.ibm.mq.rest.utils.jar"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/libs/com.ibm.mq.restapi.common.jar"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/libs/org.json.jar"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/apps/com.ibm.mq.webconsole.ear"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/apps/com.ibm.mq.rest.ear"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/libs/com.ibm.wmqfte.cmdline.jar"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/libs/com.ibm.wmqfte.common.jar"
%attr(440,mqm,mqm) "/opt/mqm/web/mq/libs/com.ibm.wmqfte.exitroutines.api.jar"
%attr(440,mqm,mqm) %verify(not md5 mtime size) "/opt/mqm/web/etc/server.env"
%attr(440,mqm,mqm) "/opt/mqm/web/mq_wlp.tar.gz"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqwlpver"
%attr(550,mqm,mqm) %verify(not md5 mtime size) "/opt/mqm/bin/dspmqweb"
%attr(550,mqm,mqm) %verify(not md5 mtime size) "/opt/mqm/bin/setmqweb"
%attr(550,mqm,mqm) %verify(not md5 mtime size) "/opt/mqm/bin/strmqweb"
%attr(550,mqm,mqm) %verify(not md5 mtime size) "/opt/mqm/bin/endmqweb"

%pre
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ REST API and Console"
RPM_PACKAGE_NAME="MQSeriesWeb"
RPM_PACKAGE_VERSION="9.4.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService                     MQSeriesAMS                     MQSeriesRDQM                     MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
MQ_UPGRADE="No"
if [  ${1} -gt 1  ] ; then 
  MQ_UPGRADE="Yes"
fi
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/preinstall.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2005,2024"
#   crc="3530070126" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2005, 2024 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Common Preinstallation script for all packages
#
# Check that this package is not being installed to a location where
# a different VR exists
#######################################################################################################
#  Change these values to match the required SOE. 
#  These values need to be in sync with mqlicense.sh present in cmd/install/unix
#######################################################################################################
MIN_SLES_VERSION=15
MIN_SLES_RELEASE=4
MIN_RH_VERSION=8
MIN_RH_RELEASE=8
MIN_UBUNTU_VERSION=22
#  Note:  This does not need to be integer as it is not used for numeric comparison
#         and will almost certainly always be 04 as that is the Ubuntu LTS release.
MIN_UBUNTU_RELEASE=04
#
#######################################################################################################
# Check the install path does not exceed the MQ maximum length of 256
#######################################################################################################
if [ ${#MQ_INSTALLATION_PATH} -gt 256 ]; then
  echo "" >&2
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) exceeds MQ maximum length of 256" >&2
  echo "" >&2
  exit 1
fi

#######################################################################################################
# Check the install path does not contain unsupported charaters
#######################################################################################################
echo "${MQ_INSTALLATION_PATH}" | grep "[:%# ]" > /dev/null
if [ $? -eq 0 ] ; then
  echo "" >&2
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) contains an unsupported character" >&2
  echo "" >&2
  exit 1
fi
# Trailing blanks
echo "${MQ_INSTALLATION_PATH}" | grep "[ ]$" > /dev/null
if [ $? -eq 0 ] ; then
  echo "" >&2
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) contains an unsupported character" >&2
  echo "" >&2
  exit 1
fi

#######################################################################################################
# Check the distribution
#######################################################################################################
Ubuntu=no
if [ -x /usr/bin/lsb_release ]
 then
    lsb_release_out=`/usr/bin/lsb_release -s -i | grep -i ubuntu`
  if [ ${?} -eq 0 ] ; then
    Ubuntu=yes
  fi
  else if [ -e /etc/os-release ]
    then
    .  /etc/os-release
    if [ ${ID} = 'ubuntu' ]
    then
      Ubuntu=yes
    fi
  else
    uname_out=`uname -a | grep -i ubuntu`
      if [ ${?} -eq 0 ]  ; then
        Ubuntu=yes
      fi
  fi
fi
Debian=no
if [ -f /etc/debian_version ]
then
  Debian=yes
fi
#######################################################################################################
# Checking unsupported OS versions
#######################################################################################################

if [ -x /usr/bin/lsb_release ] ; then
   lsb_release_out=`/usr/bin/lsb_release -s -i 2>&1 | grep SUSE`
   if [ $? -eq 0 ] ; then
     SUSE_Version=`/usr/bin/lsb_release -s -r | awk -F. '{print $1}'`
     SUSE_NUM_FIELDS=`/usr/bin/lsb_release -s -r | awk -F. '{print NF}'`
     if [ ${SUSE_NUM_FIELDS} -eq  1 ] ;then
       SUSE_Release=0
     else
       SUSE_Release=`/usr/bin/lsb_release -s -r | awk -F. '{print $2}'`
     fi
     if [ ${SUSE_Version} -lt ${MIN_SLES_VERSION} ] ; then
       echo "" >&2
       echo "ERROR:   This package is incompatible with this system."
       echo "         For SUSE systems, Version should be ${MIN_SLES_VERSION}.${MIN_SLES_RELEASE} or later."
       echo "         Installation terminated."
       echo "" >&2
       exit 1
     else
       if [ ${SUSE_Version} -eq ${MIN_SLES_VERSION} ] ; then
         if [ ${SUSE_Release} -lt ${MIN_SLES_RELEASE} ] ; then
           echo "" >&2
           echo "ERROR:   This package is incompatible with this system."
           echo "         For SUSE systems, Version should be ${MIN_SLES_VERSION}.${MIN_SLES_RELEASE} or later."
           echo "         Installation terminated."
           echo "" >&2
           exit 1
         fi
       fi
     fi
   else
     lsb_release_out=`/usr/bin/lsb_release -s -i 2>&1 | grep -i redhat`
     if [ $? -eq 0 ] ; then
       RH_Version=`/usr/bin/lsb_release -s -r | cut -f1 -d'.'`
       RH_Release=`/usr/bin/lsb_release -s -r | cut -f2 -d'.'`
       if [ ${RH_Version} -lt ${MIN_RH_VERSION} ] ; then
         echo "" >&2
         echo "ERROR:   This package is incompatible with this system."
         echo "         For Red Hat systems, Version should be ${MIN_RH_VERSION}.${MIN_RH_RELEASE} or later."
         echo "         Installation terminated."
         echo ""
         echo "" >&2
         exit 1
       else if [ ${RH_Version} -eq  ${MIN_RH_VERSION} ] && [  ${RH_Release} -lt  ${MIN_RH_RELEASE} ] ; then
         echo "" >&2
         echo "ERROR:   This package is incompatible with this system."
         echo "         For Red Hat systems, Version should be ${MIN_RH_VERSION}.${MIN_RH_RELEASE} or later."
         echo "         Installation terminated."
         echo ""
         echo "" >&2
         exit 1
       fi
       fi
     else
       lsb_release_out=`/usr/bin/lsb_release -s -i 2>&1 | grep -i Ubuntu`
       if [ $? -eq 0 ] ; then
         Ubuntu_Version=`/usr/bin/lsb_release -s -r | cut -f1 -d'.'`
         if [ ${Ubuntu_Version} -lt ${MIN_UBUNTU_VERSION} ] ; then
           echo "" >&2
           echo "ERROR:   This package is incompatible with this system."
           echo "         For Ubuntu systems, Version must be ${MIN_UBUNTU_VERSION}.${MIN_UBUNTU_RELEASE} or later."
           echo "         Installation terminated."
           echo "" >&2
           exit 1
         fi
       fi
     fi
   fi
 else
   # try another approach...
   if [ -e /etc/os-release ] ; then
     . /etc/os-release
     if [ ${ID} = "rhel" ] ; then
       RH_Version=`echo ${VERSION_ID} | cut -f1 -d'.'`
       RH_Release=`echo ${VERSION_ID} | cut -f2 -d'.'`
       if [ ${RH_Version} -lt ${MIN_RH_VERSION} ] ; then
         echo "" >&2
         echo "ERROR:   This package is incompatible with this system."
         echo "         For Red Hat systems, Version should be ${MIN_RH_VERSION}.${MIN_RH_RELEASE} or later."
         echo "         Installation terminated."
         echo ""
         echo "" >&2
         exit 1
       else
         if [ ${RH_Version} -eq ${MIN_RH_VERSION} ] && [  ${RH_Release} -lt ${MIN_RH_RELEASE} ] ; then
           echo "" >&2
           echo "ERROR:   This package is incompatible with this system."
           echo "         For Red Hat systems, Version should be ${MIN_RH_VERSION}.${MIN_RH_RELEASE} or later."
           echo "         Installation terminated."
           echo ""
           echo "" >&2
           exit 1
         fi
       fi
     else
       if [ ${ID} = "ubuntu" ] ; then
         Ubuntu_Version=`echo ${VERSION_ID} | cut -f1 -d'.'`
         if [ ${Ubuntu_Version} -lt  ${MIN_UBUNTU_VERSION} ] ; then
           echo "" >&2
           echo "ERROR:   This package is incompatible with this system."
           echo "         For Ubuntu systems, Version must be ${MIN_UBUNTU_VERSION}.${MIN_UBUNTU_RELEASE} or later."
           echo "         Installation terminated."
           echo "" >&2
           exit 1
         fi
       else
         if [ ${ID} = "sles" ] ; then
           Sles_Version=`echo ${VERSION_ID} | cut -f1 -d'.'`
           Sles_Num_Fields=`echo ${VERSION_ID} | awk -F. '{print NF}'`
           if [ ${Sles_Num_Fields} -eq 1 ] ; then
             Sles_Release=0
           else
             Sles_Release=`echo ${VERSION_ID} | awk -F. '{print $2}'`
           fi
           if [ ${Sles_Version} -lt ${MIN_SLES_VERSION} ] ; then
             echo "" >&2
             echo "ERROR:   This package is incompatible with this system."
             echo "         For SUSE systems, Version must be ${MIN_SLES_VERSION}.${MIN_SLES_RELEASE} or later."
             echo "         Installation terminated."
             echo "" >&2
             exit 1
           else
             if [ ${Sles_Version} -eq ${MIN_SLES_VERSION} ] ; then
               if [ ${Sles_Release} -eq ${MIN_SLES_RELEASE} ] ; then
                 echo "" >&2
                 echo "ERROR:   This package is incompatible with this system."
                 echo "         For SUSE systems, Version must be ${MIN_SLES_VERSION}.${MIN_SLES_RELEASE} or later."
                 echo "         Installation terminated."
                 echo "" >&2
                 exit 1
               fi
             fi
           fi
         else
             echo " "
             echo "WARNING: Unable to determine distribution and release for this system. "
             echo "         Check that it is supported before continuing with installation."
             echo " "
         fi
       fi
     fi
   else
     echo " "
     echo "WARNING: Unable to determine distribution and release for this system. "
     echo "         Check that it is supported before continuing with installation."
     echo " "
   fi
 fi


#######################################################################################################
# Starting with 9.1 fail the install if doing rpm install on Ubuntu
#######################################################################################################
command=`basename $(ls -l /proc/${PPID}/exe | awk '{print $NF}')`
if [ ${command} = 'rpm' ] ; then
  if [ ${Ubuntu} = 'yes' ]
  then
     echo "" >&2
     echo "ERROR:   Use of rpm to install ${RPM_PACKAGE_NAME} on the Ubuntu distribution is no longer supported" >&2
     echo "         Installation terminated" >&2
     echo "" >&2
     exit 255
  fi
fi

#######################################################################################################
# Prevent downgrade across VRM for CD release and VR for LTS release
#######################################################################################################

if [  -f ${MQ_INSTALLATION_PATH}/bin/dspmqver ];then
    INSTALLED_VER=$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b )
    PACKAGE_VER=`echo ${RPM_PACKAGE_VERSION} `
        
    PACKAGE_VER_NUM=`echo ${PACKAGE_VER} | awk -F. '{print $1 }'`
    PACKAGE_REL_NUM=`echo ${PACKAGE_VER} | awk -F. '{print $2 }'`
    PACKAGE_MOD_NUM=`echo ${PACKAGE_VER} | awk -F. '{print $3 }'`
    
    INSTALLED_VER_NUM=`echo ${INSTALLED_VER} | awk -F. '{print $1 }'`
    INSTALLED_REL_NUM=`echo ${INSTALLED_VER} | awk -F. '{print $2 }'`
    INSTALLED_MOD_NUM=`echo ${INSTALLED_VER} | awk -F. '{print $3 }'`
    
    ILLEGAL_DOWNGRADE=0
    if [ ${INSTALLED_VER_NUM} -gt ${PACKAGE_VER_NUM} ]; then 
        ILLEGAL_DOWNGRADE=1
    elif [ ${INSTALLED_VER_NUM} -lt ${PACKAGE_VER_NUM} ]; then 
        ILLEGAL_DOWNGRADE=0
    else
         if [ $INSTALLED_REL_NUM -gt $PACKAGE_REL_NUM ] ; then
            ILLEGAL_DOWNGRADE=2
         elif [ $INSTALLED_REL_NUM -lt $PACKAGE_REL_NUM ] ; then
            ILLEGAL_DOWNGRADE=0
         else 
             if [ $INSTALLED_MOD_NUM -gt $PACKAGE_MOD_NUM ]; then
                ILLEGAL_DOWNGRADE=3
             else 
                ILLEGAL_DOWNGRADE=0
             fi
         fi
    fi
    
    if [ $ILLEGAL_DOWNGRADE -ne 0 ] ; then
            echo "" >&2
            echo "ERROR: Downgrade to a lower version, release, or modification is not supported. " >&2
            echo "" >&2
            exit 1
    fi
fi


#######################################################################################################
# Runtime checks
#######################################################################################################
echo ${RPM_PACKAGE_NAME} | grep  "MQSeriesRuntime" > /dev/null
if [ $? -eq 0 ] ; then    
    
  #####################################################################################################
  # Check that the install path does not contain a Blockchain bridge tag file 
  #################################################################################################### 
  if [ -d ${MQ_INSTALLATION_PATH}/swidtag ] ; then 
    tag_found=`ls ${MQ_INSTALLATION_PATH}/swidtag | grep IBM_MQ_BCBridge` 
    if [ $? -eq 0  ]; then
      echo "" >&2
      echo "ERROR:   Specified installation path '${MQ_INSTALLATION_PATH}' contains the IBM MQ Blockchain Bridge" >&2
      echo "         which is not supported on this release of IBM MQ." >&2
      echo "         You must uninstall the Blockchain Bridge before proceeding." >&2
      echo "         Installation cancelled." >&2
      echo "" >&2
      exit 1
    fi
  fi
  #################################################################################################### 
  # Check that the install path does not contain a Salesforce bridege tag file 
  #################################################################################################### 
  if [ -d ${MQ_INSTALLATION_PATH}/swidtag ] ; then 
    tag_found=`ls ${MQ_INSTALLATION_PATH}/swidtag | grep IBM_MQ_SFBridge` 
    if [ $? -eq 0  ]; then
      echo "" >&2
      echo "ERROR:   Specified installation path '${MQ_INSTALLATION_PATH}' contains the IBM MQ Salesforce Bridge" >&2
      echo "         which is not supported on this release of IBM MQ." >&2
      echo "         You must uninstall the Salesforce Bridge before proceeding." >&2
      echo "         Installation cancelled." >&2
      echo "" >&2
      exit 1
    fi
  fi
  #################################################################################################### 
  
  # Check that the install path is empty
  # ignore lost+found and .snapshots(GPFS) directories
  # The .snapshots directory can also be renamed within GPFS, so we allow an alternate name to be specified with
  # AMQ_IGNORE_SNAPDIRNAME
  #####################################################################################################
 if [ ${Ubuntu} = 'no' -a ${Debian} = 'no' ] ; then
  if [ $1 -eq 0 ] ; then
    if [ x${AMQ_OVERRIDE_EMPTY_INSTALL_PATH} = x ] ;then
      if [ -d ${MQ_INSTALLATION_PATH} ] && [ ${MQ_INSTALLATION_PATH} != ${MQ_DEFAULT_INSTALLATION_PATH} ] ; then
        if [ "${AMQ_IGNORE_SNAPDIRNAME}" = "" ] ; then
          SNAPDIR_NAME=".snapshots"
        else
          SNAPDIR_NAME="${AMQ_IGNORE_SNAPDIRNAME}"
        fi
        LS_ALL=`ls -A ${MQ_INSTALLATION_PATH} 2>/dev/null | grep -F -v "lost+found" | grep -F -v "${SNAPDIR_NAME}"`
        if [ "${LS_ALL}" ] ; then
          echo "" >&2
          echo "ERROR:   Specified installation path '${MQ_INSTALLATION_PATH}' is not empty" >&2
          echo "" >&2
          exit 1
       fi
      fi
    fi
  fi
 fi
#######################################################################################################
# Non Runtime checks
#######################################################################################################
else
  #####################################################################################################
  # Check the version/release of the product already at MQ_INSTALLATION_PATH is the same as this one
  #####################################################################################################
  if [ -x ${MQ_INSTALLATION_PATH}/bin/dspmqver ] ; then
    INSTALLED_VRMF=`${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b `
    verrc=$?
    if [ ${verrc} -ne 0 ]
      then
        echo ""
        echo "ERROR: Return code \"${verrc}\" from dspmqver"
        echo ""
        exit 1
      else
      INSTALLED_VR=$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b | awk -F. '{print $1 "." $2}')
      PACKAGE_VR=`echo ${RPM_PACKAGE_VERSION} | awk -F. '{print $1 "." $2}'`
      if [ "${INSTALLED_VR}" != "${PACKAGE_VR}" ] ; then
        echo "" >&2
        echo "ERROR:   This package is not applicable to the MQ installation at ${MQ_INSTALLATION_PATH}" >&2
        echo "" >&2
        exit 1
      fi
    fi
  else
    echo "" >&2
    echo "ERROR:   There is no MQSeriesRuntime installed at ${MQ_INSTALLATION_PATH}" >&2
    echo "" >&2
    exit 1
  fi
fi
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/web_preinstall.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72,"
#   years="2004,2023"
#   crc="3529340042" >
#   Licensed Materials - Property of IBM
#
#   5724-H72,
#
#   (C) Copyright IBM Corp. 2004, 2023 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#

#   preinstall script for the MQSeriesWeb package
script="preinstall script for the MQSeriesWeb package"
ARG1=${1}
WEB_DIR=`echo ${MQ_INSTALLATION_PATH}/web`
if [ ${MQ_UPGRADE} = 'Yes' ] ; then 
  if [ -r ${WEB_DIR}/mq_wlp.tar.gz ] ; then 
    cp ${WEB_DIR}/mq_wlp.tar.gz /tmp/mq_wlp.tar.gz.prev
  fi
fi

echo > /dev/null 2>/dev/null

%post
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ REST API and Console"
RPM_PACKAGE_NAME="MQSeriesWeb"
RPM_PACKAGE_VERSION="9.4.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService                     MQSeriesAMS                     MQSeriesRDQM                     MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
MQ_UPGRADE="No"
if [  ${1} -gt 1  ] ; then 
  MQ_UPGRADE="Yes"
fi
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi
if [ ${MQ_INSTALLATION_PATH} !=  ${MQ_DEFAULT_INSTALLATION_PATH} ] ; then 
  if [ -x ${MQ_INSTALLATION_PATH}/bin/amqicrel ] ; then 
     ${MQ_RUNSCRIPT} ${MQ_INSTALLATION_PATH}/bin/amqicrel ${MQ_INSTALLATION_PATH} ${RPM_PACKAGE_NAME}${PACKAGE_SUFFIX}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
  fi
fi
#  Set advanced entitlement if appropriate 
if [ ${RPM_PACKAGE_NAME} != MQSeriesRuntime ] ; then 
  rpm_query_out=`rpm -q MQSeriesServer${PACKAGE_SUFFIX} 2>&1`
  if [ ${?} -eq 0 ] ; then 
    licensetype=`${MQ_INSTALLATION_PATH}/bin/dspmqver -b -f 8192`
    if [ "${licensetype}" != 'Developer' ] ; then 
      echo ${ADVANCEDPACKAGELIST} | grep ${RPM_PACKAGE_NAME} >/dev/null 2>&1 
      if [ ${?} -eq 0 ] ; then 
        setmqinst_out=`${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l advanced -e yes 2>&1` 
        setmqinst_rc=${?}
          if [ ${setmqinst_rc} -ne 0 ] ; then 
            echo  Return code ${setmqinst_rc} from setmqinst command, output was:  >&2
            echo ${setmqinst_out} >&2
          else
            echo ${setmqinst_out}
          fi
        echo > /dev/null 2>/dev/null
      fi
    fi
  fi
fi

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/web_postinstall.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72,"
#   years="2004,2023"
#   crc="3529340042" >
#   Licensed Materials - Property of IBM
#
#   5724-H72,
#
#   (C) Copyright IBM Corp. 2004, 2023 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#

#   post install script for the MQSeriesWeb package
script="post install script for the MQSeriesWeb package"
ARG1=$1
TARFLAGS='-xzf'
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then
  TARFLAGS='-xvzf'
fi
# if we are doing an upgrade the 'old' liberty tar file was saved in /tmp 
  WEB_DIR=`echo ${MQ_INSTALLATION_PATH}/web`
  if [ -r /tmp/mq_wlp.tar.gz.prev ] ;  then  
    cd ${WEB_DIR} 
    tar -tzf /tmp/mq_wlp.tar.gz.prev | awk '{print $(1)}' | xargs rm -rvf 
    rm -v /tmp/mq_wlp.tar.gz.prev
  fi 

  if [ -r ${WEB_DIR}/mq_wlp.tar.gz ]
  then
    cd ${WEB_DIR} 
    tar ${TARFLAGS} mq_wlp.tar.gz
    tarrc=$?
    if [ ${tarrc} -ne 0 ]
      then
        echo "WARNING: Return code \"${tarrc}\" from tar while expanding \"${MQ_INSTALLATION_PATH}/web/mq_wlp.tar.gz\""
      else
        chown -h -R mqm:mqm .
        chmod -R u-w,g-w,o= .
    fi
  fi

#####################################################################################
# Create wlp configuration
#####################################################################################
   INSTALLATION_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -f512 -b `
   verrc=$?
   if [ ${verrc} -ne 0 ]
     then
       echo ""
       echo "ERROR: Return code \"${verrc}\" from dspmqver"
       echo "       Configuration of MQ web server incomplete"
       echo ""
       exit 1
     else
       VAR_WEB_DIR=/var/mqm/web/installations/${INSTALLATION_NAME}
       if [ -x "${MQ_INSTALLATION_PATH}/java/jre64/jre" ]
         then
           echo  "JAVA_HOME=${MQ_INSTALLATION_PATH}/java/jre64/jre" >> ${MQ_INSTALLATION_PATH}/web/etc/server.env
       fi
       echo  "WLP_USER_DIR=${VAR_WEB_DIR}" >> ${MQ_INSTALLATION_PATH}/web/etc/server.env
   fi


#####################################################################################
# Invoke setmqinst to create / refresh symlinks if this installation is the primary
#####################################################################################
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi
echo > /dev/null

#####################################################################################
# Fix scripts to run under bash if available
#####################################################################################
if [ -x /bin/bash ] ; then
  for script in ${MQ_INSTALLATION_PATH}/bin/*mqweb
   do
     sed -i s@#!/bin/sh@#!/bin/bash@ ${script}
   done
fi

%preun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ REST API and Console"
RPM_PACKAGE_NAME="MQSeriesWeb"
RPM_PACKAGE_VERSION="9.4.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService                     MQSeriesAMS                     MQSeriesRDQM                     MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
MQ_UPGRADE="No"
if [  ${1} -gt 1  ] ; then 
  MQ_UPGRADE="Yes"
fi
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/uninstall_servercheck.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2005,2020"
#   crc="122768040" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2005, 2020 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Pre-uninstallation script
# Checks for already running Q Managers, and if it finds one, stops the
# uninstall.

# If amqiclen exists (should do during uninstall) then run it to clean up
# IPCC resources. If amqiclen returns an error then a queue manager is still
# running so stop the uninstall.
export LANG=C
export LC_ALL=C

# There is a defect in some levels of rpm which causes the return code from the preun
# scriptlet to be ignored. For those levels of rpm we will attempt to shut down
# running queue managers before proceeding
Stop_QM='False'
if [ -x /usr/bin/lsb_release ] ; then
   Distribution=`/usr/bin/lsb_release -is`
   Dist_Rel=`/usr/bin/lsb_release -rs`
   command=`basename $(ls -l /proc/${PPID}/exe | awk '{print $NF}')`
   if [ "${Distribution}" = 'Ubuntu' -a  "${Dist_Rel}" = '16.04' -a ${command} = 'rpm' ] ; then
      Stop_QM='True'
   fi
fi

# We need the sg command to put root into the mqm  group if Q Managers are to be stopped
if [ ! -x /usr/bin/sg ] ; then
  Stop_QM='False'
fi

if [ -x ${MQ_INSTALLATION_PATH}/bin/amqiclen ] && [ -f /var/mqm/mqs.ini ]
then
    ${MQ_INSTALLATION_PATH}/bin/amqiclen -v -x > /tmp/amqiclen.$$.out 2>&1
    amqiclen_rc=$?
    if [ $amqiclen_rc -eq 1 ]
    then
      if [ ${Stop_QM} = 'True' ]
        then
          echo " " >&2
          echo "WARNING: MQ shared resources associated with the installation at" >&2
          echo "         '${MQ_INSTALLATION_PATH}' are still in use." >&2
          echo "         Attempting to end queue managers" >&2
          ${MQ_INSTALLATION_PATH}/bin/amqiclen -v -x | grep QMGR | grep -w active | awk '{print $5}' | sed s#\'##g | while read QM
	    do
	      echo "         Stopping '${QM}'" >&2
              # Use 'sg' to force root into the mqm group for this command
              /usr/bin/sg mqm -c "${MQ_INSTALLATION_PATH}/bin/endmqm -i ${QM}" | while read line
	      do
	        echo "         " $line
	      done
	    done
          echo "         Uninstallation will continue" >&2
          echo " " >&2
        else
          echo " " >&2
          echo "ERROR: MQ shared resources associated with the installation at" >&2
          echo "      '${MQ_INSTALLATION_PATH}' are still in use." >&2
          echo "       You must stop all MQ processing, including applications, Queue Managers" >&2
          echo "       and Listeners before attempting to install, update or delete" >&2
          echo "       the MQ product." >&2
          echo " " >&2
          echo "       'amqiclen -v -x' return code was: '$amqiclen_rc', output was:" >&2
          cat /tmp/amqiclen.$$.out >&2
          echo " " >&2
          rm -f /tmp/amqiclen.$$.out
          exit 1
        fi
    elif [ $amqiclen_rc -ne 0 ] 
    then
      echo "ERROR: 'amqiclen -v -x' return code was: '$amqiclen_rc', output was:" >&2
      cat /tmp/amqiclen.$$.out >&2
      echo " " >&2
      rm -f /tmp/amqiclen.$$.out
      exit 1
    fi
    rm -f /tmp/amqiclen.$$.out
fi
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/uninstall_fixpack_check.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72,"
#   years="2005,2019"
#   crc="1595222582" >
#   Licensed Materials - Property of IBM
#
#   5724-H72,
#
#   (C) Copyright IBM Corp. 2005, 2019 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Pre-uninstallation check script for all components
# A check is performed to see if there are any fixpack filesets applied to
# the base component which is currently being uninstalled.  If the fixpack
# has been applied, the uninstallation of this component is aborted to prevent
# the situation where the base fileset has been uninstalled leaving an
# uninstallable fixpack.

FIXPACK_BACKUPDIR="${MQ_INSTALLATION_PATH}/maintenance"

unset fix_exists

fix_exists=$(find $FIXPACK_BACKUPDIR -type d -maxdepth 2 -print 2>/dev/null | \
while read directory ; do
  component=`basename $directory`
  if [ "$RPM_PACKAGE_NAME" = "$component" ]; then
    # safety check - are there actually files under this directory?
    num_files=`find "$directory" -type f -print 2>/dev/null | wc -l`
    if [ $num_files -gt 0 ]; then
      echo  $num_files
      exit
    fi
  fi
done
)
if [ ! -z $fix_exists ] ; then
  echo "ERROR:  There appears to be a fixpack installed on this machine for this" >&2
  echo "        component." >&2
  echo "" >&2
  echo "        Please ensure you have removed all fixpacks for the ${RPM_PACKAGE_NAME}" >&2
  echo "        component before trying to remove this package." >&2
  echo "" >&2
  exit 1
fi
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/web_preuninstall.sh
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2004,2023" 
#   crc="1338020911" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2004, 2023 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
#   pre-uninstall script for the MQSeriesWeb package
script="pre-uninstall script for the MQSeriesWeb package"
ARG1=$1
UPGRADE=${MQ_UPGRADE}
TARFLAGS='-tzf'
if [ ${MQ_UPGRADE} = "No" ] ; then
  # See if the Liberty server is running and if so stop it 
  server_out=`${MQ_INSTALLATION_PATH}/web/bin/server status mqweb 2>&1`
  if [ $? -eq 0 ] ; then
    echo ${server_out}
    server_out=`${MQ_INSTALLATION_PATH}/web/bin/server stop mqweb 2>&1`
    echo ${server_out}
  fi
  WEB_DIR=`echo ${MQ_INSTALLATION_PATH}/web | sed s#//#/#g`
  if [ -r ${WEB_DIR}/mq_wlp.tar.gz ]  
  then 
    cd ${WEB_DIR}
    tar ${TARFLAGS}  mq_wlp.tar.gz | awk '{print $1}' | xargs rm -rf 
  fi
fi


if [ ${1} -eq 0 ] ; then
:

# Removing product links
fi

%postun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ REST API and Console"
RPM_PACKAGE_NAME="MQSeriesWeb"
RPM_PACKAGE_VERSION="9.4.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService                     MQSeriesAMS                     MQSeriesRDQM                     MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
MQ_UPGRADE="No"
if [  ${1} -gt 1  ] ; then 
  MQ_UPGRADE="Yes"
fi
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi
# Remove the MQ Advanced swidtag if no Advanced packages are now installed 
if [ ${RPM_PACKAGE_NAME} != MQSeriesRuntime ] ; then  
 if [ -x /bin/rpm ] ; then 
 for packagename in ${ADVANCEDPACKAGELIST} 
   do  
     if [ ${packagename}${PACKAGE_SUFFIX} != ${RPM_PACKAGE_NAME} ] ; then
       rpmout=`rpm -q ${packagename}${PACKAGE_SUFFIX} 2>&1`
       rpm -q ${packagename}${PACKAGE_SUFFIX} --qf '%{INSTPREFIXES}
' 2>&1 | grep -w ${MQ_INSTALLATION_PATH} > /dev/null 2>&1 
       if [ $? -eq 0 ] ; then  
          touch /tmp/$$.advanced_yes
       fi
     fi
   done
 fi
# 
# dpkg equivalent of above 
#
 if [ -x /usr/bin/dpkg ] ; then 
   for packagename in ${ADVANCEDPACKAGELIST} 
     do  
       if [ ${packagename}${PACKAGE_SUFFIX} != ${RPM_PACKAGE_NAME} ] ; then
         deb_pkgname=`echo ${packagename} | sed s#_#-#g| awk '{print tolower($0)}' | sed s#mqseries#ibmmq-#`
         dpkg_status=`dpkg-query --showformat='${Status}
' -W ${deb_pkgname} 2>/dev/null | awk '{print $3}'`
         if [ "${dpkg_status}" = 'installed' ] ; then
            touch /tmp/$$.advanced_yes
         fi
       fi
     done
 fi
#
 if [ ! -f /tmp/$$.advanced_yes  ]
   then 
     setmqinst_out=`${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l advanced -e no 2>&1` 
     setmqinst_rc=${?}
       if [ ${setmqinst_rc} -ne 0 ] ; then 
         echo  Return code ${setmqinst_rc} from setmqinst command, output was:  >&2
         echo ${setmqinst_out} >&2
       fi
     echo > /dev/null 2>/dev/null
   else 
     rm -f /tmp/$$.advanced_yes 
 fi
fi
rmflags=
findflags=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = 'on' ] ; then 
  rmflags=-v
  findflags=-print
fi
if [ -d ${MQ_INSTALLATION_PATH} ] ; then 
  files_left=`rpm -ql /${RPM_PACKAGE_NAME}`
  find ${MQ_INSTALLATION_PATH} -xtype l -exec rm ${rmflags} {} \;
  find ${MQ_INSTALLATION_PATH} -type d -empty | while read dirname 
  do
    owning_package=`rpm -qf ${dirname} --qf "%{N}.%{V}-%{R}"`
    rpmrc=$?
    if [ ${rpmrc} -eq 0 ] ; then 
      if [ "${owning_package}" = "${RPM_PACKAGE_NAME}.${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}" ] ; then  
        rmdir ${rmflags} ${dirname}  
      fi
    fi
    if [ ${rpmrc} -ne 0 ] ; then 
      rmdir ${rmflags} ${dirname}  
    fi
  done 
fi
echo "reset exit code to zero" > /dev/null
echo ${RPM_PACKAGE_NAME} | grep MQSeriesRuntime > /dev/null 2>&1
if [ ${?} -eq 0 ]; then 
  if [ -d ${MQ_INSTALLATION_PATH} ] ; then 
    rpmout=`rpm -qf ${MQ_INSTALLATION_PATH} 1>&2` 
    rpmrc=${?}
    rpmout=`rpm -ql ${RPM_PACKAGE_NAME} 1>&2` 
    rpmrc2=${?}
      if [ ${rpmrc} -eq 0 ]; then 
        if [ ! -f ${MQ_INSTALLATION_PATH}/bin/dspmqver ];then 
          rmdir -v ${MQ_INSTALLATION_PATH}/* 
        fi
      fi
  fi
fi

%posttrans
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ REST API and Console"
RPM_PACKAGE_NAME="MQSeriesWeb"
RPM_PACKAGE_VERSION="9.4.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
PACKAGE_SUFFIX=
ADVANCEDPACKAGELIST="MQSeriesFTService                     MQSeriesAMS                     MQSeriesRDQM                     MQSeriesXRService"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
MQ_UPGRADE="No"
if [  ${1} -gt 1  ] ; then 
  MQ_UPGRADE="Yes"
fi
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
xtrace_switch=`set -o | grep xtrace | awk '{print $NF}'`
if [ ${xtrace_switch} = "on" ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/web_posttrans.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72,"
#   years="2023"
#   crc="3529340042" >
#   Licensed Materials - Property of IBM
#
#   5724-H72,
#
#   (C) Copyright IBM Corp. 2023 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#

#   post trans script for the MQSeriesWeb package
script="post trans script for the MQSeriesWeb package"
ARG1=$1
TARFLAGS='-xzf'
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then
  TARFLAGS='-xvzf'
fi
WEB_DIR=`echo ${MQ_INSTALLATION_PATH}/web`

# If the lib directory doesn't exist re-run the post install steps.
if [ ! -d ${WEB_DIR}/lib ]
then
  cd ${WEB_DIR} 
  tar ${TARFLAGS} mq_wlp.tar.gz
  tarrc=$?
  if [ ${tarrc} -ne 0 ]
  then
    echo "WARNING: Return code \"${tarrc}\" from tar while expanding \"${MQ_INSTALLATION_PATH}/web/mq_wlp.tar.gz\""
  else
    chown -h -R mqm:mqm .
    chmod -R u-w,g-w,o= .
  fi

  #####################################################################################
  # Create wlp configuration
  #####################################################################################
  INSTALLATION_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -f512 -b `
  verrc=$?
  if [ ${verrc} -ne 0 ]
  then
    echo ""
    echo "ERROR: Return code \"${verrc}\" from dspmqver"
    echo "       Configuration of MQ web server incomplete"
    echo ""
    exit 1
  else
    VAR_WEB_DIR=/var/mqm/web/installations/${INSTALLATION_NAME}
    if [ -x "${MQ_INSTALLATION_PATH}/java/jre64/jre" ]
    then
      echo  "JAVA_HOME=${MQ_INSTALLATION_PATH}/java/jre64/jre" >> ${MQ_INSTALLATION_PATH}/web/etc/server.env
    fi
    echo  "WLP_USER_DIR=${VAR_WEB_DIR}" >> ${MQ_INSTALLATION_PATH}/web/etc/server.env
  fi

  #####################################################################################
  # Invoke setmqinst to create / refresh symlinks if this installation is the primary
  #####################################################################################
  setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
  rc=$?
  if [ $rc -ne 0 ] ; then
    echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
    echo "       ${setmqinst_out}" >&2
  fi
  echo > /dev/null

  #####################################################################################
  # Fix scripts to run under bash if available
  #####################################################################################
  if [ -x /bin/bash ] ; then
    for script in ${MQ_INSTALLATION_PATH}/bin/*mqweb
     do
       sed -i s@#!/bin/sh@#!/bin/bash@ ${script}
     done
  fi
fi

