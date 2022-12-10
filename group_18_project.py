# Python program to find angle between hour and minute hands
# Function to Calculate angle b/w hour hand and minute hand
def calcAngle(h,m):
   if(h < 0 or m < 0 or h > 24 or m > 60):
       print('Wrong input')
       exit()
   else:
       if (h == 12):
               h = 0
       if (m == 60):
           m = 0
           h += 1
       # handle 24-hour notation
       if(h>12):
           h = h-12
       # Calculate the angles moved by
       # hour and minute hands with reference to 12:00
       hour_angle = 0.5 * (h * 60 + m)
       minute_angle = 6 * m 
       # Find the difference between two angles
       angle = abs(hour_angle - minute_angle)
       # Return the smaller angle of two possible angles
       angle = min(360 - angle, angle)  
       return angle
# Driver Code
h = int(input("Enter Hours: "))
m = int(input("Enter Minutes: "))
print("{}°".format (calcAngle(h,m)))
# This code is contributed by Anshu Goyal,Dinesh,Hemanth
