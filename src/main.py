from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from texttohtml import text_node_to_html_node
from splitnodes import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("Hello **world** how **are** you", TextType.TEXT)
    nodes = [node, node2]
    new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)   
    print(new_nodes)
main()