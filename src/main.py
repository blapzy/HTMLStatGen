from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    testnode = TextNode("hello world", TextType.PLAIN)
    print(testnode)

    testhtmlnode = HTMLNode("p", "hello world", None, {
    "href": "https://www.google.com",
    "target": "_blank",
    })
    print(testhtmlnode)
    print(testhtmlnode.props_to_html())
    

main()