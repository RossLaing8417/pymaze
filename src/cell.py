class Cell:
    def __init__(self, p1, p2, top=True, bottom=True, left=True, right=True):
        self.p1 = p1
        self.p2 = p2
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def draw(self, canvas, fill_color):
        if self.top:
            canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p1.y,
                               fill=fill_color, width=2)
        if self.bottom:
            canvas.create_line(self.p1.x, self.p2.y, self.p2.x, self.p2.y,
                               fill=fill_color, width=2)
        if self.left:
            canvas.create_line(self.p1.x, self.p1.y, self.p1.x, self.p2.y,
                               fill=fill_color, width=2)
        if self.right:
            canvas.create_line(self.p2.x, self.p1.y, self.p2.x, self.p2.y,
                               fill=fill_color, width=2)
