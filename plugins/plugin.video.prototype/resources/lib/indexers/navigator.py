# -*- coding: utf-8 -*-

'''
    prototype Add-on
    Copyright (C) 2016 prototype

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import os,sys,urlparse,base64

from resources.lib.modules import control
from resources.lib.modules import trakt
inprogress_db = control.setting('inprogress_db')

sysaddon = base64.b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnRlbXBsYXRlX2Iv==')

syshandle = int(sys.argv[1])

artPath = control.artPath()

addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')

movielist1 = control.setting('tmdb.movielist_name1')		
movielist2 = control.setting('tmdb.movielist_name2')		
movielist3 = control.setting('tmdb.movielist_name3')		
movielist4 = control.setting('tmdb.movielist_name4')		
movielist5 = control.setting('tmdb.movielist_name5')		
movielist6 = control.setting('tmdb.movielist_name6')		
movielist7 = control.setting('tmdb.movielist_name7')		
movielist8 = control.setting('tmdb.movielist_name8')		
movielist9 = control.setting('tmdb.movielist_name9')		
movielist10 = control.setting('tmdb.movielist_name10')

tvlist1 = control.setting('tmdb.tvlist_name1')		
tvlist2 = control.setting('tmdb.tvlist_name2')		
tvlist3 = control.setting('tmdb.tvlist_name3')		
tvlist4 = control.setting('tmdb.tvlist_name4')		
tvlist5 = control.setting('tmdb.tvlist_name5')		
tvlist6 = control.setting('tmdb.tvlist_name6')		
tvlist7 = control.setting('tmdb.tvlist_name7')		
tvlist8 = control.setting('tmdb.tvlist_name8')		
tvlist9 = control.setting('tmdb.tvlist_name9')		
tvlist10 = control.setting('tmdb.tvlist_name10')		
class navigator:
    def root(self):
        self.addDirectoryItem('[COLORcrimson]**[Direct Search]** !!REAL DEBRID REQUIRED!![/COLOR]', 'directs', 'direct.png', 'direct.png')
        self.addDirectoryItem('[COLORcrimson]**Providers**[/COLOR]', 'providers', 'providers.png', 'providers.png')
        self.addDirectoryItem('[COLORcrimson]Symbiotor[/COLOR] Settings', 'symbiotorSettings&query=0.0', 'tools.png', 'settings.png')
        self.addDirectoryItem('[COLORcrimson]**Random Sport Replays/IMDB Lists**[/COLOR]', 'lists', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem(32001, 'movieNavigator', 'movies.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'channels.png', 'DefaultTVShows.png')
        if not control.setting('movie.widget') == '0': self.addDirectoryItem('[COLORcrimson]Spotlight[/COLOR]', 'movieWidget', 'latest-movies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLORcrimson]New Movies[/COLOR]', 'movies&url=premiere', 'trending.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'years.png', 'DefaultTVShows.png')
        self.addDirectoryItem('[COLORcrimson]TMDB/Misc[/COLOR]', 'lists_navigator', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(32027, '[COLORcrimson]calendars[/COLOR]', 'networks.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(32007, '[COLORcrimson]channels[/COLOR]', 'channels.png', 'DefaultMovies.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'tools.png', 'DefaultAddonProgram.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.addDirectoryItem(32010, 'searchNavigator', 'search.png', 'DefaultFolder.png')
        self.addDirectoryItem('[COLORcrimson]Changelog[/COLOR]', 'ShowChangelog', 'icon.png', 'DefaultFolder.png')
        self.endDirectory()

    def movies(self, lite=False):
        if inprogress_db == 'true': self.addDirectoryItem("[COLORcrimson]In Progress[/COLOR]", 'movieProgress', 'trending.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson]Symbiotor Movies[/COLOR]', control.setting('library.symovie'), 'movies.png', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem('[COLORcrimson]Trending[/COLOR]', 'movies&url=trending', 'trending.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLORcrimson]Populars[/COLOR]', 'movies&url=popular', 'most-popular.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson]New Movies[/COLOR]', 'movies&url=premiere', 'trending.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLORcrimson]Top Rated[/COLOR]', 'movies&url=views', 'most-viewed.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson]In Theaters[/COLOR]', 'movies&url=theaters', 'in-theaters.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLORcrimson]Marvel Universe[/COLOR]', 'movies&url=tmdbmarvel', 'marvel.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLORcrimson]Oscar Winners[/COLOR]', 'movies&url=tmdboscars', 'oscars.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLORcrimson]Disney Collection[/COLOR]', 'movies&url=tmdbdisney', 'disney.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('[COLORcrimson]Genres[/COLOR]', 'movieGenres', 'genres.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson]Years[/COLOR]', 'movieYears', 'years.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson]Persons[/COLOR]', 'moviePersons', 'people.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson]Certificates[/COLOR]', 'movieCertificates', 'certificates.png', 'DefaultMovies.png')
        self.addDirectoryItem(32028, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'DefaultMovies.png')


        self.endDirectory()

    def lists_navigator(self):
        self.addDirectoryItem('[COLORcrimson][WATCHLIST] Movies[/COLOR]', 'movieFavourites', 'mymovies.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson][WATCHLIST] TV Shows[/COLOR]', 'tvFavourites', 'mymovies.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson][TMDB LIST] Movies[/COLOR]', 'movielist', 'movies.png', 'DefaultMovies.png')
        #self.addDirectoryItem('[COLORcrimson][TMDB LIST] Tv Shows[/COLOR]', 'tvlist', 'channels.png', 'DefaultTVShows.png')

        self.endDirectory()
	
    def mymovies(self):
        self.addDirectoryItem(movielist1, 'movies&url=mycustomlist1', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist2, 'movies&url=mycustomlist2', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist3, 'movies&url=mycustomlist3', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist4, 'movies&url=mycustomlist4', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist5, 'movies&url=mycustomlist5', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist6, 'movies&url=mycustomlist6', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist7, 'movies&url=mycustomlist7', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist8, 'movies&url=mycustomlist8', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist9, 'movies&url=mycustomlist9', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(movielist10, 'movies&url=mycustomlist10', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()

    def mytv(self):
        self.addDirectoryItem(tvlist1, 'tvshows&url=mycustomlist1', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist2, 'tvshows&url=mycustomlist2', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist3, 'tvshows&url=mycustomlist3', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist4, 'tvshows&url=mycustomlist4', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist5, 'tvshows&url=mycustomlist5', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist6, 'tvshows&url=mycustomlist6', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist7, 'tvshows&url=mycustomlist7', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist8, 'tvshows&url=mycustomlist8', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist9, 'tvshows&url=mycustomlist9', 'channels.png', 'DefaultTVShows.png')
        self.addDirectoryItem(tvlist10, 'tvshows&url=mycustomlist10', 'mymovies.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()

    def tvshows(self, lite=False):
        if inprogress_db == 'true': self.addDirectoryItem("[COLORcrimson]In Progress[/COLOR]", 'showsProgress', 'trending.png', 'DefaultMovies.png')
        self.addDirectoryItem('[COLORcrimson]Symbiotor Tv Shows[/COLOR]', control.setting('library.sytv'), 'tvshows.png', 'DefaultTVShows.png', isAction=False) 
        self.addDirectoryItem('[COLORcrimson]Featured[/COLOR]', 'tvshows&url=featured', 'most-popular.png', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem('[COLORcrimson]Populars[/COLOR]', 'tvshows&url=popular', 'most-viewed.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32019, 'tvshows&url=views', 'most-viewed.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'years.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32025, 'tvshows&url=active', 'years.png', 'DefaultTVShows.png')       
        self.addDirectoryItem(32023, 'tvshows&url=rating', 'featured.png', 'DefaultTVShows.png')
 
        self.addDirectoryItem(32011, 'tvGenres', 'genres.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32016, 'tvNetworks', 'networks.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32024, 'tvshows&url=airing', 'airing-today.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32027, 'calendars', 'networks.png', 'DefaultRecentlyAddedEpisodes.png')



        self.addDirectoryItem(32010, 'tvSearch', 'search.png', 'DefaultTVShows.png')

        self.endDirectory()

    def tools(self):
        self.addDirectoryItem('[B]URL RESOLVER[/B]: Settings', 'resolveurlsettings', 'tools.png', 'DefaultAddonProgram.png')

        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png')
        # self.addDirectoryItem(32044, 'openSettings&query=3.1', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Accounts', 'openSettings&query=2.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Providers', 'openSettings&query=3.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Debrid', 'openSettings&query=4.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Downloads', 'openSettings&query=5.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Subtitles', 'openSettings&query=6.0', 'tools.png', 'DefaultAddonProgram.png') 
        self.addDirectoryItem('[B]SETTINGS[/B]: Watchlist', 'openSettings&query=7.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Lists', 'openSettings&query=8.0', 'tools.png', 'DefaultAddonProgram.png')
		
        self.addDirectoryItem('[B]PROTOTYPE[/B]: Views', 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]PROTOTYPE[/B]: Clear Providers', 'clearSources', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]PROTOTYPE[/B]: Clear Cache', 'clearCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]BACKUP[/B]: Watchlist', 'backupwatchlist', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]RESTORE[/B]: Watchlist', 'restorewatchlist', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]PROTOTYPE[/B]: Clear Progress Database', 'clearProgress', 'tools.png', 'DefaultAddonProgram.png')
 
	
		
        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        # tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'search.png', 'DefaultMovies.png')
        self.addDirectoryItem(32002, 'tvSearch', 'search.png', 'DefaultTVShows.png')
        self.addDirectoryItem(32029, 'moviePerson', 'people-search.png', 'DefaultMovies.png')
        # self.addDirectoryItem(32030, 'tvPerson', 'people-search.png', 'DefaultTVShows.png')

        self.endDirectory()


    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'tvshow.poster': poster, 'season.poster': poster, 'banner': banner, 'tvshow.banner': banner, 'season.banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import cache
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def addDirectoryItem(self, name, query, thumb, icon, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self):
        # control.do_block_check(False)
        control.directory(syshandle, cacheToDisc=True)


