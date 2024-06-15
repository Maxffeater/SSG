class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attr_string = ''
        for key,value in self.props.items():
            attr_string += f' {key}="{value}"'
        return attr_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"