import unittest
from htmlnode import HTMLNode, LeafNode

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
        
class TestLeafNode(unittest.TestCase):
    def test_to_html_value_is_none(self):
        node = LeafNode(tag="p", value=None, props={"href": "test.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_to_html_tag_is_none(self):
        node = LeafNode(tag=None, value="this is text", props={"href": "test.com", "target": "_blank"})
        self.assertEqual(node.to_html(), "this is text")
    
    def test_to_html(self):
        node = LeafNode(tag="p", value="this is text", props={"href": "test.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<p href="test.com" target="_blank">this is text</p>')
        

if __name__ == "__main__":
    unittest.main()