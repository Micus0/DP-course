class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"


class PersonFactory:
    def __init__(self):
        self.id = -1

    def create_person(self, name):
        self.id += 1
        return Person(self.id, name)


pf = PersonFactory()
p1 = pf.create_person("Chri")
p2 = pf.create_person("Teo")

print(p1)
print(p2)
