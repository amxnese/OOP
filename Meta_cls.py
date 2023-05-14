class Meta(type):
    def __new__(self,class_name,bases,attrs):
        print(attrs)
        modified_attrs = {}
        for name,val in attrs.items():
            if name.startswith("__"):
                modified_attrs[name] = val
            else:
                if isinstance(val,int):
                    modified_attrs[name] = val*2
                elif isinstance(val,str):
                    modified_attrs[name] = val.upper()
        return type(class_name,bases,modified_attrs)
class rand(metaclass=Meta):
    num1 = 4
    num2 = 8
    name = "amine"
print(rand.num1,rand.num2,rand.name)