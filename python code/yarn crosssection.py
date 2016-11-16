import scipy.io as sio
import numpy as np
import scipy.misc
import heapq
import sys
import csv
import pygame.font, pygame.event, pygame.draw
import scipy.misc
from scipy import ndimage
from pygame.locals import *

imagefile = "image.csv";
labelfile = "label.csv";
def drawPixelated(A, screen):
    """Draw 30x30 image of input"""
    A = A.ravel()
    A = (255 - A * 255).transpose()
    size = 30 #here check A
    for x in range(size):
        for y in range(size):
            z = x * 30 + y
            c = int(A[z])
            pygame.draw.rect(screen, (c, c, c), (x * 11 + 385, 15 + y * 11, 11, 11))



def calculateImage(background, screen, lineWidth):
    """Crop and resize the input"""

    global changed
    focusSurface = pygame.surfarray.array3d(background)
    focus = abs(1 - focusSurface / 255)
    focus = np.mean(focus, 2)
    x = []
    xaxis = np.sum(focus, axis=1)
    for i, v in enumerate(xaxis):
        if v > 0:
            x.append(i)
            break
    for i, v in enumerate(xaxis[::-1]):
        if v > 0:
            x.append(len(xaxis) - i)
            break

    y = []
    yaxis = np.sum(focus, axis=0)
    for i, v in enumerate(yaxis):
        if v > 0:
            y.append(i)
            break
    for i, v in enumerate(yaxis[::-1]):
        if v > 0:
            y.append(len(yaxis) - i)
            break

    try:
        dx = x[1] - x[0]
        dy = y[1] - y[0]
        bound = focus.shape[0]
        if dx > dy:
            d = dx - dy
            y0t = y[0] - d // 2
            y1t = y[1] + d // 2 + d % 2
            if y0t < 0: y0t = y[0]; y1t = y[1] + d
            if y1t > bound: y0t = y[0] - d; y1t = y[1]
            y[0], y[1] = y0t, y1t
        else:
            d = dy - dx
            x0t = x[0] - d // 2
            x1t = x[1] + d // 2 + d % 2
            if x0t < 0: x0t = x[0]; x1t = x[1] + d
            if x1t > bound: x0t = x[0] - d; x1t = x[1]
            x[0], x[1] = x0t, x1t
        dx = x[1] - x[0]
        dy = y[1] - y[0]
        changed = True
        crop_surf = pygame.Surface((dx, dy))
        crop_surf.blit(background, (0, 0), (x[0], y[0], x[1], y[1]), special_flags=BLEND_RGBA_MAX)
        scaledBackground = pygame.transform.smoothscale(crop_surf, (30, 30))

        image = pygame.surfarray.array3d(scaledBackground)
        image = abs(1 - image / 253)
        image = np.mean(image, 2)
        image = np.matrix(image.ravel())
        drawPixelated(image, screen)
    #     (value, prob), (value2, prob2) = probabilty(Theta1, Theta2, image)
    #     prob = round(prob, 1)
    #     prob2 = round(prob2, 1)
    #
    #     myLabel = showStats(lineWidth, value, prob)
    #     myLabelSmall = showStatsSmall(lineWidth, value2, prob2)
    #     (x, y) = screen.get_size()
    #     screen.blit(myLabel, (17, y - 90))
    #     screen.blit(myLabelSmall, (20, y - 38))
    except:
        image = np.zeros((30, 30))

    return image


def display_box(screen, message):
    "Print a message in a box on the screen"

    fontobject = pygame.font.Font(None, 120)
    pygame.draw.rect(screen, (0, 0, 0),
                     ((screen.get_width() / 2) - 100,
                      (screen.get_height()) - 170,
                      70, 90), 0)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                    ((screen.get_width() / 2) - 110, (screen.get_height()) - 168))
        pygame.display.flip()
def get_key():
    """Get key event"""
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def ask(screen, question):
    """create input box for entering correct value of y"""

    pygame.font.init()
    current_string = str()
    display_box(screen, question + " " + current_string + "")
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string += (chr(inkey))
        display_box(screen, question + " " + current_string + "")
    return current_string


