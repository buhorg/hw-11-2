import json


def get_candidates_list(filename):
    """
    Подключаем из json файла данные в виде списка словарей
    """
    with open(filename, encoding='utf-8') as file:
       candidates_list = json.load(file)
    return candidates_list


def get_person_by_id(my_id, candidate_list):
    """
    Проверка на удовлетворение экземпляра класса совпадению на id и распечатка
    """
    for person in candidate_list:
        if person['id'] == my_id:
            return person
    return False


def get_persons_by_name(name, candidate_list):
    """
    Проверка на вхождение name в имя кандидата
    """
    candidates = []
    for person in candidate_list:
        if person['name'].lower().count(name.lower()):
            candidates.append(person)
    return candidates


def get_persons_by_skill(skill, candidate_list):
    """
    Проверка на совпадение skill
    """
    candidates = []
    for person in candidate_list:
        skills_list = person["skills"].lower().split(", ")
        for num in skills_list:
            if num == skill.lower():
                candidates.append(person)
                break
    return candidates
