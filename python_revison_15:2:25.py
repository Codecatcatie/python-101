#hello
# hi!

# a room full of people
# 99% left-handed people
# how many of left-handed people to leave the room
# 50% left-h / 50% right-h
#left_percentage = int(input("how many left handed people are there?"))

# 100 people in the room
# 99% left-handed 





people_inside = 100
left_percentage = 99
right_percentage  = 1
people_leaving = 49 + 1 

while  left_percentage != 49 and  right_percentage != 1 :
    people_leaving += 1
    left_percentage = left_percentage - 1
print(f"{people_leaving} need to leave so that the ratio is 98:2 for right handed :left handed people  " )
 


#Around 75% of left-handers have two right-handed parents and only 2% have two left-handed parents. Between 7 and 8 out of 10 children born to two left handed parents will be right handed.




#HTTP was initiated by Tim Berners-Lee
#Britih scientist
#1989 CERN
#https://www.w3.org/People/Berners-Lee/   = first website

#info.cern.ch
#he got banned form usign computer sat oxford as his friends end toplay computer games,then invented the world wide web.
# GET( fidn and get info ),POST (save, sending ),PUT(edit), DELETE(edit) =types of requests  https and http. 
#request a server andthe server gives you a response
# 404 error: no website found.
# https://github.com/123123sdfwf

#https://www.pixar.com/213123

#https://www.npr.org/sdfdgsdg
# urban legend :in the early 80s before the worldwide web.in CERN there was ar oomw ehre all important files were stored,(where they couldn't findinfo they went there (to CERN)). the room was called 404. there is no confirmation of  this rumour



# Function to calculate the number of people who need to leave
def calculate_people_to_leave(total_people, left_percentage, desired_left_percentage):
    # Calculate the initial number of left-handed and right-handed people
    left_handed = (left_percentage / 100) * total_people
    right_handed = total_people - left_handed
    
    # Ensure inputs make sense
    if desired_left_percentage >= left_percentage:
        return "The desired percentage must be lower than the current percentage."
    
    # Start removing people until the new ratio is achieved
    people_leaving = 0
    while (left_handed / (total_people - people_leaving)) * 100 > desired_left_percentage:
        left_handed -= 1  # Remove one left-handed person
        people_leaving += 1
    
    return people_leaving

# User input for flexibility
total_people = int(input("Enter the total number of people in the room: "))
left_percentage = float(input("Enter the current percentage of left-handed people: "))
desired_left_percentage = float(input("Enter the desired percentage of left-handed people: "))

# Compute the result
result = calculate_people_to_leave(total_people, left_percentage, desired_left_percentage)

# Print the result
print(f"{result} people need to leave to achieve the desired ratio.")
