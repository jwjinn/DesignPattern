b# Observer 패턴 정리

## 옵져버 패턴은 무엇인가? 
옵져버 패턴은 한 객체의 상태가 바뀌면 그 객체에 의존하는 다른 객체에게 연락이 가고 자동으로 갱신되는 방식으로 일대다 의존성을 정의합니다.

간단하게 표현 하자면

1. 주체 객체의 정보가 변했다.
2. 옵저버 인터페이스를 통해서 클래스들에게 변한 정보를 전달한다.


## Observer 패턴을 신문 배달, 구독으로 예시

1. 나는 신문을 구독하기를 원합니다.
2. 그래서 주체 객체(신문사)에게 신문을 구독한다고 연락을 해야 합니다.
3. 주체 객체에게 구독한다라는 말을 전달해야 하고, 정보도 전달 받을 수 있기를 원합니다.
4. 주체 객체(신문사)와 나는 혈연관계가 아닙니다. 최소한의 관계성만 유지해야 합니다.
5. 그래서 인터페이스를 주체 객체에게 주입하고 인터페이스를 통해서 정보를 전달합니다.

</br>

## JAVA에서의 구현 - Observer, Subject, DisplayElement
> 인터페이스는 3개가 필요합니다.

1. Observer
    - 주체 객체와 구독하는 객체간의 연결 통로가 된다.
    - Observer 인터페이스를 implements를 한 클래스들을 호출한다고 생각하면 간단하다.
    - 주체 객체로 부터 받고 싶은 정보를 명시한 것이 옵저버 인터페이스의 매서드가 된다.
  
2. Subject
   - 주체 객체에게 옵저버를 다룰 수 있는 매서드를 설정한다.
   - 매개인자에 옵저버를 넣으면서, 옵저버 인터페이스를 implements한 모든 클래스들을 다룰 수 있게 설정하였다.

3. DisplayElement
    - 고객의 요구


</br>

```java

public interface Subject {
	
	public void registerObserver(Observer o);
	public void removeObserver(Observer o);
	public void notifyObserver();

}

public interface Observer {
	
	public void update(float temp, float humidity, float pressure);

}

public interface DisplayElement {
	
	public void display();

}

```
## 코드 설명
1. 내가 신문사에게 신문을 전화로 구독하겠다고 연락을 한다면 갖춰져야 하는 것은 신문사의 준비입니다.</br>
해당 준비역할을 하는 것이 'Subject 인터페이스'

2. 나랑 옆집의 사람이 해당 신문을 구독을 한다면, 서로의 위치는 달라도 같은 정보를 받을 수 있어야 합니다.</br>
통일성을 위해서 같은 신문 배달부가 배달합니다. 위 코드의 해당 역할을 하는 것이 Observer 인터페이스입니다.

3. 추후 코드에서는 Observer 인터페이스를 implements를 하므로, 해당 구현 클래스가 Subject 인터페이스의 매개변수로 들어와서 관리되게 합니다.


## 파이선에서의 구현 - Observer, Subject, DisplayElement

</br>

```python

class Subject(metaclass=ABCMeta):

    @abstractmethod
    def registerObserve(self, Observer):
        pass

    @abstractmethod
    def removeObserver(self, Observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass


class DisplayElement(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass


```

</br>

## 코드 설명
- 기본적으로 위와 같은 역할을 합니다. 분명 다중상속에 의한 방법도 있을 거라 생각됩니다.
- python은 java와 매개변수를 주는 형식이 다르다는 것을 다시한번 상기합니다.

## JAVA - WeatherData 구현
> 지금까지 통로를 구현했습니다. 이제 구체화해봅시다.

</br>

## 신문사를 예시로 구현하고자 하는 것

1. 내가 신문사에게 구독 및 계약해지를 할 수 있어야 합니다.
2. 신문사는 당연하게도 구독자들의 정보를 가지고 있어야 합니다.
3. 신문사는 해당 구독자 정보를 토대로 신규 정보가 들어왔을 경우, 전달 할 수 있어야 합니다.
4. 물론, 위 3번의 방식을 pull 방식으로 바꿀 수 있습니다.

