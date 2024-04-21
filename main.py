import pygame.examples.aliens as aliens
aliens.main()
import os

if os.abortname=='__main__':
    print("weicome to robospeaker 1.1.created by harry")
    while True:
        x=input("enter whwt you want me speak:")
        if x=="q":
            os.system("say'bye bye friend'")
            break
        command=f"say{x}"
        os.system(command)