

def even_odd(num):

    if num % 2 == 0:
        print("even")
    else:
        print("odd") 

#even_odd(11)
#even_odd(2)

def max(num1,num2):
  print('')


# Rands to usd
# R18.754 == 1 USD
# Y*18.754 = Y US
# R18.754 x 3 == 3 USD


# def function (4)
def usd_to_rands(usd):
    # const R =18.754
    rand = 18.754
    # Y = 18.754 * 4
    output = rand * usd
    # print(Y)
    print(output)

# X = 1 then Y = 18,75
#usd_to_rands(1)
# X = 4 then Y = 75,02
#usd_to_rands(4)




def compare(num1,num2):
  print('Is Equal:',num1 == num2)
  print('Is num1 Greater than Num2:',num1 > num2)
  print("Is num1 less than num2:",num1 < num2 )
  

compare(3,5)
