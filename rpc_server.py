"""
   Practical_1 - Design a distributed application using RPC for remote computation where client submits an integer value
                 to the server and server calculates factorial and returns the result to the client program."""

from xmlrpc.server import SimpleXMLRPCServer

def compute_factorial(number):
    
    result = 1

    if number > 1:
        for i in range(1,number+1):
            result *= i
        return result
    
    return result

server = SimpleXMLRPCServer(("localhost",8000))

print("Server listening on port 8000")

server.register_function(compute_factorial, 'compute_factorial')
server.serve_forever()

