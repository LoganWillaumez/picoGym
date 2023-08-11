import socket

dataToDecode = []

# Create a connection to the specified server and port
with socket.create_connection(('mercury.picoctf.net', 21135)) as s:
    # Receive data from the server
    get = s.recv(1024).decode()
    
    # For each line of data (assuming they are separated by newlines),
    # convert the number to its corresponding ASCII character
    dataToDecode = ''.join([chr(int(code.strip())) for code in get.split("\n") if code])

# Print the decoded data
print(dataToDecode)
