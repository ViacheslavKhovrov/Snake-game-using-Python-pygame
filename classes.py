class Snake():
    def __init__(self, x, y, size):
        self.posx = x
        self.posy = y
        self.size = size
        self.velx = 5
        self.vely = 0
        self.food = False
        self.foodx = 0
        self.foody = 0
        self.food_radius = 10
        self.body = [[[x, y], [x - 20, y], [x - 15, y], [x - 10, y], [x - 5, y]]]
        self.body.append([[x - 20, y], [], [], [], []])
        self.game_over = False
        self.turn_possible = True
        self.turn_counter = 5

        
    def movement(self, SCREENWIDTH, SCREENHEIGHT):

        predicted_location_x = self.posx + self.velx
        predicted_location_y = self.posy + self.vely

        if predicted_location_x < 0:
            self.velx = 0
            self.game_over = True
        elif predicted_location_x + self.size > SCREENWIDTH:
            self.velx = 0
            self.game_over = True

        if predicted_location_y < 0:
            self.vely = 0
            self.game_over = True
        elif predicted_location_y + self.size > SCREENHEIGHT:
            self.vely = 0
            self.game_over = True

        
        self.posx += self.velx
        self.posy += self.vely

        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].append(self.body[i][0])
            self.body[i].pop(1)
            self.body[i][0] = self.body[i - 1][1]

        self.body[0].append([self.posx, self.posy])
        self.body[0].pop(1)
        self.body[0][0] = [self.posx, self.posy]
        

            

        
