import socket
import time

HOST = '127.0.0.1'
PORT = 3000

type Headers = list[(str, str)]
type Body = str

def http_response(headers: Headers, body: Body) -> str:
    headers_string= "\r\n".join(f"{k}: {v}" for k, v in headers)
    response = (
        f"HTTP/1.1 200 OK\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"{headers_string}\r\n"
        f"\r\n"
        f"{body}"
    )
    return response

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Serving on http://{HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            request = conn.recv(1024).decode('utf-8')

            print("\n\n** New request **")
            print(f"Request from: {addr} \n\n")

            print("Request info:")
            print(request)

            response = http_response(
                [
                    ("Content-Type", "text/plain"),
                    ("token", "1234567890")
                ],
                ("Hello, World!\nThis is a simple HTTP server.\n"),
            )
            conn.sendall(response.encode('utf-8'))

            print(f"Response to: {addr}")