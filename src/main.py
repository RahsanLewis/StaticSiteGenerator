from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    testlist = []
    testdict = {}
    text_node_object = TextNode("hi", TextType.BOLD, "www.test.com")
    html_node_object = HTMLNode("<p>", "para", testlist, testdict)
    print(html_node_object)
main()