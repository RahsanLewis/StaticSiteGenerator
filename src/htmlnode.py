class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_list = []
        if self.props is None:
            return ""
        for key in self.props:
            text = key.replace('"', "")
            props_list.append(f' {text}="{self.props[key]}"')
        return "".join(props_list)
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r} props={self.props!r})"