"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):
    
    class_name = [None, 'StrightFlush', 'FourOfAKind', 'FullHouse', 'Flush', 
                        'Straight', 'ThreeOfAKind', 'TwoPair', 'Pair']
    
    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
    
    def has_pair(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
    
    def has_twopair(self):
        self.rank_hist()
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1
                if count >= 2:
                    return True
        return False
    
    def has_threeofakind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
    
    def has_straight(self):
        self.rank_hist()
        sort_rank = self.ranks.keys()
        sort_rank.sort()
        if 13 in sort_rank and 1 in sort_rank:
            sort_rank.append(14)
        stright_count = 0
        pre_rank = None
        for rank in sort_rank:
            if pre_rank == None or pre_rank == rank:
                pre_rank = rank
                continue
            if pre_rank + 1 == rank:
                stright_count += 1
            else:
                stright_count = 0
            pre_rank = rank
            if stright_count >= 4:
                return True
        return False
    
    def has_fullhouse(self):
        self.rank_hist()
        if 3 in self.ranks.values() and 2 in self.ranks.values():
            return True
        return False
    
    def has_fourofakind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False
    
    def has_straightflush(self):
        suit_ranks = {}
        for card in self.cards:
            suit_ranks[card.suit] = suit_ranks.get(card.suit, []) + [card.rank]
        for suit_rank in suit_ranks:
            if len(suit_ranks[suit_rank]) >= 5:
                sort_rank = suit_ranks[suit_rank]
                sort_rank.sort()
                if 13 in sort_rank and 1 in sort_rank:
                    sort_rank.append(14)
                stright_count = 0
                pre_rank = None
                for rank in sort_rank:
                    if pre_rank == None or pre_rank == rank:
                        pre_rank = rank
                        continue
                    if pre_rank + 1 == rank:
                        stright_count += 1
                    else:
                        stright_count = 0
                    pre_rank = rank
                    if stright_count >= 4:
                        return True
        return False
    
    def classify(self):
        if self.has_straightflush():
            self.label = 1
        elif self.has_fourofakind():
            self.label = 2
        elif self.has_fullhouse():
            self.label = 3
        elif self.has_flush():
            self.label = 4
        elif self.has_straight():
            self.label = 5
        elif self.has_threeofakind():
            self.label = 6
        elif self.has_twopair():
            self.label = 7
        elif self.has_pair():
            self.label = 8
        else:
            self.label = 0

if __name__ == '__main__':
    # make a deck

    # deal the cards and classify the hands
    result = {}
    for i in range(10000):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        #print hand
        hand.classify()
        #print PokerHand.class_name[hand.label]
        #print ''
        result[hand.label] = result.get(hand.label, 0) + 1
    for k in result:
        print '%s is %f%%' % (PokerHand.class_name[k], result[k] / 10000.0 * 100.0)

