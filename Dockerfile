FROM python:3.9-slim

RUN pip3 install websockets

COPY ./python_server.py home/root/WEB_SOCKET_WS/server_drone_python/python_server.py
RUN chmod +x /home/root/WEB_SOCKET_WS/server_drone_python/python_server.py

WORKDIR /home/root/WEB_SOCKET_WS/server_drone_python/
CMD ["python3", "python_server.py"]
