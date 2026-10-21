class Solution(object):
    def evalRPN(self, tokens):

        stack = []

        for t in tokens:

            if t not in "+-/*":
                stack.append(int(t))

            else:

                l, r = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(l + r)

                if t == "*":
                    stack.append(l * r)

                if t == "-":
                    stack.append(r - l)

                if t == "/":
                    stack.append(int(float(r) / l))

        return stack.pop()


        