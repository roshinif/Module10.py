
# Phase 1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top_floor:
            print(f"Elevator is moving from {self.current} to {self.current + 1}")
            self.current += 1
            return True
        else:
            print("Elevator is already at the top floor.")
            return False

    def floor_down(self):
        if self.current > self.bottom_floor:
            print(f"Elevator is moving from {self.current} to {self.current - 1}")
            self.current -= 1
            return True
        else:
            print("Elevator is already at the bottom floor.")
            return False

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print(f"Error: Floor {floor} is out of range.")
            return

        if floor > self.current:
            for _ in range(floor - self.current):
                if not self.floor_up():
                    break
        elif floor < self.current:
            for _ in range(self.current - floor):
                if not self.floor_down():
                    break
        else:
            print(f"Elevator is already at the required floor {self.current}.")


Kara_ele = Elevator(1, 7)
target_floor = int(input("Which floor do you want to go to? "))
Kara_ele.go_to_floor(target_floor)
Kara_ele.go_to_floor(1)


# Phase 2

class Building:
    def __init__(self, bottom, top, elevators):
        self.elevators = []
        for _ in range(elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, floor):
        if elevator_num < 1 or elevator_num > len(self.elevators):
            print(f"Error: Elevator number {elevator_num} is out of range.")
            return
        print(f"Elevator {elevator_num} is moving to floor {floor}.")
        self.elevators[elevator_num - 1].go_to_floor(floor)

    def fire_alarm(self):
        print("Fire alarm is ringing! Returning all elevators to the bottom floor.")
        for e in self.elevators:
            e.go_to_floor(e.bottom_floor)


print("\nElevator in the building: ")
building1 = Building(1, 7, 3)
building1.run_elevator(1, 4)  # Run elevator 1 to the bottom floor (1)
building1.run_elevator(2, 2)  # Run elevator 1 to the bottom floor (1)
building1.run_elevator(3, 7)  # Run elevator 1 to the bottom floor (1)
building1.fire_alarm()


# Phase 4

import random
import time


class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance_traveled = 0

    def drive(self):
        self.distance_traveled += self.speed

    def change_speed(self):
        change = random.randint(-20, 20)
        self.speed = max(0, self.speed + change)

    def __str__(self):
        return f"{self.name:<20} | {self.speed:<10} | {self.distance_traveled:<15}"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.change_speed()
            car.drive()

    def print_status(self):
        print(f"\n{'Car Name':<20} | {'Speed (km/h)':<10} | {'Distance Traveled (km)':<15}")
        print("-" * 55)
        for car in self.cars:
            print(car)

    def race_finished(self):
        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False


def main():

    cars = [Car(f"Car {i + 1}") for i in range(10)]


    race = Race(name="Grand Demolition Derby", distance=8000, cars=cars)


    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1


        if hours_passed % 10 == 0:
            race.print_status()


    race.print_status()
    print(f"\nThe race is finished after {hours_passed} hours!")


if __name__ == "__main__":
    main()
