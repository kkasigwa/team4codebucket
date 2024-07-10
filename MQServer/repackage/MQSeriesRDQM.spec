Summary: IBM MQ Replicated Data FileSet
Name: MQSeriesRDQM
Version: 9.4.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesServer = 9.4.0-0
Requires: drbd-bash-completion >= 9.27.0
Requires:                            drbd-pacemaker >= 9.27.0
Requires:                            drbd-udev >= 9.27.0
Requires:                            drbd-utils >= 9.27.0
Requires:                            kmod-drbd >= 9.2.8
Requires:                            lvm2
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
This package provides the IBM MQ Replicated Data support.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/samp
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/etc
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/etc/drbd.d
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/ocf
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/ocf/resource.d
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/ocf/resource.d/ibm
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/services
install -d $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/systemd
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rdqmadm $RPM_BUILD_ROOT/opt/mqm/bin/rdqmadm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rdqmadm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rdqmdr $RPM_BUILD_ROOT/opt/mqm/bin/rdqmdr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rdqmdr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rdqmclean $RPM_BUILD_ROOT/opt/mqm/bin/rdqmclean
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rdqmclean
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rdqmint $RPM_BUILD_ROOT/opt/mqm/bin/rdqmint
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rdqmint
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rdqmstatus $RPM_BUILD_ROOT/opt/mqm/bin/rdqmstatus
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rdqmstatus
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rdqmhandler $RPM_BUILD_ROOT/opt/mqm/bin/rdqmhandler
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rdqmhandler
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rdqmd $RPM_BUILD_ROOT/opt/mqm/bin/rdqmd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rdqmd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rdqmalert $RPM_BUILD_ROOT/opt/mqm/bin/rdqmalert
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rdqmalert
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/rdqm.ini $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/rdqm.ini
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/rdqm.ini
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/etc/drbd.d/global_common.conf $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/etc/drbd.d/global_common.conf
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/etc/drbd.d/global_common.conf
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/ocf/resource.d/ibm/rdqm $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/ocf/resource.d/ibm/rdqm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/ocf/resource.d/ibm/rdqm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/ocf/resource.d/ibm/rdqmx $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/ocf/resource.d/ibm/rdqmx
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/ocf/resource.d/ibm/rdqmx
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/firewalld/configure.sh $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/configure.sh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/configure.sh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/firewalld/unconfigure.sh $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/unconfigure.sh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/unconfigure.sh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/firewalld/services/rdqm-drbd.xml $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/services/rdqm-drbd.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/services/rdqm-drbd.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/firewalld/services/rdqm-pacemaker.xml $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/services/rdqm-pacemaker.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/services/rdqm-pacemaker.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/firewalld/services/rdqm-mq.xml $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/services/rdqm-mq.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/firewalld/services/rdqm-mq.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/rdqm/systemd/rdqm.service $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/systemd/rdqm.service
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/rdqm/systemd/rdqm.service
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_RDQM-9.4.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_RDQM-9.4.0.mqtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_RDQM-9.4.0.mqtag

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm/etc"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm/etc/drbd.d"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm/ocf"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm/ocf/resource.d"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm/ocf/resource.d/ibm"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm/firewalld"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm/firewalld/services"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/rdqm/systemd"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rdqmadm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rdqmdr"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rdqmclean"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rdqmint"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rdqmstatus"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rdqmhandler"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rdqmd"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rdqmalert"
%attr(444,mqm,mqm) "/opt/mqm/samp/rdqm/rdqm.ini"
%attr(644,root,root) "/opt/mqm/samp/rdqm/etc/drbd.d/global_common.conf"
%attr(555,root,root) %verify(not md5 mtime) "/opt/mqm/samp/rdqm/ocf/resource.d/ibm/rdqm"
%attr(555,root,root) %verify(not md5 mtime) "/opt/mqm/samp/rdqm/ocf/resource.d/ibm/rdqmx"
%attr(500,root,root) "/opt/mqm/samp/rdqm/firewalld/configure.sh"
%attr(500,root,root) "/opt/mqm/samp/rdqm/firewalld/unconfigure.sh"
%attr(444,root,root) "/opt/mqm/samp/rdqm/firewalld/services/rdqm-drbd.xml"
%attr(444,root,root) "/opt/mqm/samp/rdqm/firewalld/services/rdqm-pacemaker.xml"
%attr(444,root,root) "/opt/mqm/samp/rdqm/firewalld/services/rdqm-mq.xml"
%attr(444,root,root) "/opt/mqm/samp/rdqm/systemd/rdqm.service"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_RDQM-9.4.0.mqtag"

