#!/bin/bash

echo ""
echo ""
echo "system: "
echo "-----"
cat /etc/system-release
echo ""

echo ""
echo ""
echo "os: "
echo "-----"
cat /etc/os-release
echo ""

echo ""
echo ""
echo "glibc: "
echo "-----"
ldd --version
echo ""
