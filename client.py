import pygame
from network import Network
import math

win = pygame.display.set_mode((500,500))
background= pygame.transform.scale(pygame.image.load('assets/chessboard.png'), (500, 500))
pygame.display.set_caption("Chess")

pawn_b = pygame.transform.scale(pygame.image.load('assets/black_pawn.png'), (32, 32))
pawn_w = pygame.transform.scale(pygame.image.load('assets/white_pawn.png'), (32, 32))
king_b = pygame.transform.scale(pygame.image.load('assets/black_king.png'), (32, 32))
king_w = pygame.transform.scale(pygame.image.load('assets/white_king.png'), (32, 32))
queen_b = pygame.transform.scale(pygame.image.load('assets/black_queen.png'), (32, 32))
queen_w = pygame.transform.scale(pygame.image.load('assets/white_queen.png'), (32, 32))
knight_b = pygame.transform.scale(pygame.image.load('assets/black_knight.png'), (32, 32))
knight_w = pygame.transform.scale(pygame.image.load('assets/white_knight.png'), (32, 32))
rook_b = pygame.transform.scale(pygame.image.load('assets/black_rook.png'), (32, 32))
rook_w = pygame.transform.scale(pygame.image.load('assets/white_rook.png'), (32, 32))
bishop_b = pygame.transform.scale(pygame.image.load('assets/black_bishop.png'), (32, 32))
bishop_w = pygame.transform.scale(pygame.image.load('assets/white_bishop.png'), (32, 32))

mark =  pygame.transform.scale(pygame.image.load('assets/bonus.png'), (32, 32))


clientNumber = 0
positions = []
pawn_black,pawn_white, king_black, king_white,queen_black ,queen_white, knight_black, knight_white, rook_black, rook_white, bishop_black, bishop_white =[] , [], [], [], [], [], [], [], [], [], [], []
for i in range(0, 450, 60):
    pawn_black.append((i+20,60+20))
    pawn_white.append((i+20, 360+20))


rook_black.append((0+20,0+20))
rook_black.append((420+20,0+20))
rook_white.append((0+20 , 420+20))
rook_white.append((420+20, 420+20))

bishop_black.append((120+20,0+20))
bishop_black.append((300+20,0+20))
bishop_white.append((120+20 , 420+20))
bishop_white.append((300+20, 420+20))

knight_black.append((60+20,0+20))
knight_black.append((360+20,0+20))
knight_white.append((60+20 , 420+20))
knight_white.append((360+20, 420+20))

king_black.append((240+20,0+20))
king_white.append((240+20,420+20))

queen_black.append((180+20 , 0+20))
queen_white.append((180+20, 420+20))



for i in range(00,450,60):
    for j in range(00,450,60):
        positions.append((i+20,j+20))



def pos_update():
    for i in range(len(pawn_black)):
        win.blit(pawn_b, pawn_black[i])
        win.blit(pawn_w, pawn_white[i])
    
    for i in range(len(bishop_white)):
        win.blit(rook_b, rook_black[i])
        win.blit(rook_w, rook_white[i])
        win.blit(knight_b, knight_black[i])
        win.blit(knight_w, knight_white[i])
        win.blit(bishop_b, bishop_black[i])
        win.blit(bishop_w, bishop_white[i])
    
    win.blit(king_b, king_black[0])
    win.blit(king_w, king_white[0])
    win.blit(queen_b, queen_black[0])
    win.blit(queen_w, queen_white[0])

def click(x1,y1, x2,y2):
    
    dist = math.sqrt(math.pow(x1 - (x2+20), 2) + (math.pow(y1 - (y2+20), 2)))
    
    if dist<29 :
        return True
    else :
        return False

