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
  "request": [
   {
    "title": "Google Custom Search - Pipe Dream Yudho Aditya",
    "totalResults": "8",
    "searchTerms": "Pipe Dream Yudho Aditya",
    "count": 8,
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
  "searchTime": 0.215283,
  "formattedSearchTime": "0.22",
  "totalResults": "8",
  "formattedTotalResults": "8"
 },
 "items": [
  {
   "kind": "customsearch#result",
   "title": "Pipe Dream (2015) - IMDb",
   "htmlTitle": "\u003cb\u003ePipe Dream\u003c/b\u003e (2015) - IMDb",
   "link": "http://www.imdb.com/title/tt3756812/",
   "displayLink": "www.imdb.com",
   "snippet": "Directed by Yudho Aditya. With Eric Tabach, Elise Metcalf, Zachary Steinback, \nVic Chao. Peter Epstein-Takahashi is popular with a certain female classmate, \nbut ...",
   "htmlSnippet": "Directed by \u003cb\u003eYudho Aditya\u003c/b\u003e. With Eric Tabach, Elise Metcalf, Zachary Steinback, \u003cbr\u003e\nVic Chao. Peter Epstein-Takahashi is popular with a certain female classmate, \u003cbr\u003e\nbut&nbsp;...",
   "cacheId": "kUs5E9x4tV0J",
   "formattedUrl": "www.imdb.com/title/tt3756812/",
   "htmlFormattedUrl": "www.imdb.com/title/tt3756812/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTQ3MzIyMTI1MF5BMl5BanBnXkFtZTgwMDIzMjQwNTE@._V1_UY1200_CR93,0,630,1200_AL_.jpg"
     }
    ],
    "organization": [
     {
      "url": "DTF Pictures",
      "name": "DTF Pictures"
     }
    ],
    "person": [
     {
      "url": "Yudho Aditya",
      "name": "Yudho Aditya"
     },
     {
      "url": "Max Rifkind-Barron",
      "name": "Max Rifkind-Barron"
     },
     {
      "url": "Eric Tabach",
      "name": "Eric Tabach"
     },
     {
      "url": "Elise Metcalf",
      "name": "Elise Metcalf"
     },
     {
      "url": "Zachary Steinback",
      "name": "Zachary Steinback"
     },
     {
      "url": "Eric Tabach",
      "name": "Eric Tabach"
     },
     {
      "url": "Elise Metcalf",
      "name": "Elise Metcalf"
     },
     {
      "url": "Zachary Steinback",
      "name": "Zachary Steinback"
     },
     {
      "url": "Vic Chao",
      "name": "Vic Chao"
     },
     {
      "url": "Zachary Roozen",
      "name": "Zachary Roozen"
     },
     {
      "url": "Dalena Nguyen",
      "name": "Dalena Nguyen"
     },
     {
      "url": "Matthew Marzo",
      "name": "Matthew Marzo"
     },
     {
      "url": "Yudha Adiputera",
      "name": "Yudha Adiputera"
     },
     {
      "url": "Adam Furukawa",
      "name": "Adam Furukawa"
     },
     {
      "url": "Theodore Lin",
      "name": "Theodore Lin"
     },
     {
      "url": "Arnold Ng",
      "name": "Arnold Ng"
     },
     {
      "url": "Aigul Seitmetova",
      "name": "Aigul Seitmetova"
     },
     {
      "url": "Royce Wang",
      "name": "Royce Wang"
     },
     {
      "url": "Christopher Yao",
      "name": "Christopher Yao"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT5hUqIvmiXZKa3mxSbhYOx9z9y5d5WG5SBG5dx9NdJg5jyOp6vd-IS0cI"
     }
    ],
    "aggregaterating": [
     {
      "ratingvalue": "8.0",
      "bestrating": "10",
      "ratingcount": "11"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt3756812?src=mdot",
      "og:url": "http://www.imdb.com/title/tt3756812/",
      "theme-color": "#000000",
      "pageid": "tt3756812",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTQ3MzIyMTI1MF5BMl5BanBnXkFtZTgwMDIzMjQwNTE@._V1_UY1200_CR93,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Pipe Dream (2015)",
      "og:site_name": "IMDb",
      "title": "Pipe Dream (2015) - IMDb",
      "og:description": "Directed by Yudho Aditya.  With Eric Tabach, Elise Metcalf, Zachary Steinback, Vic Chao. Peter Epstein-Takahashi is popular with a certain female classmate, but he's concerned about his, er, endowment. Who else to turn to for advice but his two gay dads? They may not be quite prepared to handle the situation... Peter presents.",
      "request_id": "0QQX704Z1VRR32ET9W3G"
     }
    ],
    "hcard": [
     {
      "fn": "Yudho Aditya",
      "url": "http://www.imdb.com/name/nm4723897?ref_=tt_ov_dr"
     },
     {
      "fn": "Max Rifkind-Barron",
      "url": "http://www.imdb.com/name/nm3708135?ref_=tt_ov_wr"
     },
     {
      "fn": "Eric Tabach",
      "url": "http://www.imdb.com/name/nm5897418?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Elise Metcalf",
      "url": "http://www.imdb.com/name/nm6564551?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Zachary Steinback",
      "url": "http://www.imdb.com/name/nm1848968?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Eric Tabach",
      "url": "http://www.imdb.com/name/nm5897418/?ref_=tt_cl_t1"
     },
     {
      "fn": "Elise Metcalf",
      "url": "http://www.imdb.com/name/nm6564551/?ref_=tt_cl_t2"
     },
     {
      "fn": "Zachary Steinback",
      "url": "http://www.imdb.com/name/nm1848968/?ref_=tt_cl_t3"
     },
     {
      "fn": "Vic Chao",
      "url": "http://www.imdb.com/name/nm0152059/?ref_=tt_cl_t4"
     },
     {
      "fn": "Zachary Roozen",
      "url": "http://www.imdb.com/name/nm4635907/?ref_=tt_cl_t5"
     },
     {
      "fn": "Dalena Nguyen",
      "url": "http://www.imdb.com/name/nm5690061/?ref_=tt_cl_t6"
     },
     {
      "fn": "Matthew Marzo",
      "url": "http://www.imdb.com/name/nm6409343/?ref_=tt_cl_t7"
     },
     {
      "fn": "Yudha Adiputera",
      "url": "http://www.imdb.com/name/nm5382508/?ref_=tt_cl_t8"
     },
     {
      "fn": "Adam Furukawa",
      "url": "http://www.imdb.com/name/nm6597829/?ref_=tt_cl_t9"
     },
     {
      "fn": "Theodore Lin",
      "url": "http://www.imdb.com/name/nm6597830/?ref_=tt_cl_t10"
     },
     {
      "fn": "Arnold Ng",
      "url": "http://www.imdb.com/name/nm6597831/?ref_=tt_cl_t11"
     },
     {
      "fn": "Aigul Seitmetova",
      "url": "http://www.imdb.com/name/nm6597828/?ref_=tt_cl_t12"
     },
     {
      "fn": "Royce Wang",
      "url": "http://www.imdb.com/name/nm6597832/?ref_=tt_cl_t13"
     },
     {
      "fn": "Christopher Yao",
      "url": "http://www.imdb.com/name/nm6597833/?ref_=tt_cl_t14"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Pipe Dream (2015) - Full Cast & Crew - IMDb",
   "htmlTitle": "\u003cb\u003ePipe Dream\u003c/b\u003e (2015) - Full Cast &amp; Crew - IMDb",
   "link": "http://www.imdb.com/title/tt3756812/fullcredits/",
   "displayLink": "www.imdb.com",
   "snippet": "Pipe Dream (2015) cast and crew credits, including actors, actresses, directors, \nwriters and ... Pipe Dream (I) (2015). Full Cast & Crew. Directed by. Yudho Aditya\n ...",
   "htmlSnippet": "\u003cb\u003ePipe Dream\u003c/b\u003e (2015) cast and crew credits, including actors, actresses, directors, \u003cbr\u003e\nwriters and ... \u003cb\u003ePipe Dream\u003c/b\u003e (I) (2015). Full Cast &amp; Crew. Directed by. \u003cb\u003eYudho Aditya\u003c/b\u003e\u003cbr\u003e\n&nbsp;...",
   "cacheId": "vzsnlyu5WbcJ",
   "formattedUrl": "www.imdb.com/title/tt3756812/fullcredits/",
   "htmlFormattedUrl": "www.imdb.com/title/tt3756812/fullcredits/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTQ3MzIyMTI1MF5BMl5BanBnXkFtZTgwMDIzMjQwNTE@._V1_UY1200_CR93,0,630,1200_AL_.jpg"
     }
    ],
    "person": [
     {
      "url": "Eric Tabach",
      "name": "Eric Tabach"
     },
     {
      "url": "Elise Metcalf",
      "name": "Elise Metcalf"
     },
     {
      "url": "Zachary Steinback",
      "name": "Zachary Steinback"
     },
     {
      "url": "Vic Chao",
      "name": "Vic Chao"
     },
     {
      "url": "Zachary Roozen",
      "name": "Zachary Roozen"
     },
     {
      "url": "Dalena Nguyen",
      "name": "Dalena Nguyen"
     },
     {
      "url": "Matthew Marzo",
      "name": "Matthew Marzo"
     },
     {
      "url": "Yudha Adiputera",
      "name": "Yudha Adiputera"
     },
     {
      "url": "Adam Furukawa",
      "name": "Adam Furukawa"
     },
     {
      "url": "Theodore Lin",
      "name": "Theodore Lin"
     },
     {
      "url": "Arnold Ng",
      "name": "Arnold Ng"
     },
     {
      "url": "Aigul Seitmetova",
      "name": "Aigul Seitmetova"
     },
     {
      "url": "Royce Wang",
      "name": "Royce Wang"
     },
     {
      "url": "Christopher Yao",
      "name": "Christopher Yao"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT5hUqIvmiXZKa3mxSbhYOx9z9y5d5WG5SBG5dx9NdJg5jyOp6vd-IS0cI"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt3756812?src=mdot",
      "og:url": "http://www.imdb.com/title/tt3756812/fullcredits/",
      "theme-color": "#000000",
      "pageid": "tt3756812",
      "pagetype": "title",
      "subpagetype": "fullcredits",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTQ3MzIyMTI1MF5BMl5BanBnXkFtZTgwMDIzMjQwNTE@._V1_UY1200_CR93,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Pipe Dream (2015)",
      "og:site_name": "IMDb",
      "title": "Pipe Dream (2015) - IMDb",
      "og:description": "Pipe Dream (2015) cast and crew credits, including actors, actresses, directors, writers and more.",
      "request_id": "0HGZG0TNKS9E14GE9WMK"
     }
    ],
    "hcard": [
     {
      "fn": "Eric Tabach",
      "url": "http://www.imdb.com/name/nm5897418/?ref_=ttfc_fc_cl_t1"
     },
     {
      "fn": "Elise Metcalf",
      "url": "http://www.imdb.com/name/nm6564551/?ref_=ttfc_fc_cl_t2"
     },
     {
      "fn": "Zachary Steinback",
      "url": "http://www.imdb.com/name/nm1848968/?ref_=ttfc_fc_cl_t3"
     },
     {
      "fn": "Vic Chao",
      "url": "http://www.imdb.com/name/nm0152059/?ref_=ttfc_fc_cl_t4"
     },
     {
      "fn": "Zachary Roozen",
      "url": "http://www.imdb.com/name/nm4635907/?ref_=ttfc_fc_cl_t5"
     },
     {
      "fn": "Dalena Nguyen",
      "url": "http://www.imdb.com/name/nm5690061/?ref_=ttfc_fc_cl_t6"
     },
     {
      "fn": "Matthew Marzo",
      "url": "http://www.imdb.com/name/nm6409343/?ref_=ttfc_fc_cl_t7"
     },
     {
      "fn": "Yudha Adiputera",
      "url": "http://www.imdb.com/name/nm5382508/?ref_=ttfc_fc_cl_t8"
     },
     {
      "fn": "Adam Furukawa",
      "url": "http://www.imdb.com/name/nm6597829/?ref_=ttfc_fc_cl_t9"
     },
     {
      "fn": "Theodore Lin",
      "url": "http://www.imdb.com/name/nm6597830/?ref_=ttfc_fc_cl_t10"
     },
     {
      "fn": "Arnold Ng",
      "url": "http://www.imdb.com/name/nm6597831/?ref_=ttfc_fc_cl_t11"
     },
     {
      "fn": "Aigul Seitmetova",
      "url": "http://www.imdb.com/name/nm6597828/?ref_=ttfc_fc_cl_t12"
     },
     {
      "fn": "Royce Wang",
      "url": "http://www.imdb.com/name/nm6597832/?ref_=ttfc_fc_cl_t13"
     },
     {
      "fn": "Christopher Yao",
      "url": "http://www.imdb.com/name/nm6597833/?ref_=ttfc_fc_cl_t14"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Yudho Aditya - IMDb",
   "htmlTitle": "\u003cb\u003eYudho Aditya\u003c/b\u003e - IMDb",
   "link": "http://www.imdb.com/name/nm4723897/",
   "displayLink": "www.imdb.com",
   "snippet": "Yudho Aditya, Writer: Midnights with Adam. Yudho Aditya was born on \nSeptember 29, 1990 in Jakarta, Indonesia as Yudho Vanderhof Aditya. He is a \nwriter and ...",
   "htmlSnippet": "\u003cb\u003eYudho Aditya\u003c/b\u003e, Writer: Midnights with Adam. \u003cb\u003eYudho Aditya\u003c/b\u003e was born on \u003cbr\u003e\nSeptember 29, 1990 in Jakarta, Indonesia as Yudho Vanderhof Aditya. He is a \u003cbr\u003e\nwriter and&nbsp;...",
   "cacheId": "8_uAM_qW-8gJ",
   "formattedUrl": "www.imdb.com/name/nm4723897/",
   "htmlFormattedUrl": "www.imdb.com/name/nm4723897/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMjE3NTQ3NzU0NV5BMl5BanBnXkFtZTgwOTEwMjg4MTE@._V1_UY1200_CR115,0,630,1200_AL_.jpg"
     }
    ],
    "person": [
     {
      "role": "Writer"
     },
     {
      "image": "http://ia.media-imdb.com/images/M/MV5BMjE3NTQ3NzU0NV5BMl5BanBnXkFtZTgwOTEwMjg4MTE@._V1_UY317_CR6,0,214,317_AL_.jpg",
      "name": "Yudho Aditya",
      "jobtitle": "Writer",
      "description": "Yudho Aditya was born on September 29, 1990 in Jakarta, Indonesia as Yudho Vanderhof Aditya. He is a writer and producer, known for Midnights with Adam (2013), Heart & Soles (2012) and Heights...",
      "birthdate": "1990-9-29",
      "url": "http://www.imdb.com/video/user/vi3091568921?ref_=nm_demo_1",
      "awards": "1 win."
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRed4H5_67EHSABcjF4Ut9hM1FeDX6PsJ-6bFnMajzPBdfSVH5W8i9VHP3q"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///name/nm4723897?src=mdot",
      "og:url": "http://www.imdb.com/name/nm4723897/",
      "theme-color": "#000000",
      "pageid": "nm4723897",
      "pagetype": "name",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMjE3NTQ3NzU0NV5BMl5BanBnXkFtZTgwOTEwMjg4MTE@._V1_UY1200_CR115,0,630,1200_AL_.jpg",
      "og:type": "actor",
      "fb:app_id": "115109575169727",
      "og:title": "Yudho Aditya",
      "og:site_name": "IMDb",
      "title": "Yudho Aditya - IMDb",
      "og:description": "Yudho Aditya, Writer: Midnights with Adam. Yudho Aditya was born on September 29, 1990 in Jakarta, Indonesia as Yudho Vanderhof Aditya. He is a writer and producer, known for Midnights with Adam (2013), Heart & Soles (2012) and Heights or A Bisexual Woman's Existential Musings on Los Angeles (2016).",
      "request_id": "1H0FYMVYV9DA6PWGNFJN"
     }
    ],
    "hcard": [
     {
      "fn": "Yudho Aditya",
      "title": "Writer",
      "url": "http://www.imdb.com/video/user/vi4067727897?ref_=nm_demo_2",
      "bday": "1990-09-29",
      "photo": "http://ia.media-imdb.com/images/M/MV5BMTAyNzM0NjI5MzFeQTJeQWpwZ15BbWU3MDA3NzE0Njc@._V1_UX148_CR0,0,148,200_AL_.jpg"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Pipe Dream (2015/I)",
   "htmlTitle": "\u003cb\u003ePipe Dream\u003c/b\u003e (2015/I)",
   "link": "http://www.imdb.com/title/tt3756812/combined",
   "displayLink": "www.imdb.com",
   "snippet": "Directed by Yudho Aditya. With Eric Tabach, Elise Metcalf, Zachary Steinback. \nPeter Epstein-Takahashi is popular with a certain female classmate, but he's ...",
   "htmlSnippet": "Directed by \u003cb\u003eYudho Aditya\u003c/b\u003e. With Eric Tabach, Elise Metcalf, Zachary Steinback. \u003cbr\u003e\nPeter Epstein-Takahashi is popular with a certain female classmate, but he&#39;s&nbsp;...",
   "cacheId": "jL239gn9THsJ",
   "formattedUrl": "www.imdb.com/title/tt3756812/combined",
   "htmlFormattedUrl": "www.imdb.com/title/tt3756812/combined",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTQ3MzIyMTI1MF5BMl5BanBnXkFtZTgwMDIzMjQwNTE@._V1._SX95_SY140_.jpg"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "76",
      "height": "112",
      "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQhPoYy2RStbygZBptPQtFyS5sPwx19bA75HzQt9SLTRa_l81YIrIHc_g"
     }
    ],
    "metatags": [
     {
      "og:url": "http://www.imdb.com/title/tt3756812/combined",
      "title": "Pipe Dream (2015/I)",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTQ3MzIyMTI1MF5BMl5BanBnXkFtZTgwMDIzMjQwNTE@._V1._SX95_SY140_.jpg",
      "application-name": "IMDb",
      "msapplication-tooltip": "IMDb Web App",
      "msapplication-window": "width=1500;height=900",
      "msapplication-task": "name=Find Movie Showtimes;action-uri=/showtimes/;icon-uri=http://i.media-imdb.com/images/SFff39adb4d259f3c3fd166853a6714a32/favicon.ico",
      "og:type": "movie",
      "fb:app_id": "115109575169727",
      "og:title": "Pipe Dream (2015/I)",
      "og:site_name": "IMDb"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Pria (2017) - IMDb",
   "htmlTitle": "Pria (2017) - IMDb",
   "link": "http://www.imdb.com/title/tt5019254/",
   "displayLink": "www.imdb.com",
   "snippet": "Directed by Yudho Aditya. With Chicco ... Photos. Eun-ah Lee, Yudho Aditya and \nChicco Kurniawan in Pria (2017) Add Image · 1 photo » ... Pipe Dream · 10-16.",
   "htmlSnippet": "Directed by \u003cb\u003eYudho Aditya\u003c/b\u003e. With Chicco ... Photos. Eun-ah Lee, \u003cb\u003eYudho Aditya\u003c/b\u003e and \u003cbr\u003e\nChicco Kurniawan in Pria (2017) Add Image &middot; 1 photo » ... \u003cb\u003ePipe Dream\u003c/b\u003e &middot; 10-16.",
   "cacheId": "Qc8BTe8RGFwJ",
   "formattedUrl": "www.imdb.com/title/tt5019254/",
   "htmlFormattedUrl": "www.imdb.com/title/tt5019254/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BZjRkMzc3MzYtNDViNy00NTdjLTg2N2QtNjdkZWNmODFmOWY0XkEyXkFqcGdeQXVyMjU2OTY3MzE@._V1_UY105_CR26,0,105,105_AL_.jpg"
     }
    ],
    "organization": [
     {
      "url": "Babibutafilm",
      "name": "Babibutafilm"
     }
    ],
    "person": [
     {
      "url": "Yudho Aditya",
      "name": "Yudho Aditya"
     },
     {
      "url": "Barbara Cigarroa",
      "name": "Barbara Cigarroa"
     },
     {
      "url": "Yudho Aditya",
      "name": "Yudho Aditya"
     },
     {
      "url": "Chicco Kurniawan",
      "name": "Chicco Kurniawan"
     },
     {
      "url": "Karlina Inawati",
      "name": "Karlina Inawati"
     },
     {
      "url": "Jacob McCarthy",
      "name": "Jacob McCarthy"
     },
     {
      "url": "Chicco Kurniawan",
      "name": "Chicco Kurniawan"
     },
     {
      "url": "Karlina Inawati",
      "name": "Karlina Inawati"
     },
     {
      "url": "Jacob McCarthy",
      "name": "Jacob McCarthy"
     },
     {
      "url": "Otig Pakis",
      "name": "Otig Pakis"
     },
     {
      "url": "Gladhys Elliona Syahutari",
      "name": "Gladhys Elliona Syahutari"
     },
     {
      "url": "H. Jaelani",
      "name": "H. Jaelani"
     },
     {
      "url": "Acum Bin Kosim",
      "name": "Acum Bin Kosim"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "84",
      "height": "84",
      "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYR-tI1_G7Yb2zDi-urcKYuL21PemgKXeGxgxuGHy-vurQEPpNR2v-pg"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt5019254?src=mdot",
      "og:url": "http://www.imdb.com/title/tt5019254/",
      "theme-color": "#000000",
      "pageid": "tt5019254",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/G/01/imdb/images/logos/imdb_fb_logo-1730868325._CB306318125_.png",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Pria (2017)",
      "og:site_name": "IMDb",
      "title": "Pria (2017) - IMDb",
      "og:description": "Directed by Yudho Aditya.  With Chicco Kurniawan, Karlina Inawati, Jacob McCarthy, Otig Pakis. An LGBT teen living in rural Indonesia struggles between the traditions of his upbringing and his romantic idealization of the freedom of the west.",
      "request_id": "0X5GKGB9RJQ0082FXENN"
     }
    ],
    "hcard": [
     {
      "fn": "Yudho Aditya",
      "url": "http://www.imdb.com/name/nm4723897?ref_=tt_ov_dr"
     },
     {
      "fn": "Barbara Cigarroa",
      "url": "http://www.imdb.com/name/nm5291237?ref_=tt_ov_wr"
     },
     {
      "fn": "Yudho Aditya",
      "url": "http://www.imdb.com/name/nm4723897?ref_=tt_ov_wr"
     },
     {
      "fn": "Chicco Kurniawan",
      "url": "http://www.imdb.com/name/nm7820251?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Karlina Inawati",
      "url": "http://www.imdb.com/name/nm1224075?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Jacob McCarthy",
      "url": "http://www.imdb.com/name/nm7058487?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Chicco Kurniawan",
      "url": "http://www.imdb.com/name/nm7820251/?ref_=tt_cl_t1"
     },
     {
      "fn": "Karlina Inawati",
      "url": "http://www.imdb.com/name/nm1224075/?ref_=tt_cl_t2"
     },
     {
      "fn": "Jacob McCarthy",
      "url": "http://www.imdb.com/name/nm7058487/?ref_=tt_cl_t3"
     },
     {
      "fn": "Otig Pakis",
      "url": "http://www.imdb.com/name/nm2683695/?ref_=tt_cl_t4"
     },
     {
      "fn": "Gladhys Elliona Syahutari",
      "url": "http://www.imdb.com/name/nm7821232/?ref_=tt_cl_t5"
     },
     {
      "fn": "H. Jaelani",
      "url": "http://www.imdb.com/name/nm7859704/?ref_=tt_cl_t6"
     },
     {
      "fn": "Acum Bin Kosim",
      "url": "http://www.imdb.com/name/nm7866521/?ref_=tt_cl_t7"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Lilies (2014) - IMDb",
   "htmlTitle": "Lilies (2014) - IMDb",
   "link": "http://www.imdb.com/title/tt3466190/",
   "displayLink": "www.imdb.com",
   "snippet": "Directed by Yudho Aditya. With Priscilla Liang, Dalena ... Pipe Dream I (2015). \nShort | Comedy | Romance ... Director: Yudho Aditya. Stars: Eric Tabach, Elise ...",
   "htmlSnippet": "Directed by \u003cb\u003eYudho Aditya\u003c/b\u003e. With Priscilla Liang, Dalena ... \u003cb\u003ePipe Dream\u003c/b\u003e I (2015). \u003cbr\u003e\nShort | Comedy | Romance ... Director: \u003cb\u003eYudho Aditya\u003c/b\u003e. Stars: Eric Tabach, Elise&nbsp;...",
   "cacheId": "2-3zujjyzWUJ",
   "formattedUrl": "www.imdb.com/title/tt3466190/",
   "htmlFormattedUrl": "www.imdb.com/title/tt3466190/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMjI5NDMzNDQxOV5BMl5BanBnXkFtZTgwMzA1MzIwMTE@._V1_UY1200_CR80,0,630,1200_AL_.jpg"
     }
    ],
    "organization": [
     {
      "url": "DTF Pictures",
      "name": "DTF Pictures"
     }
    ],
    "person": [
     {
      "url": "Yudho Aditya",
      "name": "Yudho Aditya"
     },
     {
      "url": "Yudho Aditya",
      "name": "Yudho Aditya"
     },
     {
      "url": "Priscilla Liang",
      "name": "Priscilla Liang"
     },
     {
      "url": "Dalena Nguyen",
      "name": "Dalena Nguyen"
     },
     {
      "url": "Paul Yen",
      "name": "Paul Yen"
     },
     {
      "url": "Priscilla Liang",
      "name": "Priscilla Liang"
     },
     {
      "url": "Dalena Nguyen",
      "name": "Dalena Nguyen"
     },
     {
      "url": "Paul Yen",
      "name": "Paul Yen"
     },
     {
      "url": "Gene Phan",
      "name": "Gene Phan"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQaW8OE6PE16Vh2hxF8cD3hv0st6Pop-poPI4YC_o1_LUwQYyKrWtQmjFc"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt3466190?src=mdot",
      "og:url": "http://www.imdb.com/title/tt3466190/",
      "theme-color": "#000000",
      "pageid": "tt3466190",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMjI5NDMzNDQxOV5BMl5BanBnXkFtZTgwMzA1MzIwMTE@._V1_UY1200_CR80,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Lilies (2014)",
      "og:site_name": "IMDb",
      "title": "Lilies (2014) - IMDb",
      "og:description": "Directed by Yudho Aditya.  With Priscilla Liang, Dalena Nguyen, Paul Yen, Gene Phan. Past and present coincide when a chance meeting reveals a love story as intricate as origami.",
      "request_id": "17KMJMDWN455GWTF14HZ"
     }
    ],
    "hcard": [
     {
      "fn": "Yudho Aditya",
      "url": "http://www.imdb.com/name/nm4723897?ref_=tt_ov_dr"
     },
     {
      "fn": "Yudho Aditya",
      "url": "http://www.imdb.com/name/nm4723897?ref_=tt_ov_wr"
     },
     {
      "fn": "Priscilla Liang",
      "url": "http://www.imdb.com/name/nm4408517?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Dalena Nguyen",
      "url": "http://www.imdb.com/name/nm5690061?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Paul Yen",
      "url": "http://www.imdb.com/name/nm0947459?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Priscilla Liang",
      "url": "http://www.imdb.com/name/nm4408517/?ref_=tt_cl_t1"
     },
     {
      "fn": "Dalena Nguyen",
      "url": "http://www.imdb.com/name/nm5690061/?ref_=tt_cl_t2"
     },
     {
      "fn": "Paul Yen",
      "url": "http://www.imdb.com/name/nm0947459/?ref_=tt_cl_t3"
     },
     {
      "fn": "Gene Phan",
      "url": "http://www.imdb.com/name/nm5349483/?ref_=tt_cl_t4"
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Dropout (TV Series 2015– ) - IMDb",
   "htmlTitle": "Dropout (TV Series 2015– ) - IMDb",
   "link": "http://www.imdb.com/title/tt4264556/",
   "displayLink": "www.imdb.com",
   "snippet": "People who liked this also liked... Pipe Dream ... Pipe Dream I (2015). Short | \nComedy | Romance ... Director: Yudho Aditya. Stars: Eric Tabach, Elise Metcalf, ...",
   "htmlSnippet": "People who liked this also liked... \u003cb\u003ePipe Dream\u003c/b\u003e ... \u003cb\u003ePipe Dream\u003c/b\u003e I (2015). Short | \u003cbr\u003e\nComedy | Romance ... Director: \u003cb\u003eYudho Aditya\u003c/b\u003e. Stars: Eric Tabach, Elise Metcalf,&nbsp;...",
   "cacheId": "jKeh_vBmg44J",
   "formattedUrl": "www.imdb.com/title/tt4264556/",
   "htmlFormattedUrl": "www.imdb.com/title/tt4264556/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTQ3MzIyMTI1MF5BMl5BanBnXkFtZTgwMDIzMjQwNTE@._V1_UY190_CR0,0,128,190_AL_.jpg"
     }
    ],
    "person": [
     {
      "url": "Bob Mclean",
      "name": "Bob Mclean"
     },
     {
      "url": "Philip Labes",
      "name": "Philip Labes"
     },
     {
      "url": "Zachary Roozen",
      "name": "Zachary Roozen"
     },
     {
      "url": "Bob Mclean",
      "name": "Bob Mclean"
     },
     {
      "url": "Philip Labes",
      "name": "Philip Labes"
     },
     {
      "url": "Zachary Roozen",
      "name": "Zachary Roozen"
     },
     {
      "url": "Mariah Robinson",
      "name": "Mariah Robinson"
     },
     {
      "url": "Adam Venker",
      "name": "Adam Venker"
     },
     {
      "url": "Susie Yankou",
      "name": "Susie Yankou"
     },
     {
      "url": "Aaron Izek",
      "name": "Aaron Izek"
     },
     {
      "url": "Joanne Atkinson",
      "name": "Joanne Atkinson"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "102",
      "height": "152",
      "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSHZs3VBkTIuiWBrzwCenJnb0XSOzY_57j9VcyLSqIZaA-uSJcwrm_2VQ"
     }
    ],
    "tvseries": [
     {
      "name": "Dropout",
      "genre": "Comedy",
      "description": "Dropout is a comedic web series about a 17-year-old who quits school because he can't wait for the real world to start.",
      "image": "http://ia.media-imdb.com/images/M/MV5BMjUwNDkxMjcyMV5BMl5BanBnXkFtZTcwODUyMDMyNw@@._UY450_CR200,80,307,230_SY230_SX307_AL_.jpg",
      "url": "USA"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt4264556?src=mdot",
      "og:url": "http://www.imdb.com/title/tt4264556/",
      "theme-color": "#000000",
      "pageid": "tt4264556",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/G/01/imdb/images/logos/imdb_fb_logo-1730868325._CB306318125_.png",
      "og:type": "video.tv_show",
      "fb:app_id": "115109575169727",
      "og:title": "Dropout (TV Series 2015– )",
      "og:site_name": "IMDb",
      "title": "Dropout (TV Series 2015– ) - IMDb",
      "og:description": "With Bob Mclean, Philip Labes, Zachary Roozen, Mariah Robinson. Dropout is a comedic web series about a 17-year-old who quits school because he can't wait for the real world to start.",
      "request_id": "1ZEX071AAHB9J3VX3JJW"
     }
    ],
    "moviereview": [
     {
      "image_href": "http://ia.media-imdb.com/images/G/01/imdb/images/widget/amazon._CB339202444_.png",
      "name": "Dropout",
      "genre": "Comedy/Drama",
      "starring": "Bob Mclean, Philip Labes, Zachary Roozen",
      "summary": "Dropout is a comedic web series about a 17-year-old who quits school because he can't wait for the real world to start."
     }
    ]
   }
  },
  {
   "kind": "customsearch#result",
   "title": "Laugh Along the Way (2015) - IMDb",
   "htmlTitle": "Laugh Along the Way (2015) - IMDb",
   "link": "http://www.imdb.com/title/tt4007486/",
   "displayLink": "www.imdb.com",
   "snippet": "Pipe Dream. Roots. Twilight. Dead of Summer. ◅ Prev 6 Next 6 ▻. Tomorrow. \nAdd to Watchlist. 0 Next ». Tomorrow III (2014). Short | Drama. 1 2 3 4 5 6 7 8 9 \n10 ...",
   "htmlSnippet": "\u003cb\u003ePipe Dream\u003c/b\u003e. Roots. Twilight. Dead of Summer. ◅ Prev 6 Next 6 ▻. Tomorrow. \u003cbr\u003e\nAdd to Watchlist. 0 Next ». Tomorrow III (2014). Short | Drama. 1 2 3 4 5 6 7 8 9 \u003cbr\u003e\n10&nbsp;...",
   "cacheId": "RMFD1G1s3KMJ",
   "formattedUrl": "www.imdb.com/title/tt4007486/",
   "htmlFormattedUrl": "www.imdb.com/title/tt4007486/",
   "pagemap": {
    "cse_image": [
     {
      "src": "http://ia.media-imdb.com/images/M/MV5BMTcxODI2NjU3OF5BMl5BanBnXkFtZTgwNzk5ODI0MzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg"
     }
    ],
    "person": [
     {
      "url": "Brandon Baer",
      "name": "Brandon Baer"
     },
     {
      "url": "David Mandell",
      "name": "David Mandell"
     },
     {
      "url": "David Mandell",
      "name": "David Mandell"
     },
     {
      "url": "David Mandell",
      "name": "David Mandell"
     },
     {
      "url": "Kelton DuMont",
      "name": "Kelton DuMont"
     },
     {
      "url": "Zachary Roozen",
      "name": "Zachary Roozen"
     },
     {
      "url": "David Mandell",
      "name": "David Mandell"
     },
     {
      "url": "Kelton DuMont",
      "name": "Kelton DuMont"
     },
     {
      "url": "Zachary Roozen",
      "name": "Zachary Roozen"
     },
     {
      "url": "Amber Coney",
      "name": "Amber Coney"
     },
     {
      "url": "James DuMont",
      "name": "James DuMont"
     },
     {
      "url": "Elizabeth Burr",
      "name": "Elizabeth Burr"
     },
     {
      "url": "Hilty Bowen",
      "name": "Hilty Bowen"
     },
     {
      "url": "Ali Gallo",
      "name": "Ali Gallo"
     },
     {
      "url": "Charlotte Guerry",
      "name": "Charlotte Guerry"
     },
     {
      "url": "Andrea Moore",
      "name": "Andrea Moore"
     },
     {
      "url": "Aubrey Rhodes",
      "name": "Aubrey Rhodes"
     },
     {
      "url": "Sammantha Demmeyer",
      "name": "Sammantha Demmeyer"
     },
     {
      "url": "Julia Stier",
      "name": "Julia Stier"
     },
     {
      "url": "Erin Soares",
      "name": "Erin Soares"
     },
     {
      "url": "Katie Snyder",
      "name": "Katie Snyder"
     }
    ],
    "cse_thumbnail": [
     {
      "width": "163",
      "height": "310",
      "src": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRjDEfPn3UnXTS6nDoF_ufiXKDuDqaS5r0i-3uB2Uw8t0MLQjrf-58xN3S1"
     }
    ],
    "metatags": [
     {
      "apple-itunes-app": "app-id=342792525, app-argument=imdb:///title/tt4007486?src=mdot",
      "og:url": "http://www.imdb.com/title/tt4007486/",
      "theme-color": "#000000",
      "pageid": "tt4007486",
      "pagetype": "title",
      "subpagetype": "main",
      "og:image": "http://ia.media-imdb.com/images/M/MV5BMTcxODI2NjU3OF5BMl5BanBnXkFtZTgwNzk5ODI0MzE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
      "og:type": "video.movie",
      "fb:app_id": "115109575169727",
      "og:title": "Laugh Along the Way (2015)",
      "og:site_name": "IMDb",
      "title": "Laugh Along the Way (2015) - IMDb",
      "og:description": "Directed by Brandon Baer.  With David Mandell, Kelton DuMont, Zachary Roozen, Amber Coney. In chemotherapy, John, a newly diagnosed high school senior, befriends an 11-year-old Sam and with Sam's older brother, who was once bullied by John, help John come to terms with his cancer.",
      "request_id": "1JE2QABB6BWA74GAAQXA"
     }
    ],
    "hcard": [
     {
      "fn": "Brandon Baer",
      "url": "http://www.imdb.com/name/nm5142289?ref_=tt_ov_dr"
     },
     {
      "fn": "David Mandell",
      "url": "http://www.imdb.com/name/nm5522710?ref_=tt_ov_wr"
     },
     {
      "fn": "David Mandell",
      "url": "http://www.imdb.com/name/nm5522710?ref_=tt_ov_wr"
     },
     {
      "fn": "David Mandell",
      "url": "http://www.imdb.com/name/nm5522710?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Kelton DuMont",
      "url": "http://www.imdb.com/name/nm6374072?ref_=tt_ov_st_sm"
     },
     {
      "fn": "Zachary Roozen",
      "url": "http://www.imdb.com/name/nm4635907?ref_=tt_ov_st_sm"
     },
     {
      "fn": "David Mandell",
      "url": "http://www.imdb.com/name/nm5522710/?ref_=tt_cl_t1"
     },
     {
      "fn": "Kelton DuMont",
      "url": "http://www.imdb.com/name/nm6374072/?ref_=tt_cl_t2"
     },
     {
      "fn": "Zachary Roozen",
      "url": "http://www.imdb.com/name/nm4635907/?ref_=tt_cl_t3"
     },
     {
      "fn": "Amber Coney",
      "url": "http://www.imdb.com/name/nm4371874/?ref_=tt_cl_t4"
     },
     {
      "fn": "James DuMont",
      "url": "http://www.imdb.com/name/nm0003069/?ref_=tt_cl_t5"
     },
     {
      "fn": "Elizabeth Burr",
      "url": "http://www.imdb.com/name/nm6767170/?ref_=tt_cl_t6"
     },
     {
      "fn": "Hilty Bowen",
      "url": "http://www.imdb.com/name/nm5167893/?ref_=tt_cl_t7"
     },
     {
      "fn": "Ali Gallo",
      "url": "http://www.imdb.com/name/nm6821153/?ref_=tt_cl_t8"
     },
     {
      "fn": "Charlotte Guerry",
      "url": "http://www.imdb.com/name/nm6821157/?ref_=tt_cl_t9"
     },
     {
      "fn": "Andrea Moore",
      "url": "http://www.imdb.com/name/nm6821156/?ref_=tt_cl_t10"
     },
     {
      "fn": "Aubrey Rhodes",
      "url": "http://www.imdb.com/name/nm6828554/?ref_=tt_cl_t11"
     },
     {
      "fn": "Sammantha Demmeyer",
      "url": "http://www.imdb.com/name/nm6821158/?ref_=tt_cl_t12"
     },
     {
      "fn": "Julia Stier",
      "url": "http://www.imdb.com/name/nm6821154/?ref_=tt_cl_t13"
     },
     {
      "fn": "Erin Soares",
      "url": "http://www.imdb.com/name/nm6821159/?ref_=tt_cl_t14"
     },
     {
      "fn": "Katie Snyder",
      "url": "http://www.imdb.com/name/nm6821160/?ref_=tt_cl_t15"
     }
    ]
   }
  }
 ]
}



