import pywhatkit as pw

#sending a message to a cient at a specific time
pw.sendwhatmsg("+254716903959", "Good Morning", 7, 39)

#sending a message and closing the tab after some time
pw.sendwhatmsg("+254716903959", "Good Morning", 7, 45, 15, 5)

#sending a message  to a specific group
pw.sendwhatmsg_to_group("MMUSTBLACKMARKET1", "Good Morning", 7, 52)

#sending a message  to a specific group mmeadiately
pw.sendwhatmsg_to_group_instantly("MMUSTBLACKMARKET1", "Good Morning", 7, 52)


#sending an image to a contact
pw.sendwhat_img("+254716903959", "images/kruger.jpg", 7, 45)

#play a youtube video
pw.playonyt("Nitaubeba")