#   Connects REQ socket to tcp://localhost:5555
#   Sends something to the server and expects a return message back
#

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send(b"London, 3")

#  Get the reply.
message = socket.recv()
print(f"Received reply \n [ {bytes.decode(message)} ]")