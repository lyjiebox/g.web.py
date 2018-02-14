# -*- coding: UTF-8 -*-
import web
import sqlite3

# Global configuration
web.config.debug = False


# wpy0001
urls = (
'/', 'index',
# wpy0301
'/movie/(\d+)', 'movie',
)

# wpy0101
#movies = [
#	{
#		'title': 'Forrest Gump',
#		'year': 1994,
#	},
#	{
#		'title': 'Titanic',
#		'year':	1997,
#	},
#	{
#		'title': 'nn',
#		'year': 1999,
#	}
#]

# wpy0102
render = web.template.render('templates/')

# wpy0201
db = web.database(dbn='sqlite', db='MovieSite.db')


class index:
	def GET(self):

		# wpy0001
#		return 'hello world!'

		# wpy0101
#		page = ''
#		for m in movies:
#			page += '%s (%d)\n' % (m['title'], m['year'])
#		return page

		# wpy0102
#		return render.index(movies)

		# wpy0201
		movies = db.select('movie')
		return render.index(movies)

	def POST(self):

		# wpy0401
		data = web.input()
		condition = r'title like "%' + data.title + r'%"'
		movies = db.select('movie', where=condition)
		return render.index(movies)


# wpy0301
class movie:
	def GET(self, movieID):

		#movieID = int(movieID)

		# wpy0301
		#movie = db.select('movie', where='id=$movieID', vars=locals())[0]

		# wpy0301
		condition = 'id=' + movieID
		#print condition		# for debug
		movie = db.select('movie', where=condition)[0]
		return render.movie(movie)
		


if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()

