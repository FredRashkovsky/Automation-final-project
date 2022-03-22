from HomePage import HomePage

class TestRestfulBooker:
    
    def setup_method(self):
        self.new_test = HomePage()
    
    def test_contect_us(self):
        self.new_test.contect_us()
    
    def test_book_room(self):
        self.new_test.book_room()
    
    def test_book_room_taken(self):
        self.new_test.book_room_taken()

    def teardown_method(self):
        self.new_test.driver.close()

