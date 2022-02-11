DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

#Crear las listas all_python_devs y all_Platzi_workers utilizando una
#combinación de filter y map.
#Crear la lista old_people y adults con list comprehension
def run():
    all_python_devs = list(filter(lambda worker: worker["language"] =="python", DATA ))
    for worker in all_python_devs:
          print(worker)
    
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs ))
    for worker in all_python_devs:
          print(worker)    

    all_Platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_Platzi_workers = list(map(lambda worker: worker["name"], all_Platzi_workers))
    for worker in all_Platzi_workers:
          print(worker)      
    
    #all_Platzi_workers = list

    adult = [worker["name"] for worker in DATA if worker ["age"] > 18]
    for worker in adult:
        print(worker)
    old_people = [worker["name"] for worker in DATA if worker["age"] > 70] 
    for worker in old_people:
        print(worker)   


if __name__ == '__main__':
    run()