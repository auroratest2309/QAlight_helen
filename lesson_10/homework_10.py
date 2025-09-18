"""
Шаблони класів об'єктів природи та побуту (ЗАГОТОВКИ)
Template classes for nature and household objects (TEMPLATES)

ІНСТРУКЦІЯ / INSTRUCTION:
Реалізуйте всі методи та властивості згідно з вимогами в коментарях
Implement all methods and properties according to requirements in comments
"""

import math


class Tree:
    """
    Клас природного об'єкта "Дерево"
    Class for natural object "Tree"
    
    Атрибути / Attributes:
    - height: висота дерева (0 < height < 150 метрів)
    - trunk_diameter: діаметр стовбура (0 < diameter < 1000 см)
    - leaf_count: кількість листя (обчислюється автоматично)
    """
    
    def __init__(self, height, trunk_diameter):
        self._height = None
        self._trunk_diameter = None
        self._leaf_count = 0

        self.height = height
        self.trunk_diameter = trunk_diameter
        self._leaf_count = self._calculate_leaf_count()
        """
        Ініціалізація дерева / Initialize tree
        
        Args:
            height (float): Висота дерева в метрах / Tree height in meters
            trunk_diameter (float): Діаметр стовбура в см / Trunk diameter in cm
        
        TODO: 
        - Встановити атрибути через властивості для валідації
        - Обчислити початкову кількість листя
        """
     
    
    @property
    def height(self):
        return self._height
        """
        Властивість: висота дерева / Property: tree height
        
        TODO: Повернути значення приватного атрибута _height
        """
        
    
    @height.setter
    def height(self, value):
        if not (0 < value < 150):
            raise ValueError ("Висота дерева повинна бути між 0 і 150 м")
        self._height = value
        self._leaf_count = self._calculate_leaf_count()

        """
        Сетер для висоти дерева / Setter for tree height
        
        TODO: 
        - Перевірити що 0 < value < 150
        - Встановити _height = value
        - Перерахувати кількість листя
        - Викинути ValueError при неправильному значенні
        """
        
    
    @property
    def trunk_diameter(self):
       return self._trunk_diameter
    """
        Властивість: діаметр стовбура / Property: trunk diameter
        
        TODO: Повернути значення приватного атрибута _trunk_diameter
        """
   
    
    @trunk_diameter.setter
    def trunk_diameter(self, value):
        if not (0 < value < 1000):
            raise ValueError ("Діаметр стовбура повинен бути між 0 і 1000 см")
        self._trunk_diameter = value
        self._leaf_count = self._calculate_leaf_count()

        """
        Сетер для діаметра стовбура / Setter for trunk diameter
        
        TODO:
        - Перевірити що 0 < value < 1000
        - Встановити _trunk_diameter = value
        - Перерахувати кількість листя
        - Викинути ValueError при неправильному значенні
        """
      
    
    @property
    def leaf_count(self):
        return self._leaf_count
        """
        Властивість: кількість листя (тільки читання) / Property: leaf count (read-only)
        
        TODO: Повернути значення _leaf_count
        """
      
    
    def _calculate_leaf_count(self):
        if self._height is None or self._trunk_diameter is None:
            return 0
        return int(self._height * self._trunk_diameter * 100)
        """
        Приватний метод: обчислення кількості листя / Private method: calculate leaf count
        
        Формула: height * trunk_diameter * 100
        
        TODO: 
        - Обчислити кількість листя за формулою
        - Повернути результат
        """
       
    
    def grow(self):
        self.height = min(self.height + 0.5, 149.9)
        self.trunk_diameter = min(self.trunk_diameter + 2, 999.9)
        self._leaf_count = self._calculate_leaf_count()
        print(f"Дерево виросло: тепер висота {self.height} м, діаметр {self.trunk_diameter} см")
        """
        Метод: ріст дерева / Method: tree growth
        
        TODO:
        - Збільшити висоту на 0.5 м (але не більше 149.9)
        - Збільшити діаметр стовбура на 2 см (але не більше 999.9)
        - Використовувати властивості для автоматичного перерахунку листя
        - Вивести повідомлення про ріст
        """
        
    
    def leaf_fall(self):
        self._leaf_count = int(self.leaf_count * 0.7)
        print(f"Листя опало: тепер приблизно {self.leaf_count} листків")
        """
        Метод: опадання листя / Method: leaf fall
        
        TODO:
        - Зменшити кількість листя на 30% (помножити на 0.7)
        - Вивести повідомлення про опадання
        """
      
    
    def get_info(self):
        return (f"Дерево: висота = {self.height} м, "
                f"діаметр = {self.trunk_diameter} см, "
                f"кількість листя = {self.leaf_count}")
        """
        Метод: отримати інформацію про дерево / Method: get tree information
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити висоту, діаметр стовбура, кількість листя
        """
  


