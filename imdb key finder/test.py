 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import re
import csv
res = {
 "kind": "customsearch#search",
 "url": {
	"type": "application/json",
	"template": "https://www.googleapis.com/customsearch/v1?q={searchTerms}&num={count?}&start={startIndex?}&lr={language?}&safe={safe?}&cx={cx?}&cref={cref?}&sort={sort?}&filter={filter?}&gl={gl?}&cr={cr?}&googlehost={googleHost?}&c2coff={disableCnTwTranslation?}&hq={hq?}&hl={hl?}&siteSearch={siteSearch?}&siteSearchFilter={siteSearchFilter?}&exactTerms={exactTerms?}&excludeTerms={excludeTerms?}&linkSite={linkSite?}&orTerms={orTerms?}&relatedSite={relatedSite?}&dateRestrict={dateRestrict?}&lowRange={lowRange?}&highRange={highRange?}&searchType={searchType}&fileType={fileType?}&rights={rights?}&imgSize={imgSize?}&imgType={imgType?}&imgColorType={imgColorType?}&imgDominantColor={imgDominantColor?}&alt=json"
 },
 "queries": {
	"nextPage": [
	 {
		"title": "Google Custom Search - The Celluloid Closet",
		"totalResults": "6270",
		"searchTerms": "The Celluloid Closet",
		"count": 10,
		"startIndex": 11,
		"inputEncoding": "utf8",
		"outputEncoding": "utf8",
		"safe": "off",
		"cx": "009241977094486741223:3agszpaq5sy"
	 }
	],
	"request": [
	 {
		"title": "Google Custom Search - The Celluloid Closet",
		"totalResults": "6270",
		"searchTerms": "The Celluloid Closet",
		"count": 10,
		"startIndex": 1,
		"inputEncoding": "utf8",
		"outputEncoding": "utf8",
		"safe": "off",
		"cx": "009241977094486741223:3agszpaq5sy"
	 }
	]
 },
 "context": {
	"title": "Imdb"
 },
 "searchInformation": {
	"searchTime": 0.482974,
	"formattedSearchTime": "0.48",
	"totalResults": "6270",
	"formattedTotalResults": "6,270"
 },
 "items": [
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet (1995) - IMDb",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) - IMDb",
	 "link": "http://www.imdb.com/title/tt0112651/",
	 "displayLink": "www.imdb.com",
	 "snippet": "The Celluloid Closet Poster. A documentary surveying the various Hollywood \nscreen depictions of homosexuals and the attitudes behind them throughout the ...",
	 "htmlSnippet": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e Poster. A documentary surveying the various Hollywood \u003cbr\u003e\nscreen depictions of homosexuals and the attitudes behind them throughout the&nbsp;...",
	 "cacheId": "hdz-kklJj2MJ",
	 "formattedUrl": "www.imdb.com/title/tt0112651/",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/",
	 "pagemap": {
		"cse_image": [
		 {
			"src": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg"
		 }
		],
		"videoobject": [
		 {
			"duration": "T101M0S",
			"url": "http://www.imdb.com/offsite/?page-action=watch-aiv&token=BCYrGNP0p_Kw5UKsr4VzsLOj8uhq1H-tA4J4pYkcujOFXXrdBgFtu-3KLGSdqNzkN983YlzXimOB%0D%0A6TorV7G3kBsAjGmzc_8kFcZM_Lf1uLKv876dNxaXRIIoIS5v55j9LET5bfmbjB6w3aOBj_aNGOx1%0D%0AdiZIWBVLiInIvVlFT_TNWPsHrolDZcVJzXQPbibub5oIv-qNRoFKntfTfNCG6LKPaQrnQod7zyaN%0D%0A2ASna5y5Gpgz3okznZoW0TfX_wcUW74_FTZOHpRLVpQzEIIX2xQ9oCeH9TOv4XFxZ_p6r_d5PJA%0D%0A&ref_=tt_pv_vi_aiv_1",
			"image": "http://ia.media-imdb.com/images/G/01/imdb/images/nopicture/small/no-video-slate-856072904._CB379390253_.png"
		 },
		 {
			"duration": "T2M9S",
			"url": "http://www.imdb.com/video/screenplay/vi2576744729?ref_=tt_pv_vi_aiv_2",
			"image": "http://ia.media-imdb.com/images/G/01/imdb/images/nopicture/small/no-video-slate-856072904._CB379390253_.png"
		 }
		],
		"organization": [
		 {
			"url": "Arte",
			"name": "Arte"
		 },
		 {
			"url": "Brillstein-Grey Entertainment",
			"name": "Brillstein-Grey Entertainment"
		 },
		 {
			"url": "Channel Four Films",
			"name": "Channel Four Films"
		 }
		],
		"person": [
		 {
			"url": "Rob Epstein",
			"name": "Rob Epstein"
		 },
		 {
			"url": "Jeffrey Friedman",
			"name": "Jeffrey Friedman"
		 },
		 {
			"url": "Vito Russo",
			"name": "Vito Russo"
		 },
		 {
			"url": "Rob Epstein",
			"name": "Rob Epstein"
		 },
		 {
			"url": "Lily Tomlin",
			"name": "Lily Tomlin"
		 },
		 {
			"url": "Tony Curtis",
			"name": "Tony Curtis"
		 },
		 {
			"url": "Susie Bright",
			"name": "Susie Bright"
		 },
		 {
			"url": "Lily Tomlin",
			"name": "Lily Tomlin"
		 },
		 {
			"url": "Tony Curtis",
			"name": "Tony Curtis"
		 },
		 {
			"url": "Susie Bright",
			"name": "Susie Bright"
		 },
		 {
			"url": "Arthur Laurents",
			"name": "Arthur Laurents"
		 },
		 {
			"url": "Armistead Maupin",
			"name": "Armistead Maupin"
		 },
		 {
			"url": "Whoopi Goldberg",
			"name": "Whoopi Goldberg"
		 },
		 {
			"url": "Jan Oxenberg",
			"name": "Jan Oxenberg"
		 },
		 {
			"url": "Harvey Fierstein",
			"name": "Harvey Fierstein"
		 },
		 {
			"url": "Quentin Crisp",
			"name": "Quentin Crisp"
		 },
		 {
			"url": "Richard Dyer",
			"name": "Richard Dyer"
		 },
		 {
			"url": "Jay Presson Allen",
			"name": "Jay Presson Allen"
		 },
		 {
			"url": "Mrs. Gustav Ketterer",
			"name": "Mrs. Gustav Ketterer"
		 },
		 {
			"url": "Gore Vidal",
			"name": "Gore Vidal"
		 },
		 {
			"url": "Will H. Hays",
			"name": "Will H. Hays"
		 },
		 {
			"url": "Farley Granger",
			"name": "Farley Granger"
		 }
		],
		"cse_thumbnail": [
		 {
			"width": "163",
			"height": "310",
			"src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR5QIrEuH8KdHGUMJDjli1ZqLFul8F7cD_0fPUd7D_xgLeRtShTbsRkFVtK"
		 }
		],
		"aggregaterating": [
		 {
			"ratingvalue": "7.8",
			"bestrating": "10",
			"ratingcount": "4,956",
			"reviewcount": "46 user"
		 }
		],
		"movie": [
		 {
			"name": "The Celluloid Closet (1995)",
			"contentrating": "R",
			"duration": "PT102M",
			"genre": "Documentary",
			"datepublished": "1996-03-15",
			"image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY268_CR1,0,182,268_AL_.jpg",
			"description": "A documentary surveying the various Hollywood screen depictions of homosexuals and the attitudes behind them throughout the history of North American film.",
			"headline": "Exclusive: 14 Finalists Compete for $300K in San Francisco Film Society Grants",
			"provider": "Thompson on Hollywood",
			"url": "Show HTML",
			"awards": "Nominated for 4 Primetime Emmys.",
			"thumbnailurl": "http://www.imdb.com/media/rm3986726656/tt0112651?ref_=tt_pv_md_1",
			"keywords": "Plot Keywords: gay | lesbian | reference to eve arden | reference to bette davis | gay subtext | See All (32) »"
		 }
		],
		"rating": [
		 {
			"worstrating": "1",
			"ratingvalue": "10",
			"bestrating": "10"
		 }
		],
		"metatags": [
		 {
			"apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt0112651?src=mdot",
			"og:url": "http://www.imdb.com/title/tt0112651/",
			"theme-color": "#000000",
			"pageid": "tt0112651",
			"pagetype": "title",
			"subpagetype": "main",
			"og:image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg",
			"og:type": "video.movie",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet (1995)",
			"og:site_name": "IMDb",
			"title": "The Celluloid Closet (1995) - IMDb",
			"og:description": "Directed by Rob Epstein, Jeffrey Friedman.  With Lily Tomlin, Tony Curtis, Susie Bright, Arthur Laurents. A documentary surveying the various Hollywood screen depictions of homosexuals and the attitudes behind them throughout the history of North American film.",
			"request_id": "161BC9SVQCCW31H861P4"
		 }
		],
		"moviereview": [
		 {
			"ratingstars": "4.0",
			"best": "10",
			"originalrating": "7.8",
			"votes": "4,956",
			"ratingcount": "46 user",
			"image_href": "http://ia.media-imdb.com/images/G/01/imdb/images/nopicture/small/unknown-1394846836._CB379391227_.png",
			"name": "The Celluloid Closet (1995)",
			"release_date": "1996-03-15",
			"release_year": "1996",
			"runtime": "PT102M",
			"genre": "Documentary/History",
			"directed_by": "Rob Epstein",
			"starring": "Lily Tomlin, Tony Curtis, Susie Bright",
			"summary": "A comprehensive documentary of the history of gays and lesbians in cinema, from negative to positive reflections of gay characters and the troubles of..."
		 }
		],
		"review": [
		 {
			"name": "Out of the closet and into the picture",
			"author": "jotix100",
			"datepublished": "2005-09-17",
			"reviewbody": "\"The Celluloid Closet\" is a documentary that dares to go where others haven't gone before. Hollywood, that dream factory, has always been a magnet for the artistic gays and lesbians that have..."
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet (1995)",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995)",
	 "link": "http://www.imdb.com/title/tt0112651/combined",
	 "displayLink": "www.imdb.com",
	 "snippet": "The Celluloid Closet -- Narrated by Lily Tomlin, this exuberant, eye-opening · The \nCelluloid Closet -- A documentary surveying the various Hollywood screen ...",
	 "htmlSnippet": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e -- Narrated by Lily Tomlin, this exuberant, eye-opening &middot; \u003cb\u003eThe\u003c/b\u003e \u003cbr\u003e\n\u003cb\u003eCelluloid Closet\u003c/b\u003e -- A documentary surveying the various Hollywood screen&nbsp;...",
	 "cacheId": "buINqznOgHkJ",
	 "formattedUrl": "www.imdb.com/title/tt0112651/combined",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/combined",
	 "pagemap": {
		"cse_image": [
		 {
			"src": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_BR-65_CT-15_SP198,198,0,C,0,0,0_CR39,54,120,90_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,120,90_PIimdb-goldbutton-big,BottomRight,-1,-1_ZAFull%2520Movie,2,61,16,118,verdenab,8,255,255,255,1_ZAat%2520Amazon%2520%25BB,2,1,14,118,verdenab,7,255,255,255,1_ZA101%253A00,84,1,14,36,verdenab,7,255,255,255,1_.jpg"
		 }
		],
		"cse_thumbnail": [
		 {
			"width": "96",
			"height": "72",
			"src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcScpSprjKqChpyhvbE3tUOBbtnvhQs8oi-4D7LdZPgmc3CeZ3Zp3XlO"
		 }
		],
		"metatags": [
		 {
			"og:url": "http://www.imdb.com/title/tt0112651/combined",
			"title": "The Celluloid Closet (1995)",
			"og:image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1._SX96_SY140_.jpg",
			"application-name": "IMDb",
			"msapplication-tooltip": "IMDb Web App",
			"msapplication-window": "width=1500;height=900",
			"msapplication-task": "name=Find Movie Showtimes;action-uri=/showtimes/;icon-uri=http://i.media-imdb.com/images/SFff39adb4d259f3c3fd166853a6714a32/favicon.ico",
			"og:type": "movie",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet (1995)",
			"og:site_name": "IMDb"
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet (1995) - Full Cast & Crew - IMDb",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) - Full Cast &amp; Crew - IMDb",
	 "link": "http://www.imdb.com/title/tt0112651/fullcredits/",
	 "displayLink": "www.imdb.com",
	 "snippet": "The Celluloid Closet (1995) cast and crew credits, including actors, actresses, \ndirectors, writers and more.",
	 "htmlSnippet": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) cast and crew credits, including actors, actresses, \u003cbr\u003e\ndirectors, writers and more.",
	 "cacheId": "UZ17uunYJ0gJ",
	 "formattedUrl": "www.imdb.com/title/tt0112651/fullcredits/",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/fullcredits/",
	 "pagemap": {
		"cse_image": [
		 {
			"src": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg"
		 }
		],
		"person": [
		 {
			"url": "Lily Tomlin",
			"name": "Lily Tomlin"
		 },
		 {
			"url": "Tony Curtis",
			"name": "Tony Curtis"
		 },
		 {
			"url": "Susie Bright",
			"name": "Susie Bright"
		 },
		 {
			"url": "Arthur Laurents",
			"name": "Arthur Laurents"
		 },
		 {
			"url": "Armistead Maupin",
			"name": "Armistead Maupin"
		 },
		 {
			"url": "Whoopi Goldberg",
			"name": "Whoopi Goldberg"
		 },
		 {
			"url": "Jan Oxenberg",
			"name": "Jan Oxenberg"
		 },
		 {
			"url": "Harvey Fierstein",
			"name": "Harvey Fierstein"
		 },
		 {
			"url": "Quentin Crisp",
			"name": "Quentin Crisp"
		 },
		 {
			"url": "Richard Dyer",
			"name": "Richard Dyer"
		 },
		 {
			"url": "Jay Presson Allen",
			"name": "Jay Presson Allen"
		 },
		 {
			"url": "Mrs. Gustav Ketterer",
			"name": "Mrs. Gustav Ketterer"
		 },
		 {
			"url": "Gore Vidal",
			"name": "Gore Vidal"
		 },
		 {
			"url": "Will H. Hays",
			"name": "Will H. Hays"
		 },
		 {
			"url": "Farley Granger",
			"name": "Farley Granger"
		 },
		 {
			"url": "Paul Rudnick",
			"name": "Paul Rudnick"
		 },
		 {
			"url": "Shirley MacLaine",
			"name": "Shirley MacLaine"
		 },
		 {
			"url": "Barry Sandler",
			"name": "Barry Sandler"
		 },
		 {
			"url": "Mart Crowley",
			"name": "Mart Crowley"
		 },
		 {
			"url": "Antonio Fargas",
			"name": "Antonio Fargas"
		 },
		 {
			"url": "Tom Hanks",
			"name": "Tom Hanks"
		 },
		 {
			"url": "Ron Nyswaner",
			"name": "Ron Nyswaner"
		 },
		 {
			"url": "Daniel Melnick",
			"name": "Daniel Melnick"
		 },
		 {
			"url": "Harry Hamlin",
			"name": "Harry Hamlin"
		 },
		 {
			"url": "John Schlesinger",
			"name": "John Schlesinger"
		 },
		 {
			"url": "Susan Sarandon",
			"name": "Susan Sarandon"
		 },
		 {
			"url": "Demetrius Alexis",
			"name": "Demetrius Alexis"
		 },
		 {
			"url": "Judith Anderson",
			"name": "Judith Anderson"
		 },
		 {
			"url": "Richard Arlen",
			"name": "Richard Arlen"
		 },
		 {
			"url": "Antonio Banderas",
			"name": "Antonio Banderas"
		 },
		 {
			"url": "Joseph Breen",
			"name": "Joseph Breen"
		 },
		 {
			"url": "Steve Buscemi",
			"name": "Steve Buscemi"
		 },
		 {
			"url": "Eric Campbell",
			"name": "Eric Campbell"
		 },
		 {
			"url": "Margery Chapin",
			"name": "Margery Chapin"
		 },
		 {
			"url": "Charles Chaplin",
			"name": "Charles Chaplin"
		 },
		 {
			"url": "Marguerite Churchill",
			"name": "Marguerite Churchill"
		 },
		 {
			"url": "Gary Cooper",
			"name": "Gary Cooper"
		 },
		 {
			"url": "Tyrell Davis",
			"name": "Tyrell Davis"
		 },
		 {
			"url": "Sandy Dennis",
			"name": "Sandy Dennis"
		 },
		 {
			"url": "Marlene Dietrich",
			"name": "Marlene Dietrich"
		 },
		 {
			"url": "Divine",
			"name": "Divine"
		 },
		 {
			"url": "Joan Fontaine",
			"name": "Joan Fontaine"
		 },
		 {
			"url": "Gloria Holden",
			"name": "Gloria Holden"
		 },
		 {
			"url": "Edward Everett Horton",
			"name": "Edward Everett Horton"
		 },
		 {
			"url": "Al Jolson",
			"name": "Al Jolson"
		 },
		 {
			"url": "John Marlowe",
			"name": "John Marlowe"
		 },
		 {
			"url": "Josephine McKim",
			"name": "Josephine McKim"
		 },
		 {
			"url": "Liza Minnelli",
			"name": "Liza Minnelli"
		 },
		 {
			"url": "Dermot Mulroney",
			"name": "Dermot Mulroney"
		 },
		 {
			"url": "Maureen O'Sullivan",
			"name": "Maureen O'Sullivan"
		 },
		 {
			"url": "Dick Powell",
			"name": "Dick Powell"
		 },
		 {
			"url": "Edna Purviance",
			"name": "Edna Purviance"
		 },
		 {
			"url": "Charles 'Buddy' Rogers",
			"name": "Charles 'Buddy' Rogers"
		 },
		 {
			"url": "Stewart Stern",
			"name": "Stewart Stern"
		 },
		 {
			"url": "Sharon Stone",
			"name": "Sharon Stone"
		 },
		 {
			"url": "Johnny Weissmuller",
			"name": "Johnny Weissmuller"
		 },
		 {
			"url": "Michael York",
			"name": "Michael York"
		 }
		],
		"movie": [
		 {
			"image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY98_CR0,0,67,98_AL_.jpg",
			"name": "The Celluloid Closet (1995)",
			"url": "The Celluloid Closet"
		 }
		],
		"metatags": [
		 {
			"apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt0112651?src=mdot",
			"og:url": "http://www.imdb.com/title/tt0112651/fullcredits/",
			"theme-color": "#000000",
			"pageid": "tt0112651",
			"pagetype": "title",
			"subpagetype": "fullcredits",
			"og:image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg",
			"og:type": "video.movie",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet (1995)",
			"og:site_name": "IMDb",
			"title": "The Celluloid Closet (1995) - IMDb",
			"og:description": "The Celluloid Closet (1995) cast and crew credits, including actors, actresses, directors, writers and more.",
			"request_id": "0M4YKXR1XEBZTY17T859"
		 }
		],
		"moviereview": [
		 {
			"image_href": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY98_CR0,0,67,98_AL_.jpg",
			"name": "The Celluloid Closet (1995)",
			"starring": "Lily Tomlin, Tony Curtis, Susie Bright"
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet (1995) - Quotes - IMDb",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) - Quotes - IMDb",
	 "link": "http://www.imdb.com/title/tt0112651/quotes",
	 "displayLink": "www.imdb.com",
	 "snippet": "The Celluloid Closet (1995) Quotes on IMDb: Memorable quotes and exchanges \nfrom movies, TV series and more...",
	 "htmlSnippet": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) Quotes on IMDb: Memorable quotes and exchanges \u003cbr\u003e\nfrom movies, TV series and more...",
	 "cacheId": "el5dlnSLWmoJ",
	 "formattedUrl": "www.imdb.com/title/tt0112651/quotes",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/quotes",
	 "pagemap": {
		"cse_image": [
		 {
			"src": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg"
		 }
		],
		"cse_thumbnail": [
		 {
			"width": "163",
			"height": "310",
			"src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR5QIrEuH8KdHGUMJDjli1ZqLFul8F7cD_0fPUd7D_xgLeRtShTbsRkFVtK"
		 }
		],
		"movie": [
		 {
			"image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY98_CR0,0,67,98_AL_.jpg",
			"name": "The Celluloid Closet (1995)",
			"url": "The Celluloid Closet"
		 }
		],
		"metatags": [
		 {
			"apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt0112651?src=mdot",
			"og:url": "http://www.imdb.com/title/tt0112651/quotes",
			"theme-color": "#000000",
			"pageid": "tt0112651",
			"pagetype": "title",
			"subpagetype": "quotes",
			"og:image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg",
			"og:type": "video.movie",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet (1995)",
			"og:site_name": "IMDb",
			"title": "The Celluloid Closet (1995) - IMDb",
			"og:description": "The Celluloid Closet (1995) Quotes on IMDb: Memorable quotes and exchanges from movies, TV series and more...",
			"request_id": "0S1E6M9TS54TXPZ6NSST"
		 }
		],
		"moviereview": [
		 {
			"image_href": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY98_CR0,0,67,98_AL_.jpg",
			"name": "The Celluloid Closet (1995)"
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet Reviews & Ratings - IMDb",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e Reviews &amp; Ratings - IMDb",
	 "link": "http://www.imdb.com/title/tt0112651/reviews",
	 "displayLink": "www.imdb.com",
	 "snippet": "Review: Out of the closet and into the picture - \"The Celluloid Closet\" is a \ndocumentary that dares to go where others haven't gone before. Hollywood...",
	 "htmlSnippet": "Review: Out of the closet and into the picture - &quot;\u003cb\u003eThe Celluloid Closet\u003c/b\u003e&quot; is a \u003cbr\u003e\ndocumentary that dares to go where others haven&#39;t gone before. Hollywood...",
	 "cacheId": "eimlGmNrb-4J",
	 "formattedUrl": "www.imdb.com/title/tt0112651/reviews",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/reviews",
	 "pagemap": {
		"cse_image": [
		 {
			"src": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1._SX96_SY140_.jpg"
		 }
		],
		"cse_thumbnail": [
		 {
			"width": "76",
			"height": "112",
			"src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTxVNmqEs43e9UNztxtPeHXv8_yihWrGliweFQNy3LZLCmU2epO_t1MoQ"
		 }
		],
		"metatags": [
		 {
			"og:url": "http://www.imdb.com/title/tt0112651/reviews",
			"title": "The Celluloid Closet  Reviews & Ratings - IMDb",
			"application-name": "IMDb",
			"msapplication-tooltip": "IMDb Web App",
			"msapplication-window": "width=1500;height=900",
			"msapplication-task": "name=Find Movie Showtimes;action-uri=/showtimes/;icon-uri=http://i.media-imdb.com/images/SFff39adb4d259f3c3fd166853a6714a32/favicon.ico",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet  Reviews & Ratings - IMDb",
			"og:site_name": "IMDb"
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet (1995) - Connections - IMDb",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) - Connections - IMDb",
	 "link": "http://www.imdb.com/title/tt0112651/movieconnections",
	 "displayLink": "www.imdb.com",
	 "snippet": "The Celluloid Closet (1995) Connections on IMDb: Referenced in, Featured in, \nSpoofed and more...",
	 "htmlSnippet": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) Connections on IMDb: Referenced in, Featured in, \u003cbr\u003e\nSpoofed and more...",
	 "cacheId": "r7xcqyLhi7EJ",
	 "formattedUrl": "www.imdb.com/title/tt0112651/movieconnections",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/movieconnections",
	 "pagemap": {
		"cse_image": [
		 {
			"src": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg"
		 }
		],
		"cse_thumbnail": [
		 {
			"width": "163",
			"height": "310",
			"src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR5QIrEuH8KdHGUMJDjli1ZqLFul8F7cD_0fPUd7D_xgLeRtShTbsRkFVtK"
		 }
		],
		"movie": [
		 {
			"image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY98_CR0,0,67,98_AL_.jpg",
			"name": "The Celluloid Closet (1995)",
			"url": "The Celluloid Closet"
		 }
		],
		"metatags": [
		 {
			"apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt0112651?src=mdot",
			"og:url": "http://www.imdb.com/title/tt0112651/movieconnections",
			"theme-color": "#000000",
			"pageid": "tt0112651",
			"pagetype": "title",
			"subpagetype": "connections",
			"og:image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg",
			"og:type": "video.movie",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet (1995)",
			"og:site_name": "IMDb",
			"title": "The Celluloid Closet (1995) - IMDb",
			"og:description": "The Celluloid Closet (1995) Connections on IMDb: Referenced in, Featured in, Spoofed and more...",
			"request_id": "0QJ3JVN0MDYXJ4QNFW0A"
		 }
		],
		"moviereview": [
		 {
			"image_href": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY98_CR0,0,67,98_AL_.jpg",
			"name": "The Celluloid Closet (1995)"
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet (1995) - News",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) - News",
	 "link": "http://www.imdb.com/title/tt0112651/news?year=2012",
	 "displayLink": "www.imdb.com",
	 "snippet": "The Celluloid Closet on IMDb: Movies, TV, Celebs, and more...",
	 "htmlSnippet": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e on IMDb: Movies, TV, Celebs, and more...",
	 "cacheId": "5LCohbpy19EJ",
	 "formattedUrl": "www.imdb.com/title/tt0112651/news?year=2012",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/news?year=2012",
	 "pagemap": {
		"metatags": [
		 {
			"og:url": "http://www.imdb.com/title/tt0112651/news?year=2012",
			"title": "The Celluloid Closet (1995) - News",
			"application-name": "IMDb",
			"msapplication-tooltip": "IMDb Web App",
			"msapplication-window": "width=1500;height=900",
			"msapplication-task": "name=Find Movie Showtimes;action-uri=/showtimes/;icon-uri=http://i.media-imdb.com/images/SFff39adb4d259f3c3fd166853a6714a32/favicon.ico",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet (1995) - News",
			"og:site_name": "IMDb"
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet (1995) - Soundtracks - IMDb",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) - Soundtracks - IMDb",
	 "link": "http://www.imdb.com/title/tt0112651/soundtrack",
	 "displayLink": "www.imdb.com",
	 "snippet": "The Celluloid Closet (1995) SoundTracks on IMDb: Memorable quotes and \nexchanges from movies, TV series and more...",
	 "htmlSnippet": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) SoundTracks on IMDb: Memorable quotes and \u003cbr\u003e\nexchanges from movies, TV series and more...",
	 "cacheId": "uO_YBbXeCXoJ",
	 "formattedUrl": "www.imdb.com/title/tt0112651/soundtrack",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/soundtrack",
	 "pagemap": {
		"cse_image": [
		 {
			"src": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg"
		 }
		],
		"cse_thumbnail": [
		 {
			"width": "163",
			"height": "310",
			"src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR5QIrEuH8KdHGUMJDjli1ZqLFul8F7cD_0fPUd7D_xgLeRtShTbsRkFVtK"
		 }
		],
		"movie": [
		 {
			"image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY98_CR0,0,67,98_AL_.jpg",
			"name": "The Celluloid Closet (1995)",
			"url": "The Celluloid Closet"
		 }
		],
		"metatags": [
		 {
			"apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt0112651?src=mdot",
			"og:url": "http://www.imdb.com/title/tt0112651/soundtrack",
			"theme-color": "#000000",
			"pageid": "tt0112651",
			"pagetype": "title",
			"subpagetype": "soundtrack",
			"og:image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg",
			"og:type": "video.movie",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet (1995)",
			"og:site_name": "IMDb",
			"title": "The Celluloid Closet (1995) - IMDb",
			"og:description": "The Celluloid Closet (1995) SoundTracks on IMDb: Memorable quotes and exchanges from movies, TV series and more...",
			"request_id": "0C98A5HR1905BRMH9FPR"
		 }
		],
		"moviereview": [
		 {
			"image_href": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY98_CR0,0,67,98_AL_.jpg",
			"name": "The Celluloid Closet (1995)"
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet Reviews & Ratings - IMDb",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e Reviews &amp; Ratings - IMDb",
	 "link": "http://www.imdb.com/title/tt0112651/reviews-16",
	 "displayLink": "www.imdb.com",
	 "snippet": "Rob Epstein & Jeffrey Friedman's 1995 documentary \"The Celluloid Closet\" \nexamines the role of homosexuality throughout film history. From the silent era ...",
	 "htmlSnippet": "Rob Epstein &amp; Jeffrey Friedman&#39;s 1995 documentary &quot;\u003cb\u003eThe Celluloid Closet\u003c/b\u003e&quot; \u003cbr\u003e\nexamines the role of homosexuality throughout film history. From the silent era&nbsp;...",
	 "cacheId": "eVztiDiYm8EJ",
	 "formattedUrl": "www.imdb.com/title/tt0112651/reviews-16",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/reviews-16",
	 "pagemap": {
		"metatags": [
		 {
			"og:url": "http://www.imdb.com/title/tt0112651/reviews-16",
			"title": "The Celluloid Closet  Reviews & Ratings - IMDb",
			"application-name": "IMDb",
			"msapplication-tooltip": "IMDb Web App",
			"msapplication-window": "width=1500;height=900",
			"msapplication-task": "name=Find Movie Showtimes;action-uri=/showtimes/;icon-uri=http://i.media-imdb.com/images/SFff39adb4d259f3c3fd166853a6714a32/favicon.ico",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet  Reviews & Ratings - IMDb",
			"og:site_name": "IMDb"
		 }
		]
	 }
	},
	{
	 "kind": "customsearch#result",
	 "title": "The Celluloid Closet (1995) - IMDb",
	 "htmlTitle": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e (1995) - IMDb",
	 "link": "http://www.imdb.com/title/tt0112651/?_encoding=UTF8&ref_=amzn_dp_dvd",
	 "displayLink": "www.imdb.com",
	 "snippet": "The Celluloid Closet -- Narrated by Lily Tomlin, this exuberant, eye-opening · The \nCelluloid Closet -- A documentary surveying the various Hollywood screen ...",
	 "htmlSnippet": "\u003cb\u003eThe Celluloid Closet\u003c/b\u003e -- Narrated by Lily Tomlin, this exuberant, eye-opening &middot; \u003cb\u003eThe\u003c/b\u003e \u003cbr\u003e\n\u003cb\u003eCelluloid Closet\u003c/b\u003e -- A documentary surveying the various Hollywood screen&nbsp;...",
	 "cacheId": "DHGhkjZOsW4J",
	 "formattedUrl": "www.imdb.com/title/tt0112651/?_encoding=UTF8&ref...dp...",
	 "htmlFormattedUrl": "www.imdb.com/title/tt0112651/?_encoding=UTF8&amp;ref...dp...",
	 "pagemap": {
		"cse_image": [
		 {
			"src": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY268_CR1,0,182,268_AL_.jpg"
		 }
		],
		"videoobject": [
		 {
			"duration": "T101M0S",
			"url": "http://www.imdb.com/offsite/?page-action=watch-aiv&token=BCYsuDaZDZ309OQ24oW4Ak-yS4tf3irJ3GP85ae9mChexvOfrrZs0ELinXo4UcSjId_LWfnsDazr%0D%0AYkkidvI7i036_UycDajWtOuJ8-btSGG7h86QwulM4hgrpAdtCY_Z3DQD8ZcLkp3Weh9CKjiEwmJy%0D%0Afku6j5_Cl6nYCvrFJzqABfS163-uIUqhhW80yOi8ha5WcGFemLc55eAvkpn-mdSk5Mhm6ZDfh3TA%0D%0AFOnYWQCHHgeGFLRkqbzzluPy9-WsWYNSvqSbEE920VYKXq3L1X0cmf4jRpQLyGY4epGF9FtGOXo%0D%0A&ref_=tt_pv_vi_aiv_1",
			"image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_BR-65_CT-15_SP229,229,0,C,0,0,0_CR45,62,139,105_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,139,105_PIimdb-goldbutton-big,BottomRight,-1,-1_ZAFull%2520Movie,2,76,16,137,verdenab,8,255,255,255,1_ZAat%2520Amazon%2520%25BB,2,1,14,137,verdenab,7,255,255,255,1_ZA101:00,103,1,14,36,verdenab,7,255,255,255,1_.jpg"
		 },
		 {
			"duration": "T2M9S",
			"url": "http://www.imdb.com/video/screenplay/vi2576744729?ref_=tt_pv_vi_aiv_2",
			"image": "http://ia.media-imdb.com/images/M/MV5BMTYwNjc2MzEzOF5BMl5BanBnXkFtZTcwNDAxMTc2MQ@@._V1_SP229,229,0,C,0,0,0_CR45,62,139,105_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,139,105_PIimdb-bluebutton-big,BottomRight,-1,-1_ZATrailer,2,76,16,137,verdenab,8,255,255,255,1_ZAon%2520IMDb,2,1,14,137,verdenab,7,255,255,255,1_ZA02:09,103,1,14,36,verdenab,7,255,255,255,1_.jpg"
		 }
		],
		"organization": [
		 {
			"url": "Arte",
			"name": "Arte"
		 },
		 {
			"url": "Brillstein-Grey Entertainment",
			"name": "Brillstein-Grey Entertainment"
		 },
		 {
			"url": "Channel Four Films",
			"name": "Channel Four Films"
		 }
		],
		"person": [
		 {
			"url": "Rob Epstein",
			"name": "Rob Epstein"
		 },
		 {
			"url": "Jeffrey Friedman",
			"name": "Jeffrey Friedman"
		 },
		 {
			"url": "Vito Russo",
			"name": "Vito Russo"
		 },
		 {
			"url": "Rob Epstein",
			"name": "Rob Epstein"
		 },
		 {
			"url": "Lily Tomlin",
			"name": "Lily Tomlin"
		 },
		 {
			"url": "Tony Curtis",
			"name": "Tony Curtis"
		 },
		 {
			"url": "Susie Bright",
			"name": "Susie Bright"
		 },
		 {
			"url": "Lily Tomlin",
			"name": "Lily Tomlin"
		 },
		 {
			"url": "Tony Curtis",
			"name": "Tony Curtis"
		 },
		 {
			"url": "Susie Bright",
			"name": "Susie Bright"
		 },
		 {
			"url": "Arthur Laurents",
			"name": "Arthur Laurents"
		 },
		 {
			"url": "Armistead Maupin",
			"name": "Armistead Maupin"
		 },
		 {
			"url": "Whoopi Goldberg",
			"name": "Whoopi Goldberg"
		 },
		 {
			"url": "Jan Oxenberg",
			"name": "Jan Oxenberg"
		 },
		 {
			"url": "Harvey Fierstein",
			"name": "Harvey Fierstein"
		 },
		 {
			"url": "Quentin Crisp",
			"name": "Quentin Crisp"
		 },
		 {
			"url": "Richard Dyer",
			"name": "Richard Dyer"
		 },
		 {
			"url": "Jay Presson Allen",
			"name": "Jay Presson Allen"
		 },
		 {
			"url": "Mrs. Gustav Ketterer",
			"name": "Mrs. Gustav Ketterer"
		 },
		 {
			"url": "Gore Vidal",
			"name": "Gore Vidal"
		 },
		 {
			"url": "Will H. Hays",
			"name": "Will H. Hays"
		 },
		 {
			"url": "Farley Granger",
			"name": "Farley Granger"
		 }
		],
		"cse_thumbnail": [
		 {
			"width": "145",
			"height": "214",
			"src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQEVC0rPPbKmtDcIt-OBHWt7KNK9U-K9xuucEBd-a-AYu-cvRVU547et8gx"
		 }
		],
		"aggregaterating": [
		 {
			"ratingvalue": "7.8",
			"bestrating": "10",
			"ratingcount": "4,946",
			"reviewcount": "46 user"
		 }
		],
		"movie": [
		 {
			"name": "The Celluloid Closet (1995)",
			"contentrating": "R",
			"duration": "PT102M",
			"genre": "Documentary",
			"datepublished": "1996-03-15",
			"image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY268_CR1,0,182,268_AL_.jpg",
			"description": "A documentary surveying the various Hollywood screen depictions of homosexuals and the attitudes behind them throughout the history of North American film.",
			"headline": "Exclusive: 14 Finalists Compete for $300K in San Francisco Film Society Grants",
			"provider": "Thompson on Hollywood",
			"url": "Show HTML",
			"awards": "Nominated for 4 Primetime Emmys.",
			"thumbnailurl": "http://www.imdb.com/media/rm1357027840/tt0112651?ref_=tt_pv_md_1",
			"keywords": "Plot Keywords: gay | lesbian | reference to eve arden | reference to bette davis | gay subtext | See All (32) »"
		 }
		],
		"rating": [
		 {
			"worstrating": "1",
			"ratingvalue": "10",
			"bestrating": "10"
		 }
		],
		"metatags": [
		 {
			"apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt0112651?src=mdot",
			"og:url": "http://www.imdb.com/title/tt0112651/",
			"theme-color": "#000000",
			"pageid": "tt0112651",
			"pagetype": "title",
			"subpagetype": "main",
			"og:image": "http://ia.media-imdb.com/images/M/MV5BMTI2NjIzOTI5MV5BMl5BanBnXkFtZTcwNTcwNTEyMQ@@._V1_UY1200_CR97,0,630,1200_AL_.jpg",
			"og:type": "video.movie",
			"fb:app_id": "115109575169727",
			"og:title": "The Celluloid Closet (1995)",
			"og:site_name": "IMDb",
			"title": "The Celluloid Closet (1995) - IMDb",
			"og:description": "Directed by Rob Epstein, Jeffrey Friedman.  With Lily Tomlin, Tony Curtis, Susie Bright, Arthur Laurents. A documentary surveying the various Hollywood screen depictions of homosexuals and the attitudes behind them throughout the history of North American film.",
			"request_id": "0EQ8MGVCDZ3SH4RGFKE5"
		 }
		],
		"moviereview": [
		 {
			"ratingstars": "4.0",
			"best": "10",
			"originalrating": "7.8",
			"votes": "4,946",
			"ratingcount": "46 user",
			"image_href": "http://ia.media-imdb.com/images/M/MV5BMTc2Nzc4NTg0Nl5BMl5BanBnXkFtZTYwMzc2MjA5._V1_UX105_CR0,0,105,105_AL_.jpg",
			"name": "The Celluloid Closet (1995)",
			"release_date": "1996-03-15",
			"release_year": "1996",
			"runtime": "PT102M",
			"genre": "Documentary/History",
			"directed_by": "Rob Epstein",
			"starring": "Lily Tomlin, Tony Curtis, Susie Bright",
			"summary": "A comprehensive documentary of the history of gays and lesbians in cinema, from negative to positive reflections of gay characters and the troubles of..."
		 }
		],
		"review": [
		 {
			"name": "Out of the closet and into the picture",
			"author": "jotix100",
			"datepublished": "2005-09-17",
			"reviewbody": "\"The Celluloid Closet\" is a documentary that dares to go where others haven't gone before. Hollywood, that dream factory, has always been a magnet for the artistic gays and lesbians that have..."
		 }
		]
	 }
	}
 ]
}


key ={}
with open ('output2.csv', 'wb') as csvoutput: 
		fieldnames = ['Entity','url','Director','Year','Alias','IMDB URL','genre','Runtime']
		writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
		writer.writeheader()
		imdb_key =''
		response = res.get('items')
		if response:
			imdb_key =''
			for i in range(0,len(response)):
				flag = 0
				check = 0
				print "===================================="
				json_title = res['items'][i].get('title')
				json_title = re.sub(r'<.*?>','',json_title)
				print 'fetched title:',json_title

				json_director = res['items'][i]['snippet']
				json_director = re.sub(r'...','',json_director)
				json_director = re.search(r'Robert Epstein, Jeffrey Friedman',json_director)
			 
				if re.sub(r'\s+\(.*','',json_title).strip() == 'The Celluloid Closet':
					print "##"
					if json_director is None:
						print "###"
						try:
							print 'inside try'
							json_director = res['items'][i]['pagemap']['metatags'][0].get('og:description')
							json_director = re.search(r'Robert Epstein, Jeffrey Friedman',json_director)
							if json_director:
								print '####' 
								if json_director.group(0) == 'Robert Epstein, Jeffrey Friedman':
									print '#####'
									imdb_key = res['items'][i]['link']

									print imdb_key
									writer.writerow({'Entity':'The Celluloid Closet','Director':'Robert Epstein, Jeffrey Friedman','IMDB URL': imdb_key})
									check = 1
									break
								else:
									print "######"
							else:
									print "director not found:"
									flag = 1	
								
						except:
							print "Exception caught, no og:description"
							
				else:
					print 'no key found'
					flag = 1
			if flag == 1 and check == 0:
				print "NO == NO == No"
				print flag	
				writer.writerow({'Entity':'The Celluloid Closet','Director':'Robert Epstein, Jeffrey Friedman','IMDB URL': imdb_key})

		elif response is None:
			print 'No Response'
			writer.writerow({'Entity':'The Celluloid Closet','Director':'Robert Epstein, Jeffrey Friedman','IMDB URL': imdb_key})