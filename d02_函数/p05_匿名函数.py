def test_fun(hehe):
    res=hehe(1,2)
    return res

res=test_fun(lambda x,y:x+y)
print(res)