class Kettle:
    """
    Клас побутового об'єкта "Чайник"
    Class for household object "Kettle"
    
    Атрибути / Attributes:
    - volume: максимальний об'єм (0.5 <= volume <= 5 літрів)
    - current_volume: поточний об'єм води (0 <= current <= volume)
    - water_temperature: температура води (за замовчуванням 20°C)
    - is_on: чи включений чайник (за замовчуванням False)
    """
    
    def __init__(self, volume):
        self._volume = None
        self._current_volume = 0
        self._water_temperature = 20
        self._is_on = False
        
        # Встановлюємо максимальний об'єм через властивість (з валідацією)
        self.volume = volume
        """
        Ініціалізація чайника / Initialize kettle
        
        Args:
            volume (float): Максимальний об'єм в літрах / Maximum volume in liters
        
        TODO:
        - Встановити volume через властивість
        - Ініціалізувати current_volume = 0
        - Ініціалізувати water_temperature = 20
        - Ініціалізувати is_on = False
        """
     
    
    @property
    def volume(self):
        return self._volume
    
        """
        Властивість: максимальний об'єм / Property: maximum volume
        
        TODO: Повернути _volume
        """
      
    
    @volume.setter
    def volume(self, value):
        if not (0.5 <= value <= 5):
            raise ValueError("Об'єм чайника повинен бути між 0.5 та 5 літрів")
        self._volume = value

        """
        Сетер для максимального об'єму / Setter for maximum volume
        
        TODO:
        - Перевірити що 0.5 <= value <= 5
        - Встановити _volume = value
        - Викинути ValueError при неправильному значенні
        """
       
    
    @property
    def current_volume(self):
        return self._current_volume
        """
        Властивість: поточний об'єм води / Property: current water volume
        
        TODO: Повернути _current_volume
        """
 
    
    @property
    def water_temperature(self):
        return self._water_temperature
    
        """
        Властивість: температура води / Property: water temperature
        
        TODO: Повернути _water_temperature
        """
   
    
    @property
    def is_on(self):
        return self._is_on
        """
        Властивість: стан чайника / Property: kettle state
        
        TODO: Повернути _is_on
        """
      
    
    def pour_water(self, amount):
        if amount < 0:
            raise ValueError("Кількість води для додавання повинна бути >= 0")
        available_space = self.volume - self._current_volume
        if amount > available_space:
            self._current_volume = self.volume
            print(f"Чайник переповнений! Додано лише {available_space} л води")
        else:
            self._current_volume += amount
            print(f"Додано {amount} л води. Поточний об'єм: {self._current_volume} л")

        """

        Метод: налити воду / Method: pour water
        
        Args:
            amount (float): Кількість води для додавання / Amount of water to add
        
        TODO:
        - Перевірити що amount >= 0
        - Обчислити скільки води можна додати (не більше ніж volume)
        - Додати воду до current_volume
        - Вивести повідомлення про додавання
        - Повідомити якщо чайник переповнений
        """
   
    
    def drain_water(self, amount):
        if amount < 0:
            raise ValueError("Кількість води для зливання повинна бути >= 0")
        
        drained = min(amount, self._current_volume)
        self._current_volume -= drained
        print(f"Злито {drained} л води. Поточний об'єм: {self._current_volume} л")
        
        """
        Метод: злити воду / Method: drain water
        
        Args:
            amount (float): Кількість води для зливання / Amount of water to drain
        
        TODO:
        - Перевірити що amount >= 0
        - Зменшити current_volume (але не менше 0)
        - Вивести повідомлення про зливання
        """
    
    
    def turn_on(self):
        if self._current_volume <= 0:
            print("Чайник порожній! Не можна включити.")
            return
        self._is_on = True
        self._water_temperature = 100
        print(f"Чайник увімкнено. Температура води: {self._water_temperature}°C")

        """
        Метод: включити чайник / Method: turn on kettle
        
        TODO:
        - Перевірити що в чайнику є вода (current_volume > 0)
        - Встановити is_on = True
        - Встановити water_temperature = 100
        - Вивести повідомлення про включення
        - Якщо води немає - вивести попередження
        """
  
    
    def turn_off(self):
        self._is_on = False
        print("Чайник вимкнено.")

        """
        Метод: вимкнути чайник / Method: turn off kettle
        
        TODO:
        - Встановити is_on = False
        - Вивести повідомлення про вимкнення
        """
      
    
    def get_status(self):
        return (f"Чайник: об'єм = {self._current_volume}/{self._volume} л, "
                f"температура = {self._water_temperature}°C, "
                f"включений = {self._is_on}")
        """
        Метод: отримати статус чайника / Method: get kettle status
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити об'єм, температуру, стан включення
        """



