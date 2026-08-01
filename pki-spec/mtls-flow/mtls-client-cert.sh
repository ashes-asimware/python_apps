#!/bin/bash
set -e

cd certs

echo "== Creating Client Key & CSR =="
openssl genrsa -out client.key 2048
openssl req -new -key client.key \
  -subj "/C=US/ST=CA/O=DemoClient/CN=client" \
  -out client.csr

echo "== Signing Client Cert with CA =="
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -out client.crt -days 365 -sha256

echo "Client cert generated"
