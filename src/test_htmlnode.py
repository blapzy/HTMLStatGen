import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()