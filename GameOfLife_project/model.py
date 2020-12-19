class Model:
    def __init__(self):
        self.cells = {}

    def insert_cell(self, posn):
        #вставка клеток
        if (posn not in self.cells) or (not self.cells[posn][0]):
            x, y = posn
            #print(self.cells)

            n = 0

            def neighbour(posn):
                if posn in self.cells:
                    c1, c2 = self.cells[posn]
                    self.cells[posn] = (c1, c2 + 1)
                    return int(c1)
                else:
                    self.cells[posn] = (False, 1)
                    return 0

            n += neighbour((x - 1, y - 1))
            n += neighbour((x - 1, y))
            n += neighbour((x - 1, y + 1))
            n += neighbour((x, y - 1))
            n += neighbour((x, y + 1))
            n += neighbour((x + 1, y - 1))
            n += neighbour((x + 1, y))
            n += neighbour((x + 1, y + 1))

            self.cells[posn] = (True, n)
            #print(self.cells)

    def delete_cell(self, posn):
        if (posn in self.cells) and (self.cells[posn][0]):

            x, y = posn

            def del_c2(posn):
                c1, c2 = self.cells[posn]
                self.cells[posn] = (c1, c2 - 1)

            del_c2((x - 1, y - 1))
            del_c2((x - 1, y))
            del_c2((x - 1, y + 1))
            del_c2((x, y - 1))
            del_c2((x, y + 1))
            del_c2((x + 1, y - 1))
            del_c2((x + 1, y))
            del_c2((x + 1, y + 1))

            self.cells[posn] = (False, self.cells[posn][1])

    #def clean(self):
    #    ...в разработке...
    #    new_cells = {}
    #    for posn in iter(self.cells):
    #        if self.cells[posn] != (0, 0):
    #            x, y = posn
    #            new_cells[posn] = self.cells[posn]
    #    self.cells = new_cells

    def next_g(self):
        model = Model()
        for posn in iter(self.cells):
            c1, c2 = self.cells[posn]
            if (c2 == 3) or (c1 and c2 == 2):
                model.insert_cell(posn)
        return model


