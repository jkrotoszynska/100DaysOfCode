try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["new_key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
    
except KeyError as error_message:
    print(f"The key {error_message} does not exist")