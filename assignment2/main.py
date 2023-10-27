import js as p5
from js import document

data_string = None
data_list = None
angle_val = None
sensor_val = None


# # load image data and assign it to variable:
# swirl_img = p5.loadImage('swirl.png')

# # load font data and assign it to variable:
# jellee_font = p5.loadFont('Jellee.otf')

def setup():
  p5.createCanvas(400, 400)


def draw():
  global data_string, data_list
  global angle_val, sensor_val

  p5.background(5, 2, 40) # dark blue background

  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')
  #print(data_list)

  # assign 1st item of data_list to angle_val:
  angle_val = int(data_list[0])
  # assign 2nd item of data_list to sensor_val:
  sensor_val = int(data_list[1])

  draw_track()
  draw_planet(0, 0, 50, 250, 101, 22)
  draw_planet(-15, 47, 12, 167, 161, 131)
  draw_planet(56, 30, 19, 0, 156, 193)
  draw_planet(5, 80, 18, 158, 49, 51)
  draw_planet(-75, -80, 24, 206, 163, 50)
  draw_jupiter(-100, 85, 26, 208, 205, 152)
  draw_planet(145, -50, 22, 142, 229, 209)
  draw_planet(160, 75, 20, 20, 116, 193)
  draw_stars(sensor_val - 155)


def draw_track():
  p5.strokeWeight(1)
  p5.stroke(255)
  p5.noFill()
  p5.push()
  p5.translate(200, 200)
  for i in range(3):
    p5.ellipse(0, 0, 100 + i * 30, 100 + i * 30)
  for i in range(4):
    p5.ellipse(0, 0, 220 + i * 45, 220 + i * 45)
  p5.pop()


def draw_planet(x, y, size, r, g, b):
  p5.fill(r, g, b)
  p5.noStroke()
  p5.push()
  p5.translate(p5.width/2, p5.height/2)
  p5.rotate(angle_val/60)
  p5.ellipse(x, y, size, size)
  p5.pop()


def draw_jupiter(x, y, size, r, g, b):
  p5.fill(r, g, b)
  p5.noStroke()
  p5.push()
  p5.translate(p5.width/2, p5.height/2)
  p5.rotate(angle_val/60)
  p5.ellipse(x, y, size, size)
  p5.noFill()
  p5.stroke(208, 205, 152)
  p5.strokeWeight(2)
  p5.ellipse(x, y, 35, 8)
  p5.pop()

def draw_stars(number):
    p5.noStroke()
    for i in range(100):
        p5.fill(255, 255, 255, number)
        
        # Randomly position each circle
        x = p5.random(0, p5.width)
        y = p5.random(0, p5.height)
        
        # Randomly size each circle between 1 and 4
        star_size = p5.random(1, 5)
        
        p5.ellipse(x, y, star_size, star_size)
