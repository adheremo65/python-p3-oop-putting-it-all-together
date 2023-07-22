#!/usr/bin/env python3

class Book:
    def __init__(self, title="", page_count=0):
        self.title = title
        self._page_count = page_count

    def get_value(self):
        return self._page_count

    def set_value(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
   
    page_count = property(get_value, set_value)
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    
        