import io, math
import hilbert as hc
import cairocffi as cairo

class visual_binary():

    def __init__(self, in_f, wdth, hght):

        #init varibles
        self.file = in_f
        self.width = wdth
        self.height = hght
        self.x = 0
        self.y = 0
  
        #init functions
        self.canvas()
        self.open_file()
        
    def canvas(self):
        #creates canvas
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,self.width,self.height)
        self.canvas = cairo.Context(self.surface)
        self.canvas.set_source_rgb(0,0,0)
      
    def open_file(self):
        #reads file into raw format
        try:
            file_o = io.FileIO(self.file,mode='r',closefd = True)
            self.binary = file_o.read((self.height*self.width))
        except:
            print("Could not open file.")
            
    def draw(self,pix_char):
        #draw the pixel on the canvas
        #color is based off ascii table
        if (pix_char >= 37) and (pix_char <= 127):
            self.canvas.set_source_rgb(0,0,1)
        elif pix_char == 0:
            self.canvas.set_source_rgb(0,0,0)
        else:
            self.canvas.set_source_rgb(1,0,0)
        self.canvas.rectangle(self.x,self.y,1,1)
        self.canvas.fill()
            
    def lft_rgt(self):
        #starts left moves to right
        #once end of row starts a 0
        #loop through data
        for pix in self.binary:
            self.draw(pix)
            if self.x >= self.width:
                self.x = 0
                self.y += 1
            else:
                self.x += 1
        #png out
        self.surface.write_to_png ("leftToRight.png")
    
    def zig_zag(self):
        #goes to end of row
        #then moves up one and opposite direction
        #contants to help direction
        k = [0, self.width]
        d, dx = 1, 1
        #loop through data
        for pix in self.binary:
            self.draw(pix)
            if (self.x == k[d]):
                d = (d+1)%2
                self.y  += 1
                dx *= -1
            else:
                self.x += dx
        
        #png out    
        self.surface.write_to_png("zig_zag.png")

    def hilbert(self):
        #hilbert curve
        gen = hc.Hilbert(math.log(self.width,2))
        for pix in self.binary:
            self.draw(pix)	
            try:
                next(gen)
            except:
                break
            self.x = gen.x
            self.y = gen.y
    
        self.surface.write_to_png("hilbert.png")