%pre
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Replicated Data FileSet"
RPM_PACKAGE_NAME="MQSeriesRDQM"
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
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/rdqm_preinstall.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2021,2024"
#   crc="" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2021, 2024 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Pre installation script for RDQM

checkPackageVersion()
{
  RPM_QUERY=$(rpm -qi $1)

  if [ $? -ne 0 ]
  then
    echo "" >&2
    echo "ERROR:   RDQM requires $1 to be installed" >&2
    echo "" >&2
    exit 1
  fi

  RPM_VERSION=$(echo "$RPM_QUERY" | grep "Version *: " | sed "s/Version *: //")

  IFS='.' read -a ver <<< $RPM_VERSION
  IFS='.' read -a chk <<< $2

  if [[ "${ver[0]}" -lt "${chk[0]}" ||
        "${ver[1]}" -lt "${chk[1]}" ||
        "${ver[2]}" -lt "${chk[2]}" ]]
  then
    echo "" >&2
    echo "ERROR:   RDQM requires $1 >= $2 to be installed" >&2
    echo "" >&2
    exit 1
  fi
}

# Check there are no other RDQM installations
for FILEPATH in $(grep FilePath= /etc/opt/mqm/mqinst.ini | cut -d '=' -f2)
do
  if [ $FILEPATH != $MQ_INSTALLATION_PATH ] && [ -f $FILEPATH/bin/rdqmadm ]
  then
    echo "" >&2
    echo "ERROR:   Another RDQM installation exists in $FILEPATH" >&2
    echo "" >&2
    exit 1
  fi
done

if grep -q "release 8" /etc/redhat-release
then
  checkPackageVersion pacemaker 2.0.5
  checkPackageVersion crmsh 4.3.0
elif grep -q "release 9" /etc/redhat-release
then
  checkPackageVersion pacemaker 2.1.2
  checkPackageVersion crmsh 4.4.0
else
   echo "" >&2
   echo "ERROR:   RDQM requires RHEL 8 or RHEL 9" >&2
   echo "" >&2
   exit 1
fi
echo > /dev/null 2>/dev/null

%post
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Replicated Data FileSet"
RPM_PACKAGE_NAME="MQSeriesRDQM"
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

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/rdqm_postinstall.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2017,2022"
#   crc="" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2017, 2022 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Post installation script for RDQM

#
# Create the top-level data files / directories required for RDQM
#
LANG=C
LC_ALL=C
export LANG
export LC_ALL

amqicdir_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/amqicdir -i -f 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from amqicdir for \"-i -f\", output is:" >&2
  echo "       ${amqicdir_out}" >&2
fi

# Invoke setmqinst to refresh symlinks if this installation is the primary
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi

#
# Copy /usr/lib files
#
if [ ! -d "/usr/lib/ocf/resource.d/ibm" ]
then
  mkdir /usr/lib/ocf/resource.d/ibm
  chmod 755 /usr/lib/ocf/resource.d/ibm
fi

cp ${MQ_INSTALLATION_PATH}/samp/rdqm/ocf/resource.d/ibm/rdqm /usr/lib/ocf/resource.d/ibm
chmod 755 /usr/lib/ocf/resource.d/ibm/rdqm

cp ${MQ_INSTALLATION_PATH}/samp/rdqm/ocf/resource.d/ibm/rdqmx /usr/lib/ocf/resource.d/ibm
chmod 755 /usr/lib/ocf/resource.d/ibm/rdqmx

cp ${MQ_INSTALLATION_PATH}/samp/rdqm/systemd/rdqm.service /usr/lib/systemd/system
chmod 644 /usr/lib/systemd/system/rdqm.service

#
# Add /var/mqm/rdqm symlinks symlinks
#
ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/quorum-lost
chown -h mqm:mqm /var/mqm/rdqm/quorum-lost

ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/before-resync-source
chown -h mqm:mqm /var/mqm/rdqm/before-resync-source

ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/before-resync-target
chown -h mqm:mqm /var/mqm/rdqm/before-resync-target

ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/after-resync-target
chown -h mqm:mqm /var/mqm/rdqm/after-resync-target

ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/disconnected
chown -h mqm:mqm /var/mqm/rdqm/disconnected

ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmd /var/mqm/rdqm/rdqmd
chown -h mqm:mqm /var/mqm/rdqm/rdqmd

