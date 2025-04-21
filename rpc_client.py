"""
   Practical_1 - Design a distributed application using RPC for remote computation where client submits an integer value
                 to the server and server calculates factorial and returns the result to the client program."""


import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

number = int(input("Enter an integer to compute factorial for: "))

result = server.compute_factorial(number)

print(f"The factorial of {number} is {result}")
