# Abstract factory

This pattern proves itself very useful when you want to create objects that are related to each other, in the sense that if you want to substitute one of the object's implementation, then you probably want to replace the other objects as well (following the Liskov Substitution Principle).

Let's show an example of how this would work:

Say you own a store with a fancy automation system in place, which you can control with some simple Python code.
Every day, you come in and run the same code, which drives the background music, your advertisement display and your LED board. The classes are defined below:

```python
class BackgroundMusic:
    def play(self):
        print("Playing typical store jingles.")

class AdvertisementDisplay:
    def start(self):
        print("Check out our bakery, 5 donuts for the price of 4")

class LedBoard:
    def run(self):
        print("Welcome to our store during a normal time of the year!")
```

You have written a simple client that interfaces with them in the following manner:

```python
class StoreClient:
    def __init__(self):      
        self.background_music = BackgroundMusic()
        self.advertisement_display = AdvertisementDisplay()
        self.led_board = LedBoard()

        self.background_music.play()
        self.advertisement_display.start()
        self.led_board.run()
```

This is all fine and dandy, but sometimes you want differently themed music, ads and messages, for instance when it's Christmas time. At first you figured: 'no problem, I'll just create an interface for the different classes and implement a Christmas version'. This might end up looking like the following:

```python
from abc import ABC, abstractmethod

class AbstractBackgroundMusic(ABC):

    @abstractmethod
    def play(self):
        """Starts the music"""
        raise NotImplementedError

class AbstractAdvertisementDisplay(ABC):

    @abstractmethod
    def start(self):
        """Boots up the display and starts displaying ads"""
        raise NotImplementedError

class AbstractLedBoard(ABC):

    @abstractmethod
    def run(self):
        """Starts displaying text"""
        raise NotImplementedError
```

with the concrete Christmas implementations looking like

```python
class ChristmasBackgroundMusic(AbstractBackgroundMusic):
    def play(self):
        print("Playing 'All I want for Christmas is you' on repeat")

class ChristmasAdvertisementDisplay(AbstractAdvertisementDisplay):
    def start(self):
        print("Check out all these Christmas deals we have for you!")

class ChristmasLedBoard(AbstractLedBoard):
    def run(self):
        print("Merry Christmas")
```

Happily, you go back to your StoreClient class and update it so that it now uses the Christmas implementations.

```python
class StoreClient:
    def __init__(self):      
        self.background_music = ChristmasBackgroundMusic()
        self.advertisement_display = ChristmasAdvertisementDisplay()
        self.led_board = ChristmasLedBoard()

        self.background_music.play()
        self.advertisement_display.start()
        self.led_board.run()
```

You feel good about yourself. You did an overhaul of the entire store theme, and you only had to change the code at a couple of places.

But you realize you also want to change things up when it's Easter, Halloween, Valentine's Day, etc. This means you have to go into your code and replace all of the concrete implementation calls. In the example above this is at only 3 places, but you can imagine in real-world complex code, the invocations of the object creation can happen at multiple places, and can span many more related objects. Think themed receipt, price displays, emails, etc. This can quickly spiral out of control.

Ideally, you'd want to just change it at one place and keep the rest of the code intact. This is where the `abstract factory` comes into play.

The abstract factory itself provides an interface with which you can create objects conforming to a specific interface itself. An example says more than a thousand words, so see below an example of our abstract factory interface:

```python
from abc import ABC, abstractmethod

class AbstractStoreFactory(ABC):

    @abstractmethod
    def create_background_music(self):
        raise NotImplementedError

    @abstractmethod
    def create_advertisement_display(self):
        raise NotImplementedError

    @abstractmethod
    def create_led_board(self):
        raise NotImplementedError
```
As you can see, the abstract factory allows us to create our background_music, advertisement_display and led_board objects, without knowing which concrete implementation we are dealing with. This is a Good Thing because it decouples the code from the specific implementations. An example for our normally themed store would look like:

```python
class StoreFactory(AbstractStoreFactory):
    def create_background_music(self):
        return BackgroundMusic()

    def create_advertisement_display(self):
        return AdvertisementDisplay()

    def create_led_board(self):
        return LedBoard()
```

while the Christmas themed store factory would look like

```python
class ChristmasStoreFactory(AbstractStoreFactory):
    def create_background_music(self):
        return ChristmasBackgroundMusic()

    def create_advertisement_display(self):
        return ChristmasAdvertisementDisplay()

    def create_led_board(self):
        return ChristmasLedBoard()
```

If we now inject the factory into our client, we can completely overhaul our entire store by just changing one variable at startup time: the factory.

```python
class StoreClient:
    def __init__(self, factory):
        self.factory = factory
        
        self.background_music = self.factory.create_background_music()
        self.advertisement_display = self.factory.create_advertisement_display()
        self.led_board = self.factory.create_led_board()

        self.background_music.play()
        self.advertisement_display.start()
        self.led_board.run()
```

```python
if __name__ == "__main__":
    factory = ChristmasStoreFactory()  # replace this with whatever factory you'd like
    store_client = StoreClient(factory)
```