# Домашнее задание по теме "Простые Юнит-Тесты"

from unittest import TestCase


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


class RunnerTest(TestCase):

    def test_walk(self):
        run_cls1 = Runner('test')
        for _ in range(10):
            run_cls1.walk()
        #print(f' Результат функции walk: {run_cls1.distance}')
        self.assertEqual(run_cls1.distance, 50)
        #self.assertEqual(run_cls1.distance, 150)

    def test_run(self):
        run_cls2 = Runner('test')
        for _ in range(10):
            run_cls2.run()
        #print(f' Результат функции run: {run_cls2.distance}')
        self.assertEqual(run_cls2.distance, 100)
        #self.assertEqual(run_cls2.distance, 500)

    def test_challenge(self):
        run_cls_r = Runner('test')
        run_cls_w = Runner('test')
        for _ in range(10):
            run_cls_r.run()
            run_cls_w.walk()
        self.assertNotEqual(run_cls_r.distance, run_cls_w.distance)
        #self.assertEqual(run_cls_r.distance, run_cls_w.distance)
