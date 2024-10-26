class HtmlDocument:
    extension = 'html'  # Class attribute for file extension
    version = '5'       # Class attribute for version

    def __init__(self, css):
        self.css = 'Yes'  # Instance attribute initialized with 'Yes'
    
    def instancemethod(self):
        """Instance method that prints a message."""
        print(f'This is an instance method!')  # Can access instance attributes (e.g., self.css)

    @staticmethod 
    def staticmethod():
        """Static method that prints a message."""
        print(f'I am static method')  # Cannot access instance (self) or class (cls) attributes

    @classmethod
    def classmethod(cls):
        """Class method that prints a message and can access class attributes."""
        print(f'I am class method')  # Can access class attributes via 'cls'

    def __call__(self, *args, **kwargs):
        """Makes the instance callable like a function."""
        return f'Called with arguments: {args} and keyword arguments: {kwargs}'  
        # Allows instances of this class to be called with arguments
        # This is useful for when you want the instance to behave like a function

# Create a reference to the HtmlDocument class
htmlDocument = HtmlDocument('css.attribute')

# Accessing class variable 'extension' using dot notation
print(f'Fetching Class variables using dot notation: {HtmlDocument.extension}')

# Accessing class variable 'extension' using getattr() function
print(f'Fetching Class variables using getattr() notation: {getattr(HtmlDocument, "extension")}')

# Modifying the class variable 'version'
HtmlDocument.version = 100  # Changes the class variable 'version' to 100

# Modifying the class variable 'extension'
setattr(HtmlDocument, 'extension', 'XHTML')  # Changes 'extension' to 'XHTML'

# Printing the class's __dict__, which shows all its attributes
print(HtmlDocument.__dict__)

# Fetching class variable 'version' using getattr() after modification
print(f'Fetching Class variables using getattr() notation: {getattr(HtmlDocument, "version")}')

# Deleting the class variable 'version'
delattr(HtmlDocument, 'version')  # Removes 'version' from the class

# Deleting the class variable 'extension'
del HtmlDocument.extension  # Removes 'extension' from the class

# Printing the class's __dict__ after deletions
print(HtmlDocument.__dict__)  # Shows remaining attributes of the class


# Callable Class Attributes

# Statie Method 

HtmlDocument.staticmethod()

# Class Method

HtmlDocument.classmethod()

# Callable Object

print(htmlDocument(1,2,key='value'))

