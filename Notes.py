#Create an empty list to store hits
num_hits= int(input('How many hits:'))
hit_list = []

#Take user input
for i in range(num_hits):
    hit_list.append(input('Enter your top hit #' + str(i+1)))

#Correct their choices
if 'Bieber' not in hit_list:
    hit_list.insert(0,'Justin Bieber the Magnificent')
    del hit_list[-1]

#Print output
for i in range(len(num_hits)):
    print('Number' + str(i+1)+ 'Hit:'+ hit_list[i][0:4]) # Prints only the first 4 characters
