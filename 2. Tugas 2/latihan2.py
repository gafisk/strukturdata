class Stack:
    def _init_(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []

    tokenList = infixexpr.split()
    tokenList.reverse()
    for i in range(len(tokenList)):
        if tokenList[i] == '(':
            tokenList[i] = ')'
        elif tokenList[i] == ')':
            tokenList[i] = '('
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while (not opStack.isEmpty()):
        postfixList.append(opStack.pop())
    postfixList = postfixList[::-1]
    return " ".join(postfixList)


print("infix: A * B + C * D")
print("postfix:"),
print(infixToPostfix("A * B + C * D"))
print('')
print("infix: ( A + B ) * C - ( D - E ) * ( F + G )")
print("postfix:"),
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
