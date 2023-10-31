from abc import ABC, abstractmethod
from typing import Union


class Dance:
    def __init__(self, genre, head, hands, body, legs):
        self.genre = genre
        self.head = head
        self.hands = hands
        self.body = body
        self.legs = legs


class DanceAction(ABC):
    @abstractmethod
    def dance(self, obj: Dance) -> None:
        pass


class Drink(ABC):
    @abstractmethod
    def drink(self, what) -> None:
        pass


class Person(DanceAction, Drink):
    def __init__(self, name: str, gender: str, age: int, can_dance: Union[set, None]):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__can_dance = can_dance

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str) -> None:
        self.__gender = gender

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age

    @property
    def can_dance(self) -> Union[set, None]:
        return self.__can_dance

    @can_dance.setter
    def can_dance(self, can_dance: Union[set, None]):
        self.__can_dance = can_dance

    def dance(self, obj: Dance) -> None:
        print(f'{self.__name} танцует {obj.genre} вот так: {obj.head}, {obj.hands}, {obj.body}, {obj.legs}')

    def drink(self, what='Vodka') -> None:
        print(f'{self.name} пьет напиток: {what}')


class Club:

    def __init__(self, club_name: str):
        self.club_name = club_name
        self.__persons = []
        print(f'Клуб {self.club_name} создан. Кол-во людей в клубе: {len(self.__persons)} ')

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, person: Union[Person, None]):
        if person:
            self.__persons.append(person)
            print(f'Кол-во людей в клубе: {len(self.__persons)} ')


if __name__ == '__main__':

    DANCE_RNB = Dance(genre='rnb', head='головой вперед-назад', hands='руки согнуты в локтях',
                      body='покачивает телом вперед и назад', legs='ноги в полу-присяде')
    DANCE_ELECTRO = Dance(genre='electro', head='почти нет движения головой', hands='круговые движения вращения руками',
                          body='покачивание туловищем вперед-назад', legs='ноги двигаются в ритме')
    DANCE_POP = Dance(genre='pop', head='плавное движение головой', hands='плавное движение рукой',
                      body='плавное движение туловищем', legs='плавное движение ногой')
    DANCES_TYPES = {1: DANCE_RNB, 2: DANCE_ELECTRO, 3: DANCE_POP}

    humans = {
        0: dict(name='Маша', gender='женщина', age=20, can_dance={'electro', 'rnb'}),
        1: dict(name='Вася', gender='мужчина', age=21, can_dance={'electro'}),
        2: dict(name='Петя', gender='мужчина', age=22, can_dance=None),
        3: dict(name='Надя', gender='женщина', age=23, can_dance={'pop', 'electro'}),
    }
    try:
        club = Club('BASH')
        for _, bio in humans.items():
            person = Person(name=bio['name'], gender=bio['gender'], age=bio['age'], can_dance=bio['can_dance'])
            print(f'Человек {person.name} зашел в клуб.', end=' ')
            if person.can_dance:
                print(f'Он умеет танцевать под {", ".join(person.can_dance)}')
            else:
                print(f'Он не умеет танцевать')
            club.persons = person

        print(f'Сегодня на танцполе будет звучать следующий плейлист:')
        for song, genre in DANCES_TYPES.items():
            print(f'\tНазвание песни: {song} - Жанр песни: {genre.genre}')

        print('Да начнется вечеринка!')
        for song, genre in DANCES_TYPES.items():
            print(f'\tИграет трек номер {song}, стиль {genre.genre}')
            for person in club.persons:
                if person.can_dance and genre.genre in person.can_dance:
                    person.dance(genre)
                else:
                    person.drink()
    except Exception as msg:
        print(msg)
