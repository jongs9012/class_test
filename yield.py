import random

class Person:
    num_of_people = 0
    def __init__(self, name, id_num, address):
        Person.num_of_people += 1
        self.name = str(name)
        self.id_num = str(id_num)
        self.address = str(address)

    def show_info(self):
        return self.name, self.id_num, self.address

    def show_name(self):
        return self.name
    
    def change_name(self, new_name):
        self.name = str(new_name)
    
    def show_age(self, curr_year):
        return curr_year[2:] - self.id_num[0:1]
    
    def male_or_female(self):
        if self.id_num[7] == "1" or self.id_num[7] == "3":
            return "male"
        else:
            return "female"
    
    def show_address(self):
        return self.address
    
    def change_add(self, new_add):
        self.address = new_add

    def population():
        return Person.num_of_people


# def info_generator():
#     num = "0123456789"
#     city = "Buhceon", "Incheon", 'Busan', "Seoul"
#     result = ""
#     for i in range(6):
#         result += str(random.choice(num))
#     result += "-"
#     result += str(random.randint(1, 4))
#     for i in range(5):
#         result += random.choice(num)
#     user_city = random.choice(city)
#     return f"TestPerson", result, user_city

# population = 2
# people = []

# for i in range(0, population):
#     name, result, city = info_generator()
#     people.append(Person(name + str(i + 1), result, city))


# for i in range(0, len(people)):
#     print(people[i].show_info())
# print(Person.num_of_people)

# total_male = 0
# total_female = 0
# for i in range(0, len(people)):
#     if people[i].male_or_female() == "male":
#         total_male += 1
#     else:
#         total_female += 1
# print(f"Male : {total_male} \nFemale : {total_female}")


s = "Hello world"
it_ = iter(s)
print(next(it_))
print(next(it_))
print(next(it_))
print()

def yield_test():
    print("Hello")
    yield 1
    print("World")
    yield 2

gene = yield_test()
print(next(gene))
print(next(gene))
