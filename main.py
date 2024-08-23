import unittest


# Исходный класс Runner
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


# Класс тестирования
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)  # Проверяем, что distance равен 50

    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)  # Проверяем, что distance равен 100

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")

        for _ in range(10):
            runner1.run()  # Каждый раз увеличиваем distance на 10
            runner2.walk()  # Каждый раз увеличиваем distance на 5

        # Проверяем, что distance у двух бегунов не равны
        self.assertNotEqual(runner1.distance, runner2.distance)


# Запуск тестов
if __name__ == '__main__':
    unittest.main()