def check_click(x,y):
    for i in range(2):
        if(click(x,y,rook_black[i][0], rook_black[i][1])):
            return ("black rook") , rook_black[i]
        if(click(x,y,rook_white[i][0], rook_white[i][1])):
            return("white rook") , rook_white[i]
        if(click(x,y,knight_black[i][0], knight_black[i][1])):
            return("black knight"), knight_black[i]
        if(click(x,y,knight_white[i][0], knight_white[i][1])):
            return("white knight"), knight_white[i]
        if(click(x,y,bishop_black[i][0], bishop_black[i][1])):
            return("black bishop"), bishop_black[i]
        if(click(x,y,bishop_white[i][0], bishop_white[i][1])):
            return("white bishop"), bishop_white[i]
                
    for i in range(8):
        if(click(x,y,pawn_black[i][0], pawn_black[i][1])): 
            return ("black pawn"), pawn_black[i]
        if(click(x,y,pawn_white[i][0], pawn_white[i][1])): 
            return ("white pawn"), pawn_white[i]
                
    if(click(x,y,king_black[0][0], king_black[0][1])): 
        return ("black king"), king_black[0]
    if(click(x,y,king_white[0][0], king_white[0][1])): 
        return ("white king"),king_white[0]
    if(click(x,y,queen_black[0][0], queen_black[0][1])): 
        return ("black queen"), queen_black[0]
    if(click(x,y,queen_white[0][0], queen_white[0][1])): 
        return ("white queen"), queen_white[0]

def check_empty_space(x,y):
    for i in range(8):
        if(pawn_black[i] == (x,y)):
            print("yes1")
            return False
        if(pawn_white[i] == (x,y)):
            
            return False
        
    print("k")
    for i in range(2):
        print("k")
        if(bishop_black[i] == (x,y)):
            print("yes3")
            return False
        if(bishop_white[i] == (x,y)):
            print("yes4")
            return False
        if(rook_black[i] == (x,y)):
            print("yes5")
            return False
        if(rook_white[i] == (x,y)):
            print("yes6")
            return False
        if(knight_black[i] == (x,y)):
            print("yes7")
            return False
        if(knight_white[i] == (x,y)):
            print("yes8")
            return False
        
    if king_black[0] == (x,y) :
        print("yes9")
        return False
    if king_white[0] == (x,y):
        print("yes10")
        return False
    if queen_black[0] == (x,y):
        print("yes11")
        return False
    if queen_white[0] == (x,y):
        print("yes12")
        return False
    
    return True



def handle_movement(s,pos):

    s1, s2= s.split(" ", 2)
    if(s1 == "white"):
        if (s2== "pawn"):
            for i in range(pos[0]-60 , 0+20, 60):
                if check_empty_space(i, pos[1]):
                    pass
                else:
                    print("yes")
                    win.blit(mark, (i,pos[1]))
            for i in range(pos[0]+60 , 420+20, 60):
                if check_empty_space(i, pos[1]):
                    pass
                else:
                    
                    win.blit(mark, (i,pos[1]))
            for i in range(pos[1]-60 , 0+20, 60):
                if check_empty_space(pos[0], i):
                    pass
                else:
                    
                    win.blit(mark, (pos[0], i))
            
            for i in range(pos[1]+60 , 420+20, 60):
                if check_empty_space(pos[0], i):
                    pass
                else:
                    
                    win.blit(mark, (pos[0], i))
        


        if (s2== "knight"):
            pass
        if (s2== "bishop"):
            pass
        if (s2== "king"):
            pass
        if (s2== "queen"):
            pass
        if (s2== "pawn"):
            pass

    if(s1 == "black"):
        if (s2== "rook"):
            pass
        if (s2== "knight"):
            pass
        if (s2== "bishop"):
            pass
        if (s2== "king"):
            pass
        if (s2== "queen"):
            pass
        if (s2== "pawn"):
            pass
    pass
    

    



def main():
    run= True
    clicked_one = False


    while run:
        win.blit(background, (0,0))
        pos_update()

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run= False
            
            if events.type == pygame.MOUSEBUTTONUP:
                x, y = events.pos
                piece, peice_pos = check_click(x,y)
                clicked_one=True
        
        if clicked_one :
            handle_movement(piece, peice_pos)
                
            
                

            


        pygame.display.update()


main()