ln -s ${MQ_INSTALLATION_PATH}/bin/crtmqm /var/mqm/rdqm/crtmqm
chown -h mqm:mqm /var/mqm/rdqm/crtmqm

ln -s ${MQ_INSTALLATION_PATH}/bin/dltmqm /var/mqm/rdqm/dltmqm
chown -h mqm:mqm /var/mqm/rdqm/dltmqm

ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmadm /var/mqm/rdqm/rdqmadm
chown -h mqm:mqm /var/mqm/rdqm/rdqmadm

ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmalert /var/mqm/rdqm/rdqmalert
chown -h mqm:mqm /var/mqm/rdqm/rdqmalert

#
# Update /etc/drbd.d/global_common.conf
#
cp /etc/drbd.d/global_common.conf /etc/drbd.d/global_common.conf.rdqmsave

cp ${MQ_INSTALLATION_PATH}/samp/rdqm/etc/drbd.d/global_common.conf /etc/drbd.d

#
# Unload drbd kernel module
#
/usr/sbin/lsmod | while read line
do
  out=($line)

  if [[ "${out[0]}" == "drbd_transport_tcp" && "${out[2]}" == "0" ]]
  then
    modprobe -r drbd_transport_tcp
  fi
done

#
# Compact memory
#
echo 1 > /proc/sys/vm/compact_memory

#
# Any postinstall activity
#
${MQ_INSTALLATION_PATH}/bin/rdqmd -i

if [ -f /etc/corosync/corosync.conf ]
then
  # Migrate corosync configuration
  if grep -q "ringnumber: 1" /etc/corosync/corosync.conf
  then
    sed -i 's/rrp_mode: active/rrp_mode: passive/' /etc/corosync/corosync.conf
  else
    sed -i -E 's/rrp_mode: (active|passive)/rrp_mode: none/' /etc/corosync/corosync.conf
  fi

  if ! grep -q token: /etc/corosync/corosync.conf
  then
    sed -i '/clear_node_high_bit: yes/a\    token: 3000' /etc/corosync/corosync.conf
  fi

  # Prevent repeated "Set r/w permissions for uid=189, gid=189 on /var/log/pacemaker/pacemaker.log" messages
  if grep -q "release 8" /etc/redhat-release
  then
    if ! grep -q 'PCMK_logfile_mode=""' /etc/sysconfig/pacemaker
    then
      cp /etc/sysconfig/pacemaker /etc/sysconfig/pacemaker.rdqmsave

      sed -i '/# PCMK_logfile_mode=0660/a PCMK_logfile_mode=""' /etc/sysconfig/pacemaker
    fi
  fi

  #
  # Re-enable pacemaker on upgrade
  #
  if ! /usr/bin/systemctl -q is-enabled pacemaker
  then
    /usr/bin/systemctl -q enable pacemaker
    /usr/bin/systemctl -q start pacemaker
  fi

  # Upgrade pacemaker configuration
  ${MQ_INSTALLATION_PATH}/bin/rdqmd -u
fi

#
# DR initialization
#
/usr/bin/systemctl -q enable rdqm
/usr/bin/systemctl -q start rdqm

