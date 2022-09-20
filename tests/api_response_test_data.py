success_data = {
    "items": [
        {
            "request_url": "KNDPM3AC8N7015597?odometer=13&date=2021-12-29",
            "response_status": 200,
            "response_body": {
                "href": "https://api.manheim.com/valuations/vin/KNDPM3AC8N7015597?country=US&date=2021-12-29&odometer=13",
                "count": 1,
                "items": [
                    {
                        "href": "https://api.manheim.com/valuations/id/202208559805724?country=US&date=2021-12-29&odometer=13",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202208559805724?country=US&date=2021-12-29&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "bestMatch": True,
                        "wholesale": {
                            "above": 32700,
                            "below": 28000,
                            "average": 30400
                        },
                        "sampleSize": "6",
                        "description": {
                            "make": "KIA",
                            "trim": "4D SUV 2.4L LX",
                            "year": 2022,
                            "model": "SPORTAGE FWD",
                            "subSeries": "LX"
                        },
                        "averageGrade": 47,
                        "returnedDate": "2021-12-29",
                        "valuationsId": "202208559805724",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-29",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 33400,
                                "below": 28700,
                                "average": 31000
                            },
                            "adjustedBy": {
                                "Odometer": "13",
                                "OdometerAdjustmentValue": "680"
                            }
                        },
                        "averageOdometer": 5326
                    }
                ]
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        }
    ]
}

no_best_match = {"items": [
    {
        "request_url": "WBA43AT0XNCJ44572?odometer=11&date=2021-12-31",
        "response_status": 200,
        "response_body": {
            "href": "https://api.manheim.com/valuations/vin/WBA43AT0XNCJ44572?country=US&date=2021-12-31&odometer=11",
            "count": 2,
            "items": [
                {
                    "href": "https://api.manheim.com/valuations/id/202200666940042?country=US&date=2021-12-31&odometer=11",
                    "samples": {
                        "href": "https://api.manheim.com/valuation-samples/id/202200666940042?country=US&date=2021-12-31&orderBy=location+asc&limit=25&start=1"
                    },
                    "currency": "USD",
                    "wholesale": {
                        "above": 0,
                        "below": 0,
                        "average": 0
                    },
                    "sampleSize": "0",
                    "description": {
                        "make": "B M W",
                        "trim": "2D CONVERTIBLE 430I XDRIVE",
                        "year": 2022,
                        "model": "4 SERIES",
                        "subSeries": "430I XDRIV"
                    },
                    "averageGrade": 0,
                    "returnedDate": "2021-12-31",
                    "valuationsId": "202200666940042",
                    "odometerUnits": "miles",
                    "requestedDate": "2021-12-31",
                    "adjustedPricing": {
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "adjustedBy": {}
                    },
                    "averageOdometer": 0
                },
                {
                    "href": "https://api.manheim.com/valuations/id/202200666940334?country=US&date=2021-12-31&odometer=11",
                    "samples": {
                        "href": "https://api.manheim.com/valuation-samples/id/202200666940334?country=US&date=2021-12-31&orderBy=location+asc&limit=25&start=1"
                    },
                    "currency": "USD",
                    "wholesale": {
                        "above": 0,
                        "below": 0,
                        "average": 0
                    },
                    "sampleSize": "0",
                    "description": {
                        "make": "B M W",
                        "trim": "2D CONVERTIBLE 430I XDRIVE MSPT",
                        "year": 2022,
                        "model": "4 SERIES",
                        "subSeries": "430I MSPT"
                    },
                    "averageGrade": 0,
                    "returnedDate": "2021-12-31",
                    "valuationsId": "202200666940334",
                    "odometerUnits": "miles",
                    "requestedDate": "2021-12-31",
                    "adjustedPricing": {
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "adjustedBy": {}
                    },
                    "averageOdometer": 0
                }
            ]
        },
        "request_headers": {
            "X-Mashery-Host": "api.manheim.com",
            "X-Mashery-Plan": "Internal",
            "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
            "X-Mashery-Username": "cads__sword"
        }
    }]}
