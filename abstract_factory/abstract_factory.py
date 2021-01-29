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


# Note that we purposely choose for different interfaces for the different parts
# although they all have some kind of 'start-up' method. That is not what this
# pattern is about.


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


class BackgroundMusic(AbstractBackgroundMusic):
    def play(self):
        print("Playing typical store jingles.")


class AdvertisementDisplay(AbstractAdvertisementDisplay):
    def start(self):
        print("Check out our bakery, 5 donuts for the price of 4")


class LedBoard(AbstractLedBoard):
    def run(self):
        print("Welcome to our store during a normal time of the year!")


class StoreFactory(AbstractStoreFactory):
    def create_background_music(self):
        return BackgroundMusic()

    def create_advertisement_display(self):
        return AdvertisementDisplay()

    def create_led_board(self):
        return LedBoard()


class ChristmasBackgroundMusic(AbstractBackgroundMusic):
    def play(self):
        print("Playing 'All I want for Christmas is you' on repeat")


class ChristmasAdvertisementDisplay(AbstractAdvertisementDisplay):
    def start(self):
        print("Check out all these Christmas deals we have for you!")


class ChristmasLedBoard(AbstractLedBoard):
    def run(self):
        print("Merry Christmas")


class ChristmasStoreFactory(AbstractStoreFactory):
    def create_background_music(self):
        return ChristmasBackgroundMusic()

    def create_advertisement_display(self):
        return ChristmasAdvertisementDisplay()

    def create_led_board(self):
        return ChristmasLedBoard()


class StoreClient:
    def __init__(self, factory):
        self.factory = factory

        self.background_music = self.factory.create_background_music()
        self.advertisement_display = self.factory.create_advertisement_display()
        self.led_board = self.factory.create_led_board()

        self.background_music.play()
        self.advertisement_display.start()
        self.led_board.run()


if __name__ == "__main__":
    # Uncomment the factory you'd want to use, and comment the other out
    factory = StoreFactory()
    # factory = ChristmasStoreFactory()
    store_client = StoreClient(factory)
