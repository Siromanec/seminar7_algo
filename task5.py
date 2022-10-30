from random import randint
class BinaryCounter():
    def __init__(self, k) -> None:
        self.arr = [0]*k
        self.len = 1
        self.tokens = 1
        self.__k = k
    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, item):
        self.arr[key] = item
    def __str__(self) -> str:
        return str(self.arr)
    def increment(self):

        i = 0
        self.tokens += 3
        while i < self.len and self[i] == 1:
            self.tokens -= 1
            if self.tokens <0:
                raise ValueError("out of tokens!")
            self[i] = 0
            i += 1
        if i < self.len:
            self.tokens -= 1
            self[i] = 1
        if self[self.len-1] == 1 and self.len<self.__k:


            self.len += 1

    def reset(self):
        
        i = 0
        while i < self.len:
            self.tokens-=1

            if self.tokens <0:
                raise ValueError("out of tokens!")
            self[i] = 0
            i += 1
        self.len = 1

counter = BinaryCounter(20)
for i in range(2**20-1):
    counter.increment()
for i in range(2**20-1):
    counter.increment()
    if not i%8191:
        counter.reset()
print(counter)
print(counter.tokens)
for i in range(2**20-1):
    counter.increment()
    if not i%4095:
        counter.reset()

print(counter)
print(counter.tokens)
for i in range(2**20-1):
    counter.increment()
    if not i%256:
        counter.reset()
print(counter)
print(counter.tokens)
for i in range(2**20-1):
    counter.increment()
    if not i%128:
        counter.reset()
print(counter)
print(counter.tokens)
for i in range(2**20-1):
    counter.increment()
    if not i%8:
        counter.reset()
print(counter)
print(counter.tokens)
for i in range(2**20-1):
    counter.increment()
    if not i%randint(256,8191):
        counter.reset()
print(counter)
print(counter.tokens)
counter.reset()
print(counter)
print(counter.tokens)