def checkKeys(myData):
    """test for various keyboard inputs"""
    (event, background, drawColor, lineWidth, keepGoing, screen, image) = myData
    if event.key == pygame.K_q: #check image here
        keepGoing = False
    elif event.key == pygame.K_c:
        background.fill((255, 255, 255))
        drawPixelated(np.zeros((30, 30)), screen)
    elif event.key == pygame.K_s:
        global changed
        error = False
        try :
          mat_contents = sio.loadmat('newXorg.mat')
          X = mat_contents['X']
          theta = 10;
          size = 30
          midimage = np.reshape(image, (size, size))

          midimage = np.absolute(midimage*256); # see how to take array as an integer so that space could be saved
          midimage = midimage.astype(int)
          myfile = open(imagefile, 'a', newline='')
          wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
          #plt.figure(figsize=(12.5, 2.5))
          for i in range(0,36) :
              rotate_image = np.absolute(ndimage.rotate(midimage, i*theta,reshape=False))
              s = "Demoimages/myfile " + str(i) + ".jpg";
              scipy.misc.imsave(s, rotate_image)
              rotate_image = np.reshape(rotate_image,(1,900))
              wr.writerow(rotate_image[0])
              X = np.append(X,rotate_image, axis=0)
              #X = np.append(X, image, axis=0)
        except:
            #this is for checking if there is no file still
            error = True
            print("Unexpected error:", sys.exc_info()[0])
            X = image
        answer = np.matrix(int(ask(screen, "")))
        try:
            mat_contents = sio.loadmat('newyorg.mat')
            y = mat_contents['y']
            myfile = open(labelfile, 'a', newline='')
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            for i in range(0,36):
                y = np.append(y, answer, axis=0)
                answer = np.array(answer)
                wr.writerow(answer[0])

        except:
            error = True
            print("Unexpected error:", sys.exc_info()[0])
            y = answer
        if changed:
            sio.savemat('newXorg.mat', {'X': X})
            sio.savemat('newyorg.mat', {'y': y})
            changed = False
        if error :
            myfile = open(imagefile, 'a', newline='')
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            imagew = np.array(image);
            imagew = np.absolute(256*imagew);
            imagew = imagew.astype(int)
            wr.writerow(imagew[0])
            myfile = open(labelfile, 'a', newline='')
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            y2 = np.array(y)
            wr.writerow(y2[0])

        background.fill((255, 255, 255))
        drawPixelated(np.zeros((30, 30)), screen)

    # elif event.key == pygame.K_t:
    #     screen.fill((255, 255, 255))
    #     myFont1 = pygame.font.SysFont("Verdana", 55)
    #     myFont2 = pygame.font.SysFont("Verdana", 17)
    #     myFont3 = pygame.font.SysFont("Verdana", 9)
    #     screen.blit(myFont1.render("Please wait!", 1, ((0, 0, 0))), (365, 90))
    #     screen.blit(myFont2.render("Neural network training in progress...", 1, ((50, 50, 50))), (368, 150))
    #     screen.blit(myFont3.render("Depending on the training data size this could take long time", 1, ((80, 80, 80))),
    #                 (370, 190))
    #     pygame.display.flip()
    #     global Xtrain;
    #     global Xtest;
    #     global ytrain;
    #     global ytest
    #     mat_contents = sio.loadmat('newXorg.mat')
    #     Xs = mat_contents['X']
    #     mat_contents = sio.loadmat('newyorg.mat')
    #     ys = mat_contents['y']
    #     Xtrain, Xtest, ytrain, ytest = splitData(Xs, ys)
    #
    #     rndInit = randomInitialization(25 * 901 + 10 * 26)
    #     answer = sc.fmin_cg(calculateJ, rndInit, calculateGrad, maxiter=100, disp=True, callback=callback)
    #     Theta1 = np.reshape(answer[:num_hidden * (num_input + 1)], (num_hidden, -1))
    #     Theta2 = np.reshape(answer[num_hidden * (num_input + 1):], (num_lables, -1))
    #
    #     acc = returnAccuracy(probabiltyForDrawing(Theta1, Theta2, Xtest), ytest)
    #     sio.savemat('scaledTheta.mat', {'t': answer, 'acc': acc})
    #     screen.fill((0, 0, 0))
    #     background.fill((255, 255, 255))
    # elif event.key == pygame.K_v:
    #     drawStatistics(screen)

    myData = (event, background, drawColor, lineWidth, keepGoing)
    return myData


def main():
    """Main method. Draw interface"""
    global screen
    pygame.init()
    screen = pygame.display.set_mode((730, 450))
    pygame.display.set_caption("Yarn Type recognition")

    background = pygame.Surface((360, 360))
    background.fill((255, 255, 255))
    background2 = pygame.Surface((360, 360))
    background2.fill((255, 255, 255))

    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (255, 0, 0)
    lineWidth = 1

  #  inputTheta = sio.loadmat('scaledTheta.mat')
   # theta = inputTheta['t']
    num_hidden = 25
    num_input = 900
    num_lables = 10

    #Theta1 = np.reshape(theta[:num_hidden * (num_input + 1)], (num_hidden, -1))
    #Theta2 = np.reshape(theta[num_hidden * (num_input + 1):], (num_lables, -1))

    pygame.display.update()
    image = None

    while keepGoing:

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.MOUSEBUTTONUP:
                screen.fill((0, 0, 0))
                screen.blit(background2, (370, 0))
                #w = threading.Thread(name='worker', target=worker)
                image = calculateImage(background, screen, lineWidth)

            elif event.type == pygame.KEYDOWN:
                myData = (event, background, drawColor, lineWidth, keepGoing, screen, image)
                myData = checkKeys(myData) #check image field here
                (event, background, drawColor, lineWidth, keepGoing) = myData

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()