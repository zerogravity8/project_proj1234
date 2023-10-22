from utils import arrs



def test_get():
   # Тестирование случая, когда индекс находится в диапазоне массива
   assert arrs.get([1, 2, 3], 1, "default") == 2

   # Тестирование случая, когда индекс находится вне диапазона массива
   assert arrs.get([1, 2, 3], 3, "default") == "default"


def test_my_slice():
   # Тестирование случая, когда указан только start
   assert arrs.my_slice([1, 2, 3, 4, 5, 6], start=2) == [3, 4, 5, 6]

   # Тестирование случая, когда указаны start и end
   assert arrs.my_slice([1, 2, 3, 4, 5, 6], start=1, end=4) == [2, 3, 4]

   # Тестирование случая, когда указан только end
   assert arrs.my_slice([1, 2, 3, 4, 5, 6], end=3) == [1, 2, 3]

   # Тестирование случая, когда список пустой
   assert arrs.my_slice([], start=1, end=3) == []









