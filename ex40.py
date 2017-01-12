class Mystuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between\n"

	def apple(self):
		print "I AM CLASSY APPLES!"

thing = Mystuff()
thing.apple()
print thing.tangerine

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()




# https://www.youtube.com/watch?v=trOZBgZ8F_c
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def eat(self, food):
        if food == 'apple':
            self.health -= 100
        elif food == 'ham':
            self.health += 20
Bob = Hero('Bob')
print Bob.name
print Bob.health
Bob.eat('apple')
print Bob.health
Bob.eat('ham')
print Bob.health
