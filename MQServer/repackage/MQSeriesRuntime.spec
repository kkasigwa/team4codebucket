Summary: IBM MQ Runtime FileSet
Name: MQSeriesRuntime
Version: 9.4.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Conflicts: 	                  MQSeriesHtml_base = 5.2.0-0
Conflicts:  	                  MQSeriesDMQRuntime = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_en = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_de = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_es = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_fr = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_it = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_ja = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_ko = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_pt = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_Zh_CN = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_Zh_TW = 5.2.0-0
Conflicts:  	                  MQSeriesClient < 7.0.0-0
Conflicts:  	                  MQSeriesJava <  7.0.0-0
Conflicts:  	                  MQSeriesKeyMan  < 7.0.0-0
Conflicts: 	                  MQSeriesGSKit  < 7.0.0-0
Conflicts:  	                  MQSeriesMan < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_de < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_es < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_fr < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_it < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_ja < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_ko < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_pt < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_Zh_CN < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_Zh_TW < 7.0.0-0
Conflicts:  	                  MQSeriesSamples < 7.0.0-0
Conflicts:  	                  MQSeriesSDK < 7.0.0-0
Conflicts:  	                  MQSeriesServer < 7.0.0-0
Conflicts:  	                  MQSeriesRuntime < 7.0.0-0
Conflicts:  	                  MQSeriesXRService < 7.0.0-0
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
This package provides the common files to both IBM MQ client and server
installations, and is a prerequisite package of all other IBM MQ
packages.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/lib
install -d $RPM_BUILD_ROOT/opt/mqm/lib/compat
install -d $RPM_BUILD_ROOT/opt/mqm/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/lib64/compat
install -d $RPM_BUILD_ROOT/opt/mqm/java
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib
install -d $RPM_BUILD_ROOT/opt/mqm/samp
install -d $RPM_BUILD_ROOT/opt/mqm/samp/web
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/lib/iconv
install -d $RPM_BUILD_ROOT/opt/mqm/msg
install -d $RPM_BUILD_ROOT/opt/mqm/msg/en_US
install -d $RPM_BUILD_ROOT/opt/mqm/READMES
install -d $RPM_BUILD_ROOT/opt/mqm/licenses
install -d $RPM_BUILD_ROOT/opt/mqm/lap
install -d $RPM_BUILD_ROOT/opt/mqm/lap/licenses
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/samp/mqccred
install -d $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib
install -d $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib64
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqm.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqm.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqm.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqm.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqm.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqm.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcs.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcs.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcs.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcs.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcs.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcs.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqe.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqe.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqe.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqe.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqe.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqe.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqecs.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqecs.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqecs.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqecs.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqecs.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqecs.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqxzu.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqxzu.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqxzu.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqxzu.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqxzu.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqxzu.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqzsd.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqzsd.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqzsd.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqzsd.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzsd.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzsd.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqz.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqz.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqz.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqz.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqz.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqz.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqm_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqm_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqm_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqm_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqm_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqm_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcs_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcs_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcs_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcs_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcs_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcs_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqe_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqe_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqe_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqe_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqe_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqe_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqecs_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqecs_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqecs_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqecs_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqecs_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqecs_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqxzu_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqxzu_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqxzu_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqxzu_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqxzu_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqxzu_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqzsd_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqzsd_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqzsd_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqzsd_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzsd_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzsd_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqz_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqz_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqz_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqz_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqz_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqz_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqjx_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqjx_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqjx_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqjx_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjx_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjx_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqjxx_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxx_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxx_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqjxx_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxx_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxx_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/ffstsummary $RPM_BUILD_ROOT/opt/mqm/bin/ffstsummary
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/ffstsummary
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqltmc0 $RPM_BUILD_ROOT/opt/mqm/bin/amqltmc0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqltmc0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqltmc064 $RPM_BUILD_ROOT/opt/mqm/bin/amqltmc064
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqltmc064
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqb23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqb23gl.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libimqb23gl.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqb23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqb23gl_r.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libimqb23gl_r.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqb23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqb23gl.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libimqb23gl.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqb23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqb23gl_r.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libimqb23gl_r.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/ccsid.tbl $RPM_BUILD_ROOT/opt/mqm/samp/ccsid.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/ccsid.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/ccsid_part2.tbl $RPM_BUILD_ROOT/opt/mqm/samp/ccsid_part2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/ccsid_part2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/ccsid.new $RPM_BUILD_ROOT/opt/mqm/samp/ccsid.new
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/ccsid.new
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqs.ini $RPM_BUILD_ROOT/opt/mqm/samp/mqs.ini
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqs.ini
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqclient.ini $RPM_BUILD_ROOT/opt/mqm/samp/mqclient.ini
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqclient.ini
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/service.env $RPM_BUILD_ROOT/opt/mqm/samp/service.env
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/service.env
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/web/mqwebuser.xml $RPM_BUILD_ROOT/opt/mqm/samp/web/mqwebuser.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/web/mqwebuser.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/web/server.xml $RPM_BUILD_ROOT/opt/mqm/samp/web/server.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/web/server.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/web/jvm.options $RPM_BUILD_ROOT/opt/mqm/samp/web/jvm.options
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/web/jvm.options
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/strmqtrc $RPM_BUILD_ROOT/opt/mqm/bin/strmqtrc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/strmqtrc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqtrc $RPM_BUILD_ROOT/opt/mqm/bin/endmqtrc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/endmqtrc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqras $RPM_BUILD_ROOT/opt/mqm/bin/dspmqras
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqras
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqtrc $RPM_BUILD_ROOT/opt/mqm/bin/dspmqtrc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqtrc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqtrc.fmt $RPM_BUILD_ROOT/opt/mqm/lib/amqtrc.fmt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqtrc.fmt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/ccdt_schema.json $RPM_BUILD_ROOT/opt/mqm/lib/ccdt_schema.json
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/ccdt_schema.json
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqxdbg $RPM_BUILD_ROOT/opt/mqm/bin/amqxdbg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqxdbg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqxmsg0 $RPM_BUILD_ROOT/opt/mqm/bin/amqxmsg0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqxmsg0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqicdir $RPM_BUILD_ROOT/opt/mqm/bin/amqicdir
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqicdir
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/crtmqdir $RPM_BUILD_ROOT/opt/mqm/bin/crtmqdir
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/crtmqdir
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmzse.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzse.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzse.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmzse.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzse.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzse.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/msg/en_US/amq.cat $RPM_BUILD_ROOT/opt/mqm/msg/en_US/amq.cat
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/msg/en_US/amq.cat
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002501B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002501B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002501B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250388.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250388.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250388.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250411.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250411.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250413.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250413.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250413.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025045A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025045A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002504E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002504FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011101B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011101B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011101B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01110333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01110352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01110381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011104E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011104E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011104E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011104FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011104FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011104FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011501B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011501B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011501B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011504E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011504E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011504E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011504FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011504FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011504FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011601B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011601B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011601B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011604E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011604E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011604E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011604FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011604FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011604FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011634B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011634B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011801B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011801B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011801B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01180333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01180352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01180381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011804E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011804E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011804E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011804FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011804FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011804FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011834B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011834B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C0381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D0381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01220381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01220411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220411.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220411.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012901B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012901B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012901B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01290333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01290352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01290381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012904E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012904E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012904E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012904FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012904FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012904FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012934B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012934B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C012D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C012D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C03AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C03AD.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C03AD.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D012C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D012C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D03AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D03AD.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D03AD.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A40360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A40416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40416.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40416.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A40441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40441.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40441.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A404E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A404E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A404E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A80358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A8035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A8035E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A8035E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A80394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80394.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80394.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A804E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A804E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A804E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A834B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A834B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B501F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B501F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B501F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B504E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B504FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F401B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F401B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F401B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F404E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F404E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F404E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F404FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F404FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F404FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D0365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D036B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D036B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D04E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D04E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D04E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D0500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0500.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0500.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033301B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033301B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033301B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033301F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033301F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033301F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0341037B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0341037B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0341037B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03410410.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410410.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410410.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03410440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410440.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410440.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0342039E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0342039E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0342039E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034203B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034203B7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034203B7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0343039F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0343039F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0343039F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034303B3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034303B3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034303B3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03440387.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03440387.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03440387.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03440412.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03440412.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03440412.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0344045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0344045A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0344045A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0344045B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0344045B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0344045B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034503A0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034503A0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034503A0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03450564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03450564.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03450564.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03450569.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03450569.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03450569.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0346036A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0346036A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0346036A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034634B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034634B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035201B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035201B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035201B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035201F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035201F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035201F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035204E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035204FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540366.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540366.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540390.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540390.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035404E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035404E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035404E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540502.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540502.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570370.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570370.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035704E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035704E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035704E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035801A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035801A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035801A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0358035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0358035E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0358035E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03580394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03580394.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03580394.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035804E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035804E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035804E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035834B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035834B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03590398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590398.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590398.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03590402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590402.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590402.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035904E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035904E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035904E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03590501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590501.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590501.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035934B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035934B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E01A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E01A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E01A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E0358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E0394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0394.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0394.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E04E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E04E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E04E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036001A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036001A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036001A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03600416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600416.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600416.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03600441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600441.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600441.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036004E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036004E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036004E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036034B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036034B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036101B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036101B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036101B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036101F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036101F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036101F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036104E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036104E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036104E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620370.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620370.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036204E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036204E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036204E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03640396.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03640396.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03640396.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036403EE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036403EE.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036403EE.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0365032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0365032D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0365032D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0365036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0365036B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0365036B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036504E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036504E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036504E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03650500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03650500.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03650500.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03660354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03660390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660390.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660390.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036604E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036604E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036604E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03660502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660502.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660502.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036634B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036634B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036701B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036701B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036701B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03670333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03670333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03670333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03670352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03670352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03670352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036704E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036704E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036704E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036704FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036704FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036704FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036A0346.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036A0346.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036A0346.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036A34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036A34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B032D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B032D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B0365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B0365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B0365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B04E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B04E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B04E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B0500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B0500.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B0500.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03700357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03700362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03700393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037004E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037004E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037004E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03700503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037034B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037034B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037B0341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B0341.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B0341.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037B0440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B0440.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B0440.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037B34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0381011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0381011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0381011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0381011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0381011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0381011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038101B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038101B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038101B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038101F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038101F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038101F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810411.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810411.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038104E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038104E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038104E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03870344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03870344.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03870344.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03870412.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03870412.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03870412.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0387045B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0387045B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0387045B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03880025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03880025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03880025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0388045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0388045A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0388045A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038834B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038834B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900366.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900366.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039004E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039004E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039004E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900502.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900502.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039034B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039034B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930370.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930370.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0393046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0393046B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0393046B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039304E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039304E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039401A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039401A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039401A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03940358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0394035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0394035E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0394035E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039404E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039404E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039404E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03960364.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03960364.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03960364.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039603EE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039603EE.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039603EE.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039634B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039634B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03980359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980359.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980359.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03980402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980402.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980402.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039804E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039804E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039804E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03980501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980501.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980501.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039834B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039834B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03990458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03990458.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03990458.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039904E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039904E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039904E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039934B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039934B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A0462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A0462.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A0462.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A04E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A04E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A04E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039E0342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039E0342.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039E0342.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039E03B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039E03B7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039E03B7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039F0343.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F0343.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F0343.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039F03B3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F03B3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F03B3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039F34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A00345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A00345.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A00345.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A00564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A00564.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A00564.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A034B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A034B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A213BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A213BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A213BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A413BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A413BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A413BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A503CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A503CA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A503CA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A70567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A70567.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A70567.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A903C4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A903C4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A903C4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A934B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A934B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AA34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AA34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AA34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AB13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AB13BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AB13BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AB34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AB34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AB34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD012C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD012C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD012D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD012D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AE13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE13BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE13BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AE34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AF13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF13BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF13BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AF34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B30343.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B30343.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B30343.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B3039F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B3039F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B3039F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B403C4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B403C4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B403C4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B503CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B503CA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B503CA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B603C4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B603C4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B603C4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B634B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B634B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B70342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B70342.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B70342.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B7039E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B7039E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B7039E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03C403A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403A9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403A9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03C403B4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403B4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403B4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03C403B6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403B6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403B6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03C434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA03A5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA03A5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA03A5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA03B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA03B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA03B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03EE0364.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE0364.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE0364.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03EE0396.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE0396.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE0396.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03EE34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04010357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04010362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04010393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0401046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0401046B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0401046B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040104E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040104E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040104E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04010503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04020359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020359.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020359.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04020398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020398.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020398.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040204E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040204E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040204E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04020501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020501.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020501.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04030381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04030411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030411.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030411.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04100341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04100341.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04100341.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04100440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04100440.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04100440.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041034B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041034B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04110025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04110122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04110381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04110403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04120344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04120344.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04120344.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04120387.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04120387.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04120387.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04130025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04130025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04130025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0413045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0413045A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0413045A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041601A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041601A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041601A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04160360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04160360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04160360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04160441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04160441.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04160441.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041604E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041604E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041604E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041634B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041634B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041701B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041701B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041701B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04400341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400341.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400341.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0440037B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0440037B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0440037B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04400410.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400410.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400410.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044034B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044034B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044101A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044101A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044101A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04410360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04410416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410416.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410416.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044104E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044104E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044104E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0449044A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0449044A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0449044A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044934B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044934B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044A0449.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044A0449.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044A0449.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044A34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044A34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04580399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04580399.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04580399.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045804E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045804E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045804E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045834B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045834B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A0344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0344.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0344.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A0388.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0388.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0388.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A0413.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0413.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0413.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A045B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A045B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A045B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045B0344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B0344.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B0344.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045B0387.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B0387.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B0387.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045B045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B045A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B045A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045B34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0462039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0462039A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0462039A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046204E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046204E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046204E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04630464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04630464.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04630464.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046304E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046304E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04640463.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04640463.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04640463.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04640465.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04640465.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04640465.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046404E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046404E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046404E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04650464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04650464.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04650464.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B0393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B0393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B0393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B0401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B0401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B0401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B04E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B04E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B04E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20366.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20366.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20390.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20390.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20502.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20502.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30370.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30370.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30463.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30463.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30463.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30464.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30464.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E3046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E3046B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E3046B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E401B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E401B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E401B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E401F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E401F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E401F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E404FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E404FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E404FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E5032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E5032D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E5032D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E50365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E5036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E5036B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E5036B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E50500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50500.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50500.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60359.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60359.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60398.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60398.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60402.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60402.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60501.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60501.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E634B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E634B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E701A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E701A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E701A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E70358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E7035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E7035E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E7035E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E70394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70394.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70394.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E801A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E801A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E801A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E80360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E80416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80416.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80416.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E80441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80441.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80441.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E834B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E834B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90399.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90399.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E9039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E9039A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E9039A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90458.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90458.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90462.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90462.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E934B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E934B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0500032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0500032D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0500032D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05000365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05000365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05000365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0500036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0500036B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0500036B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050004E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050004E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050004E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050034B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050034B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05010359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010359.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010359.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05010398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010398.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010398.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05010402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010402.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010402.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050104E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050104E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050104E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05020354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05020366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020366.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020366.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05020390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020390.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020390.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050204E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050204E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050204E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050234B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050234B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030370.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030370.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050304E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050304E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050334B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050334B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05640345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05640345.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05640345.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056403A0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056403A0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056403A0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05640569.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05640569.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05640569.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05641345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05641345.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05641345.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05650567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05650567.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05650567.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056534B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056534B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056703A7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056703A7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056703A7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05670565.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05670565.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05670565.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0567056A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0567056A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0567056A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0567056C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0567056C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0567056C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05690345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05690345.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05690345.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05690564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05690564.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05690564.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05691345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05691345.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05691345.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056A0567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A0567.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A0567.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056C0567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C0567.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C0567.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13450564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13450564.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13450564.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13450569.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13450569.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13450569.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03A2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03A2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03A2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03AB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03AE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AE.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AE.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03AF.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AF.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AF.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0012C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0012C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0012D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0012D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B001A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B001A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B001B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B001F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0032D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0032D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00341.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00341.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00343.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00343.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00343.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00344.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00344.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00345.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00345.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00346.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00346.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00346.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00359.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00359.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00364.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00364.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00364.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00366.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00366.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0036A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00370.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00370.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0037B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0037B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0037B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00387.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00387.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00387.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00388.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00388.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00388.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00390.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00390.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00394.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00394.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00396.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00396.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00396.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00398.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00398.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00399.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00399.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0039A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0039A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0039F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0039F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0039F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AD.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AD.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AF.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003C4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003C4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003C4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003CA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003CA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003EE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003EE.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003EE.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00402.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00402.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00410.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00410.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00410.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00411.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00411.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00412.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00412.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00412.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00413.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00413.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00413.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00416.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00416.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00440.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00440.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00441.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00441.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00449.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00449.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00449.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0044A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0044A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0044A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00458.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00458.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0045A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0045A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0045B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0045B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0045B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00462.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00462.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00463.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00463.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00463.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00464.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00464.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00500.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00500.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00501.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00501.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00502.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00502.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00564.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00564.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00565.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00565.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00565.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00567.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00567.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0056A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0056A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0056A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0056C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0056C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0056C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B013BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B013BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B013BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/readme.ccs $RPM_BUILD_ROOT/opt/mqm/lib/iconv/readme.ccs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/readme.ccs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035214E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035214E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035214E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E404E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E404E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E404E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011514E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011514E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011514E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D14E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D14E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D14E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B514E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B514E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B514E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E7035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E7035E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E7035E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011614E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011614E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011614E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E401B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E401B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E401B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01180478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046414E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046414E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046414E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036014E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036014E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036014E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A814E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A814E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A814E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033314E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033314E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033314E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039814E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039814E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039814E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011314E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011314E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011314E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20505.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20505.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20505.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045814E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045814E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045814E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046214E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046214E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046214E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40113.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40113.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40113.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036614E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036614E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036614E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E50365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E50365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E50365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14EA0469.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA0469.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA0469.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046914EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046914EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046914EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E14E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E14E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E14E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035714E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035714E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035714E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30463.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30463.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30463.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046314E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046314E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046314E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0361035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036514E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036514E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036514E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E3046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E3046B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E3046B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B14E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B14E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B14E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050014E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050014E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050014E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036214E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036214E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036214E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0361047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035814E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035814E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035814E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035914E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035914E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035914E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047904FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047904FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047904FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B14E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B14E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B14E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0361039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E80360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E204E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E204E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E204E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039914E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039914E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039914E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30370.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30370.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA14EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA14EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA14EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E714E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E714E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E714E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E814E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E814E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E814E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040114E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040114E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040114E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14EA046A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA046A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA046A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050414E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050414E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050414E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050314E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050314E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050314E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011114E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011114E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011114E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30464.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30464.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041614E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041614E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041614E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E80416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80416.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80416.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90462.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90462.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E60398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60398.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60398.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E514E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E514E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E514E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E801A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E801A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E801A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039014E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039014E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039014E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474035C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474035C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047404E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047404E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047404E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046A14EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A14EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A14EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047404FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047404FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047404FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E214E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E214E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E214E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047801F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047801F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047801F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E60501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60501.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60501.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047414E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047414E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047414E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30465.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30465.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30465.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047504FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047504FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047504FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90458.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90458.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036114E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036114E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036114E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047514E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047514E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047514E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E701A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E701A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E701A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047604E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047604E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047604E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036714E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036714E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036714E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047604FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047604FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047604FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050514E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050514E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050514E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047601F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047601F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047601F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039314E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039314E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039314E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047614E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047614E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047614E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047704E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047704E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047704E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046514E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046514E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046514E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047704FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047704FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047704FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047901F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047901F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047901F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047714E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047714E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047714E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047804E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047804E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047804E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047814E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047814E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047814E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047501F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047501F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047501F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047901B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047901B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047901B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047914E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047914E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047914E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14EA04EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA04EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA04EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E50500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E50500.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E50500.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E414E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E414E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E414E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4011C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4011C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E504E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E504E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E504E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E404FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E404FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E404FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A14E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A14E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A14E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047601B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047601B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047601B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20504.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20504.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20504.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E70394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70394.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70394.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E5036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5036B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5036B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E60359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60359.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60359.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20502.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20502.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E70358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E704E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E704E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E704E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E804E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E804E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E804E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E304E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E304E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047401F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047401F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047401F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047804FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047804FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047804FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039414E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039414E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039414E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047701F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047701F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047701F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0115.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0115.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012914E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012914E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012914E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01110475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D04E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D04E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047401B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047401B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047401B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E9039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E9039A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E9039A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011814E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011814E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011814E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4011D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4011D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E60402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60402.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60402.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D14E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D14E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90399.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90399.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050114E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050114E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050114E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040214E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040214E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040214E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047904E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047904E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047904E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770116.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770116.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A04FB.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A04FB.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035414E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035414E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035414E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E80441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80441.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80441.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E314E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E314E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E314E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0361039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B01B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B01B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044114E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044114E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044114E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20366.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20366.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047504E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047504E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047504E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047701B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047701B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047701B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047501B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047501B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047501B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20390.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20390.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0111.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0111.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0118.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0118.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0129.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0129.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037014E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037014E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037014E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002514E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002514E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002514E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E604E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E604E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E604E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E904E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E904E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E904E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050214E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050214E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050214E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E614E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E614E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E614E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A414E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A414E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A414E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E914E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E914E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E914E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780417.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780417.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E5032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5032D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5032D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0361.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0361.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047801B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047801B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047801B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0367.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0367.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E644B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E644B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E644B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E344B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E344B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E344B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E244B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E244B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E244B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E944B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E944B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047444B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047444B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E844B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E844B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E844B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047544B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047544B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E744B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E744B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E744B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047644B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047644B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047644B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047744B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047744B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047744B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047844B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047844B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047844B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047944B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047944B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E444B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E444B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00474.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00474.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00475.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00475.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00476.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00476.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00477.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00477.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00478.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00478.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00479.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00479.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14EA44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0039C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0039C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E544B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E544B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B01323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B01323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B01323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13AF34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13AF34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13AF34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/054703AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/054703AD.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/054703AD.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD0547.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD0547.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD0547.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B031A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B031A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B031A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00363.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00363.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B02358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00553.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C0547.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C0547.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C0547.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0547012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547012C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547012C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00554.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00554.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00554.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/23580363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23580363.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23580363.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E731A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E731A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E731A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235814E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235814E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235814E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/23581323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23581323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23581323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A814E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A814E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A814E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A81323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A81323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A81323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235831A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235831A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235831A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235844B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235844B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235844B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A80363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A80363.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A80363.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E72358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E72358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E72358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E71323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E71323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E71323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E70363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70363.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70363.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A82358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A82358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A82358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055303CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055303CA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055303CA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A844B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A844B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A844B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055344B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00469.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00469.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00469.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0046D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0046C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0046A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055444B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055444B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13230363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13230363.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13230363.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B013AF.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B013AF.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B013AF.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13420342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13420342.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13420342.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/134203B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/134203B7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/134203B7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13420552.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13420552.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13420552.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132331A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132331A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132331A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132344B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132344B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132344B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132314E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132314E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132314E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13232358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13232358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13232358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E3036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E3036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E3036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D0547.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D0547.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D0547.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA13AF.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA13AF.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA13AF.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0547012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547012D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547012D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13AF13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13AF13BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13AF13BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A80323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01220403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B70552.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B70552.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B70552.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B71342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B71342.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B71342.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA0553.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA0553.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA0553.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032301A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032301A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032301A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0323035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0323035E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0323035E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03230358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03230358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03230358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03230394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03230394.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03230394.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03410466.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410466.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410466.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03420552.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03420552.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03420552.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03421342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03421342.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03421342.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A041B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A041B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E0323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0357036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0357036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0357036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03580323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03580323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03580323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0370.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0370.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E04E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E04E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E04E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0401.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0401.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E046B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E046B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E14E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E14E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E14E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0362036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0362036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0362036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03631323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03631323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03631323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036314E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036314E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036314E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03632358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03632358.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03632358.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036331A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036331A8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036331A8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036344B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036344B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036344B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0370036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0370036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0370036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0393036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0393036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0393036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03940323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA046A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA046A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA046A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA0469.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA0469.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA0469.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E3036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E3036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E3036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0401036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0401036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0401036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04030122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B01F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B01F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B035A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B035A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04400466.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400466.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400466.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046A04EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A04EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A04EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046A0469.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A0469.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A0469.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046C046D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046C046D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046C046D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046C34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046C34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046D046C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046D046C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046D046C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046D34B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046D34B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04660341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04660341.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04660341.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04660440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04660440.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04660440.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046904EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046904EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046904EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0469046A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0469046A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0469046A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046934B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046934B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0503036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0503036E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0503036E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055203B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055203B7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055203B7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05520342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05520342.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05520342.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05521342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05521342.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05521342.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B002E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B002E1.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B002E1.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050002E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050002E1.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050002E1.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E10500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E10500.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E10500.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E104E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E104E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E104E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B02E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B02E1.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B02E1.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E502E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E502E1.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E502E1.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E1032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E1032D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E1032D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E1036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E1036B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E1036B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E10365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E10365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E10365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036502E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036502E1.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036502E1.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D02E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D02E1.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D02E1.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F414E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F414E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F414E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E401F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E401F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E401F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032304E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032304E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032304E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352039B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352039B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E70323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70323.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70323.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA0554.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA0554.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA0554.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055403CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055403CA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055403CA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/057744B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057744B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057744B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00577.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00577.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00577.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0056E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0056E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0056E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056E44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21221403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21221403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21221403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14032122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14032122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14032122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA0577.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA0577.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA0577.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/057713BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057713BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057713BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA056E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA056E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA056E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056E13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E13BA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E13BA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0547412C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547412C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547412C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/412C0547.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C0547.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C0547.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C412C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C412C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C412C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/412C012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C012D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C012D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D412C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D412C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D412C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14030122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01221403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01221403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01221403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04111403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04111403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04111403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14030411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030411.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030411.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14030381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03811403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03811403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03811403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21220122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01222122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01222122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01222122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03812122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03812122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03812122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21220381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220381.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220381.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21220411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220411.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220411.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04112122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04112122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04112122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14030403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04031403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04031403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04031403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21220403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220403.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220403.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04032122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04032122.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04032122.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/412C012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C012C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C012C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132D136B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D136B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D136B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132D14E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D14E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D14E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132D2365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D2365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D2365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/136B132D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B132D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B132D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/136B14E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B14E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B14E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/136B2365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B2365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B2365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E5132D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5132D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5132D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E5136B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5136B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5136B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E52365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E52365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E52365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/2365132D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/2365132D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/2365132D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/2365136B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/2365136B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/2365136B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/236514E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236514E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236514E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/136B44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0136B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0136B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0136B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/236544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236544B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236544B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B02365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132D44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0132D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0132D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0132D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A402D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A402D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A402D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A902D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A902D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A902D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A90360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A904E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A904E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A904E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A90416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90416.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90416.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A90441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90441.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90441.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A944B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A944B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D001A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D001A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D001A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D001A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D001A9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D001A9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D00360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D00360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D00360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D004E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D004E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D004E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D00416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D00416.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D00416.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D034B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D034B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/030704E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/030704E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/030704E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03070458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03070458.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03070458.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03070462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03070462.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03070462.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/030734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/030734B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/030734B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036001A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036001A9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036001A9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036002D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036002D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036002D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E801A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E801A9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E801A9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E802D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E802D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E802D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90307.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90307.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90307.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041601A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041601A9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041601A9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041602D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041602D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041602D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044101A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044101A9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044101A9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04580307.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04580307.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04580307.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04620307.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04620307.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04620307.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B002D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B002D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B002D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00307.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00307.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00307.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B001A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B001A9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B001A9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03260471.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03260471.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03260471.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04710326.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04710326.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04710326.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047134B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047134B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00471.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00471.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00471.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032634B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032634B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00326.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00326.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00326.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD412C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD412C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD412C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/412C03AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C03AD.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C03AD.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056C1570.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C1570.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C1570.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/1570056C_1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_1.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_1.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/1570056C_2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/1570056C_4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B01570.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B01570.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B01570.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/157034B0_1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_1.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_1.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/157034B0_2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/157034B0_4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A434B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A434B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AE34B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AE34B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AF34B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AF34B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B534B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B534B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055344B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055344B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A4.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A4.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AE.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AE.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AF.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AF.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B5.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B5.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00553.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.glyph
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.glyph
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00553.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.syn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.syn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/234353B3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/234353B3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/234353B3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0487145A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0487145A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0487145A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/145A0487.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/145A0487.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/145A0487.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/53B32343.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/53B32343.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/53B32343.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0055A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0055A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0055A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055A44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055A44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055A44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0055B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0055B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0055B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055B44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055B44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055B44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21A434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21A434B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21A434B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B021A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B021A4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B021A4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30465.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30465.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30465.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046504E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046504E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046504E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039144B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039144B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039144B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00391.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00391.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00391.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333032D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333032D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330357.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330357.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330359.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330359.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330360.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330360.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330362.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330362.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330365.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330365.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330390.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330390.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330393.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330393.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330394.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330394.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330398.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330398.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330399.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330399.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330441.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330441.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E3.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E3.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E6.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E6.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E7.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E7.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304EA.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304EA.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330500.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330500.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330501.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330501.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330503.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330503.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03590333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03600333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03650333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03650333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03650333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03940333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03980333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03990333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03990333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03990333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04410333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E50333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E70333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA0333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA0333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05000333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05000333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05000333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05010333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330481.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330481.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330484.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330484.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330484.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330485.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330485.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330485.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540481.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540481.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03662354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03662354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03662354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03850484.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03850484.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03850484.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038514E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038514E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038514E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038544B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038544B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03860485.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03860485.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03860485.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038614E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038614E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038614E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038644B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038644B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038644B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900481.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900481.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04810333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04810354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04810390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810390.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810390.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04810502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810502.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810502.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048114E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048114E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048114E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04812354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04812354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04812354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048144B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048144B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048144B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04840333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04840333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04840333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04840385.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04840385.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04840385.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048414E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048414E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048414E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048444B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048444B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04850333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04850333.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04850333.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04850386.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04850386.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04850386.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048514E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048514E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048514E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048544B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048544B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05020481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020481.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020481.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20481.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20481.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E22354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E22354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E22354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90385.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90385.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90385.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90386.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90386.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90386.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90484.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90484.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90484.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90485.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90485.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90485.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/23540366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23540366.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23540366.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/23540481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23540481.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23540481.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235414E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235414E2.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235414E2.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235444B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235444B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24E944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E944B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E944B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00385.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00385.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00385.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00386.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00386.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00386.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00481.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00481.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00484.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00484.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00484.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00485.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00485.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00485.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B02354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02354.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02354.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B024E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B024E9.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B024E9.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0497B4B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0497B4B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0497B4B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04B024E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B024E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B024E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04D00561.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D00561.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D00561.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055EF204.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055EF204.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055EF204.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055FF204.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055FF204.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055FF204.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056104D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056104D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056104D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056E54B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E54B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E54B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/11A554B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/11A554B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/11A554B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/1471A4B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1471A4B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1471A4B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14D0612C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14D0612C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14D0612C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/155EF204.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/155EF204.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/155EF204.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/232D54B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/232D54B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/232D54B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/236B54B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236B54B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236B54B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24D02561.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24D02561.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24D02561.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24E404B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E404B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E404B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24E4F204.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E4F204.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E4F204.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24E854B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E854B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E854B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/256124D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/256124D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/256124D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/356154D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/356154D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/356154D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B0056E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0056E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0056E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B011A5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B011A5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B011A5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B0232D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0232D.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0232D.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B0236B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0236B.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0236B.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B024E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B024E8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B024E8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/612C14D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/612C14D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/612C14D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/A4B01471.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/A4B01471.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/A4B01471.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/B4B00497.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/B4B00497.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/B4B00497.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/F20424E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F20424E4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F20424E4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/F204055E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204055E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204055E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/F204055F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204055F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204055F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/F204155E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204155E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204155E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B504B8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504B8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504B8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04B801B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B801B5.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B801B5.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035204B8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204B8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204B8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04B80352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B80352.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B80352.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04B80025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B80025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B80025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002504B8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504B8.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504B8.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54D03561.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D03561.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D03561.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04D0055F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D0055F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D0055F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055F04D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055F04D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055F04D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056944B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056944B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056A44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A44B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A44B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/156274D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/156274D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/156274D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/156374D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/156374D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/156374D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/355E54D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/355E54D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/355E54D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/355F54D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/355F54D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/355F54D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/356054D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/356054D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/356054D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00569.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00569.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00569.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0056A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0056A.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0056A.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54D0355E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D0355E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D0355E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54D0355F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D0355F.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D0355F.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54D03560.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D03560.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D03560.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/556C84D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/556C84D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/556C84D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/734584D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/734584D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/734584D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/74D01562.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/74D01562.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/74D01562.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/74D01563.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/74D01563.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/74D01563.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/84D0556C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/84D0556C.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/84D0556C.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/84D07345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/84D07345.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/84D07345.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/057754B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057754B0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057754B0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B00577.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B00577.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B00577.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002501F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002501F4.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002501F4.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40025.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40025.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04D0356E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D0356E.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D0356E.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04D03577.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D03577.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D03577.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/356E04D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/356E04D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/356E04D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/357704D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/357704D0.tbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/iconv/357704D0.tbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_zh_TW $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_TW
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_TW
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_ru_RU $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ru_RU
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ru_RU
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_es_ES $RPM_BUILD_ROOT/opt/mqm/READMES/readme_es_ES
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_es_ES
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_pt_BR $RPM_BUILD_ROOT/opt/mqm/READMES/readme_pt_BR
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_pt_BR
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_pl_PL $RPM_BUILD_ROOT/opt/mqm/READMES/readme_pl_PL
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_pl_PL
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_zh_TW.BIG5 $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_TW.BIG5
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_TW.BIG5
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_ja_JP.PCK $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ja_JP.PCK
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ja_JP.PCK
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_ko_KR $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ko_KR
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ko_KR
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_zh_CN $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_CN
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_CN
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_en_US $RPM_BUILD_ROOT/opt/mqm/READMES/readme_en_US
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_en_US
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_it_IT $RPM_BUILD_ROOT/opt/mqm/READMES/readme_it_IT
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_it_IT
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_de_DE $RPM_BUILD_ROOT/opt/mqm/READMES/readme_de_DE
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_de_DE
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_hu_HU $RPM_BUILD_ROOT/opt/mqm/READMES/readme_hu_HU
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_hu_HU
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_cs_CZ $RPM_BUILD_ROOT/opt/mqm/READMES/readme_cs_CZ
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_cs_CZ
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_fr_FR $RPM_BUILD_ROOT/opt/mqm/READMES/readme_fr_FR
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_fr_FR
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_ja_JP $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ja_JP
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ja_JP
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqlic $RPM_BUILD_ROOT/opt/mqm/bin/dspmqlic
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqlic
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/mqlicense $RPM_BUILD_ROOT/opt/mqm/bin/mqlicense
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/mqlicense
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/notices.txt $RPM_BUILD_ROOT/opt/mqm/licenses/notices.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/notices.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/status.dat $RPM_BUILD_ROOT/opt/mqm/licenses/status.dat
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/status.dat
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/non_ibm_license.txt $RPM_BUILD_ROOT/opt/mqm/licenses/non_ibm_license.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/non_ibm_license.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Czech.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Czech.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Czech.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/German.txt $RPM_BUILD_ROOT/opt/mqm/licenses/German.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/German.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Greek.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Greek.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Greek.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/English.txt $RPM_BUILD_ROOT/opt/mqm/licenses/English.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/English.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Spanish.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Spanish.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Spanish.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/French.txt $RPM_BUILD_ROOT/opt/mqm/licenses/French.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/French.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Indonesian.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Indonesian.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Indonesian.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Italian.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Italian.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Italian.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Japanese.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Japanese.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Japanese.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Korean.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Korean.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Korean.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Lithuanian.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Lithuanian.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Lithuanian.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Polish.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Polish.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Polish.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Portuguese.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Portuguese.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Portuguese.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Russian.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Russian.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Russian.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Slovenian.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Slovenian.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Slovenian.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Turkish.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Turkish.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Turkish.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Chinese.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Chinese.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Chinese.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/licenses/Chinese_TW.txt $RPM_BUILD_ROOT/opt/mqm/licenses/Chinese_TW.txt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/licenses/Chinese_TW.txt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/LAPApp.jar $RPM_BUILD_ROOT/opt/mqm/lap/LAPApp.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/LAPApp.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/icon.gif $RPM_BUILD_ROOT/opt/mqm/lap/licenses/icon.gif
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/icon.gif
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/logo.gif $RPM_BUILD_ROOT/opt/mqm/lap/licenses/logo.gif
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/logo.gif
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_cs $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_cs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_cs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_de $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_de
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_de
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_el $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_el
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_el
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_en $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_en
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_en
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_es $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_es
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_es
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_fr $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_fr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_fr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_in $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_in
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_in
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_id $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_id
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_id
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_it $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_it
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_it
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_ja $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_ja
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_ja
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_ko $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_ko
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_ko
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_lt $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_lt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_lt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_pl $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_pl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_pl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_pt $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_pt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_pt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_ru $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_ru
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_ru
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_sl $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_sl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_sl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_tr $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_tr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_tr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_zh $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_zh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_zh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LA_zh_TW $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_zh_TW
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LA_zh_TW
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_cs $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_cs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_cs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_de $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_de
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_de
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_el $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_el
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_el
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_en $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_en
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_en
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_es $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_es
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_es
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_fr $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_fr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_fr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_in $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_in
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_in
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_id $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_id
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_id
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_it $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_it
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_it
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_ja $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_ja
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_ja
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_ko $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_ko
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_ko
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_lt $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_lt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_lt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_pl $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_pl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_pl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_pt $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_pt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_pt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_ru $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_ru
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_ru
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_sl $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_sl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_sl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_tr $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_tr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_tr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_zh $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_zh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_zh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/LI_zh_TW $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_zh_TW
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/LI_zh_TW
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/non_ibm_license $RPM_BUILD_ROOT/opt/mqm/lap/licenses/non_ibm_license
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/non_ibm_license
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lap/licenses/notices $RPM_BUILD_ROOT/opt/mqm/lap/licenses/notices
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lap/licenses/notices
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqtcert.lic $RPM_BUILD_ROOT/opt/mqm/samp/amqtcert.lic
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqtcert.lic
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqpcert.lic $RPM_BUILD_ROOT/opt/mqm/samp/amqpcert.lic
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqpcert.lic
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqdcert.lic $RPM_BUILD_ROOT/opt/mqm/samp/amqdcert.lic
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqdcert.lic
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dmpmqcfg $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqcfg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqcfg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dmpmqmsg $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqmsg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqmsg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqver $RPM_BUILD_ROOT/opt/mqm/bin/dspmqver
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqver
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/crtmqenv $RPM_BUILD_ROOT/opt/mqm/bin/crtmqenv
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/crtmqenv
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqenv $RPM_BUILD_ROOT/opt/mqm/bin/setmqenv
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/setmqenv
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/mqrc $RPM_BUILD_ROOT/opt/mqm/bin/mqrc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/mqrc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.commonservices.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.commonservices.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.commonservices.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqiclen $RPM_BUILD_ROOT/opt/mqm/bin/amqiclen
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqiclen
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/crtmqinst $RPM_BUILD_ROOT/opt/mqm/bin/crtmqinst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/crtmqinst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dltmqinst $RPM_BUILD_ROOT/opt/mqm/bin/dltmqinst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dltmqinst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqinst $RPM_BUILD_ROOT/opt/mqm/bin/dspmqinst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqinst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqrte $RPM_BUILD_ROOT/opt/mqm/bin/dspmqrte
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqrte
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqinst $RPM_BUILD_ROOT/opt/mqm/bin/setmqinst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/setmqinst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ-9.4.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ-9.4.0.mqtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ-9.4.0.mqtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Runtime-9.4.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Runtime-9.4.0.mqtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Runtime-9.4.0.mqtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/ibm.com_IBM_MQ_Advanced_for_Developers_Non-Warranted-9.4.0.swidtag $RPM_BUILD_ROOT/opt/mqm/swidtag/ibm.com_IBM_MQ_Advanced_for_Developers_Non-Warranted-9.4.0.swidtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/ibm.com_IBM_MQ_Advanced_for_Developers_Non-Warranted-9.4.0.swidtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.tools.ras.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.tools.ras.jar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.tools.ras.jar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqras $RPM_BUILD_ROOT/opt/mqm/bin/runmqras
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqras
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqjrever $RPM_BUILD_ROOT/opt/mqm/bin/amqjrever
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqjrever
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/isa.xml $RPM_BUILD_ROOT/opt/mqm/bin/isa.xml
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/isa.xml
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqiclib $RPM_BUILD_ROOT/opt/mqm/bin/amqiclib
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqiclib
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqicvar $RPM_BUILD_ROOT/opt/mqm/bin/amqicvar
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqicvar
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqicrel $RPM_BUILD_ROOT/opt/mqm/bin/amqicrel
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqicrel
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqicfil $RPM_BUILD_ROOT/opt/mqm/bin/amqicfil
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqicfil
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/mqconfig $RPM_BUILD_ROOT/opt/mqm/bin/mqconfig
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/mqconfig
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/mqinstconf $RPM_BUILD_ROOT/opt/mqm/bin/mqinstconf
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/mqinstconf
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/instinfo.tsk $RPM_BUILD_ROOT/opt/mqm/instinfo.tsk
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/instinfo.tsk
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/mqpatch.dat $RPM_BUILD_ROOT/opt/mqm/mqpatch.dat
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/mqpatch.dat
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqsc $RPM_BUILD_ROOT/opt/mqm/bin/runmqsc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqsc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libcurl.so $RPM_BUILD_ROOT/opt/mqm/lib/libcurl.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libcurl.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libcurl.so $RPM_BUILD_ROOT/opt/mqm/lib64/libcurl.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libcurl.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/runmqccred $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/runmqccred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/runmqccred
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/mqccred.ini $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/mqccred.ini
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/mqccred.ini
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/lib/mqccred $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib/mqccred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib/mqccred
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/lib/mqccred_r $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib/mqccred_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib/mqccred_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/lib64/mqccred $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib64/mqccred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib64/mqccred
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/lib64/mqccred_r $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib64/mqccred_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib64/mqccred_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libedit.so $RPM_BUILD_ROOT/opt/mqm/lib64/libedit.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libedit.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runp11cred $RPM_BUILD_ROOT/opt/mqm/bin/runp11cred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runp11cred
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqicred $RPM_BUILD_ROOT/opt/mqm/bin/runmqicred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqicred
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqdlq $RPM_BUILD_ROOT/opt/mqm/bin/runmqdlq
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqdlq

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/web"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib/iconv"
%dir %attr(555,mqm,mqm) "/opt/mqm/msg"
%dir %attr(555,mqm,mqm) "/opt/mqm/msg/en_US"
%dir %attr(555,mqm,mqm) "/opt/mqm/READMES"
%dir %attr(555,mqm,mqm) "/opt/mqm/licenses"
%dir %attr(555,mqm,mqm) "/opt/mqm/lap"
%dir %attr(555,mqm,mqm) "/opt/mqm/lap/licenses"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/mqccred"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/mqccred/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/mqccred/lib64"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqm.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqm.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcs.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcs.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqe.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqe.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqecs.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqecs.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqxzu.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqxzu.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqzsd.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqzsd.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqz.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqz.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqm_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqm_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqe_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqe_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqecs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqecs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqxzu_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqxzu_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqzsd_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqzsd_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqz_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqz_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqjx_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqjx_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqjxx_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqjxx_r.so"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/ffstsummary"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqltmc0"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqltmc064"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqb23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqb23gl_r.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqb23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqb23gl_r.so.4.1"
%attr(444,mqm,mqm) "/opt/mqm/samp/ccsid.tbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/ccsid_part2.tbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/ccsid.new"
%attr(444,mqm,mqm) "/opt/mqm/samp/mqs.ini"
%attr(444,mqm,mqm) "/opt/mqm/samp/mqclient.ini"
%attr(444,mqm,mqm) "/opt/mqm/samp/service.env"
%attr(444,mqm,mqm) "/opt/mqm/samp/web/mqwebuser.xml"
%attr(444,mqm,mqm) "/opt/mqm/samp/web/server.xml"
%attr(444,mqm,mqm) "/opt/mqm/samp/web/jvm.options"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/strmqtrc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqtrc"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqras"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqtrc"
%attr(444,mqm,mqm) "/opt/mqm/lib/amqtrc.fmt"
%attr(444,mqm,mqm) "/opt/mqm/lib/ccdt_schema.json"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqxdbg"
%attr(6555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqxmsg0"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqicdir"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/crtmqdir"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmzse.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmzse.so"
%attr(444,mqm,mqm) "/opt/mqm/msg/en_US/amq.cat"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002501B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250388.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250413.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002504E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002504FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011101B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01110333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01110352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01110381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011104E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011104FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011501B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011504E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011504FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011601B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011604E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011604FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011801B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01180333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01180352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01180381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011804E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011804FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C0381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D0381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01220381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01220411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012901B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01290333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01290352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01290381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012904E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012904FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C03AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D03AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A40360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A40416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A40441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A404E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A80358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A8035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A80394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A804E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B501F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B504E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B504FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F401B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F404E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F404FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D0365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D04E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D0500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033301B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033301F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0341037B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03410410.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03410440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0342039E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034203B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0343039F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034303B3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03440387.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03440412.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0344045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0344045B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034503A0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03450564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03450569.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0346036A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035201B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035201F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035204E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035204FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035404E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035704E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035801A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0358035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03580394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035804E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03590398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03590402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035904E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03590501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E01A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E0358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E0394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E04E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036001A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03600416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03600441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036004E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036101B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036101F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036104E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036204E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03640396.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036403EE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0365032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0365036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036504E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03650500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03660354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03660390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036604E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03660502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036701B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03670333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03670352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036704E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036704FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036A0346.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B0365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B04E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B0500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03700357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03700362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03700393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037004E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03700503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037B0341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037B0440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037B34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0381011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0381011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038101B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038101F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038104E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03870344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03870412.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0387045B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03880025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0388045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039004E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0393046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039401A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03940358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0394035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039404E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03960364.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039603EE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03980359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03980402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039804E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03980501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03990458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039904E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A0462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A04E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039E0342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039E03B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039F0343.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039F03B3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039F34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A00345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A00564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A213BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A413BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A503CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A70567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A903C4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AA34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AB13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AB34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AE13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AE34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AF13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AF34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B30343.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B3039F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B403C4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B503CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B603C4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B70342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B7039E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03C403A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03C403B4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03C403B6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03C434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA03A5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA03B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03EE0364.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03EE0396.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03EE34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04010357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04010362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04010393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0401046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040104E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04010503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04020359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04020398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040204E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04020501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04030381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04030411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04100341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04100440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04110025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04110122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04110381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04110403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04120344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04120387.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04130025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0413045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041601A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04160360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04160441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041604E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041701B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04400341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0440037B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04400410.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044101A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04410360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04410416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044104E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0449044A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044A0449.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04580399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045804E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A0344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A0388.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A0413.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A045B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045B0344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045B0387.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045B045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045B34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0462039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046204E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04630464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04640463.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04640465.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046404E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04650464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B0393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B0401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B04E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30463.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E3046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E401B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E401F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E404FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E5032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E50365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E5036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E50500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E701A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E70358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E7035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E70394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E801A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E80360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E80416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E80441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E9039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0500032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05000365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0500036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050004E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05010359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05010398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05010402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050104E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05020354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05020366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05020390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050204E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05640345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056403A0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05640569.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05641345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05650567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056703A7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05670565.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0567056A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0567056C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05690345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05690564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05691345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056A0567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056C0567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13450564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13450569.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03A2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03AB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03AE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03AF.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B001A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B001A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B001B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B001F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00343.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00346.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00364.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0036A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0037B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00387.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00388.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00396.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0039F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AF.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003C4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003EE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00410.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00412.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00413.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00449.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0044A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0045B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00463.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00565.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0056A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0056C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B013BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/readme.ccs"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035214E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E404E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011514E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D14E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B514E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E7035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011614E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E401B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01180478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046414E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036014E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A814E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033314E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039814E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011314E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20505.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045814E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046214E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40113.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036614E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E50365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14EA0469.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046914EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E14E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035714E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30463.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046314E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0361035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036514E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E3046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B14E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050014E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036214E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0361047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035814E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035914E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047904FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B14E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0361039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E80360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E204E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039914E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA14EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E714E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E814E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040114E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14EA046A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050414E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050314E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011114E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041614E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E80416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E60398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E514E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E801A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039014E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047404E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046A14EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047404FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E214E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047801F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E60501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047414E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30465.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047504FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036114E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047514E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E701A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047604E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036714E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047604FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050514E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047601F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039314E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047614E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047704E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046514E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047704FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047901F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047714E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047804E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047814E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047501F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047901B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047914E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14EA04EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E50500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E414E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E504E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E404FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A14E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047601B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20504.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E70394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E5036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E60359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E70358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E704E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E804E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047401F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047804FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039414E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047701F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012914E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01110475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047401B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E9039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011814E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E60402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050114E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040214E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047904E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035414E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E80441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E314E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0361039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044114E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047504E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047701B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047501B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037014E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002514E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E604E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E904E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050214E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E614E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A414E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E914E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E5032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047801B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E644B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E344B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E244B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E844B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E744B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047644B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047744B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047844B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14EA44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B01323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13AF34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/054703AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD0547.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B031A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B02358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00553.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C0547.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0547012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00554.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/23580363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E731A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235814E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/23581323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A814E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A81323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235831A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235844B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A80363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E72358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E71323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E70363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A82358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055303CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A844B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055344B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00469.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0046D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0046C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0046A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13230363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B013AF.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13420342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/134203B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13420552.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132331A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132344B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132314E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13232358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E3036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D0547.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA13AF.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0547012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13AF13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A80323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01220403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B70552.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B71342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA0553.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032301A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0323035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03230358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03230394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03410466.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03420552.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03421342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E0323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0357036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03580323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E04E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E14E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0362036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03631323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036314E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03632358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036331A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036344B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0370036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0393036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03940323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA046A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA0469.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E3036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0401036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04030122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04400466.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046A04EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046A0469.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046C046D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046D046C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04660341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04660440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046904EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0469046A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0503036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055203B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05520342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05521342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B002E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050002E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E10500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E104E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B02E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E502E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E1032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E1036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E10365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036502E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D02E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F414E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E401F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032304E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E70323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA0554.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055403CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/057744B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00577.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0056E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056E44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21221403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14032122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA0577.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/057713BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA056E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056E13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0547412C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/412C0547.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C412C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/412C012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D412C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14030122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01221403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04111403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14030411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14030381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03811403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21220122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01222122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03812122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21220381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21220411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04112122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14030403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04031403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21220403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04032122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/412C012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132D136B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132D14E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132D2365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/136B132D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/136B14E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/136B2365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E5132D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E5136B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E52365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/2365132D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/2365136B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/236514E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/136B44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0136B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/236544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B02365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132D44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0132D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A402D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A902D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A90360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A904E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A90416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A90441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D001A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D001A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D00360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D004E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D00416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/030704E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03070458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03070462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/030734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036001A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036002D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E801A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E802D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90307.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041601A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041602D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044101A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04580307.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04620307.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B002D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00307.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B001A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03260471.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04710326.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00471.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00326.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD412C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/412C03AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056C1570.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/1570056C_1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/1570056C_2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/1570056C_4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B01570.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/157034B0_1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/157034B0_2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/157034B0_4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A434B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A434B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AE34B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AE34B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AF34B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AF34B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B534B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B534B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055344B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055344B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A4.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A4.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AE.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AE.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AF.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AF.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B5.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B5.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00553.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00553.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/234353B3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0487145A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/145A0487.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/53B32343.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0055A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055A44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0055B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055B44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21A434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B021A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30465.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046504E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039144B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00391.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03590333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03600333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03650333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03940333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03980333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03990333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04410333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E50333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E70333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05000333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05010333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330484.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330485.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03662354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03850484.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038514E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03860485.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038614E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038644B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04810333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04810354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04810390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04810502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048114E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04812354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048144B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04840333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04840385.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048414E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04850333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04850386.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048514E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05020481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E22354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90385.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90386.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90484.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90485.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/23540366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/23540481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235414E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24E944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00385.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00386.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00484.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00485.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B02354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B024E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0497B4B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04B024E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04D00561.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055EF204.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055FF204.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056104D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056E54B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/11A554B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/1471A4B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14D0612C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/155EF204.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/232D54B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/236B54B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24D02561.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24E404B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24E4F204.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24E854B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/256124D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/356154D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B0056E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B011A5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B0232D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B0236B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B024E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/612C14D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/A4B01471.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/B4B00497.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/F20424E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/F204055E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/F204055F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/F204155E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B504B8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04B801B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035204B8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04B80352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04B80025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002504B8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54D03561.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04D0055F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055F04D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056A44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/156274D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/156374D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/355E54D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/355F54D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/356054D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00569.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0056A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54D0355E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54D0355F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54D03560.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/556C84D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/734584D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/74D01562.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/74D01563.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/84D0556C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/84D07345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/057754B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B00577.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002501F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04D0356E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04D03577.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/356E04D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/357704D0.tbl"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_zh_TW"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_ru_RU"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_es_ES"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_pt_BR"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_pl_PL"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_zh_TW.BIG5"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_ja_JP.PCK"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_ko_KR"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_zh_CN"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_en_US"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_it_IT"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_de_DE"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_hu_HU"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_cs_CZ"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_fr_FR"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_ja_JP"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqlic"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/mqlicense"
%attr(444,mqm,mqm) "/opt/mqm/licenses/notices.txt"
%attr(444,mqm,mqm) %verify(not md5 mtime size) "/opt/mqm/licenses/status.dat"
%attr(444,mqm,mqm) "/opt/mqm/licenses/non_ibm_license.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Czech.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/German.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Greek.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/English.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Spanish.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/French.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Indonesian.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Italian.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Japanese.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Korean.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Lithuanian.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Polish.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Portuguese.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Russian.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Slovenian.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Turkish.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Chinese.txt"
%attr(444,mqm,mqm) "/opt/mqm/licenses/Chinese_TW.txt"
%attr(444,mqm,mqm) "/opt/mqm/lap/LAPApp.jar"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/icon.gif"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/logo.gif"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_cs"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_de"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_el"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_en"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_es"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_fr"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_in"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_id"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_it"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_ja"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_ko"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_lt"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_pl"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_pt"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_ru"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_sl"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_tr"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_zh"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LA_zh_TW"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_cs"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_de"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_el"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_en"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_es"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_fr"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_in"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_id"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_it"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_ja"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_ko"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_lt"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_pl"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_pt"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_ru"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_sl"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_tr"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_zh"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/LI_zh_TW"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/non_ibm_license"
%attr(444,mqm,mqm) "/opt/mqm/lap/licenses/notices"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqtcert.lic"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqpcert.lic"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqdcert.lic"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dmpmqcfg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dmpmqmsg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqver"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/crtmqenv"
%attr(555,mqm,mqm) "/opt/mqm/bin/setmqenv"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/mqrc"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.commonservices.jar"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqiclen"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/crtmqinst"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dltmqinst"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqinst"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqrte"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqinst"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ-9.4.0.mqtag"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Runtime-9.4.0.mqtag"
%attr(444,mqm,mqm) %config(missingok) "/opt/mqm/swidtag/ibm.com_IBM_MQ_Advanced_for_Developers_Non-Warranted-9.4.0.swidtag"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.tools.ras.jar"
%attr(555,mqm,mqm) "/opt/mqm/bin/runmqras"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqjrever"
%attr(444,bin,mqm) "/opt/mqm/bin/isa.xml"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqiclib"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqicvar"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqicrel"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqicfil"
%attr(555,mqm,mqm) "/opt/mqm/bin/mqconfig"
%attr(555,mqm,mqm) "/opt/mqm/bin/mqinstconf"
%attr(444,mqm,mqm) "/opt/mqm/instinfo.tsk"
%attr(444,mqm,mqm) %verify(not md5 mtime size) "/opt/mqm/mqpatch.dat"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqsc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libcurl.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libcurl.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/runmqccred"
%attr(444,mqm,mqm) "/opt/mqm/samp/mqccred/mqccred.ini"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/lib/mqccred"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/lib/mqccred_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/lib64/mqccred"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/lib64/mqccred_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libedit.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runp11cred"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqicred"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqdlq"

%pre
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/runtime_preinstall.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72,"
#   years="2005,2024"
#   crc="935548272" >
#   Licensed Materials - Property of IBM
#
#   5724-H72,
#
#   (C) Copyright IBM Corp. 2005, 2024 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Preinstallation script for MQSeriesRuntime package
#
# Check for mqm group and user
#
# Set up environment variables
TMPDIR="/tmp"
RC=0
DUMMY=""

create_mqm_group()
{
  echo "Creating group mqm"
  ErrorText=`groupadd mqm 2>&1`
  RC=$?
  if [ $RC -ne 0 ]; then
    echo "ERROR:  Failed to add 'mqm' group:" >&2
    echo $ErrorText >&2
    exit $RC
  fi
}

preserve_license()
{
    INSTALLED_VRM=$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b | awk -F. '{print $1 "." $2 "." $3}')
    PACKAGE_VRM=`echo ${RPM_PACKAGE_VERSION} | awk -F. '{print $1 "." $2 "." $3}'`
    MQ_INSTALL_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -bf 512`

    # create a temp dir to preserve the license
    mkdir -p /tmp/mq_preserved_license /tmp/mq_preserved_license/${MQ_INSTALL_NAME} 2>/dev/null

    if [ "${INSTALLED_VRM}" = "${PACKAGE_VRM}" ] ; then
      # If the VRM is same, Could be a CSU or fixpack
      # Preserve the license status
      cp -f ${MQ_INSTALLATION_PATH}/licenses/status.dat /tmp/mq_preserved_license/${MQ_INSTALL_NAME} 2>/dev/null
    fi
    
    if [ $1 != "Production" ] ; then
      # Preserve a license type
      echo $1 > /tmp/mq_preserved_license/${MQ_INSTALL_NAME}/LicenseType.txt
    fi
}

# Determine if the group exists on the system.  The solution used here is to
# create a file in the temporary location, attempt to change its group id to
# mqm.  This method should work independent of the multitude of ways groups can
# be defined across distributions and network environments
TMPFILE="${TMPDIR}/amq_grouptest"
touch $TMPFILE 2>/dev/null
if [ -f "$TMPFILE" ]; then
  chown :mqm $TMPFILE 2>/dev/null
  if [ $? -ne 0 ]; then
    create_mqm_group
  fi
  rm -f $TMPFILE
else  # Unable to create temporary file.  This is also needed by other install
      # processes - so it is fair to abort the install at this point
  echo "ERROR: Unable to write to ${TMPDIR} - aborting install"
  exit 1
fi

# Determine if the user id "mqm" exists, and is in the group mqm
ErrorText=`id -u mqm 2>&1`
RC=$?
if [ $RC -ne 0 ]; then
  echo "Creating user mqm"
  ErrorText=`useradd -r -d /var/mqm -g mqm mqm 2>&1`
  RC=$?
  if [ $RC -ne 0 ]; then
    echo "ERROR:  Failed to add 'mqm' user:" >&2
    echo $ErrorText >&2
    exit $RC
  fi
else    # Check the user mqm is in the group mqm
  ErrorText=`id -Gn mqm | grep -w mqm 2>&1`
  if [ $? -ne 0 ]; then
    ErrorText=`usermod -G mqm mqm 2>&1`
    if [ $RC -ne 0 ]; then
      echo "ERROR:  Failed to add user mqm to group mqm:" >&2
      echo $ErrorText >&1
      echo $RC
    fi
  fi
fi

# Remove any Advanced swidtag - it will get regenerated later if required

rm -f ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced-*.swidtag

# If the license is accepted for a current installer
# Then Preserve the license into a temp dir
if [ ${MQ_UPGRADE} = "Yes" ] ; then 
  LICENSE_TYPE=`${MQ_INSTALLATION_PATH}/bin/dspmqver -bf 8192`
  if [ "${LICENSE_TYPE}" != "License not accepted" ] ; then
    preserve_license $LICENSE_TYPE
  else
    BUILD_TYPE=`${MQ_INSTALLATION_PATH}/bin/amqicvar -f ${MQ_INSTALLATION_PATH}/lib64/libmqmcs_r.so -b -n -z -q -i MQ_LICENSE_TYPE`
    case ${BUILD_TYPE} in
      "PRODUCTION")
        if [ -r ${MQ_INSTALLATION_PATH}/lib/amqdcert.lic ]; then
          preserve_license "Developer"
        else
          if [ -r ${MQ_INSTALLATION_PATH}/lib/amqtcert.lic ]; then
            preserve_license "Trial"
          fi
        fi
        ;;
      "DEVELOPER")
        preserve_license "Developer"
      ;;
      "TRIAL")
        preserve_license "Trial"
      ;;
    esac    
  fi
fi
echo > /dev/null 2>/dev/null

%post
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqm.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqm.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqm.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqm.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqm_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqm_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqm_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqm_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/runtime_postinstall.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2005,2023"
#   crc="1956258177" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2005, 2023 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Postinstallation script for MQ

#
# Create the top-level data files / directories required for MQ
#
LANG=C
LC_ALL=C
export LANG
export LC_ALL

amqicdir_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/amqicdir -i -f 2>&1`
rc=$?
if [ $rc -gt 10 ] ; then
  echo "ERROR: Return code \"$rc\" from amqicdir for \"-i -f\", output is:" >&2
  echo "       ${amqicdir_out}" >&2
fi
# Some Debian based systems do not have a /usr/lib64 but
# setminst -i will fail without it
if [ ! -d /usr/lib64 ]  ; then
  mkdir /usr/lib64
  chown 755 /usr/lib64
fi

#
# Record the installation in the mqinst.ini file
#
crtmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/crtmqinst -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
 case $rc in
  10)
    echo "WARNING: Return code \"$rc\" from crtmqinst for \"-p ${MQ_INSTALLATION_PATH} \", output is:" >&2
    echo "         ${crtmqinst_out}" >&2
  ;;
  *)
    echo "ERROR:   Return code \"$rc\" from crtmqinst for \"-p ${MQ_INSTALLATION_PATH} \", output is:" >&2
    echo "         ${crtmqinst_out}" >&2
  ;;
 esac
