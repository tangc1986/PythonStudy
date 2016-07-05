def check_fermat(a, b, c, n):
    if (n > 2):
        if a**n + b**n == c**n:
            print '天哪，费马弄错了！'
        else:
            print '不，那样不行'
            
def fun():
    print '请依次输入a、b、c、n，每行一个'
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    n = int(raw_input())
    check_fermat(a, b, c, n)
    
if __name__ == '__main__':
    fun()
    
    
    