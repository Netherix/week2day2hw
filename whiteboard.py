
# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

# fix_string('T0PP1NG5') => 'TOPPINGS'
# fix_string('5OUR') => 'SOUR'
# fix_string('1GLO0') => 'IGLOO'

def fix_string(word): # ASK IF U CAN PUT A LIST IN PARAMETER
    solution = ''
    for letter in word:
        if letter == '0':
            solution += 'O'
        elif letter == '5':
            solution += 'S'
        elif letter == '1':
            solution += 'I'
        else:
            solution += letter
    return solution

print(fix_string('T0PPING5'))
print(fix_string('5OUR'))
print(fix_string('1GLOO'))

