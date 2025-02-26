# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size = (600, 480))
print('Setup End')

print('Loop Start')
while True:
  # Check for all events
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Clocse Window
            quit() # end pygame

