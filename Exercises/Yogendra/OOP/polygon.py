class Polygon:
      def __init__(self,poly,a,b=1):
        self.poly=poly
        self.one = a
        self.two = b

      def tri_area(self):
         return 0.5*(self.one*self.two)

      def sq_area(self):
         return self.one*self.one

      def rect_area(self):
         return self.one*self.two
