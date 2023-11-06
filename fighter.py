import pygame

#Owen Gibbs
class Fighter():
    def __init__(self, player, x, y,flip,data,sprite_sheet,animation_steps):
        self.player = player
        self.width = data[0]
        self.height = data[1]
        self.image_scale = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0: idle #1: run #2: jump #3: attack1 #4: attack2 #5: hit #6: death #7: transform
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time= pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.hit = False
        self.health = 100
        self.alive = True


    def load_images(self,sprite_sheet,animation_steps):
        #Extract images from spritesheet - Owen Gibbs
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.width,y * self.height,self.width,self.height)
                temp_img_list.append(pygame.transform.scale(temp_img,(self.width * self.image_scale, self.height * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
    
    def move(self, screen_width, screen_height, surface, target, round_over):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0

        #get keypresses - Zain Khalil
        key = pygame.key.get_pressed()

        #can only perfom other actions if not currently attacking
        #movement
        if self.attacking == False and self.alive == True and round_over == False:
            #checks player 1's controls - Ryaan Mohideen
            if self.player == 1:
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED 
                    self.running = True
                #jump
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.attack(target)
                    #determine which attack type was used
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
            #checks player 2's controls - Ryaan Mohideen
            if self.player == 2:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                if key[pygame.K_RIGHT]:
                    dx = SPEED 
                #jump
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                #attack
                if key[pygame.K_RETURN] or key[pygame.K_RSHIFT]:
                    self.attack(target)
                    #determine which attack type was used
                    if key[pygame.K_RETURN]:
                        self.attack_type = 1
                    if key[pygame.K_RSHIFT]:
                        self.attack_type = 2

            
            
        #apply gravity - Owen Gibbs
        self.vel_y += GRAVITY
        dy += self.vel_y

        #ensure player stays on screen - Owen Gibbs
        if self.rect.left + dx < 0:
            dx = 0 -self.rect.left
        if self.rect.right +dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom
        
        #ensure plays face eachother - Zain Khalil
        if target.rect.centerx > self.rect.centerx:
            self.flip = True
        else:
            self.flip = False
        
        #Apply attack cooldown - Ryan Rahman
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        #update player position - Zain Khalil
        self.rect.x += dx
        self.rect.y += dy
    

    #Handle animation updates - Ryan Rahman
    def update(self):
        #Check what action the player is performing - Ryan Rahman
        if self.health<= 0:
            self.health = 0
            self.alive = False
            self.update_action(11)
        elif self.hit == True:
           self.update_action(10) 
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(7)
            elif self.attack_type == 2:
                self.update_action(8)
        elif self.jump == True:
            self.update_action(5)
        elif self.running == True:
            self.update_action(6)
        else:
            self.update_action(12)
        animation_cooldown = 150
        self.image = self.animation_list[self.action][self.frame_index]
        #Check if enough time has passed since the last update - Ryan Rahman
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #Check if the animation has finished - Ryan Rahman
        if self.frame_index >= len(self.animation_list[self.action]):
            #If the player is dead then end the animation - Ryan Rahman
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                #Check if an attack has been executed - Ryan Rahman
                if self.action == 7 or self.action == 8:
                    self.attacking = False
                    self.attack_cooldown = 50
                #Check if Damage was taken - Ryan Rahman
                if self.action == 10:
                    self.hit = False
                    #If the player was on the middle of the attack, stop attack - Ryan Rahman
                    self.attacking = False
                    self.attack_cooldown = 20

    def attack(self, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            attacking_rect = pygame.Rect(self.rect.centerx - 2* self.rect.width * self.flip, self.rect.y, 2 * self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= 10
                target.hit = True
    
   #Ryan Rahman
    def update_action(self,new_action):
        #Check if the new action is different to the previous one
        if new_action  != self.action:
            self.action = new_action
            #Update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    #Zain Khalil
    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip,False)
        surface.blit(img,(self.rect.x,self.rect.y))





