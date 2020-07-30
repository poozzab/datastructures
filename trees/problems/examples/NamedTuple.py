# example code from a hackerrank problem that utilized namedtuple
# this is being archived in my github so that I can remember how awesome this feature is
# https://www.hackerrank.com/challenges/py-collections-namedtuple/

from collections import namedtuple
N = int(input())
n = N
Student = namedtuple('Student',input())
students = list()
while n > 0:
    inp = input().split()
    students.append(Student(*inp))
    n = n - 1
print(sum(list(map((lambda x : int(x.MARKS)) , students))) / len(students))
