def push(stack, data, max_length):
   if len(stack) < max_length:
       stack.append(data)
   else:
       print("over flow")

   return stack


def pop(stack):
    if stack.append[2]:
        del stack[2]
    else:
        print("under flow")
max_length = 3
stack = []


while True:

    que = input("Enter push or pop : ")

    if que == "push":
        data = int(input("Enter you number : "))
        stack = push(stack, data, max_length)

    elif que == "pop":
        data = int(input("Enter you number : "))


