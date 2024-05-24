from lab_5 import tt1, tt2, tt3, tt4, tt5

def test_a1():
    words = "test te tes".split()

    s=''
    s = tt1.a1(words[0],words[1])
    for i in words:
        if(s in i):
            continue
        else:
            s = tt1.a1(s,i)
    assert s == "ta" #te

def test_a2():
    n = "1 2 3 4 6".split()

    assert tt2.a2(n)==5

def test_a3():
    assert tt3.a3("IV")==4

def test_a4():
    assert tt4.a4("listen", "silent", "enlist")==True

def test_a5():
    assert tt5.a5(10)==55