with open ('output2.csv', 'wb') as csvoutput: 
		fieldnames = ['Entity','url','Director','Year','Alias','IMDB URL','genre','Runtime']
		writer = csv.DictWriter(csvoutput, fieldnames=fieldnames)
		writer.writeheader()

		response = res.get('items')
		if response:
			flag = 0
			for i in range(0,len(response)):
				print "===================================="
				json_title = res['items'][i]['pagemap']['metatags'][0]['title']
				json_title = re.sub(r'<.*?>','',json_title)
				print 'fetched title:',json_title

				json_director = res['items'][i]['snippet']
				json_director = re.sub(r'...','',json_director)
				json_director = re.search(r'Yudho Aditya',json_director)
			 
				if re.sub(r'\s+\(.*','',json_title).strip() == 'Pipe Dream':
					print "##"
					if json_director is None:
						print "###"
						try:
							print 'isnside try'
							json_director = res['items'][i]['pagemap']['metatags'][0]['og:description']
							json_director = re.search(r'Yudho Aditya',json_director)
							if json_director:
								print '####' 
								if json_director.group(0) == 'Yudho Aditya':
									print '#####'
									imdb_key = res['items'][i]['link']
									print imdb_key
									writer.writerow({'Entity':'Pipe Dream','Director':'Yudho Aditya','IMDB URL': imdb_key})
									break
								else:
									print "######"
								
						except:
							print "director not found"
							
				else:
					print 'no key found'
					flag = 1
			if flag == 1:
				print "FUCK == FUCK == FUCK"
				print flag	
				writer.writerow({'Entity':'Pipe Dream','Director':'Yudho Aditya','IMDB URL': 'ww'})
		elif response is None:
			print 'No Response'
			writer.writerow({'Entity':'Pipe Dream','Director':'Yudho Aditya','IMDB URL': ''})