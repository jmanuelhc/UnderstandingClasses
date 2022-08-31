#Small project to simulate an exportation of apples, where 1000 have to be exported. Each apple weighs randomly between 0.2 and 0.5 kg,
#as long as it does not exceed 300kg the exportation can be done if the 300kg is exceeded, then the number of apples is up to the 
#max apples generated before reaching 300kg
#Useful to test class variables and instance variables.

import random
class Apple:
    apple_counter = 0
    apples_weight = 0

    def __init__(self):
        self.appleSN = "apple"+str(Apple.apple_counter+1)
        self.weight = random.uniform(0.2,0.5)
        Apple.apples_weight += self.weight
        if Apple.apples_weight > 300:
            Apple.apples_weight -= self.weight
            print(f"Max weight units reached. Total apples:{Apple.apple_counter}. Total weight:{Apple.apples_weight} ")
            quit()
        Apple.apple_counter +=1
    
    def __str__(self):
        return self.appleSN

cesto = []
for x in range(1000):
    cesto.append(f"Apple{x}")
    cesto[x] = Apple()    
    #print(cesto[x],cesto[x].weight) #can be used to check the specific apple's info

print(Apple.__dict__["apple_counter"],Apple.__dict__["apples_weight"]) # if the apples reach 1000, then the program prints the apples and the weight
