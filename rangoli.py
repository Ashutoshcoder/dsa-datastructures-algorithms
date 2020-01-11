def print_rangoli(size):
    # your code goes here
    alphabets = []
    alpha = 'a'
    for i in range(0,size): 
        alphabets.append(alpha) 
        alpha = chr(ord(alpha) + 1)  

    print(alphabets)


if __name__ == '__main__':
    n = input()
    print_rangoli(int(n))