test_data = {
    "items": [
        {
            "request_url": "3GKALMEV3NL119778?odometer=7&date=2021-12-31",
            "response_status": 404,
            "response_body": {
                "message": "Matching vehicles not found",
                "developerMessage": "Matching vehicles not found"
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "3GTU9DED6NG146805?odometer=8&date=2021-12-29",
            "response_status": 404,
            "response_body": {
                "message": "Matching vehicles not found",
                "developerMessage": "Matching vehicles not found"
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "5TFLA5DB4NX001671?odometer=15&date=2021-12-30",
            "response_status": 404,
            "response_body": {
                "message": "Matching vehicles not found",
                "developerMessage": "Matching vehicles not found"
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "KNDPM3AC8N7015597?odometer=13&date=2021-12-29",
            "response_status": 200,
            "response_body": {
                "href": "https://api.manheim.com/valuations/vin/KNDPM3AC8N7015597?country=US&date=2021-12-29&odometer=13",
                "count": 1,
                "items": [
                    {
                        "href": "https://api.manheim.com/valuations/id/202208559805724?country=US&date=2021-12-29&odometer=13",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202208559805724?country=US&date=2021-12-29&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "bestMatch": True,
                        "wholesale": {
                            "above": 32700,
                            "below": 28000,
                            "average": 30400
                        },
                        "sampleSize": "6",
                        "description": {
                            "make": "KIA",
                            "trim": "4D SUV 2.4L LX",
                            "year": 2022,
                            "model": "SPORTAGE FWD",
                            "subSeries": "LX"
                        },
                        "averageGrade": 47,
                        "returnedDate": "2021-12-29",
                        "valuationsId": "202208559805724",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-29",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 33400,
                                "below": 28700,
                                "average": 31000
                            },
                            "adjustedBy": {
                                "Odometer": "13",
                                "OdometerAdjustmentValue": "680"
                            }
                        },
                        "averageOdometer": 5326
                    }
                ]
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "WBA43AT0XNCJ44572?odometer=11&date=2021-12-31",
            "response_status": 200,
            "response_body": {
                "href": "https://api.manheim.com/valuations/vin/WBA43AT0XNCJ44572?country=US&date=2021-12-31&odometer=11",
                "count": 2,
                "items": [
                    {
                        "href": "https://api.manheim.com/valuations/id/202200666940042?country=US&date=2021-12-31&odometer=11",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202200666940042?country=US&date=2021-12-31&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "sampleSize": "0",
                        "description": {
                            "make": "B M W",
                            "trim": "2D CONVERTIBLE 430I XDRIVE",
                            "year": 2022,
                            "model": "4 SERIES",
                            "subSeries": "430I XDRIV"
                        },
                        "averageGrade": 0,
                        "returnedDate": "2021-12-31",
                        "valuationsId": "202200666940042",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-31",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 0,
                                "below": 0,
                                "average": 0
                            },
                            "adjustedBy": {}
                        },
                        "averageOdometer": 0
                    },
                    {
                        "href": "https://api.manheim.com/valuations/id/202200666940334?country=US&date=2021-12-31&odometer=11",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202200666940334?country=US&date=2021-12-31&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "sampleSize": "0",
                        "description": {
                            "make": "B M W",
                            "trim": "2D CONVERTIBLE 430I XDRIVE MSPT",
                            "year": 2022,
                            "model": "4 SERIES",
                            "subSeries": "430I MSPT"
                        },
                        "averageGrade": 0,
                        "returnedDate": "2021-12-31",
                        "valuationsId": "202200666940334",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-31",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 0,
                                "below": 0,
                                "average": 0
                            },
                            "adjustedBy": {}
                        },
                        "averageOdometer": 0
                    }
                ]
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "1FT7X2B6XNEC49200?odometer=20&date=2021-12-30",
            "response_status": 200,
            "response_body": {
                "href": "https://api.manheim.com/valuations/vin/1FT7X2B6XNEC49200?country=US&date=2021-12-30&odometer=20",
                "count": 3,
                "items": [
                    {
                        "href": "https://api.manheim.com/valuations/id/202201757675750?country=US&date=2021-12-30&odometer=20",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202201757675750?country=US&date=2021-12-30&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "sampleSize": "0",
                        "description": {
                            "make": "FORD",
                            "trim": "EXT CAB 6.2L LARIAT",
                            "year": 2022,
                            "model": "F250 4WD V8 FFV",
                            "subSeries": "LARIAT"
                        },
                        "averageGrade": 0,
                        "returnedDate": "2021-12-30",
                        "valuationsId": "202201757675750",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-30",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 0,
                                "below": 0,
                                "average": 0
                            },
                            "adjustedBy": {}
                        },
                        "averageOdometer": 0
                    },
                    {
                        "href": "https://api.manheim.com/valuations/id/202201757675754?country=US&date=2021-12-30&odometer=20",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202201757675754?country=US&date=2021-12-30&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "sampleSize": "0",
                        "description": {
                            "make": "FORD",
                            "trim": "EXT CAB 6.2L XL",
                            "year": 2022,
                            "model": "F250 4WD V8 FFV",
                            "subSeries": "XL"
                        },
                        "averageGrade": 0,
                        "returnedDate": "2021-12-30",
                        "valuationsId": "202201757675754",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-30",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 0,
                                "below": 0,
                                "average": 0
                            },
                            "adjustedBy": {}
                        },
                        "averageOdometer": 0
                    },
                    {
                        "href": "https://api.manheim.com/valuations/id/202201757675755?country=US&date=2021-12-30&odometer=20",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202201757675755?country=US&date=2021-12-30&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "sampleSize": "0",
                        "description": {
                            "make": "FORD",
                            "trim": "EXT CAB 6.2L XLT",
                            "year": 2022,
                            "model": "F250 4WD V8 FFV",
                            "subSeries": "XLT"
                        },
                        "averageGrade": 0,
                        "returnedDate": "2021-12-30",
                        "valuationsId": "202201757675755",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-30",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 0,
                                "below": 0,
                                "average": 0
                            },
                            "adjustedBy": {}
                        },
                        "averageOdometer": 0
                    }
                ]
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "WA1B4AFY9N2039787?date=2021-12-30",
            "response_status": 404,
            "response_body": {
                "message": "Matching vehicles not found",
                "developerMessage": "Matching vehicles not found"
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "3N1AB8DV4NY204982?odometer=10&date=2021-12-29",
            "response_status": 404,
            "response_body": {
                "message": "Matching vehicles not found",
                "developerMessage": "Matching vehicles not found"
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "3GNKBKRS7NS124096?date=2021-12-30",
            "response_status": 200,
            "response_body": {
                "href": "https://api.manheim.com/valuations/vin/3GNKBKRS7NS124096?country=US&date=2021-12-30&odometer=0",
                "count": 1,
                "items": [
                    {
                        "href": "https://api.manheim.com/valuations/id/202201176340110?country=US&date=2021-12-30&odometer=0",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202201176340110?country=US&date=2021-12-30&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "bestMatch": True,
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "sampleSize": "0",
                        "description": {
                            "make": "CHEVROLET",
                            "trim": "4D SUV RS",
                            "year": 2022,
                            "model": "BLAZER AWD V6",
                            "subSeries": "RS"
                        },
                        "averageGrade": 0,
                        "returnedDate": "2021-12-30",
                        "valuationsId": "202201176340110",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-30",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 0,
                                "below": 0,
                                "average": 0
                            },
                            "adjustedBy": {}
                        },
                        "averageOdometer": 0
                    }
                ]
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        },
        {
            "request_url": "4S4BTAAC2N3175429?odometer=4&date=2021-12-29",
            "response_status": 200,
            "response_body": {
                "href": "https://api.manheim.com/valuations/vin/4S4BTAAC2N3175429?country=US&date=2021-12-29&odometer=4",
                "count": 1,
                "items": [
                    {
                        "href": "https://api.manheim.com/valuations/id/202204815660010?country=US&date=2021-12-29&odometer=4",
                        "samples": {
                            "href": "https://api.manheim.com/valuation-samples/id/202204815660010?country=US&date=2021-12-29&orderBy=location+asc&limit=25&start=1"
                        },
                        "currency": "USD",
                        "bestMatch": True,
                        "wholesale": {
                            "above": 0,
                            "below": 0,
                            "average": 0
                        },
                        "sampleSize": "0",
                        "description": {
                            "make": "SUBARU",
                            "trim": "4D SUV 2.5L",
                            "year": 2022,
                            "model": "OUTBACK",
                            "subSeries": "NONE"
                        },
                        "averageGrade": 0,
                        "returnedDate": "2021-12-29",
                        "valuationsId": "202204815660010",
                        "odometerUnits": "miles",
                        "requestedDate": "2021-12-29",
                        "adjustedPricing": {
                            "wholesale": {
                                "above": 0,
                                "below": 0,
                                "average": 0
                            },
                            "adjustedBy": {}
                        },
                        "averageOdometer": 0
                    }
                ]
            },
            "request_headers": {
                "X-Mashery-Host": "api.manheim.com",
                "X-Mashery-Plan": "Internal",
                "X-CoxAuto-Bulk-ID": "019c35a8-7741-495f-aa20-9e4346699b52",
                "X-Mashery-Username": "cads__sword"
            }
        }
    ]
}