class Cloud:
    """
    Клас природного об'єкта "Хмара"
    Class for natural object "Cloud"
    
    Атрибути / Attributes:
    - area: площа хмари (1 <= area <= 10000 км²)
    - altitude: висота над землею (0.5 <= altitude <= 15 км)
    - humidity_density: щільність вологи (0 <= humidity <= 30 г/м³)
    - rain_probability: ймовірність дощу (обчислюється автоматично)
    """
    
    def __init__(self, area, altitude, humidity_density):
        self._area = None
        self._altitude = None
        self._humidity_density = None
        self._rain_probability = 0

        self.area = area
        self.altitude = altitude
        self.humidity_density = humidity_density

        """
        Ініціалізація хмари / Initialize cloud
        
        Args:
            area (float): Площа хмари в км² / Cloud area in km²
            altitude (float): Висота над землею в км / Altitude above ground in km
            humidity_density (float): Щільність вологи в г/м³ / Humidity density in g/m³
        
        TODO:
        - Встановити всі атрибути через властивості
        - Обчислити початкову ймовірність дощу
        """

    
    @property
    def area(self):
        return self._area
        """
        Властивість: площа хмари / Property: cloud area
        
        TODO: Повернути _area
        """

    
    @area.setter
    def area(self, value):
        if not (1 <= value <= 10000):
            raise ValueError("Площа хмари повинна бути між 1 та 10000 км²")
        self._area = value
        """
        Сетер для площі хмари / Setter for cloud area
        
        TODO:
        - Перевірити що 1 <= value <= 10000
        - Встановити _area = value
        - Викинути ValueError при неправильному значенні
        """

    
    @property
    def altitude(self):
        return self._altitude
        """
        Властивість: висота / Property: altitude
        
        TODO: Повернути _altitude
        """

    
    @altitude.setter
    def altitude(self, value):
        if not (0.5 <= value <= 15):
            raise ValueError("Висота хмари повинна бути між 0.5 та 15 км")
        self._altitude = value
        """
        Сетер для висоти / Setter for altitude
        
        TODO:
        - Перевірити що 0.5 <= value <= 15
        - Встановити _altitude = value
        - Викинути ValueError при неправильному значенні
        """

    
    @property
    def humidity_density(self):
        return self._humidity_density
        """
        Властивість: щільність вологи / Property: humidity density
        
        TODO: Повернути _humidity_density
        """
 
    
    @humidity_density.setter
    def humidity_density(self, value):
        if not (0 <= value <= 30):
            raise ValueError("Щільність вологи повинна бути між 0 та 30 г/м³")
        self._humidity_density = value
        self._rain_probability = self._calculate_rain_probability()

        """
        Сетер для щільності вологи / Setter for humidity density
        
        TODO:
        - Перевірити що 0 <= value <= 30
        - Встановити _humidity_density = value
        - Перерахувати ймовірність дощу
        - Викинути ValueError при неправильному значенні
        """
    
    
    @property
    def rain_probability(self):
        return self._rain_probability
        """
        Властивість: ймовірність дощу (тільки читання) / Property: rain probability (read-only)
        
        TODO: Повернути _rain_probability
        """
   
    
    def _calculate_rain_probability(self):
        return min(self._humidity_density * 3, 100)
    
        """
        Приватний метод: обчислення ймовірності дощу / Private method: calculate rain probability
        
        Формула: min(humidity_density * 3, 100)
        
        TODO:
        - Обчислити ймовірність за формулою
        - Повернути результат
        """
  
    
    def accumulate_moisture(self, amount):
        if amount < 0:
            raise ValueError("Кількість вологи повинна бути >= 0")
        new_humidity = min(self._humidity_density + amount, 30)
        added = new_humidity - self._humidity_density
        self.humidity_density = new_humidity
        print(f"Накопичено {added} г/м³ вологи. Поточна щільність: {self._humidity_density} г/м³")

        """
        Метод: накопичити вологу / Method: accumulate moisture
        
        Args:
            amount (float): Кількість вологи для додавання / Amount of moisture to add
        
        TODO:
        - Перевірити що amount >= 0
        - Збільшити humidity_density на amount (але не більше 30)
        - Використати властивість для автоматичного перерахунку ймовірності
        - Вивести повідомлення про накопичення
        """
   
    
    def rain(self):
        if self.rain_probability > 70:
            self.humidity_density *= 0.5
            print(f"Йде дощ! Щільність вологи зменшилась до {self._humidity_density} г/м³")
            return True
        else:
            print(f"Дощу немає. Ймовірність: {self.rain_probability}%")
            return False
        """
        Метод: дощ / Method: rain
        
        TODO:
        - Перевірити чи rain_probability > 70
        - Якщо так: зменшити humidity_density на 50% і вивести повідомлення про дощ
        - Якщо ні: вивести повідомлення що дощу немає з поточною ймовірністю
        - Повернути True якщо йде дощ, False якщо ні
        """
    
    
    def move(self, new_altitude):
        self.altitude = new_altitude
        print(f"Хмара перемістилася на висоту {self.altitude} км")

        """
        Метод: рух хмари / Method: cloud movement
        
        Args:
            new_altitude (float): Нова висота / New altitude
        
        TODO:
        - Встановити нову висоту через властивість
        - Вивести повідомлення про переміщення
        """
   
    
    def get_forecast(self):
        return (f"Хмара: площа = {self.area} км², висота = {self.altitude} км, "
                f"щільність вологи = {self.humidity_density} г/м³, "
                f"ймовірність дощу = {self.rain_probability}%")
    
        """
        Метод: отримати прогноз / Method: get forecast
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити площу, висоту, щільність вологи, ймовірність дощу
        """
     


