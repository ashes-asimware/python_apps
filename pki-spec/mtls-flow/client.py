import ssl
import urllib.request


def main():
    url = "https://localhost:4443"

    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(cafile="certs/ca.crt")
    context.load_cert_chain(certfile="certs/client.crt", keyfile="certs/client.key")

    with urllib.request.urlopen(url, context=context) as response:
        print("Response status:", response.status)
        print("Body:")
        print(response.read().decode())


if __name__ == "__main__":
    main()
