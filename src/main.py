from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    testlist = []
    testdict = {}
    text_node_object = TextNode("hi", TextType.BOLD, "www.test.com")
    html_node_object = HTMLNode("<p>", "para", testlist, testdict)
    leaf_node_object = LeafNode(tag="p", value="this is text", props={"href": "test.com", "target": "_blank"})
    print(text_node_object.text_type)
main()