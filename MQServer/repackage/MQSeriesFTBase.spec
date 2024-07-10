Summary: IBM MQ Managed File Transfer Base Component
Name: MQSeriesFTBase
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
This package provides the common IBM MQ Managed File Transfer
functionality which is used by all the other Managed File Transfer components.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/mqft
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/lib
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/credentials
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/email
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/hub
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/timeout
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/zip
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Base-9.4.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Base-9.4.0.mqtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Base-9.4.0.mqtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/INSTALL $RPM_BUILD_ROOT/opt/mqm/mqft/ant/INSTALL
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/INSTALL
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/KEYS $RPM_BUILD_ROOT/opt/mqm/mqft/ant/KEYS
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/KEYS
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/LICENSE $RPM_BUILD_ROOT/opt/mqm/mqft/ant/LICENSE
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/LICENSE
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/NOTICE $RPM_BUILD_ROOT/opt/mqm/mqft/ant/NOTICE
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/NOTICE
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/README $RPM_BUILD_ROOT/opt/mqm/mqft/ant/README
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/README
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/WHATSNEW $RPM_BUILD_ROOT/opt/mqm/mqft/ant/WHATSNEW
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/WHATSNEW
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/CONTRIBUTORS $RPM_BUILD_ROOT/opt/mqm/mqft/ant/CONTRIBUTORS
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/CONTRIBUTORS
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/contributors.xml $RPM_BUILD_ROOT/opt/mqm/mqft/ant/contributors.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/contributors.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/patch.xml $RPM_BUILD_ROOT/opt/mqm/mqft/ant/patch.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/patch.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/ant $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/ant.bat $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant.bat
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant.bat
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/ant.cmd $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant.cmd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant.cmd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/antRun $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/antRun.bat $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun.bat
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun.bat
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/antRun.pl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun.pl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun.pl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/antenv.cmd $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antenv.cmd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antenv.cmd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/complete-ant-cmd.pl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/complete-ant-cmd.pl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/complete-ant-cmd.pl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/envset.cmd $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/envset.cmd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/envset.cmd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/lcp.bat $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/lcp.bat
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/lcp.bat
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/runant.pl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runant.pl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runant.pl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/runant.py $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runant.py
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runant.py
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/runrc.cmd $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runrc.cmd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runrc.cmd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/ant-bootstrap.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/ant-bootstrap.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/ant-bootstrap.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/changelog.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/changelog.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/changelog.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-text.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-text.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-text.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-xdoc.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-xdoc.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-xdoc.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames-sortby-check.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames-sortby-check.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames-sortby-check.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/coverage-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/coverage-frames.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/coverage-frames.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/jdepend-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/jdepend-frames.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/jdepend-frames.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/jdepend.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/jdepend.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/jdepend.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/junit-frames-xalan1.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-frames-xalan1.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-frames-xalan1.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/junit-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-frames.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-frames.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/junit-noframes.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-noframes.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-noframes.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/log.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/log.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/log.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/maudit-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/maudit-frames.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/maudit-frames.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/mmetrics-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/mmetrics-frames.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/mmetrics-frames.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/tagdiff.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/tagdiff.xsl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/tagdiff.xsl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/fetch.xml $RPM_BUILD_ROOT/opt/mqm/mqft/ant/fetch.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/fetch.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/get-m2.xml $RPM_BUILD_ROOT/opt/mqm/mqft/ant/get-m2.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/get-m2.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/README $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/README
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/README
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-antlr.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-antlr.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-antlr.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-antlr.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-antlr.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-antlr.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-bcel.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bcel.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bcel.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-bcel.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bcel.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bcel.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-bsf.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bsf.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bsf.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-bsf.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bsf.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bsf.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-log4j.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-log4j.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-log4j.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-log4j.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-log4j.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-log4j.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-oro.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-oro.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-oro.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-oro.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-oro.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-oro.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-regexp.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-regexp.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-regexp.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-regexp.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-regexp.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-regexp.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-resolver.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-resolver.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-resolver.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-resolver.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-resolver.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-resolver.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-xalan2.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-xalan2.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-xalan2.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-xalan2.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-xalan2.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-xalan2.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-commons-logging.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-logging.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-logging.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-commons-logging.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-logging.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-logging.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-commons-net.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-net.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-net.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-commons-net.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-net.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-net.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jai.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jai.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jai.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jai.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jai.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jai.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-javamail.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-javamail.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-javamail.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-javamail.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-javamail.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-javamail.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jdepend.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jdepend.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jdepend.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jdepend.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jdepend.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jdepend.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jmf.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jmf.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jmf.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jmf.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jmf.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jmf.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jsch.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jsch.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jsch.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jsch.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jsch.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jsch.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junit.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junit.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junit4.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit4.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit4.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junit4.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit4.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit4.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-launcher.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-launcher.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-launcher.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-launcher.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-launcher.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-launcher.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-netrexx.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-netrexx.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-netrexx.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-netrexx.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-netrexx.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-netrexx.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-parent.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-parent.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-parent.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-swing.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-swing.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-swing.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-swing.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-swing.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-swing.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-testutil.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-testutil.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-testutil.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-testutil.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-testutil.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-testutil.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/libraries.properties $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/libraries.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/libraries.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junitlauncher.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junitlauncher.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junitlauncher.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junitlauncher.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junitlauncher.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junitlauncher.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-weblogic.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-weblogic.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-weblogic.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-xz.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-xz.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-xz.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-xz.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-xz.pom
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-xz.pom
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/xercesImpl.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/xercesImpl.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/xercesImpl.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/xml-apis.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/xml-apis.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/xml-apis.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.ant.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.ant.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.ant.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.bootstrap.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.bootstrap.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.bootstrap.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.cmdline.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.cmdline.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.cmdline.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.common.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.common.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.common.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.daemon.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.daemon.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.daemon.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.databaselogger.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.databaselogger.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.databaselogger.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.exitroutines.api.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.exitroutines.api.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.exitroutines.api.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.native.jni.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.native.jni.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.native.jni.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/logging.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/logging.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/logging.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_cs.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_cs.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_cs.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_cs.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_cs.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_cs.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_cs.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_cs.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_cs.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_cs.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_cs.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_cs.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_de.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_de.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_de.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_de.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_de.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_de.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_de.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_de.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_de.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_de.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_de.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_de.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_es.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_es.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_es.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_es.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_es.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_es.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_es.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_es.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_es.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_es.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_es.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_es.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_fr.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_fr.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_fr.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_fr.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_fr.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_fr.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_fr.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_fr.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_fr.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_fr.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_fr.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_fr.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_hu.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_hu.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_hu.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_hu.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_hu.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_hu.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_hu.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_hu.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_hu.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_hu.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_hu.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_hu.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_it.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_it.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_it.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_it.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_it.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_it.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_it.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_it.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_it.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_it.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_it.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_it.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_ja.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_ja.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_ja.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_ja.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_ja.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_ja.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_ja.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_ja.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_ja.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_ja.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_ja.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_ja.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_ko.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_ko.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_ko.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_ko.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_ko.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_ko.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_ko.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_ko.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_ko.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_ko.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_ko.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_ko.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_pl.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_pl.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_pl.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_pl.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_pl.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_pl.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_pl.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_pl.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_pl.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_pl.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_pl.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_pl.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_pt_BR.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_pt_BR.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_pt_BR.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_pt_BR.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_pt_BR.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_pt_BR.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_pt_BR.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_pt_BR.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_pt_BR.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_pt_BR.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_pt_BR.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_pt_BR.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_ru.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_ru.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_ru.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_ru.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_ru.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_ru.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_ru.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_ru.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_ru.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_ru.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_ru.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_ru.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_zh_CN.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_zh_CN.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_zh_CN.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_zh_CN.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_zh_CN.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_zh_CN.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_zh_CN.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_zh_CN.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_zh_CN.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_zh_CN.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_zh_CN.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_zh_CN.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements_zh_TW.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_zh_TW.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements_zh_TW.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages_zh_TW.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_zh_TW.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages_zh_TW.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements_zh_TW.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_zh_TW.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements_zh_TW.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages_zh_TW.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_zh_TW.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages_zh_TW.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib64/libmqmft.so $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/libmqmft.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/libmqmft.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-beanutils.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-beanutils.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-beanutils.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-collections.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-collections.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-collections.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-digester.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-digester.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-digester.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-io.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-io.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-io.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-lang.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-lang.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-lang.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-logging.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-logging.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-logging.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-net.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-net.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-net.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/icu4j.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/icu4j-charset.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j-charset.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j-charset.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/icu4j-localespi.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j-localespi.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j-localespi.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib64/libmqmftpc.so $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/libmqmftpc.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/libmqmftpc.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib64/mqmftpc $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/mqmftpc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/mqmftpc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/credentials/MQMFTCredentials.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/credentials/MQMFTCredentials.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/credentials/MQMFTCredentials.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/email/email.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/email/email.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/email/email.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/hub/hubcopy.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/hub/hubcopy.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/hub/hubcopy.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/hub/hubprocess.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/hub/hubprocess.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/hub/hubprocess.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/timeout/timeout.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/timeout/timeout.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/timeout/timeout.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/zip/zip.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/zip/zip.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/zip/zip.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/zip/zipfiles.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/zip/zipfiles.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/zip/zipfiles.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/4690/basic.zip $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/basic.zip
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/basic.zip
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/4690/custom1.zip $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/custom1.zip
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/custom1.zip
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/4690/custom2.zip $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/custom2.zip
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/custom2.zip
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/4690/SSL.zip $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/SSL.zip
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/SSL.zip
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Trace.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Trace.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Trace.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/AgentTraceStatus.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/AgentTraceStatus.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/AgentTraceStatus.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ConnectDirectCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectCredentials.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectCredentials.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ConnectDirectNodeProperties.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectNodeProperties.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectNodeProperties.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ConnectDirectProcessDefinitions.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectProcessDefinitions.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectProcessDefinitions.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/FileLoggerFormat.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileLoggerFormat.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileLoggerFormat.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/FileSpaceInfo.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileSpaceInfo.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileSpaceInfo.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/FileTransfer.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileTransfer.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileTransfer.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Filespace.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Filespace.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Filespace.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Internal.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Internal.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Internal.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Log.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Log.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Log.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Monitor.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Monitor.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Monitor.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/MonitorList.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MonitorList.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MonitorList.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/MonitorLog.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MonitorLog.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MonitorLog.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/MQMFTCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MQMFTCredentials.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MQMFTCredentials.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Notification.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Notification.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Notification.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/PingAgent.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/PingAgent.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/PingAgent.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ProtocolBridgeCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ProtocolBridgeCredentials.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ProtocolBridgeCredentials.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ProtocolBridgeProperties.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ProtocolBridgeProperties.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ProtocolBridgeProperties.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Reply.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Reply.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Reply.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ScheduleList.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ScheduleList.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ScheduleList.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ScheduleLog.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ScheduleLog.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ScheduleLog.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/TransferLog.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/TransferLog.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/TransferLog.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/TransferStatus.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/TransferStatus.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/TransferStatus.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/UserInfo.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/UserInfo.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/UserInfo.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/UserSandboxes.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/UserSandboxes.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/UserSandboxes.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/fteutils.xjb $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/fteutils.xjb
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/fteutils.xjb
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/fteutils.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/fteutils.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/fteutils.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectCredentials.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectCredentials.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectNodeProperties.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectNodeProperties.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectNodeProperties.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeCredentials.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeCredentials.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeProperties.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeProperties.xsd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeProperties.xsd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteChangeDefaultConfigurationOptions $RPM_BUILD_ROOT/opt/mqm/bin/fteChangeDefaultConfigurationOptions
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/fteChangeDefaultConfigurationOptions
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteCommon $RPM_BUILD_ROOT/opt/mqm/bin/fteCommon
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/fteCommon
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteDisplayVersion $RPM_BUILD_ROOT/opt/mqm/bin/fteDisplayVersion
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/fteDisplayVersion
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteObfuscate $RPM_BUILD_ROOT/opt/mqm/bin/fteObfuscate
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/fteObfuscate
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/ftePlatform $RPM_BUILD_ROOT/opt/mqm/bin/ftePlatform
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/ftePlatform
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteSetupCommands $RPM_BUILD_ROOT/opt/mqm/bin/fteSetupCommands
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/fteSetupCommands
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteSetupCoordination $RPM_BUILD_ROOT/opt/mqm/bin/fteSetupCoordination
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/fteSetupCoordination
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteListAgents $RPM_BUILD_ROOT/opt/mqm/bin/fteListAgents
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/fteListAgents
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteShowAgentDetails $RPM_BUILD_ROOT/opt/mqm/bin/fteShowAgentDetails
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/fteShowAgentDetails

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,bin,bin) "/opt/mqm/mqft"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant/bin"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant/etc"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant/lib"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/lib"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/lib/messages"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/lib64"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/credentials"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant/email"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant/hub"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant/timeout"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant/zip"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/4690"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/schema"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Base-9.4.0.mqtag"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/INSTALL"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/KEYS"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/LICENSE"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/NOTICE"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/README"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/WHATSNEW"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/CONTRIBUTORS"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/contributors.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/patch.xml"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/ant"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/ant.bat"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/ant.cmd"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/antRun"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/antRun.bat"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/antRun.pl"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/antenv.cmd"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/complete-ant-cmd.pl"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/envset.cmd"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/lcp.bat"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/runant.pl"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/runant.py"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/runrc.cmd"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/ant-bootstrap.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/changelog.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-text.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-xdoc.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames-sortby-check.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/coverage-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/jdepend-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/jdepend.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/junit-frames-xalan1.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/junit-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/junit-noframes.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/log.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/maudit-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/mmetrics-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/tagdiff.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/fetch.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/get-m2.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/README"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-antlr.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-antlr.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-bcel.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-bcel.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-bsf.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-bsf.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-log4j.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-log4j.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-oro.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-oro.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-regexp.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-regexp.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-resolver.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-resolver.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-xalan2.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-xalan2.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-commons-logging.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-commons-logging.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-commons-net.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-commons-net.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jai.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jai.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-javamail.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-javamail.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jdepend.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jdepend.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jmf.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jmf.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jsch.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jsch.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junit.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junit.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junit4.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junit4.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-launcher.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-launcher.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-netrexx.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-netrexx.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-parent.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-swing.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-swing.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-testutil.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-testutil.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/libraries.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junitlauncher.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junitlauncher.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-weblogic.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-xz.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-xz.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/xercesImpl.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/xml-apis.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.ant.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.bootstrap.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.cmdline.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.common.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.daemon.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.databaselogger.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.exitroutines.api.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.native.jni.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/logging.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_cs.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_cs.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_cs.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_cs.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_de.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_de.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_de.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_de.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_es.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_es.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_es.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_es.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_fr.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_fr.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_fr.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_fr.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_hu.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_hu.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_hu.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_hu.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_it.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_it.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_it.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_it.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_ja.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_ja.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_ja.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_ja.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_ko.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_ko.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_ko.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_ko.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_pl.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_pl.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_pl.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_pl.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_pt_BR.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_pt_BR.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_pt_BR.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_pt_BR.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_ru.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_ru.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_ru.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_ru.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_zh_CN.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_zh_CN.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_zh_CN.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_zh_CN.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements_zh_TW.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages_zh_TW.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements_zh_TW.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages_zh_TW.properties"
%attr(555,bin,bin) %verify(not md5 mtime) "/opt/mqm/mqft/lib64/libmqmft.so"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-beanutils.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-collections.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-digester.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-io.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-lang.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-logging.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-net.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/icu4j.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/icu4j-charset.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/icu4j-localespi.jar"
%attr(555,bin,bin) %verify(not md5 mtime) "/opt/mqm/mqft/lib64/libmqmftpc.so"
%attr(555,bin,bin) %verify(not md5 mtime) "/opt/mqm/mqft/lib64/mqmftpc"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/credentials/MQMFTCredentials.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/email/email.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/hub/hubcopy.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/hub/hubprocess.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/timeout/timeout.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/zip/zip.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/zip/zipfiles.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/4690/basic.zip"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/4690/custom1.zip"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/4690/custom2.zip"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/4690/SSL.zip"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Trace.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/AgentTraceStatus.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ConnectDirectCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ConnectDirectNodeProperties.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ConnectDirectProcessDefinitions.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/FileLoggerFormat.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/FileSpaceInfo.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/FileTransfer.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Filespace.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Internal.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Log.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Monitor.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/MonitorList.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/MonitorLog.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/MQMFTCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Notification.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/PingAgent.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ProtocolBridgeCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ProtocolBridgeProperties.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Reply.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ScheduleList.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ScheduleLog.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/TransferLog.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/TransferStatus.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/UserInfo.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/UserSandboxes.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/fteutils.xjb"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/fteutils.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectNodeProperties.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeProperties.xsd"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteChangeDefaultConfigurationOptions"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteCommon"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteDisplayVersion"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteObfuscate"
%attr(555,mqm,mqm) "/opt/mqm/bin/ftePlatform"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteSetupCommands"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteSetupCoordination"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteListAgents"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteShowAgentDetails"

%pre
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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

