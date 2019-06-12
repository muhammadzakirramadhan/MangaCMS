

from .DbLoader import DbLoader
from .ContentLoader import ContentLoader

import settings

import runStatus

import MangaCMS.ScrapePlugins.RunBase

class Runner(MangaCMS.ScrapePlugins.RunBase.ScraperBase):


	loggerPath = "Main.Manga.Pururin.Run"
	pluginName = "Pururin"


	sourceName = "Pururin"
	feedLoader = DbLoader
	contentLoader = ContentLoader





if __name__ == "__main__":
	import utilities.testBase as tb

	with tb.testSetup():
		mon = Runner()
		mon.go()

