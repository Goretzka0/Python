
# coding: utf-8

# In[361]:


from math import sqrt
class Polynomial:
    def __init__(self,cfs):
        self.deg = len(cfs)-1
        self.cfs = cfs
    def __add__(self,other):
        (cfs1,cfs2) = (self.cfs,other.cfs)
        if (len(cfs1)>len(cfs2)):
            (cfs1,cfs2) = (cfs2,cfs1)
        cfs1 = [0]*(len(cfs2)-len(cfs1)) + cfs1
        sumcfs = [cfs1[i]+cfs2[i] for i in range(len(cfs1))]
        return sumcfs
    def __mul__(self,other):
        proddeg = self.deg + other.deg
        prodcfs = [0]*(proddeg + 1)
        for i in range(0, self.deg + 1):
            for j in range(0, other.deg + 1):
                prodcfs[i+j] += self.cfs[i] * other.cfs[j]
        return prodcfs
    def __sub__(self,other):
        (cfs1,cfs2) = (self.cfs,other.cfs)
        if (len(cfs1)>len(cfs2)):
            (cfs1,cfs2) = (cfs2,cfs1)
        cfs1 = [0]*(len(cfs2)-len(cfs1)) + cfs1
        subcfs = [cfs1[i]-cfs2[i] for i in range(len(cfs1))]
        return subcfs
    def __neg__(self):
        for i in range(len(self.cfs)):
            self.cfs[i] = - self.cfs[i]
        return self.cfs
    def __mod__(self,other):
        ostatok = 0
        if (len(self.cfs) < len(other.cfs)):
            return ostatok
        else:
            while (len(self.cfs) >= len(other.cfs)):
                stepdeg = len(self.cfs) - len(other.cfs)
                stepcf = self.cfs[0]/other.cfs[0]
                stepcfs = [other.cfs[i]*stepcf for i in range(len(other.cfs))]
                if (len(stepcfs) < len(self.cfs)):
                    stepcfs =stepcfs+[0]*(len(self.cfs)-len(stepcfs))
                self.cfs = [self.cfs[i]-stepcfs[i] for i in range(len(self.cfs))]
                if (self.cfs[0] == 0):
                    self.cfs = [self.cfs[i+1] for i in range(len(self.cfs)-1)]
            return self.cfs
    def __eq__(self,other):
        return self.cfs==other.cfs
    def __str__(self):
        result =''
        for i in range(len(self.cfs)):
            result += str(' + ' + str(self.cfs[i]) + 'x**' + str(self.deg - i))
        return result
    def gcd(self, pol2):
        pass
    def subset(self,x):
        result = 0
        for i in range(len(self.cfs)):
            result += self.cfs[i]*x**(len(self.cfs) - i-1)
        return result   
    def der(self, d = 1):
        dercfs = self.cfs
        for j in range(d):
            dercfs = [(len(dercfs)-i-1)*dercfs[i] for i in range(len(dercfs)-1)]
        return dercfs
    def dersubst(self, x, d=1):
        result = 0
        for i in range(len(self.der(d))):
            result += self.der(d)[i]*x**(len(self.der(d)) - i-1)
        return result   
    def taylor(self, x, d):
        def fact(n):
            fac = 1
            while n>0:
                fac *=n
                n -=1
            return fac
        tl0 = 0
        result = ''
        if d<=0:
            return tl0
        tl = [self.subset(x)]
        for i in range(d):
            tl.insert(0,self.dersubst(x,i)/fact(i))
        for i in range(len(tl)):
            result += str(' + ' + str(tl[i]) + '(x-' + str(x) +')**' + str(len(tl)-1 - i))
        return result
    def degree(self):
        degree = len(self.cfs)-1
        return degree
    
class RealPolynomial(Polynomial):
    def __init__(self,cfs):
        Polynomial.__init__(self,cfs)
    def find_root(self):
        if (len(self.cfs)%2 == 1):
            print('Многочлен должен быть нечетной степени')
        if (self.cfs[0] == 0):
            print('Многочлен должен быть нечетной степени')
        rightboard = 1
        leftboard = -1
        if (self.cfs[0] < 0):
            while self.subset(leftboard) < 0:
                leftboard *= 2
            while self.subset(rightboard) > 0:
                rightboard *= 2
        if (self.cfs[0] > 0):
            while self.subset(leftboard) > 0:
                leftboard *= 2
            while self.subset(rightboard) < 0:
                rightboard *= 2
        else:
            print('Корни многочлена должны быть рациональными')
        while rightboard - leftboard > 0.0001:
            mid = (rightboard + leftboard)/2
            if (self.cfs[0] < 0):
                if (self.subset(mid) < 0):
                    rightboard = mid
                else:
                    leftboard = mid
            else:
                if (self.subset(mid) > 0):
                    rightboard = mid
                else:
                    leftboard = mid
        return mid
    def locmin_value(self, left_x, right_x):
        pass
    
class DegreeIsTooBig(Exception):
    def __init__(self,x,y=2):
        self.x = x
        self.y = y
    def error(self,x,y):
        if (self.x>self.y):
            print('В результате операции получился многочлен степени',self.x,', максимально допустимая степень',self.y)
def degree(x,y):
    raise DegreeIsTooBig(x,y)

class QuadraticPolynomial(Polynomial):
    def __init__(self,cfs):
        Polynomial.__init__(self,cfs)
        try:
            degree(len(self.cfs)-1,2)
        except DegreeIsTooBig as exc:
            exc.error(len(self.cfs)-1,2)
    def __mul__(self,other):
        proddeg = self.deg + other.deg
        prodcfs = [0]*(proddeg + 1)
        for i in range(0, self.deg + 1):
            for j in range(0, other.deg + 1):
                prodcfs[i+j] += self.cfs[i] * other.cfs[j]
        if (len(prodcfs)-1>2):
            try:
                degree(len(prodcfs)-1,2)
            except DegreeIsTooBig as exc:
                exc.error(len(prodcfs)-1,2)
        else:
            return prodcfs
    def taylor(self, x, d):
        def fact(n):
            fac = 1
            while n>0:
                fac *=n
                n -=1
            return fac
        tl0 = 0
        result = ''
        if d<=0:
            return tl0
        tl = [self.subset(x)]
        for i in range(d):
            tl.insert(0,self.dersubst(x,i)/fact(i))
        for i in range(len(tl)):
            result += str(' + ' + str(tl[i]) + 'x**' + str(len(tl)-1 - i))
        if (d>2):
            try:
                degree(d,2)
            except DegreeIsTooBig as exc:
                exc.error(d,2)        
        else:
            return result
    def solve(self):
        a = self.cfs[0]
        b = self.cfs[1]
        c = self.cfs[2]
        D = b**2 - 4*a*c
        otv = []
        if (D<0):
            return otv
        if (D==0):
            x = (-b)/(2*a)
            otv.append(x)
            return otv
        else:
            x1 = (-b + sqrt(D))/(2*a)
            x2 = (-b - sqrt(D))/(2*a)
            otv = [x1,x2]
            return otv

