#!/bin/bash
set -e

mkdir -p certs
cd certs

echo "== Creating CA =="
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 \
  -subj "/C=US/ST=CA/O=DemoCA/CN=Demo-CA" \
  -out ca.crt

echo "== Creating Server Key & CSR =="
openssl genrsa -out server.key 2048
openssl req -new -key server.key \
  -subj "/C=US/ST=CA/O=DemoServer/CN=localhost" \
  -out server.csr

echo "== Signing Server Cert with CA =="
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out server.crt -days 365 -sha256

echo "Server certs generated in ./certs"
``
