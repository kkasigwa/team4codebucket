Summary: IBM MQ Server FileSet
Name: MQSeriesServer
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
This package provides the queue manager messaging and queuing services for
IBM MQ.
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
install -d $RPM_BUILD_ROOT/opt/mqm/inc
install -d $RPM_BUILD_ROOT/opt/mqm/bin/security
install -d $RPM_BUILD_ROOT/opt/mqm/java
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/ibm.com_IBM_MQ-9.4.0.swidtag $RPM_BUILD_ROOT/opt/mqm/swidtag/ibm.com_IBM_MQ-9.4.0.swidtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/ibm.com_IBM_MQ-9.4.0.swidtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqbrk $RPM_BUILD_ROOT/opt/mqm/bin/runmqbrk
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqbrk
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqfcxba $RPM_BUILD_ROOT/opt/mqm/bin/amqfcxba
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqfcxba
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dltmqbrk $RPM_BUILD_ROOT/opt/mqm/bin/dltmqbrk
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dltmqbrk
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqbrk $RPM_BUILD_ROOT/opt/mqm/bin/endmqbrk
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/endmqbrk
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqfqpub $RPM_BUILD_ROOT/opt/mqm/bin/amqfqpub
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqfqpub
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqcrsta $RPM_BUILD_ROOT/opt/mqm/bin/amqcrsta
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqcrsta
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqpcsea $RPM_BUILD_ROOT/opt/mqm/bin/amqpcsea
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqpcsea
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzif_r $RPM_BUILD_ROOT/opt/mqm/lib64/amqzif_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqzif_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzfu $RPM_BUILD_ROOT/opt/mqm/lib64/amqzfu
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqzfu
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzfud $RPM_BUILD_ROOT/opt/mqm/lib64/amqzfud
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqzfud
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmz1_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmz1_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmz1_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzfuma $RPM_BUILD_ROOT/opt/mqm/bin/amqzfuma
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzfuma
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqoamd $RPM_BUILD_ROOT/opt/mqm/bin/amqoamd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqoamd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/security/amqoamax $RPM_BUILD_ROOT/opt/mqm/bin/security/amqoamax
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/security/amqoamax
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/security/amqoampx $RPM_BUILD_ROOT/opt/mqm/bin/security/amqoampx
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/security/amqoampx
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/security/amqpamcf $RPM_BUILD_ROOT/opt/mqm/bin/security/amqpamcf
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/security/amqpamcf
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqzsc $RPM_BUILD_ROOT/opt/mqm/lib/amqzsc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqzsc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqzscg $RPM_BUILD_ROOT/opt/mqm/lib/amqzscg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqzscg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcics_r.a $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcics_r.a
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcics_r.a
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzsc $RPM_BUILD_ROOT/opt/mqm/lib64/amqzsc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqzsc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzscg $RPM_BUILD_ROOT/opt/mqm/lib64/amqzscg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqzscg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcics_r.a $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcics_r.a
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcics_r.a
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzlaa0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzlaa0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzlaa0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzlsa0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzlsa0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzlsa0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzxma0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzxma0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzxma0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzmgr0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzmgr0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzmgr0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzmuc0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzmuc0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzmuc0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzmuf0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzmuf0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzmuf0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzmur0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzmur0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzmur0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/crtmqm $RPM_BUILD_ROOT/opt/mqm/bin/crtmqm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/crtmqm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dltmqm $RPM_BUILD_ROOT/opt/mqm/bin/dltmqm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dltmqm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dmpmqaut $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqaut
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqaut
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqcsv $RPM_BUILD_ROOT/opt/mqm/bin/dspmqcsv
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqcsv
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqfls $RPM_BUILD_ROOT/opt/mqm/bin/dspmqfls
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqfls
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqaut $RPM_BUILD_ROOT/opt/mqm/bin/dspmqaut
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqaut
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqtrn $RPM_BUILD_ROOT/opt/mqm/bin/dspmqtrn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqtrn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmq $RPM_BUILD_ROOT/opt/mqm/bin/dspmq
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmq
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqaut $RPM_BUILD_ROOT/opt/mqm/bin/setmqaut
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/setmqaut
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqcsv $RPM_BUILD_ROOT/opt/mqm/bin/endmqcsv
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/endmqcsv
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqm $RPM_BUILD_ROOT/opt/mqm/bin/endmqm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/endmqm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rcdmqimg $RPM_BUILD_ROOT/opt/mqm/bin/rcdmqimg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rcdmqimg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rcrmqobj $RPM_BUILD_ROOT/opt/mqm/bin/rcrmqobj
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rcrmqobj
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqchi $RPM_BUILD_ROOT/opt/mqm/bin/runmqchi
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqchi
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqlsr $RPM_BUILD_ROOT/opt/mqm/bin/runmqlsr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqlsr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runswchl $RPM_BUILD_ROOT/opt/mqm/bin/runswchl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runswchl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrcmla $RPM_BUILD_ROOT/opt/mqm/bin/amqrcmla
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqrcmla
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrrmfa $RPM_BUILD_ROOT/opt/mqm/bin/amqrrmfa
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqrrmfa
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrmppa $RPM_BUILD_ROOT/opt/mqm/bin/amqrmppa
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqrmppa
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzlwa0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzlwa0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqzlwa0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqlsr $RPM_BUILD_ROOT/opt/mqm/bin/endmqlsr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/endmqlsr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqchl $RPM_BUILD_ROOT/opt/mqm/bin/runmqchl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqchl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqtrm $RPM_BUILD_ROOT/opt/mqm/bin/runmqtrm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runmqtrm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rsvmqtrn $RPM_BUILD_ROOT/opt/mqm/bin/rsvmqtrn
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rsvmqtrn
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/addmqinf $RPM_BUILD_ROOT/opt/mqm/bin/addmqinf
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/addmqinf
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqinf $RPM_BUILD_ROOT/opt/mqm/bin/dspmqinf
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqinf
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/rmvmqinf $RPM_BUILD_ROOT/opt/mqm/bin/rmvmqinf
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/rmvmqinf
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqsstop $RPM_BUILD_ROOT/opt/mqm/bin/amqsstop
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqsstop
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqm $RPM_BUILD_ROOT/opt/mqm/bin/setmqm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/setmqm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqprd $RPM_BUILD_ROOT/opt/mqm/bin/setmqprd
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/setmqprd
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqspl $RPM_BUILD_ROOT/opt/mqm/bin/dspmqspl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dspmqspl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqspl $RPM_BUILD_ROOT/opt/mqm/bin/setmqspl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/setmqspl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runamscred $RPM_BUILD_ROOT/opt/mqm/bin/runamscred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runamscred
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/strmqm $RPM_BUILD_ROOT/opt/mqm/bin/strmqm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/strmqm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/strmqcsv $RPM_BUILD_ROOT/opt/mqm/bin/strmqcsv
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/strmqcsv
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqml_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqml_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqml_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqml_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqml_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqml_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmalda_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmalda_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmalda_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmaldb_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmaldb_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmaldb_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmzf.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzf.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzf.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmzf.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzf.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzf.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmzf_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzf_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzf_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmzf_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzf_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzf_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqutl.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqutl.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqutl.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqutl.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqutl.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqutl.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqutl_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqutl_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqutl_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqutl_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqutl_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqutl_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqzi.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqzi.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqzi.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqzi.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzi.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzi.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqzi_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqzi_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqzi_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqzi_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzi_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzi_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqds.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqds.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqds.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqds.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqds.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqds.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqds_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqds_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqds_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqds_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqds_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqds_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmr.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmr.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmr.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmr.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmr.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmr.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmr_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmr_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmr_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmr_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmr_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmr_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcb.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcb.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcb.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcb.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcb.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcb.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcb_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcb_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcb_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcb_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcb_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcb_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcbrt.o $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcbrt.o
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcbrt.o
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcbrt.o $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcbrt.o
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcbrt.o
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmxa.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmxa.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmxa.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmxa.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmxa64.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa64.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa64.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmxa_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmxa_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmxa_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmxa_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmxa64_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa64_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa64_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmax.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmax.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmax.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmax.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmax_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmax_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqmax_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmax_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmax64.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax64.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax64.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmax64_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax64_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax64_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqzaax $RPM_BUILD_ROOT/opt/mqm/lib/amqzaax
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqzaax
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzaax $RPM_BUILD_ROOT/opt/mqm/lib64/amqzaax
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqzaax
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqzaax_r $RPM_BUILD_ROOT/opt/mqm/lib/amqzaax_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqzaax_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzaax_r $RPM_BUILD_ROOT/opt/mqm/lib64/amqzaax_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqzaax_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amq64ax $RPM_BUILD_ROOT/opt/mqm/lib64/amq64ax
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amq64ax
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amq64ax_r $RPM_BUILD_ROOT/opt/mqm/lib64/amq64ax_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amq64ax_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/dmpmqlog $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqlog
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqlog
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/migmqlog $RPM_BUILD_ROOT/opt/mqm/bin/migmqlog
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/migmqlog
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqs23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqs23gl.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libimqs23gl.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqs23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqs23gl_r.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libimqs23gl_r.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqs23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqs23gl.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libimqs23gl.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqs23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqs23gl_r.so.4.1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libimqs23gl_r.so.4.1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqldmpa $RPM_BUILD_ROOT/opt/mqm/bin/amqldmpa
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqldmpa
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqlrepa $RPM_BUILD_ROOT/opt/mqm/bin/amqlrepa
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqlrepa
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqspdbg $RPM_BUILD_ROOT/opt/mqm/bin/amqspdbg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqspdbg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrfdm $RPM_BUILD_ROOT/opt/mqm/bin/amqrfdm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqrfdm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrdbgm $RPM_BUILD_ROOT/opt/mqm/bin/amqrdbgm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqrdbgm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqmfsck $RPM_BUILD_ROOT/opt/mqm/bin/amqmfsck
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqmfsck
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqorxr $RPM_BUILD_ROOT/opt/mqm/bin/amqorxr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqorxr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqwasoa $RPM_BUILD_ROOT/opt/mqm/lib64/amqwasoa
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqwasoa
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqwascx $RPM_BUILD_ROOT/opt/mqm/lib64/amqwascx
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqwascx
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqjxs_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxs_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxs_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqjxs_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxs_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxs_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqjxds_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxds_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxds_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqjxds_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxds_r.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxds_r.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzxmr0 $RPM_BUILD_ROOT/opt/mqm/lib64/amqzxmr0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqzxmr0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/libmqjbnd.so $RPM_BUILD_ROOT/opt/mqm/java/lib/libmqjbnd.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/libmqjbnd.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/libmqjbnd.so $RPM_BUILD_ROOT/opt/mqm/java/lib64/libmqjbnd.so
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib64/libmqjbnd.so
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jdbc/jdbcdb2.o $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/jdbcdb2.o
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/jdbcdb2.o
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jdbc/jdbcora.o $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/jdbcora.o
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/jdbcora.o
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jdbc/Makefile $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/Makefile
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/Makefile
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/jdbc/jdbcdb2.o $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/jdbcdb2.o
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/jdbcdb2.o
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/jdbc/jdbcora.o $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/jdbcora.o
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/jdbcora.o
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/jdbc/Makefile $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/Makefile
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/Makefile
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqp.sh $RPM_BUILD_ROOT/opt/mqm/bin/amqp.sh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/amqp.sh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqxacred $RPM_BUILD_ROOT/opt/mqm/bin/setmqxacred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/setmqxacred
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/mqcertck $RPM_BUILD_ROOT/opt/mqm/bin/mqcertck
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/mqcertck
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/bin/runqmcred $RPM_BUILD_ROOT/opt/mqm/bin/runqmcred
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/bin/runqmcred

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/inc"
%dir %attr(550,root,mqm) "/opt/mqm/bin/security"
%dir %attr(555,mqm,mqm) "/opt/mqm/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/jdbc"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib64/jdbc"
%attr(444,mqm,mqm) %config(missingok) "/opt/mqm/swidtag/ibm.com_IBM_MQ-9.4.0.swidtag"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqbrk"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqfcxba"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dltmqbrk"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqbrk"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqfqpub"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqcrsta"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqpcsea"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzif_r"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzfu"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzfud"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmz1_r.so"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzfuma"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqoamd"
%attr(4550,root,mqm) %verify(not md5 mtime) "/opt/mqm/bin/security/amqoamax"
%attr(4550,root,mqm) %verify(not md5 mtime) "/opt/mqm/bin/security/amqoampx"
%attr(555,mqm,mqm) "/opt/mqm/bin/security/amqpamcf"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqzsc"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqzscg"
%attr(555,mqm,mqm) "/opt/mqm/lib/libmqmcics_r.a"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzsc"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzscg"
%attr(555,mqm,mqm) "/opt/mqm/lib64/libmqmcics_r.a"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzlaa0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzlsa0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzxma0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzmgr0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzmuc0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzmuf0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzmur0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/crtmqm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dltmqm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dmpmqaut"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqcsv"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqfls"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqaut"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqtrn"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmq"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqaut"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqcsv"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rcdmqimg"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rcrmqobj"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqchi"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqlsr"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runswchl"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrcmla"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrrmfa"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrmppa"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzlwa0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqlsr"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqchl"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqtrm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rsvmqtrn"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/addmqinf"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqinf"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rmvmqinf"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqsstop"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqm"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqprd"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqspl"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqspl"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runamscred"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/strmqm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/strmqcsv"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqml_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqml_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmalda_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmaldb_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmzf.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmzf.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmzf_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmzf_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqutl.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqutl.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqutl_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqutl_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqzi.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqzi.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqzi_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqzi_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqds.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqds.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqds_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqds_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmr.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmr.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmr_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmr_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcb.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcb.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcb_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcb_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcbrt.o"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcbrt.o"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmxa.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmxa.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmxa64.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmxa_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmxa_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmxa64_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmax.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmax.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmax_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmax_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmax64.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmax64_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqzaax"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzaax"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqzaax_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzaax_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amq64ax"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amq64ax_r"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dmpmqlog"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/migmqlog"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqs23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqs23gl_r.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqs23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqs23gl_r.so.4.1"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqldmpa"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqlrepa"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqspdbg"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrfdm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrdbgm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqmfsck"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqorxr"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqwasoa"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqwascx"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqjxs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqjxs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqjxds_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqjxds_r.so"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzxmr0"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib/libmqjbnd.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib64/libmqjbnd.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib/jdbc/jdbcdb2.o"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib/jdbc/jdbcora.o"
%attr(555,mqm,mqm) "/opt/mqm/java/lib/jdbc/Makefile"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib64/jdbc/jdbcdb2.o"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib64/jdbc/jdbcora.o"
%attr(555,mqm,mqm) "/opt/mqm/java/lib64/jdbc/Makefile"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqp.sh"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqxacred"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/mqcertck"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runqmcred"

