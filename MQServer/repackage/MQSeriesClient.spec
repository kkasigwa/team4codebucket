Summary: IBM MQ Client FileSet
Name: MQSeriesClient
Version: 9.4.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesRuntime = 9.4.0-0
Requires: MQSeriesGSKit = 9.4.0-0
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
This package provides the IBM MQ non-Java MQI client API, which permits
applications to communicate with a IBM MQ queue manager.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/lib
install -d $RPM_BUILD_ROOT/opt/mqm/lib/compat
install -d $RPM_BUILD_ROOT/opt/mqm/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/lib64/compat
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/ibm.com_IBM_MQ_Client-9.4.0.swidtag $RPM_BUILD_ROOT/opt/mqm/swidtag/ibm.com_IBM_MQ_Client-9.4.0.swidtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/ibm.com_IBM_MQ_Client-9.4.0.swidtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqic.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqic.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqic.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqic.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqic.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqic.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqdc.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqdc.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqdc.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqdc.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqdc.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqdc.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqiz.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqiz.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqiz.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqiz.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqiz.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqiz.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqic_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqic_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqic_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqic_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqic_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqic_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqdc_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqdc_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqdc_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqdc_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqdc_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqdc_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqiz_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqiz_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqiz_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqiz_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqiz_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqiz_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqicb.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqicb.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqicb.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqicb.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqicb.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqicb.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqicb_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqicb_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqicb_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqicb_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqicb_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqicb_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqtmc $RPM_BUILD_ROOT/opt/mqm/bin/runmqtmc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqtmc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqltmcc $RPM_BUILD_ROOT/opt/mqm/bin/amqltmcc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqltmcc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqczsc $RPM_BUILD_ROOT/opt/mqm/lib/amqczsc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqczsc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqczscg $RPM_BUILD_ROOT/opt/mqm/lib/amqczscg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqczscg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqccics_r.a $RPM_BUILD_ROOT/opt/mqm/lib/libmqccics_r.a
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqccics_r.a
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqltmcc64 $RPM_BUILD_ROOT/opt/mqm/bin/amqltmcc64
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqltmcc64
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqczsc $RPM_BUILD_ROOT/opt/mqm/lib64/amqczsc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqczsc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqczscg $RPM_BUILD_ROOT/opt/mqm/lib64/amqczscg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqczscg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqccics_r.a $RPM_BUILD_ROOT/opt/mqm/lib64/libmqccics_r.a
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqccics_r.a
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqc23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqc23gl.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libimqc23gl.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqc23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqc23gl_r.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libimqc23gl_r.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqc23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqc23gl.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libimqc23gl.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqc23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqc23gl_r.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libimqc23gl_r.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqcxa.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqcxa.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqcxa.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqcxa.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqcxa.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqcxa.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqcxa64.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqcxa64.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqcxa64.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqcxa_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqcxa_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqcxa_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqcxa_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqcxa_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqcxa_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqcxa64_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqcxa64_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqcxa64_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqmdnetstd.dll $RPM_BUILD_ROOT/opt/mqm/lib64/amqmdnetstd.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqmdnetstd.dll
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqmxmsstd.dll $RPM_BUILD_ROOT/opt/mqm/lib64/amqmxmsstd.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqmxmsstd.dll

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%attr(444,mqm,mqm) %config(missingok) "/opt/mqm/swidtag/ibm.com_IBM_MQ_Client-9.4.0.swidtag"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqic.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqic.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqdc.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqdc.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqiz.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqiz.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqic_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqic_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqdc_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqdc_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqiz_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqiz_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqicb.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqicb.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqicb_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqicb_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqtmc"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqltmcc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqczsc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqczscg"
%attr(555,mqm,mqm) "/opt/mqm/lib/libmqccics_r.a"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqltmcc64"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqczsc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqczscg"
%attr(555,mqm,mqm) "/opt/mqm/lib64/libmqccics_r.a"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqc23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqc23gl_r.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqc23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqc23gl_r.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqcxa.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqcxa.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqcxa64.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqcxa_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqcxa_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqcxa64_r.so"
%attr(555,mqm,mqm) "/opt/mqm/lib64/amqmdnetstd.dll"
%attr(555,mqm,mqm) "/opt/mqm/lib64/amqmxmsstd.dll"

%pre
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Client FileSet"
RPM_PACKAGE_NAME="MQSeriesClient"
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
echo > /dev/null 2>/dev/null

%post
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Client FileSet"
RPM_PACKAGE_NAME="MQSeriesClient"
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
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqic.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqic.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqic.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqic.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqic.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqic.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqic.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqic.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqic.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqic_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqic_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqic_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqic_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqic_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqic_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqic_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqic_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqic_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqicb.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqicb.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqicb.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqicb.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqicb_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqicb_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqicb_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqicb_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqcxa.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqcxa.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqcxa.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqcxa.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqcxa64.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqcxa64.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqcxa_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqcxa_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqcxa_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqcxa_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqcxa64_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqcxa64_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64_r.so

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/client_postinstall.sh
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="3401304673" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 

# Invoke setmqinst to refresh symlinks if this installation is the primary
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi
echo > /dev/null


%preun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Client FileSet"
RPM_PACKAGE_NAME="MQSeriesClient"
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
if [ ${1} -eq 0 ] ; then
:

# Removing product links
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqic.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqic_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqic_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqicb_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqicb_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqc23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqc23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqc23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqc23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqc23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqcxa_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqcxa64_r.so
fi

%postun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Client FileSet"
RPM_PACKAGE_NAME="MQSeriesClient"
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
RPM_PACKAGE_SUMMARY="IBM MQ Client FileSet"
RPM_PACKAGE_NAME="MQSeriesClient"
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

