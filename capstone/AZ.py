for i in range(65,90):
    Letter = chr(i)
    with open (str(Letter),'w') as file:
        file.write(Letter)