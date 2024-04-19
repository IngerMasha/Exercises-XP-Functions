import random


def display_message():
    print("Hi everyone. On this course we learning python.")
def favorite_book(title):
    print(f"One of my favorite books is {title}")
def describe_city(city, country="Israel"):
    print(f"{city} is in the {country}")
def random_gess(my_number):
    number = random.randint(1, 100)
    print(f" {number} = {my_number} success! " if number==my_number else f"{my_number} != {number} Fail!")
def make_shirt(size = "large", text="I love Python"):
    print(f" The size of the shirt is {size} and the text is {text}")
def make_great(list):
    new_list = []
    for name in list:
        new_list.append("the Great "+name)
    return new_list
def show_magicians(list_magicians):
    for name in list_magicians:
        print(name)
def main():
    display_message()
    title = input("Enter your favorite book: ")
    favorite_book(title)
    city = input("Enter city: ")
    country = input("Enter country: ")
    describe_city(city.capitalize(), country.capitalize())
    describe_city("Ashdod")
    my_number = int(input("Enter number between 1 and 100:  "))
    random_gess(my_number)
    make_shirt()
    make_shirt("medium")
    make_shirt(size="small", text="Cat's cute!")
    magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    show_magicians(magician_names)
    magician_names = make_great(magician_names)
    show_magicians(magician_names)

if __name__ == "__main__":
    main()
