from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        node_list = []
        if node.text_type != TextType.TEXT:
            node_list.append(node)
        else:
            if delimiter in node.text:
                split_text = node.text.split(delimiter)
                if len(split_text) % 2 == 0:
                    raise exception('opening delimiter must have matching closing delimiter')
                for i in range(0,len(split_text)):
                    if i % 2 == 0:
                        node_list.append(TextNode(split_text[i], TextType.TEXT))
                    else:
                        node_list.append(TextNode(split_text[i],text_type))
            else:
                node_list.append(node)
        new_nodes.extend(node_list)
    return new_nodes