fi

#
# Create the installation specific files / directories.
# This must happen AFTER recording the installation in mqinst.ini
#
amqicdir_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/amqicdir -s -f 2>&1`
rc=$?
if [ $rc -gt 10 ] ; then
  echo "ERROR: Return code \"$rc\" from amqicdir for \"-s -f\", output is:" >&2
  echo "       ${amqicdir_out}" >&2
fi

# May want to get kernel parameters updated here. For now, don't do it.
kernel_mods=0
if [ $kernel_mods -eq 1 ]
then
echo "  Updating kernel parameters..."
  # Shared memory
  # Semaphores
  # If this worked, indicate that the kernel needs to be rebuilt and
  # the system rebooted.
fi

# Create the ssl directory for migrated queue managers
DefaultPrefix=`grep DefaultPrefix /var/mqm/mqs.ini | cut -f2 -d'='`
find $DefaultPrefix/qmgrs/* -type d -prune > /dev/null 2>&1
if [ $? = 0 ]; then
  for i  in $DefaultPrefix/qmgrs/* ; do
    qm_name=`basename $i`

    if [ "$qm_name" != "@SYSTEM" ]; then

      # Only operate on directory entries
      if [ -d "$DefaultPrefix/$qm_name" ]; then
        if [ ! -d  $DefaultPrefix/qmgrs/$qm_name/ssl ]; then
          mkdir $DefaultPrefix/qmgrs/$qm_name/ssl
          chown mqm:mqm  $DefaultPrefix/qmgrs/$qm_name/ssl
          chmod 2775  $DefaultPrefix/qmgrs/$qm_name/ssl
        fi
      fi

    fi
  done
fi

#  Check to see if this package is correctly signed on rpm based systems.
if [ -x /usr/bin/rpm ] ; then
  rpm_verify_out=`rpm -Vvv --nodeps ${RPM_PACKAGE_NAME}  2>&1 |  grep NOKEY | tail -n1 | grep  NOKEY`
  if [ $? -eq 0 ] ; then 
    echo "Warning : package \"${RPM_PACKAGE_NAME}\" is signed but key is not installed on this system." >&2
    echo "          rpm verify shows \"${rpm_verify_out}\"" >&2
    echo "          rpm warning message may have been issued at install time." >&2
    echo "          See topic \"IBM MQ code signatures\" in the IBM MQ documentation for more information." >&2
  fi
fi

# Invoke setmqinst to refresh symlinks if this installation is the primary
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi
echo > /dev/null

# Hide away the exits because an old rpm -U is about to delete them. post trans will deal with them later
MQ_INSTALL_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -f512 -b`
if [ -f /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred ] ; then
  cp -f  /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred /tmp/mqccred.backup
