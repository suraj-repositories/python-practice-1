# r = read
# w - write
# a - append text

text = "Into the sunshine \nfull of the light\nleaping and flashing \nfrom morn till night"

anotherText = "\n\nInto the moonlight\nwhiter then snow\nwaving so flower like\nwhen the winds blow"

try:
    with open('documents/test.txt', 'w') as file:
        file.write(text)


    with open('documents/test.txt', 'a') as file_2:
        file_2.write(anotherText)
except Exception as e:
    print(e)
finally:
    print(file.closed)      # the file are already closed so we do not need to close the file
    
    print(file_2.closed)