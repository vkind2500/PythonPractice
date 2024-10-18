# Python Static Methods

To define a static method, we use the ``@staticmethod`` decorator:

```python
class className:
    @staticmethod
    def static_method_name(param_list):
        pass
```

To call a static method, we use this syntax:

```
className.static_method_name()
```

> **Note :** In practice, we use static methods to define utility methods or group functions that have some logical relationships in a class.

<h3>Python static methods vs class methods</h2>

<table border="2" cellpadding="8" cellspacing="0">
    <thead>
        <tr>
            <th>Class Methods</th>
            <th>Static Methods</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Python implicitly pass the cls argument to class methods.</td>
            <td>Python doesn’t implicitly pass the cls argument to static methods</td>
        </tr>
        <tr>
            <td>Class methods can access and modify the class state.</td>
            <td>Static methods cannot access or modify the class state.</td>
        </tr>
        <tr>
            <td>Use @classmethod decorators to define class methods</td>
            <td>Use @staticmethod decorators to define static methods.</td>
        </tr>
    </tbody>
</table>


#### Example : [Temperature Converter](Example6.py)