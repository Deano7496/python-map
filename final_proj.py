# Final Project
# Dean Foster
# 04/20/2022

from tkinter import *
#graphics
window = Tk()
canvas = Canvas(window, width=500, height=500, background="black")
canvas.pack()

# functions

def contains_word(word, message):
    return word in message

def get_tweet(line):
    split_line = line.split("\t")[3]
    return split_line


def get_latitude(line):
    location = line.split('\t')[0]
    return float(location[1:].split(",")[0].strip())
    
  
def get_longitude(s):
    s = s.split(", ")[1]
    s = s.split("]")[0]
    return float(s)
    

def get_gps_pixel_x(line):
    long = get_longitude(line)
    x = int((long + 180) * 500.0/360)
    return float(x)

   
def get_gps_pixel_y(line):
    return 500 - ((get_latitude(line) + 180) * 500.0 / 360)
     
def draw_gps_point(line):
    x = get_gps_pixel_x(line)
    y = get_gps_pixel_y(line)   
    canvas.create_rectangle(x, y, x+1, y+1, fill="white", width=0)

# Main Program
f = open("tweets.txt")
tweets = f.read()
split_tweet = tweets.split("\n")
print("All tweets loaded")
count = 0
user = input("Enter a search word: ")
for line in split_tweet:
    tweet = get_tweet(line)
    if contains_word(user, tweet):
        count += 1
        draw_gps_point(line)
        
summary = f'The word {user} appears {count} times.'
canvas.create_text(50, 50, anchor=S, text=summary, fill="white")
# complete drawing
window.mainloop()
