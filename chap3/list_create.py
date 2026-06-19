lst1 = [item for item in range(1,11)]
print(lst1)

lst2 = [item * item for item in range(1,11)]
print(lst2)

import random
lst3 = [random.randint(1,100) for _ in range(10)]
print(lst3)

#从列表中选择符合条件的元素组成新列表
lst4 = [i for i in range(1,11) if i%2]
print(lst4)

