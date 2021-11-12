class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9]
    suits = ['♠', '♣', '♦', '♥']
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.card = self.rank + self.suit

    def __str__(self):
        '''Hiển thị lá bài'''
        pass

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
    