lowers = "abcdefghijklmnopqrstuvwxyz"
all_letters = ""
letter_counts = [0 for i in range(26)]
import copy

if __name__ == "__main__":
    hand = "nrungiles" #Letters in hand + letters in row of board
    rules = [ #meeting these conditions dequalifies words
        '("rul" not in words[i])',  #default: ("" not in words[i])
        '(words[i][0] not in "r")',  #default: (words[i][0] not in "")
        '(len(words[i]) < 4)'  #dafault: (len(words[i]) < 2
    ]


letter_vals = [1, 4, 4, 2, 1, 4, 3, 3, 1, 10, 5, 2, 4, 2, 1, 4, 10, 1, 1, 1, 2, 5, 4, 8, 3, 10]


class board():
    def __init__(self):
        self.board = [["." for i in range(11)] for i in range(11)]
        self.rows = [self.board[i] for i in range(11)]
        self.cols = [[self.rows[i][j] for i in range(11)] for j in range(11)]
    def importBoard(self):
        with open("Board.txt","r") as f:
            self.board = f.read().splitlines()#f.readlines()
            self.refresh()
    def refresh(self):
        self.rows = [self.board[i] for i in range(11)]
        self.cols = [''.join(map(str,[self.rows[i][j] for i in range(11)])) for j in range(11)]
    def works(self):
        for i in range(11):
            pass
    def wordsFromLine(self,rowcol, num):
        if rowcol in ["row","col"]:
            self.refresh()
            if rowcol == "row":
                line = list(self.rows[num])
            else:
                line = list(self.cols[num])
            with open("enable1 - Copy.txt","r+") as f:
                wordlen,line_length = 0,11
                word,words = "",[]
                line += "."
                while line_length > 1:
                    if line[wordlen] == ".":
                        del(line[0:wordlen+1])
                        line_length -= wordlen
                        if word != "":
                            words.append(word)
                            word = ""
                            wordlen = 0
                        else:
                            line_length -= 1
                    else:
                        word += line[wordlen]
                        wordlen += 1
                if word != "":
                    words += word
                for i in range(len(words)):
                    if len(words[i]) < 2:
                        del words[i]
                        i -= 1
                return words
        else:
            0/0

#test to see if array of words are in the simplified list
def words_work(arr):
    global working_words
    if len(arr) != 0:
        for i in arr:
            if not i in working_words:
                return 0
    return 1

#simplify usable words
def filter_words(hand=[], handlen=0):
    global letters, all_letters, board_letters
    handlen=len(hand)
    with open("tmp_words.txt","w") as fw:
        pass #clear tmp_words
    with open("tmp_words.txt","a+") as fw:
        with open("enable1 - Copy.txt","r+") as fr:
            lines = fr.read().splitlines()
            overall_len_before = len(hand+board_letters)
            for i in range(172821):
                testword = lines[i]
                #print(testword)
                works = 1
                for i in testword:
                    if not i in letters:
                        works = 0
                        break
                #if "?" in hand:
                    
                all_before = hand + board_letters
                if works:
                    for i in range(26):
                        if testword.count(lowers[i]) > all_before.count(lowers[i]):
                            works = 0
                            break
                if works and len(testword) <= 11:
                    fw.write(str(testword + "\n"))
    with open("tmp_words.txt","r") as f:
        words = f.read().splitlines()
    with open("Word Values.txt","w") as f:
        for i in range(len(words)):
            Sum = 0
            for j in range(len(words[i])):
                Sum += letter_vals[lowers.find(words[i][j])]
            f.write((str(Sum)+"\n"))


def wordsFromLine(line):
    with open("tmp_words.txt","r+") as f:
        wordlen,line_length = 0,11
        word,words = "",[]
        line += "."
        while line_length > 1:
            if line[wordlen] == ".":
                del(line[0:wordlen+1])
                line_length -= wordlen
                if word != "":
                    words.append(word)
                    word = ""
                    wordlen = 0
                else:
                    line_length -= 1
            else:
                word += line[wordlen]
                wordlen += 1
        if word != "":
            words += word
        for i in range(len(words)):
            if len(words[i]) < 2:
                del words[i]
                i -= 1
        return words
    
#filters words and tests line
def test(line):
    words = wordsFromLine(line)

def adv_filter():
    global rules
    words = []
    with open("tmp_words.txt","r") as fr:
        words1 = fr.read().splitlines()
    words = copy.deepcopy(words1)
    with open("tmp_words.txt","w") as f:
        pass
    i = 0
    while i < len(words):
        try:
            x = ' or '.join(map(str,rules))
            x = eval(x)
            if x:
                words.pop(i)
            else:
                i += 1
        except:
            i += 1
    with open("tmp_words.txt","a") as fw:
        for i in range(len(words)):
            print(words[i])
            fw.write((words[i] + "\n"))
        

if __name__ == "__main__":
    board = board()
    board.importBoard()
    letters = list(hand) #testing
    board_letters = ""
    for i in range(len(hand)):
        letter_counts[lowers.find(hand[i])] += 1
    for i in range(11):
        for j in range(11):
            current = board.board[i][j]
            if current != ".":
                board_letters += current
                letter_counts[lowers.find(current)] += 1
                if current not in letters:
                    letters += current
    all_letters = board_letters + hand
    letters = list(set(letters))
    filter_words(hand)
    with open("tmp_words.txt","r") as f:
        working_words = f.read().splitlines()
    linewords =  board.wordsFromLine("row",4)
    print(linewords)
    print(words_work(linewords))
    adv_filter()
    #allnewwords = []












    
