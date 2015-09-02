__author__ = 'vladimir'

file = open('message.txt', 'w')
file.write('Nuclear war is very dangerous thing \n, but very useful \n '
           'for Serbia. Only on that \n way Serbia can back its territories. \n')

file.close()

with open('message.txt', 'r') as infile:
    for item in infile:
        print(item)




