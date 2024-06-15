import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode




class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html1 = HTMLNode("Ceci est un lien","a",None,{"href": "https://www.google.com", "target": "_blank"})
        html2 = HTMLNode("Ceci est un titre","h1",None,None)

        # What output do you expect for html1's properties?
        expected_html1_props = ' href="https://www.google.com" target="_blank"'
        # And for html2's properties (which has none)?
        expected_html2_props = ''
        
        # How can you check if html1's props_to_html method works correctly?
        self.assertEqual(html1.props_to_html(), expected_html1_props)
        # And html2's?
        self.assertEqual(html2.props_to_html(), expected_html2_props)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf1 = LeafNode("Ceci est un lien","a",{"href": "https://www.google.com", "target": "_blank"})
        leaf2 = LeafNode("Ceci est un paragraphe","p")
        leaf3 = LeafNode("Ceci n'est pas une balise")

        expected_leaf1 = '<a href="https://www.google.com" target="_blank">Ceci est un lien</a>'
        expected_leaf2 = '<p>Ceci est un paragraphe</p>'
        expected_leaf3 = 'Ceci n\'est pas une balise'

        self.assertEqual(leaf1.to_html(), expected_leaf1)
        self.assertEqual(leaf2.to_html(), expected_leaf2)
        self.assertEqual(leaf3.to_html(), expected_leaf3)



if __name__ == "__main__":
    unittest.main()