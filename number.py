class Number:
    def __init__(self, n: int):
        self.n = n


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        n=self.n
        return n

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        n=self.n
        if n%2==1:
            return True
        else:
            return False

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        n=self.n
        if n%2==0:
            return True
        else:
            return False

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        n=self.n
        i=2
        while i<=n//2 and i!=1:
            if n%i==0:
                return False
            i+=1
        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        n=self.n
        i=1
        l=[]
        while i<=n:
            if n%i==0:
                l.append(i)
            i+=1
        return l

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        n=self.n
        s=str(n)
        return len(s)

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        n=self.n
        s=str(n)
        i=0
        m=0
        while i<len(s):
            m+=int(s[i])
            i+=1
        return m

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        n=self.n
        s=str(n)
        return int(s[::-1])

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        n=self.n
        s=str(n)
        m=0
        i=0
        while i<len(s)//2:
            if s[i]==s[-i-1]:
                m+=1
            i+=1
        if m==len(s)//2:
            return True
        else:
            return False

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        n=self.n
        s=str(n)
        i=0
        l=[]
        while i<len(s):
            l.append(int(s[i]))
            i+=1
        return l

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        n=self.n
        s=str(n)
        i=1
        mx=int(s[0])
        while i<len(s):
            if int(s[i])>mx:
                mx=int(s[i])
            i+=1
        return mx

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        n=self.n
        s=str(n)
        i=1
        mn=int(s[0])
        while i<len(s):
            if int(s[i])<mn:
                mn=int(s[i])
            i+=1
        return mn

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        n=self.n
        s=str(n)
        i=0
        l=0
        while i<len(s):
            l+=int(s[i])
            i+=1
        return l/len(s)
    
    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        n=self.n
        s=str(n)
        i=0
        l=[]
        m=0
        while i<len(s):
            l.append(int(s[i]))
            i+=1
        l.sort()
        if len(l)%2==0:
            q=len(l)//2-1
            w=len(l)//2
            m=(l[q]+l[w])/2
        else:
            m=l[len(l)%2+1]
        return m

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        n=self.n
        s=str(n)
        i=1
        l=[]
        mn=int(s[0])
        mx=int(s[0])
        while i<len(s):
            if int(s[i])<mn:
                mn=int(s[i])
            if int(s[i])>mx:
                mx=int(s[i])
            i+=1
        for j in range(mn,mx+1):
            l.append(j)
        return l

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(13241)
print(number.get_median())