class Aquarium:
    """
    Клас побутового об'єкта "Акваріум"
    Class for household object "Aquarium"
    
    Атрибути / Attributes:
    - length, width, height: розміри (10 < розмір < 200 см)
    - water_level: рівень води (0 <= water_level <= height)
    - fish_count: кількість риб (максимум 1 риба на 5 літрів води)
    - temperature: температура води (18 <= temperature <= 30 °C)
    - water_volume: об'єм води (обчислюється автоматично)
    """
    
    def __init__(self, length, width, height, water_level=0, fish_count=0, temperature=24):
        self._length = None
        self._width = None
        self._height = None
        self._water_level = 0
        self._fish_count = 0
        self._temperature = 24

        self.length = length
        self.width = width
        self.height = height

        self.water_level = water_level
        self.fish_count = fish_count

        self.temperature = temperature

        """
        Ініціалізація акваріума / Initialize aquarium
        
        Args:
            length (float): Довжина в см / Length in cm
            width (float): Ширина в см / Width in cm
            height (float): Висота в см / Height in cm
            water_level (float): Рівень води в см / Water level in cm
            fish_count (int): Кількість риб / Fish count
            temperature (float): Температура води в °C / Water temperature in °C
        
        TODO:
        - Встановити всі атрибути через властивості для валідації
        - Порядок важливий: спочатку розміри, потім water_level, потім fish_count
        """

    
    @property
    def length(self):
        return self._length
        
        """
        Властивість: довжина / Property: length
        
        TODO: Повернути _length
        """

    
    @length.setter
    def length(self, value):
        if not (10 < value < 200):
            raise ValueError("Довжина акваріума повинна бути між 10 та 200 см")
        self._length = value

        """
        Сетер для довжини / Setter for length
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _length = value
        - Викинути ValueError при неправильному значенні
        """

    
    @property
    def width(self):
        return self._width
    
        """
        Властивість: ширина / Property: width
        
        TODO: Повернути _width
        """

    
    @width.setter
    def width(self, value):
        if not (10 < value < 200):
            raise ValueError("Ширина акваріума повинна бути між 10 та 200 см")
        self._width = value

        """
        Сетер для ширини / Setter for width
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _width = value
        - Викинути ValueError при неправильному значенні
        """

    
    @property
    def height(self):
        return self._height
        """
        Властивість: висота / Property: height
        
        TODO: Повернути _height
        """

    
    @height.setter
    def height(self, value):
        if not (10 < value < 200):
            raise ValueError("Висота акваріума повинна бути між 10 та 200 см")
        self._height = value
        """
        Сетер для висоти / Setter for height
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _height = value
        - Викинути ValueError при неправильному значенні
        """

    
    @property
    def water_level(self):
        return self._water_level
        """
        Властивість: рівень води / Property: water level
        
        TODO: Повернути _water_level
        """

    
    @water_level.setter
    def water_level(self, value):
        if not (0 <= value <= self.height):
            raise ValueError("Рівень води повинен бути між 0 і висотою акваріума")
        self._water_level = value
        """
        Сетер для рівня води / Setter for water level
        
        TODO:
        - Перевірити що 0 <= value <= height
        - Встановити _water_level = value
        - Викинути ValueError при неправильному значенні
        """

    
    @property
    def fish_count(self):
        return self._fish_count
        """
        Властивість: кількість риб / Property: fish count
        
        TODO: Повернути _fish_count
        """

    
    @fish_count.setter
    def fish_count(self, value):
        if value < 0:
            raise ValueError("Кількість риб не може бути від'ємною")
        max_fish = int(self.water_volume / 5)
        if value > max_fish:
            raise ValueError(f"Максимальна кількість риб для поточного об'єму: {max_fish}")
        self._fish_count = value

        """
        Сетер для кількості риб / Setter for fish count
        
        TODO:
        - Перевірити що value >= 0
        - Обчислити максимальну кількість риб (water_volume / 5)
        - Перевірити що value не перевищує максимум
        - Встановити _fish_count = value
        - Викинути ValueError при неправильному значенні
        """

    
    @property
    def temperature(self):
        return self._temperature
        """
        Властивість: температура води / Property: water temperature
        
        TODO: Повернути _temperature
        """

    
    @temperature.setter
    def temperature(self, value):
        if not (18 <= value <= 30):
            raise ValueError("Температура води повинна бути між 18 та 30 °C")
        self._temperature = value

        """
        Сетер для температури / Setter for temperature
        
        TODO:
        - Перевірити що 18 <= value <= 30
        - Встановити _temperature = value
        - Викинути ValueError при неправильному значенні
        """

    
    @property
    def water_volume(self):
        return (self.length * self.width * self.water_level) / 1000
        """
        Властивість: об'єм води в літрах (тільки читання) / Property: water volume in liters (read-only)
        
        Формула: (length * width * water_level) / 1000
        
        TODO: Обчислити та повернути об'єм води
        """

    
    def add_water(self, level_increase):
        if level_increase < 0:
            raise ValueError("Збільшення рівня води повинно бути >= 0")
        new_level = min(self.water_level + level_increase, self.height)
        self.water_level = new_level

      
        max_fish = int(self.water_volume / 5)
        if self.fish_count > max_fish:
            self.fish_count = max_fish
        print(f"Додано воду. Поточний рівень води: {self.water_level} см, об'єм: {self.water_volume} л")
    
        """
        Метод: додати воду / Method: add water
        
        Args:
            level_increase (float): Збільшення рівня в см / Level increase in cm
        
        TODO:
        - Перевірити що level_increase >= 0
        - Обчислити новий рівень (не більше height)
        - Встановити новий рівень через властивість
        - Перевірити чи кількість риб все ще допустима
        - Вивести повідомлення про додавання води
        """

    
    def add_fish(self):
        max_fish = int(self.water_volume / 5)
        if self.fish_count < max_fish:
            self.fish_count += 1
            print(f"Рибу додано. Поточна кількість риб: {self.fish_count}")
            return True
        else:
            print("Не можна додати рибу. Максимальна кількість досягнута")
            return False
        

        """
        Метод: додати рибу / Method: add fish
        
        TODO:
        - Обчислити максимальну кількість риб для поточного об'єму
        - Перевірити чи можна додати ще одну рибу
        - Якщо можна: збільшити fish_count на 1
        - Вивести повідомлення про результат операції
        - Повернути True якщо риба додана, False якщо ні
        """

    
    def remove_fish(self):
        if self.fish_count > 0:
            self.fish_count -= 1
            print(f"Рибу забрано. Поточна кількість риб: {self.fish_count}")
            return True
        else:
            print("Риб немає, нічого забирати")
            return False
        
        """
        Метод: забрати рибу / Method: remove fish
        
        TODO:
        - Перевірити чи є риби в акваріумі
        - Якщо є: зменшити fish_count на 1
        - Вивести повідомлення про результат операції
        - Повернути True якщо риба забрана, False якщо риб немає
        """

    
    def heat(self, new_temperature):
        self.temperature = new_temperature
        print(f"Температура води змінена на {self.temperature}°C")

        """
        Метод: нагріти воду / Method: heat water
        
        Args:
            new_temperature (float): Нова температура / New temperature
        
        TODO:
        - Встановити нову температуру через властивість
        - Вивести повідомлення про зміну температури
        """

    
    def inspect(self):
        max_fish = int(self.water_volume / 5)
        return (f"Акваріум: {self.length}x{self.width}x{self.height} см, "
                f"рівень води = {self.water_level} см, об'єм води = {self.water_volume} л, "
                f"риб = {self.fish_count}/{max_fish}, температура = {self.temperature}°C")
    
        """
        Метод: огляд акваріума / Method: aquarium inspection
        
        TODO:
        - Обчислити максимальну кількість риб для поточного об'єму
        - Повернути форматований рядок з усією інформацією
        - Включити розміри, рівень води, об'єм, кількість риб, температуру
        """



