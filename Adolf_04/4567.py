import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Pet:
    pet_list = {
        'Kot Vasiliy': {'fat': 10},
        'Pes Bobik': {'fat': 15},
        'Bober Vitalik': {'fat': 8},
        'Mladshiy brat Obezjana': {'fat': 100},
    }

    def __init__(self):
        self.pet = random.choice(list(Pet.pet_list))
        self.fat = Pet.pet_list[self.pet]['fat']
        logging.info(f"New pet created: {self.pet}")

    def walk(self):
        if self.fat >= 5:
            logging.info('Walking...')
            self.fat -= 0.5
            return True
        else:
            logging.info('Your pet is too thin, it needs more food!')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        logging.info("New house created")


class Auto:
    car_list = {
        'BMW': {'fuel': 100, 'durability': 100, 'consumption': 6},
        'ZAZ': {'fuel': 50, 'durability': 40, 'consumption': 10},
        'Volvo': {'fuel': 70, 'durability': 150, 'consumption': 8},
        'Ferrari': {'fuel': 80, 'durability': 120, 'consumption': 14},
    }

    def __init__(self):
        self.brand = random.choice(list(Auto.car_list))
        self.fuel = Auto.car_list[self.brand]['fuel']
        self.durability = Auto.car_list[self.brand]['durability']
        self.consumption = Auto.car_list[self.brand]['consumption']
        logging.info(f"New car created: {self.brand}")

    def drive(self):
        if self.durability > 0 and self.fuel >= self.consumption:
            logging.info('Driving...')
            self.fuel -= self.consumption
            self.durability -= 1
            return True
        else:
            logging.info('This car cannot go!')
            return False


class Job:
    job_list = {
        'Python developer': {'salary': 40, 'sadness': 3},
        'Java developer': {'salary': 50, 'sadness': 10},
        'C++ developer': {'salary': 45, 'sadness': 25},
        'Rust developer': {'salary': 70, 'sadness': 1},
    }

    def __init__(self):
        self.job_title = random.choice(list(Job.job_list))
        self.salary = Job.job_list[self.job_title]['salary']
        self.sadness = Job.job_list[self.job_title]['sadness']
        logging.info(f"New job created: {self.job_title}")


class Human:
    def __init__(
        self,
        pet=None,
        name='Human',
        job=None,
        home=None,
        car=None
    ):
        self.pet = pet
        self.name = name
        self.money = 100
        self.happiness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        logging.info(f"New human created: {self.name}")

    def get_pet(self):
        self.pet = Pet()

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto()

    def to_walk(self):
        if self.pet.walk():
            self.walk()
        else:
            self.to_feed()

    def get_job(self):
        if self.car.drive():
            self.job = Job()
        else:
            self.to_repair()

    def to_feed(self):
        self.pet.fat += 1
        self.money -= 10
        logging.info(f"Feeding the pet. Fat: {self.pet.fat}")

    def to_repair(self):
        self.car.durability += 100
        self.money -= 50
        logging.info(f"Repairing the car. Durability: {self.car.durability}")

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
            else:
                self.satiety += 5
                self.home.food -= 5

    def shopping(self, goal):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < self.car.consumption:
                goal = 'fuel'
            else:
                self.to_repair()
                return
        if goal == 'fuel':
            logging.info('Buying fuel...')
            self.money -= 100
            self.car.fuel += 100
        elif goal == 'food':
            logging.info('Buying food...')
            self.money -= 50
            self.home.food += 50
        elif goal == 'sweets':
            logging.info('Buying sweets!!!')
            self.money -= 15
            self.satiety += 2
            self.happiness += 10

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < self.car.consumption:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.happiness -= self.job.sadness
        self.satiety -= 4

    def chill(self):
        self.happiness += 10
        self.home.mess += 5

    def clean_home(self):
        self.happiness -= 5
        self.home.mess = 0

    def status(self, day):
        day_str = f'Today is the {day} day of {self.name}\'s life'
        logging.info(f"{day_str:=^50}")
        human_info = f'{self.name}\'s info'
        logging.info(f"{human_info:^50}")
        logging.info(f'money: {self.money}')
        logging.info(f'satiety: {self.satiety}')
        logging.info(f'happiness: {self.happiness}')
        home_info = 'Home info'
        logging.info(f"{home_info:^50}")
        logging.info(f'mess: {self.home.mess}')
        logging.info(f'food: {self.home.food}')
        car_info = f'{self.car.brand} car info'
        logging.info(f"{car_info:^50}")
        logging.info(f'fuel: {self.car.fuel}')
        logging.info(f'durability: {self.car.durability}')

    def is_alive(self):
        if self.happiness < 0:
            logging.info('Depression...')
            return False
        elif self.satiety < 0:
            logging.info('Dead...')
            return False
        elif self.money < -500:
            logging.info('Bankrupt')
            return False
        else:
            return
