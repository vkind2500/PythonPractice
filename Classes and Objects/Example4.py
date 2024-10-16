class HtmlDocument:
    version = 5
    extension = 'html'

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents
        
htmlDocument = HtmlDocument('Blank','Test')

print(f'The type of Class __dict__ is {type(HtmlDocument.__dict__)}')
print(f'The type of Intance __dict__ is {type(htmlDocument.__dict__)}')

print(f'Values stored in Class __dict__ :-> {HtmlDocument.__dict__}')
print(f'Values stored in Instance __dict__ :-> {htmlDocument.__dict__}')

print(f'Accessing Class variable "version" using Class "HtmlDocument" : {HtmlDocument.version}')
print(f'Accessing Class variable "extension" using Class "HtmlDocument" : {HtmlDocument.extension}')


print(f'Accessing Class variable "extension" using Instance "htmlDocument" : {htmlDocument.extension}')
print(f'Accessing Class variable "version" using Instance "htmlDocument" : {htmlDocument.version}')


print(f'Accessing Instance variable "name" using Instance "htmlDocument" : {htmlDocument.name}')
print(f'Accessing Instance variable "contents" using Instance "htmlDocument" : {htmlDocument.contents}')

# Adding Class Variable 

HtmlDocument.type = "XHTML"

# Adding Instance Variable

htmlDocument.css = "No"

print(f'HtmlDocument.type is {HtmlDocument.type} and htmlDocument.css is {htmlDocument.css}')



        