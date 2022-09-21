from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

"""first namedtuple"""
user1 = ("Waad", "Student")

print(f'{user1[0]} is a {user1[1]}')
user_info = namedtuple("user_info", ['name', 'role'])
first_user = user_info("Waed", "Student")
print(f'{first_user.name} is a {first_user.role}')

"""about defualtdict it does not return an error if the key is missing
but it create the key and a value (that we decide at the beginning.)"""
normal_dict = {"one": 1}
defualt_dict = defaultdict(list)
defualt_dict["one"] = 1
print(defualt_dict["one"])
print(defualt_dict["three"])  # not an error
print(normal_dict["one"])
# print(normal_dict["three"]) error

random_text = "I inadvertently went to See's Candy last week (I was in the mall looking for phone repair), and as it " \
              "turns out, See's Candy now charges a dollar -- a full dollar -- for even the simplest of their wee " \
              "confection offerings. I bought two chocolate lollipops and two chocolate-caramel-almond things. The " \
              "total cost was four-something. I mean, the candies were tasty and all, but let's be real: A Snickers " \
              "bar is fifty cents. After this dollar-per-candy revelation, I may not find myself wandering dreamily " \
              "back into a See's Candy any time soon.".split()

print(Counter(random_text).most_common(2))
