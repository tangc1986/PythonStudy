def check_fermat(a, b, c, n):
    if (n > 2):
        if a**n + b**n == c**n:
            print '���ģ�����Ū���ˣ�'
        else:
            print '������������'
            
def fun():
    print '����������a��b��c��n��ÿ��һ��'
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    n = int(raw_input())
    check_fermat(a, b, c, n)
    
if __name__ == '__main__':
    fun()
    
    
    