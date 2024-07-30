class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"self.{self.name} = {self.value}"


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = [f"class {self.name}:"]
        if not self.fields:
            lines.append("  pass")
        else:
            lines.append("  def __init__(self):")
            for f in self.fields:
                lines.append(f"    {f.__str__()}")
        return "\n".join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, name, value):
        self.__class.fields.append(Field(name, value))
        return self

    def __str__(self):
        return self.__class.__str__()


cb = CodeBuilder('Person').add_field('name', '""') \
    .add_field('age', '0')
print(cb)
