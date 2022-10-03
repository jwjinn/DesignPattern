# Decorator 패턴
> 생각보다 더 이해하는 데 오래걸린 패턴

## 핵심사항
1. 상속을 이용하되, 형식을 유지한다.
2. Decorate 대상이 기존 객체를 포함시키는 개념.


## Beverage - 가장 기본이 되고, 쌓아나갈 클래스

```python

class Beverage(metaclass=ABCMeta):

    def __init__(self, name):
        self.description = name

    def getDescription(self):
        return self.description


    @abstractmethod
    def cost(self):
        pass


```

데코레이터는 문법상 상속을 이용하지만, 상속을 사용하는 목적이 형식을 맞추기 위함입니다.

지금 현재 작성하고 있는 Beverage 클래스는 계속 유지해나갈 형식을 선언하는 곳입니다.

'Beverage'클래스는 description과 cost를 decorating한 값을 얻고 싶어하는 클래스입니다.

1. def __init__(self):
    - description을 받을 수 있는 변수와 decorator에 필수적인 return도 만들어져 있다. 

2. cost메서드는 현재 추상으로 해두었다. 


</br>

## Coffee 종류들 - Beverage 객체에서 상속을 받은

```python

class Espresso(Beverage):

    def __init__(self):
        super(Espresso, self).__init__("Espresso")

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__("HouseBlend")


    def cost(self):
        return 0.89


```
## 코드 설명

1. Espresso가 객체로 생성되었을 때, description에 변수가 저장이 됩니다.
2. Beverage를 상속을 받았기 때문에, description return기능을 가지고 있습니다.

3.  cost return 기능을 선언했습니다.


## CondimentDecorator - Beverage 객체에서 상속을 받은, 모든 Decorator의 어머니

</br>

```python
class CondimentDecorator(Beverage):

    def __init__(self, Beverage):
        self.beverage = Beverage

    @abstractmethod
    def getDescription(self):
        pass

```

1. 형식을 유지하기 위해서 Beverage 객체를 상속을 받았습니다.
2. CondimentDecorator를 해석하기 편하게 할려면, 데코레이터 클래스의 필요 공통부분들을 모아 둔 곳이라고 생각하면 편합니다.
3. 객체를 생성할때, Beverage class타입을 받고 beverage 변수로 저장을 하도록 받습니다.
4. 위 3번 과정이 형식을 유지하는 결정적인 방법입니다.


## Mocha - Decorator

```python

class Mocha(CondimentDecorator):

    #def __init__(self, Beverage):
    #   self.beverage =Beverage
    
    def __init__(self, Beverage):
        super(Mocha, self).__init__(Beverage)


    def getDescription(self):
        return self.beverage.getDescription() + ", 모카"

    def cost(self):
        return self.beverage.cost() + 0.2

```

beverage 객체만 객체를 생성할때, 받는 것을 알 수 있습니다.


## Starbuzzcoffee

```python

if __name__ == "__main__":

    beverage = HouseBlend()
    beverage = Mocha(beverage)
    print(beverage.getDescription())
    print(beverage.cost())

    beverage1 = Espresso()
    beverage1 = Mocha(beverage1)
    beverage1 = Mocha(beverage1)
    print(beverage1.getDescription())
    print(beverage1.cost())


```


## 정리

1. 상속을 형식을 유지하는데 사용한다. 그러깅 위해서 Beverage를 활용했다.
2. 데이터를 호출하는 느낌이므로, return기능이 필수적이다.
3. 상속을 유지하는데, 생성자를 이용을 한다. 즉, Beverage 타입만 받는.
4. 객체를 받고(Beverage 타입), 생성자로 선언을 한 다음, decorater의 데이터를 추가(self.beverage.getDescription() + ", 모카")하고 리턴한다.