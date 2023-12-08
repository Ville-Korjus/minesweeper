import pygame
import random
from sys import exit

class App:
    def clickEmptySlot(self, row, column):
        self.needToCheck.append((row,column))
        self.checkSurroundingSlots()
        for zeroSlot in self.needToCheck:
            self.clickedList[zeroSlot[0]][zeroSlot[1]] = 1
            coordinate = (10 + 30*zeroSlot[1], 10 + 30*zeroSlot[0])
            self.screen.blit(self.clickedColorBox, coordinate)
        self.needToCheck = []
        
    def solvePartTwo(self):
        # click random empty non flagged slot around chosen best slot
        clickedRandom = False
        while clickedRandom == False:
            randomSlot = random.randrange(8)
            match randomSlot:
                case 0:
                    # top left
                    if self.bestChanceCoords[1] != 0 and self.bestChanceCoords[0] != 0:
                        if self.clickedList[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1] - 1] == 0 and self.flagList[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1] - 1] == 0:
                            clickedRandom = True
                            if self.minefield2d[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1] - 1] == -1:
                                self.lossEvent(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1] - 1)
                            elif self.minefield2d[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1] - 1] == 0:
                                self.clickEmptySlot(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1] - 1)
                            else:
                                self.clickSlot(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1] - 1)
                case 1:
                    # top
                    if self.bestChanceCoords[0] != 0:
                        if self.clickedList[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1]] == 0 and self.flagList[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1]] == 0:
                            clickedRandom = True
                            if self.minefield2d[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1]] == -1:
                                self.lossEvent(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1])
                            elif self.minefield2d[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1]] == 0:
                                self.clickEmptySlot(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1])
                            else:
                                self.clickSlot(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1])
                case 2:
                    # top right
                    if self.bestChanceCoords[1] != self.columns - 1 and self.bestChanceCoords[0] != 0:
                        if self.clickedList[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1] + 1] == 0 and self.flagList[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1] + 1] == 0:
                            clickedRandom = True
                            if self.minefield2d[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1] + 1] == -1:
                                self.lossEvent(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1] + 1)
                            elif self.minefield2d[self.bestChanceCoords[0] - 1][self.bestChanceCoords[1] + 1] == 0:
                                self.clickEmptySlot(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1] + 1)
                            else:
                                self.clickSlot(self.bestChanceCoords[0] - 1, self.bestChanceCoords[1] + 1)
                case 3:
                    # bottom left
                    if self.bestChanceCoords[1] != 0 and self.bestChanceCoords[0] != self.rows - 1:
                        if self.clickedList[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1] - 1] == 0 and self.flagList[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1] - 1] == 0:
                            clickedRandom = True
                            if self.minefield2d[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1] - 1] == -1:
                                self.lossEvent(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1] - 1)
                            elif self.minefield2d[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1] - 1] == 0:
                                self.clickEmptySlot(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1] - 1)
                            else:
                                self.clickSlot(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1] - 1)
                case 4:
                    # bottom
                    if self.bestChanceCoords[0] != self.rows - 1:
                        if self.clickedList[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1]] == 0 and self.flagList[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1]] == 0:
                            clickedRandom = True
                            if self.minefield2d[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1]] == -1:
                                self.lossEvent(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1])
                            elif self.minefield2d[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1]] == 0:
                                self.clickEmptySlot(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1])
                            else:
                                self.clickSlot(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1])
                case 5:
                    # bottom right
                    if self.bestChanceCoords[1] != self.columns - 1 and self.bestChanceCoords[0] != self.rows - 1:
                        if self.clickedList[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1] + 1] == 0 and self.flagList[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1] + 1] == 0:
                            clickedRandom = True
                            if self.minefield2d[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1] + 1] == -1:
                                self.lossEvent(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1] + 1)
                            elif self.minefield2d[self.bestChanceCoords[0] + 1][self.bestChanceCoords[1] + 1] == 0:
                                self.clickEmptySlot(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1] + 1)
                            else:
                                self.clickSlot(self.bestChanceCoords[0] + 1, self.bestChanceCoords[1] + 1)
                case 6:
                    # left
                    if self.bestChanceCoords[1] != 0:
                        if self.clickedList[self.bestChanceCoords[0]][self.bestChanceCoords[1] - 1] == 0 and self.flagList[self.bestChanceCoords[0]][self.bestChanceCoords[1] - 1] == 0:
                            clickedRandom = True
                            if self.minefield2d[self.bestChanceCoords[0]][self.bestChanceCoords[1] - 1] == -1:
                                self.lossEvent(self.bestChanceCoords[0], self.bestChanceCoords[1] - 1)
                            elif self.minefield2d[self.bestChanceCoords[0]][self.bestChanceCoords[1] - 1] == 0:
                                self.clickEmptySlot(self.bestChanceCoords[0], self.bestChanceCoords[1] - 1)
                            else:
                                self.clickSlot(self.bestChanceCoords[0], self.bestChanceCoords[1] - 1)
                case 7:
                    # right
                    if self.bestChanceCoords[1] != self.columns - 1:
                        if self.clickedList[self.bestChanceCoords[0]][self.bestChanceCoords[1] + 1] == 0 and self.flagList[self.bestChanceCoords[0]][self.bestChanceCoords[1] + 1] == 0:
                            clickedRandom = True
                            if self.minefield2d[self.bestChanceCoords[0]][self.bestChanceCoords[1] + 1] == -1:
                                self.lossEvent(self.bestChanceCoords[0], self.bestChanceCoords[1] + 1)
                            elif self.minefield2d[self.bestChanceCoords[0]][self.bestChanceCoords[1] + 1] == 0:
                                self.clickEmptySlot(self.bestChanceCoords[0], self.bestChanceCoords[1] + 1)
                            else:
                                self.clickSlot(self.bestChanceCoords[0], self.bestChanceCoords[1] + 1)
        self.solvePartOne()
                    
    def coverContinueButton(self):
        self.screen.blit(self.bigCover,(10, self.rows * 30 + 15))
        self.continueButton = 0
    
    def solvePartOne(self):# do 100% success chance plays
        # remove player placed flags
        for row in range(self.rows):
            for column in range(self.columns):
                if self.flagList[row][column] == 1:
                    self.flagList[row][column] = 0
                    self.minesLeftInt += 1
        self.somethingChanced = True
        while self.somethingChanced:
            self.somethingChanced = False
            for row in range(self.rows):
                for column in range(self.columns):
                    # check every slot for a clicked slot and not a 0
                    if self.clickedList[row][column] == 1 and self.minefield2d[row][column] != 0:
                        # add empty slots around found slot into emptySlots
                        emptySlots = []
                        # check top
                        if row != 0:
                            if self.clickedList[row - 1][column] == 0:
                                emptySlots.append((row - 1, column))
                            # check top left
                            if column != 0:
                                if self.clickedList[row - 1][column - 1] == 0:
                                    emptySlots.append((row - 1, column - 1))
                            # check top right
                            if column != self.columns - 1:
                                if self.clickedList[row - 1][column + 1] == 0:
                                    emptySlots.append((row - 1, column + 1))
                        # check bottom
                        if row != self.rows - 1:
                            if self.clickedList[row + 1][column] == 0:
                                emptySlots.append((row + 1, column))
                            # check bottom left
                            if column != 0:
                                if self.clickedList[row + 1][column - 1] == 0:
                                    emptySlots.append((row + 1, column - 1))
                            # check bottom right
                            if column != self.columns - 1:
                                if self.clickedList[row + 1][column + 1] == 0:
                                    emptySlots.append((row + 1, column + 1))
                        # check left
                        if column != 0:
                            if self.clickedList[row][column - 1] == 0:
                                emptySlots.append((row, column - 1))
                        # check right
                        if column != self.columns - 1:
                            if self.clickedList[row][column + 1] == 0:
                                emptySlots.append((row, column + 1))
                        
                        # if there are the same ammount of emplty slots as there should be bombs flag all empty slots
                        if self.minefield2d[row][column] == len(emptySlots):
                            for slot in emptySlots:
                                if self.flagList[slot[0]][slot[1]] == 0 and self.lockAll == False:
                                    self.minesLeftInt -= 1
                                    self.flagList[slot[0]][slot[1]] = 1
                                    self.screen.blit(self.flagImage,self.buttonCoords[slot[0]][slot[1]])
            for row in range(self.rows):
                for column in range(self.columns):
                    # check every slot for a clicked slot and not a 0
                    if self.clickedList[row][column] == 1 and self.minefield2d[row][column] != 0:
                        # add ammount of flags to flagSlots
                        flagSlots = 0
                        # check top
                        if row != 0:
                            if self.flagList[row - 1][column] == 1:
                                flagSlots += 1
                            # check top left
                            if column != 0:
                                if self.flagList[row - 1][column - 1] == 1:
                                    flagSlots += 1
                            # check top right
                            if column != self.columns - 1:
                                if self.flagList[row - 1][column + 1] == 1:
                                    flagSlots += 1
                        # check bottom
                        if row != self.rows - 1:
                            if self.flagList[row + 1][column] == 1:
                                flagSlots += 1
                            # check bottom left
                            if column != 0:
                                if self.flagList[row + 1][column - 1] == 1:
                                    flagSlots += 1
                            # check bottom right
                            if column != self.columns - 1:
                                if self.flagList[row + 1][column + 1] == 1:
                                    flagSlots += 1
                        # check left
                        if column != 0:
                            if self.flagList[row][column - 1] == 1:
                                flagSlots += 1
                        # check right
                        if column != self.columns - 1:
                            if self.flagList[row][column + 1] == 1:
                                flagSlots += 1
                        
                        # if there is the same ammount of flags around a given slot click every non flag slot
                        if self.minefield2d[row][column] == flagSlots:
                            # check top
                            if row != 0:
                                if self.flagList[row - 1][column] == 0 and self.clickedList[row - 1][column] == 0:
                                    if self.minefield2d[row - 1][column] == 0:
                                        self.clickEmptySlot(row - 1, column)
                                    else:
                                        self.clickSlot(row - 1,column)
                                # check top left
                                if column != 0:
                                    if self.flagList[row - 1][column - 1] == 0 and self.clickedList[row - 1][column - 1] == 0:
                                        if self.minefield2d[row - 1][column - 1] == 0:
                                            self.clickEmptySlot(row - 1, column - 1)
                                        else:
                                            self.clickSlot(row - 1, column - 1)
                                # check top right
                                if column != self.columns - 1:
                                    if self.flagList[row - 1][column + 1] == 0 and self.clickedList[row - 1][column + 1] == 0:
                                        if self.minefield2d[row - 1][column + 1] == 0:
                                            self.clickEmptySlot(row - 1, column + 1)
                                        else:
                                            self.clickSlot(row - 1, column + 1)
                            # check bottom
                            if row != self.rows - 1:
                                if self.flagList[row + 1][column] == 0 and self.clickedList[row + 1][column] == 0:
                                    if self.minefield2d[row + 1][column] == 0:
                                        self.clickEmptySlot(row + 1, column)
                                    else:
                                        self.clickSlot(row + 1, column)
                                # check bottom left
                                if column != 0:
                                    if self.flagList[row + 1][column - 1] == 0 and self.clickedList[row + 1][column - 1] == 0:
                                        if self.minefield2d[row + 1][column - 1] == 0:
                                            self.clickEmptySlot(row + 1, column - 1)
                                        else:
                                            self.clickSlot(row + 1, column - 1)
                                # check bottom right
                                if column != self.columns - 1:
                                    if self.flagList[row + 1][column + 1] == 0 and self.clickedList[row + 1][column + 1] == 0:
                                        if self.minefield2d[row + 1][column + 1] == 0:
                                            self.clickEmptySlot(row + 1, column + 1)
                                        else:
                                            self.clickSlot(row + 1, column + 1)
                            # check left
                            if column != 0:
                                if self.flagList[row][column - 1] == 0 and self.clickedList[row][column - 1] == 0:
                                    if self.minefield2d[row][column - 1] == 0:
                                        self.clickEmptySlot(row, column - 1)
                                    else:
                                        self.clickSlot(row, column - 1)
                            # check right
                            if column != self.columns - 1:
                                if self.flagList[row][column + 1] == 0 and self.clickedList[row][column + 1] == 0:
                                    if self.minefield2d[row][column + 1] == 0:
                                        self.clickEmptySlot(row, column + 1)
                                    else:
                                        self.clickSlot(row, column + 1)
            self.checkWin()
            # click unclicked slot if all mines are flagged
            if self.somethingChanced == False and self.minesLeftInt == 0 and self.lockAll == False:
                for row in range(self.rows):
                    for column in range(self.columns):
                        if self.clickedList[row][column] == 0 and self.flagList[row][column] == 0:
                            self.clickSlot(row, column)
            self.checkWin()
        #if game didnt end
        if self.lockAll == False:
            self.bestChance = 0
        # check every slot for a clicked slot
        for row in range(self.rows):
            for column in range(self.columns):
                if self.clickedList[row][column] == 1 and self.minefield2d[row][column] != 0:
                    # add empty slots around found slot into emptySlots and flags into flags
                    emptySlots = 0
                    flags = 0
                    # check top
                    if row != 0:
                        if self.clickedList[row - 1][column] == 0:
                            emptySlots += 1
                        if self.flagList[row - 1][column] == 1:
                            flags += 1
                        # check top left
                        if column != 0:
                            if self.clickedList[row - 1][column - 1] == 0:
                                emptySlots += 1
                            if self.flagList[row - 1][column - 1] == 1:
                                flags += 1
                        # check top right
                        if column != self.columns - 1:
                            if self.clickedList[row - 1][column + 1] == 0:
                                emptySlots += 1
                            if self.flagList[row - 1][column + 1] == 1:
                                flags += 1
                    # check bottom
                    if row != self.rows - 1:
                        if self.clickedList[row + 1][column] == 0:
                            emptySlots += 1
                        if self.flagList[row + 1][column] == 1:
                            flags += 1
                        # check bottom left
                        if column != 0:
                            if self.clickedList[row + 1][column - 1] == 0:
                                emptySlots += 1
                            if self.flagList[row + 1][column - 1] == 1:
                                flags += 1
                        # check bottom right
                        if column != self.columns - 1:
                            if self.clickedList[row + 1][column + 1] == 0:
                                emptySlots += 1
                            if self.flagList[row + 1][column + 1] == 1:
                                flags += 1
                    # check left
                    if column != 0:
                        if self.clickedList[row][column - 1] == 0:
                            emptySlots += 1
                        if self.flagList[row][column - 1] == 1:
                            flags += 1
                    # check right
                    if column != self.columns - 1:
                        if self.clickedList[row][column + 1] == 0:
                            emptySlots += 1
                        if self.flagList[row][column + 1] == 1:
                            flags += 1
                    # if slot only has flagged empty slots
                    if emptySlots - flags > 0:
                        # if this slots chance of succeeding is higher then the last checked same this slot as best one
                        succeedChance = (1 - (self.minefield2d[row][column] - flags) / (emptySlots - flags)) * 100
                        if succeedChance > self.bestChance:
                            self.bestChance = round(succeedChance)
                            self.bestChanceCoords = (row, column)
        # step bro stuck in a corner with a mine
        if self.bestChance == 0:
            for row in range(self.rows):
                for column in range(self.columns):
                    if self.clickedList[row][row] == 0 and self.minefield2d[row][column] != -1:
                        self.clickSlot(row, column)
            
        # show chance of next bot move if game didnt end
        if self.lockAll == False:
            
            self.screen.blit(self.bigCover,(25 + 30 * self.columns,305))
            
            self.bestChanceText = self.smallFont.render('Winning',False,self.textColor)
            self.screen.blit(self.bestChanceText,((25 + 30 * self.columns) + self.gap,305))
            
            lossChanceText = self.smallFont.render('Losing',False,self.lossColor)
            self.screen.blit(lossChanceText,((130 + 30 * self.columns) + self.gap,305))
            
            winningChance = self.font.render(f'{self.bestChance}%',False,self.textColor)
            self.screen.blit(winningChance,((30 + 30 * self.columns) + self.gap,330))
            
            middleDevider = self.font.render('|',False,self.clickedBgColor)
            self.screen.blit(middleDevider,((100 + 30 * self.columns) + self.gap,330))
            
            losingChance = self.font.render(f'{100 - self.bestChance}%',False,self.lossColor)
            self.screen.blit(losingChance,((135 + 30 * self.columns) + self.gap,330))
        
            self.continueSmallText1 = self.smallFont.render('continue auto solve',False,self.textColor)
            self.continueSmallText2 = self.smallFont.render('even if you could lose',False,self.textColor)
            self.continueText = self.font.render('Continue',False,self.textColor)
            self.continueButton = pygame.Rect(220, self.rows * 30 + 15, 180, 50)
            self.screen.blit(self.buttonColorBox,(220, self.rows * 30 + 15))
            self.screen.blit(self.continueText,(245, self.rows * 30 + 28))
            self.screen.blit(self.continueSmallText1,(10, self.rows * 30 + 15))
            self.screen.blit(self.continueSmallText2,(10, self.rows * 30 + 35))
                            
    def lossEvent(self, clickedRow, clickedColumn):
        # lock board and draw LOSS on the screen
        self.lockAll = True
        self.outcomeText = self.bigFont.render('LOSS',False,self.lossColor)
        self.screen.blit(self.outcomeText,((30 + 30 * self.columns) + self.gap,220))
        for row in range(self.rows):
            for column in range(self.columns):
                # if slot hasnt been clicked          and hasnt been flagged
                if self.clickedList[row][column] == 0 and self.flagList[row][column] == 0:
                    # draw red box and its numner or mine in the slot
                    self.screen.blit(self.lossColorBox,self.buttonCoords[row][column])
                    if self.minefield2d[row][column] == -1:
                        self.screen.blit(self.textList[row][column],self.buttonCoords[row][column])
                    else:
                        self.screen.blit(self.textList[row][column],self.textCoords[row][column])
                # if slot is flagged and is a bomb draw clicked color box and mine
                if self.flagList[row][column] == 1 and self.minefield2d[row][column] == -1:
                    self.screen.blit(self.clickedColorBox,self.buttonCoords[row][column])
                    self.screen.blit(self.textList[row][column],self.buttonCoords[row][column])
                # if slot is flagged and isnt a bomb draw loss color box and its number
                elif self.flagList[row][column] == 1 and self.minefield2d[row][column] != -1:
                    self.screen.blit(self.lossColorBox,self.buttonCoords[row][column])
                    self.screen.blit(self.textList[row][column],self.textCoords[row][column])
        # put expliding mine sprite on clicked mine
        self.screen.blit(self.mineExploding,self.buttonCoords[clickedRow][clickedColumn])
        # show if used solvebot
        if self.bestChance != None:
            outcomeChanceText = self.smallFont.render('chance on last click:',False,self.clickedBgColor)
            self.screen.blit(outcomeChanceText,((15 + 30 * self.columns) + self.gap,280))
            
            self.bestChanceText = self.smallFont.render('Winning',False,self.textColor)
            self.screen.blit(self.bestChanceText,((25 + 30 * self.columns) + self.gap,305))
            
            lossChanceText = self.smallFont.render('Losing',False,self.lossColor)
            self.screen.blit(lossChanceText,((130 + 30 * self.columns) + self.gap,305))
            
            winningChance = self.font.render(f'{self.bestChance}%',False,self.textColor)
            self.screen.blit(winningChance,((30 + 30 * self.columns) + self.gap,330))
            
            middleDevider = self.font.render('|',False,self.clickedBgColor)
            self.screen.blit(middleDevider,((100 + 30 * self.columns) + self.gap,330))
            
            losingChance = self.font.render(f'{100 - self.bestChance}%',False,self.lossColor)
            self.screen.blit(losingChance,((135 + 30 * self.columns) + self.gap,330))
    
    def checkWin(self):
        # if there is a number slot that isnt clicked return nothing else lock all slots and draw WIN on screen
        for row in range(self.rows):
            for column in range(self.columns):
                if self.minefield2d[row][column] >= 0:
                    if self.clickedList[row][column] == 0:
                        return
        # flag every mines slot
        for row in range(self.rows):
            for column in range(self.columns):
                if self.minefield2d[row][column] == -1 and self.flagList[row][column] == 0:
                    self.screen.blit(self.flagImage,self.buttonCoords[row][column])
        self.screen.blit(self.bigCover,(25 + 30 * self.columns,305))
        self.lockAll = True
        self.outcomeText = self.bigFont.render('WIN',False,self.textColor)
        self.screen.blit(self.outcomeText,((60 + 30 * self.columns) + self.gap,220))
        self.minesLeftInt = 0
        
    def clickSlot(self, row, column):
        self.somethingChanced = True
        # draws clicked slots number on screen and makes the box lighter and adds it to clicked list so it cant be clicked again
        self.clickedList[row][column] = 1
        self.screen.blit(self.clickedColorBox,self.buttonCoords[row][column])
        self.screen.blit(self.textList[row][column],self.textCoords[row][column])
        
    def checkSurroundingSlots(self, coordinate=None):

        if coordinate == None: coordinate = self.needToCheck[0]

        x = coordinate[1]
        y = coordinate[0]

        # Searching Left
        if x - 1 >= 0 and (y, x - 1) not in self.needToCheck:
            if self.minefield2d[y][x - 1] == 0:
                self.needToCheck.append((y, x - 1))
                self.checkSurroundingSlots((y, x - 1))
            else:
                self.clickSlot(y,x-1)
                try:
                    # if not top row
                    if y != 0:
                        # search top left
                        if self.minefield2d[y][x-1] > 0 and self.minefield2d[y-1][x] > 0 and self.minefield2d[y-1][x-1] == 0 and (y - 1, x - 1) not in self.needToCheck:
                            self.needToCheck.append((y - 1, x - 1))
                            self.checkSurroundingSlots((y - 1, x - 1))
                        else:
                            self.clickSlot(y-1,x-1)
                    # if not bottom row
                    if y != self.rows:
                        # search bottom left
                        if self.minefield2d[y][x-1] > 0 and self.minefield2d[y+1][x] > 0 and self.minefield2d[y+1][x-1] == 0 and (y + 1, x - 1) not in self.needToCheck:
                            self.needToCheck.append((y + 1, x - 1))
                            self.checkSurroundingSlots((y + 1, x - 1))
                        else:
                            self.clickSlot(y+1,x-1)
                except: pass

        # Searching Right
        if x + 1 < self.columns and (y, x + 1) not in self.needToCheck:
            if self.minefield2d[y][x + 1] == 0:
                self.needToCheck.append((y, x + 1))
                self.checkSurroundingSlots((y, x + 1))
            else:
                self.clickSlot(y,x+1)
                try:
                    # if not top row
                    if y != 0:
                        # search top right
                        if self.minefield2d[y][x+1] > 0 and self.minefield2d[y-1][x] > 0 and self.minefield2d[y-1][x+1] == 0 and (y - 1, x + 1) not in self.needToCheck:
                            self.needToCheck.append((y - 1, x + 1))
                            self.checkSurroundingSlots((y - 1, x + 1))
                        else:
                            self.clickSlot(y-1,x+1)
                    # if not buttom row
                    if y != self.rows:
                        # search buttom right
                        if self.minefield2d[y][x+1] > 0 and self.minefield2d[y+1][x] > 0 and self.minefield2d[y+1][x+1] == 0 and (y + 1, x + 1) not in self.needToCheck:
                            self.needToCheck.append((y + 1, x + 1))
                            self.checkSurroundingSlots((y + 1, x + 1))
                        else:
                            self.clickSlot(y+1,x+1)
                except: pass

        # Searching Up
        if y - 1 >= 0 and (y - 1, x) not in self.needToCheck:
            if self.minefield2d[y - 1][x] == 0:
                self.needToCheck.append((y - 1, x))
                self.checkSurroundingSlots((y - 1, x))
            else:
                self.clickSlot(y-1,x)

        # Searching Down
        if y + 1 < self.rows and (y + 1, x) not in self.needToCheck:
            if self.minefield2d[y + 1][x] == 0:
                self.needToCheck.append((y + 1, x))
                self.checkSurroundingSlots((y + 1, x))
            else:
                self.clickSlot(y+1,x)
                
    def surroundingMines(self, coords):
        row = coords[0]
        column = coords[1]
        mines = 0
        
        if self.minefield2d[row][column] == -1: return -1
        
        if row == 0 or row < len(self.minefield2d) - 1: # Bottom cell
            if self.minefield2d[row+1][column] == -1: mines += 1

        if row == len(self.minefield2d) - 1 or row > 0: # Top cell
            if self.minefield2d[row-1][column] == -1: mines += 1

        if column == 0 or column < len(self.minefield2d[row]) - 1: # Right cell
            if self.minefield2d[row][column+1] == -1: mines += 1

        if column == len(self.minefield2d[row]) - 1 or column > 0: # Left cell
            if self.minefield2d[row][column-1] == -1: mines += 1

        # Checks for corners
        if column < len(self.minefield2d[row]) - 1 and row > 0: # Top Right
            if self.minefield2d[row-1][column+1] == -1: mines += 1
        if column > 0 and row > 0: # Top Left
            if self.minefield2d[row-1][column-1] == -1: mines += 1
        if column < len(self.minefield2d[row]) - 1 and row < len(self.minefield2d) - 1: # Bottom Right
            if self.minefield2d[row+1][column+1] == -1: mines += 1
        if column > 0 and row < len(self.minefield2d) - 1: # Bottom Left
            if self.minefield2d[row+1][column-1] == -1: mines += 1

        return mines
        
    def return2dCoords(self, randomSlot):
        count = 0
        for row in range(0, self.rows):
            for column in range(0, self.columns):
                if count == randomSlot:
                    return row, column
                count += 1
    
    def createMines(self):
        # avalible slots to place mines
        self.availableSlots = [slot for slot in range(self.rows * self.columns)]
        
        # make middle slots empty to start the play
        if self.rows % 2 == 0:
            self.middleSlot = self.rows * self.columns / 2 - (self.columns / 2).__ceil__()
        else:
            self.middleSlot = round(self.rows * self.columns / 2)
                
        self.availableSlots.remove(self.middleSlot - 1 - self.columns)
        self.availableSlots.remove(self.middleSlot - self.columns)
        self.availableSlots.remove(self.middleSlot + 1 - self.columns)
        
        self.availableSlots.remove(self.middleSlot - 1)
        self.availableSlots.remove(self.middleSlot)
        self.availableSlots.remove(self.middleSlot + 1)
        
        self.availableSlots.remove(self.middleSlot - 1 + self.columns)
        self.availableSlots.remove(self.middleSlot + self.columns)
        self.availableSlots.remove(self.middleSlot + 1 + self.columns)
        
        # place mines
        for _ in range(self.mines):
            randomSlot = random.choice(self.availableSlots)
            self.availableSlots.remove(randomSlot)
            randomRow, randomColumn = self.return2dCoords(randomSlot)

            self.minefield2d[randomRow][randomColumn] = -1
        
        # Count surrounding mines
        for row in range(self.rows):
            for column in range(self.columns):
                coords = (row, column)
                mines = self.surroundingMines(coords)
                self.minefield2d[row][column] = mines
                if mines > 0:
                    self.textList[row][column] = self.smallFont.render(str(mines),False,self.textColor)
                elif mines == -1:
                    self.textList[row][column] = pygame.image.load('./images/mine.png')
                else:
                    self.textList[row][column] = self.smallFont.render('',False,self.textColor)
                    self.screen.blit(self.clickedColorBox,self.buttonCoords[row][column])
        
    def startGame(self):
        while True:
            for event in pygame.event.get():
                # close game event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # left click menu events
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.gameActive == False:
                    # easy button event
                    if self.easyButton.collidepoint(event.pos):
                        self.setupBoard(7,10)
                    # hard button event
                    elif self.hardButton.collidepoint(event.pos):
                        self.setupBoard(10,15)
                    # gl button event
                    elif self.glButton.collidepoint(event.pos):
                        self.setupBoard(25,50)
                    # custom button event
                    elif self.customButton.collidepoint(event.pos):
                        self.setupBoard(self.customWidth,self.customHeight)
                    # custom height increase button event
                    elif self.customXPlusButton.collidepoint(event.pos):
                        self.customHeight += 1
                        self.customXText = self.font.render(str(self.customHeight),False,self.textColor)
                    # custom height decrease button event (min is 5)
                    elif self.customXMinusButton.collidepoint(event.pos):
                        if self.customHeight > 5: self.customHeight -= 1
                        self.customXText = self.font.render(str(self.customHeight),False,self.textColor)
                    # custom width increase button event
                    elif self.customYPlusButton.collidepoint(event.pos):
                        self.customWidth += 1
                        self.customYText = self.font.render(str(self.customWidth),False,self.textColor)
                    # custom width decrease button event (min is 5)
                    elif self.customYMinusButton.collidepoint(event.pos):
                        if self.customWidth > 5: self.customWidth -= 1
                        self.customYText = self.font.render(str(self.customWidth),False,self.textColor)
                # left click game events
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1  and self.gameActive == True:
                    for row in range(self.rows):
                        for column in range(self.columns):
                            # click slot event
                            # if clicked button pos                                 and is not flagged                  and board isnt locked     and slot isnt clicked already
                            if self.buttonList[row][column].collidepoint(event.pos) and self.flagList[row][column] == 0 and self.lockAll == False and self.clickedList[row][column] == 0:
                                self.coverContinueButton()
                                # if clicked mine
                                if self.minefield2d[row][column] == -1:
                                    self.lossEvent(row,column)
                                # if clicked empty slot
                                elif self.minefield2d[row][column] == 0:
                                    self.clickEmptySlot(row, column)
                                # if clicked number
                                else:
                                    self.clickSlot(row,column)
                                self.checkWin()
                    # restart button event
                    if self.restartButton.collidepoint(event.pos):
                        self.once = False
                        self.setupBoard(self.rows,self.columns)
                        for row in range(self.rows):
                            for column in range(self.columns):
                                self.screen.blit(self.smallColorBox,self.buttonCoords[row][column])
                    # menu button event
                    elif self.menuButton.collidepoint(event.pos):
                        self.once = False
                        self.gameActive = False
                        self.screen = pygame.display.set_mode((400,400))
                    # solve button event
                    elif self.solveButton.collidepoint(event.pos) and self.lockAll == False:
                        self.solvePartOne()
                    try:
                        # continue button event
                        if self.continueButton.collidepoint(event.pos):
                            self.coverContinueButton()
                            self.solvePartTwo()
                    except: pass
                # right click game events
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3  and self.gameActive == True:
                    for row in range(self.rows):
                        for column in range(self.columns):
                            # if clicked button pos                                 and board isnt locked     and slot isnt clicked already
                            if self.buttonList[row][column].collidepoint(event.pos) and self.lockAll == False and self.clickedList[row][column] == 0:
                                # flags slot
                                if self.flagList[row][column] == 0:
                                    self.minesLeftInt -= 1
                                    self.flagList[row][column] = 1
                                    self.screen.blit(self.flagImage,self.buttonCoords[row][column])
                                # unflags slot
                                else:
                                    self.minesLeftInt += 1
                                    self.flagList[row][column] = 0
                                    self.screen.blit(self.smallColorBox,self.buttonCoords[row][column])
            # update mines left list
            self.minesLeft = self.smallFont.render(f'{self.minesLeftInt}',False,self.textColor)
            # draws game
            if self.gameActive:
                # draws background grey boxes once
                if self.once == False:
                    for row in range(self.rows):
                        for column in range(self.columns):
                            self.screen.blit(self.smallColorBox,self.buttonCoords[row][column])
                    self.once = True
                    # clicks middle empty slot to give a better start to the player
                    self.needToCheck.append(self.return2dCoords(self.middleSlot))
                    self.checkSurroundingSlots()
                    for zeroSlot in self.needToCheck:
                        self.clickedList[zeroSlot[0]][zeroSlot[1]] = 1
                        coordinate = (10 + 30*zeroSlot[1], 10 + 30*zeroSlot[0])
                        self.screen.blit(self.clickedColorBox, coordinate)
                    self.needToCheck = []
                # draws buttons on the right side of the game board
                self.screen.blit(self.buttonColorBox,((15 + 30 * self.columns) + self.gap,10))
                self.screen.blit(self.restartText,((45 + 30 * self.columns) + self.gap,24))
                self.screen.blit(self.buttonColorBox,((15 + 30 * self.columns) + self.gap,70))
                self.screen.blit(self.menuText,((65 + 30 * self.columns) + self.gap,84))
                self.screen.blit(self.buttonColorBox,((15 + 30 * self.columns) + self.gap,130))
                self.screen.blit(self.solveText,((65 + 30 * self.columns) + self.gap,144))
                self.screen.blit(self.minesLeftText,((30 + 30 * self.columns) + self.gap,190))
                self.screen.blit(self.minesLeftCover,((140 + 30 * self.columns) + self.gap,190))
                self.screen.blit(self.minesLeft,((140 + 30 * self.columns) + self.gap,190))
            else:
                # draw everything in the menu
                self.screen.blit(self.buttonColorBox,(110,20))
                self.screen.blit(self.easyText,(120,30))
                self.screen.blit(self.buttonColorBox,(110,100))
                self.screen.blit(self.hardText,(120,110))
                self.screen.blit(self.buttonColorBox,(110,180))
                self.screen.blit(self.glText,(120,190))
                self.screen.blit(self.buttonColorBox,(40,290))
                self.screen.blit(self.customText,(50,300))
                self.screen.blit(self.customChangeColorBox,(240,260))
                self.screen.blit(self.customPlusText,(252,260))
                self.screen.blit(self.customColorBox,(240,290))
                self.screen.blit(self.customXText,(245,303))
                self.screen.blit(self.customChangeColorBox,(240,343))
                self.screen.blit(self.customMinusText,(252,345))
                self.screen.blit(self.customChangeColorBox,(315,260))
                self.screen.blit(self.customPlusText,(327,260))
                self.screen.blit(self.customColorBox,(315,290))
                self.screen.blit(self.customYText,(320,303))
                self.screen.blit(self.customChangeColorBox,(315,343))
                self.screen.blit(self.customMinusText,(327,345))
                self.screen.blit(self.customTimesText,(290,303))
                
            # update game 60fps
            pygame.display.update()
            self.clock.tick(60)
    
    def setupBoard(self,rows,columns):
        # create variables
        self.rows = rows
        self.columns = columns
        self.everyTime = self.rowWidth = 0
        self.slots = self.rows*self.columns
        self.minefield2d =  [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.buttonList =   [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.buttonCoords = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.textCoords =   [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.textList =     [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.flagList =     [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.clickedList =  [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        
        # create game board
        self.smallColorBox = pygame.Surface((25,25))
        self.smallColorBox.fill(self.buttonBgColor)
        self.clickedColorBox = pygame.Surface((25,25))
        self.clickedColorBox.fill(self.clickedBgColor)
        self.lossColorBox = pygame.Surface((25,25))
        self.lossColorBox.fill(self.lossColor)
        for row in range(self.rows):
            for column in range(self.columns):
                x = 10 + self.everyTime
                y = 10 + self.rowWidth
                self.textCoords[row][column] = x+8,y+5
                self.buttonCoords[row][column] = x,y
                self.everyTime += 30
                if self.everyTime == 30 * self.columns:
                    self.rowWidth += 30
                    self.everyTime = 0
                self.buttonList[row][column] = pygame.Rect(x,y,25,25)
        # set minimum screen width to 
        while (180 + 25 + 30 * self.columns) + self.gap < 600:
            self.gap += 1
        # set minimum screen height to 370
        if 15 + 30 * self.rows < 375:
            self.screen = pygame.display.set_mode(((180 + 25 + 30 * self.columns) + self.gap,375))
        else:
            self.screen = pygame.display.set_mode(((180 + 25 + 30 * self.columns) + self.gap,75 + 30 * self.rows))
        
        self.mines = (self.rows * self.columns * .2).__ceil__()
        self.minesLeftInt = self.mines
        
        # create buttons next to game board
        self.restartText = self.font.render('Restart',False,self.textColor)
        self.restartButton = pygame.Rect((15 + 30 * self.columns) + self.gap,10,180,50)
        
        self.menuText = self.font.render('Menu',False,self.textColor)
        self.menuButton = pygame.Rect((15 + 30 * self.columns) + self.gap,70,180,50)
        
        self.solveText = self.font.render('Solve',False,self.textColor)
        self.solveButton = pygame.Rect((15 + 30 * self.columns) + self.gap,130,180,50)
        
        self.minesLeftText = self.smallFont.render('Mines left:',False,self.textColor)
        self.minesLeft = self.smallFont.render(f'{self.minesLeftInt}',False,self.textColor)
        
        self.createMines()
        for mine in self.minefield2d: # prints minefield xray in the terminal
            print(mine)
        print('\n')
        self.gameActive = True
        self.lockAll = False
        self.needToCheck = []
                
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.display.set_caption('Minesweeper')
        # set variables
        self.screen = pygame.display.set_mode((400,400))
        self.clock = pygame.time.Clock()
        self.buttonBgColor = 'grey25'
        self.clickedBgColor = 'grey35'
        self.textColor = 'forestgreen'
        self.lossColor = 'red4'
        self.bigFont = pygame.font.Font('./fonts/Pixeltype.ttf', 100)
        self.font = pygame.font.Font('./fonts/Pixeltype.ttf', 50)
        self.smallFont = pygame.font.Font('./fonts/Pixeltype.ttf', 30)
        self.flagImage = pygame.image.load('./images/flag.png')
        self.mineExploding = pygame.image.load('./images/mineExploding.png')
        self.gameActive = self.once = self.slotStuck = False
        self.lockAll = True
        self.customWidth = self.customHeight = 10
        self.needToCheck = []
        self.minesLeftInt = self.gap = 0
        
        self.bigCover = pygame.Surface((400,50))
        self.bigCover.fill('black')
        
        # create mines left cover
        self.minesLeftCover = pygame.Surface((50,20))
        self.minesLeftCover.fill('black')

        # create menu buttons
        self.buttonColorBox = pygame.Surface((180,50))
        self.buttonColorBox.fill(self.buttonBgColor)
        
        self.easyText = self.font.render('Easy',False,self.textColor)
        self.easyButton = pygame.Rect(110,20,180,50)

        self.hardText = self.font.render('Hard',False,self.textColor)
        self.hardButton = pygame.Rect(110,100,180,50)

        self.glText = self.font.render('Good Luck',False,self.textColor)
        self.glButton = pygame.Rect(110,180,180,50)
        
        self.customText = self.font.render('Custom',False,self.textColor)
        self.customButton = pygame.Rect(40,290,180,50)
        
        # create custom ammount buttons
        self.customChangeColorBox = pygame.Surface((40,27))
        self.customChangeColorBox.fill(self.buttonBgColor)
        self.customColorBox = pygame.Surface((40,50))
        self.customColorBox.fill(self.buttonBgColor)
        self.customPlusText =  self.font.render('+',False,self.textColor)
        self.customMinusText = self.font.render('-',False,self.textColor)
        self.customTimesText = self.font.render('x',False,self.textColor)
        
        self.customXPlusButton = pygame.Rect(240,260,40,27)
        self.customXText = self.font.render(str(self.customWidth),False,self.textColor)
        self.customXMinusButton = pygame.Rect(240,343,40,27)
        
        self.customYPlusButton = pygame.Rect(315,260,40,27)
        self.customYText = self.font.render(str(self.customHeight),False,self.textColor)
        self.customYMinusButton = pygame.Rect(315,343,40,27)

        # run game loop
        self.startGame()

if __name__ == "__main__":
    app = App()

""" 
| TO NOT DO list
V
a way to hardcode the minefield for testing

| Changes compared to last version
V

ADDED:

REMOVED:

CHANGE:

"""