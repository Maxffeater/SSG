from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(text_node)

    html_node = HTMLNode("a","Ceci est un lien",None,'{"href": "https://www.google.com", "target": "_blank"}')
    print(html_node)

if __name__ == "__main__":
    main()