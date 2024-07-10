Summary: IBM MQ Java, JMS and Web Services support
Name: MQSeriesJava
Version: 9.4.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesRuntime = 9.4.0-0
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
This package provides the IBM MQ classes for Java and JMS application
programming interfaces, as well as Java Web Services support.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/java
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/jca
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/modules
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta
install -d $RPM_BUILD_ROOT/opt/mqm/java/bin
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/jmscc
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Java_Messaging-9.4.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Java_Messaging-9.4.0.mqtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Java_Messaging-9.4.0.mqtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/libmqjexitstub02.so $RPM_BUILD_ROOT/opt/mqm/java/lib/libmqjexitstub02.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/libmqjexitstub02.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/libmqjexitstub02.so $RPM_BUILD_ROOT/opt/mqm/java/lib64/libmqjexitstub02.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib64/libmqjexitstub02.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/bcprov-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/bcprov-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/bcprov-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/bcpkix-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/bcpkix-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/bcpkix-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/bcutil-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/bcutil-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/bcutil-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/javax/bcprov-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/bcprov-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/bcprov-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/javax/bcpkix-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/bcpkix-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/bcpkix-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/javax/bcutil-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/bcutil-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/bcutil-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/jakarta/bcprov-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/bcprov-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/bcprov-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/jakarta/bcpkix-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/bcpkix-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/bcpkix-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/jakarta/bcutil-jdk18on.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/bcutil-jdk18on.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/bcutil-jdk18on.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.headers.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.headers.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.headers.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.pcf.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.pcf.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.pcf.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.jmqi.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jmqi.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jmqi.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mqjms.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mqjms.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mqjms.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.traceControl.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.traceControl.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.traceControl.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.allclient.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.allclient.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.allclient.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.jakarta.client.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jakarta.client.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jakarta.client.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/javax/com.ibm.mq.allclient.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/com.ibm.mq.allclient.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/com.ibm.mq.allclient.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/jakarta/com.ibm.mq.jakarta.client.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/com.ibm.mq.jakarta.client.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/com.ibm.mq.jakarta.client.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/fscontext.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/fscontext.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/fscontext.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/providerutil.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/providerutil.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/providerutil.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/javax/fscontext.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/fscontext.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/fscontext.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/javax/providerutil.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/providerutil.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/providerutil.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/jakarta/fscontext.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/fscontext.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/fscontext.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/jakarta/providerutil.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/providerutil.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/providerutil.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/org.json.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/org.json.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/org.json.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/javax/org.json.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/org.json.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/org.json.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/jakarta/org.json.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/org.json.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/org.json.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jms.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/jms.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jms.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jakarta.jms-api.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/jakarta.jms-api.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jakarta.jms-api.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/javax/jms.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/jms.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/javax/jms.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/modules/jakarta/jakarta.jms-api.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/jakarta.jms-api.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/modules/jakarta/jakarta.jms-api.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jca/wmq.jmsra.ivt.ear $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jmsra.ivt.ear
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jmsra.ivt.ear
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jca/wmq.jakarta.jmsra.ivt.ear $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jakarta.jmsra.ivt.ear
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jakarta.jmsra.ivt.ear
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jca/wmq.jakarta.jmsra.rar $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jakarta.jmsra.rar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jakarta.jmsra.rar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jca/wmq.jmsra.rar $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jmsra.rar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jmsra.rar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.java_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.java_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.java_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.jms30.client_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.jms30.client_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.jms30.client_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclient_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclient_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclient_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclientprereqs_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclientprereqs_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclientprereqs_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.jms30.clientprereqs_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.jms30.clientprereqs_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.jms30.clientprereqs_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.commonservices.j2se_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.commonservices.j2se_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.commonservices.j2se_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms.prereq_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms.prereq_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms.prereq_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.nls_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.nls_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.nls_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.nls_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.nls_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.nls_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.prereq_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.prereq_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.prereq_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq_9.4.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq_9.4.0.0.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq_9.4.0.0.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/IVTRun $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTRun
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTRun
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/IVTSetup $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTSetup
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTSetup
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/IVTTidy $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTTidy
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTTidy
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/JMSAdmin $RPM_BUILD_ROOT/opt/mqm/java/bin/JMSAdmin
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/JMSAdmin
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/JMS30Admin $RPM_BUILD_ROOT/opt/mqm/java/bin/JMS30Admin
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/JMS30Admin
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/PSIVTRun $RPM_BUILD_ROOT/opt/mqm/java/bin/PSIVTRun
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/PSIVTRun
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/Cleanup $RPM_BUILD_ROOT/opt/mqm/java/bin/Cleanup
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/Cleanup
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/runjms $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/runjms64 $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms64
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms64
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/runjms30 $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms30
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms30
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/runjms30_64 $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms30_64
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms30_64
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/setjmsenv $RPM_BUILD_ROOT/opt/mqm/java/bin/setjmsenv
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/setjmsenv
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/setjms30env $RPM_BUILD_ROOT/opt/mqm/java/bin/setjms30env
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/setjms30env
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/setjms30env64 $RPM_BUILD_ROOT/opt/mqm/java/bin/setjms30env64
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/setjms30env64
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/setjmsenv64 $RPM_BUILD_ROOT/opt/mqm/java/bin/setjmsenv64
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/setjmsenv64
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/MQJMS_PSQ.mqsc $RPM_BUILD_ROOT/opt/mqm/java/bin/MQJMS_PSQ.mqsc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/MQJMS_PSQ.mqsc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/JMSAdmin.config $RPM_BUILD_ROOT/opt/mqm/java/bin/JMSAdmin.config
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/JMSAdmin.config
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/JMS30Admin.config $RPM_BUILD_ROOT/opt/mqm/java/bin/JMS30Admin.config
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/JMS30Admin.config
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/jms.config $RPM_BUILD_ROOT/opt/mqm/java/bin/jms.config
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/jms.config
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/mqjava.config $RPM_BUILD_ROOT/opt/mqm/java/bin/mqjava.config
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/mqjava.config
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/formatLog $RPM_BUILD_ROOT/opt/mqm/java/bin/formatLog
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/formatLog
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/PSReportDump.class $RPM_BUILD_ROOT/opt/mqm/java/bin/PSReportDump.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/PSReportDump.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jmscc/com.ibm.msg.client.commonservices.wmq.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/jmscc/com.ibm.msg.client.commonservices.wmq.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jmscc/com.ibm.msg.client.commonservices.wmq.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/runamscred $RPM_BUILD_ROOT/opt/mqm/java/bin/runamscred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/bin/runamscred
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCD.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCD.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCSP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCSP.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCSP.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCXP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCXP.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCXP.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQReceiveExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQReceiveExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSecurityExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSecurityExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSendExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSendExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/JmqiException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/JmqiException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/JmqiException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/BrokerCommandFailedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/BrokerCommandFailedException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/BrokerCommandFailedException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/Cleanup.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/Cleanup.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/Cleanup.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldNameException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldNameException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldNameException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldTypeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldTypeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldTypeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/IntErrorException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/IntErrorException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/IntErrorException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/ISSLException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/ISSLException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/ISSLException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSInvalidParameterException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSInvalidParameterException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSInvalidParameterException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSListenerSetException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSListenerSetException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSListenerSetException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSMessageQueueOverflowException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSMessageQueueOverflowException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSMessageQueueOverflowException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotActiveException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotActiveException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotActiveException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotSupportedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotSupportedException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotSupportedException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSParameterIsNullException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSParameterIsNullException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSParameterIsNullException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.ConnectionFactoryProperty.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.ConnectionFactoryProperty.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.ConnectionFactoryProperty.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionMetaData.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionMetaData.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionMetaData.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQDestination.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQDestination.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQDestination.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSAbstractIVT.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSAbstractIVT.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSAbstractIVT.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSLevel.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSLevel.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSLevel.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageConsumer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageConsumer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageProducer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageProducer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueBrowser.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueBrowser.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueBrowser.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueEnumeration.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueEnumeration.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueEnumeration.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueReceiver.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueReceiver.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueReceiver.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSender.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSender.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSender.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQRoot.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQRoot.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQRoot.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicPublisher.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicPublisher.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicPublisher.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSubscriber.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSubscriber.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSubscriber.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXASession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXASession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXASession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/NoBrokerResponseException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/NoBrokerResponseException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/NoBrokerResponseException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SessionClosedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SessionClosedException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SessionClosedException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SyntaxException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SyntaxException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SyntaxException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/MQException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/MQException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/MQException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQBC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQBC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQCFC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQCFC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQPSC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQPSC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQXC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQXC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQZC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQZC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrAdvancedCapability.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrAdvancedCapability.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrAdvancedCapability.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrSplCapability.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrSplCapability.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrSplCapability.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageEOFException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageEOFException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageEOFException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotReadableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotReadableException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotReadableException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsCapabilityContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsCapabilityContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsCapabilityContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionMetaData.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionMetaData.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionMetaData.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConsumer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConsumer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConvertableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConvertableException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConvertableException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsDestination.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsDestination.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsDestination.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsExceptionDetail.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsExceptionDetail.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsExceptionDetail.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsFactoryFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsFactoryFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsFactoryFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageConsumer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageConsumer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageProducer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageProducer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsProducer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsProducer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsPropertyContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsPropertyContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsPropertyContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueBrowser.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueBrowser.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueBrowser.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueReceiver.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueReceiver.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueReceiver.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSender.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSender.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSender.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsReadablePropertyContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsReadablePropertyContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsReadablePropertyContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicPublisher.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicPublisher.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicPublisher.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSubscriber.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSubscriber.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSubscriber.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXASession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXASession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXASession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Trace.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Trace.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Trace.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.Component.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.Component.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.Component.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/CommonConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/CommonConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/CommonConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/WMQConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/WMQConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/WMQConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSBytesMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSBytesMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSBytesMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMapMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMapMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMapMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSObjectMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSObjectMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSObjectMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSStreamMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSStreamMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSStreamMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSTextMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSTextMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSTextMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/package-list $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/package-list
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/package-list
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/overview-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/constant-values.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/constant-values.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/constant-values.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/serialized-form.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/serialized-form.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/serialized-form.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/overview-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/index-all.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/index-all.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/index-all.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/deprecated-list.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/deprecated-list.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/deprecated-list.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/allclasses-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/allclasses-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/allclasses-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/allclasses-noframe.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/allclasses-noframe.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/allclasses-noframe.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/index.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/index.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/index.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/overview-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/help-doc.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/help-doc.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/help-doc.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/stylesheet.css $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/stylesheet.css
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/stylesheet.css
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/script.js $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/script.js
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/script.js
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/errorcodes.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/errorcodes.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/errorcodes.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Trace.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Trace.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Trace.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Version.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Version.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Version.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Version.Component.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Version.Component.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Version.Component.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/CommonConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/CommonConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/CommonConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/WMQConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/WMQConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/WMQConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedIllegalStateException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedIllegalStateException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedIllegalStateException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedIllegalStateRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedIllegalStateRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedIllegalStateRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidClientIDException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidClientIDException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidClientIDException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidClientIDRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidClientIDRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidClientIDRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidDestinationException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidDestinationException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidDestinationException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidDestinationRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidDestinationRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidDestinationRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidSelectorException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidSelectorException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidSelectorException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidSelectorRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidSelectorRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidSelectorRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSSecurityException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSSecurityException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSSecurityException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSSecurityRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSSecurityRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSSecurityRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageEOFException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageEOFException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageEOFException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageFormatException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageFormatException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageFormatException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageFormatRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageFormatRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageFormatRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotReadableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotReadableException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotReadableException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotWriteableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotWriteableException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotWriteableException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotWriteableRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotWriteableRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotWriteableRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedResourceAllocationException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedResourceAllocationException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedResourceAllocationException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedResourceAllocationRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedResourceAllocationRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedResourceAllocationRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionInProgressException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionInProgressException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionInProgressException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionInProgressRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionInProgressRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionInProgressRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionRolledBackException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionRolledBackException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionRolledBackException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionRolledBackRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionRolledBackRuntimeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionRolledBackRuntimeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsCapabilityContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsCapabilityContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsCapabilityContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnectionMetaData.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnectionMetaData.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnectionMetaData.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConsumer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConsumer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConvertableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConvertableException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConvertableException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsDestination.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsDestination.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsDestination.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsExceptionDetail.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsExceptionDetail.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsExceptionDetail.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsFactoryFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsFactoryFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsFactoryFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessageConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessageConsumer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessageConsumer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessageProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessageProducer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessageProducer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsProducer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsProducer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsPropertyContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsPropertyContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsPropertyContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueBrowser.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueBrowser.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueBrowser.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueReceiver.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueReceiver.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueReceiver.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueSender.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueSender.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueSender.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsReadablePropertyContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsReadablePropertyContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsReadablePropertyContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTemporaryQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTemporaryQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTemporaryQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTemporaryTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTemporaryTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTemporaryTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicPublisher.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicPublisher.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicPublisher.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicSubscriber.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicSubscriber.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicSubscriber.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXASession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXASession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXASession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCD.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCD.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCSP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCSP.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCSP.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCXP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCXP.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCXP.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQReceiveExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQReceiveExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQSecurityExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQSecurityExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQSendExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQSendExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/BrokerCommandFailedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/BrokerCommandFailedException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/BrokerCommandFailedException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/Cleanup.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/Cleanup.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/Cleanup.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/FieldNameException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/FieldNameException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/FieldNameException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/FieldTypeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/FieldTypeException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/FieldTypeException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/IntErrorException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/IntErrorException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/IntErrorException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/ISSLException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/ISSLException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/ISSLException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSInvalidParameterException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSInvalidParameterException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSInvalidParameterException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSListenerSetException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSListenerSetException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSListenerSetException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSMessageQueueOverflowException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSMessageQueueOverflowException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSMessageQueueOverflowException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSNotActiveException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSNotActiveException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSNotActiveException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSNotSupportedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSNotSupportedException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSNotSupportedException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSParameterIsNullException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSParameterIsNullException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSParameterIsNullException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionFactory.ConnectionFactoryProperty.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionFactory.ConnectionFactoryProperty.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionFactory.ConnectionFactoryProperty.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionMetaData.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionMetaData.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionMetaData.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQDestination.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQDestination.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQDestination.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQJMSAbstractIVT.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQJMSAbstractIVT.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQJMSAbstractIVT.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQJMSLevel.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQJMSLevel.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQJMSLevel.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQMessageConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQMessageConsumer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQMessageConsumer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQMessageProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQMessageProducer.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQMessageProducer.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueBrowser.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueBrowser.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueBrowser.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueEnumeration.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueEnumeration.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueEnumeration.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueReceiver.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueReceiver.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueReceiver.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueSender.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueSender.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueSender.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQRoot.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQRoot.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQRoot.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTemporaryQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTemporaryQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTemporaryQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTemporaryTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTemporaryTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTemporaryTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicPublisher.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicPublisher.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicPublisher.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicSubscriber.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicSubscriber.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicSubscriber.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXASession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXASession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXASession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicConnection.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicConnection.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicConnectionFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicConnectionFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicSession.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicSession.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/NoBrokerResponseException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/NoBrokerResponseException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/NoBrokerResponseException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/SessionClosedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/SessionClosedException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/SessionClosedException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/SyntaxException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/SyntaxException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/SyntaxException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/JmqiException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/JmqiException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/JmqiException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/MQException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/MQException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/MQException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQBC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQBC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQCFC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQCFC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQPSC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQPSC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQXC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQXC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQZC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQZC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.FieldValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.FieldValueComparator.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.FieldValueComparator.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.ValueValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.ValueValueComparator.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.ValueValueComparator.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQPropertyIdentifiers.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQPropertyIdentifiers.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQPropertyIdentifiers.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/QmgrAdvancedCapability.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/QmgrAdvancedCapability.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/QmgrAdvancedCapability.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/QmgrSplCapability.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/QmgrSplCapability.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/QmgrSplCapability.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSBytesMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSBytesMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSBytesMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSMapMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSMapMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSMapMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSObjectMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSObjectMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSObjectMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSStreamMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSStreamMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSStreamMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSTextMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSTextMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSTextMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/package-list $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/package-list
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/package-list
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/overview-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/overview-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/overview-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/constant-values.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/constant-values.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/constant-values.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/serialized-form.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/serialized-form.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/serialized-form.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/overview-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/overview-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/overview-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/index-all.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/index-all.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/index-all.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/deprecated-list.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/deprecated-list.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/deprecated-list.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/allclasses-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/allclasses-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/allclasses-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/allclasses-noframe.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/allclasses-noframe.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/allclasses-noframe.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/index.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/index.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/index.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/overview-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/overview-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/overview-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/help-doc.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/help-doc.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/help-doc.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/stylesheet.css $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/stylesheet.css
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/stylesheet.css
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/script.js $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/script.js
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/script.js
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMS30Classes/errorcodes.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/errorcodes.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMS30Classes/errorcodes.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQBC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQBC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQCFC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQCFC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQPSC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQPSC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQXC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQXC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQZC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQZC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBF.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBF.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBS.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBS.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBS.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFGR.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFGR.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFGR.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIF.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIF.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL64.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL64.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL64.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN64.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN64.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN64.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSF.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSF.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSL.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSL.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSL.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFST.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFST.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFST.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFAgent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFAgent.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFAgent.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFContent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFContent.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFContent.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFFilterParameter.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFFilterParameter.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFFilterParameter.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeader.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeader.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeader.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeaderFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeaderFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeaderFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessageAgent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessageAgent.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessageAgent.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFParameter.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFParameter.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFParameter.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCD.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCD.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCSP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCSP.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCSP.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCXP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCXP.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCXP.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQReceiveExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQReceiveExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSecurityExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSecurityExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSendExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSendExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CCSID.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CCSID.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CCSID.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQBC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQBC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQCFC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQCFC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQPSC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQPSC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQXC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQXC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQZC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQZC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBF.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBF.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBS.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBS.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBS.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFGR.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFGR.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFGR.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIF.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIF.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL64.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL64.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL64.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN64.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN64.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN64.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSF.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSF.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSL.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSL.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSL.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFST.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFST.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFST.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQEPH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQEPH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQEPH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFAgent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFAgent.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFAgent.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFContent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFContent.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFContent.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFFilterParameter.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFFilterParameter.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFFilterParameter.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeader.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeader.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeader.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeaderFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeaderFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeaderFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgent.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgent.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgentResponseTracker.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgentResponseTracker.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgentResponseTracker.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFParameter.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFParameter.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFParameter.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CCSID.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CCSID.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CCSID.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/Charsets.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/Charsets.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/Charsets.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQBC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQBC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQCFC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQCFC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQPSC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQPSC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQXC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQXC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQZC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQZC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQChainable.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQChainable.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQChainable.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQCIH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQCIH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQCIH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQData.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQData.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQData.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDataException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDataException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDataException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDLH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDLH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDLH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.Field.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.Field.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.Field.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderContext.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderContext.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.Registry.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.Registry.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.Registry.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderIterator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderIterator.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderIterator.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderList.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderList.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderList.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderRegistry.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderRegistry.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderRegistry.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQIIH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQIIH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQIIH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD1.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD1.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD1.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMDE.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMDE.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMDE.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.NameValuePair.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.NameValuePair.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.NameValuePair.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.Element.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.Element.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.Element.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRMH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRMH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRMH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQSAPH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQSAPH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQSAPH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM2.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM2.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM2.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTMC2.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTMC2.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTMC2.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQWIH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQWIH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQWIH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQXQH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQXQH.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQXQH.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/JmqiException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/JmqiException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/JmqiException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/JmqiSESSION.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/JmqiSESSION.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/JmqiSESSION.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQAsyncStatus.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQAsyncStatus.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQAsyncStatus.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelDefinition.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelDefinition.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelDefinition.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQConnectionSecurityParameters.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQConnectionSecurityParameters.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQConnectionSecurityParameters.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDestination.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDestination.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDestination.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionList.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionList.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionList.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionListItem.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionListItem.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionListItem.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQEnvironment.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQEnvironment.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQEnvironment.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQException.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQException.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExitChain.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExitChain.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExitChain.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalReceiveExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalReceiveExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSecurityExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSecurityExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSendExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSendExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalUserExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalUserExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalUserExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQGetMessageOptions.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQGetMessageOptions.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQGetMessageOptions.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaComponent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaComponent.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaComponent.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaLevel.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaLevel.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaLevel.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQManagedObject.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQManagedObject.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQManagedObject.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMD.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMD.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMessage.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMessage.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQOD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQOD.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQOD.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPoolToken.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPoolToken.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPoolToken.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQProcess.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQProcess.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQProcess.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPropertyDescriptor.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPropertyDescriptor.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPropertyDescriptor.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPutMessageOptions.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPutMessageOptions.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPutMessageOptions.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueue.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueue.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueueManager.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueueManager.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueueManager.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExitChain.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExitChain.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExitChain.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSecurityExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSecurityExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExit.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExit.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExitChain.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExitChain.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExitChain.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSimpleConnectionManager.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSimpleConnectionManager.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSimpleConnectionManager.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSubscription.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSubscription.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSubscription.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQTopic.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQTopic.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQBC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQBC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQCFC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQCFC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQPSC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQPSC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQXC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQXC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQZC.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQZC.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrAdvancedCapability.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrAdvancedCapability.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrAdvancedCapability.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrSplCapability.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrSplCapability.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrSplCapability.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/package-list $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/package-list
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/package-list
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/overview-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/constant-values.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/constant-values.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/constant-values.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/serialized-form.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/serialized-form.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/serialized-form.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/overview-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-tree.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-tree.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/index-all.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/index-all.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/index-all.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/deprecated-list.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/deprecated-list.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/deprecated-list.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/allclasses-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/allclasses-frame.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/allclasses-frame.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/allclasses-noframe.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/allclasses-noframe.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/allclasses-noframe.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/index.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/index.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/index.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/overview-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-summary.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-summary.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/help-doc.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/help-doc.html
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/help-doc.html
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/stylesheet.css $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/stylesheet.css
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/stylesheet.css
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/script.js $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/script.js
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/script.js

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/jca"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/OSGi"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/modules"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/modules/javax"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/jmscc"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Java_Messaging-9.4.0.mqtag"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib/libmqjexitstub02.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib64/libmqjexitstub02.so"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/bcprov-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/bcpkix-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/bcutil-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/javax/bcprov-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/javax/bcpkix-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/javax/bcutil-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta/bcprov-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta/bcpkix-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta/bcutil-jdk18on.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.headers.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.pcf.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.jmqi.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mqjms.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.traceControl.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.allclient.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.jakarta.client.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/javax/com.ibm.mq.allclient.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta/com.ibm.mq.jakarta.client.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/fscontext.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/providerutil.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/javax/fscontext.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/javax/providerutil.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta/fscontext.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta/providerutil.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/org.json.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/javax/org.json.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta/org.json.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jms.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jakarta.jms-api.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/javax/jms.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/modules/jakarta/jakarta.jms-api.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jca/wmq.jmsra.ivt.ear"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jca/wmq.jakarta.jmsra.ivt.ear"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jca/wmq.jakarta.jmsra.rar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jca/wmq.jmsra.rar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.java_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.jms30.client_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclient_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclientprereqs_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.jms30.clientprereqs_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.commonservices.j2se_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms.prereq_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.nls_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.nls_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.prereq_9.4.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq_9.4.0.0.jar"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/IVTRun"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/IVTSetup"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/IVTTidy"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/JMSAdmin"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/JMS30Admin"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/PSIVTRun"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/Cleanup"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/runjms"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/runjms64"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/runjms30"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/runjms30_64"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/setjmsenv"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/setjms30env"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/setjms30env64"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/setjmsenv64"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/MQJMS_PSQ.mqsc"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/JMSAdmin.config"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/JMS30Admin.config"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/jms.config"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/mqjava.config"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/formatLog"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/PSReportDump.class"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jmscc/com.ibm.msg.client.commonservices.wmq.jar"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/runamscred"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCSP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCXP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/JmqiException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/BrokerCommandFailedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/Cleanup.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldNameException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldTypeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/IntErrorException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/ISSLException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSInvalidParameterException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSListenerSetException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSMessageQueueOverflowException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotActiveException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotSupportedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSParameterIsNullException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.ConnectionFactoryProperty.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionMetaData.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQDestination.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSAbstractIVT.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSLevel.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueBrowser.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueEnumeration.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueReceiver.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSender.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQRoot.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicPublisher.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSubscriber.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXASession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/NoBrokerResponseException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SessionClosedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SyntaxException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/MQException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrAdvancedCapability.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrSplCapability.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageEOFException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotReadableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsCapabilityContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionMetaData.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConvertableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsDestination.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsExceptionDetail.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsFactoryFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsPropertyContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueBrowser.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueReceiver.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSender.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsReadablePropertyContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicPublisher.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSubscriber.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXASession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Trace.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.Component.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/CommonConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/WMQConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSBytesMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMapMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSObjectMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSStreamMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSTextMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/package-list"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/overview-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/constant-values.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/serialized-form.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/overview-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/index-all.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/deprecated-list.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/allclasses-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/allclasses-noframe.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/index.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/overview-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/help-doc.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/stylesheet.css"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/script.js"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/errorcodes.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Trace.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Version.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/Version.Component.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/services/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/CommonConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/common/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/WMQConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/wmq/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedIllegalStateException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedIllegalStateRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidClientIDException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidClientIDRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidDestinationException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidDestinationRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidSelectorException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedInvalidSelectorRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSSecurityException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedJMSSecurityRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageEOFException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageFormatException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageFormatRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotReadableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotWriteableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedMessageNotWriteableRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedResourceAllocationException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedResourceAllocationRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionInProgressException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionInProgressRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionRolledBackException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/DetailedTransactionRolledBackRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsCapabilityContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConnectionMetaData.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsConvertableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsDestination.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsExceptionDetail.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsFactoryFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessageConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsMessageProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsPropertyContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueBrowser.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueReceiver.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueSender.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsReadablePropertyContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTemporaryQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTemporaryTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicPublisher.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsTopicSubscriber.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXAQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXASession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/JmsXATopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/msg/client/jakarta/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCSP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/MQCXP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/WMQSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/exits/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/BrokerCommandFailedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/Cleanup.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/FieldNameException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/FieldTypeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/IntErrorException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/ISSLException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSInvalidParameterException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSListenerSetException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSMessageQueueOverflowException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSNotActiveException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSNotSupportedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/JMSParameterIsNullException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionFactory.ConnectionFactoryProperty.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQConnectionMetaData.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQDestination.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQJMSAbstractIVT.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQJMSLevel.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQMessageConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQMessageProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueBrowser.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueEnumeration.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueReceiver.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueSender.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQRoot.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTemporaryQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTemporaryTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicPublisher.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQTopicSubscriber.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXAQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXASession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/MQXATopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/NoBrokerResponseException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/SessionClosedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/SyntaxException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jakarta/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/JmqiException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/jmqi/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/MQException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.FieldValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQConstants.ValueValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/MQPropertyIdentifiers.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/QmgrAdvancedCapability.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/QmgrSplCapability.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/constants/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/mq/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSBytesMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSMapMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSObjectMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSStreamMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/JMSTextMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/com/ibm/jakarta/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/package-list"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/overview-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/constant-values.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/serialized-form.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/overview-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/index-all.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/deprecated-list.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/allclasses-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/allclasses-noframe.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/index.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/overview-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/help-doc.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/stylesheet.css"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/script.js"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMS30Classes/errorcodes.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBS.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFGR.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL64.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN64.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSL.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFST.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFAgent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFContent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFFilterParameter.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeader.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeaderFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessageAgent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFParameter.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCSP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCXP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CCSID.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBS.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFGR.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL64.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN64.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSL.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFST.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQEPH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFAgent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFContent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFFilterParameter.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeader.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeaderFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgentResponseTracker.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFParameter.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CCSID.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/Charsets.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQChainable.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQCIH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQData.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDataException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDLH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.Field.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.Registry.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderIterator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderList.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderRegistry.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQIIH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD1.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMDE.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.NameValuePair.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.Element.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRMH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQSAPH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM2.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTMC2.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQWIH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQXQH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/JmqiException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/JmqiSESSION.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQAsyncStatus.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelDefinition.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQConnectionSecurityParameters.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDestination.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionList.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionListItem.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQEnvironment.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExitChain.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalUserExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQGetMessageOptions.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaComponent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaLevel.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQManagedObject.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQOD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPoolToken.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQProcess.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPropertyDescriptor.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPutMessageOptions.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueueManager.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExitChain.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExitChain.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSimpleConnectionManager.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSubscription.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrAdvancedCapability.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrSplCapability.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/package-list"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/overview-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/constant-values.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/serialized-form.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/overview-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/index-all.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/deprecated-list.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/allclasses-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/allclasses-noframe.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/index.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/overview-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/help-doc.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/stylesheet.css"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/script.js"

%pre
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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

%preun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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
fi

%postun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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