fi 
if [ -f /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred_r ]; then  
  cp -f /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred_r /tmp/mqccred_r.backup
fi 
if [ -f /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred ] ; then
  cp -f /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred /tmp/mqccred.backup64
fi 
if [ -f /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred_r ] ; then
  cp -f /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred_r /tmp/mqccred_r.backup64
fi 
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/copy_license.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72,"
#   years="2005,2024"
#   crc="512007515" >
#   Licensed Materials - Property of IBM
#
#   5724-H72,
#
#   (C) Copyright IBM Corp. 2005, 2024 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>

# If the license agreement was accepted, status.dat should have been
# installed into /tmp/mq_license_${RPM_PACKAGE_VERSION}.
# This needs to be copied to ${MQ_INSTALLATION_PATH}/licenses.

MQ_INSTALL_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -bf 512`
if [ -r /tmp/mq_license_${RPM_PACKAGE_VERSION}/license/status.dat ]
then
  cp /tmp/mq_license_${RPM_PACKAGE_VERSION}/license/* ${MQ_INSTALLATION_PATH}/licenses 2>/dev/null
  chown mqm ${MQ_INSTALLATION_PATH}/licenses/status.dat 2>/dev/null
  chgrp mqm ${MQ_INSTALLATION_PATH}/licenses/status.dat 2>/dev/null
  chmod 444 ${MQ_INSTALLATION_PATH}/licenses/status.dat 2>/dev/null
  rm -Rf /tmp/mq_license_${RPM_PACKAGE_VERSION}
else
  # If license is already accepted with previous installation
  if [ -r /tmp/mq_preserved_license/${MQ_INSTALL_NAME}/status.dat ]
  then
    cp /tmp/mq_preserved_license/${MQ_INSTALL_NAME}/status.dat ${MQ_INSTALLATION_PATH}/licenses 2>/dev/null
    chown mqm ${MQ_INSTALLATION_PATH}/licenses/status.dat 2>/dev/null
    chgrp mqm ${MQ_INSTALLATION_PATH}/licenses/status.dat 2>/dev/null
    chmod 444 ${MQ_INSTALLATION_PATH}/licenses/status.dat 2>/dev/null
  else
    # If MQLICENSE=accept is specified, call the mqlicense command to
    # accept the license now while we're root.
    if [ "${MQLICENSE}" = "accept" ]
    then
      ${MQ_INSTALLATION_PATH}/bin/mqlicense -accept
    fi
  fi
fi

###########################################################################
# Check if any preserved license type exists
# If any preserved license exists and the current installation edition is different
# Then copy the lic files into /lib
###########################################################################
LICENSE_TYPE=`${MQ_INSTALLATION_PATH}/bin/dspmqver -bf 8192`
if [ -r /tmp/mq_preserved_license/${MQ_INSTALL_NAME}/LicenseType.txt ] ; then
  PRESERVED_LICENSE=`cat /tmp/mq_preserved_license/${MQ_INSTALL_NAME}/LicenseType.txt`
  if [ "${PRESERVED_LICENSE}" != "${LICENSE_TYPE}" ] ; then
    # If the preserved license type is Developer copies the developer licenses
    if [ ${PRESERVED_LICENSE} = "Developer" ] ; then
      cp -f ${MQ_INSTALLATION_PATH}/samp/amqpcert.lic ${MQ_INSTALLATION_PATH}/lib 2>/dev/null
      cp -f ${MQ_INSTALLATION_PATH}/samp/amqdcert.lic ${MQ_INSTALLATION_PATH}/lib 2>/dev/null
    else
      # If the preserved license type is Trial copies the trial licenses
      if [ ${PRESERVED_LICENSE} = "Trial" ] ; then
        cp -f ${MQ_INSTALLATION_PATH}/samp/amqtcert.lic ${MQ_INSTALLATION_PATH}/lib 2>/dev/null
      fi
    fi
  fi
fi

command=`basename $(ls -l /proc/${PPID}/exe | awk '{print $NF}')`
if [ ${command} = 'dpkg' ] ; then # For rpm removing of a temp dir handled in runtime_posttrans script
  rm -rf /tmp/mq_preserved_license/${MQ_INSTALL_NAME}
fi

echo "Resetting return code to success" > /dev/null

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/check_acceptance.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72,"
#   years="2005,2019"
#   crc="1114153681" >
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
# Preinstallation script
# Checks to see if the license agreement has been accepted and
# display a message if it hasn't telling the customer to view the license.

MQ_INSTALL_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -f512 -b`

