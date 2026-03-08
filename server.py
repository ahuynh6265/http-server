import socket, threading, json


HOST = '127.0.0.1'
PORT = 8080 

#create an IPv4 (AF_INET) TCP (SOCK_STREAM) socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#associate the socket with a specific network interface (HOST) and port number (PORT)
server_socket.bind((HOST, PORT))
#enable the server to accept connections of up to 5 users
server_socket.listen(5)

json_test = {
  "pet": "Wally",
  "players": {
    "lakers": ["Luka Doncic", "Lebron"], 
    "heat": ["Jimmy Butler", "Bam Adebayo"]
  }
}



print(f"Server listening on {HOST}:{PORT}")

def handle_connection(client_socket): 

  #read up to 1024 bytes of data from the client and convert from bytes to a string
  request = client_socket.recv(1024).decode()
  headers_section, _, body_section = request.partition("\r\n\r\n")
  print(request)

  if request:
    first_line = request.splitlines()[0]
    print(f"Request line: {first_line}")

    
    get_line = first_line.split()
    method = get_line[0] 
    path = get_line[1]
    version = get_line[2]
    print(f"get line: {get_line}")
    print(f"method: {method}")

    path, _, query = path.partition("?")
     
    print(path)
    if path == "/": 
      body = "Welcome to my HTTP server"
      status = "HTTP/1.1 200 OK"
      content_type = "text/plain"

    elif path == "/users" and method == "POST": 
      data = json.loads(body_section)
      body = json.dumps(data)
      status = "HTTP/1.1 201 CREATED"
      content_type = "application/json"

    elif path == "/about":
      body = "About page"
      status = "HTTP/1.1 200 OK"
      content_type = "text/plain"

    elif path == "/data":
      body = json.dumps(json_test)
      status = "HTTP/1.1 200 OK"
      content_type = "application/json"

    elif path.startswith("/static/"):
      file_path = path.lstrip("/")
      try:
        with open(file_path, "r") as file:
          data = file.read() 
      except FileNotFoundError:
        body = "File not found"
        status = "HTTP/1.1 404 NOT FOUND"
        content_type = "text/html"
      else: 
        body = data 
        status = "HTTP/1.1 200 OK"
        content_type = "text/html"
    
    elif path == "/search":
      results = {}
      split = query.split("&")
      for s in split:
        key, value = s.split("=")
        results[key] = value
      if "q" in results:
        body = json.dumps(results)
        status = "HTTP/1.1 200 OK"
        content_type = "text/html"


    else:
      body = "Not found"
      status = "HTTP/1.1 404 NOT FOUND"
      content_type = "text/plain"
    
    response = (
    f"{status}\r\n"
    f"Content-Type: {content_type}\r\n"
    f"Content-Length: {len(body)}\r\n"
    "\r\n"
    + body
    )

    #send the complete http response to the client and shut down the connection
    client_socket.sendall(response.encode())
    client_socket.close() 
  

while True:
  #accept an incoming connection and delegate it to a new thread for parallel processing 
  client_socket, client_address = server_socket.accept()
  print(f"Connection from {client_address}")

  #create and start a background thread to handle specific client
  thread = threading.Thread(target=handle_connection, args=(client_socket,))
  thread.start() 
  
