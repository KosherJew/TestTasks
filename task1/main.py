import json,random

debug = False
class town:
    def __init__(self, path):
        self.path = path
        try:
            with open(self.path, 'r') as f:
                self.citys = json.load(f)
            self.__normalise_population()
        except FileNotFoundError:
            if debug:
                print(f"Файл {path} не существует")
            exit(1)
        except json.decoder.JSONDecodeError:
            if debug:
                print("В файле",path,"ошибки структуры Json")
            exit(1)
        except TypeError:
            if debug:
                print(f"В файле {path} Типы данных не соответвуют задаче")
            exit(1)
        except Exception as err:
            if debug:
                print(f"Неизвестная ошибка", repr(err))
            exit(1)

    def __normalise_population(self):
        sum = 0
        for city in self.citys:

            sum += city['population']
        for city in self.citys:
            city['population'] = city['population']/sum

    def get_rtown(self):
        sum = 0
        lucky = random.random()
        for city in self.citys:
            sum += city['population']
            if sum< lucky:
                pass
            else:
                return city['name']
        return city['name']
if __name__ == '__main__':
     debug = True
     city = town("input.json")
     print('Случайный город:',city.get_rtown())