if [ ! -s "${MQ_INSTALLATION_PATH}/licenses/status.dat" ] ; then
    ${MQ_INSTALLATION_PATH}/bin/mqrc -b -c "${MQ_INSTALL_NAME}" -c "${MQ_INSTALLATION_PATH}" AMQ7172
fi

echo "Resetting return code to success" > /dev/null


%preun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/runtime_preuninstall.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2005,2024"
#   crc="598641773" >
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
# Pre uninstallation script
FILE='@(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/runtime_preuninstall.sh'
if [ ${MQ_UPGRADE} = 'No' ] ; then 
  MQ_INSTALL_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -f512 -b`

  #####################################################################################
  # Remove the mqccred exits from /var/mqm
  #####################################################################################
  rm -f /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred*
  rm -f /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred*

  #####################################################################################
  # If this installation is currently the primary remove any symlinks..
  #####################################################################################
  if [ "${RPM_PACKAGE_VERSION}.${RPM_PACKAGE_RELEASE}" = "$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b)" ] ; then 
    setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -U -p ${MQ_INSTALLATION_PATH} 2>&1`
    rc=$?
    if [ $rc -ne 0 ] ; then
      echo "ERROR: Return code \"$rc\" from setmqinst for \"-U -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
      echo "       ${setmqinst_out}" >&2
    fi
  fi

  #####################################################################################
  # Remove any certificate license files.
  #####################################################################################
  rm -f ${MQ_INSTALLATION_PATH}/lib/amq?cert.lic 2>/dev/null