# Область для тестування / Testing area
if __name__ == "__main__":
    print("=== ТЕСТУВАННЯ ШАБЛОНІВ КЛАСІВ / TESTING CLASS TEMPLATES ===\n")
    
    # TODO: Розкоментуйте код нижче після реалізації класів
    # Uncomment code below after implementing classes
    
   
    # Тестування дерева / Testing tree
    print("1. ТЕСТУВАННЯ ДЕРЕВА / TESTING TREE")
    try:
        tree = Tree(10, 50)
        print(tree.get_info())
        tree.grow()
        tree.leaf_fall()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування чайника / Testing kettle
    print("2. ТЕСТУВАННЯ ЧАЙНИКА / TESTING KETTLE")
    try:
        kettle = Kettle(2.0)
        kettle.pour_water(1.5)
        print(kettle.get_status())
        kettle.turn_on()
        kettle.turn_off()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування хмари / Testing cloud
    print("3. ТЕСТУВАННЯ ХМАРИ / TESTING CLOUD")
    try:
        cloud = Cloud(100, 2.5, 15)
        print(cloud.get_forecast())
        cloud.accumulate_moisture(10)
        cloud.rain()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування акваріума / Testing aquarium
    print("4. ТЕСТУВАННЯ АКВАРІУМА / TESTING AQUARIUM")
    try:
        aquarium = Aquarium(50, 30, 40)
        aquarium.add_water(35)
        print(aquarium.inspect())
        aquarium.add_fish()
        aquarium.add_fish()
        aquarium.heat(26)
        print(aquarium.inspect())
    except Exception as e:
        print(f"Помилка: {e}")
    """    
    print("Реалізуйте методи класів та розкоментуйте код для тестування!")
    print("Implement class methods and uncomment code for testing!")"""