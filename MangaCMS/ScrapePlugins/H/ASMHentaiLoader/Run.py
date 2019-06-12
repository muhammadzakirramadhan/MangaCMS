

from .DbLoader import DbLoader
from .ContentLoader import ContentLoader

import runStatus

import MangaCMS.ScrapePlugins.RunBase

class Runner(MangaCMS.ScrapePlugins.RunBase.ScraperBase):


	loggerPath = "Main.Manga.ASMHentai.Run"
	pluginName = "ASMHentai"

	sourceName = "ASMHentai"

	feedLoader = DbLoader
	contentLoader = ContentLoader


if __name__ == "__main__":
	import utilities.testBase as tb

	with tb.testSetup():
		run = Runner()
		run.go()
