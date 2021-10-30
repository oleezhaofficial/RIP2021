from gen_random import get_random

class Unique(object):

    def __init__(self, items, **kwargs):
        self.unicList = list()
        self.data = items
        self.index = 0
        if 'ignore_case' in kwargs.keys() and kwargs['ignore_case'] == True:
            self.ignore_case = True
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index < len(self.data):
                if self.ignore_case == False:
                    current = self.data[self.index]
                    self.index += 1
                    if not current in self.unicList:
                        self.unicList.append(current)
                        return current
                else:
                    current = self.data[self.index]
                    self.index += 1
                    if isinstance(current, str):
                        current = current.lower()
                    if not current in self.unicList:
                        self.unicList.append(current)
                        return current
            else:
                raise StopIteration


    def __iter__(self):
        return self

def main():
    data = ['a','A','b', 'B', 'c', 'C', 'C', 'A', 'D']
    random_nums = get_random(10, 1, 7)
    print(data)
    for i in Unique(data, ignore_case=True):
        print(i, end='\t') 
    print('\n')   
        
    print(random_nums)
    for i in Unique(random_nums):
        print(i, end='\t')

if __name__ == "__main__":
    main()