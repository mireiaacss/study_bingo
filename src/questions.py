import csv

def give_answers(csv_path):
    "Return a list with all the answers (second column) from the CSV."
    answers = []
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # skip header if there is one
        for row in reader:
            if len(row) >= 2:
                answers.append(row[1].strip())
    return answers

def give_questions (csv_path):
    "Return a list with all the questions (first column) from the CSV."
    questions = []
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # skip header if there is one
        for row in reader:
            if len(row) >= 1:
                questions.append(row[0].strip())
    return questions


