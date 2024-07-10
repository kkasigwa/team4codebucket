Summary: IBM MQ Samples FileSet
Name: MQSeriesSamples
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
This package provides the sample applications which can be used to check a
IBM MQ installation using the verification procedures.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/samp
install -d $RPM_BUILD_ROOT/opt/mqm/samp/bin
install -d $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl
install -d $RPM_BUILD_ROOT/opt/mqm/samp/xatm
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dlq
install -d $RPM_BUILD_ROOT/opt/mqm/samp/pubsub
install -d $RPM_BUILD_ROOT/opt/mqm/inc
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer
install -d $RPM_BUILD_ROOT/opt/mqm/java
install -d $RPM_BUILD_ROOT/opt/mqm/samp/preconnexit
install -d $RPM_BUILD_ROOT/opt/mqm/lib
install -d $RPM_BUILD_ROOT/opt/mqm/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava
install -d $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple
install -d $RPM_BUILD_ROOT/opt/mqm/samp/pcf
install -d $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Samples-9.4.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Samples-9.4.0.mqtag
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Samples-9.4.0.mqtag
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscic0 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscic0
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscic0
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscicc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscicc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscicc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscic064 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscic064
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscic064
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscicc64 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscicc64
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscicc64
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscbf $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscbf
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscbf
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsech $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsech
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsech
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsact $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsact
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsact
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsinq $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsinq
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsinq
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsset $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsset
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsset
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgbr $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgbr
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgbr
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsget $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsget
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsget
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsreq $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsreq
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsreq
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsput $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsput
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsput
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsapt $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsapt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsapt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssub $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssub
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssub
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspub $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspub
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspub
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsptl $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsptl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsptl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqstrg $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqstrg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqstrg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsbcg $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsbcg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsbcg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgrm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgrm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgrm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsprm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsprm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsprm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsqrm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsqrm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsqrm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsxrm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsxrm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsxrm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqswlm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqswlm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqswlm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsrua $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsrua
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsrua
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaxe $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaxe
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaxe
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaxe_r $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaxe_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaxe_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaem $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaem
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaem
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaem_r $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaem_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaem_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspse $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspse
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspse
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsmon $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsmon
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsmon
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsmonc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsmonc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsmonc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsevt $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsevt
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsevt
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsstm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsstm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsstm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsiqm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsiqm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsiqm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/inc/amqsvmha.h $RPM_BUILD_ROOT/opt/mqm/inc/amqsvmha.h
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/inc/amqsvmha.h
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsauth.h $RPM_BUILD_ROOT/opt/mqm/samp/amqsauth.h
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsauth.h
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsauth.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsauth.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsauth.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsgbr0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsgbr0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsgbr0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscbf0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqscbf0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqscbf0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsget0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsget0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsget0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsact0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsact0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsact0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsinqa.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsinqa.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsinqa.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstrg0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqstrg0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqstrg0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsreq0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsreq0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsreq0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsput0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsput0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsput0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsapt0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsapt0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsapt0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqssuba.c $RPM_BUILD_ROOT/opt/mqm/samp/amqssuba.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqssuba.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqspuba.c $RPM_BUILD_ROOT/opt/mqm/samp/amqspuba.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqspuba.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsptl0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsptl0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsptl0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsseta.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsseta.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsseta.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsecha.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsecha.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsecha.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsvfc0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsvfc0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsvfc0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsbcg0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsbcg0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsbcg0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsgrma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsgrma.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsgrma.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsprma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsprma.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsprma.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsqrma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsqrma.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsqrma.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsxrma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsxrma.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsxrma.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqswlm0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqswlm0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqswlm0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsaxe0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsaxe0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsaxe0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsaem0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsaem0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsaem0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqspse0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqspse0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqspse0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsmon0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsmon0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsmon0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsevta.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsevta.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsevta.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsaicq.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsaicq.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsaicq.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsaiem.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsaiem.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsaiem.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsailq.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsailq.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsailq.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsstop.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsstop.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsstop.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscnxc.c $RPM_BUILD_ROOT/opt/mqm/samp/amqscnxc.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqscnxc.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqssslc.c $RPM_BUILD_ROOT/opt/mqm/samp/amqssslc.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqssslc.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsstma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsstma.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsstma.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsiqma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsiqma.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsiqma.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscos0.tst $RPM_BUILD_ROOT/opt/mqm/samp/amqscos0.tst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqscos0.tst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsruaa.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsruaa.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsruaa.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqmechx.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amqmechx.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqmechx.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqmsetx.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amqmsetx.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqmsetx.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0gbr0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0gbr0.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amq0gbr0.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0get0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0get0.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amq0get0.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0ptl0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0ptl0.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amq0ptl0.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqminqx.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amqminqx.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqminqx.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0put0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0put0.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amq0put0.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0req0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0req0.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amq0req0.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqmdefs.tst $RPM_BUILD_ROOT/opt/mqm/samp/amqmdefs.tst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqmdefs.tst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0pub0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0pub0.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amq0pub0.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0sub0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0sub0.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amq0sub0.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscic0.ccs $RPM_BUILD_ROOT/opt/mqm/samp/amqscic0.ccs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqscic0.ccs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscic0.tst $RPM_BUILD_ROOT/opt/mqm/samp/amqscic0.tst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqscic0.tst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscih0.h $RPM_BUILD_ROOT/opt/mqm/samp/amqscih0.h
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqscih0.h
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqzscix.c $RPM_BUILD_ROOT/opt/mqm/samp/amqzscix.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqzscix.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqzscgx.c $RPM_BUILD_ROOT/opt/mqm/samp/amqzscgx.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqzscgx.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/xa.h $RPM_BUILD_ROOT/opt/mqm/samp/xatm/xa.h
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/xa.h
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxas0.sqc $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.sqc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.sqc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxas0.ec $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.ec
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.ec
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxas0.cp $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.cp
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.cp
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxas0.pc $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.pc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.pc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxag0.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxag0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxag0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxag0.c.inf $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxag0.c.inf
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxag0.c.inf
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxab0.sqc $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxab0.sqc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxab0.sqc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxab0.ec $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxab0.ec
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxab0.ec
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxaf0.sqc $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxaf0.sqc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxaf0.sqc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxaf0.ec $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxaf0.ec
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxaf0.ec
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amq0xas0.sqb $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xas0.sqb
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xas0.sqb
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amq0xag0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xag0.cbl
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xag0.cbl
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amq0xab0.sqb $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xab0.sqb
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xab0.sqb
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amq0xaf0.sqb $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xaf0.sqb
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xaf0.sqb
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/xaswit.mak $RPM_BUILD_ROOT/opt/mqm/samp/xatm/xaswit.mak
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/xaswit.mak
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/db2swit.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/db2swit.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/db2swit.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/db2swits.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/db2swits.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/db2swits.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/oraswit.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/oraswit.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/oraswit.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/oraswitd.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/oraswitd.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/oraswitd.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/sybswit.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/sybswit.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/sybswit.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/infswit.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/infswit.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/xatm/infswit.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxgx.c $RPM_BUILD_ROOT/opt/mqm/samp/amqstxgx.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqstxgx.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxpx.c $RPM_BUILD_ROOT/opt/mqm/samp/amqstxpx.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqstxpx.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxsx.c $RPM_BUILD_ROOT/opt/mqm/samp/amqstxsx.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqstxsx.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/ubbstxcx.cfg $RPM_BUILD_ROOT/opt/mqm/samp/ubbstxcx.cfg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/ubbstxcx.cfg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxvx.v $RPM_BUILD_ROOT/opt/mqm/samp/amqstxvx.v
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqstxvx.v
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxvx.flds $RPM_BUILD_ROOT/opt/mqm/samp/amqstxvx.flds
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqstxvx.flds
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqka.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqka.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqka.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqla.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqla.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqla.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqma.y $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.y
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.y
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqna.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqna.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqna.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqoa.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqoa.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqoa.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqpa.l $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqpa.l
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqpa.l
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqha.h $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqha.h
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqha.h
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodkha.h $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodkha.h
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodkha.h
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodtha.h $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodtha.h
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodtha.h
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqpa.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqpa.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqpa.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqua.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqua.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqua.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqx.mk $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqx.mk
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqx.mk
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqma.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqma.h $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.h
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.h
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqsdlq.msg $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqsdlq.msg
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqsdlq.msg
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsdlq $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsdlq
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsdlq
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsputc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsputc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsputc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaptc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaptc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaptc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssubc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssubc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssubc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspubc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspubc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspubc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsptlc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsptlc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsptlc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscnxc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscnxc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscnxc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssslc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssslc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssslc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscbfc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscbfc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscbfc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgetc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgetc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgetc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgrmc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgrmc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgrmc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsprmc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsprmc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsprmc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqstrgc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqstrgc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqstrgc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgbrc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgbrc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgbrc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsreqc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsreqc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsreqc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssetc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssetc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssetc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsbcgc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsbcgc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsbcgc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsactc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsactc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsactc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsinqc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsinqc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsinqc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsechc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsechc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsechc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsstmc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsstmc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsstmc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsiqmc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsiqmc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsiqmc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsruac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsruac
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsruac
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsdlqc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsdlqc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsdlqc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqdputs $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqdputs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqdputs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqsputs $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsputs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsputs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqsgets $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsgets
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsgets
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqwrlds $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqwrlds
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqwrlds
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqdputc $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqdputc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqdputc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqsputc $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsputc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsputc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqsgetc $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsgetc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsgetc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqwrldc $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqwrldc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqwrldc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/imqdput.cpp $RPM_BUILD_ROOT/opt/mqm/samp/imqdput.cpp
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/imqdput.cpp
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/imqsget.cpp $RPM_BUILD_ROOT/opt/mqm/samp/imqsget.cpp
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/imqsget.cpp
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/imqsput.cpp $RPM_BUILD_ROOT/opt/mqm/samp/imqsput.cpp
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/imqsput.cpp
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/imqwrld.cpp $RPM_BUILD_ROOT/opt/mqm/samp/imqwrld.cpp
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/imqwrld.cpp
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/SimpleGet.cs $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/SimpleGet.cs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/SimpleGet.cs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/SimpleGet.csproj $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/SimpleGet.csproj
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/SimpleGet.csproj
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/build.sh $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/build.sh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/build.sh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimpleGet.dll $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimpleGet.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimpleGet.dll
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimpleGet.runtimeconfig.json $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimpleGet.runtimeconfig.json
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimpleGet.runtimeconfig.json
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/bin/amqmdnetstd.dll $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/amqmdnetstd.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/amqmdnetstd.dll
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/SimplePut.cs $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/SimplePut.cs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/SimplePut.cs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/build.sh $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/build.sh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/build.sh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/SimplePut.csproj $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/SimplePut.csproj
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/SimplePut.csproj
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimplePut.dll $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimplePut.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimplePut.dll
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimplePut.runtimeconfig.json $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimplePut.runtimeconfig.json
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimplePut.runtimeconfig.json
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/SimpleProducer.cs $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/SimpleProducer.cs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/SimpleProducer.cs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/SimpleProducer.csproj $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/SimpleProducer.csproj
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/SimpleProducer.csproj
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/build.sh $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/build.sh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/build.sh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/amqmdnetstd.dll $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/amqmdnetstd.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/amqmdnetstd.dll
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/amqmxmsstd.dll $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/amqmxmsstd.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/amqmxmsstd.dll
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleProducer.dll $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleProducer.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleProducer.dll
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleProducer.runtimeconfig.json $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleProducer.runtimeconfig.json
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleProducer.runtimeconfig.json
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/build.sh $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/build.sh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/build.sh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/SimpleConsumer.cs $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/SimpleConsumer.cs
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/SimpleConsumer.cs
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/SimpleConsumer.csproj $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/SimpleConsumer.csproj
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/SimpleConsumer.csproj
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleConsumer.dll $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleConsumer.dll
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleConsumer.dll
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleConsumer.runtimeconfig.json $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleConsumer.runtimeconfig.json
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleConsumer.runtimeconfig.json
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsppc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsppc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsppc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsspc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsspc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsspc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspr1 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspr1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspr1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssr1 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssr1
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssr1
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspr2 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspr2
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspr2
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssr2 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssr2
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssr2
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsrr2 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsrr2
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsrr2
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgr2 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgr2
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgr2
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgam $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgam
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgam
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsres $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsres
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsres
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsspca.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsspca.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsspca.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqspr1a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspr1a.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspr1a.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqssr1a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqssr1a.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqssr1a.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqspr2a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspr2a.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspr2a.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqssr2a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqssr2a.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqssr2a.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsrr2a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsrr2a.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsrr2a.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsgr2a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgr2a.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgr2a.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsppca.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsppca.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsppca.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsgama.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgama.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgama.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsgama.tst $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgama.tst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgama.tst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqspsra.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspsra.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspsra.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsresa.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsresa.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsresa.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsresa.tst $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsresa.tst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsresa.tst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqssbxa.c $RPM_BUILD_ROOT/opt/mqm/samp/amqssbxa.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqssbxa.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssbx $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssbx
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssbx
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssbxc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssbxc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssbxc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsblst.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsblst.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsblst.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsblst $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsblst
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsblst
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsblstc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsblstc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsblstc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqslog0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqslog0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqslog0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqslog $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqslog
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqslog
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqslogc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqslogc
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqslogc
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsphac.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsphac.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsphac.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsghac.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsghac.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsghac.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsmhac.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsmhac.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsmhac.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsfhac.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsfhac.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsfhac.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsphac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsphac
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsphac
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsghac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsghac
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsghac
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsmhac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsmhac
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsmhac
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsfhac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsfhac
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsfhac
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsclma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsclma.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/amqsclma.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsclm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsclm
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsclm
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/preconnexit/amqlcel0.c $RPM_BUILD_ROOT/opt/mqm/samp/preconnexit/amqlcel0.c
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/preconnexit/amqlcel0.c
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqlcelp $RPM_BUILD_ROOT/opt/mqm/lib/amqlcelp
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqlcelp
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqlcelp_r $RPM_BUILD_ROOT/opt/mqm/lib/amqlcelp_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib/amqlcelp_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqlcelp $RPM_BUILD_ROOT/opt/mqm/lib64/amqlcelp
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqlcelp
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqlcelp_r $RPM_BUILD_ROOT/opt/mqm/lib64/amqlcelp_r
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/lib64/amqlcelp_r
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/preconnexit/ibm-amq.schema $RPM_BUILD_ROOT/opt/mqm/samp/preconnexit/ibm-amq.schema
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/preconnexit/ibm-amq.schema
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqat.ini $RPM_BUILD_ROOT/opt/mqm/samp/mqat.ini
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/mqat.ini
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqauthg.sh $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqauthg.sh
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqauthg.sh
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQIVP.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQIVP.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQIVP.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample\$Subscriber.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample\$Subscriber.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample\$Subscriber.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQSample.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSample.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSample.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQIVP.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQIVP.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQIVP.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQSample.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSample.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSample.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/mqjcivp.properties $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/mqjcivp.properties
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/mqjcivp.properties
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/example.security.policy $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/example.security.policy
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/example.security.policy
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsBrowser.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsBrowser.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsBrowser.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsConsumer.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsConsumer.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsConsumer.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiBrowser.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiBrowser.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiBrowser.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiConsumer.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiConsumer.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiConsumer.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiProducer.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiProducer.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiProducer.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsProducer.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsProducer.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsProducer.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava\$1.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava\$1.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava\$1.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/MyContext.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/MyContext.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/MyContext.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Keys.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Keys.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Keys.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsGreaterThanOrEqualZero.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsGreaterThanOrEqualZero.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsGreaterThanOrEqualZero.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsOneWord.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsOneWord.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsOneWord.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidDestination.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidDestination.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidDestination.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidICConnFactName.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidICConnFactName.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidICConnFactName.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidICDestName.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidICDestName.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidICDestName.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidInitialContextURI.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidInitialContextURI.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidInitialContextURI.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidNumberOfMessages.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidNumberOfMessages.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidNumberOfMessages.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidPortNumber.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidPortNumber.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidPortNumber.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidRTTDestination.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidRTTDestination.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidRTTDestination.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Literals.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Literals.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Literals.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Options.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Options.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Options.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Keys.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Keys.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Keys.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Literals.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Literals.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Literals.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/MyContext.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/MyContext.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/MyContext.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Options.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Options.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Options.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/Requestor.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Requestor.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Requestor.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/Responder\$RespondingMessageListener.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Responder\$RespondingMessageListener.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Responder\$RespondingMessageListener.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/Responder.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Responder.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Responder.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$CleaningListener.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$CleaningListener.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$CleaningListener.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$RequestCleaner.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$RequestCleaner.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$RequestCleaner.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$1.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$1.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor\$1.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/Requestor.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Requestor.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Requestor.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/Responder.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Responder.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/Responder.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimplePTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePTP.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePTP.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimplePubSub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePubSub.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePubSub.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimplePTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePTP.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePTP.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimplePubSub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePubSub.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePubSub.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsBrowser.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsBrowser.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsBrowser.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsConsumer.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsConsumer.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsConsumer.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiBrowser.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiBrowser.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiBrowser.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiConsumer.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiConsumer.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiConsumer.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiProducer.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiProducer.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiProducer.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsProducer.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsProducer.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsProducer.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms3.0/samples/simple/SimpleAsyncPutPTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimpleAsyncPutPTP.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimpleAsyncPutPTP.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms3.0/samples/simple/SimplePTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePTP.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePTP.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms3.0/samples/simple/SimplePTPJNDI.class $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePTPJNDI.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePTPJNDI.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms3.0/samples/simple/SimplePubSub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePubSub.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePubSub.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms3.0/samples/simple/SimpleAsyncPutPTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimpleAsyncPutPTP.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimpleAsyncPutPTP.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms3.0/samples/simple/SimplePTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePTP.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePTP.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms3.0/samples/simple/SimplePTPJNDI.java $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePTPJNDI.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePTPJNDI.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms3.0/samples/simple/SimplePubSub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePubSub.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/jms3.0/samples/simple/SimplePubSub.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CommonMethods.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CommonMethods.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CommonMethods.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ClearQueue.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ClearQueue.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ClearQueue.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CreateChannel.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateChannel.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateChannel.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CreateQueue.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateQueue.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateQueue.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_StartChannel.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StartChannel.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StartChannel.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_StopChannel.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StopChannel.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StopChannel.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.class
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.class
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ClearQueue.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ClearQueue.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ClearQueue.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CommonMethods.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CommonMethods.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CommonMethods.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CreateChannel.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateChannel.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateChannel.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CreateQueue.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateQueue.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateQueue.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_StartChannel.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StartChannel.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StartChannel.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_StopChannel.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StopChannel.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StopChannel.java
install /build/jslot0/p940_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.java
touch -t '202406061327' $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.java

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/bin/gl"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/xatm"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dlq"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/pubsub"
%dir %attr(555,mqm,mqm) "/opt/mqm/inc"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer"
%dir %attr(555,mqm,mqm) "/opt/mqm/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/preconnexit"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/wmqjava"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/wmqjava/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples/simple"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms3.0"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms3.0/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/pcf"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/pcf/samples"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Samples-9.4.0.mqtag"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscic0"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscicc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscic064"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscicc64"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscbf"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsech"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsact"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsinq"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsset"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgbr"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsget"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsreq"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsput"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsapt"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssub"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspub"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsptl"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqstrg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsbcg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgrm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsprm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsqrm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsxrm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqswlm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsrua"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaxe"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaxe_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaem"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaem_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspse"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsmon"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsmonc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsevt"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsstm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsiqm"
%attr(444,mqm,mqm) "/opt/mqm/inc/amqsvmha.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsauth.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsauth.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsgbr0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscbf0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsget0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsact0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsinqa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstrg0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsreq0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsput0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsapt0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqssuba.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqspuba.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsptl0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsseta.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsecha.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsvfc0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsbcg0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsgrma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsprma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsqrma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsxrma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqswlm0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsaxe0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsaem0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqspse0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsmon0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsevta.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsaicq.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsaiem.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsailq.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsstop.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscnxc.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqssslc.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsstma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsiqma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscos0.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsruaa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqmechx.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqmsetx.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0gbr0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0get0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0ptl0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqminqx.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0put0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0req0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqmdefs.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0pub0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0sub0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscic0.ccs"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscic0.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscih0.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqzscix.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqzscgx.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/xa.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxas0.sqc"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxas0.ec"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxas0.cp"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxas0.pc"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxag0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxag0.c.inf"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxab0.sqc"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxab0.ec"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxaf0.sqc"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxaf0.ec"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amq0xas0.sqb"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amq0xag0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amq0xab0.sqb"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amq0xaf0.sqb"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/xaswit.mak"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/db2swit.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/db2swits.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/oraswit.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/oraswitd.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/sybswit.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/infswit.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxgx.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxpx.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxsx.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/ubbstxcx.cfg"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxvx.v"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxvx.flds"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqka.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqla.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqma.y"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqna.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqoa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqpa.l"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqha.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodkha.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodtha.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqpa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqua.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqx.mk"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqma.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqsdlq.msg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsdlq"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsputc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaptc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssubc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspubc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsptlc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscnxc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssslc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscbfc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgetc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgrmc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsprmc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqstrgc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgbrc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsreqc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssetc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsbcgc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsactc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsinqc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsechc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsstmc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsiqmc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsruac"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsdlqc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqdputs"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqsputs"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqsgets"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqwrlds"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqdputc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqsputc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqsgetc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqwrldc"
%attr(444,mqm,mqm) "/opt/mqm/samp/imqdput.cpp"
%attr(444,mqm,mqm) "/opt/mqm/samp/imqsget.cpp"
%attr(444,mqm,mqm) "/opt/mqm/samp/imqsput.cpp"
%attr(444,mqm,mqm) "/opt/mqm/samp/imqwrld.cpp"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/SimpleGet.cs"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/SimpleGet.csproj"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/SimpleGet/build.sh"
%attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimpleGet.dll"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimpleGet.runtimeconfig.json"
%attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/bin/amqmdnetstd.dll"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/SimplePut.cs"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/build.sh"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/SimplePut/SimplePut.csproj"
%attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimplePut.dll"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/base/bin/SimplePut.runtimeconfig.json"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/SimpleProducer.cs"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/SimpleProducer.csproj"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleProducer/build.sh"
%attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/amqmdnetstd.dll"
%attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/amqmxmsstd.dll"
%attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleProducer.dll"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleProducer.runtimeconfig.json"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/build.sh"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/SimpleConsumer.cs"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/SimpleConsumer/SimpleConsumer.csproj"
%attr(555,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleConsumer.dll"
%attr(444,mqm,mqm) "/opt/mqm/samp/dotnet/samples/cs/core/xms/bin/SimpleConsumer.runtimeconfig.json"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsppc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsspc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspr1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssr1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspr2"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssr2"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsrr2"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgr2"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgam"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsres"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsspca.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqspr1a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqssr1a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqspr2a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqssr2a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsrr2a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsgr2a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsppca.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsgama.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsgama.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqspsra.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsresa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsresa.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqssbxa.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssbx"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssbxc"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsblst.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsblst"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsblstc"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqslog0.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqslog"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqslogc"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsphac.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsghac.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsmhac.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsfhac.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsphac"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsghac"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsmhac"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsfhac"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsclma.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsclm"
%attr(444,mqm,mqm) "/opt/mqm/samp/preconnexit/amqlcel0.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqlcelp"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqlcelp_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqlcelp"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqlcelp_r"
%attr(444,mqm,mqm) "/opt/mqm/samp/preconnexit/ibm-amq.schema"
%attr(444,mqm,mqm) "/opt/mqm/samp/mqat.ini"
%attr(555,mqm,mqm) "/opt/mqm/samp/bin/amqauthg.sh"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQIVP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample$Subscriber.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQSample.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQIVP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQSample.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/mqjcivp.properties"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/example.security.policy"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsBrowser.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsConsumer.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiBrowser.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiConsumer.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiProducer.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsProducer.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava$1.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/MyContext.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Keys.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsGreaterThanOrEqualZero.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsOneWord.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidDestination.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidICConnFactName.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidICDestName.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidInitialContextURI.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidNumberOfMessages.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidPortNumber.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidRTTDestination.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Literals.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Options.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Keys.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Literals.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/MyContext.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Options.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/Requestor.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/Responder$RespondingMessageListener.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/Responder.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor$CleaningListener.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor$RequestCleaner.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor$1.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/Requestor.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/Responder.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/requestReply/ThreadedRequestor.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimplePTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimplePubSub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimplePTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimplePubSub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsBrowser.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsConsumer.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiBrowser.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiConsumer.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiProducer.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsProducer.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple/SimpleAsyncPutPTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple/SimplePTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple/SimplePTPJNDI.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple/SimplePubSub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple/SimpleAsyncPutPTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple/SimplePTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple/SimplePTPJNDI.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms3.0/samples/simple/SimplePubSub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CommonMethods.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ClearQueue.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CreateChannel.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CreateQueue.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_StartChannel.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_StopChannel.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ClearQueue.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CommonMethods.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CreateChannel.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CreateQueue.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_StartChannel.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_StopChannel.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.java"

%pre
if [ ! -z "${INST_DEBUG}" ] ; then 
  set -x
fi
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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