#
# Remove old style trace files
#
rm -f /var/mqm/trace/*-RDQM.LOG

#
# Move trace files to errors folder
#
for (( i=0; i<3; i++ ))
do
  [ -f /var/mqm/trace/RDQM.$i.LOG ] && mv /var/mqm/trace/RDQM.$i.LOG /var/mqm/errors
done

exit 0

%preun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Replicated Data FileSet"
RPM_PACKAGE_NAME="MQSeriesRDQM"
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
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/rdqm_preuninstall.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2022"
#   crc="" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2022 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Pre uninstallation script for RDQM
if [ ${MQ_UPGRADE} = "No" ] ; then
  # Check that our VRMF matches the Runtime VRMF
  if [ "${RPM_PACKAGE_VERSION}.${RPM_PACKAGE_RELEASE}" = "$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b)" ] ; then
    ${MQ_INSTALLATION_PATH}/bin/rdqmd -p
  fi
fi 
echo "Resetting return code to success" > /dev/null
if [ ${1} -eq 0 ] ; then
:

# Removing product links
fi

%postun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Replicated Data FileSet"
RPM_PACKAGE_NAME="MQSeriesRDQM"
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

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/rdqm_postuninstall.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2017,2022"
#   crc="" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2017, 2022 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Post uninstallation script for RDQM

# Invoke setmqinst to refresh symlinks if this installation is the primary
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi

# DR termination
/usr/bin/systemctl -q disable rdqm

#
# Remove /var/mqm/vols
#
if (($(find "/var/mqm/vols" -empty -maxdepth 0 2>/dev/null | wc -l)))
then
  rmdir /var/mqm/vols
fi

#
# Remove files copied to /usr/lib
#
rm /usr/lib/ocf/resource.d/ibm/rdqm
rm /usr/lib/ocf/resource.d/ibm/rdqmx
rm /usr/lib/systemd/system/rdqm.service

if (($(find "/usr/lib/ocf/resource.d/ibm" -empty -maxdepth 0 2>/dev/null | wc -l)))
then
  rmdir /usr/lib/ocf/resource.d/ibm
fi

#
# Remove /var/mqm/rdqm symlinks
#
rm /var/mqm/rdqm/quorum-lost
rm /var/mqm/rdqm/before-resync-source
rm /var/mqm/rdqm/before-resync-target
rm /var/mqm/rdqm/after-resync-target
rm /var/mqm/rdqm/disconnected
rm /var/mqm/rdqm/rdqmd
rm /var/mqm/rdqm/crtmqm
rm /var/mqm/rdqm/dltmqm
rm /var/mqm/rdqm/rdqmadm
rm /var/mqm/rdqm/rdqmalert

#
# Remove /var/mqm/rdqm
#
if (($(find "/var/mqm/rdqm" -empty -maxdepth 0 2>/dev/null | wc -l)))
then
  rmdir /var/mqm/rdqm
fi

#
# Restore /etc/drbd.d/global_common.conf
#
mv /etc/drbd.d/global_common.conf.rdqmsave /etc/drbd.d/global_common.conf

#
# Unload drbd kernel module
#
/usr/sbin/lsmod | while read line
do
  out=($line)

  if [[ "${out[0]}" == "drbd_transport_tcp" && "${out[2]}" == "0" ]]
  then
    modprobe -r drbd_transport_tcp
  fi
done

# Remove /etc/sysconfig/pacemaker update
if grep -q "release 8" /etc/redhat-release
then
  if [ -f /etc/sysconfig/pacemaker.rdqmsave ]
  then
    mv /etc/sysconfig/pacemaker.rdqmsave /etc/sysconfig/pacemaker
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
RPM_PACKAGE_SUMMARY="IBM MQ Replicated Data FileSet"
RPM_PACKAGE_NAME="MQSeriesRDQM"
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

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/rdqm_posttrans.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2023"
#   crc="" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2023 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Post trans script for RDQM

#
# Create the top-level data files / directories required for RDQM
#
LANG=C
LC_ALL=C
export LANG
export LC_ALL

# If this directory/symlink exists then post install worked fine.
if [ ! -d /var/mqm/rdqm ]
then
  amqicdir_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/amqicdir -i -f 2>&1`
  rc=$?
  if [ $rc -ne 0 ] ; then
    echo "ERROR: Return code \"$rc\" from amqicdir for \"-i -f\", output is:" >&2
    echo "       ${amqicdir_out}" >&2
  fi

  # Invoke setmqinst to refresh symlinks if this installation is the primary
  setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
  rc=$?
  if [ $rc -ne 0 ] ; then
    echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
    echo "       ${setmqinst_out}" >&2
  fi

  #
  # Copy /usr/lib files
  #
  if [ ! -d "/usr/lib/ocf/resource.d/ibm" ]
  then
    mkdir /usr/lib/ocf/resource.d/ibm
    chmod 755 /usr/lib/ocf/resource.d/ibm
  fi

  cp ${MQ_INSTALLATION_PATH}/samp/rdqm/ocf/resource.d/ibm/rdqm /usr/lib/ocf/resource.d/ibm
  chmod 755 /usr/lib/ocf/resource.d/ibm/rdqm

  cp ${MQ_INSTALLATION_PATH}/samp/rdqm/ocf/resource.d/ibm/rdqmx /usr/lib/ocf/resource.d/ibm
  chmod 755 /usr/lib/ocf/resource.d/ibm/rdqmx

  cp ${MQ_INSTALLATION_PATH}/samp/rdqm/systemd/rdqm.service /usr/lib/systemd/system
  chmod 644 /usr/lib/systemd/system/rdqm.service

  #
  # Add /var/mqm/rdqm symlinks symlinks
  #
  ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/quorum-lost
  chown -h mqm:mqm /var/mqm/rdqm/quorum-lost

  ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/before-resync-source
  chown -h mqm:mqm /var/mqm/rdqm/before-resync-source

  ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/before-resync-target
  chown -h mqm:mqm /var/mqm/rdqm/before-resync-target

  ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/after-resync-target
  chown -h mqm:mqm /var/mqm/rdqm/after-resync-target

  ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmhandler /var/mqm/rdqm/disconnected
  chown -h mqm:mqm /var/mqm/rdqm/disconnected

  ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmd /var/mqm/rdqm/rdqmd
  chown -h mqm:mqm /var/mqm/rdqm/rdqmd

  ln -s ${MQ_INSTALLATION_PATH}/bin/crtmqm /var/mqm/rdqm/crtmqm
  chown -h mqm:mqm /var/mqm/rdqm/crtmqm

  ln -s ${MQ_INSTALLATION_PATH}/bin/dltmqm /var/mqm/rdqm/dltmqm
  chown -h mqm:mqm /var/mqm/rdqm/dltmqm

  ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmadm /var/mqm/rdqm/rdqmadm
  chown -h mqm:mqm /var/mqm/rdqm/rdqmadm

  ln -s ${MQ_INSTALLATION_PATH}/bin/rdqmalert /var/mqm/rdqm/rdqmalert
  chown -h mqm:mqm /var/mqm/rdqm/rdqmalert

  #
  # Update /etc/drbd.d/global_common.conf
  #
  cp /etc/drbd.d/global_common.conf /etc/drbd.d/global_common.conf.rdqmsave

  cp ${MQ_INSTALLATION_PATH}/samp/rdqm/etc/drbd.d/global_common.conf /etc/drbd.d

  #
  # Unload drbd kernel module
  #
  /usr/sbin/lsmod | while read line
  do
    out=($line)

    if [[ "${out[0]}" == "drbd_transport_tcp" && "${out[2]}" == "0" ]]
    then
      modprobe -r drbd_transport_tcp
    fi
  done

  #
  # Compact memory
  #
  echo 1 > /proc/sys/vm/compact_memory

  #
  # Any postinstall activity
  #
  ${MQ_INSTALLATION_PATH}/bin/rdqmd -i

  if [ -f /etc/corosync/corosync.conf ]
  then
    # Migrate corosync configuration
    if grep -q "ringnumber: 1" /etc/corosync/corosync.conf
    then
      sed -i 's/rrp_mode: active/rrp_mode: passive/' /etc/corosync/corosync.conf
    else
      sed -i -E 's/rrp_mode: (active|passive)/rrp_mode: none/' /etc/corosync/corosync.conf
    fi

    if ! grep -q token: /etc/corosync/corosync.conf
    then
      sed -i '/clear_node_high_bit: yes/a\    token: 3000' /etc/corosync/corosync.conf
    fi

    # Prevent repeated "Set r/w permissions for uid=189, gid=189 on /var/log/pacemaker/pacemaker.log" messages
    if grep -q "release 8" /etc/redhat-release
    then
      if ! grep -q 'PCMK_logfile_mode=""' /etc/sysconfig/pacemaker
      then
        cp /etc/sysconfig/pacemaker /etc/sysconfig/pacemaker.rdqmsave

        sed -i '/# PCMK_logfile_mode=0660/a PCMK_logfile_mode=""' /etc/sysconfig/pacemaker
      fi
    fi

    #
    # Re-enable pacemaker on upgrade
    #
    if ! /usr/bin/systemctl -q is-enabled pacemaker
    then
      /usr/bin/systemctl -q enable pacemaker
      /usr/bin/systemctl -q start pacemaker
    fi

    # Upgrade pacemaker configuration
    ${MQ_INSTALLATION_PATH}/bin/rdqmd -u
  fi

  #
  # DR initialization
  #
  /usr/bin/systemctl -q enable rdqm
  /usr/bin/systemctl -q start rdqm

  #
  # Remove old style trace files
  #
  rm -f /var/mqm/trace/*-RDQM.LOG

  #
  # Move trace files to errors folder
  #
  for (( i=0; i<3; i++ ))
  do
    [ -f /var/mqm/trace/RDQM.$i.LOG ] && mv /var/mqm/trace/RDQM.$i.LOG /var/mqm/errors
  done
fi

exit 0

