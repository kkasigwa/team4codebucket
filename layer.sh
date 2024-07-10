#!/bin/bash

mkdir python
cd python

unzip ../pymqi-1.12.10-cp39-cp39-linux_x86_64.whl -d ./

cp -rpv ../MQServer/lib/ ./lib/

zip -r ../layer-pymqi.zip ./

cd ../