fi 
echo "Resetting return code to success" > /dev/null
if [ ${1} -eq 0 ] ; then
:

# Removing product links
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
fi

%postun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/runtime_postuninstall.sh
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2020" 
#   crc="632453442" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2020 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# Post uninstallation script
FILE='@(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/runtime_postuninstall.sh'
MYENV=`env`

# Remove any interim fix backup directories

backups_count=`ls -1d  ${MQ_INSTALLATION_PATH}/fix-backups.* 2> /dev/null | wc -l` 
if [ $backups_count -ne 0 ] ; then 
  rm -rf ${MQ_INSTALLATION_PATH}/fix-backups.*
  rm -rf ${MQ_INSTALLATION_PATH}/mqpatch.log
  rm -rf ${MQ_INSTALLATION_PATH}/mqpatch.dat
fi

# Remove any remaining empty directories (except lost+found and .snapshots (GPFS),
# also honour AMQ_IGNORE_SNAPDIRNAME which allows user to supply location to ignore if .snapshots has been renamed)

if [ "${AMQ_IGNORE_SNAPDIRNAME}" = "" ] ; then
  SNAPDIR_NAME=".snapshots"
else
  SNAPDIR_NAME="${AMQ_IGNORE_SNAPDIRNAME}"
fi

if [ ${MQ_UPGRADE} = 'No' ] ; then 
  find ${MQ_INSTALLATION_PATH} -depth -type d ! -name lost+found ! -name "${SNAPDIR_NAME}" -exec rmdir {} > /dev/null 2>&1 \;
