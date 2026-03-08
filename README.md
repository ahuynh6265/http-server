# HTTP Server
HTTP/1.1 Server built from scratch using raw Python sockets, no frameworks. 

## Live Demo
https://web-production-c67a8.up.railway.app/

## Tech Stack
Built entirely with Python standard library, no external dependencies.
- **socket** - TCP handling 
- **threading** - Concurrent connections
- **json** - Request/Response serialization
- **datetime** - Request logging

## Features 
- Static file serving from /static/ directory 
- Multithreaded connection handling 
- Query parameter parsing 
- In-memory user storage with GET, POST, DELETE 
- JSON response/request support 
- Request logging with timestamp 

## Getting Started
**1. Clone the repo**
```bash 
git clone https://github.com/ahuynh6265/http-server.git
cd http-server 
```

**2. Start Server**
```bash
python3 server.py
```