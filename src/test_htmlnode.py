import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType


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
        node = LeafNode(
            tag="p", value=None, props={"href": "test.com", "target": "_blank"}
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_tag_is_none(self):
        node = LeafNode(
            tag=None,
            value="this is text",
            props={"href": "test.com", "target": "_blank"},
        )
        self.assertEqual(node.to_html(), "this is text")

    def test_to_html(self):
        node = LeafNode(
            tag="p",
            value="this is text",
            props={"href": "test.com", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(), '<p href="test.com" target="_blank">this is text</p>'
        )


class TestParentNode(unittest.TestCase):
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

    def test_to_html_tag_is_none(self):
        child_node = LeafNode("b", "child")
        node = ParentNode(tag=None, children=[child_node])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_children_is_none(self):
        node = ParentNode(tag="div", children=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_props(self):
        child_node = LeafNode("b", "child")
        node = ParentNode(
            tag="div",
            children=[child_node],
            props={"href": "test.com", "target": "_blank"},
        )
        self.assertEqual(
            node.to_html(),
            '<div href="test.com" target="_blank"><b>child</b></div>',
        )

    def test_multiple_children(self):
        child1 = LeafNode("b", "bold")
        child2 = LeafNode("i", "italic")
        parent = ParentNode("p", [child1, child2])
        self.assertEqual(parent.to_html(), "<p><b>bold</b><i>italic</i></p>")

    def test_empty_props(self):
        child = LeafNode("span", "text")
        parent = ParentNode("div", [child], props={})
        self.assertEqual(parent.to_html(), "<div><span>text</span></div>")

    def test_grandchildren_siblings(self):
        grand1 = LeafNode("b", "one")
        grand2 = LeafNode("i", "two")
        child = ParentNode("span", [grand1, grand2])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(), "<div><span><b>one</b><i>two</i></span></div>"
        )


class TestTextToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is Bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        
    def test_italic(self):
        node = TextNode("This is Italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")

    def test_code(self):
        node = TextNode("This is Code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
    
    def test_link(self):
        node = TextNode("This is a Link", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode("This is an Image", TextType.IMAGE, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://example.com", "alt": "This is an Image"})
    
    def test_exception(self):
        node = TextNode("This is wrong", None, "https://example.com")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
    
    
    
    
if __name__ == "__main__":
    unittest.main()