fi


echo "Resetting return code to success" > /dev/null
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
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/runtime_posttrans.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2023,2024"
#   crc="1956258177" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2023, 2024 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Posttrans script for MQ

LANG=C
LC_ALL=C
export LANG
export LC_ALL

MQ_INSTALL_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -f512 -b`

# if the mqccred exit is missing and we stored a backup before, copy it back
if [ ! -r /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred ]
then
  if [ -r /tmp/mqccred.backup ]
  then
    cp /tmp/mqccred.backup /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred
  fi
fi

if [ ! -r /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred_r ]
then
  if [ -r /tmp/mqccred.backup ]
  then
    cp /tmp/mqccred_r.backup /var/mqm/exits/${MQ_INSTALL_NAME}/mqccred_r
  fi
fi

if [ ! -r /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred ]
then
  if [ -r /tmp/mqccred.backup64 ]
  then
    cp /tmp/mqccred.backup64 /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred
  fi
fi

if [ ! -r /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred_r ]
then
  if [ -r /tmp/mqccred.backup64 ]
  then
    cp /tmp/mqccred_r.backup64 /var/mqm/exits64/${MQ_INSTALL_NAME}/mqccred_r
  fi
fi

# tidy up any backups that might exist for completeness
rm -f /tmp/mqccred*

###########################################################################
# Check if any preserved license type exists
# If any preserved license exists and the current installation edition is different
# Then copy the lic files into /lib
###########################################################################
LICENSE_TYPE=`${MQ_INSTALLATION_PATH}/bin/dspmqver -bf 8192`
if [ -r /tmp/mq_preserved_license/${MQ_INSTALL_NAME}/LicenseType.txt ] ; then
  PRESERVED_LICENSE=`cat /tmp/mq_preserved_license/${MQ_INSTALL_NAME}/LicenseType.txt`
  if [ "$PRESERVED_LICENSE" != "$LICENSE_TYPE" ] ; then
    # If the preserved license type is Developer copies the developer licenses
    if [ "$PRESERVED_LICENSE" == 'Developer' ] ; then
      cp -f ${MQ_INSTALLATION_PATH}/samp/amqpcert.lic ${MQ_INSTALLATION_PATH}/lib 2>/dev/null
      cp -f ${MQ_INSTALLATION_PATH}/samp/amqdcert.lic ${MQ_INSTALLATION_PATH}/lib 2>/dev/null
    else
      # If the preserved license type is Trial copies the Trial licenses
      if [ "$PRESERVED_LICENSE" == 'Trial' ] ; then
        cp -f ${MQ_INSTALLATION_PATH}/samp/amqtcert.lic ${MQ_INSTALLATION_PATH}/lib 2>/dev/null
      fi
    fi
  fi
fi

rm -rf /tmp/mq_preserved_license/${MQ_INSTALL_NAME} 2>/dev/null

