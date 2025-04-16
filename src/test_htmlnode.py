import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode("<p>", "para")
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html(self):
        node = HTMLNode("<p>", "para", props={"<a>": "test.com"})
        self.assertEqual(node.props_to_html(), ' <a>="test.com"')
        
    def test_props_to_html_multiple(self):
        node = HTMLNode("<a>", "link", props={"href": "test.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="test.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()