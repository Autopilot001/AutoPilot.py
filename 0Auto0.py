import socket

# Define the IP address and port to listen on
HOST = 'localhost'  # replace with your desired IP address
PORT = 8080  # replace with your desired port number

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified IP address and port
s.bind((HOST, PORT))

# Listen for incoming connections
s.listen()

print(f'Listening on {HOST}:{PORT}...')

# Accept incoming connections and handle data
while True:
    # Wait for a client to connect
    conn, addr = s.accept()
    print(f'Connected by {addr}')

    # Receive data from the client
    data = conn.recv(1024)
    print(f'Received: {data.decode()}')

    # Close the connection
    conn.close()
