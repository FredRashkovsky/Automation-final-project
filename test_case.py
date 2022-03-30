from HomePage import HomePage
from applitools.selenium import VisualGridRunner


class TestRestfulBooker:
    
    def setup_method(self):
        self.new_test = HomePage()
        self.new_test.setup(VisualGridRunner(1))
    
    def test_contect_us(self):
        self.new_test.contect_us()
    
    def test_book_room(self):
        self.new_test.book_room()
    
    def test_book_room_taken(self):
        self.new_test.book_room_taken()

    def teardown_method(self):
        self.new_test.eyes.close_async()
        self.new_test.driver.close()

