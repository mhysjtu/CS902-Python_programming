import random
from Tkinter import *


class Cards:
    def __init__(self):
        self.cards=[]
        
    def createCards(self):
        for i in range(1,14):
            self.cards.append((i, 'heart'))
            self.cards.append((i, 'clubs'))
            self.cards.append((i, 'diamond'))
            self.cards.append((i, 'spade'))
        return self.cards


class Player:
    def __init__(self, playerID):
        self.id = playerID
        self.hand = []
        
    def addToHand(self,nextcard):
        self.hand.append(nextcard)
        
    def showHand(self):
        print "Player"+self.id+"'s hand is:"
        print self.hand


class Deck:
    def __init__(self,cards):
        self.cards = cards
        
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards
    
    def getNextCard(self, num):
        nextcard = self.cards[num]
        return nextcard


class GUI:
    def __init__(self,p):
        self.num=0
        self.p = p

        self.root = Tk()
        self.root.title("PokerGame")
        self.root.geometry("1400x450")
        
        self.img1=PhotoImage(file="heart.gif")
        self.img2=PhotoImage(file="clubs.gif")
        self.img3=PhotoImage(file="diamonds.gif")
        self.img4=PhotoImage(file="spades.gif")

        Label(self.root,text="Player North").grid(row=0,column=9,sticky=N)
        Label(self.root,text="Player West").grid(row=2,column=4,sticky=N)
        Label(self.root,text="Player South").grid(row=7,column=9,sticky=N)
        Label(self.root,text="Player East").grid(row=2,column=14,sticky=N)
     
        self.f1=Frame(self.root,bd=4,relief="groove")
        self.f1.grid(row=1,column=7,rowspan=2,columnspan=5)
        self.f2=Frame(self.root,bd=4,relief="groove")
        self.f2.grid(row=3,column=2,rowspan=2,columnspan=5)
        self.f3=Frame(self.root,bd=4,relief="groove")
        self.f3.grid(row=5,column=7,rowspan=2,columnspan=5)
        self.f4=Frame(self.root,bd=4,relief="groove")
        self.f4.grid(row=3,column=12,rowspan=2,columnspan=5)

        self.b=Button(self.root,text="Getcard!",command=self.getcard).grid(row=4,column=9)

        self.q=Button(self.root,text="Quit",command=self.close).grid(row=7,column=14)
        
        self.root.mainloop()
        
    def convert(self,p):
        if p=="heart":
            return self.img1
        if p=="clubs":
            return self.img2
        if p=="diamond":
            return self.img3
        if p=="spade":
            return self.img4
        
    def getcard(self):
        self.num=self.num+1
        for j in range(self.num):
            Label(self.f1,image=self.convert(self.p[0].hand[j][1])).grid(row=0,column=j)
            Label(self.f1,text=self.p[0].hand[j][0]).grid(row=1,column=j)

            Label(self.f2,image=self.convert(self.p[1].hand[j][1])).grid(row=0,column=j)
            Label(self.f2,text=self.p[1].hand[j][0]).grid(row=1,column=j)

            Label(self.f3,image=self.convert(self.p[2].hand[j][1])).grid(row=0,column=j)
            Label(self.f3,text=self.p[2].hand[j][0]).grid(row=1,column=j)

            Label(self.f4,image=self.convert(self.p[3].hand[j][1])).grid(row=0,column=j)
            Label(self.f4,text=self.p[3].hand[j][0]).grid(row=1,column=j)
        print self.num
        if self.num==5:
            Label(self.root,text="Game End!").grid(row=3,column=9)
            
    def close(self):
        self.root.quit()
        self.root.destroy()
        



def main():

    newcards = Cards()
    newcards.createCards()
    print newcards.cards
    
    newDeck = Deck(newcards.cards)
    newDeck.shuffle()
    print "shuffled deck is:"
    print newDeck.cards

    p=[]
    for i in range(1,5):
        p.append(Player(str(i)))

    for i in range(5):
        for j in range(1,5):
            p[j-1].addToHand(newDeck.getNextCard((j-1)+i*4))
        
    for i in range(4):
        p[i].showHand()

    GUI(p)
    

if __name__=="__main__":
    main()
