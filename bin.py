import pygame

class Bin:
    def __init__(self, screen_width, screen_height, screen):
        self.screenwidth = screen_width
        self.screenheight = screen_height
        self.screen = screen
        self.recycle = pygame.image.load("recycle_bin.png")
        self.general = pygame.image.load("general_bin.png")
        self.recycle = pygame.transform.smoothscale(self.recycle, (round(self.screenwidth*0.2), round(self.screenheight*0.3)))
        self.general = pygame.transform.smoothscale(self.general, (round(self.screenwidth*0.2), round(self.screenheight*0.2)))
        # original code
        self.rx = round(self.screenwidth*0.15)
        self.ry = round(self.screenheight*0.65)
        self.gx = round(self.screenwidth*0.55)
        self.gy = round(self.screenheight*0.7)

    def renderbin(self):
        self.screen.blit(self.recycle, (self.rx, self.ry))
        self.screen.blit(self.general, (self.gx, self.gy))
    def movebin(self):
        key = pygame.key.get_pressed()
        if self.rx > self.screenwidth*0.8:
            self.rx = self.screenwidth*0.8
        elif self.rx <0:
            self.rx = 0
        if self.gx > self.screenwidth*0.8:
            self.gx = self.screenwidth*0.8
        elif self.gx <0:
            self.gx = 0
        else:
            if key[pygame.K_a]:
                self.rx -= 1.5
            elif key[pygame.K_d]:
                self.rx += 1.5
            if key[pygame.K_LEFT]:
                self.gx -= 1.5
            elif key[pygame.K_RIGHT]:
                self.gx += 1.5
        
    def checkDist(self,coords):
        recycable_dist = ((coords[0]-self.rx)**2 + (coords[1]-self.ry)**2)**0.5 #dist formula 
        non_recycable_dist = ((coords[0]-self.gx)**2 + (coords[1]-self.gy)**2)**0.5 #dist formula
        if recycable_dist < non_recycable_dist:
            return [recycable_dist,0]
        else:
            return [non_recycable_dist,1]
