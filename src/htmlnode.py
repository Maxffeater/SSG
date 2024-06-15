class HTMLNode:
    def __init__(self, value=None, tag=None, children=None, props=None):
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
    

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(value=value, tag=tag, props=props, children=[])

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        elif self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'