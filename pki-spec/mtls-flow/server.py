import ssl
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
async def root(request: Request):
    client_cert = request.scope.get("ssl_object")

    client_cn = "Unknown"
    if client_cert:
        cert = client_cert.getpeercert()
        if cert:
            subject = dict(x[0] for x in cert['subject'])
            client_cn = subject.get("commonName", "Unknown")

    return {"message": f"Hello, {client_cn}!"}


def create_ssl_context():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    # Require client certificate
    context.verify_mode = ssl.CERT_REQUIRED

    context.load_cert_chain(
        certfile="certs/server.crt",
        keyfile="certs/server.key"
    )

    context.load_verify_locations(cafile="certs/ca.crt")

    return context


if __name__ == "__main__":
    ssl_context = create_ssl_context()

    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=4443,
        ssl_certfile="certs/server.crt",
        ssl_keyfile="certs/server.key",
        ssl_ca_certs="certs/ca.crt",
        ssl_cert_reqs=ssl.CERT_REQUIRED,  # enforce mTLS
    )
``
