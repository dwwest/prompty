{
    "GET": {
        "scheme": "https",
        "host": "caching.graphql.imdb.com",
        "filename": "/",
        "query": {
            "operationName": "AdvancedTitleSearch",
            "variables": "{\"after\":\"eyJlc1Rva2VuIjpbIjExNjMyNDMiLCI3MDMiLCJ0dDAxMTAzNTciXSwiZmlsdGVyIjoie1wiY29uc3RyYWludHNcIjp7XCJ0aXRsZVR5cGVDb25zdHJhaW50XCI6e1wiYW55VGl0bGVUeXBlSWRzXCI6W1wibW92aWVcIl0sXCJleGNsdWRlVGl0bGVUeXBlSWRzXCI6W119LFwidXNlclJhdGluZ3NDb25zdHJhaW50XCI6e1wicmF0aW5nc0NvdW50UmFuZ2VcIjp7XCJtaW5cIjoyNTAwMH19fSxcImxhbmd1YWdlXCI6XCJlbi1VU1wiLFwic29ydFwiOntcInNvcnRCeVwiOlwiVVNFUl9SQVRJTkdfQ09VTlRcIixcInNvcnRPcmRlclwiOlwiREVTQ1wifSxcInJlc3VsdEluZGV4XCI6NDl9In0=\",\"first\":50,\"locale\":\"en-US\",\"sortBy\":\"USER_RATING_COUNT\",\"sortOrder\":\"DESC\",\"titleTypeConstraint\":{\"anyTitleTypeIds\":[\"movie\"],\"excludeTitleTypeIds\":[]},\"userRatingsConstraint\":{\"ratingsCountRange\":{\"min\":25000}}}",
            "extensions": "{\"persistedQuery\":{\"sha256Hash\":\"f3e9d880ef5404e832446904abc3c455b762cf23c66089c3747ae96dfb3c0065\",\"version\":1}}"
        },
        "remote": {
            "Address": "18.238.55.6:443"
        }
    }
}

example = 'https: //caching.graphql.imdb.com/?operationName=AdvancedTitleSearch&variables={"after":"eyJlc1Rva2VuIjpbIjExNjMyNDMiLCI3MDMiLCJ0dDAxMTAzNTciXSwiZmlsdGVyIjoie1wiY29uc3RyYWludHNcIjp7XCJ0aXRsZVR5cGVDb25zdHJhaW50XCI6e1wiYW55VGl0bGVUeXBlSWRzXCI6W1wibW92aWVcIl0sXCJleGNsdWRlVGl0bGVUeXBlSWRzXCI6W119LFwidXNlclJhdGluZ3NDb25zdHJhaW50XCI6e1wicmF0aW5nc0NvdW50UmFuZ2VcIjp7XCJtaW5cIjoyNTAwMH19fSxcImxhbmd1YWdlXCI6XCJlbi1VU1wiLFwic29ydFwiOntcInNvcnRCeVwiOlwiVVNFUl9SQVRJTkdfQ09VTlRcIixcInNvcnRPcmRlclwiOlwiREVTQ1wifSxcInJlc3VsdEluZGV4XCI6NDl9In0=","first":50,"locale":"en-US","sortBy":"USER_RATING_COUNT","sortOrder":"DESC","titleTypeConstraint":{"anyTitleTypeIds":["movie"],"excludeTitleTypeIds":[]},"userRatingsConstraint":{"ratingsCountRange":{"min":25000}}}&extensions={"persistedQuery":{"sha256Hash":"f3e9d880ef5404e832446904abc3c455b762cf23c66089c3747ae96dfb3c0065","version":1}}'
example_after = "eyJlc1Rva2VuIjpbIjExNjMyNDMiLCI3MDMiLCJ0dDAxMTAzNTciXSwiZmlsdGVyIjoie1wiY29uc3RyYWludHNcIjp7XCJ0aXRsZVR5cGVDb25zdHJhaW50XCI6e1wiYW55VGl0bGVUeXBlSWRzXCI6W1wibW92aWVcIl0sXCJleGNsdWRlVGl0bGVUeXBlSWRzXCI6W119LFwidXNlclJhdGluZ3NDb25zdHJhaW50XCI6e1wicmF0aW5nc0NvdW50UmFuZ2VcIjp7XCJtaW5cIjoyNTAwMH19fSxcImxhbmd1YWdlXCI6XCJlbi1VU1wiLFwic29ydFwiOntcInNvcnRCeVwiOlwiVVNFUl9SQVRJTkdfQ09VTlRcIixcInNvcnRPcmRlclwiOlwiREVTQ1wifSxcInJlc3VsdEluZGV4XCI6NDl9In0="
example_vars = {
    "after": example_after,
    "first": 50,
    "locale": "en-US",
    "sortBy": "USER_RATING_COUNT",
    "sortOrder": "DESC",
    "titleTypeConstraint": {
        "anyTitleTypeIds": [
            "movie"
        ],
        "excludeTitleTypeIds": []
    },
    "userRatingsConstraint": {
        "ratingsCountRange": {
            "min": 25000
        }
    }
}
# [vote count, ?, id]
decoded_after = b'{"esToken":["1163243","703","tt0110357"],"filter":"{\\"constraints\\":{\\"titleTypeConstraint\\":{\\"anyTitleTypeIds\\":[\\"movie\\"],\\"excludeTitleTypeIds\\":[]},\\"userRatingsConstraint\\":{\\"ratingsCountRange\\":{\\"min\\":25000}}},\\"language\\":\\"en-US\\",\\"sort\\":{\\"sortBy\\":\\"USER_RATING_COUNT\\",\\"sortOrder\\":\\"DESC\\"},\\"resultIndex\\":49}"}'

extensions={
    "persistedQuery": {
        "sha256Hash": "f3e9d880ef5404e832446904abc3c455b762cf23c66089c3747ae96dfb3c0065",
        "version": 1
    }
}