%pre
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
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
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
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
# Linking ${MQ_INSTALLATION_PATH}/bin/runmqbrk to ${MQ_INSTALLATION_PATH}/bin/strmqbrk
if [ ! -d ${MQ_INSTALLATION_PATH}/bin ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/bin
else
    rm -f ${MQ_INSTALLATION_PATH}/bin/strmqbrk
fi
ln -s ${MQ_INSTALLATION_PATH}/bin/runmqbrk ${MQ_INSTALLATION_PATH}/bin/strmqbrk
chown -fh mqm ${MQ_INSTALLATION_PATH}/bin/strmqbrk
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/bin/strmqbrk
# Linking ${MQ_INSTALLATION_PATH}/lib64/amqzfu to ${MQ_INSTALLATION_PATH}/lib/amqzfu
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/amqzfu
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/amqzfu ${MQ_INSTALLATION_PATH}/lib/amqzfu
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/amqzfu
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/amqzfu
# Linking ${MQ_INSTALLATION_PATH}/lib64/amqzfud to ${MQ_INSTALLATION_PATH}/lib/amqzfud
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/amqzfud
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/amqzfud ${MQ_INSTALLATION_PATH}/lib/amqzfud
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/amqzfud
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/amqzfud
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmzf.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmzf.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmzf.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmzf.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmzf_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmzf_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmzf_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmzf_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqutl.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqutl.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqutl.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqutl.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqutl_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqutl_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqutl_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqutl_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmcb.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmcb.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmcb.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmcb.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmcb_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmcb_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmcb_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmcb_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmxa.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmxa.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmxa.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmxa.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmxa64.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmxa64.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmxa_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmxa_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmxa_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmxa_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmxa64_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmxa64_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmax.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmax.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmax.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmax.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmax_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmax_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmax_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmax_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmax64.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmax64.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmax64_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmax64_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/server_postinstall.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2012,2024"
#   crc="3622503993" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2012, 2024 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>


INSTALLROOT=${MQ_INSTALLATION_PATH}


# Invoke setmqinst to refresh symlinks if this installation is the primary
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi
echo > /dev/null

# Create a default PAM configuration
if [ -x ${MQ_INSTALLATION_PATH}/bin/security/amqpamcf ] ; then
  ${MQ_INSTALLATION_PATH}/bin/security/amqpamcf 2>&1
fi

#  Run the mqconfig tool to analyse the system against  the kernel requirements etc.

if [ -x  ${MQ_INSTALLATION_PATH}/bin/mqconfig ]  ; then
  MQCONFIG_LOGFILE=/tmp/mqconfig.$$.log
  INSTALL_VR="`${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b | awk -F. '{print $1 "." $2}'`"
  ${MQ_INSTALLATION_PATH}/bin/mqconfig -v ${INSTALL_VR} > ${MQCONFIG_LOGFILE} 2>&1
  if [ $?  -ne 0 ] ; then
    echo "" >&2
    echo "WARNING: System settings for this system do not meet recommendations for this product " >&2
    echo "         See the log file at \"${MQCONFIG_LOGFILE}\" for more information" >&2
    echo "" >&2
  else
     rm  ${MQCONFIG_LOGFILE}
  fi
fi

#  Scan for any previously installed Advanced components
LICENSE_TYPE=`${MQ_INSTALLATION_PATH}/bin/dspmqver -b -f 8192`
if [ "$LICENSE_TYPE" != "Developer" ] || [ "$LICENSE_TYPE" != "License not accepted" ] ; then 
  command=`basename $(ls -l /proc/${PPID}/exe | awk '{print $NF}')`
  for packagename in ${ADVANCEDPACKAGELIST}
    do
      if [ ${command} = 'rpm' ] ; then
        rpm_query_out=`rpm -q ${packagename}${PACKAGE_SUFFIX}`
        if [ ${?} = 0 ] ; then
          setmqinst_out=`${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l advanced -e yes 2>&1`
          rc=$?
          if [ $rc -ne 0 ] ; then
            echo "ERROR: Return code \"$rc\" from setmqinst for \"-p ${MQ_INSTALLATION_PATH}\", output is:" >&2
            echo "       ${setmqinst_out}" >&2
          fi
        fi
      else
        deb_pkgname=`echo ${packagename} | sed s#_#-#g| awk '{print tolower($0)}' | sed s#mqseries#ibmmq-#`
        dpkg_out=`dpkg-query --showformat='${Status}\n' -W ${deb_pkgname} 2>&1`
        if [ $? -eq 0  ] ; then
          dpkg_status=`dpkg-query --showformat='${Status}\n' -W ${deb_pkgname}  2>/dev/null | awk '{print $3}'`
          if [  ${dpkg_status} = 'installed' ] ; then
            setmqinst_out=`${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l advanced -e yes 2>&1`
            rc=$?
            if [ $rc -ne 0 ] ; then
              echo "ERROR: Return code \"$rc\" from setmqinst for \"-p ${MQ_INSTALLATION_PATH}\", output is:" >&2
              echo "       ${setmqinst_out}" >&2
            fi
          fi
        fi
      fi
  done
fi
  # ########################################################################################################
  # If a Non-production swtag exists then delete it and issue the appropriate setmqinst command to create
  # a new one at the current level
  # ########################################################################################################
  if [ -f ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced_for_Non-Production_Environment-*swtag ] ; then 
    ls ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced_for_Non-Production_Environment-*swtag
    rm ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced_for_Non-Production_Environment-*swtag
    ${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l nonprod -e y 2>&1
    rc=$?
    if [ $rc -ne 0 ] ; then
      echo "ERROR: Return code \"$rc\" from setmqinst for \"-p ${MQ_INSTALLATION_PATH}\", output is:" >&2
      echo "       ${setmqinst_out}" >&2
    fi 
  fi 
 


%preun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
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
# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/server_preuninstall.sh
#
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72,"
#   years="2005,2023"
#   crc="2836959397" >
#   Licensed Materials - Property of IBM
#
#   5724-H72,
#
#   (C) Copyright IBM Corp. 2005, 2023 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>
#
# Pre uninstallation script for Server
set -o vi 
if [ ${MQ_UPGRADE} = "No" ] ; then 
  if [ -x ${MQ_INSTALLATION_PATH}/bin/setmqinst ] ; then 
   setmqinst_out=`${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l nonprod -e no 2>&1 `
   setmqinst_out=`${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l advanced -e no 2>&1 `
  fi 

  rm -vf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_High_Availability_Replica-*.swidtag

fi 
# If we are upgrading remove the 'old' version Advanced swiidtag
if [ ${MQ_UPGRADE} = "Yes" ] ; then 
  rm -f ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced-${RPM_PACKAGE_VERSION}.swidtag
fi 
echo "Resetting return code to success" > /dev/null
if [ ${1} -eq 0 ] ; then
:

# Removing product links
rm -f ${MQ_INSTALLATION_PATH}/bin/strmqbrk
rm -f ${MQ_INSTALLATION_PATH}/lib/amqzfu
rm -f ${MQ_INSTALLATION_PATH}/lib/amqzfud
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
fi

%postun
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
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
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
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

# @(#) MQMBID sn=p940-L240606.TRIAL su=_kuor4iPzEe-M5d-9sa1WMw pn=install/unix/linux_2/server_posttrans.sh
#   <copyright
#   notice="lm-source-program"
#   pids="5724-H72"
#   years="2024"
#   crc="3622503993" >
#   Licensed Materials - Property of IBM
#
#   5724-H72
#
#   (C) Copyright IBM Corp. 2024 All Rights Reserved.
#
#   US Government Users Restricted Rights - Use, duplication or
#   disclosure restricted by GSA ADP Schedule Contract with
#   IBM Corp.
#   </copyright>


INSTALLROOT=${MQ_INSTALLATION_PATH}

# Old rpm -U would be a little too aggressive and undo everything that was done in the post install script.
# So here we re-run everything just in case.

# Invoke setmqinst to refresh symlinks if this installation is the primary
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi
echo > /dev/null

#  Scan for any previously installed Advanced components
licensetype=`${MQ_INSTALLATION_PATH}/bin/dspmqver -b -f 8192`
if [ "${licensetype}" != 'Developer' ] ; then
  command=`basename $(ls -l /proc/${PPID}/exe | awk '{print $NF}')`
  for packagename in ${ADVANCEDPACKAGELIST}
    do
    if [ ${command} = 'rpm' ] ; then
      rpm_query_out=`rpm -q ${packagename}${PACKAGE_SUFFIX}`
      if [ ${?} = 0 ] ; then
        setmqinst_out=`${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l advanced -e yes 2>&1`
        rc=$?
        if [ $rc -ne 0 ] ; then
          echo "ERROR: Return code \"$rc\" from setmqinst for \"-p ${MQ_INSTALLATION_PATH}\", output is:" >&2
          echo "       ${setmqinst_out}" >&2
        fi
     fi
    else
      deb_pkgname=`echo ${packagename} | sed s#_#-#g| awk '{print tolower($0)}' | sed s#mqseries#ibmmq-#`
      dpkg_out=`dpkg-query --showformat='${Status}\n' -W ${deb_pkgname} 2>&1`
      if [ $? -eq 0  ] ; then
        dpkg_status=`dpkg-query --showformat='${Status}\n' -W ${deb_pkgname}  2>/dev/null | awk '{print $3}'`
        if [  ${dpkg_status} = 'installed' ] ; then
          setmqinst_out=`${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l advanced -e yes 2>&1`
          rc=$?
          if [ $rc -ne 0 ] ; then
            echo "ERROR: Return code \"$rc\" from setmqinst for \"-p ${MQ_INSTALLATION_PATH}\", output is:" >&2
            echo "       ${setmqinst_out}" >&2
          fi
        fi
     fi
   fi
  done
fi
# ########################################################################################################
# If a Non-production swtag exists then delete it and issue the appropriate setmqinst command to create
# a new one at the current level
# ########################################################################################################
if [ -f ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced_for_Non-Production_Environment-*swtag ] ; then 
  ls ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced_for_Non-Production_Environment-*swtag
  rm ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced_for_Non-Production_Environment-*swtag
  ${MQ_INSTALLATION_PATH}/bin/setmqinst -p ${MQ_INSTALLATION_PATH} -l nonprod -e y 2>&1
  rc=$?
  if [ $rc -ne 0 ] ; then
    echo "ERROR: Return code \"$rc\" from setmqinst for \"-p ${MQ_INSTALLATION_PATH}\", output is:" >&2
    echo "       ${setmqinst_out}" >&2
  fi 
fi 

# ########################################################################################################
# When upgrading from a prior DE level to a Prod image of a new release 
# use appropriate swidtags based on license type
# ########################################################################################################
LICENSE_TYPE=`${MQ_INSTALLATION_PATH}/bin/dspmqver -bf 8192`
MQ_INSTALL_NAME=`${MQ_INSTALLATION_PATH}/bin/dspmqver -bf 512`
if [ "${LICENSE_TYPE}" = "License not accepted" ]; then
  BUILD_TYPE=`${MQ_INSTALLATION_PATH}/bin/amqicvar -f ${MQ_INSTALLATION_PATH}/lib64/libmqmcs_r.so -b -n -z -q -i MQ_LICENSE_TYPE`
  case ${BUILD_TYPE} in
    "PRODUCTION")
      if [ -r ${MQ_INSTALLATION_PATH}/lib/amqdcert.lic ]; then
        LICENSE_TYPE="Developer"
      else
        if [ -r ${MQ_INSTALLATION_PATH}/lib/amqtcert.lic ]; then
          LICENSE_TYPE="Trial"
        fi
      fi
      ;;
    "DEVELOPER")
      LICENSE_TYPE="Developer"
    ;;
    "TRIAL")
      LICENSE_TYPE="Trial"
    ;;
  esac    
fi
if [ "${LICENSE_TYPE}" = "Developer" ] ; then
  rm -rf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ-${RPM_PACKAGE_VERSION}.swidtag
  rm -rf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced_Message_Security-${RPM_PACKAGE_VERSION}.swidtag
  rm -rf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Client-${RPM_PACKAGE_VERSION}.swidtag
  rm -rf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Managed_File_Transfer_Agent-${RPM_PACKAGE_VERSION}.swidtag
  rm -rf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Managed_File_Transfer_Service-${RPM_PACKAGE_VERSION}.swidtag
  rm -rf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Telemetry-${RPM_PACKAGE_VERSION}.swidtag
  rm -rf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced-${RPM_PACKAGE_VERSION}.swidtag
else
  rm -rf ${MQ_INSTALLATION_PATH}/swidtag/ibm.com_IBM_MQ_Advanced_for_Developers_Non-Warranted-${RPM_PACKAGE_VERSION}.swidtag
fi

