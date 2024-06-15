import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html1 = HTMLNode("a","Ceci est un lien",None,{"href": "https://www.google.com", "target": "_blank"})
        html2 = HTMLNode("h1","Ceci est un titre",None,None)

        # What output do you expect for html1's properties?
        expected_html1_props = ' href="https://www.google.com" target="_blank"'
        # And for html2's properties (which has none)?
        expected_html2_props = ''
        
        # How can you check if html1's props_to_html method works correctly?
        self.assertEqual(html1.props_to_html(), expected_html1_props)
        # And html2's?
        self.assertEqual(html2.props_to_html(), expected_html2_props)

if __name__ == "__main__":
    unittest.main()