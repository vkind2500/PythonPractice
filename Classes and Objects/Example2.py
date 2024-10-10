class Request:
    def send(*args):
        return f'Sent {args}'
        
html_request = Request()

print(f'The vaue of Request.send is {Request.send}')     
print(f'The type of Request.send is {type(Request.send)}')


print(f'Calling send via Request class :  {Request.send()}')
print (f'Calling send via html_request : {html_request.send()}')
print(f'Object Id : {hex(id(html_request))}')