# Builder

The Builder pattern is a typical Java pattern that you see less of in the 
Python world. This is because a lot of the examples can be solved by using 
keyword arguments in the objects constructor, negating the need for a Builder pattern.

## How does it work

You have a Builder object that knows how to build a complex object. Often, this 
object will be a Composite (an object which consists of several similar objects, 
which can again consists of several similar objects, etc.). You can build these 
complex objects by calling certain methods on the Builder, in the order you require.
This is often done by a Director, but could also be done directly by the client, 
depending on the situation. The Director does nothing more than instruct the Builder
which specific steps have to be taken. In the case that the instructions come from a
different source (say, a user interface), then the Director becomes an unnecessary 
extra layer and you can leave it out.
The Builder is not concerned with how to parse the input, because it just knows how to create the parts that need to be created.
So you separate the logic of parsing your input and creating a complex object. 
At the end, you ask the Builder to build() your object and you get the end result.


## Applicability

As said, most of the older examples given for Java users can be solved by just using
keyword arguments. However, there are still some cases where you could make use of the 
Builder pattern in Python, and I think the place where it shines the most is where 
input is sequentially parsed and used to create an object, for instance when creating
a document in a certain different format.

To illustrate, let's create a MarkdownBuilder, that allows us to create a nicely
formatted markdown document.

Of course, we start with an interface for our BlogPostBuilder:

```python
from abc import ABC, abstractmethod

class BlogPostBuilder(ABC):
    @abstractmethod
    def add_title(self, text):
        raise NotImplementedError

    @abstractmethod
    def add_header(self, text):
        raise NotImplementedError

    @abstractmethod
    def add_paragraph(self, text):
        raise NotImplementedError

    @abstractmethod
    def add_list(self, list_of_points):
        raise NotImplementedError

    def build():
        raise NotImplementedError
```

Then the MarkdownBlogPostBuilder code could be something very rudimentary like:

```python

class MarkdownBlogPostBuilder(BlogPostBuilder):
    def __init__(self):
        self.lines = []

    def add_title(self, text):
        self.lines.append(f"# {text}")

    def add_header(self, text):
        self.lines.append(f"## {text}")

    def add_paragraph(self, text):
        self.lines.append(f"{text}\n")

    def add_list(self, list_of_points):
        list_text = ""
        for point in list_of_points:
            list_text += f"* {point}\n"
        self.lines.append(list_text)
    
    def build(self):
        return "\n".join(self.lines)

```

We can now make a very simple blogpost to test it out

```python

if __name__ == "__main__":

    builder = MarkdownBlogPostBuilder()

    builder.add_title("The Builder design pattern")
    builder.add_paragraph("Used to create a complex object in several steps.")

    builder.add_header("Builder")

    builder.add_paragraph(
        "The Builder pattern is a typical Java pattern that you see less of in the "
        "Python world. This is because a lot of the examples can be solved by using "
        "keyword arguments in the objects constructor, negating the need for a "
        "Builder pattern."
    )

    builder.add_paragraph(
        "However, there are some cases where you could make use of the Builder "
        "pattern, and I think the place where it shines the most is where input "
        "is sequentially parsed and used to create an object."
    )

    builder.add_list(
        [
            "Effective when you can't construct an object completely in one go",
            "In most cases you can just use keyword args for your constructor",
            "Not used often in Python",
        ]
    )

    text = builder.build()
    print(text)
```

Which gives the output
```
# The Builder design pattern
Used to create a complex object in several steps.

## Builder
The Builder pattern is a typical Java pattern that you see less of in the Python world. This is because a lot of the examples can be solved by using keyword arguments in the objects constructor, negating the need for a Builder pattern.

However, there are some cases where you could make use of the Builder pattern, and I think the place where it shines the most is where input is sequentially parsed and used to create an object.

* Effective when you can't construct an object completely in one go
* In most cases you can just use keyword args for your constructor
* Not used often in Python
```

You can see that if we switched the MarkdownBlogPostBuilder for an HTMLBlogPostBuilder
or a LaTeXBlogPostBuilder, our client code would not have to change, and we'd get the
output we expect.

We used the builder now directly, but you could also have a `Director` that will parse
and convert input for you. All you have to do is deliver the data to the Director and
it will give you a correctly formatted text back. (You could for instance use this to
convert HTML to Markdown).

## Fluent interface

A lot of people think one of the key characteristics of a Builder object is being able
to chain methods like so `builder.addThing().addOtherThing().doMore()`. This chaining of
methods is called a `fluent interface`. And although you could definitely have your builder
implement a fluent interface, it's not a prerequisite. In fact, I think one of the key
advantages of using a Builder is in cases where you do not have all the info at your
disposal to create the object in one go. And that is what you would be doing with a
fluent interface.