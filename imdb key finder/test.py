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
    "title": "Google Custom Search - Chance Jake Graf",
    "totalResults": "943",
    "searchTerms": "Chance Jake Graf",
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
    "title": "Google Custom Search - Chance Jake Graf",
    "totalResults": "943",
    "searchTerms": "Chance Jake Graf",
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
  "searchTime": 0.261493,
  "formattedSearchTime": "0.26",
  "totalResults": "943",
  "formattedTotalResults": "943"
 },
 "items": [
  {
   "kind": "customsearch#result",
   "title": "Jake Graf - IMDb",
   "htmlTitle": "\u003cb\u003eJake Graf\u003c/b\u003e - IMDb",
   "link": "http://www.imdb.com/name/nm4261422/",
   "displayLink": "www.imdb.com",
   "snippet": "Jake Graf, Actor: The Danish Girl. Jake Graf is an actor and writer, known for \nChance (2015), The Danish Girl (2015) and Dawn (2016).",
   "htmlSnippet": "\u003cb\u003eJake Graf\u003c/b\u003e, Actor: The Danish Girl. \u003cb\u003eJake Graf\u003c/b\u003e is an actor and writer, known for \u003cbr\u003e\n\u003cb\u003eChance\u003c/b\u003e (2015), The Danish Girl (2015) and Dawn (2016).",
   "cacheId": "JhN83vAuISoJ",
   "formattedUrl": "www.imdb.com/name/nm4261422/",
   "htmlFormattedUrl": "www.imdb.com/name/nm4261422/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY1200_CR164,0,630,1200_AL_.jpg"
     }
    ],
    "person": [
     {
      "role": "Actor"
     },
     {
      "image": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY317_CR19,0,214,317_AL_.jpg",
      "name": "Jake Graf",
      "jobtitle": "Actor",
      "description": "Jake Graf is an actor and writer, known for Chance (2015), The Danish Girl (2015) and Dawn (2016). See full bio »",
      "thumbnailurl": "http://www.imdb.com/media/rm952496896/nm4261422?ref_=nm_phs_md_1",
      "headline": "Lgbt festival taking five gay films global",
      "datepublished": "19 March 2015 9:21 AM, -05:00",
      "provider": "ScreenDaily",
      "url": "Watch Now"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzlnyzE8EJfydYmvosDfb5BPbgem1rbi1UyR3pJ8VSpMGEurOEjZxoxDg"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///name/nm4261422?src=mdot",
      "og:url": "http://www.imdb.com/name/nm4261422/",
      "theme-color": "#000000",
      "pageid": "nm4261422",
      "pagetype": "name",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY1200_CR164,0,630,1200_AL_.jpg",
      "og:type": "actor",
      "fb:app_id": "115109575169727",
      "og:title": "Jake Graf",
      "og:site_name": "IMDb",
      "title": "Jake Graf - IMDb",
      "og:description": "Jake Graf, Actor: The Danish Girl. Jake Graf is an actor and writer, known for Chance (2015), The Danish Girl (2015) and Dawn (2016).",
      "request_id": "0JNY96DJBE46GKM551GJ"
     }
    ],
    "hcard": [
     {
      "fn": "Jake Graf",
      "title": "Actor",
      "url": "http://www.imdb.com/video/user/vi4067727897?ref_=nm_demo_2",
      "photo": "http://ia.media-imdb.com/images/M/MV5BMjExNzUzMTAxOV5BMl5BanBnXkFtZTgwNjUwMTkxMzE@._V1_UX148_CR0,0,148,200_AL_.jpg"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Chance (2015) - IMDb",
   "htmlTitle": "\u003cb\u003eChance\u003c/b\u003e (2015) - IMDb",
   "link": "http://www.imdb.com/title/tt4070722/",
   "displayLink": "www.imdb.com",
   "snippet": "Directed by Jake Graf. With Jake Graf, Lewis Hancox, Clifford Hume, Amale \nMohamed. Sometimes, life gives you another Chance.",
   "htmlSnippet": "Directed by \u003cb\u003eJake Graf\u003c/b\u003e. With \u003cb\u003eJake Graf\u003c/b\u003e, Lewis Hancox, Clifford Hume, Amale \u003cbr\u003e\nMohamed. Sometimes, life gives you another \u003cb\u003eChance\u003c/b\u003e.",
   "cacheId": "7lMlmKC62zMJ",
   "formattedUrl": "www.imdb.com/title/tt4070722/",
   "htmlFormattedUrl": "www.imdb.com/title/tt4070722/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTcwOTgzMjk0OF5BMl5BanBnXkFtZTgwNDM0NzI2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg"
     }
    ],
    "organization": [
     {
      "url": "Up And Up Productions",
      "name": "Up And Up Productions"
     }
    ],
    "person": [
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Pablo Brandao",
      "name": "Pablo Brandao"
     },
     {
      "url": "Pablo Brandao",
      "name": "Pablo Brandao"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Lewis Hancox",
      "name": "Lewis Hancox"
     },
     {
      "url": "Clifford Hume",
      "name": "Clifford Hume"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Lewis Hancox",
      "name": "Lewis Hancox"
     },
     {
      "url": "Clifford Hume",
      "name": "Clifford Hume"
     },
     {
      "url": "Amale Mohamed",
      "name": "Amale Mohamed"
     },
     {
      "url": "Abs",
      "name": "Abs"
     },
     {
      "url": "Olivia James",
      "name": "Olivia James"
     },
     {
      "url": "Georgie Smart",
      "name": "Georgie Smart"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRCCTgDFBnwEq37X92-AHLrlwYkXEWauX8QI37BUU_L98B9ZzRl2ln4T_M"
     }
    ],
    "aggregaterating": [
     {
      "ratingvalue": "8.3",
      "bestrating": "10",
      "ratingcount": "7",
      "reviewcount": "4 critic"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt4070722?src=mdot",
      "og:url": "http://www.imdb.com/title/tt4070722/",
      "theme-color": "#000000",
      "pageid": "tt4070722",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTcwOTgzMjk0OF5BMl5BanBnXkFtZTgwNDM0NzI2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Chance (2015)",
      "og:site_name": "IMDb",
      "title": "Chance (2015) - IMDb",
      "og:description": "Directed by Jake Graf.  With Jake Graf, Lewis Hancox, Clifford Hume, Amale Mohamed. Sometimes, life gives you another Chance.",
      "request_id": "17WKN2X8267KDBQC87ZG"
     }
    ],
    "hcard": [
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_dr"
     },
     {
      "fn": "Pablo Brandao",
      "url": "http://www.imdb.com/name/nm6848330?ref_=tt_ov_wr"
     },
     {
      "fn": "Pablo Brandao",
      "url": "http://www.imdb.com/name/nm6848330?ref_=tt_ov_wr"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Lewis Hancox",
      "url": "http://www.imdb.com/name/nm7097831?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Clifford Hume",
      "url": "http://www.imdb.com/name/nm5405166?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422/?ref_=tt_cl_t1"
     },
     {
      "fn": "Lewis Hancox",
      "url": "http://www.imdb.com/name/nm7097831/?ref_=tt_cl_t2"
     },
     {
      "fn": "Clifford Hume",
      "url": "http://www.imdb.com/name/nm5405166/?ref_=tt_cl_t3"
     },
     {
      "fn": "Amale Mohamed",
      "url": "http://www.imdb.com/name/nm6924652/?ref_=tt_cl_t4"
     },
     {
      "fn": "Abs",
      "nickname": "Abs",
      "url": "http://www.imdb.com/name/nm7114222/?ref_=tt_cl_t5"
     },
     {
      "fn": "Olivia James",
      "url": "http://www.imdb.com/name/nm7114322/?ref_=tt_cl_t6"
     },
     {
      "fn": "Georgie Smart",
      "url": "http://www.imdb.com/name/nm6604103/?ref_=tt_cl_t7"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Jake Graf - IMDb",
   "htmlTitle": "\u003cb\u003eJake Graf\u003c/b\u003e - IMDb",
   "link": "http://www.imdb.com/name/nm4261422/?nmdp=1",
   "displayLink": "www.imdb.com",
   "snippet": "Jake Graf, Actor: Chance. Jake Graf is an actor and writer, known for Chance (\n2015), The Danish Girl (2015) and Dawn (2016).",
   "htmlSnippet": "Jake Graf, Actor: \u003cb\u003eChance\u003c/b\u003e. \u003cb\u003eJake Graf\u003c/b\u003e is an actor and writer, known for Chance (\u003cbr\u003e\n2015), The Danish Girl (2015) and Dawn (2016).",
   "cacheId": "AXwHk-GQQAQJ",
   "formattedUrl": "www.imdb.com/name/nm4261422/?nmdp=1",
   "htmlFormattedUrl": "www.imdb.com/name/nm4261422/?nmdp=1",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY1200_CR164,0,630,1200_AL_.jpg"
     }
    ],
    "person": [
     {
      "role": "Actor"
     },
     {
      "image": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY317_CR19,0,214,317_AL_.jpg",
      "name": "Jake Graf",
      "jobtitle": "Actor",
      "description": "Jake Graf is an actor and writer, known for Chance (2015), The Danish Girl (2015) and Dawn (2016). See full bio »",
      "thumbnailurl": "http://www.imdb.com/media/rm952496896/nm4261422?ref_=nm_phs_md_1",
      "headline": "Lgbt festival taking five gay films global",
      "datepublished": "19 March 2015 9:21 AM, -05:00",
      "provider": "ScreenDaily",
      "url": "Watch Now"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzlnyzE8EJfydYmvosDfb5BPbgem1rbi1UyR3pJ8VSpMGEurOEjZxoxDg"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///name/nm4261422?src=mdot",
      "og:url": "http://www.imdb.com/name/nm4261422/",
      "theme-color": "#000000",
      "pageid": "nm4261422",
      "pagetype": "name",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY1200_CR164,0,630,1200_AL_.jpg",
      "og:type": "actor",
      "fb:app_id": "115109575169727",
      "og:title": "Jake Graf",
      "og:site_name": "IMDb",
      "title": "Jake Graf - IMDb",
      "og:description": "Jake Graf, Actor: Chance. Jake Graf is an actor and writer, known for Chance (2015), The Danish Girl (2015) and Dawn (2016).",
      "request_id": "0WRRT8XW1FQPT6PY791F"
     }
    ],
    "hcard": [
     {
      "fn": "Jake Graf",
      "title": "Actor",
      "url": "http://www.imdb.com/video/user/vi4067727897?ref_=nm_demo_2",
      "photo": "http://ia.media-imdb.com/images/M/MV5BMjExNzUzMTAxOV5BMl5BanBnXkFtZTgwNjUwMTkxMzE@._V1_UX148_CR0,0,148,200_AL_.jpg"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Chance (2015) - Plot Summary - IMDb",
   "htmlTitle": "\u003cb\u003eChance\u003c/b\u003e (2015) - Plot Summary - IMDb",
   "link": "http://www.imdb.com/title/tt4070722/plotsummary",
   "displayLink": "www.imdb.com",
   "snippet": "Chance (2015) on IMDb: Trevor's life has become a void, following the passing of \nhis wife and ... Chance (2015) - Plot Summary Poster ... Written by Jake Graf.",
   "htmlSnippet": "\u003cb\u003eChance\u003c/b\u003e (2015) on IMDb: Trevor&#39;s life has become a void, following the passing of \u003cbr\u003e\nhis wife and ... \u003cb\u003eChance\u003c/b\u003e (2015) - Plot Summary Poster ... Written by \u003cb\u003eJake Graf\u003c/b\u003e.",
   "cacheId": "cWsYeGcOV9oJ",
   "formattedUrl": "www.imdb.com/title/tt4070722/plotsummary",
   "htmlFormattedUrl": "www.imdb.com/title/tt4070722/plotsummary",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTcwOTgzMjk0OF5BMl5BanBnXkFtZTgwNDM0NzI2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRCCTgDFBnwEq37X92-AHLrlwYkXEWauX8QI37BUU_L98B9ZzRl2ln4T_M"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt4070722?src=mdot",
      "og:url": "http://www.imdb.com/title/tt4070722/plotsummary",
      "theme-color": "#000000",
      "pageid": "tt4070722",
      "pagetype": "title",
      "subpagetype": "plotsummary",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTcwOTgzMjk0OF5BMl5BanBnXkFtZTgwNDM0NzI2NDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Chance (2015)",
      "og:site_name": "IMDb",
      "title": "Chance (2015) - Plot Summary - IMDb",
      "og:description": "Chance (2015) on IMDb: Trevor's life has become a void, following the passing of his wife and long term companion, Doris. Days run into weeks, as Trevor slowly finds himself",
      "request_id": "14M4TRFQ18WYCJ0RYGT1"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Jake Graf - Biography - IMDb",
   "htmlTitle": "\u003cb\u003eJake Graf\u003c/b\u003e - Biography - IMDb",
   "link": "http://www.imdb.com/name/nm4261422/bio",
   "displayLink": "www.imdb.com",
   "snippet": "Jake Graf is an actor and writer, known for Chance (2015), The Danish Girl (2015\n) and Dawn (2016).",
   "htmlSnippet": "\u003cb\u003eJake Graf\u003c/b\u003e is an actor and writer, known for \u003cb\u003eChance\u003c/b\u003e (2015), The Danish Girl (2015\u003cbr\u003e\n) and Dawn (2016).",
   "cacheId": "cymSOg0kCmoJ",
   "formattedUrl": "www.imdb.com/name/nm4261422/bio",
   "htmlFormattedUrl": "www.imdb.com/name/nm4261422/bio",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY1200_CR164,0,630,1200_AL_.jpg"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzlnyzE8EJfydYmvosDfb5BPbgem1rbi1UyR3pJ8VSpMGEurOEjZxoxDg"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///name/nm4261422?src=mdot",
      "og:url": "http://www.imdb.com/name/nm4261422/bio",
      "theme-color": "#000000",
      "pageid": "nm4261422",
      "pagetype": "name",
      "subpagetype": "bio",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY1200_CR164,0,630,1200_AL_.jpg",
      "og:type": "actor",
      "fb:app_id": "115109575169727",
      "og:title": "Jake Graf",
      "og:site_name": "IMDb",
      "title": "Jake Graf - IMDb",
      "og:description": "Jake Graf is an actor and writer, known for Chance (2015), The Danish Girl (2015) and Dawn (2016).",
      "request_id": "1G1J0HHMETP4Y5NS8AP7"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Jake Graf on IMDb: Movies, TV, Celebs, and more... - Photo Gallery ...",
   "htmlTitle": "\u003cb\u003eJake Graf\u003c/b\u003e on IMDb: Movies, TV, Celebs, and more... - Photo Gallery \u003cb\u003e...\u003c/b\u003e",
   "link": "http://www.imdb.com/name/nm4261422/mediaindex",
   "displayLink": "www.imdb.com",
   "snippet": "Jake Graf photos, including production stills, premiere photos and other event ... \nJake Graf is an actor and writer, known for Chance (2015), The Danish Girl ...",
   "htmlSnippet": "\u003cb\u003eJake Graf\u003c/b\u003e photos, including production stills, premiere photos and other event ... \u003cbr\u003e\n\u003cb\u003eJake Graf\u003c/b\u003e is an actor and writer, known for \u003cb\u003eChance\u003c/b\u003e (2015), The Danish Girl&nbsp;...",
   "cacheId": "hjySWvPmjLUJ",
   "formattedUrl": "www.imdb.com/name/nm4261422/mediaindex",
   "htmlFormattedUrl": "www.imdb.com/name/nm4261422/mediaindex",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY1200_CR164,0,630,1200_AL_.jpg"
     }
    ],
    "person": [
     {
      "image": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY98_CR5,0,67,98_AL_.jpg",
      "name": "Jake Graf",
      "url": "Jake Graf",
      "thumbnailurl": "http://www.imdb.com/media/rm952496896/nm4261422?ref_=nmmi_mi_all_pbl_1",
      "description": "Jake Graf is an actor and writer, known for Chance (2015), The Danish Girl (2015) and Dawn (2016). See full bio »"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzlnyzE8EJfydYmvosDfb5BPbgem1rbi1UyR3pJ8VSpMGEurOEjZxoxDg"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///name/nm4261422?src=mdot",
      "og:url": "http://www.imdb.com/name/nm4261422/mediaindex",
      "theme-color": "#000000",
      "pageid": "nm4261422",
      "pagetype": "name",
      "subpagetype": "mediaindex",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UY1200_CR164,0,630,1200_AL_.jpg",
      "og:type": "actor",
      "fb:app_id": "115109575169727",
      "og:title": "Jake Graf on IMDb: Movies, TV, Celebs, and more...",
      "og:site_name": "IMDb",
      "title": "Jake Graf on IMDb: Movies, TV, Celebs, and more... - IMDb",
      "og:description": "Jake Graf photos, including production stills, premiere photos and other event photos, publicity photos, behind-the-scenes, and more.",
      "request_id": "1MSWKSVE0G8T4WSZ9J4Y"
     }
    ],
    "hcard": [
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422/?ref_=nmmi_mi_nm",
      "photo": "http://ia.media-imdb.com/images/M/MV5BMTg0NTA2MzQ5N15BMl5BanBnXkFtZTgwNzk2OTcxMzE@._V1_UX100_CR0,0,100,100_AL_.jpg"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "X-Why (2011) - IMDb",
   "htmlTitle": "X-Why (2011) - IMDb",
   "link": "http://www.imdb.com/title/tt2371252/",
   "displayLink": "www.imdb.com",
   "snippet": "XWHY is the first film from writer/director/actor Jake Graf. Shot over two ... People \nwho liked this also liked... Chance. Cocktale. Brace. The Danish Girl. Dawn.",
   "htmlSnippet": "XWHY is the first film from writer/director/actor \u003cb\u003eJake Graf\u003c/b\u003e. Shot over two ... People \u003cbr\u003e\nwho liked this also liked... \u003cb\u003eChance\u003c/b\u003e. Cocktale. Brace. The Danish Girl. Dawn.",
   "cacheId": "ix5rhsBsZx4J",
   "formattedUrl": "www.imdb.com/title/tt2371252/",
   "htmlFormattedUrl": "www.imdb.com/title/tt2371252/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMjExNzUzMTAxOV5BMl5BanBnXkFtZTgwNjUwMTkxMzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg"
     }
    ],
    "organization": [
     {
      "url": "Up And Up Productions",
      "name": "Up And Up Productions"
     },
     {
      "url": "Apropos International Productions",
      "name": "Apropos International Productions"
     }
    ],
    "person": [
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Pavlo Schtakleff",
      "name": "Pavlo Schtakleff"
     },
     {
      "url": "Roberto Boella",
      "name": "Roberto Boella"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Pavlo Schtakleff",
      "name": "Pavlo Schtakleff"
     },
     {
      "url": "Roberto Boella",
      "name": "Roberto Boella"
     },
     {
      "url": "Laurent Corneille",
      "name": "Laurent Corneille"
     },
     {
      "url": "Anna Bladzich",
      "name": "Anna Bladzich"
     },
     {
      "url": "Cheryl Wilson",
      "name": "Cheryl Wilson"
     },
     {
      "url": "Danny Parry",
      "name": "Danny Parry"
     },
     {
      "url": "David Hess",
      "name": "David Hess"
     },
     {
      "url": "Kali Madden",
      "name": "Kali Madden"
     },
     {
      "url": "Esther Trendall",
      "name": "Esther Trendall"
     },
     {
      "url": "Sophie Boella",
      "name": "Sophie Boella"
     },
     {
      "url": "Alice Nutt",
      "name": "Alice Nutt"
     },
     {
      "url": "Corvin Roman",
      "name": "Corvin Roman"
     },
     {
      "url": "Clare Wooton",
      "name": "Clare Wooton"
     },
     {
      "url": "Ammon",
      "name": "Ammon"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQ6wt8zF2sWyjNBvnvzWot6F9_RB6nzbWCBn85vhgiEuTrH1ldFfeo45D8"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt2371252?src=mdot",
      "og:url": "http://www.imdb.com/title/tt2371252/",
      "theme-color": "#000000",
      "pageid": "tt2371252",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMjExNzUzMTAxOV5BMl5BanBnXkFtZTgwNjUwMTkxMzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "X-Why (2011)",
      "og:site_name": "IMDb",
      "title": "X-Why (2011) - IMDb",
      "og:description": "Directed by Jake Graf.  With Jake Graf, Pavlo Schtakleff, Roberto Boella, Laurent Corneille. XWHY is the first film from writer/director/actor Jake Graf. Shot over two years, this film accurately reflects some of the natural changes, both physical and emotional, that a young transman undergoes during transition. XWHY is a groundbreaking look at some of the trials and tribulations that trans people face both pre, and post transition, told in a light hearted, often humorous manner.",
      "request_id": "0C80E1DQSQBZMPTAQEGA"
     }
    ],
    "hcard": [
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_dr"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_wr"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Pavlo Schtakleff",
      "url": "http://www.imdb.com/name/nm5870304?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Roberto Boella",
      "url": "http://www.imdb.com/name/nm5870305?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422/?ref_=tt_cl_t1"
     },
     {
      "fn": "Pavlo Schtakleff",
      "url": "http://www.imdb.com/name/nm5870304/?ref_=tt_cl_t2"
     },
     {
      "fn": "Roberto Boella",
      "url": "http://www.imdb.com/name/nm5870305/?ref_=tt_cl_t3"
     },
     {
      "fn": "Laurent Corneille",
      "url": "http://www.imdb.com/name/nm5870306/?ref_=tt_cl_t4"
     },
     {
      "fn": "Anna Bladzich",
      "url": "http://www.imdb.com/name/nm5870307/?ref_=tt_cl_t5"
     },
     {
      "fn": "Cheryl Wilson",
      "url": "http://www.imdb.com/name/nm5870260/?ref_=tt_cl_t6"
     },
     {
      "fn": "Danny Parry",
      "url": "http://www.imdb.com/name/nm5870263/?ref_=tt_cl_t7"
     },
     {
      "fn": "David Hess",
      "url": "http://www.imdb.com/name/nm5870310/?ref_=tt_cl_t8"
     },
     {
      "fn": "Kali Madden",
      "url": "http://www.imdb.com/name/nm4903805/?ref_=tt_cl_t9"
     },
     {
      "fn": "Esther Trendall",
      "url": "http://www.imdb.com/name/nm5870311/?ref_=tt_cl_t10"
     },
     {
      "fn": "Sophie Boella",
      "url": "http://www.imdb.com/name/nm5870312/?ref_=tt_cl_t11"
     },
     {
      "fn": "Alice Nutt",
      "url": "http://www.imdb.com/name/nm5870313/?ref_=tt_cl_t12"
     },
     {
      "fn": "Corvin Roman",
      "url": "http://www.imdb.com/name/nm5870314/?ref_=tt_cl_t13"
     },
     {
      "fn": "Clare Wooton",
      "url": "http://www.imdb.com/name/nm5870315/?ref_=tt_cl_t14"
     },
     {
      "fn": "Ammon",
      "nickname": "Ammon",
      "url": "http://www.imdb.com/name/nm5870316/?ref_=tt_cl_t15"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Cocktale (2012) - IMDb",
   "htmlTitle": "Cocktale (2012) - IMDb",
   "link": "http://www.imdb.com/title/tt2640854/",
   "displayLink": "www.imdb.com",
   "snippet": "Brian (Jake Graf) is struggling to reconcile his feelings for his flatmate and the \ndesire ... People who liked this also liked... Chance. X-Why. Brace. The Danish \nGirl.",
   "htmlSnippet": "Brian (\u003cb\u003eJake Graf\u003c/b\u003e) is struggling to reconcile his feelings for his flatmate and the \u003cbr\u003e\ndesire ... People who liked this also liked... \u003cb\u003eChance\u003c/b\u003e. X-Why. Brace. The Danish \u003cbr\u003e\nGirl.",
   "cacheId": "4Hkv3-BLIMcJ",
   "formattedUrl": "www.imdb.com/title/tt2640854/",
   "htmlFormattedUrl": "www.imdb.com/title/tt2640854/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTc1ODE1OTU5N15BMl5BanBnXkFtZTgwODU4OTAwMDE@._V1_UY1200_CR117,0,630,1200_AL_.jpg"
     }
    ],
    "organization": [
     {
      "url": "Up And Up Productions",
      "name": "Up And Up Productions"
     }
    ],
    "person": [
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Katy Tucker",
      "name": "Katy Tucker"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Katy Tucker",
      "name": "Katy Tucker"
     },
     {
      "url": "Paul DuBois",
      "name": "Paul DuBois"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Katy Tucker",
      "name": "Katy Tucker"
     },
     {
      "url": "Paul DuBois",
      "name": "Paul DuBois"
     },
     {
      "url": "Ferenc Szabadi",
      "name": "Ferenc Szabadi"
     },
     {
      "url": "Katharine Blackshaw",
      "name": "Katharine Blackshaw"
     },
     {
      "url": "Waj Ali",
      "name": "Waj Ali"
     },
     {
      "url": "Miranda Magee",
      "name": "Miranda Magee"
     },
     {
      "url": "Clifford Hume",
      "name": "Clifford Hume"
     },
     {
      "url": "Samuel Humphreys",
      "name": "Samuel Humphreys"
     },
     {
      "url": "Jonathan Ow",
      "name": "Jonathan Ow"
     },
     {
      "url": "Aka Awesomelicious",
      "name": "Aka Awesomelicious"
     },
     {
      "url": "Alexandra D'Sa",
      "name": "Alexandra D'Sa"
     },
     {
      "url": "Laura Gomes",
      "name": "Laura Gomes"
     },
     {
      "url": "Rachel Holifield",
      "name": "Rachel Holifield"
     },
     {
      "url": "Briony Shay de Klerk",
      "name": "Briony Shay de Klerk"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS-9lsHUk0hF8LoN0yf6WqdmQc5wS6ZmtjNf9-D-ER32q38ADb4GPRZIVs"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt2640854?src=mdot",
      "og:url": "http://www.imdb.com/title/tt2640854/",
      "theme-color": "#000000",
      "pageid": "tt2640854",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTc1ODE1OTU5N15BMl5BanBnXkFtZTgwODU4OTAwMDE@._V1_UY1200_CR117,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Cocktale (2012)",
      "og:site_name": "IMDb",
      "title": "Cocktale (2012) - IMDb",
      "og:description": "Directed by Jake Graf.  With Jake Graf, Katy Tucker, Paul DuBois, Ferenc Szabadi. Sex and alcohol are a heady blend in COCKTALE, a refreshing new British comedy by Jake Graf (Iris Prize Nominee 2012). Brian (Jake Graf) is struggling to reconcile his feelings for his flatmate and the desire for the conventional life. As Brian embarks on a one night stand with Kelly (Katy Tucker) he is unprepared for the disastrous and embarrassing consequences. Set in the glamorous world of ...",
      "request_id": "1CDPEKSHA7RXX379GFVN"
     }
    ],
    "hcard": [
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_dr"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_wr"
     },
     {
      "fn": "Katy Tucker",
      "url": "http://www.imdb.com/name/nm5251352?ref_=tt_ov_wr"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Katy Tucker",
      "url": "http://www.imdb.com/name/nm5251352?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Paul DuBois",
      "url": "http://www.imdb.com/name/nm5279413?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422/?ref_=tt_cl_t1"
     },
     {
      "fn": "Katy Tucker",
      "url": "http://www.imdb.com/name/nm5251352/?ref_=tt_cl_t2"
     },
     {
      "fn": "Paul DuBois",
      "url": "http://www.imdb.com/name/nm5279413/?ref_=tt_cl_t3"
     },
     {
      "fn": "Ferenc Szabadi",
      "url": "http://www.imdb.com/name/nm5473870/?ref_=tt_cl_t4"
     },
     {
      "fn": "Katharine Blackshaw",
      "url": "http://www.imdb.com/name/nm4360198/?ref_=tt_cl_t5"
     },
     {
      "fn": "Waj Ali",
      "url": "http://www.imdb.com/name/nm5400084/?ref_=tt_cl_t6"
     },
     {
      "fn": "Miranda Magee",
      "url": "http://www.imdb.com/name/nm3678847/?ref_=tt_cl_t7"
     },
     {
      "fn": "Clifford Hume",
      "url": "http://www.imdb.com/name/nm5405166/?ref_=tt_cl_t8"
     },
     {
      "fn": "Samuel Humphreys",
      "url": "http://www.imdb.com/name/nm5299363/?ref_=tt_cl_t9"
     },
     {
      "fn": "Jonathan Ow",
      "url": "http://www.imdb.com/name/nm4358560/?ref_=tt_cl_t10"
     },
     {
      "fn": "Aka Awesomelicious",
      "url": "http://www.imdb.com/name/nm5875514/?ref_=tt_cl_t11"
     },
     {
      "fn": "Alexandra D'Sa",
      "url": "http://www.imdb.com/name/nm5171829/?ref_=tt_cl_t12"
     },
     {
      "fn": "Laura Gomes",
      "url": "http://www.imdb.com/name/nm5875511/?ref_=tt_cl_t13"
     },
     {
      "fn": "Rachel Holifield",
      "url": "http://www.imdb.com/name/nm5875510/?ref_=tt_cl_t14"
     },
     {
      "fn": "Briony Shay de Klerk",
      "url": "http://www.imdb.com/name/nm5875513/?ref_=tt_cl_t15"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Dawn (2016) - IMDb",
   "htmlTitle": "Dawn (2016) - IMDb",
   "link": "http://www.imdb.com/title/tt5354406/",
   "displayLink": "www.imdb.com",
   "snippet": "Directed by Jake Graf. With Harry ... Sometimes, life gives you another Chance. \nDirector: ... XWHY is the first film from writer/director/actor Jake Graf. Shot over ...",
   "htmlSnippet": "Directed by \u003cb\u003eJake Graf\u003c/b\u003e. With Harry ... Sometimes, life gives you another \u003cb\u003eChance\u003c/b\u003e. \u003cbr\u003e\nDirector: ... XWHY is the first film from writer/director/actor \u003cb\u003eJake Graf\u003c/b\u003e. Shot over&nbsp;...",
   "cacheId": "XNfqkKDqvE8J",
   "formattedUrl": "www.imdb.com/title/tt5354406/",
   "htmlFormattedUrl": "www.imdb.com/title/tt5354406/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/G/01imdb/images/logos/imdb_fb_logo-1730868325._CB306318125_.png"
     }
    ],
    "person": [
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Jake Graf",
      "name": "Jake Graf"
     },
     {
      "url": "Harry Rundle",
      "name": "Harry Rundle"
     },
     {
      "url": "Nicole Gibson",
      "name": "Nicole Gibson"
     },
     {
      "url": "Harry Rundle",
      "name": "Harry Rundle"
     },
     {
      "url": "Nicole Gibson",
      "name": "Nicole Gibson"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt5354406?src=mdot",
      "og:url": "http://www.imdb.com/title/tt5354406/",
      "theme-color": "#000000",
      "pageid": "tt5354406",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/G/01imdb/images/logos/imdb_fb_logo-1730868325._CB306318125_.png",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Dawn (2016)",
      "og:site_name": "IMDb",
      "title": "Dawn (2016) - IMDb",
      "og:description": "Directed by Jake Graf.  With Harry Rundle, Nicole Gibson. It's always darkest before Dawn.",
      "request_id": "0SPMC87SHKPNT0Q4N6A5"
     }
    ],
    "hcard": [
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_dr"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_wr"
     },
     {
      "fn": "Jake Graf",
      "url": "http://www.imdb.com/name/nm4261422?ref_=tt_ov_wr"
     },
     {
      "fn": "Harry Rundle",
      "url": "http://www.imdb.com/name/nm5269791?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Nicole Gibson",
      "url": "http://www.imdb.com/name/nm7862335?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Harry Rundle",
      "url": "http://www.imdb.com/name/nm5269791/?ref_=tt_cl_t1"
     },
     {
      "fn": "Nicole Gibson",
      "url": "http://www.imdb.com/name/nm7862335/?ref_=tt_cl_t2"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Project Arbiter (2013) - Full Cast & Crew - IMDb",
   "htmlTitle": "Project Arbiter (2013) - Full Cast &amp; Crew - IMDb",
   "link": "http://www.imdb.com/title/tt3102156/fullcredits/",
   "displayLink": "www.imdb.com",
   "snippet": "Michael Chance. Writing Credits (in alphabetical order). Michael Chance. Cast (\nin credits order). Alexis Cassar ... Joe Colburn. Jake Lyall . ... Florian Graf .",
   "htmlSnippet": "Michael \u003cb\u003eChance\u003c/b\u003e. Writing Credits (in alphabetical order). Michael \u003cb\u003eChance\u003c/b\u003e. Cast (\u003cbr\u003e\nin credits order). Alexis Cassar ... Joe Colburn. \u003cb\u003eJake\u003c/b\u003e Lyall . ... Florian \u003cb\u003eGraf\u003c/b\u003e .",
   "cacheId": "cm0cHPfDrO8J",
   "formattedUrl": "www.imdb.com/title/tt3102156/fullcredits/",
   "htmlFormattedUrl": "www.imdb.com/title/tt3102156/fullcredits/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BODkxODU5MTU1OF5BMl5BanBnXkFtZTgwNzIzNjcwMDE@._V1_UY1200_CR73,0,630,1200_AL_.jpg"
     }
    ],
    "person": [
     {
      "url": "Alexis Cassar",
      "name": "Alexis Cassar"
     },
     {
      "url": "Jake Lyall",
      "name": "Jake Lyall"
     },
     {
      "url": "Tim Coyne",
      "name": "Tim Coyne"
     },
     {
      "url": "William Charlton",
      "name": "William Charlton"
     },
     {
      "url": "Andrew Dillon",
      "name": "Andrew Dillon"
     },
     {
      "url": "Artem Mishin",
      "name": "Artem Mishin"
     },
     {
      "url": "Zachary Gossett",
      "name": "Zachary Gossett"
     },
     {
      "url": "Terra Flowers",
      "name": "Terra Flowers"
     },
     {
      "url": "Zak Waters",
      "name": "Zak Waters"
     },
     {
      "url": "Hans Beerbaum",
      "name": "Hans Beerbaum"
     },
     {
      "url": "David Aires",
      "name": "David Aires"
     },
     {
      "url": "Jesse Boots",
      "name": "Jesse Boots"
     },
     {
      "url": "Jason C.H. Burton",
      "name": "Jason C.H. Burton"
     },
     {
      "url": "Florian Graf",
      "name": "Florian Graf"
     },
     {
      "url": "Chuck Phelps",
      "name": "Chuck Phelps"
     },
     {
      "url": "Jacob Rangel",
      "name": "Jacob Rangel"
     },
     {
      "url": "Robert O. Simons",
      "name": "Robert O. Simons"
     },
     {
      "url": "Jesee Walker",
      "name": "Jesee Walker"
     },
     {
      "url": "Peter Berner",
      "name": "Peter Berner"
     },
     {
      "url": "Michael Chabot",
      "name": "Michael Chabot"
     },
     {
      "url": "Jesse Chapman",
      "name": "Jesse Chapman"
     },
     {
      "url": "Ivan David",
      "name": "Ivan David"
     },
     {
      "url": "Luc Goggins",
      "name": "Luc Goggins"
     },
     {
      "url": "Matthias Graf",
      "name": "Matthias Graf"
     },
     {
      "url": "Aron Kiraly",
      "name": "Aron Kiraly"
     },
     {
      "url": "Cody Moore",
      "name": "Cody Moore"
     },
     {
      "url": "Thomas Nakanishi",
      "name": "Thomas Nakanishi"
     },
     {
      "url": "Mark Van Klaveren",
      "name": "Mark Van Klaveren"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR19zu5WZTF0cYXrxOj4e_bAncSRUEFUXn1yPPU0z1tO7_df-8xvBqtrGym"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt3102156?src=mdot",
      "og:url": "http://www.imdb.com/title/tt3102156/fullcredits/",
      "theme-color": "#000000",
      "pageid": "tt3102156",
      "pagetype": "title",
      "subpagetype": "fullcredits",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BODkxODU5MTU1OF5BMl5BanBnXkFtZTgwNzIzNjcwMDE@._V1_UY1200_CR73,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Project Arbiter (2013)",
      "og:site_name": "IMDb",
      "title": "Project Arbiter (2013) - IMDb",
      "og:description": "Project Arbiter (2013) cast and crew credits, including actors, actresses, directors, writers and more.",
      "request_id": "0ZBA5EBC89ABBY72QMAE"
     }
    ],
    "hcard": [
     {
      "fn": "Alexis Cassar",
      "url": "http://www.imdb.com/name/nm0143977/?ref_=ttfc_fc_cl_t1"
     },
     {
      "fn": "Jake Lyall",
      "url": "http://www.imdb.com/name/nm3168360/?ref_=ttfc_fc_cl_t2"
     },
     {
      "fn": "Tim Coyne",
      "url": "http://www.imdb.com/name/nm1058140/?ref_=ttfc_fc_cl_t3"
     },
     {
      "fn": "William Charlton",
      "url": "http://www.imdb.com/name/nm0153316/?ref_=ttfc_fc_cl_t4"
     },
     {
      "fn": "Andrew Dillon",
      "url": "http://www.imdb.com/name/nm2595668/?ref_=ttfc_fc_cl_t5"
     },
     {
      "fn": "Artem Mishin",
      "url": "http://www.imdb.com/name/nm3175916/?ref_=ttfc_fc_cl_t6"
     },
     {
      "fn": "Zachary Gossett",
      "url": "http://www.imdb.com/name/nm2714760/?ref_=ttfc_fc_cl_t7"
     },
     {
      "fn": "Terra Flowers",
      "url": "http://www.imdb.com/name/nm3441219/?ref_=ttfc_fc_cl_t8"
     },
     {
      "fn": "Zak Waters",
      "url": "http://www.imdb.com/name/nm5027767/?ref_=ttfc_fc_cl_t9"
     },
     {
      "fn": "Hans Beerbaum",
      "url": "http://www.imdb.com/name/nm2506047/?ref_=ttfc_fc_cl_t10"
     },
     {
      "fn": "David Aires",
      "url": "http://www.imdb.com/name/nm2869577/?ref_=ttfc_fc_cl_t11"
     },
     {
      "fn": "Jesse Boots",
      "url": "http://www.imdb.com/name/nm2373354/?ref_=ttfc_fc_cl_t12"
     },
     {
      "fn": "Jason C.H. Burton",
      "url": "http://www.imdb.com/name/nm4968950/?ref_=ttfc_fc_cl_t13"
     },
     {
      "fn": "Florian Graf",
      "url": "http://www.imdb.com/name/nm3525880/?ref_=ttfc_fc_cl_t14"
     },
     {
      "fn": "Chuck Phelps",
      "url": "http://www.imdb.com/name/nm3286428/?ref_=ttfc_fc_cl_t15"
     },
     {
      "fn": "Jacob Rangel",
      "url": "http://www.imdb.com/name/nm2491004/?ref_=ttfc_fc_cl_t16"
     },
     {
      "fn": "Robert O. Simons",
      "url": "http://www.imdb.com/name/nm4734823/?ref_=ttfc_fc_cl_t17"
     },
     {
      "fn": "Jesee Walker",
      "url": "http://www.imdb.com/name/nm4543071/?ref_=ttfc_fc_cl_t18"
     },
     {
      "fn": "Peter Berner",
      "url": "http://www.imdb.com/name/nm6254334/?ref_=ttfc_fc_cl_t19"
     },
     {
      "fn": "Michael Chabot",
      "url": "http://www.imdb.com/name/nm6254327/?ref_=ttfc_fc_cl_t20"
     },
     {
      "fn": "Jesse Chapman",
      "url": "http://www.imdb.com/name/nm6254328/?ref_=ttfc_fc_cl_t21"
     },
     {
      "fn": "Ivan David",
      "url": "http://www.imdb.com/name/nm6254329/?ref_=ttfc_fc_cl_t22"
     },
     {
      "fn": "Luc Goggins",
      "url": "http://www.imdb.com/name/nm6254330/?ref_=ttfc_fc_cl_t23"
     },
     {
      "fn": "Matthias Graf",
      "url": "http://www.imdb.com/name/nm6254335/?ref_=ttfc_fc_cl_t24"
     },
     {
      "fn": "Aron Kiraly",
      "url": "http://www.imdb.com/name/nm6254336/?ref_=ttfc_fc_cl_t25"
     },
     {
      "fn": "Cody Moore",
      "url": "http://www.imdb.com/name/nm6254332/?ref_=ttfc_fc_cl_t26"
     },
     {
      "fn": "Thomas Nakanishi",
      "url": "http://www.imdb.com/name/nm6254333/?ref_=ttfc_fc_cl_t27"
     },
     {
      "fn": "Mark Van Klaveren",
      "url": "http://www.imdb.com/name/nm6254331/?ref_=ttfc_fc_cl_t28"
     }
    ]
   }
  }
 ]
}

