with open("./input/names/invited_names.txt") as nameFile:
    names = nameFile.readlines()


with open("./input/letters/starting_letter.txt") as file:
    letter = file.read()
    for item in names:
        strippedName = item.strip()
        updatedLetter = letter.replace("[name]", strippedName)
        with open(f"./output/readytosend/letter_for_{strippedName}", mode="w") as completedLetter:
            completedLetter.write(updatedLetter)
            