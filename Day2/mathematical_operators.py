# Mathematical Operators +, -, /, %, //

#Suppose you invest ₹1,00,000 at 6% per year for 2 years

if __name__=="__main__":
    #principal = int(float("9.5"))
    #rate = float(input())  
    #print(principal)
    principal = float(input())
    rate = float(input())
    time = float(input())
    simple_interest = (principal*rate*time)/100
    print(simple_interest)