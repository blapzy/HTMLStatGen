import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "ashd", None, {
        "href": "https://www.google.com",
        "target": "_blank",
        })
        output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), output)

    def test_neq(self):
        node = HTMLNode("This is plain text", "asd", None, {"a": "asdi"})
        output = ' a="asi"'
        self.assertNotEqual(node.props_to_html(), output)

    def test_url(self):
        node = HTMLNode("This has a url", "asiodh", None, None)
        output = ""
        self.assertEqual(node.props_to_html(), output)

    def test_leaf(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafa(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()