```java
public class WeatherData implements Subject {
	
	private List<Observer> observers;
	private float temperature;
	private float humidity;
	private float pressure;
	
	
	public WeatherData() {
		observers = new ArrayList<Observer>();
	}
	
	
	
	public void registerObserver(Observer o) {
		observers.add(o);

	}

	
	public void removeObserver(Observer o) {
		observers.remove(0);

	}

```
</br>

주체 객체인 WeatherData는 Observer들의 명단을 arraylist형식으로 저장하고 있습니다.


```java

public void notifyObserver() {
		
		for(Observer observer : observers) {
			observer.update(temperature, humidity, pressure);
		}

```
## 코드 설명
위 코드들을 Obsrver로 등록을 한다 라고 생각하면, 헷갈릴 수 있습니다. </br>

옵져버 자체는 아무 역할이 없습니다. 저 옵져버 자리에는 옵져버를 implements한 클래스들이 온다고 생각하면 됩니다.

즉, 각각의 클래스들이 arraylist에 등록이 된다고 생각하면 됩니다.<br>

notifiyObserver를 보면, 왜 observer의 메서드를 설정한 이유를 알게 됩니다. </br>
클래스들은 Observer 인터페이스를 implements 하므로, 위 메서드를 공통적으로 보유하고 있습니다. 그러하니, observer.update를 통해서, 저장된 모든 클래스들에게 값의 전달이 가능합니다.


## PYthon - WeatherData 구현


```python

class WeatherData(Subject):


    def __init__(self):
        self.observer = []

    def notifyObservers(self):
        for k in self.observer:
            k.update(self.temperature, self.humidity, self.pressure)


    def registerObserve(self, Observer):
        self.observer.append(Observer)

    def removeObserver(self, Observer):
        self.observer.remove(Observer)


    def measurementsChanged(self):
        self.notifyObservers()


    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()
```

</br>

## 코드 설명

객체지향을 대학에서 그리고 책에서 JAVA로 먼저 배우다 보니, 두 언어간의 충돌이 가장 많았었던 부분이라고 생각됩니다.

## JAVA

```java

private List<Observer> observers;

public WeatherData() {
		observers = new ArrayList<Observer>();
	}

public void notifyObserver() {
		
		for(Observer observer : observers) {
			observer.update(temperature, humidity, pressure);
		}

	}
```

## Python

```python

def __init__(self):
        self.observer = []

def registerObserve(self, Observer):
    self.observer.append(Observer)

def notifyObservers(self):
        for k in self.observer:
            k.update(self.temperature, self.humidity, self.pressure)
```

1. ArrayList 선언방식의 차이와 문법의 허용 범위
   - JAVA에서는 리스트에서 데이터타입을 명시해야 합니다. 그리고 해당 데이터 타입에 맞는 데이터만 받게 됩니다.
   - 그러나 Python의 리스트는 모든 데이터 형식을 받습니다. 따라서, 리스트 타입을 명시할 필요가 없습니다.

2. pytohn의 For in
   - 파이선의 For in 의 매개변수는 데이터 타입을 명시할 필요가 없다.


## python 나머지.


### CurrentConditionsDisplay
```python
class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, WeatherData):
        self.weatherData = WeatherData
        self.weatherData.registerObserve(self)

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity

        self.display()


    def disconnect(self):
        print("CurrentConditionsDisplay - observer와의 관계를 청산하겠습니다.")
        self.weatherData.removeObserver(self)


    def display(self):
        print("CurrentConditoin의 현재 상태: 온도 " + str(self.temperature) + " 습도 " + str(self.humidity))

```

객체가 생성될 때, 이미 생성된 주체 객체(WeatherData)를 받고 주체 객체에 등록을 합니다.


```python

	weatherData = WeatherData()

    currentDisplay = CurrentConditionsDisplay(weatherData)
    current3 = Current3(weatherData)


    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)

    currentDisplay.disconnect()

    weatherData.setMeasurements(82, 70, 29.2)

```

### Main문 플로우 정리

1. 당연히 신문사는 내가 구독하기 전에 있어야 한다. WeatherData 객체를 생성한다.

2. 객체를 생성할때마다, WeatherData()를 매개변수로 대입시켜, Arraylist에 담아지게 만든다.


### pull 방식으로 변경하기

- update()메서드의 매개변수를 다 없애고, 값을 WeatherData.getTemperature 처럼, 직접 주체 객체에서 얻어오는 방식을 채용하면 된다.


