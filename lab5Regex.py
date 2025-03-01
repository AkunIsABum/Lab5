import re

row = open("text.txt", encoding="UTF-8")
text = row.read()

def task1(text):
    return re.findall(r'ab*', text)

#print(task1(text))

def task2(text):
    return re.findall(r'ab{2,3}', text)

#print(task2(text))

def task3(text):
    return re.findall(r'[a-z]+_[a-z]+', text) 

#print(task3(text))

def task4(text):
    return re.findall(r'[a-z][A-Z]', text)

#print(task4(text))

def task5(text):
    return re.findall(r'^a.*b$', text)

#print(task5(text))

def task6(text):
    return re.sub(r'[ ,.]', ":", text)

#print(task6(text))

def task7(text):
    camel_case_str = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)
    return camel_case_str

#print(task7(text))

def task8(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

#print(task8("ASF njafk bKAb Fa BFN,ASDF JNA knmdn  fNfM  n"))
    
def task9(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)


def task10(text):
    snake_case_str = re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()
    return snake_case_str
