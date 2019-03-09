# ---------------------------------------------------------------- #
# Title: HTML Render: A class-based system for rendering html
# Change Log: (Who, When, What)
# D. Rodriguez, 2019-03-05, Initial release
# ---------------------------------------------------------------- #
# !/usr/bin/env python3


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = [] if content is None else [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        open_tag = ["<{}".format(self.tag)]

        # Attributes
        for key, value in self.attributes.items():
            open_tag.append(' ' + key + '=' + '"' + value + '"')

        open_tag.append(">\n")
        out_file.write("".join(open_tag))

        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")

        out_file.write("</{}>\n".format(self.tag))


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, out_file):
        out_file.write("<{}".format(self.tag))

        for key, value in self.attributes.items():
            out_file.write(' ')
            out_file.write(key)
            out_file.write('="')
            out_file.write(str(value))
            out_file.write('"')

        out_file.write(">".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, out_file):
        out_file.write("<{} ".format(self.tag))

        # Attributes
        for key, value in self.attributes.items():
            out_file.write(key) # + '=' + '"' + value + '"')
            out_file.write('="')
            out_file.write(str(value))
            out_file.write('" ')

        out_file.write("/>\n".format(self.tag))

    def append(self, *args):
        raise TypeError("You can not add content to a SelfClosingTag")

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content=content, **kwargs)


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h' + str(level)
        super().__init__(content, **kwargs)