flag = 0
check = 0
key ={}
with open ('output2.csv', 'wb') as csvoutput: 
		fieldnames = ['Entity','url','Director','Year','Alias','IMDB URL','genre','Runtime']
		writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
		writer.writeheader()
		imdb_key =''
		response = res.get('items')
		if response:
			for i in range(0,len(response)):
				print "===================================="
				json_title = res['items'][i].get('title')
				json_title = re.sub(r'<.*?>','',json_title)
				print 'fetched title:',json_title

				json_director = res['items'][i]['snippet']
				json_director = re.sub(r'...','',json_director)
				json_director = re.search(r'Jake Graf',json_director)
			 
				if re.sub(r'\s+\(.*','',json_title).strip() == 'Chance':
					print "##"
					if json_director is None:
						print "###"
						try:
							print 'inside try'
							json_director = res['items'][i]['pagemap']['metatags'][0].get('og:description')
							json_director = re.search(r'Jake Graf',json_director)
							if json_director:
								print '####' 
								if json_director.group(0) == 'Jake Graf':
									print '#####'
									imdb_key = res['items'][i]['link']

									print imdb_key
									writer.writerow({'Entity':'Chance','Director':'Jake Graf','IMDB URL': imdb_key})
									check = 1
									break
								else:
									print "######"
								
						except:
							print "director not found"
							
				else:
					print 'no key found'
					flag = 1
			if flag == 1 and check == 0:
				print "NO == NO == No"
				print flag	
				writer.writerow({'Entity':'Chance','Director':'Jake Graf','IMDB URL': imdb_key})

		elif response is None:
			print 'No Response'
			writer.writerow({'Entity':'Chance','Director':'Jake Graf','IMDB URL': imdb_key})