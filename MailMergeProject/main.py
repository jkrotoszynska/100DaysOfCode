PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as schema:
    schema = schema.read()
    for name in names:
        name = name.strip()
        official_letter = schema.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as letter:
            letter.write(official_letter)
