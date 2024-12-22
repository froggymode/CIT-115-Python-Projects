# project for calculating body weight on each planet in our solar system
# inputs need to be name and weight in pounds
# output needs to show each planet and the interplanetary corresponding weight

#inputs
sName=input("What is your name? ")
nWeight=float(input("What is your current weight, in pounds? "))

#calculations
#need 10 total, one for each planet or moon named as such
nMercury=nWeight*0.38
nVenus=nWeight*0.91
nMoon=nWeight*0.165
nMars=nWeight*0.38
nJupiter=nWeight*2.34
nSaturn=nWeight*0.93
nUranus=nWeight*0.92
nNeptune=nWeight*1.12
nPluto=nWeight*0.066

print("Hi",sName,", here is what you would weigh (in pounds) on the different planets in our solar system!")
print("Weight on Mercury  " +format(nMercury,'10.2f'))
print("Weight on Venus    " +format(nVenus,'10.2f'))
print("Weight on the Moon " +format(nMoon,'10.2f'))
print("Weight on Mars     " +format(nMars,'10.2f'))
print("Weight on Jupiter  " +format(nJupiter,'10.2f'))
print("Weight on Saturn   " +format(nSaturn,'10.2f'))
print("Weight on Uranus   " +format(nUranus,'10.2f'))
print("Weight on Neptune  " +format(nNeptune,'10.2f'))
print("Weight on Pluto    " +format(nPluto,'10.2f'))



