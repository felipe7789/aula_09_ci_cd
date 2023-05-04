import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    num1=3
    num2=4
    output=methods.soma(num1,num2)
    assert output==7

def test_multi():
    num3=2
    num4=2
    output=methods.multi(num3,num4)
    assert output==4

def test_subtr():
    num5=4
    num6=2
    output=methods.subtr(num5,num6)
    assert output==2

def test_divi():
    num7=8
    num8=4
    output=methods.divi(num7,num8)
    assert output==2

test_area()
test_perimeter()
test_soma()
test_multi()
test_subtr()
test_divi()