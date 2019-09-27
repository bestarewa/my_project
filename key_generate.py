#usr/bin/env python3 
'''
__author__ = 'abba y abdullahi ,lastloaded@gmail.com'
'''
import random

class Key:
    def __init__(self,key=''):
        if key == '':
            self.Key = self.generate()
        else:
            self.key = key.lower()
    def verify(self):
        score = 0
        check_digit = self.Key[0]
        check_digit_count = 0
        chunks = self.key.split('_')
        for chunk in chunks:
            if len(chunk) != 4:
                return False
            for char in chunk:
                if char == check_digit:
                    check_digit_count += 1
                score += ord(char)
        if score == 1772 and check_digit_count == 3:
            return True
        return False
    def generate(self):
        key = ''
        chunk = ''
        check_digit_count = 0
        alphabet = 'abcdefghcijklmnopqrstuvwxyz1234567890'
        while True:
            while len(key) < 25:
                char = random.choice(alphabet)
                key += char
                chunk += char
                if len(chunk) == 4:
                    key += '_'
                    chunk = ''
            key = key[:-1]
            if  Key(key).verify():
                return key
            else:
                key = ''
    def __str__(self):
        valid = ' Invalid'
        if self.verify():
            valid = 'Valid'
        return self.key.upper() + ':' + valid

key = Key('aaaa-bbbb-cccc-dddd-1111')
print(Key())
