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
