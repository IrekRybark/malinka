import pygame.mixer

def play(soundFile):

    pygame.mixer.init()
    pygame.mixer.music.load(soundFile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
        
        
        
def main():
    play("../../malinka/media_priv/sounds/scifi057.mp3")
    
    
if __name__ == "__main__":
    main()
