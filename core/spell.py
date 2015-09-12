"""class to predict manga in case of mismatch.

   It reads a list of manga and finds number of spaces being equal to user's input.
  It then finds mininum number of operations needed to make both the strings equal.
   Operations include deletion, insertion and substitution. Read `edit_distance()`
   to know more about algorithm"""

class spell:

    def __init__(self, name):

        self.name = name.lower()
        self.count_space = self.name.count(' ')
        self.data = self.load_list()
        self.candidates = self.compare()
        self.cand_length = len(self.candidates)

    def load_list(self):
        data = []
        fi = open('core/manga.txt', 'r')
        lines = fi.readlines()
        for line in lines:
            data.append(line.replace('\n','').rstrip())

        return data

    def compare(self):
        candidates = []
        for x in self.data:
            if x.count(' ') == self.count_space:
                candidates.append(x)
        
        return candidates

    def _edit_distance(self, cand, manga):
        #read about algorithm here 
        #https://web.stanford.edu/class/cs124/lec/med.pdf

        if cand == manga:
            return 0

        n = len(cand)
        m = len(manga)
        d = [[0 for x in xrange(m+1)] for x in xrange(n+1)]
        for x in xrange(n+1):
            d[x][0] = x

        for y in xrange(m+1):
            d[0][y] = y

        for x in xrange(1, n+1):
            for y in xrange(1, m+1):
                if cand[x-1] == manga[y-1]:
                    sub = d[x-1][y-1]
                else:
                    sub = d[x-1][y-1] + 1


                d[x][y] = min(d[x-1][y] + 1, d[x][y-1] + 1, sub)

        return d[n][m]


    def correct(self):
        manga = self.name.split(' ')
        distance = []

        for x in xrange(self.cand_length):

            correct = self.candidates[x].split(' ')
            dist = 0
            for y in xrange(len(correct)):
                dist += self._edit_distance(manga[y], correct[y])

            distance.append((dist, ' '.join(correct)))    

        return min(distance)[1]        


if __name__ == '__main__':
    s = spell('FAIRY TALE')
    print(s.correct())
