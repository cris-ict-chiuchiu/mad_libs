# Siyun, ChiuChiu, Grade 8 ICT

# Lists

names1 = ["ChiuChiu", "Siyun", "(The very handsome) Teacher Isaac", "John", "Nadia Sofia Martinez", "Miguel", "Al3jadr0", "Minseo"]

names2 = ["Jame’s food shop", "Tipsy diner", "Chiang Rai’s best restaurant", "Eat-with-Siyunny", "Siyunny’s mukbang", "ChiuChiu’s mukbang", "Jame’s noodle stall"]

foods = ['mini waffles', 'frozen orange juice', 'dry soup', 'ice cream with ketchup', 'kimchi with tofu flavored popcorn', 'live squids', 'fried chicken flavored cotton candy']

nouns = ['Kids', 'sea urchins', 'horse figurines', 'mini firetrucks', 'triangular apples', 'snakes', 'Human-sized barbie dolls', 'balls of yarn', '3am mystery box', 'taxidermized dogs']

colors = ['periwinkle', 'beige', 'gray', 'lavender', 'turquoise', 'neon pink', 'aquamarine', 'mint']

verbs = ['eating', 'playing', 'looking', 'crying', 'flying', 'cooking', 'painting', 'drinking', 'listening', 'walking', 'running', 'laughing', 'reading', 'building', 'catching', 'live laugh loving', 'loving', 'affecting', 'agreeing']

numbers = [423413413, 5.5, -6,4.4444444444444444444444444,1,2,3,4,5,6,7,8,9,10, 3.14159265359, 70, 836, 4030, 5830, 7192, 7912, 9272, 10430, 6174, 666, 999, 444]

directions = ['up', 'down', 'left', 'right', 'away', 'forward', 'below', 'above', 'around'] 

jobs = ['Nurse', 'Firefighter', 'Cook',  'Programmers', 'Teachers', 'Businessmen', 'Farmers', 'Air Hostage', 'Doctors', 'Maids']

medications = ['Paracetamol', 'vaseline', 'adderall', 'gaviscon', 'Levothyroxine',  'Lipitor', 'Diabetes', 'blood']

songs = ['Billie Jean by Michael Jackson', 'Easy On Me by Adele', 'Cold Heart by EltonJohn and Dua Lipa', 'Bad habits by Ed sheeran', 'My universe by Coldplay and BTS', 'On the ground by ROSE', 'Leave before you love me by Marshmello and Jonas brothers', 'Stay by Kid Laro']

somethingcools = ['purple coins', 'rainbow rubber cow toys', 'fairy dust','beautiful mini Qing dynasty robes', 'Pickachu pokemon cards', 'Ferero rochers', 'Medical gloves', 'Empty tomato juice cartons']

# Create a random lists

import random

name1 = random.choice(names1)

name2 = random.choice(names2)

food = random.choice(foods)

noun = random.choice(nouns)

color = random.choice(colors)

verb = random.choice(verbs)

number = random.choice(numbers)

direction = random.choice(directions)

job = random.choice(jobs)

medication = random.choice(medications)

song = random.choice(songs)

somethingcool = random.choice(somethingcools)

# Create a mad lib

mad_lib = f""" It was a sunny day when {name1} dicided to go to eat {food} at a place called {name2}. 
But everything went wrong after that........ As he went to his favorite restaurant, a bunch of {noun} went tunbling into the streets blocking his way. 
These {noun} are covered in {color} glitter and as the {noun} went tunbling down. The {color} glitter on the {noun} went into {name1}'s nose. 
He is very allergic to {color} glitter and caused him to {verb} profusely. 
The {number} people around him just having a relaxing time saw {name1} {verb} profusely felt weird out by the sudden outburst of this random person and the weird glittered {noun} on the ground made them run {direction} from {name1}.
Seeing all this commotion, the {job} arrived to help solve the problem. 
The {job} tried to help {name1} by giving them some {medication}. But it did not work, IT BACKFIRED.
Since {medication} contained {somethingcool} in them, they made the {noun} start violently singing {song}, shaking, violently making the {color} glitter swirl around even more.
Now the {job} are also {verb} profusely.. Who would save them now??
"""

import cowsay

cowsay.stegosaurus('\033[96m' + mad_lib)

