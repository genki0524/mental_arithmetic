from random import randint

class Question:
    def __init__(self):
        self.nums = []

    def make_question(self,level):
        self.level = level
        if(self.level==1):
            self.nums = []
            for i in range(10):
                self.nums.append(randint(1,9))

        if(self.level==2):
            self.nums = []
            for i in range(10):
                self.nums[i] = randint(10,99)

        if(self.level==3):
            self.nums = []
            for i in range(10):
                self.nums[i] = randint(100,999)
    
    def getCorrect(self):
        self.correct = 0
        for i in self.nums:
            self.correct += i

        return self.correct
    
