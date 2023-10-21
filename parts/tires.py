# should be initialised with an array of 4 numbers

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from serviceable import Serviceable

class CarriganTires(Serviceable):
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return (any(num >= 0.9 for num in self.tire_wear))
    
class OctoprimeTires(Serviceable):
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return (sum(self.tire_wear) >= 3)