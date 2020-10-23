class Meta(type):
    def __new__(self, class_name, bases, attributes):
        print(attributes)
        new_attr = dict()
        for attr_name, attr_value in attributes.items():
            if attr_name.startswith('__'):
                new_attr[attr_name] = attr_value
            else:
                new_attr[attr_name.upper()] = attr_value
        print(new_attr)
        return type(class_name, bases, new_attr)


class Pet(metaclass=Meta):

    pet_category = ['Cat', 'Dog', 'Snake', 'Sloth', 'Pig', 'Hippo', 'Elephant']

    def __init__(self, name, age, category):
        self.name = name
        self.age = age
        self.category = category

    def language(self):
        if self.category == 'Cat':
            print('Meow')
        elif self.category == 'Dog':
            print('Bark')
        elif self.category == 'Snake':
            print('Cici')
        elif self.category == 'Sloth':
            print('Hacihaci')
        else:
            print('Unkown')

    def __repr__(self):
        return 'Pet({},{},{})'.format(self.name, self.age, self.category)


my_pet = Pet('Dora', 3, 'Sloth')

# my_pet.LANGUAGE()