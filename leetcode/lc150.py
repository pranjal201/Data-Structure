#150. Evaluate Reverse Polish Notation
import math
class Solution:

    #Initialinzing stack and operands answer 
    def __init__(self) -> None:
        self.operand1=0
        self.opernad2=0
        self.stack = []
    

    def evalRPN(self,tokens: list[str]) ->int:
        for token in tokens:
            if token =='+': 
                self.operand2 = self.stack.pop()
                self.operand1 = self.stack.pop()
                self.stack.append(self.operand1+self.operand2)
                print(token)
            elif token =='-': 
                self.operand2 = self.stack.pop()
                self.operand1 = self.stack.pop()
                self.stack.append(self.operand1-self.operand2)
                print(token)
            elif token =='*': 
                self.operand2 = self.stack.pop()
                self.operand1 = self.stack.pop()
                self.stack.append(self.operand1*self.operand2)
                print(token)
            elif token =='/': 
                self.operand2 = self.stack.pop()
                self.operand1 = self.stack.pop()
                self.stack.append(math.trunc(self.operand1 / self.operand2))
            else:
                self.stack.append(int(token))
            print(self.stack)
            
        return self.stack[0]

if __name__ == '__main__':
    obj = Solution()
    tokens = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
    print(obj.evalRPN(tokens))
