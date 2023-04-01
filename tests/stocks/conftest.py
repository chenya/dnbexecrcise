import asyncio

import httpx
import pytest

from ...src.main import app
from ...src.stocks.models import StockPerformance


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def async_client():
    async with httpx.AsyncClient(
        app=app, base_url="http://127.0.0.1:8000"
    ) as client:
        yield client


@pytest.fixture(scope="session")
def stock_performance() -> StockPerformance:
    sample_performance: dict[str, str] = {
        "5 Day": "1.82%",
        "1 Month": "8.04%",
        "3 Month": "25.58%",
        "YTD": "25.58%",
        "1 Year": "-6.39%",
    }
    return StockPerformance(**sample_performance)


@pytest.fixture(scope="session")
def html_sample() -> str:
    return """<!DOCTYPE html>
        <html class="icons-loaded" lang="en">
        <head>
                <title>AAPL Stock Price | Apple Inc. Stock Quote (U.S.: Nasdaq) | MarketWatch</title>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0, width=device-width">
                    <meta name="robots" content="noarchive, noodp">


        <link rel="dns-prefetch" href="//sts.wsj.net" />
        <link rel="dns-prefetch" href="//s.marketwatch.com" />
        <link rel="dns-prefetch" href="//video-api.wsj.com" />
        <link rel="dns-prefetch" href="//fonts.wsj.net" />
        <link rel="dns-prefetch" href="//m.wsj.net" />
        <link rel="dns-prefetch" href="//mwstream.wsj.net" />
        <link rel="dns-prefetch" href="//tags.tiqcdn.com" />
        <link rel="dns-prefetch" href="//s.ntv.io" />
        <link rel="dns-prefetch" href="//cdn.cxense.com" />
        <link rel="dns-prefetch" href="//a248.e.akamai.net" />
        <link rel="dns-prefetch" href="//om.dowjoneson.com" />
        <link rel="dns-prefetch" href="//bam.nr-data.net" />
        <link rel="dns-prefetch" href="//www.googletagservices.com" />
        <link rel="dns-prefetch" href="//partner.googleadservices.com" />
        <link rel="dns-prefetch" href="//pagead2.googlesyndication.com" />
        <link rel="dns-prefetch" href="//pubads.g.doubleclick.net" />
        <link rel="dns-prefetch" href="//tpc.googlesyndication.com" />
        <link rel="dns-prefetch" href="//tealium.hs.llnwd.net"/>
        <link rel="dns-prefetch" href="//contextual.media.net" />
        <link rel="dns-prefetch" href="//js-agent.newrelic.com" />
        <link as="script" href="https://cdn.cxense.com/cx.js" rel="preload">
        <link as="script" href="https://cdn.cxense.com/cx.cce.js" rel="preload">



        <style>
        /* latin-ext */
        @font-face {
        font-family: 'Lato';
        font-style: italic;
        font-weight: 400;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-400-italic.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Lato';
        font-style: italic;
        font-weight: 400;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-400-italic.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 400;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-400-normal.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 400;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-400-normal.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Lato';
        font-style: italic;
        font-weight: 700;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-700-italic.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Lato';
        font-style: italic;
        font-weight: 700;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-700-italic.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 700;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-700-normal.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 700;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-700-normal.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 900;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-900-normal.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Lato';
        font-style: normal;
        font-weight: 900;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-900-normal.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* vietnamese */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 300;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-300-normal.woff2') format('woff2');
        unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 300;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-300-normal.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 300;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-300-normal.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* vietnamese */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 400;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-400-normal.woff2') format('woff2');
        unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 400;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-400-normal.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 400;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-400-normal.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* vietnamese */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 600;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-600-normal.woff2') format('woff2');
        unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 600;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-600-normal.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 600;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-600-normal.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* vietnamese */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 700;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-700-normal.woff2') format('woff2');
        unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 700;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-700-normal.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 700;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-700-normal.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        /* vietnamese */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 800;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-800-normal.woff2') format('woff2');
        unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;
        }
        /* latin-ext */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 800;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-800-normal.woff2') format('woff2');
        unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
        }
        /* latin */
        @font-face {
        font-family: 'Mulish';
        font-style: normal;
        font-weight: 800;
        font-display: optional;
        src: url('https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-800-normal.woff2') format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
        }
        </style>


        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-400-italic.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-400-italic.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-400-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-400-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-700-italic.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-700-italic.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-700-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-700-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-ext-900-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/lato/lato-latin-900-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-300-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-300-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-300-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-400-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-400-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-400-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-600-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-600-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-600-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-700-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-700-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-700-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-vietnamese-800-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-ext-800-normal.woff2" type="font/woff2" crossorigin>
        <link rel="preload" as="font" href="https://sts3.wsj.net/bucket-a/maggie/static/fonts/mulish/mulish-latin-800-normal.woff2" type="font/woff2" crossorigin><link href="https://mw4.wsj.net/mw5/content/images/favicons/apple-touch-icon.png" rel="apple-touch-icon" />
        <link href="https://mw4.wsj.net/mw5/content/images/favicons/apple-touch-icon-152x152.png" rel="apple-touch-icon" sizes="152x152" />
        <link href="https://mw4.wsj.net/mw5/content/images/favicons/apple-touch-icon-167x167.png" rel="apple-touch-icon" sizes="167x167" />
        <link href="https://mw4.wsj.net/mw5/content/images/favicons/apple-touch-icon-180x180.png" rel="apple-touch-icon" sizes="180x180" />
        <link href="https://mw4.wsj.net/mw5/content/logos/favicon.ico" rel="shortcut icon" />        <meta name="apple-itunes-app" content="app-id=336693422">
                <meta name="fb:app_id" content="283204329838">
                <meta property="fb:pages" content="131043201847" />
                <meta property="og:site_name" content="MarketWatch">
                <meta name="twitter:site:id" content="624413">
                <meta name="twitter:domain" content="marketwatch.com">
                <meta name="twitter:image:width" content="1200">
                <meta name="twitter:image:height" content="630">
                <meta name="twitter:card" content="summary_large_image">
                <meta name="twitter:creator" content="@marketwatch">
                <meta name="referrer" content="no-referrer-when-downgrade">
                    <meta name="twitter:image" content="https://s.wsj.net/public/resources/MWimages/MW-EG169_articl_NS_20160223171404.png">
                <meta name="article:publisher" content="https://www.facebook.com/marketwatch">
                <meta name="theme-color" content="#2e2e2f" />
                <meta name="chartjs" content="https://sts3.wsj.net/bucket-a/maggie/static/js/chart-33bd87a969.min.js">




                <meta name="parsely-tags" content="PageType: Quotes, US:AAPL, Stock, US: U.S.: Nasdaq, NAS, page-Overview" />
                <meta name="name" content="Apple Inc." />
                <meta name="tickerSymbol" content="AAPL" />
                <meta name="chartingSymbol" content="STOCK/US/XNAS/AAPL" />
                <meta name="instrumentType" content="Stock" />
                <meta name="exchange" content="U.S.: Nasdaq" />
                <meta name="exchangeCountry" content="US" />
                <meta name="exchangeIso" content="XNAS" />
                <meta name="priceCurrency" content="USD" />
                <meta name="price" content="$163.17" />
                <meta name="priceChange" content="0.81" />
                <meta name="priceChangePercent" content="0.50%" />
                <meta name="quoteTime" content="Mar 31, 2023 11:39 a.m. EDT" />
                <meta name="exchangeTimezone" content="(UTC-05:00) Eastern Time (US &amp; Canada)" />

        <meta name="description" content="AAPL | Complete Apple Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview." />
        <meta name="keywords" content="AAPL, AAPL analyst estimates, AAPL earnings estimates, AAPL share estimates, AAPL analyst recommendations, AAPL ratings, Apple Inc. analyst estimates, Apple Inc. earnings estimates, Apple Inc. analyst recommendations, Apple Inc. analyst ratings" />

        <meta property="og:title" content="AAPL Stock Price | Apple Inc. Stock Quote (U.S.: Nasdaq) | MarketWatch">
        <meta property="og:image" content="https://s.wsj.net/public/resources/MWimages/MW-EG169_articl_NS_20160223171404.png">

        <meta name="twitter:description" content="AAPL | Complete Apple Inc. stock news by MarketWatch. View real-time stock prices and stock quotes for a full financial overview.">
        <meta name="twitter:image" content="https://s.wsj.net/public/resources/MWimages/MW-EG169_articl_NS_20160223171404.png">

        <meta name="parsely-title" content="AAPL Stock Price | Apple Inc. Stock Quote (U.S.: Nasdaq) | MarketWatch">
        <meta name="parsely-type" content="post">
        <meta name="parsely-section" content="Quotes">

            <link rel="canonical" href="https://www.marketwatch.com/investing/stock/aapl" />
            <meta property="og:url" content="https://www.marketwatch.com/investing/stock/aapl">
            <meta name="parsely-link" content="https://www.marketwatch.com/investing/stock/aapl">
                    <link rel="stylesheet" type="text/css" href="https://sts3.wsj.net/bucket-a/maggie/static/css/quote-c163547364.min.css" />
                    <script>if(document.createElement("picture"),window.lazySizesConfig=window.lazySizesConfig||{},lazySizesConfig.loadMode=1,lazySizesConfig.throttle=600,window.addEventListener("load",(function(){lazySizesConfig.throttle=150})),
        /*! EnhanceJS: a progressive enhancement boilerplate. Copyright 2014 @scottjehl, Filament Group, Inc. Licensed MIT */
        function(e,t){"use strict";var n=e.setTimeout,a={},o=e.document,r=o.documentElement;o.head||o.getElementsByTagName("head")[0];a.loadJS=function(t,n){var a=e.document.getElementsByTagName("script")[0],o=e.document.createElement("script");return o.src=t,o.async=!0,n&&o.addEventListener("load",n),a.parentNode.insertBefore(o,a),o};var i=function(t,a,o){var r,i=e.document,d=i.createElement("link");if(a)r=a;else{var s=(i.body||i.getElementsByTagName("head")[0]).childNodes;r=s[s.length-1]}var l=i.styleSheets;d.rel="stylesheet",d.href=t,d.media="only x",function e(t){if(i.body)return t();n((function(){e(t)}))}((function(){r.parentNode.insertBefore(d,a?r:r.nextSibling)}));var c=function(e){for(var t=d.href,a=l.length;a--;)if(l[a].href===t)return e();n((function(){c(e)}))};function u(){d.addEventListener&&d.removeEventListener("load",u),d.media=o||"all"}return d.addEventListener&&d.addEventListener("load",u),d.onloadcssdefined=c,c(u),d};function d(t,n,a){var o;if(void 0===n){var r=("; "+e.document.cookie).split("; "+t+"=");return 2==r.length?r.pop().split(";").shift():null}if(!1===n&&(a=-1),a){var i=new Date;i.setTime(i.getTime()+24*a*60*60*1e3),o="; expires="+i.toGMTString()}else o="";e.document.cookie=t+"="+n+o+"; path=/; domain=.marketwatch.com"}function s(e){e.rel="stylesheet";var t=e.dataset.cookie,n=e.dataset.key;t&&n&&d(t,n,7)}"undefined"!=typeof exports?exports.loadCSS=i:e.loadCSS=i,a.loadCSS=i,a.getMeta=function(t){for(var n,a=e.document.getElementsByTagName("meta"),o=0;o<a.length;o++)if(a[o].name&&a[o].name===t){n=a[o];break}return n},a.cookie=d,e.loadedCss=s,a.loadedCss=s,"querySelector"in o&&(r.className+=" "+["enhanced"].join(" "),e.enhance=a)}(this),void 0===MarketWatch)var MarketWatch={};!function(){var e;function t(){try{var e=window.localStorage,t="__storage_test__";return e.setItem(t,t),e.removeItem(t),!0}catch(e){return!1}}MarketWatch.isStorageAvailable=function(){return void 0!==e?e:e=t()}}();</script>



        <script type="text/javascript">window.NREUM||(NREUM={});NREUM.info = {"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"cd2b77ba49","applicationID":"639647861","transactionName":"ZwEAbRQCWEVVVBYPVl5LM0wJF1MZXVkUA0pEDQxeSRBCWVdcTUw=","queueTime":0,"applicationTime":71,"agent":"","atts":""}</script><script type="text/javascript">(window.NREUM||(NREUM={})).init={privacy:{cookies_enabled:true},ajax:{deny_list:[]},distributed_tracing:{enabled:true}};(window.NREUM||(NREUM={})).loader_config={agentID:"753720625",accountID:"1684273",trustKey:"1022681",xpid:"VQAPVVRUCxAGV1hUAwYPUFU=",licenseKey:"cd2b77ba49",applicationID:"639647861"};;(()=>{var e,t,r={9071:(e,t,r)=>{"use strict";r.d(t,{I:()=>n});var n=0,i=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);i&&(n=+i[1])},6562:(e,t,r)=>{"use strict";r.d(t,{P_:()=>p,Mt:()=>v,C5:()=>f,DL:()=>y,OP:()=>R,lF:()=>L,Yu:()=>E,Dg:()=>g,CX:()=>d,GE:()=>w,sU:()=>k});var n={};r.r(n),r.d(n,{agent:()=>T,match:()=>S,version:()=>A});var i=r(6797),o=r(909),a=r(8610);class s{constructor(e,t){try{if(!e||"object"!=typeof e)return(0,a.Z)("New setting a Configurable requires an object as input");if(!t||"object"!=typeof t)return(0,a.Z)("Setting a Configurable requires a model to set its initial properties");Object.assign(this,t),Object.entries(e).forEach((e=>{let[t,r]=e;const n=(0,o.q)(t);n.length&&r&&"object"==typeof r&&n.forEach((e=>{e in r&&((0,a.Z)('"'.concat(e,'" is a protected attribute and can not be changed in feature ').concat(t,".  It will have no effect.")),delete r[e])})),this[t]=r}))}catch(e){(0,a.Z)("An error occured while setting a Configurable",e)}}}const c={beacon:i.ce.beacon,errorBeacon:i.ce.errorBeacon,licenseKey:void 0,applicationID:void 0,sa:void 0,queueTime:void 0,applicationTime:void 0,ttGuid:void 0,user:void 0,account:void 0,product:void 0,extra:void 0,jsAttributes:{},userAttributes:void 0,atts:void 0,transactionName:void 0,tNamePlain:void 0},u={};function f(e){if(!e)throw new Error("All info objects require an agent identifier!");if(!u[e])throw new Error("Info for ".concat(e," was never set"));return u[e]}function d(e,t){if(!e)throw new Error("All info objects require an agent identifier!");u[e]=new s(t,c),(0,i.Qy)(e,u[e],"info")}const l={allow_bfcache:!0,privacy:{cookies_enabled:!0},ajax:{deny_list:void 0,enabled:!0,harvestTimeSeconds:10},distributed_tracing:{enabled:void 0,exclude_newrelic_header:void 0,cors_use_newrelic_header:void 0,cors_use_tracecontext_headers:void 0,allowed_origins:void 0},ssl:void 0,obfuscate:void 0,jserrors:{enabled:!0,harvestTimeSeconds:10},metrics:{enabled:!0},page_action:{enabled:!0,harvestTimeSeconds:30},page_view_event:{enabled:!0},page_view_timing:{enabled:!0,harvestTimeSeconds:30,long_task:!1},session_trace:{enabled:!0,harvestTimeSeconds:10},spa:{enabled:!0,harvestTimeSeconds:10}},h={};function p(e){if(!e)throw new Error("All configuration objects require an agent identifier!");if(!h[e])throw new Error("Configuration for ".concat(e," was never set"));return h[e]}function g(e,t){if(!e)throw new Error("All configuration objects require an agent identifier!");h[e]=new s(t,l),(0,i.Qy)(e,h[e],"config")}function v(e,t){if(!e)throw new Error("All configuration objects require an agent identifier!");var r=p(e);if(r){for(var n=t.split("."),i=0;i<n.length-1;i++)if("object"!=typeof(r=r[n[i]]))return;r=r[n[n.length-1]]}return r}const m={accountID:void 0,trustKey:void 0,agentID:void 0,licenseKey:void 0,applicationID:void 0,xpid:void 0},b={};function y(e){if(!e)throw new Error("All loader-config objects require an agent identifier!");if(!b[e])throw new Error("LoaderConfig for ".concat(e," was never set"));return b[e]}function w(e,t){if(!e)throw new Error("All loader-config objects require an agent identifier!");b[e]=new s(t,m),(0,i.Qy)(e,b[e],"loader_config")}const E=(0,i.mF)().o;var T=null,A=null;if(navigator.userAgent){var x=navigator.userAgent,_=x.match(/Version\/(\S+)\s+Safari/);_&&-1===x.indexOf("Chrome")&&-1===x.indexOf("Chromium")&&(T="Safari",A=_[1])}function S(e,t){if(!T)return!1;if(e!==T)return!1;if(!t)return!0;if(!A)return!1;for(var r=A.split("."),n=t.split("."),i=0;i<n.length;i++)if(n[i]!==r[i])return!1;return!0}var O=r(5526),P=r(2374);const j="NRBA_SESSION_ID";function D(){if(!P.il)return null;try{let e;return null===(e=window.sessionStorage.getItem(j))&&(e=(0,O.ky)(16),window.sessionStorage.setItem(j,e)),e}catch(e){return null}}var N=r(8226);const C=e=>({customTransaction:void 0,disabled:!1,isolatedBacklog:!1,loaderType:void 0,maxBytes:3e4,offset:Math.floor(P._A?.performance?.timeOrigin||P._A?.performance?.timing?.navigationStart||Date.now()),onerror:void 0,origin:""+P._A.location,ptid:void 0,releaseIds:{},sessionId:1==v(e,"privacy.cookies_enabled")?D():null,xhrWrappable:"function"==typeof P._A.XMLHttpRequest?.prototype?.addEventListener,userAgent:n,version:N.q}),I={};function R(e){if(!e)throw new Error("All runtime objects require an agent identifier!");if(!I[e])throw new Error("Runtime for ".concat(e," was never set"));return I[e]}function k(e,t){if(!e)throw new Error("All runtime objects require an agent identifier!");I[e]=new s(t,C(e)),(0,i.Qy)(e,I[e],"runtime")}function L(e){return function(e){try{const t=f(e);return!!t.licenseKey&&!!t.errorBeacon&&!!t.applicationID}catch(e){return!1}}(e)}},8226:(e,t,r)=>{"use strict";r.d(t,{q:()=>n});const n="1228.PROD"},9557:(e,t,r)=>{"use strict";r.d(t,{w:()=>o});var n=r(8610);const i={agentIdentifier:""};class o{constructor(e){try{if("object"!=typeof e)return(0,n.Z)("shared context requires an object as input");this.sharedContext={},Object.assign(this.sharedContext,i),Object.entries(e).forEach((e=>{let[t,r]=e;Object.keys(i).includes(t)&&(this.sharedContext[t]=r)}))}catch(e){(0,n.Z)("An error occured while setting SharedContext",e)}}}},4329:(e,t,r)=>{"use strict";r.d(t,{L:()=>f,R:()=>c});var n=r(3752),i=r(7022),o=r(4045),a=r(2325);const s={};function c(e,t){const r={staged:!1,priority:a.p[t]||0};u(e),s[e].get(t)||s[e].set(t,r)}function u(e){e&&(s[e]||(s[e]=new Map))}function f(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"",t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"feature";if(u(e),!e||!s[e].get(t))return a(t);s[e].get(t).staged=!0;const r=Array.from(s[e]);function a(t){const r=e?n.ee.get(e):n.ee,a=o.X.handlers;if(r.backlog&&a){var s=r.backlog[t],c=a[t];if(c){for(var u=0;s&&u<s.length;++u)d(s[u],c);(0,i.D)(c,(function(e,t){(0,i.D)(t,(function(t,r){r[0].on(e,r[1])}))}))}delete a[t],r.backlog[t]=null,r.emit("drain-"+t,[])}}r.every((e=>{let[t,r]=e;return r.staged}))&&(r.sort(((e,t)=>e[1].priority-t[1].priority)),r.forEach((e=>{let[t]=e;a(t)})))}function d(e,t){var r=e[1];(0,i.D)(t[r],(function(t,r){var n=e[0];if(r[0]===n){var i=r[1],o=e[3],a=e[2];i.apply(o,a)}}))}},3752:(e,t,r)=>{"use strict";r.d(t,{c:()=>d,ee:()=>u});var n=r(6797),i=r(3916),o=r(7022),a=r(6562),s="nr@context";let c=(0,n.fP)();var u;function f(){}function d(e){return(0,i.X)(e,s,l)}function l(){return new f}function h(){u.aborted=!0,u.backlog={}}c.ee?u=c.ee:(u=function e(t,r){var n={},c={},d={},p=!1;try{p=16===r.length&&(0,a.OP)(r).isolatedBacklog}catch(e){}var g={on:b,addEventListener:b,removeEventListener:y,emit:m,get:E,listeners:w,context:v,buffer:T,abort:h,aborted:!1,isBuffering:A,debugId:r,backlog:p?{}:t&&"object"==typeof t.backlog?t.backlog:{}};return g;function v(e){return e&&e instanceof f?e:e?(0,i.X)(e,s,l):l()}function m(e,r,n,i,o){if(!1!==o&&(o=!0),!u.aborted||i){t&&o&&t.emit(e,r,n);for(var a=v(n),s=w(e),f=s.length,d=0;d<f;d++)s[d].apply(a,r);var l=x()[c[e]];return l&&l.push([g,e,r,a]),a}}function b(e,t){n[e]=w(e).concat(t)}function y(e,t){var r=n[e];if(r)for(var i=0;i<r.length;i++)r[i]===t&&r.splice(i,1)}function w(e){return n[e]||[]}function E(t){return d[t]=d[t]||e(g,t)}function T(e,t){var r=x();g.aborted||(0,o.D)(e,(function(e,n){t=t||"feature",c[n]=t,t in r||(r[t]=[])}))}function A(e){return!!x()[c[e]]}function x(){return g.backlog}}(void 0,"globalEE"),c.ee=u)},9252:(e,t,r)=>{"use strict";r.d(t,{E:()=>n,p:()=>i});var n=r(3752).ee.get("handle");function i(e,t,r,i,o){o?(o.buffer([e],i),o.emit(e,t,r)):(n.buffer([e],i),n.emit(e,t,r))}},4045:(e,t,r)=>{"use strict";r.d(t,{X:()=>o});var n=r(9252);o.on=a;var i=o.handlers={};function o(e,t,r,o){a(o||n.E,i,e,t,r)}function a(e,t,r,i,o){o||(o="feature"),e||(e=n.E);var a=t[o]=t[o]||{};(a[r]=a[r]||[]).push([e,i])}},8544:(e,t,r)=>{"use strict";r.d(t,{bP:()=>s,iz:()=>c,m$:()=>a});var n=r(2374);let i=!1,o=!1;try{const e={get passive(){return i=!0,!1},get signal(){return o=!0,!1}};n._A.addEventListener("test",null,e),n._A.removeEventListener("test",null,e)}catch(e){}function a(e,t){return i||o?{capture:!!e,passive:i,signal:t}:!!e}function s(e,t){let r=arguments.length>2&&void 0!==arguments[2]&&arguments[2];window.addEventListener(e,t,a(r))}function c(e,t){let r=arguments.length>2&&void 0!==arguments[2]&&arguments[2];document.addEventListener(e,t,a(r))}},5526:(e,t,r)=>{"use strict";r.d(t,{Ht:()=>a,M:()=>o,Rl:()=>i,ky:()=>s});var n=r(2374);function i(){var e=null,t=0,r=n._A?.crypto||n._A?.msCrypto;function i(){return e?15&e[t++]:16*Math.random()|0}r&&r.getRandomValues&&(e=r.getRandomValues(new Uint8Array(31)));for(var o,a="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx",s="",c=0;c<a.length;c++)s+="x"===(o=a[c])?i().toString(16):"y"===o?(o=3&i()|8).toString(16):o;return s}function o(){return s(16)}function a(){return s(32)}function s(e){var t=null,r=0,n=self.crypto||self.msCrypto;n&&n.getRandomValues&&Uint8Array&&(t=n.getRandomValues(new Uint8Array(31)));for(var i=[],o=0;o<e;o++)i.push(a().toString(16));return i.join("");function a(){return t?15&t[r++]:16*Math.random()|0}}},2053:(e,t,r)=>{"use strict";r.d(t,{B:()=>n,z:()=>i});const n=(new Date).getTime();function i(){return Math.round(performance.now())}},8283:(e,t,r)=>{"use strict";r.d(t,{B:()=>a,L:()=>s});var n=r(6562),i=r(2053),o={};function a(e,t,r){void 0===r&&(r=(0,i.z)()+(0,n.OP)(e).offset),o[e]=o[e]||{},o[e][t]=r}function s(e,t,r,n){const i=e.sharedContext.agentIdentifier;var a=o[i]?.[r],s=o[i]?.[n];void 0!==a&&void 0!==s&&e.store("measures",t,{value:s-a})}},2545:(e,t,r)=>{"use strict";r.d(t,{L:()=>c});var n=r(9071),i=r(8544),o=r(8305),a=r(2374),s=r(6998);if(a.v6){a._A.cleanupTasks=[];const e=a._A.close;a._A.close=()=>{for(let e of a._A.cleanupTasks)e();e()}}function c(e,t){if(a.il)if(t)(0,s.N)(e,!0),(0,i.bP)("pagehide",e);else{var r=(0,o.Z)(e);!n.I||navigator.sendBeacon?(0,i.bP)("pagehide",r):(0,i.bP)("beforeunload",r),(0,i.bP)("unload",r)}else a.v6&&a._A.cleanupTasks.push(e)}},6368:(e,t,r)=>{"use strict";r.d(t,{e:()=>o});var n=r(2374),i={};function o(e){if(e in i)return i[e];if(0===(e||"").indexOf("data:"))return{protocol:"data"};let t;var r=n._A?.location,o={};if(n.il)t=document.createElement("a"),t.href=e;else try{t=new URL(e,r.href)}catch(e){return o}o.port=t.port;var a=t.href.split("://");!o.port&&a[1]&&(o.port=a[1].split("/")[0].split("@").pop().split(":")[1]),o.port&&"0"!==o.port||(o.port="https"===a[0]?"443":"80"),o.hostname=t.hostname||r.hostname,o.pathname=t.pathname,o.protocol=a[0],"/"!==o.pathname.charAt(0)&&(o.pathname="/"+o.pathname);var s=!t.protocol||":"===t.protocol||t.protocol===r.protocol,c=t.hostname===r.hostname&&t.port===r.port;return o.sameOrigin=s&&(!t.hostname||c),"/"===o.pathname&&(i[e]=o),o}},8610:(e,t,r)=>{"use strict";function n(e,t){console&&console.warn&&"function"==typeof console.warn&&(console.warn("New Relic: ".concat(e)),t&&console.warn(t))}r.d(t,{Z:()=>n})},3916:(e,t,r)=>{"use strict";r.d(t,{X:()=>i});var n=Object.prototype.hasOwnProperty;function i(e,t,r){if(n.call(e,t))return e[t];var i=r();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:i,writable:!0,enumerable:!1}),i}catch(e){}return e[t]=i,i}},2374:(e,t,r)=>{"use strict";r.d(t,{_A:()=>o,il:()=>n,lW:()=>a,v6:()=>i});const n=Boolean("undefined"!=typeof window&&window.document),i=Boolean("undefined"!=typeof WorkerGlobalScope&&self.navigator instanceof WorkerNavigator);let o=(()=>{if(n)return window;if(i){if("undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope)return globalThis;if(self instanceof WorkerGlobalScope)return self}throw new Error('New Relic browser agent shutting down due to error: Unable to locate global scope. This is possibly due to code redefining browser global variables like "self" and "window".')})();function a(){return o}},7022:(e,t,r)=>{"use strict";r.d(t,{D:()=>i});var n=Object.prototype.hasOwnProperty;function i(e,t){var r=[],i="",o=0;for(i in e)n.call(e,i)&&(r[o]=t(i,e[i]),o+=1);return r}},8305:(e,t,r)=>{"use strict";r.d(t,{Z:()=>o});var n=r(8683),i=r.n(n);function o(e){var t,r=!1;return function(){return r?t:(r=!0,t=e.apply(this,i()(arguments)))}}},2438:(e,t,r)=>{"use strict";r.d(t,{P:()=>o});var n=r(3752);const i=()=>{const e=new WeakSet;return(t,r)=>{if("object"==typeof r&&null!==r){if(e.has(r))return;e.add(r)}return r}};function o(e){try{return JSON.stringify(e,i())}catch(e){try{n.ee.emit("internal-error",[e])}catch(e){}}}},2650:(e,t,r)=>{"use strict";r.d(t,{K:()=>a,b:()=>o});var n=r(8544);function i(){return"undefined"==typeof document||"complete"===document.readyState}function o(e,t){if(i())return e();(0,n.bP)("load",e,t)}function a(e){if(i())return e();(0,n.iz)("DOMContentLoaded",e)}},6797:(e,t,r)=>{"use strict";r.d(t,{EZ:()=>u,Qy:()=>c,ce:()=>o,fP:()=>a,gG:()=>f,mF:()=>s});var n=r(2053),i=r(2374);const o={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net"};function a(){return i._A.NREUM||(i._A.NREUM={}),void 0===i._A.newrelic&&(i._A.newrelic=i._A.NREUM),i._A.NREUM}function s(){let e=a();return e.o||(e.o={ST:i._A.setTimeout,SI:i._A.setImmediate,CT:i._A.clearTimeout,XHR:i._A.XMLHttpRequest,REQ:i._A.Request,EV:i._A.Event,PR:i._A.Promise,MO:i._A.MutationObserver,FETCH:i._A.fetch}),e}function c(e,t,r){let i=a();const o=i.initializedAgents||{},s=o[e]||{};return Object.keys(s).length||(s.initializedAt={ms:(0,n.z)(),date:new Date}),i.initializedAgents={...o,[e]:{...s,[r]:t}},i}function u(e,t){a()[e]=t}function f(){return function(){let e=a();const t=e.info||{};e.info={beacon:o.beacon,errorBeacon:o.errorBeacon,...t}}(),function(){let e=a();const t=e.init||{};e.init={...t}}(),s(),function(){let e=a();const t=e.loader_config||{};e.loader_config={...t}}(),a()}},6998:(e,t,r)=>{"use strict";r.d(t,{N:()=>i,e:()=>o});var n=r(8544);function i(e){let t=arguments.length>1&&void 0!==arguments[1]&&arguments[1];return void(0,n.iz)("visibilitychange",(function(){if(t){if("hidden"!=document.visibilityState)return;e()}e(document.visibilityState)}))}function o(){return"hidden"===document.visibilityState?-1:1/0}},6408:(e,t,r)=>{"use strict";r.d(t,{W:()=>i});var n=r(2374);function i(){return"function"==typeof n._A?.PerformanceObserver}},8675:(e,t,r)=>{"use strict";r.d(t,{t:()=>n});const n=r(2325).D.ajax},8322:(e,t,r)=>{"use strict";r.d(t,{A:()=>i,t:()=>n});const n=r(2325).D.jserrors,i="nr@seenError"},6034:(e,t,r)=>{"use strict";r.d(t,{gF:()=>o,mY:()=>i,t9:()=>n,vz:()=>s,xS:()=>a});const n=r(2325).D.metrics,i="sm",o="cm",a="storeSupportabilityMetrics",s="storeEventMetrics"},6486:(e,t,r)=>{"use strict";r.d(t,{t:()=>n});const n=r(2325).D.pageAction},2484:(e,t,r)=>{"use strict";r.d(t,{t:()=>n});const n=r(2325).D.pageViewEvent},6382:(e,t,r)=>{"use strict";r.d(t,{t:()=>n});const n=r(2325).D.pageViewTiming},2628:(e,t,r)=>{"use strict";r.r(t),r.d(t,{ADD_EVENT_LISTENER:()=>g,BST_RESOURCE:()=>a,BST_TIMER:()=>l,END:()=>u,FEATURE_NAME:()=>i,FN_END:()=>d,FN_START:()=>f,ORIG_EVENT:()=>p,PUSH_STATE:()=>h,RESOURCE:()=>s,RESOURCE_TIMING_BUFFER_FULL:()=>o,START:()=>c});var n=r(6562);const i=r(2325).D.sessionTrace,o="resourcetimingbufferfull",a="bstResource",s="resource",c="-start",u="-end",f="fn"+c,d="fn"+u,l="bstTimer",h="pushState",p=n.Yu.EV,g="addEventListener"},755:(e,t,r)=>{"use strict";r.r(t),r.d(t,{BODY:()=>T,CB_END:()=>A,CB_START:()=>u,END:()=>E,FEATURE_NAME:()=>i,FETCH:()=>_,FETCH_BODY:()=>m,FETCH_DONE:()=>v,FETCH_START:()=>g,FN_END:()=>c,FN_START:()=>s,INTERACTION:()=>l,INTERACTION_API:()=>f,INTERACTION_EVENTS:()=>o,JSONP_END:()=>b,JSONP_NODE:()=>p,JS_TIME:()=>x,MAX_TIMER_BUDGET:()=>a,REMAINING:()=>d,SPA_NODE:()=>h,START:()=>w,originalSetTimeout:()=>y});var n=r(6562);r(2374);const i=r(2325).D.spa,o=["click","submit","keypress","keydown","keyup","change"],a=999,s="fn-start",c="fn-end",u="cb-start",f="api-ixn-",d="remaining",l="interaction",h="spaNode",p="jsonpNode",g="fetch-start",v="fetch-done",m="fetch-body-",b="jsonp-end",y=n.Yu.ST,w="-start",E="-end",T="-body",A="cb"+E,x="jsTime",_="fetch"},1509:(e,t,r)=>{"use strict";r.d(t,{W:()=>s});var n=r(6562),i=r(3752),o=r(2384),a=r(6797);class s{constructor(e,t,r){this.agentIdentifier=e,this.aggregator=t,this.ee=i.ee.get(e,(0,n.OP)(this.agentIdentifier).isolatedBacklog),this.featureName=r,this.blocked=!1,this.checkConfiguration()}checkConfiguration(){if(!(0,n.lF)(this.agentIdentifier)){let e={...(0,a.gG)().info?.jsAttributes};try{e={...e,...(0,n.C5)(this.agentIdentifier)?.jsAttributes}}catch(e){}(0,o.j)(this.agentIdentifier,{...(0,a.gG)(),info:{...(0,a.gG)().info,jsAttributes:e}})}}}},2384:(e,t,r)=>{"use strict";r.d(t,{j:()=>w});var n=r(8683),i=r.n(n),o=r(2325),a=r(6562),s=r(9252),c=r(7022),u=r(3752),f=r(2053),d=r(4329),l=r(2650),h=r(2374),p=r(8610),g=r(6034);function v(e){["setErrorHandler","finished","addToTrace","inlineHit","addRelease","addPageAction","setCurrentRouteName","setPageViewName","setCustomAttribute","interaction","noticeError"].forEach((t=>{e[t]=function(){for(var r=arguments.length,n=new Array(r),i=0;i<r;i++)n[i]=arguments[i];return function(t){for(var r=arguments.length,n=new Array(r>1?r-1:0),i=1;i<r;i++)n[i-1]=arguments[i];Object.values(e.initializedAgents).forEach((e=>{e.exposed&&e.api[t]&&e.api[t](...n)}))}(t,...n)}}))}var m=r(6797);const b={stn:[o.D.sessionTrace],err:[o.D.jserrors,o.D.metrics],ins:[o.D.pageAction],spa:[o.D.spa]};const y={};function w(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},n=arguments.length>2?arguments[2]:void 0,w=arguments.length>3?arguments[3]:void 0,{init:E,info:T,loader_config:A,runtime:x={loaderType:n},exposed:_=!0}=t;const S=(0,m.gG)();let O={};return T||(E=S.init,T=S.info,A=S.loader_config,O=S),h.v6&&(T.jsAttributes={...T.jsAttributes,isWorker:!0}),(0,a.CX)(e,T),(0,a.Dg)(e,E||{}),(0,a.GE)(e,A||{}),(0,a.sU)(e,x),function(e,t,n){n||(0,d.R)(e,"api"),v(t);var m=u.ee.get(e),b=m.get("tracer"),y="api-",w=y+"ixn-";function E(){}(0,c.D)(["setErrorHandler","finished","addToTrace","inlineHit","addRelease"],(function(e,r){t[r]=A(y,r,!0,"api")})),t.addPageAction=A(y,"addPageAction",!0,o.D.pageAction),t.setCurrentRouteName=A(y,"routeName",!0,o.D.spa),t.setPageViewName=function(t,r){if("string"==typeof t)return"/"!==t.charAt(0)&&(t="/"+t),(0,a.OP)(e).customTransaction=(r||"http://custom.transaction")+t,A(y,"setPageViewName",!0,"api")()},t.setCustomAttribute=function(t,r){const n=(0,a.C5)(e);return(0,a.CX)(e,{...n,jsAttributes:{...n.jsAttributes,[t]:r}}),A(y,"setCustomAttribute",!0,"api")()},t.interaction=function(){return(new E).get()};var T=E.prototype={createTracer:function(e,t){var r={},n=this,i="function"==typeof t;return(0,s.p)(w+"tracer",[(0,f.z)(),e,r],n,o.D.spa,m),function(){if(b.emit((i?"":"no-")+"fn-start",[(0,f.z)(),n,i],r),i)try{return t.apply(this,arguments)}catch(e){throw b.emit("fn-err",[arguments,this,"string"==typeof e?new Error(e):e],r),e}finally{b.emit("fn-end",[(0,f.z)()],r)}}}};function A(e,t,r,n){return function(){return(0,s.p)(g.xS,["API/"+t+"/called"],void 0,o.D.metrics,m),(0,s.p)(e+t,[(0,f.z)()].concat(i()(arguments)),r?null:this,n,m),r?void 0:this}}function x(){r.e(439).then(r.bind(r,5692)).then((t=>{let{setAPI:r}=t;r(e),(0,d.L)(e,"api")})).catch((()=>(0,p.Z)("Downloading runtime APIs failed...")))}(0,c.D)("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),(function(e,t){T[t]=A(w,t,void 0,o.D.spa)})),t.noticeError=function(e,t){"string"==typeof e&&(e=new Error(e)),(0,s.p)(g.xS,["API/noticeError/called"],void 0,o.D.metrics,m),(0,s.p)("err",[e,(0,f.z)(),!1,t],void 0,o.D.jserrors,m)},h.v6?x():(0,l.b)((()=>x()),!0)}(e,O,w),(0,m.Qy)(e,S,"api"),(0,m.Qy)(e,_,"exposed"),(0,m.EZ)("activatedFeatures",y),(0,m.EZ)("setToken",(t=>function(e,t){var r=u.ee.get(t);e&&"object"==typeof e&&((0,c.D)(e,(function(e,t){if(!t)return(b[e]||[]).forEach((t=>{(0,s.p)("block-"+e,[],void 0,t,r)}));y[e]||((0,s.p)("feat-"+e,[],void 0,b[e],r),y[e]=!0)})),(0,d.L)(t,o.D.pageViewEvent))}(t,e))),O}},909:(e,t,r)=>{"use strict";r.d(t,{Z:()=>i,q:()=>o});var n=r(2325);function i(e){switch(e){case n.D.ajax:return[n.D.jserrors];case n.D.sessionTrace:return[n.D.ajax,n.D.pageViewEvent];case n.D.pageViewTiming:return[n.D.pageViewEvent];default:return[]}}function o(e){return e===n.D.jserrors?[]:["auto"]}},2325:(e,t,r)=>{"use strict";r.d(t,{D:()=>n,p:()=>i});const n={ajax:"ajax",jserrors:"jserrors",metrics:"metrics",pageAction:"page_action",pageViewEvent:"page_view_event",pageViewTiming:"page_view_timing",sessionTrace:"session_trace",spa:"spa"},i={[n.pageViewEvent]:1,[n.pageViewTiming]:2,[n.metrics]:3,[n.jserrors]:4,[n.ajax]:5,[n.sessionTrace]:6,[n.pageAction]:7,[n.spa]:8}},8683:e=>{e.exports=function(e,t,r){t||(t=0),void 0===r&&(r=e?e.length:0);for(var n=-1,i=r-t||0,o=Array(i<0?0:i);++n<i;)o[n]=e[t+n];return o}}},n={};function i(e){var t=n[e];if(void 0!==t)return t.exports;var o=n[e]={exports:{}};return r[e](o,o.exports,i),o.exports}i.m=r,i.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return i.d(t,{a:t}),t},i.d=(e,t)=>{for(var r in t)i.o(t,r)&&!i.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},i.f={},i.e=e=>Promise.all(Object.keys(i.f).reduce(((t,r)=>(i.f[r](e,t),t)),[])),i.u=e=>(({78:"page_action-aggregate",147:"metrics-aggregate",193:"session_trace-aggregate",317:"jserrors-aggregate",348:"page_view_timing-aggregate",439:"async-api",729:"lazy-loader",786:"page_view_event-aggregate",873:"spa-aggregate",898:"ajax-aggregate"}[e]||e)+"."+{78:"1ef08094",147:"56d9a464",193:"ada8b15b",317:"64f61365",348:"ced8c919",439:"61caf4d9",729:"37550b27",786:"46b69e61",862:"e74e95d2",873:"7222cbb6",898:"e6085a9a"}[e]+"-1228.min.js"),i.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),e={},t="NRBA:",i.l=(r,n,o,a)=>{if(e[r])e[r].push(n);else{var s,c;if(void 0!==o)for(var u=document.getElementsByTagName("script"),f=0;f<u.length;f++){var d=u[f];if(d.getAttribute("src")==r||d.getAttribute("data-webpack")==t+o){s=d;break}}s||(c=!0,(s=document.createElement("script")).charset="utf-8",s.timeout=120,i.nc&&s.setAttribute("nonce",i.nc),s.setAttribute("data-webpack",t+o),s.src=r),e[r]=[n];var l=(t,n)=>{s.onerror=s.onload=null,clearTimeout(h);var i=e[r];if(delete e[r],s.parentNode&&s.parentNode.removeChild(s),i&&i.forEach((e=>e(n))),t)return t(n)},h=setTimeout(l.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=l.bind(null,s.onerror),s.onload=l.bind(null,s.onload),c&&document.head.appendChild(s)}},i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.p="https://js-agent.newrelic.com/",(()=>{var e={771:0,338:0};i.f.j=(t,r)=>{var n=i.o(e,t)?e[t]:void 0;if(0!==n)if(n)r.push(n[2]);else{var o=new Promise(((r,i)=>n=e[t]=[r,i]));r.push(n[2]=o);var a=i.p+i.u(t),s=new Error;i.l(a,(r=>{if(i.o(e,t)&&(0!==(n=e[t])&&(e[t]=void 0),n)){var o=r&&("load"===r.type?"missing":r.type),a=r&&r.target&&r.target.src;s.message="Loading chunk "+t+" failed.\n("+o+": "+a+")",s.name="ChunkLoadError",s.type=o,s.request=a,n[1](s)}}),"chunk-"+t,t)}};var t=(t,r)=>{var n,o,[a,s,c]=r,u=0;if(a.some((t=>0!==e[t]))){for(n in s)i.o(s,n)&&(i.m[n]=s[n]);if(c)c(i)}for(t&&t(r);u<a.length;u++)o=a[u],i.o(e,o)&&e[o]&&e[o][0](),e[o]=0},r=window.webpackChunkNRBA=window.webpackChunkNRBA||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})();var o={};(()=>{"use strict";i.r(o);var e=i(2325),t=i(6562);const r=Object.values(e.D);function n(e){const n={};return r.forEach((r=>{n[r]=function(e,r){return!1!==(0,t.Mt)(r,"".concat(e,".enabled"))}(r,e)})),n}var a=i(2384),s=i(909),c=i(9252),u=i(2053),f=i(8283),d=i(4329),l=i(1509),h=i(2650),p=i(2374),g=i(8610);class v extends l.W{constructor(e,t,r){let n=!(arguments.length>3&&void 0!==arguments[3])||arguments[3];super(e,t,r),this.hasAggregator=!1,this.auto=n,this.abortHandler,n&&(0,d.R)(e,r)}importAggregator(){if(this.hasAggregator||!this.auto)return;this.hasAggregator=!0;const e=async()=>{try{const{lazyLoader:e}=await i.e(729).then(i.bind(i,8110)),{Aggregate:t}=await e(this.featureName,"aggregate");new t(this.agentIdentifier,this.aggregator)}catch(e){(0,g.Z)("Downloading ".concat(this.featureName," failed...")),this.abortHandler?.()}};p.v6?e():(0,h.b)((()=>e()),!0)}}var m,b,y,w=i(2484);class E extends v{constructor(e,r){let n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(e,r,w.t,n),(0,f.B)(e,"starttime",(0,t.OP)(e).offset),(0,f.B)(e,"firstbyte",u.B),(0,h.K)((()=>this.measureDomContentLoaded())),(0,h.b)((()=>this.measureWindowLoaded()),!0),this.importAggregator()}measureWindowLoaded(){var r=(0,u.z)();(0,f.B)(this.agentIdentifier,"onload",r+(0,t.OP)(this.agentIdentifier).offset),(0,c.p)("timing",["load",r],void 0,e.D.pageViewTiming,this.ee)}measureDomContentLoaded(){(0,f.B)(this.agentIdentifier,"domContent",(0,u.z)()+(0,t.OP)(this.agentIdentifier).offset)}}m=E,b="featureName",y=w.t,(b=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(b))in m?Object.defineProperty(m,b,{value:y,enumerable:!0,configurable:!0,writable:!0}):m[b]=y;var T=i(9557),A=i(7022);class x extends T.w{constructor(e){super(e),this.aggregatedData={}}store(e,t,r,n,i){var o=this.getBucket(e,t,r,i);return o.metrics=function(e,t){t||(t={count:0});return t.count+=1,(0,A.D)(e,(function(e,r){t[e]=_(r,t[e])})),t}(n,o.metrics),o}merge(e,t,r,n,i){var o=this.getBucket(e,t,n,i);if(o.metrics){var a=o.metrics;a.count+=r.count,(0,A.D)(r,(function(e,t){if("count"!==e){var n=a[e],i=r[e];i&&!i.c?a[e]=_(i.t,n):a[e]=function(e,t){if(!t)return e;t.c||(t=S(t.t));return t.min=Math.min(e.min,t.min),t.max=Math.max(e.max,t.max),t.t+=e.t,t.sos+=e.sos,t.c+=e.c,t}(i,a[e])}}))}else o.metrics=r}storeMetric(e,t,r,n){var i=this.getBucket(e,t,r);return i.stats=_(n,i.stats),i}getBucket(e,t,r,n){this.aggregatedData[e]||(this.aggregatedData[e]={});var i=this.aggregatedData[e][t];return i||(i=this.aggregatedData[e][t]={params:r||{}},n&&(i.custom=n)),i}get(e,t){return t?this.aggregatedData[e]&&this.aggregatedData[e][t]:this.aggregatedData[e]}take(e){for(var t={},r="",n=!1,i=0;i<e.length;i++)t[r=e[i]]=O(this.aggregatedData[r]),t[r].length&&(n=!0),delete this.aggregatedData[r];return n?t:null}}function _(e,t){return null==e?function(e){e?e.c++:e={c:1};return e}(t):t?(t.c||(t=S(t.t)),t.c+=1,t.t+=e,t.sos+=e*e,e>t.max&&(t.max=e),e<t.min&&(t.min=e),t):{t:e}}function S(e){return{t:e,min:e,max:e,sos:e*e,c:1}}function O(e){return"object"!=typeof e?[]:(0,A.D)(e,P)}function P(e,t){return t}var j=i(6797),D=i(5526),N=i(2438);var C,I=i(6998),R=i(8544),k=i(6382),L=-1,H=function(e){addEventListener("pageshow",(function(t){t.persisted&&(L=t.timeStamp,e(t))}),!0)},z=function(){return window.performance&&performance.getEntriesByType&&performance.getEntriesByType("navigation")[0]},M=function(){var e=z();return e&&e.activationStart||0},B=function(e,t){var r=z(),n="navigate";return L>=0?n="back-forward-cache":r&&(n=document.prerendering||M()>0?"prerender":document.wasDiscarded?"restore":r.type.replace(/_/g,"-")),{name:e,value:void 0===t?-1:t,rating:"good",delta:0,entries:[],id:"v3-".concat(Date.now(),"-").concat(Math.floor(8999999999999*Math.random())+1e12),navigationType:n}},F=function(e,t,r){try{if(PerformanceObserver.supportedEntryTypes.includes(e)){var n=new PerformanceObserver((function(e){Promise.resolve().then((function(){t(e.getEntries())}))}));return n.observe(Object.assign({type:e,buffered:!0},r||{})),n}}catch(e){}},U=function(e,t,r,n){var i,o;return function(a){t.value>=0&&(a||n)&&((o=t.value-(i||0))||void 0===i)&&(i=t.value,t.delta=o,t.rating=function(e,t){return e>t[1]?"poor":e>t[0]?"needs-improvement":"good"}(t.value,r),e(t))}},V=function(e){var t=function(t){"pagehide"!==t.type&&"hidden"!==document.visibilityState||e(t)};addEventListener("visibilitychange",t,!0),addEventListener("pagehide",t,!0)},W=function(e){document.prerendering?addEventListener("prerenderingchange",(function(){return e()}),!0):e()},q=(new Date,0),G=1/0,X=0,$=function(e){e.forEach((function(e){e.interactionId&&(G=Math.min(G,e.interactionId),X=Math.max(X,e.interactionId),q=X?(X-G)/7+1:0)}))},Z=function(){return C?q:performance.interactionCount||0},Y=function(){"interactionCount"in performance||C||(C=F("event",$,{type:"event",buffered:!0,durationThreshold:0}))},Q=[200,500],K=0,J=function(){return Z()-K},ee=[],te={},re=function(e){var t=ee[ee.length-1],r=te[e.interactionId];if(r||ee.length<10||e.duration>t.latency){if(r)r.entries.push(e),r.latency=Math.max(r.latency,e.duration);else{var n={id:e.interactionId,latency:e.duration,entries:[e]};te[n.id]=n,ee.push(n)}ee.sort((function(e,t){return t.latency-e.latency})),ee.splice(10).forEach((function(e){delete te[e.id]}))}},ne=i(2545);class ie extends v{constructor(r,n){var i;let o=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];if(super(r,n,k.t,o),i=this,p.il){if(this.pageHiddenTime=(0,I.e)(),this.performanceObserver,this.lcpPerformanceObserver,this.clsPerformanceObserver,this.fiRecorded=!1,"PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){this.performanceObserver=new PerformanceObserver((function(){return i.perfObserver(...arguments)}));try{this.performanceObserver.observe({entryTypes:["paint"]})}catch(e){}this.lcpPerformanceObserver=new PerformanceObserver((function(){return i.lcpObserver(...arguments)}));try{this.lcpPerformanceObserver.observe({entryTypes:["largest-contentful-paint"]})}catch(e){}this.clsPerformanceObserver=new PerformanceObserver((function(){return i.clsObserver(...arguments)}));try{this.clsPerformanceObserver.observe({type:"layout-shift",buffered:!0})}catch(e){}}this.fiRecorded=!1;["click","keydown","mousedown","pointerdown","touchstart"].forEach((e=>{(0,R.iz)(e,(function(){return i.captureInteraction(...arguments)}))})),function(e,t){t=t||{},W((function(){Y();var r,n=B("INP"),i=function(e){e.forEach((function(e){e.interactionId&&re(e),"first-input"===e.entryType&&!ee.some((function(t){return t.entries.some((function(t){return e.duration===t.duration&&e.startTime===t.startTime}))}))&&re(e)}));var t,i=(t=Math.min(ee.length-1,Math.floor(J()/50)),ee[t]);i&&i.latency!==n.value&&(n.value=i.latency,n.entries=i.entries,r())},o=F("event",i,{durationThreshold:t.durationThreshold||40});r=U(e,n,Q,t.reportAllChanges),o&&(o.observe({type:"first-input",buffered:!0}),V((function(){i(o.takeRecords()),n.value<0&&J()>0&&(n.value=0,n.entries=[]),r(!0)})),H((function(){ee=[],K=Z(),n=B("INP"),r=U(e,n,Q,t.reportAllChanges)})))}))}((t=>{let{name:r,value:n,id:i}=t;(0,c.p)("timing",[r.toLowerCase(),n,{metricId:i}],void 0,e.D.pageViewTiming,this.ee)})),!0===(0,t.Mt)(this.agentIdentifier,"page_view_timing.long_task")&&(e=>{const t=t=>{t.forEach((t=>{const r={name:"LT",value:t.duration,info:{ltFrame:t.name,ltStart:t.startTime,ltCtr:t.attribution[0].containerType}};"window"!==r.info.ltCtr&&Object.assign(r.info,{ltCtrSrc:t.attribution[0].containerSrc,ltCtrId:t.attribution[0].containerId,ltCtrName:t.attribution[0].containerName}),e(r)}))};let r;try{PerformanceObserver.supportedEntryTypes.includes("longtask")&&(r=new PerformanceObserver((e=>{Promise.resolve().then((()=>{t(e.getEntries())}))})),r.observe({type:"longtask",buffered:!0}))}catch(e){}r&&(0,ne.L)((()=>{t(r.takeRecords())}),!0)})((t=>{let{name:r,value:n,info:i}=t;(0,c.p)("timing",[r.toLowerCase(),n,i],void 0,e.D.pageViewTiming,this.ee)})),(0,I.N)((()=>{this.pageHiddenTime=(0,u.z)(),(0,c.p)("docHidden",[this.pageHiddenTime],void 0,e.D.pageViewTiming,this.ee)}),!0),(0,R.bP)("pagehide",(()=>(0,c.p)("winPagehide",[(0,u.z)()],void 0,e.D.pageViewTiming,this.ee))),this.importAggregator()}}perfObserver(t,r){t.getEntries().forEach((t=>{"first-paint"===t.name?(0,c.p)("timing",["fp",Math.floor(t.startTime)],void 0,e.D.pageViewTiming,this.ee):"first-contentful-paint"===t.name&&(0,c.p)("timing",["fcp",Math.floor(t.startTime)],void 0,e.D.pageViewTiming,this.ee)}))}lcpObserver(t,r){var n=t.getEntries();if(n.length>0){var i=n[n.length-1];if(this.pageHiddenTime<i.startTime)return;var o=[i],a=this.addConnectionAttributes({});a&&o.push(a),(0,c.p)("lcp",o,void 0,e.D.pageViewTiming,this.ee)}}clsObserver(t){t.getEntries().forEach((t=>{t.hadRecentInput||(0,c.p)("cls",[t],void 0,e.D.pageViewTiming,this.ee)}))}addConnectionAttributes(e){var t=navigator.connection||navigator.mozConnection||navigator.webkitConnection;if(t)return t.type&&(e["net-type"]=t.type),t.effectiveType&&(e["net-etype"]=t.effectiveType),t.rtt&&(e["net-rtt"]=t.rtt),t.downlink&&(e["net-dlink"]=t.downlink),e}captureInteraction(r){if(r instanceof t.Yu.EV&&!this.fiRecorded){var n=Math.round(r.timeStamp),i={type:r.type};this.addConnectionAttributes(i);const o=(0,t.OP)(this.agentIdentifier).offset;n<=(0,u.z)()?i.fid=(0,u.z)()-n:n>o&&n<=Date.now()?(n-=o,i.fid=(0,u.z)()-n):n=(0,u.z)(),this.fiRecorded=!0,(0,c.p)("timing",["fi",n,i],void 0,e.D.pageViewTiming,this.ee)}}}!function(e,t,r){(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r}(ie,"featureName",k.t);const oe={dedicated:Boolean(p._A?.Worker),shared:Boolean(p._A?.SharedWorker),service:Boolean(p._A?.navigator?.serviceWorker)};let ae,se,ce;var ue=i(6034);class fe extends v{constructor(t,r){let n=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(t,r,ue.t9,n),function(e){if(!ae){if(oe.dedicated){ae=Worker;try{p._A.Worker=r(ae,"Dedicated")}catch(e){o(e,"Dedicated")}if(oe.shared){se=SharedWorker;try{p._A.SharedWorker=r(se,"Shared")}catch(e){o(e,"Shared")}}else n("Shared");if(oe.service){ce=navigator.serviceWorker.register;try{p._A.navigator.serviceWorker.register=(t=ce,function(){for(var e=arguments.length,r=new Array(e),n=0;n<e;n++)r[n]=arguments[n];return i("Service",r[1]?.type),t.apply(navigator.serviceWorker,r)})}catch(e){o(e,"Service")}}else n("Service");var t;return}n("All")}function r(e,t){return"undefined"==typeof Proxy?e:new Proxy(e,{construct:(e,r)=>(i(t,r[1]?.type),new e(...r))})}function n(t){p.v6||e("Workers/".concat(t,"/Unavailable"))}function i(t,r){e("Workers/".concat(t,"module"===r?"/Module":"/Classic"))}function o(t,r){e("Workers/".concat(r,"/SM/Unsupported")),(0,g.Z)("NR Agent: Unable to capture ".concat(r," workers."),t)}}((t=>(0,c.p)(ue.xS,[t],void 0,e.D.metrics,this.ee))),this.importAggregator()}}!function(e,t,r){(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r}(fe,"featureName",ue.t9);var de=i(3916),le=i(3752),he=i(8683),pe=i.n(he);const ge="nr@original";var ve=Object.prototype.hasOwnProperty,me=!1;function be(e,t){return e||(e=le.ee),r.inPlace=function(e,t,n,i,o){n||(n="");var a,s,c,u="-"===n.charAt(0);for(c=0;c<t.length;c++)Ee(a=e[s=t[c]])||(e[s]=r(a,u?s+n:n,i,s,o))},r.flag=ge,r;function r(t,r,i,o,a){return Ee(t)?t:(r||(r=""),nrWrapper[ge]=t,we(t,nrWrapper,e),nrWrapper);function nrWrapper(){var s,c,u,f;try{c=this,s=pe()(arguments),u="function"==typeof i?i(s,c):i||{}}catch(t){ye([t,"",[s,c,o],u],e)}n(r+"start",[s,c,o],u,a);try{return f=t.apply(c,s)}catch(e){throw n(r+"err",[s,c,e],u,a),e}finally{n(r+"end",[s,c,f],u,a)}}}function n(r,n,i,o){if(!me||t){var a=me;me=!0;try{e.emit(r,n,i,t,o)}catch(t){ye([t,r,n,i],e)}me=a}}}function ye(e,t){t||(t=le.ee);try{t.emit("internal-error",e)}catch(e){}}function we(e,t,r){if(Object.defineProperty&&Object.keys)try{return Object.keys(e).forEach((function(r){Object.defineProperty(t,r,{get:function(){return e[r]},set:function(t){return e[r]=t,t}})})),t}catch(e){ye([e],r)}for(var n in e)ve.call(e,n)&&(t[n]=e[n]);return t}function Ee(e){return!(e&&e instanceof Function&&e.apply&&!e[ge])}var Te="fetch-",Ae=Te+"body-",xe=["arrayBuffer","blob","json","text","formData"],_e=p._A.Request,Se=p._A.Response,Oe="prototype",Pe="nr@context";const je={};function De(e){const t=function(e){return(e||le.ee).get("fetch")}(e);if(!(_e&&Se&&p._A.fetch))return t;if(je[t.debugId]++)return t;function r(e,r,n){var i=e[r];"function"==typeof i&&(e[r]=function(){var e,r=pe()(arguments),o={};t.emit(n+"before-start",[r],o),o[Pe]&&o[Pe].dt&&(e=o[Pe].dt);var a=i.apply(this,r);return t.emit(n+"start",[r,e],a),a.then((function(e){return t.emit(n+"end",[null,e],a),e}),(function(e){throw t.emit(n+"end",[e],a),e}))},e[r][ge]=i)}return je[t.debugId]=1,xe.forEach((e=>{r(_e[Oe],e,Ae),r(Se[Oe],e,Ae)})),r(p._A,"fetch",Te),t.on(Te+"end",(function(e,r){var n=this;if(r){var i=r.headers.get("content-length");null!==i&&(n.rxSize=i),t.emit(Te+"done",[null,r],n)}else t.emit(Te+"done",[e],n)})),t}const Ne={},Ce="setTimeout",Ie="setInterval",Re="clearTimeout",ke="-start",Le="-",He=[Ce,"setImmediate",Ie,Re,"clearImmediate"];function ze(e){const t=function(e){return(e||le.ee).get("timer")}(e);if(Ne[t.debugId]++)return t;Ne[t.debugId]=1;var r=be(t);return r.inPlace(p._A,He.slice(0,2),Ce+Le),r.inPlace(p._A,He.slice(2,3),Ie+Le),r.inPlace(p._A,He.slice(3),Re+Le),t.on(Ie+ke,(function(e,t,n){e[0]=r(e[0],"fn-",null,n)})),t.on(Ce+ke,(function(e,t,n){this.method=n,this.timerDuration=isNaN(e[1])?0:+e[1],e[0]=r(e[0],"fn-",this,n)})),t}const Me={},Be="requestAnimationFrame";function Fe(e){const t=function(e){return(e||le.ee).get("raf")}(e);if(!p.il||Me[t.debugId]++)return t;Me[t.debugId]=1;var r=be(t);return r.inPlace(window,[Be],"raf-"),t.on("raf-start",(function(e){e[0]=r(e[0],"fn-")})),t}const Ue={},Ve=["pushState","replaceState"];function We(e){const t=function(e){return(e||le.ee).get("history")}(e);return!p.il||Ue[t.debugId]++||(Ue[t.debugId]=1,be(t).inPlace(window.history,Ve,"-")),t}const qe={},Ge=["appendChild","insertBefore","replaceChild"];function Xe(e){const t=function(e){return(e||le.ee).get("jsonp")}(e);if(!p.il||qe[t.debugId])return t;qe[t.debugId]=!0;var r=be(t),n=/[?&](?:callback|cb)=([^&#]+)/,i=/(.*)\.([^.]+)/,o=/^(\w+)(\.|$)(.*)$/;function a(e,t){var r=e.match(o),n=r[1],i=r[3];return i?a(i,t[n]):t[n]}return r.inPlace(Node.prototype,Ge,"dom-"),t.on("dom-start",(function(e){!function(e){if(!e||"string"!=typeof e.nodeName||"script"!==e.nodeName.toLowerCase())return;if("function"!=typeof e.addEventListener)return;var o=(s=e.src,c=s.match(n),c?c[1]:null);var s,c;if(!o)return;var u=function(e){var t=e.match(i);if(t&&t.length>=3)return{key:t[2],parent:a(t[1],window)};return{key:e,parent:window}}(o);if("function"!=typeof u.parent[u.key])return;var f={};function d(){t.emit("jsonp-end",[],f),e.removeEventListener("load",d,(0,R.m$)(!1)),e.removeEventListener("error",l,(0,R.m$)(!1))}function l(){t.emit("jsonp-error",[],f),t.emit("jsonp-end",[],f),e.removeEventListener("load",d,(0,R.m$)(!1)),e.removeEventListener("error",l,(0,R.m$)(!1))}r.inPlace(u.parent,[u.key],"cb-",f),e.addEventListener("load",d,(0,R.m$)(!1)),e.addEventListener("error",l,(0,R.m$)(!1)),t.emit("new-jsonp",[e.src],f)}(e[0])})),t}const $e={};function Ze(e){const r=function(e){return(e||le.ee).get("mutation")}(e);if(!p.il||$e[r.debugId])return r;$e[r.debugId]=!0;var n=be(r),i=t.Yu.MO;return i&&(window.MutationObserver=function(e){return this instanceof i?new i(n(e,"fn-")):i.apply(this,arguments)},MutationObserver.prototype=i.prototype),r}const Ye={};function Qe(e){const r=function(e){return(e||le.ee).get("promise")}(e);if(Ye[r.debugId])return r;Ye[r.debugId]=!0;var n=le.c,i=be(r),o=t.Yu.PR;return o&&function(){function e(t){var n=r.context(),a=i(t,"executor-",n,null,!1);const s=Reflect.construct(o,[a],e);return r.context(s).getCtx=function(){return n},s}p._A.Promise=e,Object.defineProperty(e,"name",{value:"Promise"}),e.toString=function(){return o.toString()},Object.setPrototypeOf(e,o),["all","race"].forEach((function(t){const n=o[t];e[t]=function(e){let i=!1;e?.forEach((e=>{this.resolve(e).then(a("all"===t),a(!1))}));const o=n.apply(this,arguments);return o;function a(e){return function(){r.emit("propagate",[null,!i],o,!1,!1),i=i||!e}}}})),["resolve","reject"].forEach((function(t){const n=o[t];e[t]=function(e){const t=n.apply(this,arguments);return e!==t&&r.emit("propagate",[e,!0],t,!1,!1),t}})),e.prototype=o.prototype;const t=o.prototype.then;o.prototype.then=function(){var e=this,o=n(e);o.promise=e;for(var a=arguments.length,s=new Array(a),c=0;c<a;c++)s[c]=arguments[c];s[0]=i(s[0],"cb-",o,null,!1),s[1]=i(s[1],"cb-",o,null,!1);const u=t.apply(this,s);return o.nextPromise=u,r.emit("propagate",[e,!0],u,!1,!1),u},o.prototype.then[ge]=t,r.on("executor-start",(function(e){e[0]=i(e[0],"resolve-",this,null,!1),e[1]=i(e[1],"resolve-",this,null,!1)})),r.on("executor-err",(function(e,t,r){e[1](r)})),r.on("cb-end",(function(e,t,n){r.emit("propagate",[n,!0],this.nextPromise,!1,!1)})),r.on("propagate",(function(e,t,n){this.getCtx&&!t||(this.getCtx=function(){if(e instanceof Promise)var t=r.context(e);return t&&t.getCtx?t.getCtx():this})}))}(),r}const Ke={},Je=XMLHttpRequest,et="addEventListener",tt="removeEventListener";function rt(e){var t=function(e){return(e||le.ee).get("events")}(e);if(Ke[t.debugId]++)return t;Ke[t.debugId]=1;var r=be(t,!0);function n(e){r.inPlace(e,[et,tt],"-",i)}function i(e,t){return e[1]}return"getPrototypeOf"in Object&&(p.il&&nt(document,n),nt(p._A,n),nt(Je.prototype,n)),t.on(et+"-start",(function(e,t){var n=e[1];if(null!==n&&("function"==typeof n||"object"==typeof n)){var i=(0,de.X)(n,"nr@wrapped",(function(){var e={object:function(){if("function"!=typeof n.handleEvent)return;return n.handleEvent.apply(n,arguments)},function:n}[typeof n];return e?r(e,"fn-",null,e.name||"anonymous"):n}));this.wrapped=e[1]=i}})),t.on(tt+"-start",(function(e){e[1]=this.wrapped||e[1]})),t}function nt(e,t){let r=e;for(;"object"==typeof r&&!Object.prototype.hasOwnProperty.call(r,et);)r=Object.getPrototypeOf(r);for(var n=arguments.length,i=new Array(n>2?n-2:0),o=2;o<n;o++)i[o-2]=arguments[o];r&&t(r,...i)}const it={},ot=["open","send"];function at(e){var r=e||le.ee;const n=function(e){return(e||le.ee).get("xhr")}(r);if(it[n.debugId]++)return n;it[n.debugId]=1,rt(r);var i=be(n),o=t.Yu.XHR,a=t.Yu.MO,s=t.Yu.PR,c=t.Yu.SI,u="readystatechange",f=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],d=[],l=p._A.XMLHttpRequest.listeners,h=p._A.XMLHttpRequest=function(e){var t=new o(e);function r(){try{n.emit("new-xhr",[t],t),t.addEventListener(u,m,(0,R.m$)(!1))}catch(e){(0,g.Z)("An error occured while intercepting XHR",e);try{n.emit("internal-error",[e])}catch(e){}}}return this.listeners=l?[...l,r]:[r],this.listeners.forEach((e=>e())),t};function v(e,t){i.inPlace(t,["onreadystatechange"],"fn-",T)}function m(){var e=this,t=n.context(e);e.readyState>3&&!t.resolved&&(t.resolved=!0,n.emit("xhr-resolved",[],e)),i.inPlace(e,f,"fn-",T)}if(function(e,t){for(var r in e)t[r]=e[r]}(o,h),h.prototype=o.prototype,i.inPlace(h.prototype,ot,"-xhr-",T),n.on("send-xhr-start",(function(e,t){v(e,t),function(e){d.push(e),a&&(b?b.then(E):c?c(E):(y=-y,w.data=y))}(t)})),n.on("open-xhr-start",v),a){var b=s&&s.resolve();if(!c&&!s){var y=1,w=document.createTextNode(y);new a(E).observe(w,{characterData:!0})}}else r.on("fn-end",(function(e){e[0]&&e[0].type===u||E()}));function E(){for(var e=0;e<d.length;e++)v(0,d[e]);d.length&&(d=[])}function T(e,t){return t}return n}var st,ct={};try{st=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(ct.console=!0,-1!==st.indexOf("dev")&&(ct.dev=!0),-1!==st.indexOf("nr_dev")&&(ct.nrDev=!0))}catch(e){}function ut(e){try{ct.console&&ut(e)}catch(e){}}ct.nrDev&&le.ee.on("internal-error",(function(e){ut(e.stack)})),ct.dev&&le.ee.on("fn-err",(function(e,t,r){ut(r.stack)})),ct.dev&&(ut("NR AGENT IN DEVELOPMENT MODE"),ut("flags: "+(0,A.D)(ct,(function(e,t){return e})).join(", ")));var ft=i(8322);function dt(e,t){!function(e,t){if(t.has(e))throw new TypeError("Cannot initialize the same private elements twice on an object")}(e,t),t.add(e)}var lt=new WeakSet;class ht extends v{constructor(r,n){var i;let o=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(r,n,ft.t,o),i=this,dt(this,lt),this.skipNext=0,this.origOnerror=p._A.onerror;try{this.removeOnAbort=new AbortController}catch(e){}const a=this;a.ee.on("fn-start",(function(e,t,r){a.abortHandler&&(a.skipNext+=1)})),a.ee.on("fn-err",(function(e,t,r){a.abortHandler&&!r[ft.A]&&((0,de.X)(r,ft.A,(function(){return!0})),this.thrown=!0,vt(r,void 0,a.ee))})),a.ee.on("fn-end",(function(){a.abortHandler&&!this.thrown&&a.skipNext>0&&(a.skipNext-=1)})),a.ee.on("internal-error",(function(t){(0,c.p)("ierr",[t,(0,u.z)(),!0],void 0,e.D.jserrors,a.ee)})),p._A.onerror=function(){return i.origOnerror&&i.origOnerror(...arguments),i.onerrorHandler(...arguments),!1},p._A.addEventListener("unhandledrejection",(t=>{const r=function(e){let t="Unhandled Promise Rejection: ";if(e instanceof Error)try{return e.message=t+e.message,e}catch(t){return e}if(void 0===e)return new Error(t);try{return new Error(t+(0,N.P)(e))}catch(e){return new Error(t)}}(t.reason);(0,c.p)("err",[r,(0,u.z)(),!1,{unhandledPromiseRejection:1}],void 0,e.D.jserrors,this.ee)}),(0,R.m$)(!1,this.removeOnAbort?.signal)),Fe(this.ee),ze(this.ee),rt(this.ee),(0,t.OP)(r).xhrWrappable&&at(this.ee),this.abortHandler=function(e,t,r){if(!t.has(e))throw new TypeError("attempted to get private field on non-instance");return r}(this,lt,pt),this.importAggregator()}onerrorHandler(t,r,n,i,o){try{this.skipNext?this.skipNext-=1:vt(o||new gt(t,r,n),!0,this.ee)}catch(t){try{(0,c.p)("ierr",[t,(0,u.z)(),!0],void 0,e.D.jserrors,this.ee)}catch(e){}}return"function"==typeof this.origOnerror&&this.origOnerror.apply(this,pe()(arguments))}}function pt(){this.removeOnAbort?.abort(),this.abortHandler=void 0}function gt(e,t,r){this.message=e||"Uncaught error with no additional information",this.sourceURL=t,this.line=r}function vt(t,r,n){var i=r?null:(0,u.z)();(0,c.p)("err",[t,i],void 0,e.D.jserrors,n)}!function(e,t,r){(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r}(ht,"featureName",ft.t);var mt=1,bt="nr@id";function yt(e){var t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===p._A?0:(0,de.X)(e,bt,(function(){return mt++}))}var wt=i(9071);function Et(e){if("string"==typeof e&&e.length)return e.length;if("object"==typeof e){if("undefined"!=typeof ArrayBuffer&&e instanceof ArrayBuffer&&e.byteLength)return e.byteLength;if("undefined"!=typeof Blob&&e instanceof Blob&&e.size)return e.size;if(!("undefined"!=typeof FormData&&e instanceof FormData))try{return(0,N.P)(e).length}catch(e){return}}}var Tt=i(6368);class At{constructor(e){this.agentIdentifier=e,this.generateTracePayload=this.generateTracePayload.bind(this),this.shouldGenerateTrace=this.shouldGenerateTrace.bind(this)}generateTracePayload(e){if(!this.shouldGenerateTrace(e))return null;var r=(0,t.DL)(this.agentIdentifier);if(!r)return null;var n=(r.accountID||"").toString()||null,i=(r.agentID||"").toString()||null,o=(r.trustKey||"").toString()||null;if(!n||!i)return null;var a=(0,D.M)(),s=(0,D.Ht)(),c=Date.now(),u={spanId:a,traceId:s,timestamp:c};return(e.sameOrigin||this.isAllowedOrigin(e)&&this.useTraceContextHeadersForCors())&&(u.traceContextParentHeader=this.generateTraceContextParentHeader(a,s),u.traceContextStateHeader=this.generateTraceContextStateHeader(a,c,n,i,o)),(e.sameOrigin&&!this.excludeNewrelicHeader()||!e.sameOrigin&&this.isAllowedOrigin(e)&&this.useNewrelicHeaderForCors())&&(u.newrelicHeader=this.generateTraceHeader(a,s,c,n,i,o)),u}generateTraceContextParentHeader(e,t){return"00-"+t+"-"+e+"-01"}generateTraceContextStateHeader(e,t,r,n,i){return i+"@nr=0-1-"+r+"-"+n+"-"+e+"----"+t}generateTraceHeader(e,t,r,n,i,o){if(!("function"==typeof p._A?.btoa))return null;var a={v:[0,1],d:{ty:"Browser",ac:n,ap:i,id:e,tr:t,ti:r}};return o&&n!==o&&(a.d.tk=o),btoa((0,N.P)(a))}shouldGenerateTrace(e){return this.isDtEnabled()&&this.isAllowedOrigin(e)}isAllowedOrigin(e){var r=!1,n={};if((0,t.Mt)(this.agentIdentifier,"distributed_tracing")&&(n=(0,t.P_)(this.agentIdentifier).distributed_tracing),e.sameOrigin)r=!0;else if(n.allowed_origins instanceof Array)for(var i=0;i<n.allowed_origins.length;i++){var o=(0,Tt.e)(n.allowed_origins[i]);if(e.hostname===o.hostname&&e.protocol===o.protocol&&e.port===o.port){r=!0;break}}return r}isDtEnabled(){var e=(0,t.Mt)(this.agentIdentifier,"distributed_tracing");return!!e&&!!e.enabled}excludeNewrelicHeader(){var e=(0,t.Mt)(this.agentIdentifier,"distributed_tracing");return!!e&&!!e.exclude_newrelic_header}useNewrelicHeaderForCors(){var e=(0,t.Mt)(this.agentIdentifier,"distributed_tracing");return!!e&&!1!==e.cors_use_newrelic_header}useTraceContextHeadersForCors(){var e=(0,t.Mt)(this.agentIdentifier,"distributed_tracing");return!!e&&!!e.cors_use_tracecontext_headers}}var xt=i(8675);var _t=["load","error","abort","timeout"],St=_t.length,Ot=t.Yu.REQ,Pt=p._A.XMLHttpRequest;class jt extends v{constructor(r,n){let i=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(r,n,xt.t,i),(0,t.OP)(r).xhrWrappable&&(this.dt=new At(r),this.handler=(e,t,r,n)=>(0,c.p)(e,t,r,n,this.ee),De(this.ee),at(this.ee),function(r,n,i,o){function a(e){var t=this;t.totalCbs=0,t.called=0,t.cbTime=0,t.end=A,t.ended=!1,t.xhrGuids={},t.lastSize=null,t.loadCaptureCalled=!1,t.params=this.params||{},t.metrics=this.metrics||{},e.addEventListener("load",(function(r){_(t,e)}),(0,R.m$)(!1)),wt.I||e.addEventListener("progress",(function(e){t.lastSize=e.loaded}),(0,R.m$)(!1))}function s(e){this.params={method:e[0]},x(this,e[1]),this.metrics={}}function c(e,n){var i=(0,t.DL)(r);"xpid"in i&&this.sameOrigin&&n.setRequestHeader("X-NewRelic-ID",i.xpid);var a=o.generateTracePayload(this.parsedOrigin);if(a){var s=!1;a.newrelicHeader&&(n.setRequestHeader("newrelic",a.newrelicHeader),s=!0),a.traceContextParentHeader&&(n.setRequestHeader("traceparent",a.traceContextParentHeader),a.traceContextStateHeader&&n.setRequestHeader("tracestate",a.traceContextStateHeader),s=!0),s&&(this.dt=a)}}function f(e,t){var r=this.metrics,i=e[0],o=this;if(r&&i){var a=Et(i);a&&(r.txSize=a)}this.startTime=(0,u.z)(),this.listener=function(e){try{"abort"!==e.type||o.loadCaptureCalled||(o.params.aborted=!0),("load"!==e.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof t.onload)&&"function"==typeof o.end)&&o.end(t)}catch(e){try{n.emit("internal-error",[e])}catch(e){}}};for(var s=0;s<St;s++)t.addEventListener(_t[s],this.listener,(0,R.m$)(!1))}function d(e,t,r){this.cbTime+=e,t?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof r.onload||"function"!=typeof this.end||this.end(r)}function l(e,t){var r=""+yt(e)+!!t;this.xhrGuids&&!this.xhrGuids[r]&&(this.xhrGuids[r]=!0,this.totalCbs+=1)}function h(e,t){var r=""+yt(e)+!!t;this.xhrGuids&&this.xhrGuids[r]&&(delete this.xhrGuids[r],this.totalCbs-=1)}function g(){this.endTime=(0,u.z)()}function v(e,t){t instanceof Pt&&"load"===e[0]&&n.emit("xhr-load-added",[e[1],e[2]],t)}function m(e,t){t instanceof Pt&&"load"===e[0]&&n.emit("xhr-load-removed",[e[1],e[2]],t)}function b(e,t,r){t instanceof Pt&&("onload"===r&&(this.onload=!0),("load"===(e[0]&&e[0].type)||this.onload)&&(this.xhrCbStart=(0,u.z)()))}function y(e,t){this.xhrCbStart&&n.emit("xhr-cb-time",[(0,u.z)()-this.xhrCbStart,this.onload,t],t)}function w(e){var t,r=e[1]||{};"string"==typeof e[0]?t=e[0]:e[0]&&e[0].url?t=e[0].url:p._A?.URL&&e[0]&&e[0]instanceof URL&&(t=e[0].href),t&&(this.parsedOrigin=(0,Tt.e)(t),this.sameOrigin=this.parsedOrigin.sameOrigin);var n=o.generateTracePayload(this.parsedOrigin);if(n&&(n.newrelicHeader||n.traceContextParentHeader))if("string"==typeof e[0]||p._A?.URL&&e[0]&&e[0]instanceof URL){var i={};for(var a in r)i[a]=r[a];i.headers=new Headers(r.headers||{}),s(i.headers,n)&&(this.dt=n),e.length>1?e[1]=i:e.push(i)}else e[0]&&e[0].headers&&s(e[0].headers,n)&&(this.dt=n);function s(e,t){var r=!1;return t.newrelicHeader&&(e.set("newrelic",t.newrelicHeader),r=!0),t.traceContextParentHeader&&(e.set("traceparent",t.traceContextParentHeader),t.traceContextStateHeader&&e.set("tracestate",t.traceContextStateHeader),r=!0),r}}function E(e,t){this.params={},this.metrics={},this.startTime=(0,u.z)(),this.dt=t,e.length>=1&&(this.target=e[0]),e.length>=2&&(this.opts=e[1]);var r,n=this.opts||{},i=this.target;"string"==typeof i?r=i:"object"==typeof i&&i instanceof Ot?r=i.url:p._A?.URL&&"object"==typeof i&&i instanceof URL&&(r=i.href),x(this,r);var o=(""+(i&&i instanceof Ot&&i.method||n.method||"GET")).toUpperCase();this.params.method=o,this.txSize=Et(n.body)||0}function T(t,r){var n;this.endTime=(0,u.z)(),this.params||(this.params={}),this.params.status=r?r.status:0,"string"==typeof this.rxSize&&this.rxSize.length>0&&(n=+this.rxSize);var o={txSize:this.txSize,rxSize:n,duration:(0,u.z)()-this.startTime};i("xhr",[this.params,o,this.startTime,this.endTime,"fetch"],this,e.D.ajax)}function A(t){var r=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var o=0;o<St;o++)t.removeEventListener(_t[o],this.listener,!1);r.aborted||(n.duration=(0,u.z)()-this.startTime,this.loadCaptureCalled||4!==t.readyState?null==r.status&&(r.status=0):_(this,t),n.cbTime=this.cbTime,i("xhr",[r,n,this.startTime,this.endTime,"xhr"],this,e.D.ajax))}}function x(e,t){var r=(0,Tt.e)(t),n=e.params;n.hostname=r.hostname,n.port=r.port,n.protocol=r.protocol,n.host=r.hostname+":"+r.port,n.pathname=r.pathname,e.parsedOrigin=r,e.sameOrigin=r.sameOrigin}function _(e,t){e.params.status=t.status;var r=function(e,t){var r=e.responseType;return"json"===r&&null!==t?t:"arraybuffer"===r||"blob"===r||"json"===r?Et(e.response):"text"===r||""===r||void 0===r?Et(e.responseText):void 0}(t,e.lastSize);if(r&&(e.metrics.rxSize=r),e.sameOrigin){var n=t.getResponseHeader("X-NewRelic-App-Data");n&&(e.params.cat=n.split(", ").pop())}e.loadCaptureCalled=!0}n.on("new-xhr",a),n.on("open-xhr-start",s),n.on("open-xhr-end",c),n.on("send-xhr-start",f),n.on("xhr-cb-time",d),n.on("xhr-load-added",l),n.on("xhr-load-removed",h),n.on("xhr-resolved",g),n.on("addEventListener-end",v),n.on("removeEventListener-end",m),n.on("fn-end",y),n.on("fetch-before-start",w),n.on("fetch-start",E),n.on("fn-start",b),n.on("fetch-done",T)}(r,this.ee,this.handler,this.dt),this.importAggregator())}}!function(e,t,r){(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r}(jt,"featureName",xt.t);var Dt=i(6408),Nt=i(2628);function Ct(e,t){!function(e,t){if(t.has(e))throw new TypeError("Cannot initialize the same private elements twice on an object")}(e,t),t.add(e)}const{BST_RESOURCE:It,BST_TIMER:Rt,END:kt,FEATURE_NAME:Lt,FN_END:Ht,FN_START:zt,ADD_EVENT_LISTENER:Mt,PUSH_STATE:Bt,RESOURCE:Ft,RESOURCE_TIMING_BUFFER_FULL:Ut,START:Vt,ORIG_EVENT:Wt}=Nt,qt="clearResourceTimings";var Gt=new WeakSet;class Xt extends v{constructor(t,r){if(super(t,r,Lt,!(arguments.length>2&&void 0!==arguments[2])||arguments[2]),Ct(this,Gt),!p.il)return;const n=this.ee;this.timerEE=ze(n),this.rafEE=Fe(n),We(n),rt(n),n.on(zt,(function(e,t){e[0]instanceof Wt&&(this.bstStart=(0,u.z)())})),n.on(Ht,(function(t,r){var i=t[0];i instanceof Wt&&(0,c.p)("bst",[i,r,this.bstStart,(0,u.z)()],void 0,e.D.sessionTrace,n)})),this.timerEE.on(zt,(function(e,t,r){this.bstStart=(0,u.z)(),this.bstType=r})),this.timerEE.on(Ht,(function(t,r){(0,c.p)(Rt,[r,this.bstStart,(0,u.z)(),this.bstType],void 0,e.D.sessionTrace,n)})),this.rafEE.on(zt,(function(){this.bstStart=(0,u.z)()})),this.rafEE.on(Ht,(function(t,r){(0,c.p)(Rt,[r,this.bstStart,(0,u.z)(),"requestAnimationFrame"],void 0,e.D.sessionTrace,n)})),n.on(Bt+Vt,(function(e){this.time=(0,u.z)(),this.startPath=location.pathname+location.hash})),n.on(Bt+kt,(function(t){(0,c.p)("bstHist",[location.pathname+location.hash,this.startPath,this.time],void 0,e.D.sessionTrace,n)})),(0,Dt.W)()?((0,c.p)(It,[window.performance.getEntriesByType("resource")],void 0,e.D.sessionTrace,n),function(){var t=new PerformanceObserver(((t,r)=>{var i=t.getEntries();(0,c.p)(It,[i],void 0,e.D.sessionTrace,n)}));try{t.observe({entryTypes:["resource"]})}catch(e){}}()):window.performance[qt]&&window.performance[Mt]&&window.performance.addEventListener(Ut,this.onResourceTimingBufferFull,(0,R.m$)(!1)),document.addEventListener("scroll",this.noOp,(0,R.m$)(!1)),document.addEventListener("keypress",this.noOp,(0,R.m$)(!1)),document.addEventListener("click",this.noOp,(0,R.m$)(!1)),this.abortHandler=function(e,t,r){if(!t.has(e))throw new TypeError("attempted to get private field on non-instance");return r}(this,Gt,$t),this.importAggregator()}noOp(e){}onResourceTimingBufferFull(t){if((0,c.p)(It,[window.performance.getEntriesByType(Ft)],void 0,e.D.sessionTrace,this.ee),window.performance[qt])try{window.performance.removeEventListener(Ut,this.onResourceTimingBufferFull,!1)}catch(e){}}}function $t(){window.performance.removeEventListener(Ut,this.onResourceTimingBufferFull,!1),this.abortHandler=void 0}!function(e,t,r){(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r}(Xt,"featureName",Lt);var Zt=i(755);function Yt(e,t){!function(e,t){if(t.has(e))throw new TypeError("Cannot initialize the same private elements twice on an object")}(e,t),t.add(e)}const{FEATURE_NAME:Qt,START:Kt,END:Jt,BODY:er,CB_END:tr,JS_TIME:rr,FETCH:nr,FN_START:ir,CB_START:or,FN_END:ar}=Zt;var sr=new WeakSet;class cr extends v{constructor(e,r){if(super(e,r,Qt,!(arguments.length>2&&void 0!==arguments[2])||arguments[2]),Yt(this,sr),!p.il)return;if(!(0,t.OP)(e).xhrWrappable)return;try{this.removeOnAbort=new AbortController}catch(e){}let n,i=0;const o=this.ee.get("tracer"),a=Xe(this.ee),s=Qe(this.ee),c=ze(this.ee),f=at(this.ee),d=this.ee.get("events"),l=De(this.ee),h=We(this.ee),g=Ze(this.ee);function v(e,t){h.emit("newURL",[""+window.location,t])}function m(){i++,n=window.location.hash,this[ir]=(0,u.z)()}function b(){i--,window.location.hash!==n&&v(0,!0);var e=(0,u.z)();this[rr]=~~this[rr]+e-this[ir],this[ar]=e}function y(e,t){e.on(t,(function(){this[t]=(0,u.z)()}))}this.ee.on(ir,m),s.on(or,m),a.on(or,m),this.ee.on(ar,b),s.on(tr,b),a.on(tr,b),this.ee.buffer([ir,ar,"xhr-resolved"],this.featureName),d.buffer([ir],this.featureName),c.buffer(["setTimeout"+Jt,"clearTimeout"+Kt,ir],this.featureName),f.buffer([ir,"new-xhr","send-xhr"+Kt],this.featureName),l.buffer([nr+Kt,nr+"-done",nr+er+Kt,nr+er+Jt],this.featureName),h.buffer(["newURL"],this.featureName),g.buffer([ir],this.featureName),s.buffer(["propagate",or,tr,"executor-err","resolve"+Kt],this.featureName),o.buffer([ir,"no-"+ir],this.featureName),a.buffer(["new-jsonp","cb-start","jsonp-error","jsonp-end"],this.featureName),y(l,nr+Kt),y(l,nr+"-done"),y(a,"new-jsonp"),y(a,"jsonp-end"),y(a,"cb-start"),h.on("pushState-end",v),h.on("replaceState-end",v),window.addEventListener("hashchange",v,(0,R.m$)(!0,this.removeOnAbort?.signal)),window.addEventListener("load",v,(0,R.m$)(!0,this.removeOnAbort?.signal)),window.addEventListener("popstate",(function(){v(0,i>1)}),(0,R.m$)(!0,this.removeOnAbort?.signal)),this.abortHandler=function(e,t,r){if(!t.has(e))throw new TypeError("attempted to get private field on non-instance");return r}(this,sr,ur),this.importAggregator()}}function ur(){this.removeOnAbort?.abort(),this.abortHandler=void 0}!function(e,t,r){(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r}(cr,"featureName",Qt);var fr=i(6486);class dr extends v{constructor(e,t){let r=!(arguments.length>2&&void 0!==arguments[2])||arguments[2];super(e,t,fr.t,r),this.importAggregator()}}!function(e,t,r){(t=function(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!=typeof n)return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r}(dr,"featureName",fr.t),new class{constructor(e){let t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:(0,D.ky)(16);this.agentIdentifier=t,this.sharedAggregator=new x({agentIdentifier:this.agentIdentifier}),this.features={},this.desiredFeatures=new Set(e.features||[]),this.desiredFeatures.add(E),Object.assign(this,(0,a.j)(this.agentIdentifier,e,e.loaderType||"agent")),this.start()}get config(){return{info:(0,t.C5)(this.agentIdentifier),init:(0,t.P_)(this.agentIdentifier),loader_config:(0,t.DL)(this.agentIdentifier),runtime:(0,t.OP)(this.agentIdentifier)}}start(){const t="features";try{const r=n(this.agentIdentifier),i=Array.from(this.desiredFeatures);i.sort(((t,r)=>e.p[t.featureName]-e.p[r.featureName])),i.forEach((t=>{if(r[t.featureName]||t.featureName===e.D.pageViewEvent){const e=(0,s.Z)(t.featureName),n=e.every((e=>r[e]));n||(0,g.Z)("".concat(t.featureName," is enabled but one or more dependent features has been disabled (").concat((0,N.P)(e),"). This may cause unintended consequences or missing data...")),this.features[t.featureName]=new t(this.agentIdentifier,this.sharedAggregator)}})),(0,j.Qy)(this.agentIdentifier,this.features,t)}catch(e){(0,g.Z)("Failed to initialize all enabled instrument classes (agent aborted) -",e);for(const e in this.features)this.features[e].abortHandler?.();const r=(0,j.fP)();return delete r.initializedAgents[this.agentIdentifier]?.api,delete r.initializedAgents[this.agentIdentifier]?.[t],delete this.sharedAggregator,r.ee?.abort(),delete r.ee?.get(this.agentIdentifier),!1}}}({features:[jt,E,ie,Xt,fe,dr,ht,cr],loaderType:"spa"})})(),window.NRBA=o})();</script>

        <script>
            (function () {
            if (window.PerformanceObserver) {
                window._perfMarkAllowedList = [
                'cx-candybar-onload',
                'first-contentful-paint',
                'cx-candybar-onload',
                'gcRendererStart',
                'gpt-tagLoaded',
                'gpt-slotRequested',
                'gpt-slotRenderEnded',
                'gpt-slotOnload',
                'optimizely:blockBegin',
                'playerLoadStart',
                'playerReady',
                'playerDisplayed',
                'prebidAuctionInit',
                'prebidAuctionEnd',
                'reactAppRenderStart',
                'reactAppRenderEnd',
                'apstag-loaded',
                'apstag-firstBid',
                'moat-loaded',
                'moat-ace-firstAdItem',
                'moat-uac-firstAdItem',
                'djcmp-loaded',
                'djcmp-vendor-loaded',
                'djcmp-tcdata-loaded'
            ];
                var observer = new PerformanceObserver(function (list) {
                var entries = list.getEntries();
                var _loop = function _loop(i) {
                    var entry = entries[i];
                    var metricName = entry.name;
                    if ( window._perfMarkAllowedList.indexOf(entry.name) !== -1 ) {
                    var time = Math.round(entry.startTime + entry.duration);
                    if (metricName === 'gpt-slotOnload' ) {
                        if (typeof newrelic !== 'undefined') {
                        newrelic.setCustomAttribute(metricName, time);
                        }
                        setTimeout(function(){observer.disconnect()}, 8000)
                    } else {
                        if (typeof newrelic !== 'undefined') {
                        newrelic.setCustomAttribute(metricName, time);
                        }
                    }
                    }
                };
                for (var i = 0; i < entries.length; i++) {
                    _loop(i);
                }
                });
                try {
                observer.observe({
                    type: ['mark'], buffered: true
                });
                }
                catch(e) {
                console.log('observer not supported')
                }
            }
            })();
        </script>


        <script>
            if (typeof MarketWatch === 'undefined')
                MarketWatch = {};
            MarketWatch.Features = {
                
            };
        </script>


        <script>
            // Sourcepoints Transparency and Consent Framework for Consent Management Platform [GDPR, CMP, TCFAPI, other buzzwords to help when searching]
            // CMP stub code in all sites behind CMP:
            //old one
            //function _typeof(e){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}!function(){for(var e,t,n=[],o=window,r=o;r;){try{if(r.frames.__tcfapiLocator){e=r;break}}catch(e){}if(r===o.top)break;r=o.parent}e||(function e(){var t=o.document,n=!!o.frames.__tcfapiLocator;if(!n)if(t.body){var r=t.createElement("iframe");r.style.cssText="display:none",r.name="__tcfapiLocator",t.body.appendChild(r)}else setTimeout(e,5);return!n}(),o.__tcfapi=function(){for(var e=arguments.length,o=new Array(e),r=0;r<e;r++)o[r]=arguments[r];if(!o.length)return n;"setGdprApplies"===o[0]?o.length>3&&2===parseInt(o[1],10)&&"boolean"==typeof o[3]&&(t=o[3],"function"==typeof o[2]&&o[2]("set",!0)):"ping"===o[0]?"function"==typeof o[2]&&o[2]({gdprApplies:t,cmpLoaded:!1,cmpStatus:"stub"}):n.push(o)},o.addEventListener("message",(function(e){var t="string"==typeof e.data,n={};if(t)try{n=JSON.parse(e.data)}catch(e){}else n=e.data;var o="object"===_typeof(n)?n.__tcfapiCall:null;o&&window.__tcfapi(o.command,o.version,(function(n,r){var a={__tcfapiReturn:{returnValue:n,success:r,callId:o.callId}};e&&e.source&&e.source.postMessage&&e.source.postMessage(t?JSON.stringify(a):a,"*")}),o.parameter)}),!1))}(),function(){var e=function(){for(var e,t="__tcfapiLocator",n=[],o=window;o;){try{if(o.frames[t]){e=o;break}}catch(e){}if(o===window.top)break;o=o.parent}e||(function e(){var n=o.document,r=!!o.frames[t];if(!r)if(n.body){var a=n.createElement("iframe");a.style.cssText="display:none",a.name=t,n.body.appendChild(a)}else setTimeout(e,5);return!r}(),o.__tcfapi=function(){for(var e,t=arguments.length,o=new Array(t),r=0;r<t;r++)o[r]=arguments[r];if(!o.length)return n;if("setGdprApplies"===o[0])o.length>3&&2===parseInt(o[1],10)&&"boolean"==typeof o[3]&&(e=o[3],"function"==typeof o[2]&&o[2]("set",!0));else if("ping"===o[0]){var a={gdprApplies:e,cmpLoaded:!1,cmpStatus:"stub"};"function"==typeof o[2]&&o[2](a)}else n.push(o)},o.addEventListener("message",(function(e){var t="string"==typeof e.data,n={};try{n=t?JSON.parse(e.data):e.data}catch(e){}var o=n.__tcfapiCall;o&&window.__tcfapi(o.command,o.version,(function(n,r){var a={__tcfapiReturn:{returnValue:n,success:r,callId:o.callId}};t&&(a=JSON.stringify(a)),e.source.postMessage(a,"*")}),o.parameter)}),!1))};"undefined"!=typeof module?module.exports=e:e()}(),function(e){var t={};function n(o){if(t[o])return t[o].exports;var r=t[o]={i:o,l:!1,exports:{}};return e[o].call(r.exports,r,r.exports,n),r.l=!0,r.exports}n.m=e,n.c=t,n.d=function(e,t,o){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(n.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)n.d(o,r,function(t){return e[t]}.bind(null,r));return o},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="/",n(n.s=0)}([function(e,t,n){"use strict";n.r(t);var o=function(){return!(-1!==(document&&document.cookie||"").indexOf("gdprApplies=false"))},r=function(){return window&&window.djcmp&&window.djcmp.tcData&&window.djcmp.tcData.gdprApplies},a=function(){var e=r();return"boolean"!=typeof e||e},i=function(e,t){switch(e){case"cookieOnly":return o();case"tcfapiOnly":return"function"==typeof t?function(e){var t=r();return"boolean"==typeof t?e(t):window.__tcfapi("getTCData",2,(function(t){var n="boolean"!=typeof t.gdprApplies||t.gdprApplies;e(n)}))}(t):a();case"cookieFirst":return-1!==(document&&document.cookie||"").indexOf("gdprApplies=")?o():a();default:return function(){var e=r();return"boolean"==typeof e?e:o()}()}};!function(){var e=[];function t(){e.push(arguments)}window.djcmp||(t.gdprApplies=i,t.queue=e,window.djcmp=t)}()}]);
            //new one, enable on 12/7
            function _typeof(e){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}!function(){for(var e,t,n=[],r=window,o=r;o;){try{if(o.frames.__tcfapiLocator){e=o;break}}catch(e){}if(o===r.top)break;o=r.parent}e||(function e(){var t=r.document,n=!!r.frames.__tcfapiLocator;if(!n)if(t.body){var o=t.createElement("iframe");o.style.cssText="display:none",o.name="__tcfapiLocator",t.body.appendChild(o)}else setTimeout(e,5);return!n}(),r.__tcfapi=function(){for(var e=arguments.length,r=new Array(e),o=0;o<e;o++)r[o]=arguments[o];if(!r.length)return n;"setGdprApplies"===r[0]?r.length>3&&2===parseInt(r[1],10)&&"boolean"==typeof r[3]&&(t=r[3],"function"==typeof r[2]&&r[2]("set",!0)):"ping"===r[0]?"function"==typeof r[2]&&r[2]({gdprApplies:t,cmpLoaded:!1,cmpStatus:"stub"}):n.push(r)},r.addEventListener("message",(function(e){var t="string"==typeof e.data,n={};if(t)try{n=JSON.parse(e.data)}catch(e){}else n=e.data;var r="object"===_typeof(n)?n.__tcfapiCall:null;r&&window.__tcfapi(r.command,r.version,(function(n,o){var a={__tcfapiReturn:{returnValue:n,success:o,callId:r.callId}};e&&e.source&&e.source.postMessage&&e.source.postMessage(t?JSON.stringify(a):a,"*")}),r.parameter)}),!1))}(),function(){var e=window,t=document;function n(t){var n="string"==typeof t.data;try{var r=n?JSON.parse(t.data):t.data;if(r.__cmpCall){var o=r.__cmpCall;e.__uspapi(o.command,o.parameter,(function(e,r){var a={__cmpReturn:{returnValue:e,success:r,callId:o.callId}};t.source.postMessage(n?JSON.stringify(a):a,"*")}))}}catch(r){}}!function n(){if(!e.frames.__uspapiLocator)if(t.body){var r=t.body,o=t.createElement("iframe");o.style.cssText="display:none",o.name="__uspapiLocator",r.appendChild(o)}else setTimeout(n,5)}(),"function"!=typeof __uspapi&&(e.__uspapi=function(){var e=arguments;if(__uspapi.a=__uspapi.a||[],!e.length)return __uspapi.a;"ping"===e[0]?e[2]({gdprAppliesGlobally:!1,cmpLoaded:!1},!0):__uspapi.a.push([].slice.apply(e))},__uspapi.msgHandler=n,e.addEventListener("message",n,!1))}(),function(e){var t={};function n(r){if(t[r])return t[r].exports;var o=t[r]={i:r,l:!1,exports:{}};return e[r].call(o.exports,o,o.exports,n),o.l=!0,o.exports}n.m=e,n.c=t,n.d=function(e,t,r){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(n.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)n.d(r,o,function(t){return e[t]}.bind(null,o));return r},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="/",n(n.s=0)}([function(e,t,n){"use strict";n.r(t);var r=function(){var e=window.djcmp,t=void 0===e?{}:e;if(!t._params){var n=document.querySelector("#djcmp"),r=n&&n.getAttribute("data-params");t._params=r&&JSON.parse(r)}return t._params||{}},o=function(){return!(-1!==(document&&document.cookie||"").indexOf("gdprApplies=false"))},a=function(){return window&&window.djcmp&&window.djcmp.tcData&&window.djcmp.tcData.gdprApplies},i=function(){var e=a();return"boolean"==typeof e?e:null},p=function(e,t){if(r().gdprApplies)return!0;switch(e){case"cookieOnly":return o();case"serviceOnly":return function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:function(){},t=r().geoServiceUrl;if(t){var n="".concat(t,"/geolocation-services/gdpr");fetch(n).then((function(e){return e.json()})).then((function(t){var n=t.applies;e(n)})).catch((function(){e(null)}))}else"function"==typeof e&&e(null)}(t);case"tcfapiOnly":return"function"==typeof t?function(e){var t=a();return"boolean"==typeof t?e(t):window.__tcfapi("getTCData",2,(function(t){var n="boolean"!=typeof t.gdprApplies||t.gdprApplies;e(n)}))}(t):i();case"cookieFirst":return-1!==(document&&document.cookie||"").indexOf("gdprApplies=")?o():i();default:return function(){var e=a();return"boolean"==typeof e?e:o()}()}},c=function(e){return!!r().ccpaApplies};!function(){var e=[];function t(){e.push(arguments)}window.djcmp||(t.gdprApplies=p,t.ccpaApplies=c,t.queue=e,window.djcmp=t)}()}]);
            
            //old one
            //!function(){var e,t,r;window.ace=window.ace||{},e={},t={},r={addToExecutionQueue(e){return t[e]||(t[e]=[]),t[e].push(arguments),t},getSubscribedElements:()=>Object.keys(e),getSubscribedFunctions:t=>Object.keys(e[t]||{}),executeQueue(e){try{t[e]&&t[e].forEach((e=>this.execute(...e))),delete t[e]}catch(e){console.error(e)}},execute(){var[t,r,i,s]=arguments,n=e[t][r],u=e=>e,c=[];return"function"!=typeof n?n:(i&&("function"==typeof i?(u=i,s&&Array.isArray(s)&&(c=s)):Array.isArray(i)&&(c=i)),u(n.apply(null,c)))},__reset(){var r=e=>Object.keys(e).forEach((t=>delete e[t]));r(e),r(t)},hasSubscription(e){return this.getSubscribedElements().indexOf(e)>-1},hasSubscribedFunction(e,t){return this.getSubscribedFunctions(e).indexOf(t)>-1},addSubscription:(t,r)=>(e[t]=r,e),subscribe(t,r){if(this.hasSubscription(t))throw new Error("There already is a subscription under"+t);if(!r||"object"!=typeof r)throw new Error("Missing third parameter. You must provide an object.");return this.addSubscription(t,r),this.executeQueue(t),e},globalMessaging(){var[e,t,...r]=arguments;if(!e&&!t)return this.getSubscribedElements();if(e&&"string"==typeof e&&!t)return this.getSubscribedFunctions(e);if("string"!=typeof e||"string"!=typeof t)throw new Error("First and second argument must be String types");if(this.hasSubscribedFunction(e,t))return this.execute(e,t,...r);this.addToExecutionQueue(e,t,...r)}},window.__ace=r.globalMessaging.bind(r),window.__ace.subscribe=r.subscribe.bind(r)}();
            //new one, enable on 12/7
            !function(){var e,t,i;window.ace=window.ace||{},e={},t={},i={addToExecutionQueue(e){return t[e]||(t[e]=[]),t[e].push(arguments),t},getSubscribedElements:()=>Object.keys(e),getSubscribedFunctions:t=>Object.keys(e[t]||{}),executeQueue(e){try{t[e]&&t[e].forEach((e=>this.execute(...e))),delete t[e]}catch(e){console.error(e)}},execute(){var[t,i,r,n]=arguments,s=e[t][i],u=e=>e,c=[];return"function"!=typeof s?s:(r&&("function"==typeof r?(u=r,n&&Array.isArray(n)&&(c=n)):Array.isArray(r)&&(c=r)),u(s.apply(null,c)))},__reset(){var i=e=>Object.keys(e).forEach((t=>delete e[t]));i(e),i(t)},hasSubscription(e){return this.getSubscribedElements().indexOf(e)>-1},hasSubscribedFunction(e,t){return this.getSubscribedFunctions(e).indexOf(t)>-1},uniqueFucntionsUnderSubscription(t,i){const{__ace:r=(()=>({}))}=window;let n={};return Object.keys(i).forEach((s=>{e[t][s]?r("log","log",[{type:"warning",initiator:"page",message:"You are trying to subscribe the function "+s+" under the "+t+" namespace again. Use another name."}]):n[s]=i[s]})),n},addSubscription(t,i){if(this.hasSubscription(t)){const r=this.uniqueFucntionsUnderSubscription(t,i);e[t]={...e[t],...r}}else e[t]=i;return e},subscribe(t,i,r){if(r)return e[t]=i,e;if(!i||"object"!=typeof i)throw new Error("Missing third parameter. You must provide an object.");return this.addSubscription(t,i),this.executeQueue(t),e},globalMessaging(){var[e,t,...i]=arguments;if(!e&&!t)return this.getSubscribedElements();if(e&&"string"==typeof e&&!t)return this.getSubscribedFunctions(e);if("string"!=typeof e||"string"!=typeof t)throw new Error("First and second argument must be String types");if(this.hasSubscribedFunction(e,t))return this.execute(e,t,...i);this.addToExecutionQueue(e,t,...i)}},window.__ace=i.globalMessaging.bind(i),window.__ace.subscribe=i.subscribe.bind(i)}()

            var googletag=googletag||{};googletag.cmd=googletag.cmd||[];
            var pbjs=pbjs||{};pbjs.que=pbjs.que||[];

            window.__mwads = window.__mwads || {};
            window.__mwads.uacQ = [];
        </script>


            <script async
                src="https://www.marketwatch.com/asset/ace/ace.min.js"
                data-app="marketwatch"
                data-ace-uac-url="https://www.marketwatch.com/asset/ace"
                data-config="%7B%22enableSourcepoint%22%3Atrue%2C%20%22enableUsp%22%3Atrue%2C%20%22enableLog%22%3Atrue%20%7D"
                id="ace-manifest">
            </script>


            <meta name="uac-config" content="%7b%22breakpoints%22%3a%7b%22at4units%22%3a0%2c%22at8units%22%3a656%2c%22at12units%22%3a976%2c%22at16units%22%3a1296%7d%7d" />
            <script async src="https://securepubads.g.doubleclick.net/tag/js/gpt.js" onload="performance.mark('gpt-tagLoaded')"></script>
                    <script async src="https://us.tags.newscgp.com/prod/prebid/marketwatch/pb-no-auto.js" onload="performance.mark('prebid-tagLoaded')"></script>
            <script>
                window.__mwads.gptEnabled = true;
                window.__mwads.prebidEnabled = true;
                window.__mwads.moatEnabled = true;
                window.__mwads.mpuId = 'ad-display-ad'; 
                    window.__mwads.curatedMap = { A: 1088448, B: 1088449, C: 1091804, D: 1091805 };

                (function() {
                    googletag.cmd.push(function() {
                        googletag.pubads().disableInitialLoad();
                                googletag.pubads().setTargeting('keywords', ['']);
                                googletag.pubads().setTargeting('sym', ['aapl']);
                                googletag.pubads().setTargeting('pagetype', ['quotes']);
                                googletag.pubads().setTargeting('sector', ['technology']);
                                googletag.pubads().setTargeting('industry', ['computers_consumer_electronics']);
                        

                            googletag.pubads().setTargeting('usertype', ['nonsubscriber']);

                        if (typeof enhance !== 'undefined' && typeof enhance.cookie === 'function') {
                            var etear = enhance.cookie('etsFlag');
                            if (etear) {
                                googletag.pubads().setTargeting('msrc', decodeURIComponent(etear));
                            }
                        }
                    });
                })();
            </script>            
                <script async src="https://segment-data.zqtk.net/dowjones-d8s23j?url=https%3A%2F%2Fwww.marketwatch.com"></script>
                <!-- MarketWatch is all y'all -->
        </head>
        <body role="document" class="page--quote symbol--stock tab--overview  page--Index ">



        <section class="container container--masthead Inline masthead--expanded" role="banner" aria-label="site">
            <nav class="region region--full fixed" role="navigation" aria-label="site">
                <a class="skip-link screen-reader-text btn btn--primary" href="#maincontent">Skip to main content</a>
                <header class="column column--full masthead j-masthead full-width">
                    <input type="checkbox" class="hidden toggle--menu j-toggle" id="main-menu">
                    <label class="btn btn--menu j-toggle-label" for="main-menu" tabindex="0">
                        <i class="icon"></i>
                        <span class="screen-reader-text">Main Menu</span>
                    </label>
                    <div class="nav j-main-menu" role="navigation" aria-label="dropdown navigation">
                        <div class="nav__content">



                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-navigation" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-navigation',
                                            adUnitPath: '/2/marketwatch.com/investing/quotes/stock/overview',
                                            adSize: [[280,40]],
                                            adSizeMap: {'at4units':[],'at8units':[[280,40]]},
                                            adTargeting: {'alert':['volatility050','green']},
                                            adLocation: 'NAVSPONSOR',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>

                                <div class="element element--cx side-menu">
                                    <div id="cx-sidemenu"></div>
                                </div>

                            <ul class="list list--navigation j-menu-contents">

                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/">Home</a>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/latest-news">Latest News</a>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/watchlist">Watchlist</a>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/market-data">Market Data Center</a>
                                                    <button class="btn btn--subnav" aria-label="Open Market Data Center sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data/us">U.S.</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data/cryptocurrency">Cryptocurrency</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data/europe">Europe</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data/rates">Rates</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data/asia">Asia</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data/futures">Futures</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data/currencies">Currencies</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/markets">Markets</a>
                                                    <button class="btn btn--subnav" aria-label="Open Markets sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/markets/us">U.S. Markets</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/markets/canada">Canada</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/markets/europe-middle-east">Europe &amp; Middle East</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/markets/asia">Asia</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/markets/emerging-markets">Emerging Markets</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/markets/latin-america">Latin America</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data">Market Data</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/investing">Investing</a>
                                                    <button class="btn btn--subnav" aria-label="Open Investing sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/barrons">Barron&#x27;s</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/best-new-ideas-in-money">Best New Ideas</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/stocks">Stocks</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/ipo">IPOs</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/mutual-funds">Mutual Funds</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/etf">ETFs</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/options">Options</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/bonds">Bonds</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/commodities">Commodities</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/currencies">Currencies</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/cryptocurrency">Cryptocurrencies</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/futures">Futures</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/investing/financial-adviser-center">Financial Adviser Center</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/column/cannabis-watch">Cannabis</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/newswires">Newswires</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/investing/barrons">Barron&#x27;s</a>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/economy-politics">Economy &amp; Politics</a>
                                                    <button class="btn btn--subnav" aria-label="Open Economy &amp; Politics sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/column/washington-watch">Washington Watch</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/economy-politics/inflation">Inflation</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/economy-politics/coronavirus">Coronavirus</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/column/the-fed">The Federal Reserve</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/column/economic-report">Economic Report</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/economy-politics/calendars/economic">U.S. Economic Calendar</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/graphics/coronavirus-economic-recovery-tracker/">Coronavirus Recovery Tracker</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/personal-finance">Personal Finance</a>
                                                    <button class="btn btn--subnav" aria-label="Open Personal Finance sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/column/the-moneyist">The Moneyist</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/personal-finance/spending-saving">Spending &amp; Saving</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/retirement">Retirement</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/column/taxwatch">TaxWatch</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/personal-finance/credit-cards">Credit Cards</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/personal-finance/careers">Careers</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/personal-finance/travel">Travel</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/personal-finance/real-estate">Real Estate</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/personal-finance/real-estate/buy">Real Estate Listings</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/retirement">Retirement</a>
                                                    <button class="btn btn--subnav" aria-label="Open Retirement sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/retirement/best-new-ideas-in-retirement">Best New Ideas in Retirement</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/retirement/estate-planning">Estate Planning</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/column/help-me-retire">Help Me Retire</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/retirement/fire">FIRE</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/retirement/taxes">Taxes</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/retirement/social-security">Social Security</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/retirement/real-estate">Real Estate</a></li>
                                                                    <li class="list__item"><a class="link" href="https://newretirement.marketwatch.com/planner/retirement-calculator?nr_a=mw&amp;nr_creative=snrrc&amp;utm_source=mw&amp;utm_medium=referral&amp;utm_campaign=rc&amp;utm_content=snrrc">Retirement Calculator</a></li>
                                                                    <li class="list__item"><a class="link" href="https://newretirement.marketwatch.com/?nr_a=mw&amp;nr_creative=snrnp&amp;utm_source=mw&amp;utm_medium=referral&amp;utm_campaign=p&amp;utm_content=snrnp">NewRetirement Planner</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/column/where-should-i-retire?mod=retirement">Where Should I Retire</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/graphics/best-place-to-retire/">Best Places</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/how-to-invest">How to Invest</a>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/games">Virtual Stock Exchange</a>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/video">Video</a>
                                                    <button class="btn btn--subnav" aria-label="Open Video sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/marketwatch-25-years">MarketWatch 25 Years</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/sectorwatch">SectorWatch</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/the-moneyist">The Moneyist</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/getting-to-work-with">Getting to Work With</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/explainomics">Explainomics</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/how-to-invest">How to Invest</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/market-brief">MarketBrief</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/fire-starters">Fire Starters</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/how-bad-is-it">How Bad Is It</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/the-cost-of-things">The Cost of Things</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/office-hours">Office Hours</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/best-new-ideas-in-money-festival">Best New Ideas in Money Festival</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/video/mastering-your-money">Mastering Your Money</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/podcasts">Podcasts</a>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/live-qa">Live Events</a>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/newsroom/opinion">Opinion</a>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.investors.com">Investor&#x27;s Business Daily</a>
                                                    <button class="btn btn--subnav" aria-label="Open Investor&#x27;s Business Daily sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://leaderboard.investors.com">Leaderboard</a></li>
                                                                    <li class="list__item"><a class="link" href="https://swingtrader.investors.com">SwingTrader</a></li>
                                                                    <li class="list__item"><a class="link" href="https://marketsmith.investors.com">MarketSmith</a></li>
                                                                    <li class="list__item"><a class="link" href="https://research.investors.com/ibdlive">IBDLive</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item  " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/newsletters">Newsletter Center</a>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/investing/research-tools">Research &amp; Tools</a>
                                                    <button class="btn btn--subnav" aria-label="Open Research &amp; Tools sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/watchlist">Watchlist</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/partner/mortgage-calculator">Mortgage Calculator</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/multiple-quotes">Multiple Quotes Tool</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/stockresearch/screener/">Stock Screener</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/earningscalendar">Earnings Calendar</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/screener">Market Screener</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/ipo-calendar">IPO Calendar</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/screener/short-interest">Short Interest</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/screener/trending-tickers">Trending Tickers Screener</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/screener/premarket">Premarket Screener</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/options-expiration-calendar">Options Expiration Calendar</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/screener/after-hours">After Hours Screener</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/market-data/currencies">Currency Tools</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/screener/mutual-fund">Mutual Fund Screener</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/upgrades-downgrades">Upgrades &amp; Downgrades</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/top-25-mutual-funds">Top 25 Mutual Funds</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/mutual-fund/compare">Mutual Fund Comparison</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/economy-politics/calendars/economic">Economic Calendar</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/graphics/best-place-to-retire/">Where Should I Retire?</a></li>
                                                                    <li class="list__item"><a class="link" href="https://newretirement.marketwatch.com/?nr_a=mw&amp;nr_creative=snrtrp&amp;utm_source=mw&amp;utm_medium=referral&amp;utm_campaign=p&amp;utm_content=snrtrp">Retirement Planner</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/tools/top-25-etfs">Top 25 ETFs</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                                            <li class="list__item has-children " data-click-through="side_nav">
                                                <a class="link" href="https://www.marketwatch.com/picks">MarketWatch Picks</a>
                                                    <button class="btn btn--subnav" aria-label="Open MarketWatch Picks sub menu">
                                                    <i class="icon icon--caret-right"></i>
                                                    </button>
                                                    <div class="subNav">
                                                        <ul class="list list--subsections">
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/picks/loans">Loans</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/picks/money">Money</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/picks/technology">Technology</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/picks/real-estate">Real Estate</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/guides">Guides</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/picks/credit-cards">Credit Cards</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/picks/banking">Banking</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/picks/lifestyle">Lifestyle</a></li>
                                                                    <li class="list__item"><a class="link" href="https://www.marketwatch.com/picks/retirement">Retirement</a></li>
                                                        </ul>
                                                    </div>
                                            </li>
                            </ul>

                            <div class="mobile__profile">
                                <div class="group group--buttons cover">
                                    <a class="btn btn--lighten" href="/sign-up" data-track-query=".btn--signup" data-track-code="MW_Header_Signup"><span class="label">Sign Up</span></a>
                                    <a class="btn btn--primary" href="https://accounts.marketwatch.com/login?target=https%3A%2F%2Fwww.marketwatch.com%2Finvesting%2Fstock%2Faapl" data-track-query=".btn--login" data-track-code="MW_Header_Login"><span class="label">Log In</span></a>
                                </div>

                                <ul class="list list--profile">
                                    
                                        <li class="list__item" data-click-through="side_nav"><a class="link" href="https://www.marketwatch.com/my">Profile Settings</a></li>
                                        <li class="list__item" data-click-through="side_nav"><a class="link" href="https://www.marketwatch.com/newsletters">Email &amp; Alerts</a></li>
                                        <li class="list__item" data-click-through="side_nav"><a class="link" href="https://www.marketwatch.com/watchlist">Watchlist</a></li>
                                        <li class="list__item" data-click-through="side_nav"><a class="link" href="https://www.marketwatch.com/games">Games</a></li>
                                    
                                    
                                </ul>
                            </div>

                        </div>
                    </div>

                        <div class="logo"><a href="https://www.marketwatch.com/" data-track-code="MW_Masthead_Logo"><svg focusable="false" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
            viewBox="0 0 697.5 99.8" style="enable-background:new 0 0 697.5 99.8;" xml:space="preserve" role="img" aria-label="Logo" aria-labelledby="mw-logo-title mw-logo-desc">
            <title id="mw-logo-title">MarketWatch Logo</title>
            <desc id="mw-logo-desc">Go to the homepage.</desc>
        <style type="text/css">
            .mw1{fill:#ffffff;}
            .mw2{fill:#00AC4E;}
        </style>
        <g>
            <g>
                <path class="mw1" d="M168.9,41.8l-1.2,5.9h-0.3c-1.5-3.3-5.7-7.9-15-7.9c-15,0-30.3,11.6-33.7,29.9c-2.9,16,4.8,30.1,22.6,30.1
                    c6.5,0,14-2.5,17.9-8h0.3l-1.1,6H175l10.4-56H168.9z M163.5,69.7c-1.1,5.5-6.3,14.4-16.7,14.4c-10.2,0-12.3-9-11.4-14.2
                    c1.2-6.4,6.9-14.4,16.6-14.4C161.5,55.6,164.7,63.1,163.5,69.7z"/>
                <path class="mw1" d="M194.8,41.8h15.6l-1.1,5.9h0.3c2-2.7,5.9-7.9,15.5-7.9l-3.1,17c-7.9,0.1-13.6,1.7-15.1,10.3l-5.7,30.7h-16.8
                    L194.8,41.8z"/>
                <polygon class="mw1" points="236.4,19.9 253.2,19.9 245.3,62.1 245.6,62.1 265,41.8 284.7,41.8 259.1,66.4 273.8,97.8 254.8,97.8
                    244,70.8 243.7,70.8 238.8,97.8 221.9,97.8 		"/>
                <path class="mw1" d="M311.6,39.8c-17,0-32.1,14.6-34.9,30.2c-3.1,16.6,8.1,29.7,24.2,29.7c5.7,0,11.6-1.7,16.8-5.1
                    c5.3-3.2,10.2-8,14-14.3h-17.1c-2.8,2.9-6,5.2-11.2,5.2c-6.5,0-11.4-3.9-11.1-10.6h42c0.5-1.3,0.8-2.3,1.2-4.4
                    C338.7,53.4,328.7,39.8,311.6,39.8z M294.6,63.6c1.3-3.3,5.9-9.6,14.6-9.6c8.7,0,10.8,6.3,10.8,9.6H294.6z"/>
                <polygon class="mw1" points="96.5,19.9 66.9,64.3 66.7,64.3 66.7,19.9 52.4,19.9 0,97.8 20.3,97.8 49.7,53.4 50,53.4 50,97.8
                    64.4,97.8 93.8,53.4 94.1,53.4 94.1,97.8 110.9,97.8 110.9,19.9 		"/>
                <path class="mw1" d="M378,41.8h-10.6l3.1-16.6h-14.7l-1.2,6.4c-1.3,7.3-5.9,9.5-12,10.2h-0.1L340,54.5h8.3l-8,43.3H357l8-43.3
                    h10.7L378,41.8z"/>
            </g>
            <g>
                <g>
                    <path class="mw2" d="M637.2,76.6c-5.5,12.7-18.6,23.1-33.7,23.1c-17,0-27.5-13.4-24.5-30.1c3.1-16.4,18.3-29.8,35.1-29.8
                        c14.8,0,25,9.9,25.3,23.6h-17c-1.1-3.9-3.6-7.9-10.7-7.9c-7.9-0.4-14.4,6.1-15.9,14.2c-1.5,8.2,2.7,14.3,10.7,14.3
                        c6.9,0,11.1-4,13.5-7.5H637.2z M498.4,0l-32.6,19.9h9.2l-29.5,44.4h-0.3V19.9h-14.4l-29.5,44.4H401V19.9h-16.8v77.9h14.6
                        l29.5-44.4h0.3v44.4h14.4l52.2-77.9h8.3L498.4,0z M530.2,97.8h-16.6l1.1-6h-0.3c-3.9,5.5-11.4,8-17.9,8
                        c-17.8,0-25.5-14-22.6-30.1c3.3-18.3,18.7-29.9,33.7-29.9c9.2,0,13.5,4.5,15,7.9h0.3l1.2-5.9h16.6L530.2,97.8z M502,84.2
                        c10.4,0,15.6-9,16.7-14.4c1.2-6.7-2-14.2-11.5-14.2c-9.6,0-15.4,8-16.6,14.4C489.7,75.2,491.8,84.2,502,84.2L502,84.2z
                        M582.5,41.8H572l3.1-16.6h-14.7l-1.2,6.4c-1.3,7.3-5.9,9.5-12,10.2H547l-2.4,12.7h8.3l-8,43.3h16.7l8-43.3h10.7L582.5,41.8z
                        M653,19.9h16.7l-5.1,27.8h0.3c3.6-5.2,8.4-7.9,15.8-7.9c5.3,0,11.4,2,14.2,6.3c3.6,5.5,3.2,10.4,1.3,20.4l-5.7,31.3h-16.7
                        l5.6-30.5c0.5-2.7,2.1-11.8-6.8-11.8c-9.4,0-11,8.4-11.5,11.2l-5.7,31h-16.7L653,19.9z"/>
                </g>
            </g>
        </g>
        </svg>
        </a></div>


                        <ul id="nav__menu" class="list list--menu j-list">
                                <li class="menu__item" data-section="latest-news" data-click-through="top_nav"><a href="https://www.marketwatch.com/latest-news">Latest</a></li>
                                <li class="menu__item" data-section="watchlist" data-click-through="top_nav"><a href="https://www.marketwatch.com/watchlist">Watchlist</a></li>
                                <li class="menu__item" data-section="markets" data-click-through="top_nav"><a href="https://www.marketwatch.com/markets">Markets</a></li>
                                <li class="menu__item" data-section="investing" data-click-through="top_nav"><a href="https://www.marketwatch.com/investing">Investing</a></li>
                                <li class="menu__item" data-section="personal-finance" data-click-through="top_nav"><a href="https://www.marketwatch.com/personal-finance">Personal Finance</a></li>
                                <li class="menu__item" data-section="economy-politics" data-click-through="top_nav"><a href="https://www.marketwatch.com/economy-politics">Economy</a></li>
                                <li class="menu__item" data-section="retirement" data-click-through="top_nav"><a href="https://www.marketwatch.com/retirement">Retirement</a></li>
                                <li class="menu__item" data-section="how-to-invest" data-click-through="top_nav"><a href="https://www.marketwatch.com/how-to-invest">How to Invest</a></li>
                                <li class="menu__item" data-section="video" data-click-through="top_nav"><a href="https://www.marketwatch.com/video">Video Center</a></li>
                                <li class="menu__item" data-section="live-qa" data-click-through="top_nav"><a href="https://www.marketwatch.com/live-qa">Live Events</a></li>
                                <li class="menu__item" data-section="picks" data-click-through="top_nav"><a href="https://www.marketwatch.com/picks">MarketWatch Picks</a></li>
                            <li class="menu__item item--more">
                                <button class="more__btn j-more__btn">More</button>
                                <div id="j-nav__more" class="more__dropdown j-more__dropdown">
                                </div>
                            </li>
                        </ul>

                    <div class="element element--cx top-menu">
                        <div id="cx-header"></div>
                    </div>

                    

                    <div class="profile logged-out">
                        <input class="hidden toggle--profile j-toggle" type="checkbox" id="toggle--profile" />
                        <label class="btn--text btn--profile j-toggle-label" for="toggle--profile" title="Toggle account settings menu" tabindex="0">
                        <span class="screen-reader-text">Account Menu</span>
                        </label>
                        <ul class="profile__menu j-menu-contents j-toggle--profile">
                            <li class="profile__item profile--name divider">Account Settings</li>
                            <li class="profile__item"><a class="link js-btn--login" href="https://accounts.marketwatch.com/login?target=https%3A%2F%2Fwww.marketwatch.com%2Finvesting%2Fstock%2Faapl" data-track-query=".btn--login" data-track-code="MW_Header_Login">Log In</a></li>
                            <li class="profile__item"><a class="link" href="/sign-up" data-track-query=".btn--signup" data-track-code="MW_Header_Signup">Sign Up</a></li>
                        </ul>
                    </div>

                    <button class="btn btn--lighten btn--search j-btn-search"   data-track-query="" data-track-code="Search" aria-label="open site search">
                    <span class="screen-reader-text">Open Site Search</span>
                    </button>
                    <button class="toggle--overlay j-search-close">
                        <span class="screen-reader-text">Close Search Overlay</span>
                        <span class="line line--left"></span>
                        <span class="line line--right"></span>
                    </button>

                </header>
            


        <div class="column column--full bulletins full-width has-ad">


        </div>
                <template id="bulletinTemplate">
                    <mw-expires class="bulletin" duration="0">
                        <h3 class="bulletin__headline" data-click-through="bnbh">
                            <a class="link" href=""></a>
                            <span class="text"></span>
                        </h3>
                        <i class="icon icon--close"></i>
                    </mw-expires>
                </template>

            </nav>
            <div class="region region--full bulletins-mobile">


        <div class="column column--full bulletins full-width has-ad">


        </div>
            </div>
            <div class="region region--full masthead-elements" role="region" aria-label="markets summary">
                
                
            </div>
        </section>
        <div id="cx-banner"></div>

            <section class="container container--banner banner--recap hidden">
                <div class="region region--full">
                    <div class="column column--full">
                        <div class="element element--banner j-watchlist-banner-container">


                        </div>
                        <template id="watchlistBannerTemplate">
                            <mw-expires class="banner__content j-watchlist-banner" duration="0">
                                <h3 class="banner__headline" data-click-through="wlx">
                                    <a class="link" href=""></a>
                                </h3>
                                <i class="icon icon--close"></i>
                            </mw-expires>
                        </template>
                    </div>
                </div>
            </section>


            <div id="j-qt-placeholder"></div>


            <script type="application/ld+json">
            {
                "@context":"http://schema.org/","@type":"Intangible/FinancialQuote","name":"Apple Inc.","tickerSymbol":"AAPL","exchange":"U.S.: Nasdaq","price":"163.17","priceCurrency":"USD","priceChange":"0.81","priceChangePercent":"0.50%","quoteTime":"Mar 31, 2023 11:39 a.m. ","url":"https://www.marketwatch.com/investing/stock/aapl"
            }
            </script>

            <div id="maincontent" class="container container--body" role="main">


                    <div class="">


                    <div class="region region--full m-hide ad--banner">


                    <div class="column column--full">





                        <div class="element element--ad is-loading">
                            <div id="ad-banner" class="j-ad">
                                <script>
                                    !function() {
                                        window.__mwads = window.__mwads || {};
                                        window.__mwads.uacQ = window.__mwads.uacQ || [];
                                        window.__mwads.uacQ.push({
                                            options: {
                                                adActivate: true,
                                                adId: 'ad-banner',
                                                adUnitPath: '/2/marketwatch.com/investing/quotes/stock/overview',
                                                adSize: [[728,90],[970,90],[970,66],[970,250]],
                                                adSizeMap: {'at4units':[],'at12units':[[728,90],[970,90],[970,66],[970,250]]},
                                                adTargeting: {'alert':['volatility050','green']},
                                                adLocation: 'BANNERTOP',
                                                isObserve: !false,
                                                observeFromUAC: !false,
                                                triggerPrebid: true,
                                                moatEnabled: true,
                                                collapseAdBeforeFetch: true,
                                                threshold: 0.01
                                            }
                                        });
                                    }();
                                </script>
                            </div>
                        </div>
                    </div>
                    </div>
                    <div class="region region--full market--collapse">


                    <div class="column column--full">





        <div class="market__data masthead-elements collapsed">
        <div class="element element--movers">
                <div class="data__toggle j-collapseToggle" data-track-query="" data-track-code="MarketData_Header_Expand">
                    <i class="icon icon--angle-up"></i>
                    <button class="toggle__btn" type="button" name="market data" >Market Data</button>
                </div>
                <div class="header header--small">
                    <span class="primary">S&amp;P 500 Movers</span>
                </div>
                <ul class="list list--mover left" data-track-query="a.list__item">
                            <li class="mover__item">
                                <a class="link" data-track-code="MW_Header_Movers_ALGN" href="https://www.marketwatch.com/investing/stock/algn">
                                    <span class="mover__symbol">ALGN</span>
                                    <bg-quote field="percentChange" format="0,0.0" class="positive">4.6</bg-quote>
                                </a>
                            </li>
                            <li class="mover__item">
                                <a class="link" data-track-code="MW_Header_Movers_TSLA" href="https://www.marketwatch.com/investing/stock/tsla">
                                    <span class="mover__symbol">TSLA</span>
                                    <bg-quote field="percentChange" format="0,0.0" class="positive">3.9</bg-quote>
                                </a>
                            </li>
                            <li class="mover__item">
                                <a class="link" data-track-code="MW_Header_Movers_NOW" href="https://www.marketwatch.com/investing/stock/now">
                                    <span class="mover__symbol">NOW</span>
                                    <bg-quote field="percentChange" format="0,0.0" class="positive">3.8</bg-quote>
                                </a>
                            </li>
                            <li class="mover__item">
                                <a class="link" data-track-code="MW_Header_Movers_SEDG" href="https://www.marketwatch.com/investing/stock/sedg">
                                    <span class="mover__symbol">SEDG</span>
                                    <bg-quote field="percentChange" format="0,0.0" class="positive">3.5</bg-quote>
                                </a>
                            </li>
                            <li class="mover__item">
                                <a class="link" data-track-code="MW_Header_Movers_MU" href="https://www.marketwatch.com/investing/stock/mu">
                                    <span class="mover__symbol">MU</span>
                                    <bg-quote field="percentChange" format="0,0.0" class="negative mover__percent">-2.8</bg-quote>
                                </a>
                            </li>
                            <li class="mover__item">
                                <a class="link" data-track-code="MW_Header_Movers_GNRC" href="https://www.marketwatch.com/investing/stock/gnrc">
                                    <span class="mover__symbol">GNRC</span>
                                    <bg-quote field="percentChange" format="0,0.0" class="negative mover__percent">-2.7</bg-quote>
                                </a>
                            </li>
                            <li class="mover__item">
                                <a class="link" data-track-code="MW_Header_Movers_VTR" href="https://www.marketwatch.com/investing/stock/vtr">
                                    <span class="mover__symbol">VTR</span>
                                    <bg-quote field="percentChange" format="0,0.0" class="negative mover__percent">-2.7</bg-quote>
                                </a>
                            </li>
                            <li class="mover__item">
                                <a class="link" data-track-code="MW_Header_Movers_ZION" href="https://www.marketwatch.com/investing/stock/zion">
                                    <span class="mover__symbol">ZION</span>
                                    <bg-quote field="percentChange" format="0,0.0" class="negative mover__percent">-2.7</bg-quote>
                                </a>
                            </li>
                </ul>

            <template id="moverItemTemplate">
                <li class="mover__item">
                    <a class="link" data-track-code="">
                        <span class="mover__symbol"></span>
                    </a>
                </li>
            </template>
        </div>

        <div class="group group--collapse">

            <div class="element element--markets desktop j-collapse">
                    <ul class="j-dropdown--expanded-markets list list--markets horizontal" data-track-query="a" data-section-tracking-tag="">
                            <li class="j-option market__item option "><a href="https://www.marketwatch.com/markets/us" data-track-code="MW_Header_Market Data_Tab_US">US</a></li>
                            <li class="j-option market__item option "><a href="https://www.marketwatch.com/markets/europe-middle-east" data-track-code="MW_Header_Market Data_Tab_Europe">Europe</a></li>
                            <li class="j-option market__item option is-selected"><a href="https://www.marketwatch.com/markets/asia" data-track-code="MW_Header_Market Data_Tab_Asia">Asia</a></li>
                            <li class="j-option market__item option "><a href="https://www.marketwatch.com/investing/currencies" data-track-code="MW_Header_Market Data_Tab_FX">FX</a></li>
                            <li class="j-option market__item option "><a href="https://www.marketwatch.com/investing/bonds" data-track-code="MW_Header_Market Data_Tab_Rates">Rates</a></li>
                            <li class="j-option market__item option "><a href="https://www.marketwatch.com/investing/futures" data-track-code="MW_Header_Market Data_Tab_Futures">Futures</a></li>
                            <li class="j-option market__item option "><a href="https://www.marketwatch.com/investing/cryptocurrency" data-track-code="MW_Header_Market Data_Tab_Crypto">Crypto</a></li>
                        <li class="market__item dropdown">
                            <small class="label">Range</small>
                            <i class="icon"></i>
                            <label for="dropdownmarkets" class="screen-reader-text">Dropdown Markets</label>
                            <select id="dropdownmarkets" class="dropdown dropdown--markets" track>
                                <option selected value="D1" data-track-code="MW_Header_Market Data_Date Range_1D">1D</option>
                                <option value="D5" data-track-code="MW_Header_Market Data_Date Range_5D">5D</option>
                                <option value="P29D" data-track-code="MW_Header_Market Data_Date Range_1M">1M</option>
                                <option value="P3M" data-track-code="MW_Header_Market Data_Date Range_3M">3M</option>
                                <option value="P6M" data-track-code="MW_Header_Market Data_Date Range_6M">6M</option>
                                <option value="P1Y" data-track-code="MW_Header_Market Data_Date Range_1Y">1Y</option>
                                <option value="P2Y" data-track-code="MW_Header_Market Data_Date Range_2Y">2Y</option>
                            </select>
                        </li>
                    </ul>
                    <div class="markets--desktop" data-track-query="a">
                        <div class="markets__table">
                            <table class="table table--primary align--right">
                                <tbody class="markets__group">


                    <tr onclick="this.querySelector('a').click();" class="table__row index is-active" is="bg-gavel" data-charting-symbol="INDEX/XX//ADOW">
                        <td class="table__cell">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/211618636/realtime"><span class="indicator"></span></bg-quote>
                        </td>
                        <td class="table__cell symbol"><a data-track-code="MW_Header_Market Data_Quote Click_The Asia Dow Index USD" href="https://www.marketwatch.com/investing/index/adow?countrycode=xx">Asia Dow</a></td>
                        <td class="table__cell price">
                            <bg-quote class="ignore-color" field="last" format="0,0.00" channel="/zigman2/quotes/211618636/realtime">3,419.38</bg-quote>
                        </td>
                        <td class="table__cell change">
                            <bg-quote class="positive" field="change" format="0,0.00" channel="/zigman2/quotes/211618636/realtime">37.54</bg-quote>
                        </td>
                        <td class="table__cell percent">
                            <bg-quote class="positive" field="percentchange" format="0.00%" channel="/zigman2/quotes/211618636/realtime">1.11%</bg-quote>
                        </td>
                        <td class="table__cell arrow">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/211618636/realtime">
                                <i class="icon"></i>
                            </bg-quote>
                        </td>
                    </tr>
                    <tr onclick="this.querySelector('a').click();" class="table__row index is-closed" is="bg-gavel" data-charting-symbol="INDEX/JP/XTKS/NIK">
                        <td class="table__cell">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210597971/delayed"><span class="indicator"></span></bg-quote>
                        </td>
                        <td class="table__cell symbol"><a data-track-code="MW_Header_Market Data_Quote Click_NIKKEI 225 Index" href="https://www.marketwatch.com/investing/index/nik?countrycode=jp">Nikkei 225</a></td>
                        <td class="table__cell price">
                            <bg-quote class="ignore-color" field="last" format="0,0.00" channel="/zigman2/quotes/210597971/delayed">28,041.48</bg-quote>
                        </td>
                        <td class="table__cell change">
                            <bg-quote class="positive" field="change" format="0,0.00" channel="/zigman2/quotes/210597971/delayed">258.55</bg-quote>
                        </td>
                        <td class="table__cell percent">
                            <bg-quote class="positive" field="percentchange" format="0.00%" channel="/zigman2/quotes/210597971/delayed">0.93%</bg-quote>
                        </td>
                        <td class="table__cell arrow">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210597971/delayed">
                                <i class="icon"></i>
                            </bg-quote>
                        </td>
                    </tr>
                    <tr onclick="this.querySelector('a').click();" class="table__row index is-closed" is="bg-gavel" data-charting-symbol="INDEX/HK/XHKG/HSI">
                        <td class="table__cell">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210598030/delayed"><span class="indicator"></span></bg-quote>
                        </td>
                        <td class="table__cell symbol"><a data-track-code="MW_Header_Market Data_Quote Click_Hang Seng Index" href="https://www.marketwatch.com/investing/index/hsi?countrycode=hk">Hang Seng</a></td>
                        <td class="table__cell price">
                            <bg-quote class="ignore-color" field="last" format="0,0.00" channel="/zigman2/quotes/210598030/delayed">20,400.11</bg-quote>
                        </td>
                        <td class="table__cell change">
                            <bg-quote class="positive" field="change" format="0,0.00" channel="/zigman2/quotes/210598030/delayed">90.98</bg-quote>
                        </td>
                        <td class="table__cell percent">
                            <bg-quote class="positive" field="percentchange" format="0.00%" channel="/zigman2/quotes/210598030/delayed">0.45%</bg-quote>
                        </td>
                        <td class="table__cell arrow">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210598030/delayed">
                                <i class="icon"></i>
                            </bg-quote>
                        </td>
                    </tr>
                    <tr onclick="this.querySelector('a').click();" class="table__row index is-closed" is="bg-gavel" data-charting-symbol="INDEX/CN/XSHG/SHCOMP">
                        <td class="table__cell">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210598127/delayed"><span class="indicator"></span></bg-quote>
                        </td>
                        <td class="table__cell symbol"><a data-track-code="MW_Header_Market Data_Quote Click_Shanghai Composite Index" href="https://www.marketwatch.com/investing/index/shcomp?countrycode=cn">Shanghai</a></td>
                        <td class="table__cell price">
                            <bg-quote class="ignore-color" field="last" format="0,0.00" channel="/zigman2/quotes/210598127/delayed">3,272.86</bg-quote>
                        </td>
                        <td class="table__cell change">
                            <bg-quote class="positive" field="change" format="0,0.00" channel="/zigman2/quotes/210598127/delayed">11.61</bg-quote>
                        </td>
                        <td class="table__cell percent">
                            <bg-quote class="positive" field="percentchange" format="0.00%" channel="/zigman2/quotes/210598127/delayed">0.36%</bg-quote>
                        </td>
                        <td class="table__cell arrow">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210598127/delayed">
                                <i class="icon"></i>
                            </bg-quote>
                        </td>
                    </tr>
                    <tr onclick="this.querySelector('a').click();" class="table__row index is-closed" is="bg-gavel" data-charting-symbol="INDEX/IN/XBOM/1">
                        <td class="table__cell">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210597966/delayed"><span class="indicator"></span></bg-quote>
                        </td>
                        <td class="table__cell symbol"><a data-track-code="MW_Header_Market Data_Quote Click_S&amp;P BSE Sensex Index" href="https://www.marketwatch.com/investing/index/1?countrycode=in">Sensex</a></td>
                        <td class="table__cell price">
                            <bg-quote class="ignore-color" field="last" format="0,0.00" channel="/zigman2/quotes/210597966/delayed">58,991.52</bg-quote>
                        </td>
                        <td class="table__cell change">
                            <bg-quote class="positive" field="change" format="0,0.00" channel="/zigman2/quotes/210597966/delayed">1,031.43</bg-quote>
                        </td>
                        <td class="table__cell percent">
                            <bg-quote class="positive" field="percentchange" format="0.00%" channel="/zigman2/quotes/210597966/delayed">1.78%</bg-quote>
                        </td>
                        <td class="table__cell arrow">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210597966/delayed">
                                <i class="icon"></i>
                            </bg-quote>
                        </td>
                    </tr>
                    <tr onclick="this.querySelector('a').click();" class="table__row index is-closed" is="bg-gavel" data-charting-symbol="INDEX/SG/XSES/STI">
                        <td class="table__cell">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210597985/delayed"><span class="indicator"></span></bg-quote>
                        </td>
                        <td class="table__cell symbol"><a data-track-code="MW_Header_Market Data_Quote Click_FTSE Straits Times Index" href="https://www.marketwatch.com/investing/index/sti?countrycode=sg">Singapore</a></td>
                        <td class="table__cell price">
                            <bg-quote class="ignore-color" field="last" format="0,0.00" channel="/zigman2/quotes/210597985/delayed">3,258.90</bg-quote>
                        </td>
                        <td class="table__cell change">
                            <bg-quote class="positive" field="change" format="0,0.00" channel="/zigman2/quotes/210597985/delayed">1.72</bg-quote>
                        </td>
                        <td class="table__cell percent">
                            <bg-quote class="positive" field="percentchange" format="0.00%" channel="/zigman2/quotes/210597985/delayed">0.05%</bg-quote>
                        </td>
                        <td class="table__cell arrow">
                            <bg-quote tick="100" class="positive" channel="/zigman2/quotes/210597985/delayed">
                                <i class="icon"></i>
                            </bg-quote>
                        </td>
                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="markets__chart is-loading">
                            <div id="market-overview-chart"></div>
                        </div>
                    </div>
            </div>

            <div class="element element--latestNews">
                    <mw-latest-news>
                        <div class="header header--small">
                            <a class="primary link" href="https://www.marketwatch.com/newsviewer">Latest News</a>
                            <small class="secondary">All Times Eastern</small>
                            <div class="group group--buttons">
                                <button class="scroll-up js-scroll-up">
                                <i class="icon"></i>
                                <span class="screen-reader-text">scroll up</span>
                                </button>
                                <button class="scroll-down js-scroll-down">
                                <i class="icon"></i>
                                <span class="screen-reader-text">scroll down</span>
                                </button>
                            </div>
                        </div>
                        <div class="latestNews__wrapper j-scrollViewport">
                            <ul class="latestNews j-scrollElement" data-track-query=".latestNews__headline a|a.icon--facebook|a.icon--twitter" data-track-code="MW_Header_Latest News|MW_Header_Latest News_Facebook|MW_Header_Latest News_Twitter">
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736080">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/story/what-is-an-indictment-and-what-does-being-indicted-mean-for-trump-legal-terms-explained-f4b0cc7a?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:33:00" pubdate>11:33a</time>
                                                    <span class="headline">
                                                        What is an indictment, and what does being indicted mean for Trump? Legal terms explained.
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736079">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/story/the-explosive-ai-trend-is-here-to-stay-these-stocks-are-poised-to-benefit-82aed67d?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:33:00" pubdate>11:33a</time>
                                                    <span class="headline">
                                                        The &#x2018;explosive&#x2019; AI trend is here to stay. These stocks are poised to benefit.
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736077">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/story/40-of-americans-are-still-earning-less-than-1-on-their-savings-accounts-yet-some-banks-are-offering-3-to-4-ab631085?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:29:00" pubdate>11:29a</time>
                                                    <span class="headline">
                                                        40% of Americans are missing the chance to earn hundreds &#x2014; if not thousands &#x2014; of dollars in interest each year
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736075">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/story/trump-set-to-surrender-tuesday-heres-whats-next-after-his-indictment-60a11ac5?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:28:00" pubdate>11:28a</time>
                                                    <span class="headline">
                                                        Trump set to surrender Tuesday &#x2014; here&#x2019;s what&#x2019;s next after his indictment
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736074">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/data-news/intel-home-depot-share-gains-contribute-to-dow-s-nearly-250-point-climb-6b4b18a1?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:25:00" pubdate>11:25a</time>
                                                    <span class="headline">
                                                            <small class="latestNews__label breaking">Breaking</small>
                                                        Intel, Home Depot share gains contribute to Dow&#x27;s nearly 250-point climb
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736073">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/story/virgin-galactic-stock-gains-even-as-virgin-orbit-shares-plunge-after-cutting-most-of-its-staff-8e018b1f?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:20:00" pubdate>11:20a</time>
                                                    <span class="headline">
                                                        Virgin Galactic stock gains, even as Virgin Orbit shares plunge after cutting most of its staff
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736072">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/story/east-palestine-derailment-norfolk-southern-sued-by-justice-department-and-epa-aafa2125?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:20:00" pubdate>11:20a</time>
                                                    <span class="headline">
                                                        East Palestine derailment: Norfolk Southern sued by Justice Department and EPA
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736071">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/story/trump-indictment-draws-lock-him-up-cheers-and-it-is-un-american-jeers-online-cb50b861?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:19:00" pubdate>11:19a</time>
                                                    <span class="headline">
                                                        Trump indictment draws &#x2018;lock him up&#x2019; cheers and &#x2018;it is un-American&#x2019; jeers online
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736069">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/articles/block-stock-short-seller-claims-baeceae1?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:16:00" pubdate>11:16a</time>
                                                    <span class="headline">
                                                            <small class="latestNews__label barrons">Barron&#x27;s</small>
                                                        Block&#x2019;s Answer to Short-Seller Claims Gets Approval. Wall Street Still Likes the Stock.
                                                    </span>
                                                </a>
                                            </li>
                                            <li class="latestNews__item" data-sequence="8c077dc4-5ad2-4f73-b9c3-a381c5fece05" data-number="1736068">
                                                <a class="latestNews__headline" href="https://www.marketwatch.com/story/bank-stocks-end-tough-quarter-with-mixed-trades-as-sector-stabilizes-despite-outflows-from-savings-accounts-8ee4768b?mod=mw_latestnews">
                                                    <time class="latestNews__time" datetime="03/31/2023 15:09:00" pubdate>11:09a</time>
                                                    <span class="headline">
                                                        Bank stocks end tough quarter with mixed trades as sector stabilizes despite outflows from savings accounts
                                                    </span>
                                                </a>
                                            </li>
                                <li class="latestNews__loading is-loading"></li>
                            </ul>
                        </div>
                    </mw-latest-news>
                    <template id="latestNewsItemTemplate">
                        <li class="latestNews__item">
                            <time class="latestNews__time" datetime="" pubdate></time>
                            <h3 class="latestNews__headline" data-click-through="mw_latestnews">
                                <a class="link" href="#"><small class="latestNews__label"></small>to be replaced</a>
                            </h3>
                        </li>
                    </template>
            </div>

        </div>
        </div>
                    </div>
                    </div>
                    </div>
                    <div class="region region--intraday">


                    <div class="column column--full quote__nav">




                <ol class="list list--breadcrumbs" itemscope itemtype="http://schema.org/BreadcrumbList">
                                <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
                                    <a class="link" itemprop="item" href="https://www.marketwatch.com/">
                                        <span itemprop="name">Home</span>
                                    </a>
                                    <meta itemprop="position" content="1" />
                                </li>
                                <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
                                    <a class="link" itemprop="item" href="https://www.marketwatch.com/investing">
                                        <span itemprop="name">Investing</span>
                                    </a>
                                    <meta itemprop="position" content="2" />
                                </li>
                                <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
                                    <a class="link" itemprop="item" href="https://www.marketwatch.com/tools/markets">
                                        <span itemprop="name">Quotes</span>
                                    </a>
                                    <meta itemprop="position" content="3" />
                                </li>
                                <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
                                    <a class="link" itemprop="item" href="https://www.marketwatch.com/tools/markets/stocks">
                                        <span itemprop="name">Stocks</span>
                                    </a>
                                    <meta itemprop="position" content="4" />
                                </li>
                                <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
                                    <a class="link" itemprop="item" href="https://www.marketwatch.com/tools/markets/stocks/country/united-states">
                                        <span itemprop="name">United States</span>
                                    </a>
                                    <meta itemprop="position" content="5" />
                                </li>
                                <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
                                    <a class="link" itemprop="item" href="https://www.marketwatch.com/investing/stock/aapl">
                                        <span itemprop="name">AAPL</span>
                                    </a>
                                    <meta itemprop="position" content="6" />
                                </li>
                                <li class="breadcrumb__item" itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
                                    <a class="link" itemprop="item">
                                        <span itemprop="name">Overview</span>
                                    </a>
                                    <meta itemprop="position" content="7" />
                                </li>
                </ol>


                <ul class="list list--topics horizontal">
                            <li class="topic__item"><a class="link" href="https://www.marketwatch.com/tools/screener/stock">Stock Screener</a></li>
                            <li class="topic__item"><a class="link" href="https://www.marketwatch.com/tools/earningscalendar">Earnings Calendar</a></li>
                            <li class="topic__item"><a class="link" href="https://www.marketwatch.com/tools/industry/">Sectors</a></li>
                            <li class="topic__item"><a class="link" href="https://www.marketwatch.com/tools/screener/market?exchange=nasdaq&subreport=MostActive">Nasdaq</a></li>
                </ul>
                    </div>
                    <div class="column column--full">






            <div class="element element--company">
                <div class="row">
                    <div class="search__quote j-search-quote">
                        <label class="screen-reader-text" for="searchticker">Search Ticker</label>
                        <input id="searchticker" class="search__ticker j-search-ticker" type="text" is="mw-autocomplete" custom data-need="symbol" placeholder="Switch Quote" data-action="" data-track-payload='{"link_text":"switch_quote"}' />
                        <div class="search__quote__results j-search-results j-hidden">
                            <ul class="search__quote__container j-search-container" data-track-query=".j-ticker"></ul>
                        </div>
                        <template id="quoteTitleSearchItem">
                            <li class="search__item">
                                <a class="link j-link" data-track-payload='{"link_text":"switch_quote"}'>
                                    <div class="ticker j-ticker"></div>
                                </a>
                            </li>
                        </template>
                        <span class="search__divider">|</span>
                    </div>
                    <div class="company__symbol">
                        <span class="company__ticker">AAPL</span>
                            <span class="company__market">U.S.: Nasdaq</span>
                    </div>
                    <span class="company__ad">


                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-company-title" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-company-title',
                                            adUnitPath: '/2/marketwatch.com/investing/quotes/stock/overview',
                                            adSize: [[160,21]],
                                            adSizeMap: {'at4units':[],'at8units':[[160,21]]},
                                            adTargeting: {'alert':['volatility050','green']},
                                            adLocation: '',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>
                    </span>
                </div>
                <div class="row">
                    <h1 class="company__name">Apple Inc.</h1>
                    <div class="quote-actions" data-track-query=".btn">
                        <a class="btn btn--primary watchlist-add"
                            data-track-payload='{"link_text":"watchlist_add", "quote_company_name":"Apple Inc."}'
                            href="https://www.marketwatch.com/watchlist?mod=mw_quote_addwatchlist" aria-label="add AAPL to watchlist">Watch<span class="text">list</span></a> <!-- NEEDS TO BE HOOKED UP -->
                        <a class="btn btn--outline create-alert" data-track-payload='{"link_text":"alert_create", "quote_company_name":"Apple Inc."}' href="https://www.marketwatch.com/tools/alerts/priceVolume.asp?selectedType=0&alertsymbol=AAPL">Create<strong>AAPL</strong>Alert</a>
                    </div>
                </div>
            </div>
                    </div>
                    <div class="column column--aside">




            <div class="element element--intraday">
                        <small class="intraday__status status--open"><span class="company__ticker">AAPL</span><span class="company__market">US</span><i class="icon--sun"></i><div class="status">Open</div></small>
                        <div class="intraday__timestamp">
                            <span class="timestamp__time">Last Updated: <bg-quote field="date" channel="/zigman2/quotes/202934861/composite,/zigman2/quotes/202934861/lastsale">Mar 31, 2023 11:39 a.m. </bg-quote> EDT</span>
                            <small class="timestamp__type">Real time quote</small>
                        </div>
                        <div class="intraday__data">
                            <h2 class="intraday__price ">
                                <sup class="character">$</sup>
                                <bg-quote class="value" field="Last" format="0,0.00" channel="/zigman2/quotes/202934861/composite,/zigman2/quotes/202934861/lastsale">163.17</bg-quote>
                            </h2>
                            <bg-quote channel="/zigman2/quotes/202934861/composite" class="intraday__change positive">
                                <i class="icon--caret"></i>
                                <span class="change--point--q"><bg-quote field="change" format="0,0.00" channel="/zigman2/quotes/202934861/composite">0.81</bg-quote></span>
                                <span class="change--percent--q"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/202934861/composite">0.50%</bg-quote></span>
                            </bg-quote>
                        </div>
                    <div class="intraday__close">
                        <table class="table table--primary align--right">
                            <thead>
                                <tr class="table__row">
                                        <th class="table__heading">Previous Close</th>
                                </tr>
                            </thead>
                            <tbody class="remove-last-border">
                                <tr class="table__row">
                                    <td class="table__cell u-semi">$162.36</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                <div class="intraday__ad">


                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-market-data-underlay" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-market-data-underlay',
                                            adUnitPath: '/2/marketwatch.com/investing/quotes/stock/overview/underlay',
                                            adSize: [[160,20]],
                                            adSizeMap: {'at4units':[],'at8units':[[160,20]]},
                                            adTargeting: {'pos':['underlay'],'alert':['volatility050','green']},
                                            adLocation: 'QUOTEUNDERLAY',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>
                </div>
            </div>
                    </div>
                    <div class="column column--primary">




            <mw-chart class="element element--chart Stock" data-is-after-hours="False" data-is-before-hours="False" data-country-code="US" data-ticker="STOCK/US/XNAS/AAPL" data-price-history-start-date="01/01/0001 00:00:00" data-instrument-type="Stock" data-is-mobile="False">
                <i class="loading-spinner"></i>
                <div class="chart__figure">
                    <div id="mikey-chart"></div>
                </div>
                <input type="checkbox" id="toggle--chart" style="display: none;">
                <label class="toggle--chart" for="toggle--chart"><span class="screen-reader-text">Toggle Chart Options</span></label>
                <div class="chart__options" data-track-query="a.chart__customize" data-track-code="advanced_chart">
                    <a instrument-target="charts" class="chart__customize" data-track-payload='{"event_name":"advanced_chart", "quote_company_name":"Apple Inc."}' href="https://www.marketwatch.com/investing/stock/aapl/charts?mod=mw_quote_advanced">Advanced Charting</a>
                    <div class="chart__range">
                        <select id="range-dropdown" class="dropdown dropdown--chart" track>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "1D"}' value="D1">1D</option>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "5D"}' value="D5">5D</option>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "1M"}' value="P29D">1M</option>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "3M"}' value="P3M">3M</option>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "6M"}' value="P6M">6M</option>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "YTD"}' value="YTD">YTD</option>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "1Y"}' value="P1Y">1Y</option>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "3Y"}' value="P3Y">3Y</option>
                            <option data-track-payload='{"event_name" :"chart_timerange","chart_timerange" : "All"}' value="ALL">All</option>
                        </select>
                        <label for="range-dropdown"><i class="icon icon--caret-down"></i><span class="screen-reader-text">Range Dropdown</span></label>
                    </div>
                    <div id="percent-toggle" class="chart__toggle" data-track-query=".toggle__value" data-track-code="chart_type">
                        <button id="percent-toggle-last" class="toggle__value is-selected" data-track-payload='{"event_name":"chart_type", "chart_type" :"price"}'>$</button>
                        <button id="percent-toggle-percent" class="toggle__value" data-track-payload='{"event_name":"chart_type", "chart_type" :"percentage"}'>%</button>
                        <button id="percent-toggle-volume" class="toggle__value volume">Vol</button>
                    </div>
                </div>
            </mw-chart>
                    </div>
                    <div class="column column--full supportive-data">




            <mw-rangeBar class="element element--range range--volume" day-open="0" bar-low="0" bar-high="15583301.0" range-low="0" range-high="138764398.0923076" average="69382199.0461538" quote-channel="/zigman2/quotes/202934861/composite">
                <div class="range__header">
                    <span class="primary">Volume: 15.58M</span>
                    <span class="secondary">65 Day Avg: 69.38M</span>
                </div>
                <div class="range__container">
                    <div class="range__bar" style="width: 11.230042586019662773925134430%;">
                        22% vs Avg
                    </div>
                </div>
            </mw-rangeBar>


                <mw-rangeBar precision="2" day-open="162.44" bar-low="161.91" bar-high="163.17" range-low="161.91" range-high="163.17" quote-channel="/zigman2/quotes/202934861/composite" class="element element--range range--daily">
                    <div class="range__header">
                        <span class="primary">161.91</span>
                        <span class="secondary">Day Range</span>
                        <span class="primary">163.17</span>
                    </div>
                    <div class="range__container">
                        <div class="indicator-zone">
                            <span class="indicator indicator--daily" style="left: 100%"></span>
                        </div>
                    </div>
                </mw-rangeBar>


                <mw-rangeBar precision="2" day-open="162.44" bar-low="124.17" bar-high="178.49" range-low="124.17" range-high="178.49" quote-channel="/zigman2/quotes/202934861/composite" class="element element--range range--yearly">
                    <div class="range__header">
                        <span class="primary">124.17</span>
                        <span class="secondary">52 Week Range</span>
                        <span class="primary">178.49</span>
                    </div>
                    <div class="range__container">
                        <div class="indicator-zone">
                            <div class="indicator indicator--yearly" style="left: 71.796759941089837997054491900%;"></div>
                        </div>
                    </div>
                </mw-rangeBar>
                    </div>
                    </div>
                    
                    <div class="region region--aside">


                    <div class="column column--full">





                        <div class="element element--ad is-loading">
                            <div id="ad-display-ad" class="j-ad">
                                <script>
                                    !function() {
                                        window.__mwads = window.__mwads || {};
                                        window.__mwads.uacQ = window.__mwads.uacQ || [];
                                        window.__mwads.uacQ.push({
                                            options: {
                                                adActivate: true,
                                                adId: 'ad-display-ad',
                                                adUnitPath: '/2/marketwatch.com/investing/quotes/stock/overview',
                                                adSize: [[300,250]],
                                                adSizeMap: {'at4units':[],'at8units':[[300,250],[414,320],[1,6],[1,7]],'at12units':[[300,250],[300,600],[300,1050]]},
                                                adTargeting: {'alert':['volatility050','green']},
                                                adLocation: 'FIRSTMPU',
                                                isObserve: !false,
                                                observeFromUAC: !false,
                                                triggerPrebid: true,
                                                moatEnabled: true,
                                                collapseAdBeforeFetch: true,
                                                threshold: 0.01
                                            }
                                        });
                                    }();
                                </script>
                            </div>
                        </div>

        <div class="group group--brokers quote--overview">        
            <header class="header header--text">
                <h2 class="title">
                    <span class="label">Partner Center</span>
                </h2>
            </header>


                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-broker-button-1" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-broker-button-1',
                                            adUnitPath: '/2/brokerbuttons.marketwatch.com/investing/quotes/stock/overview',
                                            adSize: [[120,60]],
                                            adSizeMap: {},
                                            adTargeting: {'pos':['1'],'alert':['volatility050','green']},
                                            adLocation: 'BROKER1',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>


                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-broker-button-2" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-broker-button-2',
                                            adUnitPath: '/2/brokerbuttons.marketwatch.com/investing/quotes/stock/overview',
                                            adSize: [[120,60]],
                                            adSizeMap: {},
                                            adTargeting: {'pos':['2'],'alert':['volatility050','green']},
                                            adLocation: 'BROKER2',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>


                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-broker-button-3" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-broker-button-3',
                                            adUnitPath: '/2/brokerbuttons.marketwatch.com/investing/quotes/stock/overview',
                                            adSize: [[120,60]],
                                            adSizeMap: {},
                                            adTargeting: {'pos':['3'],'alert':['volatility050','green']},
                                            adLocation: 'BROKER3',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>


                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-broker-button-4" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-broker-button-4',
                                            adUnitPath: '/2/brokerbuttons.marketwatch.com/investing/quotes/stock/overview',
                                            adSize: [[120,60]],
                                            adSizeMap: {},
                                            adTargeting: {'pos':['4'],'alert':['volatility050','green']},
                                            adLocation: 'BROKER4',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>




        </div>


        <header class="header header--text">
            <h2 class="title">
                <span class="label">Your Watchlists</span>
            </h2>
        </header>

        <mw-watchlist class="element element--watchlist is-loading lazyload" data-expand="200">


            <div class="element element--message no-user j-message j-no-user j-hidden" data-track-query=".message--register|.message--login" data-track-code="MW_Homepage_Watchlist_Signup|MW_Homepage_Watchlist_Login">
                <div class="message__text">
                    <h5 class="primary">Customize MarketWatch</h5>
                    <p class="secondary">Have Watchlists? Log in to see them here or sign up to get started.</p>
                </div>
                <div class="group group--buttons vertical">
                    <a class="btn btn--primary" href="/sign-up">Create Account</a>
                    <span class="text">&#8230; or <a class="link" href="https://accounts.marketwatch.com/login?target=https%3A%2F%2Fwww.marketwatch.com%2Fwatchlist">Log In</a></span>
                </div>
            </div>




            <div class="element element--table watchlist has-watchlist j-watchlist j-hidden">
                <div class="table__options">
                    <div class="form">
                        <div class="form__item w100">
                            <i class="icon--caret-down"></i>
                            <select class="dropdown dropdown--form j-dropdown"></select>
                        </div>
                    </div>
                    <a href="https://www.marketwatch.com/watchlist" class="btn btn--watchlist t-in-watchlist"></a>
                </div>
                <table class="table table--secondary j-hidden j-table">
                    <thead>
                        <tr class="table__row">
                            <th class="table__heading indicator"></th>
                            <th class="table__heading w50 align--left">
                                <div class="primary">Symbol</div>
                                <small class="secondary">Company</small>
                            </th>
                            <th class="table__heading w45">
                                <div class="primary">Price</div>
                                <small class="secondary">Chg/Chg %</small>
                            </th>
                        </tr>
                    </thead>
                    <tbody class="j-watchlist-list">
                                            
                    </tbody>
                </table>
                <template class="ticker__template">
                    <table>
                        <tr class="table__row j-item">
                            <td class="table__cell t-colorBar">
                                <div class="marker"></div>
                            </td>
                            <td class="table__cell align--left">
                                <a class="primary t-link j-watchlist-tracking">
                                    <span class="symbol t-symbol"></span>
                                </a>
                                <div class="secondary">
                                    <small class="company t-company"></small>
                                </div>
                            </td>
                            <td class="table__cell">
                                <div class="primary t-last ignore-color"></div>
                                <small class="secondary">
                                    <span class="point t-change"></span><span class="percent t-percent"></span>
                                </small>
                            </td>
                        </tr>
                    </table>
                </template>
                <div class="table__details padding--small j-info">
                    <span class="details__info"><span class="details__text j-count"></span> (<a class="link" href="https://www.marketwatch.com/watchlist">Go to Your Watchlist</a>) </span>
                </div>
            </div>


            <div class="element element--message no-watchlist-items j-message j-hidden j-no-watchlist-items">
                <div class="message">
                    <div class="message__text">
                        <h5 class="primary">No Items in Watchlist</h5>
                        <p class="secondary">There are currently no items in this Watchlist.</p>
                    </div>
                    <div class="group group--buttons cover vertical">
                        <a class="btn btn--primary" href="https://www.marketwatch.com/watchlist"><i class="icon icon--plus"></i><span class="text">Add Tickers</span></a>
                    </div>
                </div>
            </div>

            <div class="element element--message no-watchlist j-message j-hidden j-no-watchlist">
                <div class="message">
                    <div class="message__text">
                        <h5 class="primary">No Saved Watchlists</h5>
                        <p class="secondary">Create a list of the investments you want to track.</p>
                    </div>
                    <div class="group group--buttons cover vertical">
                        <a href="https://www.marketwatch.com/watchlist" class="btn btn--primary">Create Watchlist</a>
                        <span class="text">&#8230;or <a class="link" href="https://www.marketwatch.com/graphics/watchlist">learn more</a></span>
                    </div>
                </div>
            </div>


            <div class="element element--message error-watchlist j-message j-hidden j-error">
                <div class="message">
                    <div class="message__text">
                        <h5 class="primary">Uh oh</h5>
                        <p class="secondary">Something went wrong while loading Watchlist.</p>
                    </div>
                    <div class="group group--buttons cover vertical">
                        <a href="https://www.marketwatch.com/watchlist" class="btn btn--primary">Go to Watchlist</a>
                    </div>
                </div>
            </div>

        </mw-watchlist>

        <header class="header header--text">
            <h2 class="title">
                <span class="label">Recently Viewed Tickers</span>
            </h2>
        </header>
        <mw-quotelist class="element element--recentTickers is-loading j-tickerList" data-track-query=".btn--tickerSearch|.ticker" data-track-code="MW_Homepage_Watchlist_Search Tickers|MW_Homepage_Watchlist_Recent Tickers">
            <div class="element element--message j-message j-hidden j-no-recent-items">
                <div class="message">
                    <div class="message__text">
                        <h3 class="primary">No Recent Tickers</h3>
                        <p class="secondary">Visit a quote page and your recently viewed tickers will be displayed here.</p>
                    </div>
                    <div class="group group--buttons">
                        <button class="btn btn--primary j-tickerSearch">Search Tickers</button>
                    </div>
                </div>
            </div>
            <div class="j-hidden j-recent">
                <template class="instruments">
                    <a class="ticker t-link j-recentlyviewed-tracking">
                        <bg-quote class="posNegNeu t-updown">
                            <h4 class="ticker__symbol t-symbol"></h4>
                            <span class="ticker__price ignore-color t-price"></span>
                            <span class="ticker__company t-company"></span>
                            <div class="ticker__change ignore-color">
                                <span class="change__price ignore-color t-change"></span>
                                <span class="change__percent ignore-color t-percent"></span>
                                <i class="icon"></i>
                            </div>
                        </bg-quote>
                    </a>
                </template>
            </div>
        </mw-quotelist>
                    </div>
                    </div>
                    <div class="region region--cx">




        <div class="column column--full">
            <div id="cx-marketdata">


            </div>
        </div>
                    </div>
                    <div class="region region--subNav">


                    <div class="column column--full">




                <input class="hidden toggle--subnav" type="checkbox" id="toggle--subnav" />
                <header class="header header--subnav">
                    <a class="game__logo hidden" href="https://www.marketwatch.com/games" aria-label="VSE Home">
                        <?xml version="1.0" encoding="utf-8"?>
                        <!-- Generator: Adobe Illustrator 25.4.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
                        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                        viewBox="0 0 311.2 92.3" style="enable-background:new 0 0 311.2 92.3;" xml:space="preserve" aria-labelledby="vse-logo-title vse-logo-desc">
                        <title id="vse-logo-title">VSE Home link</title>
                        <desc id="vse-logo-desc">Go to VSE home</desc>
                        <style type="text/css">
                        .st0{fill:#ffffff;}
                        .st1{fill:#ffffff;}
                        .st2{fill:#ffffff;}
                        </style>
                        <symbol  id="New_Symbol_38" viewBox="-61.9 -30.5 123.8 61">
                        <g>
                            <g>
                            <polygon class="st0" points="-42.4,-8.3 -42.4,5.4 -46.9,5.4 -46.9,8.5 -34.2,8.5 -34.2,5.4 -38.6,5.4 -38.6,-8.3 			"/>
                            </g>
                            <g>
                            <path class="st0" d="M-54.4-8.6c-3.2,0-5.4,0.9-6.9,2.8l-0.1,0.1l2.9,1.9l0.1-0.1c1-1.2,2.1-1.6,3.8-1.6c1.7,0,2.7,0.6,2.7,1.8
                                c0,1-0.5,1.7-3.6,2.4c-3.6,0.9-5.3,2.6-5.3,5.3c0,3,2.3,4.8,6.2,4.8c2.9,0,5-0.9,6.3-2.8l0.1-0.1l-2.9-1.9L-51.2,4
                                C-52,5.2-53,5.6-54.6,5.6C-56.1,5.6-57,5-57,3.9c0-1.1,0.9-1.7,3.4-2.3c4-0.9,5.5-2.3,5.5-5.2C-48.1-6.7-50.5-8.6-54.4-8.6z"/>
                            </g>
                            <g>
                            <path class="st0" d="M-25.9-8.6c-4.4,0-6.9,2.7-6.9,7.4v2.4c0,4.8,2.4,7.4,6.9,7.4c4.5,0,6.9-2.6,6.9-7.4v-2.4
                                C-19-5.8-21.6-8.6-25.9-8.6z M-25.9,5.6c-2.1,0-3.1-1.4-3.1-4.4v-2.4c0-3,1-4.4,3.1-4.4c2.1,0,3.1,1.4,3.1,4.4v2.4
                                C-22.8,4.2-23.8,5.6-25.9,5.6z"/>
                            </g>
                            <g>
                            <path class="st0" d="M-9.6-8.6c-4.4,0-6.9,2.7-6.9,7.4v2.4c0,4.8,2.4,7.4,6.9,7.4c3.7,0,6-1.9,6.6-5.4l0-0.1h-3.6l0,0.1
                                C-7,4.8-8,5.6-9.6,5.6c-2.1,0-3.1-1.4-3.1-4.4v-2.4c0-3,1-4.4,3.1-4.4c1.7,0,2.6,0.7,3,2.4l0,0.1H-3l0-0.1
                                C-3.6-6.8-5.8-8.6-9.6-8.6z"/>
                            </g>
                            <g>
                            <polygon class="st0" points="10,-8.3 5.5,-1.4 3.5,-3.9 3.5,-8.3 -0.3,-8.3 -0.3,8.5 3.5,8.5 3.5,1.5 8.9,8.4 13.5,8.5 8,1.6
                                14.5,-8.3 			"/>
                            </g>
                        </g>
                        <g>
                            <g>
                            <polygon class="st0" points="-55.6,13.7 -61.9,30.5 -57.7,30.5 -53.9,19.6 -50.1,30.5 -45.9,30.5 -52.2,13.7 			"/>
                            </g>
                            <g>
                            <rect x="-44" y="13.7" class="st0" width="3.8" height="16.8"/>
                            </g>
                            <g>
                            <path class="st0" d="M-26.7,13.7l-3.2,6.5h-2.7v-6.5h-3.8v16.8h6.5c4.3,0,6.7-1.9,6.7-5.2c0-2.2-1-3.7-3-4.5l3.7-7.1H-26.7z
                                M-30.3,23.3c2.4,0,3.3,0.6,3.3,2.1c0,1.5-0.9,2.1-3.3,2.1h-2.3v-4.2H-30.3z"/>
                            </g>
                            <g>
                            <polygon class="st0" points="-17.2,13.7 -17.2,27.4 -21.6,27.4 -21.6,30.5 -8.9,30.5 -8.9,27.4 -13.4,27.4 -13.4,13.7 			"/>
                            </g>
                            <g>
                            <path class="st0" d="M0.2,13.5c-4.5,0-6.9,2.5-6.9,7v10h3.8v-10c0-2.8,1-4,3.1-4s3.1,1.2,3.1,4v10h3.8v-10
                                C7.1,16,4.7,13.5,0.2,13.5z"/>
                            </g>
                            <g>
                            <polygon class="st0" points="26.6,13.7 26.6,30.5 30.4,30.5 30.4,16.8 37.9,16.8 37.9,13.7 			"/>
                            </g>
                            <g>
                            <path class="st0" d="M20.5,13.7l-1.1,3.2h-5.8l-1.1-3.2H8.5l6.3,16.8h3.6l6.3-16.8H20.5z M18.5,20.2l-2,5.7l-2-5.7H18.5z"/>
                            </g>
                        </g>
                        <g>
                            <polygon class="st0" points="-60.5,-30.3 -60.5,-13.5 -49.2,-13.5 -49.2,-16.6 -56.7,-16.6 -56.7,-20.1 -50,-20.1 -50,-23.1
                            -56.7,-23.1 -56.7,-27.2 -49.2,-27.2 -49.2,-30.3 		"/>
                        </g>
                        <g>
                            <polygon class="st0" points="-36.7,-30.3 -40,-24.7 -43.4,-30.3 -47.5,-30.3 -42.4,-21.6 -47,-13.5 -42.8,-13.5 -40,-18.7
                            -37.2,-13.5 -33.1,-13.5 -37.7,-21.6 -32.6,-30.3 		"/>
                        </g>
                        <g>
                            <path class="st0" d="M-25.1-30.5c-4.4,0-6.9,2.7-6.9,7.4v2.4c0,4.8,2.4,7.4,6.9,7.4c3.7,0,6-1.9,6.6-5.4l0-0.1h-3.6l0,0.1
                            c-0.3,1.6-1.3,2.4-3,2.4c-2.1,0-3.1-1.4-3.1-4.4v-2.4c0-3,1-4.4,3.1-4.4c1.7,0,2.6,0.7,3,2.4l0,0.1h3.6l0-0.1
                            C-19.1-28.7-21.2-30.5-25.1-30.5z"/>
                        </g>
                        <g>
                            <polygon class="st0" points="-5.9,-30.3 -5.9,-23.1 -11.8,-23.1 -11.8,-30.3 -15.6,-30.3 -15.6,-13.5 -11.8,-13.5 -11.8,-20.1
                            -5.9,-20.1 -5.9,-13.5 -2.1,-13.5 -2.1,-30.3 		"/>
                        </g>
                        <g>
                            <path class="st0" d="M12-30.3l-1.1,3.2H5.1L4-30.3H0l6.3,16.8h3.6l6.3-16.8H12z M10-23.8l-2,5.7l-2-5.7H10z"/>
                        </g>
                        <g>
                            <polygon class="st0" points="28.6,-30.3 21.7,-20.2 21.7,-30.3 18.1,-30.3 18.1,-13.5 21.2,-13.5 28.1,-23.7 28.1,-13.5
                            31.7,-13.5 31.7,-30.3 		"/>
                        </g>
                        <g>
                            <path class="st0" d="M41.4-30.5c-4.4,0-6.9,2.7-6.9,7.4v2.1c0,5,2.4,7.7,6.9,7.7c3.7,0,6.1-1.9,6.6-5.4l0-0.1h-3.6l0,0.1
                            c-0.3,1.6-1.4,2.4-3,2.4c-2.1,0-3.1-1.4-3.1-4.4v-2.4c0-3,1-4.4,3.1-4.4c1.8,0,2.7,0.9,2.9,2.9c0,0,0,0.1,0,0.2h-3v3h6.7v-1.7
                            C48.1-27.9,45.8-30.5,41.4-30.5z"/>
                        </g>
                        <g>
                            <polygon class="st0" points="50.6,-30.3 50.6,-13.5 61.9,-13.5 61.9,-16.6 54.4,-16.6 54.4,-20.1 61.1,-20.1 61.1,-23.1
                            54.4,-23.1 54.4,-27.3 61.9,-27.3 61.9,-30.3 		"/>
                        </g>
                        </symbol>
                        <symbol  id="New_Symbol_46" viewBox="-71.7 -45.2 143.4 90.3">
                        <polygon class="st0" points="18.4,42.3 17.5,41.1 18.4,42.3 	"/>
                        <polygon class="st0" points="-71.7,45.2 -60,6 -33.4,45.2 	"/>
                        <polygon class="st0" points="-39.7,-45.2 -0.9,-45.2 -13.2,-6.1 	"/>
                        <polygon class="st0" points="17.5,41.1 -8.9,0.5 36.4,0.5 18.4,42.3 	"/>
                        <polygon class="st0" points="-56.7,-4.5 -43.5,-41.6 -18.3,-4.5 	"/>
                        <polygon class="st0" points="71.7,45.2 22.7,45.2 40.8,3.3 	"/>
                        <polygon class="st0" points="-57.5,0.5 -15.5,0.5 -29.4,41.8 	"/>
                        <polygon class="st0" points="4.1,-43.8 34.9,-4.5 -8.3,-4.5 	"/>
                        </symbol>
                        <g id="logo">
                        <g id="XMLID_00000062157184710323827910000000126787317062293155_">
                            <g>
                            <g>
                                <g>
                                <polygon class="st2" points="90,4.8 89.2,6 90.1,4.9 					"/>
                                <polygon class="st2" points="0,2 11.6,41.2 38.3,2 					"/>
                                <polygon class="st2" points="32,92.3 70.8,92.3 58.5,53.2 					"/>
                                <polygon class="st2" points="89.2,6 62.8,46.6 108.1,46.6 90.1,4.9 					"/>
                                <polygon class="st2" points="15,51.6 28.2,88.7 53.4,51.6 					"/>
                                <polygon class="st2" points="143.4,2 94.4,2 112.5,43.9 					"/>
                                <polygon class="st2" points="14.2,46.6 56.2,46.6 42.3,5.3 					"/>
                                <polygon class="st2" points="75.8,90.9 106.6,51.6 63.3,51.6 					"/>
                                </g>
                            </g>
                            <g>
                                <g>
                                <g>
                                    <g>
                                    <polygon class="st2" points="176.5,63 176.5,45.3 170.8,45.3 170.8,41.4 187.2,41.4 187.2,45.3 181.4,45.3 181.4,63
                                        "/>
                                    </g>
                                    <g>
                                    <path class="st2" d="M161.2,63.3c-4.2,0-6.9-1.1-8.9-3.6l-0.1-0.1l3.8-2.4l0.1,0.1c1.3,1.5,2.7,2.1,4.9,2.1
                                        c2.2,0,3.4-0.8,3.4-2.3c0-1.3-0.7-2.2-4.6-3.1c-4.7-1.2-6.9-3.3-6.9-6.8c0-3.8,3-6.1,8-6.1c3.8,0,6.5,1.2,8.1,3.6l0.1,0.1
                                        l-3.7,2.5l-0.1-0.1c-1-1.5-2.3-2.1-4.4-2.1c-2,0-3.1,0.8-3.1,2.2c0,1.5,1.1,2.2,4.4,3c5.1,1.2,7,3,7,6.7
                                        C169.2,60.9,166.2,63.3,161.2,63.3z"/>
                                    </g>
                                    <g>
                                    <path class="st2" d="M197.8,63.3c-5.6,0-8.9-3.5-8.9-9.6v-3c0-6.2,3.2-9.6,8.9-9.6c5.8,0,8.9,3.4,8.9,9.6v3
                                        C206.7,59.8,203.5,63.3,197.8,63.3z M197.8,45c-2.7,0-4,1.8-4,5.7v3c0,3.9,1.3,5.7,4,5.7c2.7,0,4-1.8,4-5.7v-3
                                        C201.8,46.8,200.5,45,197.8,45z"/>
                                    </g>
                                    <g>
                                    <path class="st2" d="M218.8,63.3c-5.6,0-8.9-3.5-8.9-9.6v-3c0-6.2,3.2-9.6,8.9-9.6c4.8,0,7.8,2.4,8.5,7l0,0.1h-4.7l0-0.1
                                        c-0.4-2.1-1.7-3.2-3.8-3.2c-2.7,0-4,1.8-4,5.7v3c0,3.8,1.3,5.7,4,5.7c2.2,0,3.3-0.9,3.8-3.2l0-0.1h4.7l0,0.1
                                        C226.6,61,223.8,63.3,218.8,63.3z"/>
                                    </g>
                                    <g>
                                    <polygon class="st2" points="244.2,63 238.3,54.1 235.7,57.3 235.7,63 230.8,63 230.8,41.4 235.7,41.4 235.7,50.4
                                        242.7,41.4 248.6,41.4 241.5,50.2 249.9,63 							"/>
                                    </g>
                                </g>
                                <g>
                                    <g>
                                    <polygon class="st2" points="159.6,34.6 151.5,13 156.8,13 161.7,27.1 166.7,13 172,13 164,34.6 							"/>
                                    </g>
                                    <g>
                                    <rect x="174.6" y="13" class="st2" width="4.9" height="21.7"/>
                                    </g>
                                    <g>
                                    <path class="st2" d="M196.9,34.6l-4.1-8.4h-3.5v8.4h-4.9V13h8.3c5.5,0,8.7,2.4,8.7,6.7c0,2.8-1.3,4.8-3.9,5.8l4.8,9.2H196.9z
                                        M192.2,22.3c3,0,4.2-0.7,4.2-2.7c0-1.9-1.2-2.7-4.2-2.7h-3v5.4H192.2z"/>
                                    </g>
                                    <g>
                                    <polygon class="st2" points="209.1,34.6 209.1,16.9 203.4,16.9 203.4,13 219.7,13 219.7,16.9 214,16.9 214,34.6 							"/>
                                    </g>
                                    <g>
                                    <path class="st2" d="M231.5,34.9c-5.8,0-8.9-3.2-8.9-9.1V13h4.9v12.9c0,3.6,1.2,5.1,4,5.1c2.8,0,4-1.6,4-5.1V13h4.9v12.8
                                        C240.4,31.7,237.3,34.9,231.5,34.9z"/>
                                    </g>
                                    <g>
                                    <polygon class="st2" points="265.5,34.6 265.5,13 270.4,13 270.4,30.7 280,30.7 280,34.6 							"/>
                                    </g>
                                    <g>
                                    <path class="st2" d="M257.7,34.6l-1.4-4.1h-7.5l-1.4,4.1h-5.3l8.1-21.7h4.6l8.1,21.7H257.7z M255.1,26.3l-2.6-7.3l-2.6,7.3
                                        H255.1z"/>
                                    </g>
                                </g>
                                <g>
                                    <polygon class="st2" points="153.3,91.3 153.3,69.7 167.8,69.7 167.8,73.6 158.2,73.6 158.2,78.2 166.8,78.2 166.8,82.1
                                    158.2,82.1 158.2,87.4 167.8,87.4 167.8,91.3 						"/>
                                </g>
                                <g>
                                    <polygon class="st2" points="183.9,91.3 179.6,84.2 175.4,91.3 170,91.3 176.5,80.2 170.7,69.7 176.1,69.7 179.6,76.4
                                    183.2,69.7 188.5,69.7 182.7,80.2 189.2,91.3 						"/>
                                </g>
                                <g>
                                    <path class="st2" d="M198.9,91.6c-5.6,0-8.9-3.5-8.9-9.6v-3c0-6.2,3.2-9.6,8.9-9.6c4.8,0,7.8,2.4,8.5,7l0,0.1h-4.7l0-0.1
                                    c-0.4-2.1-1.7-3.2-3.8-3.2c-2.7,0-4,1.8-4,5.7v3c0,3.8,1.3,5.7,4,5.7c2.2,0,3.3-0.9,3.8-3.2l0-0.1h4.7l0,0.1
                                    C206.7,89.3,203.9,91.6,198.9,91.6z"/>
                                </g>
                                <g>
                                    <polygon class="st2" points="223.6,91.3 223.6,82.1 216,82.1 216,91.3 211.1,91.3 211.1,69.7 216,69.7 216,78.2 223.6,78.2
                                    223.6,69.7 228.5,69.7 228.5,91.3 						"/>
                                </g>
                                <g>
                                    <path class="st2" d="M246.7,91.3l-1.4-4.1h-7.5l-1.4,4.1h-5.3l8.1-21.7h4.6l8.1,21.7H246.7z M244.1,83l-2.6-7.3L239,83H244.1z
                                    "/>
                                </g>
                                <g>
                                    <polygon class="st2" points="268,91.3 259.3,78.4 259.3,91.3 254.6,91.3 254.6,69.7 258.6,69.7 267.4,82.8 267.4,69.7
                                    272.1,69.7 272.1,91.3 						"/>
                                </g>
                                <g>
                                    <path class="st2" d="M284.6,91.6c-5.6,0-8.9-3.5-8.9-9.6v-2.7c0-6.4,3.2-9.9,8.9-9.9c4.8,0,7.8,2.5,8.5,7l0,0.1h-4.7l0-0.1
                                    c-0.4-2.1-1.7-3.2-3.8-3.2c-2.7,0-4,1.8-4,5.7v3c0,3.9,1.3,5.7,4,5.7c2.3,0,3.5-1.2,3.8-3.8c0,0,0-0.1,0-0.2h-3.8v-3.8h8.6V82
                                    C293.2,88.3,290.2,91.6,284.6,91.6z"/>
                                </g>
                                <g>
                                    <polygon class="st2" points="296.5,91.3 296.5,69.7 311,69.7 311,73.6 301.4,73.6 301.4,78.2 310,78.2 310,82.1 301.4,82.1
                                    301.4,87.4 311,87.4 311,91.3 						"/>
                                </g>
                                </g>
                            </g>
                            </g>
                        </g>
                        </g>
                        <g id="Layer_2">
                        </g>
                    </svg>
                    </a>
                    <h3 class="title">Overview</h3>
                    <label class="btn btn--subnav" for="toggle--subnav">
                        <span class="label">More<span class="m-hide"> Content</span></span>
                        <i class="icon icon--reorder"></i>
                    </label>
                </header>
                <div class="list list--subnav horizontal">
                                <li data-click-through="mw_quote_tab" class="subnav__item is-selected">
                                    <a class="link" href="https://www.marketwatch.com/investing/stock/aapl?mod=mw_quote_tab">Overview</a>
                                </li>
                                <li data-click-through="mw_quote_tab" class="subnav__item ">
                                    <a class="link" instrument-target="company-profile" href="https://www.marketwatch.com/investing/stock/aapl/company-profile?mod=mw_quote_tab">Profile</a>
                                </li>
                                <li data-click-through="mw_quote_tab" class="subnav__item ">
                                    <a class="link" instrument-target="charts" href="https://www.marketwatch.com/investing/stock/aapl/charts?mod=mw_quote_tab">Charts</a>
                                </li>
                                <li data-click-through="mw_quote_tab" class="subnav__item ">
                                    <a class="link" instrument-target="financials" href="https://www.marketwatch.com/investing/stock/aapl/financials?mod=mw_quote_tab">Financials</a>
                                </li>
                                <li data-click-through="mw_quote_tab" class="subnav__item ">
                                    <a class="link" instrument-target="download-data" href="https://www.marketwatch.com/investing/stock/aapl/download-data?mod=mw_quote_tab">Historical Quotes</a>
                                </li>
                                <li data-click-through="mw_quote_tab" class="subnav__item ">
                                    <a class="link" instrument-target="analystestimates" href="https://www.marketwatch.com/investing/stock/aapl/analystestimates?mod=mw_quote_tab">Analyst Estimates</a>
                                </li>
                                <li data-click-through="mw_quote_tab" class="subnav__item ">
                                    <a class="link" instrument-target="options" href="https://www.marketwatch.com/investing/stock/aapl/options?mod=mw_quote_tab">Options</a>
                                </li>

                        <li class="subnav__item subnav__ad"><a target="_blank" class="link" href="https://get.investors.com/product-overview/?src=A00619&refcode=Site%20placement%7CMarketWatch%7CMarketWatch%7C2023%7CRecurring%7COther%2FNA%7C0%7C%7C992173">Premium Tools<i class="icon icon--external"></i></a></li>

                </div>
                    </div>
                    </div>
                    <div class="region region--primary">




            <header class="header header--primary no-background">
                <h2 class="title">
                    <span class="label">AAPL Overview</span>
                </h2>
            </header>
                    <div class="column column--aside">


                    <div class="group group--elements left">



            <div class="element element--list">
                <header class="header header--secondary">
                    <h2 class="title">
                        <span class="label">Key Data</span>
                    </h2>
                </header>
                <ul class="list list--kv list--col50">
                        <li class="kv__item">
                            <small class="label">Open</small>
                            <span class="primary ">$162.44</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Day Range</small>
                            <span class="primary ">161.91 - 163.17</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">52 Week Range</small>
                            <span class="primary ">124.17 - 178.49</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Market Cap</small>
                            <span class="primary ">$2.57T</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Shares Outstanding</small>
                            <span class="primary ">15.82B</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Public Float</small>
                            <span class="primary ">15.81B</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Beta</small>
                            <span class="primary ">1.23</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Rev. per Employee</small>
                            <span class="primary ">$2.363M</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">P/E Ratio</small>
                            <span class="primary ">27.68</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">EPS</small>
                            <span class="primary ">$5.89</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Yield</small>
                            <span class="primary ">0.56%</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Dividend</small>
                            <span class="primary ">$0.23</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Ex-Dividend Date</small>
                            <span class="primary ">Feb 10, 2023</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Short Interest</small>
                            <span class="primary ">107.42M</span>
                            <span class="secondary ">03/15/23</span>
                        </li>
                        <li class="kv__item">
                            <small class="label">% of Float Shorted</small>
                            <span class="primary ">0.68%</span>
                            <span class="secondary no-value"></span>
                        </li>
                        <li class="kv__item">
                            <small class="label">Average Volume</small>
                            <span class="primary ">69.38M</span>
                            <span class="secondary no-value"></span>
                        </li>
                </ul>
            </div>
                    </div>
                    <div class="group group--elements right">




            <div class="element element--table performance">
                <header class="header header--secondary">
                    <h2 class="title">
                        <span class="label">Performance</span>
                    </h2>
                </header>
                <table class="table table--primary no-heading c2">
                    <tbody>
                            <tr class="table__row">
                                <td class="table__cell">5 Day</td>
                                <td class="table__cell">
                                    <ul class="content u-flex positive">
                                        <li class="content__item value ignore-color">1.82%</li>
                                        <li class="content__item bar">
                                            <span class="graphic" style="width: 1.8221528861154446177847113900%;"></span>
                                        </li>
                                    </ul>
                                </td>
                            </tr>
                            <tr class="table__row">
                                <td class="table__cell">1 Month</td>
                                <td class="table__cell">
                                    <ul class="content u-flex positive">
                                        <li class="content__item value ignore-color">8.04%</li>
                                        <li class="content__item bar">
                                            <span class="graphic" style="width: 8.038138118254651393762828580%;"></span>
                                        </li>
                                    </ul>
                                </td>
                            </tr>
                            <tr class="table__row">
                                <td class="table__cell">3 Month</td>
                                <td class="table__cell">
                                    <ul class="content u-flex positive">
                                        <li class="content__item value ignore-color">25.58%</li>
                                        <li class="content__item bar">
                                            <span class="graphic" style="width: 25.583006234126067882706072500%;"></span>
                                        </li>
                                    </ul>
                                </td>
                            </tr>
                            <tr class="table__row">
                                <td class="table__cell">YTD</td>
                                <td class="table__cell">
                                    <ul class="content u-flex positive">
                                        <li class="content__item value ignore-color">25.58%</li>
                                        <li class="content__item bar">
                                            <span class="graphic" style="width: 25.583006234126067882706072500%;"></span>
                                        </li>
                                    </ul>
                                </td>
                            </tr>
                            <tr class="table__row">
                                <td class="table__cell">1 Year</td>
                                <td class="table__cell">
                                    <ul class="content u-flex negative">
                                        <li class="content__item value ignore-color">-6.39%</li>
                                        <li class="content__item bar">
                                            <span class="graphic" style="width: 6.3909127416671447421260971800%;"></span>
                                        </li>
                                    </ul>
                                </td>
                            </tr>
                    </tbody>
                </table>


            </div>



                        <div class="element element--ad is-loading">
                            <div id="ad-mobile-display-ad" class="j-ad">
                                <script>
                                    !function() {
                                        window.__mwads = window.__mwads || {};
                                        window.__mwads.uacQ = window.__mwads.uacQ || [];
                                        window.__mwads.uacQ.push({
                                            options: {
                                                adActivate: true,
                                                adId: 'ad-mobile-display-ad',
                                                adUnitPath: '/2/marketwatch.com/investing/quotes/stock/overview',
                                                adSize: [[300,250],[375,320],[1,6],[1,7]],
                                                adSizeMap: {'at4units':[[300,250],[375,320],[1,6],[1,7]],'at8units':[],'at12units':[],'at16units':[]},
                                                adTargeting: {'alert':['volatility050','green']},
                                                adLocation: 'MOBILEMPU',
                                                isObserve: !false,
                                                observeFromUAC: !false,
                                                triggerPrebid: true,
                                                moatEnabled: true,
                                                collapseAdBeforeFetch: true,
                                                threshold: 0.01
                                            }
                                        });
                                    }();
                                </script>
                            </div>
                        </div>


            <div class="element element--analyst">
                <header class="header header--secondary">
                    <h2 class="title">
                        <span class="label">Analyst Ratings</span>
                    </h2>
                </header>
                <div class="analyst__chart">
                    <ul class="analyst__rating">
                        <li class="analyst__option ">Sell</li>
                        <li class="analyst__option ">Under</li>
                        <li class="analyst__option ">Hold</li>
                        <li class="analyst__option active">Over</li>
                        <li class="analyst__option ">Buy</li>
                    </ul>
                    <span class="analyst__count">Number of Ratings <span class="count">41</span></span>
                    <a class="analyst__link" instrument-target="analystestimates" href="https://www.marketwatch.com/investing/stock/aapl/analystestimates?mod=mw_quote_analyst">Full Ratings <i class="icon--arrow-right"></i></a>
                </div>
            </div>
                    </div>
                    </div>
                    <div class="column column--primary">





                <div class="element element--tabs">
                        <header class="header header--secondary">
                            <h2 class="title">
                                <span class="label"><a>Recent News</a></span>
                            </h2>
                        </header>
                    <mw-tabs>
                        <div class="element__options">
                            <ul role="tablist" class="tabs full-width" data-track-query=".tab__item">
                                    <button role="tab" aria-selected="true" class="tab__item is-selected j-tabItem" data-tab-pane="MarketWatch" data-track-code="Index_Recent News_MarketWatch">MarketWatch</button>
                                    <button role="tab" aria-selected="" class="tab__item  j-tabItem" data-tab-pane="Dow Jones" data-track-code="Index_Recent News_Dow Jones">Dow Jones</button>
                            </ul>
                            <div class="results__count"></div>
                        </div>
                        <div class="element__body j-tabPanes">
                                <div class="tab__pane is-active j-tabPane" data-tab-pane="MarketWatch">




                
                    <mw-scrollable-news-v2 natural data-expand="200" class='collection collection--moreHeadlines j-scrollViewport lazyload '>
                    <div class="column column--primary j-moreHeadlineWrapper" data-source="ChartingSymbol" data-total-count="" data-channel="MarketWatch" data-channel-id="" data-realtimefeed="" data-layout-position="" data-tracking="mw_quote_news">
                        <div class="collection__elements j-scrollElement">





            <div data-timestamp="1680276780000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c5-930995a84621" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/the-explosive-ai-trend-is-here-to-stay-these-stocks-are-poised-to-benefit-82aed67d?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-753735?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-753735?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-753735?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-753735?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-753735?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-753735?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-753735?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/the-explosive-ai-trend-is-here-to-stay-these-stocks-are-poised-to-benefit-82aed67d?mod=mw_quote_news">
                                    
                                    
                                    The &#x2018;explosive&#x2019; AI trend is here to stay. These stocks are poised to benefit.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T11:33:00">Mar. 31, 2023 at 11:33 a.m. ET</span>

                            <span class="article__author">by James Rogers</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680267600000" data-docid="" data-msgid="" data-guid="1462659e-ccc4-11ed-88aa-05dcca6788d8" class="element element--article    BarronsOnline">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/articles/barrons-100-most-influential-women-in-u-s-finance-annie-lamont-11c07eba?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.barrons.com/im-742775/?size=1.777777777777778&amp;width=220 220w,https://images.barrons.com/im-742775/?size=1.777777777777778&amp;width=300 300w,https://images.barrons.com/im-742775/?size=1.777777777777778&amp;width=460 460w,https://images.barrons.com/im-742775/?size=1.777777777777778&amp;width=800 800w,https://images.barrons.com/im-742775/?size=1.777777777777778&amp;width=920 920w,https://images.barrons.com/im-742775/?size=1.777777777777778&amp;width=1240 1240w,https://images.barrons.com/im-742775/?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label venture capital">
        Venture Capital                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/articles/barrons-100-most-influential-women-in-u-s-finance-annie-lamont-11c07eba?mod=mw_quote_news">
                                    
                                    
                                    Annie Lamont
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T09:00:00">Mar. 31, 2023 at 9:00 a.m. ET</span>

                            <span class="article__author">by Barron&apos;s</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680264480000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c7-d051fabdff65" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/here-are-the-20-best-performing-stocks-of-march-and-the-20-worst-2f6358ea?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-755024?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-755024?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-755024?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-755024?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-755024?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-755024?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-755024?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/here-are-the-20-best-performing-stocks-of-march-and-the-20-worst-2f6358ea?mod=mw_quote_news">
                                    
                                    
                                    Here are the 20 best performing stocks of March &#x2014; and the 20 worst
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T08:08:00">Mar. 31, 2023 at 8:08 a.m. ET</span>

                            <span class="article__author">by Philip van Doorn</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680208680000" data-docid="" data-msgid="" data-guid="20a05575-0424-1529-42f8-da6c55cf5841" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/articles/walt-disney-apple-stock-price-9e1a1c80?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.barrons.com/im-754129?size=1.777777777777778&amp;width=220 220w,https://images.barrons.com/im-754129?size=1.777777777777778&amp;width=300 300w,https://images.barrons.com/im-754129?size=1.777777777777778&amp;width=460 460w,https://images.barrons.com/im-754129?size=1.777777777777778&amp;width=800 800w,https://images.barrons.com/im-754129?size=1.777777777777778&amp;width=920 920w,https://images.barrons.com/im-754129?size=1.777777777777778&amp;width=1240 1240w,https://images.barrons.com/im-754129?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label technology">
        Technology                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/articles/walt-disney-apple-stock-price-9e1a1c80?mod=mw_quote_news">
                                    
                                    
                                    An Analyst Offers a New Reason Why Apple Should Buy Disney: It&#x2019;s Too Big to Fail
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T16:38:00">Mar. 30, 2023 at 4:38 p.m. ET</span>

                            <span class="article__author">by Barron&apos;s</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680208320000" data-docid="" data-msgid="" data-guid="371320d6-04d9-453e-a6a8-94f2317b7153" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/data-news/apple-inc-stock-rises-thursday-outperforms-market-28f5c5e0-360c0526f057?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/data-news/apple-inc-stock-rises-thursday-outperforms-market-28f5c5e0-360c0526f057?mod=mw_quote_news">
                                    
                                    
                                    Apple Inc. stock rises Thursday, outperforms market
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T16:32:00">Mar. 30, 2023 at 4:32 p.m. ET</span>

                            <span class="article__author">by MarketWatch Automation</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680206100000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c4-c264e5ccef2d" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/tech-stocks-back-as-a-safe-haven-trade-after-sell-off-in-bank-sector-but-for-how-long-12a14ee8?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-752902?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-752902?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-752902?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-752902?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-752902?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-752902?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-752902?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/tech-stocks-back-as-a-safe-haven-trade-after-sell-off-in-bank-sector-but-for-how-long-12a14ee8?mod=mw_quote_news">
                                    
                                    
                                    Are tech stocks becoming a haven again? &#x2018;It&#x2019;s a mistake,&#x2019; say market analysts.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T15:55:00">Mar. 30, 2023 at 3:55 p.m. ET</span>

                            <span class="article__author">by Isabel Wang</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680205440000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c7-571f6a6a0a54" class="element element--article no-image   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/virnetx-stock-takes-sharp-u-turn-into-the-red-after-appeals-court-said-two-patents-were-unpatenable-but-special-dividend-remains-intact-63bba068?mod=mw_quote_news" role="presentation" tabindex="-1">
                            
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/virnetx-stock-takes-sharp-u-turn-into-the-red-after-appeals-court-said-two-patents-were-unpatenable-but-special-dividend-remains-intact-63bba068?mod=mw_quote_news">
                                    
                                    
                                    VirnetX stock takes sharp U-turn into the red after appeals court said two patents were &#x2018;unpatenable,&#x2019; but special dividend remains intact
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T15:44:00">Mar. 30, 2023 at 3:44 p.m. ET</span>

                            <span class="article__author">by Tomi Kilgore</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680197580000" data-docid="" data-msgid="" data-guid="20a05575-0424-1529-42de-aff104bb56a7" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/articles/nasdaq-apple-stock-microsoft-big-tech-4cf9971c?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.barrons.com/im-715622?size=1.777777777777778&amp;width=220 220w,https://images.barrons.com/im-715622?size=1.777777777777778&amp;width=300 300w,https://images.barrons.com/im-715622?size=1.777777777777778&amp;width=460 460w,https://images.barrons.com/im-715622?size=1.777777777777778&amp;width=800 800w,https://images.barrons.com/im-715622?size=1.777777777777778&amp;width=920 920w,https://images.barrons.com/im-715622?size=1.777777777777778&amp;width=1240 1240w,https://images.barrons.com/im-715622?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label markets">
        Markets                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/articles/nasdaq-apple-stock-microsoft-big-tech-4cf9971c?mod=mw_quote_news">
                                    
                                    
                                    The Nasdaq-100 Just Entered a Bull Market. Why It&#x2019;s Time to Sell Apple and Microsoft.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T13:33:00">Mar. 30, 2023 at 1:33 p.m. ET</span>

                            <span class="article__author">by Barron&apos;s</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680195180000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c6-d54ebb4ea127" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/apple-buying-disney-analyst-explains-why-theyre-worth-more-together-afdfedd0?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-754331?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-754331?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-754331?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-754331?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-754331?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-754331?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-754331?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/apple-buying-disney-analyst-explains-why-theyre-worth-more-together-afdfedd0?mod=mw_quote_news">
                                    
                                    
                                    Apple buying Disney? Analyst explains why they&#x2019;re &#x2018;worth more together&#x2019;
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T12:53:00">Mar. 30, 2023 at 12:53 p.m. ET</span>

                            <span class="article__author">by Jon Swartz</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680185580000" data-docid="" data-msgid="" data-guid="20a05575-0424-1529-400e-f0d01b28530a" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/articles/tesla-elon-musk-tesla-ai-letter-16f6df7b?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.barrons.com/im-753731?size=1.777777777777778&amp;width=220 220w,https://images.barrons.com/im-753731?size=1.777777777777778&amp;width=300 300w,https://images.barrons.com/im-753731?size=1.777777777777778&amp;width=460 460w,https://images.barrons.com/im-753731?size=1.777777777777778&amp;width=800 800w,https://images.barrons.com/im-753731?size=1.777777777777778&amp;width=920 920w,https://images.barrons.com/im-753731?size=1.777777777777778&amp;width=1240 1240w,https://images.barrons.com/im-753731?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label companies">
        Companies                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/articles/tesla-elon-musk-tesla-ai-letter-16f6df7b?mod=mw_quote_news">
                                    
                                    
                                    Tesla Needs AI to Thrive. Why Elon Musk Wants to Pause GPT-4.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T10:13:00">Mar. 30, 2023 at 10:13 a.m. ET</span>

                            <span class="article__author">by Barron&apos;s</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680182820000" data-docid="" data-msgid="" data-guid="ce537594-c9b6-11ed-90fa-055ac07d93d0" class="element element--article    BarronsOnline">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/articles/us-dollar-stocks-china-3837842c?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.barrons.com/im-750059/?size=1.777777777777778&amp;width=220 220w,https://images.barrons.com/im-750059/?size=1.777777777777778&amp;width=300 300w,https://images.barrons.com/im-750059/?size=1.777777777777778&amp;width=460 460w,https://images.barrons.com/im-750059/?size=1.777777777777778&amp;width=800 800w,https://images.barrons.com/im-750059/?size=1.777777777777778&amp;width=920 920w,https://images.barrons.com/im-750059/?size=1.777777777777778&amp;width=1240 1240w,https://images.barrons.com/im-750059/?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label markets">
        Markets                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/articles/us-dollar-stocks-china-3837842c?mod=mw_quote_news">
                                    
                                    
                                    The U.S. Is Scaring Off Foreign Investors. Why They&#x2019;re Looking Elsewhere.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T09:27:00">Mar. 30, 2023 at 9:27 a.m. ET</span>

                            <span class="article__author">by Barron&apos;s</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680181500000" data-docid="" data-msgid="" data-guid="20a05575-0424-1529-3e90-4be75b16a7a5" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/articles/tiktok-ban-us-chinese-firms-b18033e9?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.barrons.com/im-754762?size=1.777777777777778&amp;width=220 220w,https://images.barrons.com/im-754762?size=1.777777777777778&amp;width=300 300w,https://images.barrons.com/im-754762?size=1.777777777777778&amp;width=460 460w,https://images.barrons.com/im-754762?size=1.777777777777778&amp;width=800 800w,https://images.barrons.com/im-754762?size=1.777777777777778&amp;width=920 920w,https://images.barrons.com/im-754762?size=1.777777777777778&amp;width=1240 1240w,https://images.barrons.com/im-754762?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label china">
        China                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/articles/tiktok-ban-us-chinese-firms-b18033e9?mod=mw_quote_news">
                                    
                                    
                                    TikTok Won&#x2019;t Be the Last Chinese Firm Targeted. Where the Next Fronts Might Be.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T09:05:00">Mar. 30, 2023 at 9:05 a.m. ET</span>

                            <span class="article__author">by Barron&apos;s</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680181200000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c6-a2bf008261bd" class="element element--article no-image   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/virnetx-stock-rockets-after-declaring-large-special-dividend-as-positive-outcome-from-apple-litigation-nears-7f5b2a30?mod=mw_quote_news" role="presentation" tabindex="-1">
                            
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/virnetx-stock-rockets-after-declaring-large-special-dividend-as-positive-outcome-from-apple-litigation-nears-7f5b2a30?mod=mw_quote_news">
                                    
                                    
                                    VirnetX stock rockets after declaring large special dividend, as positive outcome from Apple litigation nears
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T09:00:00">Mar. 30, 2023 at 9:00 a.m. ET</span>

                            <span class="article__author">by Tomi Kilgore</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680179880000" data-docid="" data-msgid="" data-guid="20a05575-0424-1529-3bc0-1a0f97464c9b" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/articles/metaverse-apple-epic-meta-stock-price-e80bafe0?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.barrons.com/im-753037?size=1.777777777777778&amp;width=220 220w,https://images.barrons.com/im-753037?size=1.777777777777778&amp;width=300 300w,https://images.barrons.com/im-753037?size=1.777777777777778&amp;width=460 460w,https://images.barrons.com/im-753037?size=1.777777777777778&amp;width=800 800w,https://images.barrons.com/im-753037?size=1.777777777777778&amp;width=920 920w,https://images.barrons.com/im-753037?size=1.777777777777778&amp;width=1240 1240w,https://images.barrons.com/im-753037?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label technology">
        Technology                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/articles/metaverse-apple-epic-meta-stock-price-e80bafe0?mod=mw_quote_news">
                                    
                                    
                                    Epic and Apple Make Metaverse Advances. That&#x2019;s Bad News for Meta.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T08:38:00">Mar. 30, 2023 at 8:38 a.m. ET</span>

                            <span class="article__author">by Barron&apos;s</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680178860000" data-docid="" data-msgid="" data-guid="20a05575-0424-1529-3f61-d84c757b41cc" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/articles/apple-wwdc-event-june-date-vr-d4fa751b?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.barrons.com/im-616521?size=1.777777777777778&amp;width=220 220w,https://images.barrons.com/im-616521?size=1.777777777777778&amp;width=300 300w,https://images.barrons.com/im-616521?size=1.777777777777778&amp;width=460 460w,https://images.barrons.com/im-616521?size=1.777777777777778&amp;width=800 800w,https://images.barrons.com/im-616521?size=1.777777777777778&amp;width=920 920w,https://images.barrons.com/im-616521?size=1.777777777777778&amp;width=1240 1240w,https://images.barrons.com/im-616521?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label technology">
        Technology                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/articles/apple-wwdc-event-june-date-vr-d4fa751b?mod=mw_quote_news">
                                    
                                    
                                    Apple&#x2019;s WWDC Will Happen in Early June. Some Hope for a VR Headset Launch.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T08:21:00">Mar. 30, 2023 at 8:21 a.m. ET</span>

                            <span class="article__author">by Barron&apos;s</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680176280000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c1-fbb22bdaa6c5" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/whats-worth-streaming-in-april-2023-theres-almost-too-much-to-watch-but-heres-where-to-start-73bf544?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-753929?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-753929?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-753929?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-753929?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-753929?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-753929?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-753929?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            <span class="article__label opinion">
        Opinion                    </span>
                            
                                <a class="link" href="https://www.marketwatch.com/story/whats-worth-streaming-in-april-2023-theres-almost-too-much-to-watch-but-heres-where-to-start-73bf544?mod=mw_quote_news">
                                    
                                    
                                    What&#x2019;s worth streaming in April 2023? There&#x2019;s almost too much to watch, but here&#x2019;s where to start.
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T07:38:00">Mar. 30, 2023 at 7:38 a.m. ET</span>

                            <span class="article__author">by Mike Murphy</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680129720000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c6-3d9fc2012e84" class="element element--article no-image   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/disney-slices-more-than-300-streaming-jobs-in-china-report-ab604aee?mod=mw_quote_news" role="presentation" tabindex="-1">
                            
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/disney-slices-more-than-300-streaming-jobs-in-china-report-ab604aee?mod=mw_quote_news">
                                    
                                    
                                    Disney slices more than 300 streaming jobs in China: report
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-29T18:42:00">Mar. 29, 2023 at 6:42 p.m. ET</span>

                            <span class="article__author">by Jon Swartz</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680121860000" data-docid="" data-msgid="" data-guid="94149543-31bf-4ae4-96a2-faee07e2fe38" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/data-news/apple-inc-stock-outperforms-competitors-on-strong-trading-day-48324c05-41ede4407160?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-213861?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/data-news/apple-inc-stock-outperforms-competitors-on-strong-trading-day-48324c05-41ede4407160?mod=mw_quote_news">
                                    
                                    
                                    Apple Inc. stock outperforms competitors on strong trading day
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-29T16:31:00">Mar. 29, 2023 at 4:31 p.m. ET</span>

                            <span class="article__author">by MarketWatch Automation</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680121440000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c4-f76738e36879" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/u-s-stock-futures-rise-as-sliding-vix-signals-calmer-mood-3de9c056?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-753121?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-753121?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-753121?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-753121?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-753121?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-753121?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-753121?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/u-s-stock-futures-rise-as-sliding-vix-signals-calmer-mood-3de9c056?mod=mw_quote_news">
                                    
                                    
                                    S&amp;P 500 logs highest close in 3 weeks, powered by tech stocks and calm in banking sector
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-29T16:24:00">Mar. 29, 2023 at 4:24 p.m. ET</span>

                            <span class="article__author">by Frances Yue</span>
                        
                    </div>
                </div>
            </div>





            <div data-timestamp="1680112860000" data-docid="" data-msgid="" data-guid="20c06575-04d4-b545-71c5-a2a74e657a63" class="element element--article   ">
                    <figure class="article__figure">
                        
                        <a class="figure__image" data-video-guid="" href="https://www.marketwatch.com/story/apple-sets-date-for-wwdc-event-where-it-could-unveil-its-new-headset-6170e9de?mod=mw_quote_news" role="presentation" tabindex="-1">
                            <img class="lazyload" data-sizes="auto" alt="Read full story" data-srcset="https://images.mktw.net/im-753528?size=1.777777777777778&amp;width=220 220w,https://images.mktw.net/im-753528?size=1.777777777777778&amp;width=300 300w,https://images.mktw.net/im-753528?size=1.777777777777778&amp;width=460 460w,https://images.mktw.net/im-753528?size=1.777777777777778&amp;width=800 800w,https://images.mktw.net/im-753528?size=1.777777777777778&amp;width=920 920w,https://images.mktw.net/im-753528?size=1.777777777777778&amp;width=1240 1240w,https://images.mktw.net/im-753528?size=1.777777777777778&amp;width=1240 1240w">
                            
                            
                        </a>
                        
                        
                    </figure>
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" href="https://www.marketwatch.com/story/apple-sets-date-for-wwdc-event-where-it-could-unveil-its-new-headset-6170e9de?mod=mw_quote_news">
                                    
                                    
                                    Apple sets date for WWDC event where it could unveil its new headset
                                </a>
                        </h3>
                    

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-29T14:01:00">Mar. 29, 2023 at 2:01 p.m. ET</span>

                            <span class="article__author">by Emily Bary</span>
                        
                    </div>
                </div>
            </div>
                        </div>
                        

                            

                    </div>
                    </mw-scrollable-news-v2>
                <template id="moreHeadlineTemplate">
                    <div data-timestamp data-msgid data-guid class="element element--article">
                        <figure class="article__figure">
                            <a class="figure__image" data-video-guid target="_blank" href="#" role="presentation">
                                <img class="lazyload" alt="Read full story" />
                            </a>
                        </figure>
                        <div class="article__content">
                            <span class="article__label"></span>
                            <h3 class="article__headline">
                                <a class="link" target="_blank" href="#"></a>
                            </h3>
                            <p class="article__summary"></p>
                            <div class="content--secondary">
                                <div class="group group--tickers">
                                    <a class="ticker">
                                        <span class="ticker__symbol"></span>
                                        <bg-quote class="ticker__change" field="percentchange" format="0,0.00%" channel></bg-quote>
                                        <i class="icon"></i>
                                    </a>
                                </div>
                            </div>
                            <ul class="article__details">
                                <li class="article__timestamp"></li>
                                <li class="article__author"></li>
                            </ul>
                        </div>
                    </div>
                </template>
                <template id="headlineListItemDianomiTemplate">
                    <div class="lazyload element element--article dianomi j-dianomi-content">
                        <div class="dianomi_context w100"></div>
                    </div>
                </template>
                <template id="noHeadlinesTemplate">
                    <div class="element element--message">
                            <p class="message__text">No Headlines Available</p>
                        </div>
                </template>
                                </div>
                                <div class="tab__pane  j-tabPane" data-tab-pane="Dow Jones">




                
                    <mw-scrollable-news-v2 natural data-expand="200" class='collection collection--moreHeadlines j-scrollViewport lazyload '>
                    <div class="column column--primary j-moreHeadlineWrapper" data-source="ChartingSymbol" data-channel="DowJonesNetwork" data-channel-id="" data-realtimefeed="" data-layout-position="" data-tracking="mw_quote_news">
                        <div class="collection__elements j-scrollElement">
                            <div></div>
                        </div>
                    </div>
                        <div class="element element--message is-hidden">
                            <p class="message__text">No Headlines Available</p>
                        </div>
                    </mw-scrollable-news-v2>
                <template id="moreHeadlineTemplate">
                    <div data-timestamp data-msgid data-guid class="element element--article">
                        <figure class="article__figure">
                            <a class="figure__image" data-video-guid target="_blank" href="#" role="presentation">
                                <img class="lazyload" alt="Read full story" />
                            </a>
                        </figure>
                        <div class="article__content">
                            <span class="article__label"></span>
                            <h3 class="article__headline">
                                <a class="link" target="_blank" href="#"></a>
                            </h3>
                            <p class="article__summary"></p>
                            <div class="content--secondary">
                                <div class="group group--tickers">
                                    <a class="ticker">
                                        <span class="ticker__symbol"></span>
                                        <bg-quote class="ticker__change" field="percentchange" format="0,0.00%" channel></bg-quote>
                                        <i class="icon"></i>
                                    </a>
                                </div>
                            </div>
                            <ul class="article__details">
                                <li class="article__timestamp"></li>
                                <li class="article__author"></li>
                            </ul>
                        </div>
                    </div>
                </template>
                <template id="headlineListItemDianomiTemplate">
                    <div class="lazyload element element--article dianomi j-dianomi-content">
                        <div class="dianomi_context w100"></div>
                    </div>
                </template>
                <template id="noHeadlinesTemplate">
                    <div class="element element--message">
                            <p class="message__text">No Headlines Available</p>
                        </div>
                </template>
                                </div>
                        </div>
                    </mw-tabs>
                </div>



                        <div class="element element--ad is-loading">
                            <div id="ad-ribbon" class="j-ad">
                                <script>
                                    !function() {
                                        window.__mwads = window.__mwads || {};
                                        window.__mwads.uacQ = window.__mwads.uacQ || [];
                                        window.__mwads.uacQ.push({
                                            options: {
                                                adActivate: true,
                                                adId: 'ad-ribbon',
                                                adUnitPath: '/2/marketwatch.com/investing/quotes/stock/overview',
                                                adSize: [[325,30]],
                                                adSizeMap: {},
                                                adTargeting: {'alert':['volatility050','green']},
                                                adLocation: 'QUOTEBANNER',
                                                isObserve: !false,
                                                observeFromUAC: !false,
                                                triggerPrebid: true,
                                                moatEnabled: true,
                                                collapseAdBeforeFetch: true,
                                                threshold: 0.01
                                            }
                                        });
                                    }();
                                </script>
                            </div>
                        </div>



                <div class="element element--tabs">
                    <mw-tabs>
                        <div class="element__options">
                            <ul role="tablist" class="tabs full-width" data-track-query=".tab__item">
                                    <button role="tab" aria-selected="true" class="tab__item is-selected j-tabItem" data-tab-pane="Other News" data-track-code="Index_Other News">Other News</button>
                                    <button role="tab" aria-selected="" class="tab__item  j-tabItem" data-tab-pane="Press Releases" data-track-code="Index_Press Releases">Press Releases</button>
                            </ul>
                            <div class="results__count"></div>
                        </div>
                        <div class="element__body j-tabPanes">
                                <div class="tab__pane is-active j-tabPane" data-tab-pane="Other News">




                
                    <mw-scrollable-news-v2 natural data-expand="200" class='collection collection--moreHeadlines j-scrollViewport lazyload '>
                    <div class="column column--primary j-moreHeadlineWrapper" data-source="ChartingSymbol" data-total-count="" data-channel="Other" data-channel-id="" data-realtimefeed="" data-layout-position="" data-tracking="mw_quote_news">
                        <div class="collection__elements j-scrollElement">





            <div data-timestamp="1680276416000" data-docid="" data-msgid="" data-guid="8a23322f-d554-4af7-aac2-5db80cc6bffb" class="element element--article no-image    GuruFocuscom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="gurufocus.com" href="https://www.gurufocus.com/news/1973452/paypal-stock-an-absurdly-cheap-fintech-play/?r=4bf001661e6fdd88d0cd7a5659ff9748&mod=mw_quote_news">
                                    
                                    
                                    PayPal Stock: An Absurdly Cheap Fintech Play
                                </a>
                        </h3>
                    <p class="article__summary">PayPal Stock: An Absurdly Cheap Fintech Play</p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T11:26:56">Mar. 31, 2023 at 11:26 a.m. ET</span>

                            
                        <span class="article__provider">on GuruFocus.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680270595000" data-docid="" data-msgid="" data-guid="a86780d8-e6a3-4341-a6db-8b3dbd95e32b" class="element element--article no-image    MotleyFool">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="fool.com" href="https://www.fool.com/investing/2023/03/31/apple-is-still-a-buy-despite-market-rumors/?source=djc&utm_source=djc&utm_medium=feed&utm_campaign=article&mod=mw_quote_news">
                                    
                                    
                                    Apple Is Still a Buy Despite Market Rumors of an Impending Recession
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T09:49:55">Mar. 31, 2023 at 9:49 a.m. ET</span>

                            
                        <span class="article__provider">on Motley Fool</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680269460000" data-docid="" data-msgid="" data-guid="fdbd1220-173c-45b5-af35-1d5888921bfa" class="element element--article no-image    Zackscom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="zacks.com" href="https://www.zacks.com/stock/news/2073009/stock-market-news-for-mar-31-2023?cid=CS-MKTWTCH-HL-market_news-2073009&mod=mw_quote_news">
                                    
                                    
                                    Stock Market News for Mar 31, 2023
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T09:31:00">Mar. 31, 2023 at 9:31 a.m. ET</span>

                            
                        <span class="article__provider">on Zacks.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680267600000" data-docid="" data-msgid="" data-guid="087eab4a-c760-40bb-aac5-bed32799ce48" class="element element--article no-image    MotleyFool">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="fool.com" href="https://www.fool.com/investing/2023/03/31/3-things-about-apple-that-smart-investors-know/?source=djc&utm_source=djc&utm_medium=feed&utm_campaign=article&mod=mw_quote_news">
                                    
                                    
                                    3 Things About Apple That Smart Investors Know
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T09:00:00">Mar. 31, 2023 at 9:00 a.m. ET</span>

                            
                        <span class="article__provider">on Motley Fool</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680264919000" data-docid="" data-msgid="" data-guid="81debff7-71a2-41f0-90ff-ac81bad73654" class="element element--article no-image    Benzingacom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="benzinga.com" href="https://www.benzinga.com/news/earnings/23/03/31606909/tesla-recalls-some-semi-trucks-ford-slams-brakes-on-self-driving-dreams-tiktok-founder-meets-walmar?utm_campaign=partner_feed&utm_source=MarketWatch&utm_medium=partner_feed&utm_content=site&mod=mw_quote_news">
                                    
                                    
                                    Tesla Recalls Some Semi-Trucks, Ford Slams Brakes On Self-Driving Dreams, TikTok Founder Meets Walmart Chief Privately: Today&#x27;s Top Stories
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T08:15:19">Mar. 31, 2023 at 8:15 a.m. ET</span>

                            
                        <span class="article__provider">on Benzinga.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680264539000" data-docid="" data-msgid="" data-guid="4b056c0e-8073-4d92-9198-201c61d82367" class="element element--article no-image    Benzingacom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="benzinga.com" href="https://www.benzinga.com/trading-ideas/long-ideas/23/03/31603950/if-you-invested-1000-in-apple-when-it-released-its-watch-8-years-ago-heres-how-much-youd?utm_campaign=partner_feed&utm_source=MarketWatch&utm_medium=partner_feed&utm_content=site&mod=mw_quote_news">
                                    
                                    
                                    If You Invested $1000 In Apple When It Released Its Watch 8 Years Ago, Here&#x27;s How Much You&#x27;d Have Now
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T08:08:59">Mar. 31, 2023 at 8:08 a.m. ET</span>

                            
                        <span class="article__provider">on Benzinga.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680264000000" data-docid="" data-msgid="" data-guid="d5b7216b-93ea-4033-b5ae-b3516cd9624a" class="element element--article no-image    MotleyFool">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="fool.com" href="https://www.fool.com/investing/2023/03/31/which-is-the-better-dividend-stock-viatris-or-appl/?source=djc&utm_source=djc&utm_medium=feed&utm_campaign=article&mod=mw_quote_news">
                                    
                                    
                                    Which Is the Better Dividend Stock: Viatris or Apple?
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T08:00:00">Mar. 31, 2023 at 8:00 a.m. ET</span>

                            
                        <span class="article__provider">on Motley Fool</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680260400000" data-docid="" data-msgid="" data-guid="7e0d7345-233f-467c-be65-b071b6cfbb15" class="element element--article no-image    MotleyFool">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="fool.com" href="https://www.fool.com/investing/2023/03/31/have-3000-these-3-stocks-could-be-bargains-for-202/?source=djc&utm_source=djc&utm_medium=feed&utm_campaign=article&mod=mw_quote_news">
                                    
                                    
                                    Have $3,000? These 3 Stocks Could Be Bargains for 2023 and Beyond
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T07:00:00">Mar. 31, 2023 at 7:00 a.m. ET</span>

                            
                        <span class="article__provider">on Motley Fool</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680259751000" data-docid="" data-msgid="" data-guid="b5eaaf76-e1f4-41df-a9f5-5509d0dfa007" class="element element--article no-image    Benzingacom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="benzinga.com" href="https://www.benzinga.com/news/23/03/31604873/us-appeals-court-rules-in-favor-of-apple-in-patent-infringement-case-against-virnetx?utm_campaign=partner_feed&utm_source=MarketWatch&utm_medium=partner_feed&utm_content=site&mod=mw_quote_news">
                                    
                                    
                                    US Appeals Court Rules In Favor Of Apple In Patent Infringement Case Against VirnetX
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T06:49:11">Mar. 31, 2023 at 6:49 a.m. ET</span>

                            
                        <span class="article__provider">on Benzinga.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680258009000" data-docid="" data-msgid="" data-guid="6d395263-79af-4413-b437-370e8c722b96" class="element element--article no-image    Zackscom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="zacks.com" href="https://www.zacks.com/stock/news/2072826/is-wisdomtree-u-s-total-dividend-etf-dtd-a-strong-etf-right-now?cid=CS-MKTWTCH-HL-smart_beta_etf-2072826&mod=mw_quote_news">
                                    
                                    
                                    Is WisdomTree U.S. Total Dividend ETF (DTD) a Strong ETF Right Now?
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T06:20:09">Mar. 31, 2023 at 6:20 a.m. ET</span>

                            
                        <span class="article__provider">on Zacks.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680258006000" data-docid="" data-msgid="" data-guid="b1b190ba-17b5-478e-8351-d61a020cb2cb" class="element element--article no-image    Zackscom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="zacks.com" href="https://www.zacks.com/stock/news/2072833/should-invesco-s-p-500-top-50-etf-xlg-be-on-your-investing-radar?cid=CS-MKTWTCH-HL-style_box_etf-2072833&mod=mw_quote_news">
                                    
                                    
                                    Should Invesco S&amp;P 500 Top 50 ETF (XLG) Be on Your Investing Radar?
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T06:20:06">Mar. 31, 2023 at 6:20 a.m. ET</span>

                            
                        <span class="article__provider">on Zacks.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680253560000" data-docid="" data-msgid="" data-guid="544c4796-c80a-4e4a-b92f-99698d52017d" class="element element--article no-image    MotleyFool">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="fool.com" href="https://www.fool.com/investing/2023/03/31/87-warren-buffett-6-billion-dividend-from-7-stocks/?source=djc&utm_source=djc&utm_medium=feed&utm_campaign=article&mod=mw_quote_news">
                                    
                                    
                                    87% of Warren Buffett&#x27;s More Than $6.1 Billion in Dividend Income Comes From These 7 Stocks
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T05:06:00">Mar. 31, 2023 at 5:06 a.m. ET</span>

                            
                        <span class="article__provider">on Motley Fool</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680240998000" data-docid="" data-msgid="" data-guid="bafa4e27-9385-4722-a988-4aabf7caaab0" class="element element--article no-image    Benzingacom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="benzinga.com" href="https://www.benzinga.com/analyst-ratings/analyst-color/23/03/31603133/will-we-miss-out-on-next-iphone-moment-apple-analysts-see-armr-headset-hurdles?utm_campaign=partner_feed&utm_source=MarketWatch&utm_medium=partner_feed&utm_content=site&mod=mw_quote_news">
                                    
                                    
                                    Will We Miss Out On Next &#x27;iPhone Moment?&#x27; Apple Analysts See AR/MR Headset Hurdles
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T01:36:38">Mar. 31, 2023 at 1:36 a.m. ET</span>

                            
                        <span class="article__provider">on Benzinga.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680237952000" data-docid="" data-msgid="" data-guid="a5df3071-a09b-4464-bd7d-32c9dafca054" class="element element--article no-image    Benzingacom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="benzinga.com" href="https://www.benzinga.com/news/23/03/31602975/apple-tv-users-get-access-to-neflixs-cheap-plan-albeit-with-ads?utm_campaign=partner_feed&utm_source=MarketWatch&utm_medium=partner_feed&utm_content=site&mod=mw_quote_news">
                                    
                                    
                                    Apple TV Users Get Access To Neflix&#x27;s Cheap Plan...Albeit With Ads
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-31T00:45:52">Mar. 31, 2023 at 12:45 a.m. ET</span>

                            
                        <span class="article__provider">on Benzinga.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680230673000" data-docid="" data-msgid="" data-guid="d822d5d2-ab0a-4422-ad19-f2306243d552" class="element element--article no-image    Benzingacom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="benzinga.com" href="https://www.benzinga.com/news/23/01/30458620/iphone-13-might-be-most-popular-smartphone-sold-in-us-but-bill-gates-is-happy-with-this-device-1?utm_campaign=partner_feed&utm_source=MarketWatch&utm_medium=partner_feed&utm_content=site&mod=mw_quote_news">
                                    
                                    
                                    The Time Bill Gates Revealed His Choice Of Smartphone &#x2014; It Was This Foldable, Not An iPhone
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T22:44:33">Mar. 30, 2023 at 10:44 p.m. ET</span>

                            
                        <span class="article__provider">on Benzinga.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680226353000" data-docid="" data-msgid="" data-guid="c5ee4f04-ae4d-4d98-b803-f54afd16d71d" class="element element--article no-image    TipRankscom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="tipranks.com" href="https://www.tipranks.com/news/article/3-payment-tech-stocks-wall-street-is-bullish-on?mod=mw_quote_news">
                                    
                                    
                                    3 Payment Tech Stocks Wall Street is Bullish On
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T21:32:33">Mar. 30, 2023 at 9:32 p.m. ET</span>

                            
                        <span class="article__provider">on TipRanks.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680214020000" data-docid="" data-msgid="" data-guid="8cccc738-966e-45d9-b837-db854170cce5" class="element element--article no-image    Zackscom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="zacks.com" href="https://www.zacks.com/stock/news/2072685/mini-rally-in-place-ahead-of-q1-end-pce-numbers?cid=CS-MKTWTCH-HL-ahead_of_wall_street-2072685&mod=mw_quote_news">
                                    
                                    
                                    Mini-Rally in Place Ahead of Q1 End, PCE Numbers
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T18:07:00">Mar. 30, 2023 at 6:07 p.m. ET</span>

                            
                        <span class="article__provider">on Zacks.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680210040000" data-docid="" data-msgid="" data-guid="4164899d-59e6-455a-bf3c-2bbcd52b3544" class="element element--article no-image    InvestorPlacecom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="investorplace.com" href="https://investorplace.com/2023/03/friday-predictions-3-hot-stocks-for-tomorrow-3/?mod=mw_quote_news">
                                    
                                    
                                    Friday Predictions: 3 Hot Stocks for Tomorrow
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T17:00:40">Mar. 30, 2023 at 5:00 p.m. ET</span>

                            
                        <span class="article__provider">on InvestorPlace.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680210037000" data-docid="" data-msgid="" data-guid="d7c016a7-3b1b-4c28-97b1-b54df1509528" class="element element--article no-image    Benzingacom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="benzinga.com" href="https://www.benzinga.com/analyst-ratings/23/03/31597837/analyst-ratings-for-apple?utm_campaign=partner_feed&utm_source=MarketWatch&utm_medium=partner_feed&utm_content=site&mod=mw_quote_news">
                                    
                                    
                                    Analyst Ratings for Apple
                                </a>
                        </h3>
                    <p class="article__summary"></p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T17:00:37">Mar. 30, 2023 at 5:00 p.m. ET</span>

                            
                        <span class="article__provider">on Benzinga.com</span>
                    </div>
                </div>
            </div>





            <div data-timestamp="1680205705000" data-docid="" data-msgid="" data-guid="37323f84-d575-4651-9981-39b33c3b7f87" class="element element--article no-image    GuruFocuscom">
                    
                <div class="article__content">

                        <h3 class="article__headline">
                            
                            
                                <a class="link" rel="nofollow" target="_blank" data-source="gurufocus.com" href="https://www.gurufocus.com/news/1973119/announcing-gurufocus-enhanced-technical-indicators-feature/?r=4bf001661e6fdd88d0cd7a5659ff9748&mod=mw_quote_news">
                                    
                                    
                                    Announcing GuruFocus&#x27; Enhanced Technical Indicators Feature
                                </a>
                        </h3>
                    <p class="article__summary">Announcing GuruFocus&#x27; Enhanced Technical Indicators Feature</p>

                    

                    <div class="article__details">
                        <span class="article__timestamp" data-est="2023-03-30T15:48:25">Mar. 30, 2023 at 3:48 p.m. ET</span>

                            
                        <span class="article__provider">on GuruFocus.com</span>
                    </div>
                </div>
            </div>
                        </div>
                        

                            

                    </div>
                    </mw-scrollable-news-v2>
                <template id="moreHeadlineTemplate">
                    <div data-timestamp data-msgid data-guid class="element element--article">
                        <figure class="article__figure">
                            <a class="figure__image" data-video-guid target="_blank" href="#" role="presentation">
                                <img class="lazyload" alt="Read full story" />
                            </a>
                        </figure>
                        <div class="article__content">
                            <span class="article__label"></span>
                            <h3 class="article__headline">
                                <a class="link" target="_blank" href="#"></a>
                            </h3>
                            <p class="article__summary"></p>
                            <div class="content--secondary">
                                <div class="group group--tickers">
                                    <a class="ticker">
                                        <span class="ticker__symbol"></span>
                                        <bg-quote class="ticker__change" field="percentchange" format="0,0.00%" channel></bg-quote>
                                        <i class="icon"></i>
                                    </a>
                                </div>
                            </div>
                            <ul class="article__details">
                                <li class="article__timestamp"></li>
                                <li class="article__author"></li>
                            </ul>
                        </div>
                    </div>
                </template>
                <template id="headlineListItemDianomiTemplate">
                    <div class="lazyload element element--article dianomi j-dianomi-content">
                        <div class="dianomi_context w100"></div>
                    </div>
                </template>
                <template id="noHeadlinesTemplate">
                    <div class="element element--message">
                            <p class="message__text">No Headlines Available</p>
                        </div>
                </template>
                                </div>
                                <div class="tab__pane  j-tabPane" data-tab-pane="Press Releases">




                
                    <mw-scrollable-news-v2 natural data-expand="200" class='collection collection--moreHeadlines j-scrollViewport lazyload '>
                    <div class="column column--primary j-moreHeadlineWrapper" data-source="ChartingSymbol" data-channel="PressReleases" data-channel-id="" data-realtimefeed="" data-layout-position="" data-tracking="mw_quote_news">
                        <div class="collection__elements j-scrollElement">
                            <div></div>
                        </div>
                    </div>
                        <div class="element element--message is-hidden">
                            <p class="message__text">No Headlines Available</p>
                        </div>
                    </mw-scrollable-news-v2>
                <template id="moreHeadlineTemplate">
                    <div data-timestamp data-msgid data-guid class="element element--article">
                        <figure class="article__figure">
                            <a class="figure__image" data-video-guid target="_blank" href="#" role="presentation">
                                <img class="lazyload" alt="Read full story" />
                            </a>
                        </figure>
                        <div class="article__content">
                            <span class="article__label"></span>
                            <h3 class="article__headline">
                                <a class="link" target="_blank" href="#"></a>
                            </h3>
                            <p class="article__summary"></p>
                            <div class="content--secondary">
                                <div class="group group--tickers">
                                    <a class="ticker">
                                        <span class="ticker__symbol"></span>
                                        <bg-quote class="ticker__change" field="percentchange" format="0,0.00%" channel></bg-quote>
                                        <i class="icon"></i>
                                    </a>
                                </div>
                            </div>
                            <ul class="article__details">
                                <li class="article__timestamp"></li>
                                <li class="article__author"></li>
                            </ul>
                        </div>
                    </div>
                </template>
                <template id="headlineListItemDianomiTemplate">
                    <div class="lazyload element element--article dianomi j-dianomi-content">
                        <div class="dianomi_context w100"></div>
                    </div>
                </template>
                <template id="noHeadlinesTemplate">
                    <div class="element element--message">
                            <p class="message__text">No Headlines Available</p>
                        </div>
                </template>
                                </div>
                        </div>
                    </mw-tabs>
                </div>

            <div class="element element--description description__long">
                <header class="header header--secondary">
                    <h2 class="title">
                        <span class="label">Apple Inc.</span>
                    </h2>
                </header>

                    <p class="description__text">Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services. It operates through the following geographical segments: Americas, Europe, Greater China, Japan, and Rest of Asia Pacific. The Americas segment includes North and South America. The Europe segment consists of European countries, as well as India, the Middle East, and Africa. The Greater China segment comprises China, Hong Kong, and Taiwan. The Rest of Asia Pacific segment includes Australia and Asian countries. Its products and services include iPhone, Mac, iPad, AirPods, Apple TV, Apple Watch, Beats products, AppleCare, iCloud, digital content stores, streaming, and licensing services. The company was founded by Steven Paul Jobs, Ronald Gerald Wayne, and Stephen G. Wozniak in April 1976 and is headquartered in Cupertino, CA.</p>
            </div>
                    
                    
                    </div>
                    <div class="column column--aside">


                    <div class="group group--elements left">




            <div class="element element--table overflow--table Competitors">
                    <header class="header header--secondary">
                        <h2 class="title">
                            <span class="label">Competitors</span>
                        </h2>
                    </header>
                    <table class="table table--primary align--right" aria-label="Competitors data table">
                        <thead class="table__head">
                            <tr class="table__row">
                                <th class="table__heading">Name</th>
                                <th class="table__heading">Chg %</th>
                                <th class="table__heading">Market Cap</th>
                            </tr>
                        </thead>
                        <tbody class="table__body">
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/msft?mod=mw_quote_competitors">Microsoft Corp.</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/207732364/composite" class="positive">1.26%</bg-quote></td>
                                    <td class="table__cell w25 number">$2.09T</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/goog?mod=mw_quote_competitors">Alphabet Inc. Cl C</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/205453964/composite" class="negative">-0.57%</bg-quote></td>
                                    <td class="table__cell w25 number">$1.3T</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/googl?mod=mw_quote_competitors">Alphabet Inc. Cl A</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/202490156/lastsale" class="negative">-0.49%</bg-quote></td>
                                    <td class="table__cell w25 number">$1.3T</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/amzn?mod=mw_quote_competitors">Amazon.com Inc.</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/210331248/composite" class="positive">1.75%</bg-quote></td>
                                    <td class="table__cell w25 number">$1.03T</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/meta?mod=mw_quote_competitors">Meta Platforms Inc.</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/205064656/composite" class="positive">1.21%</bg-quote></td>
                                    <td class="table__cell w25 number">$532.42B</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/005930?countrycode=kr&mod=mw_quote_competitors">Samsung Electronics Co. Ltd.</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/209800866/delayed" class="positive">1.27%</bg-quote></td>
                                    <td class="table__cell w25 number">&#x20A9;418.17T</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/005935?countrycode=kr&mod=mw_quote_competitors">Samsung Electronics Co. Ltd. Pfd. Series 1</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/200586282/delayed" class="positive">0.94%</bg-quote></td>
                                    <td class="table__cell w25 number">&#x20A9;418.17T</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/6758?countrycode=jp&mod=mw_quote_competitors">Sony Group Corp.</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/201361720/delayed" class="positive">2.13%</bg-quote></td>
                                    <td class="table__cell w25 number">&#xA5;14.26T</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/dell?mod=mw_quote_competitors">Dell Technologies Inc. Cl C</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/203822527/composite" class="positive">1.89%</bg-quote></td>
                                    <td class="table__cell w25 number">$28.01B</td>
                                </tr>
                                <tr class="table__row">
                                    <td class="table__cell w50"><a class="link" href="https://www.marketwatch.com/investing/stock/hpq?mod=mw_quote_competitors">HP Inc.</a></td>
                                    <td class="table__cell w25"><bg-quote field="percentchange" format="0,0.00%" channel="/zigman2/quotes/203461582/composite" class="positive">2.08%</bg-quote></td>
                                    <td class="table__cell w25 number">$27.89B</td>
                                </tr>
                        </tbody>
                    </table>
            </div>
                    </div>
                    
                    </div>
                    </div>
                    <div class="region region--full belt-ad">


                    <div class="column column--full">





                        <div class="element element--ad is-loading">
                            <div id="ad-belt" class="j-ad">
                                <script>
                                    !function() {
                                        window.__mwads = window.__mwads || {};
                                        window.__mwads.uacQ = window.__mwads.uacQ || [];
                                        window.__mwads.uacQ.push({
                                            options: {
                                                adActivate: true,
                                                adId: 'ad-belt',
                                                adUnitPath: '/2/bottom.marketwatch.com/investing/quotes/stock/overview',
                                                adSize: [[970,250],[728,90]],
                                                adSizeMap: {'at4units':[],'at12units':[[970,250],[728,90]]},
                                                adTargeting: {'alert':['volatility050','green']},
                                                adLocation: 'BANNERBOTTOM',
                                                isObserve: !false,
                                                observeFromUAC: !false,
                                                triggerPrebid: true,
                                                moatEnabled: true,
                                                collapseAdBeforeFetch: true,
                                                threshold: 0.01
                                            }
                                        });
                                    }();
                                </script>
                            </div>
                        </div>
                    </div>
                    </div>
            </div>

                <div class="container container--sponsored">

        <div class="container container--sponsored j-dianomi-content">
            <div class="region region--full">
                <section class="component component--module sponsored-content">
                    <div class="column column--primary" role="complementary" aria-label="Advertisement">
                            <div class="element element--sponsor" aria-hidden="true">
                                <header class="header header--secondary">
                                    <h2 class="title">
                                        <span class="label">Advertisement</span>
                                    </h2>
                                </header>
                                <div class="dianomi_context" data-dianomi-context-id="1294"></div>
                            </div>
                    </div>

                    <div class="column column--aside" role="complementary" aria-label="Advertisement">
                        <div class="element element--sponsor">
                                <header class="header header--secondary">
                                    <h2 class="title">
                                        <span class="label">Advertisement</span>
                                    </h2>
                                </header>
                                <div class="dianomi_context" data-dianomi-context-id="1298"></div>
                        </div>
                    </div>
                </section>
            </div>
        </div>

                </div>


        <div class="container container--sponsored">




            <input type="hidden" id="VendorWidgetView" value="" />

        </div>


        <div class="overlay"></div>
        <div class="region region--lightbox j-ajaxContent">
        <div class="lightbox lightbox--template">
            <div class="column column--full j-content">
            </div>
        </div>
        </div>









        <!-- tealium tracking -->
        <script>
        var utag_data = {
        "page_access":"free","page_content_source":"MarketWatch","page_site":"MarketWatch","page_site_product":"MW","page_content_type":"ResearchTools","page_content_type_detail":"quote","page_section":"Company Research","page_name":"Quote_Page","page_subsection":"Company Overview","reengagement_refresh":"on","user_type":"nonsubscriber","page_ad_zone":"investing/quotes/stock/overview","quote_ticker":"AAPL","quote_company_name":"Apple Inc.","quote_exchange":"U.S.: Nasdaq","quote_instrument_type":"Stock"};
        var utag_dataOriginal = {}; 
        (function () {
            for (var prop in utag_data) {
                utag_dataOriginal[prop] = utag_data[prop];
            }
            Object.freeze(utag_dataOriginal);
        })();
        </script>
        <!-- end tealium tracking -->
        <script>
        var trackingPageInfo = {
            action: 'Index'
        };
        </script>

            



        <footer class="container container--footer full-width" aria-label="site footer">
            <button class="btn btn--primary btn--top js--top">Back to Top</button>
            <div class="region region--full">
                <div class="column column--full">
                    <div class="group group--footer-info">
                        <a class="logo logo--footer" href="https://www.marketwatch.com/"><svg width="209" height="51" viewBox="0 0 209 51" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M49.756 12.3077L49.3964 14.0501H49.3134C48.8709 13.0545 47.6263 11.7269 44.9159 11.7269C40.5183 11.7269 35.9825 15.1564 34.9868 20.5497C34.1294 25.2791 36.3974 29.4001 41.6523 29.4001C43.5883 29.4001 45.7733 28.6533 46.9349 27.0492H47.0179L46.7136 28.8193H51.609L54.679 12.3354L49.756 12.3077ZM48.1795 20.5497C47.8753 22.1538 46.3264 24.8089 43.2564 24.8089C40.1865 24.8089 39.6333 22.1815 39.9099 20.6326C40.2694 18.7519 41.9565 16.3734 44.8053 16.3734C47.654 16.3734 48.539 18.5583 48.1795 20.5497Z" fill="white"/>
        <path d="M57.3895 12.3077H62.0083L61.7041 14.0501H61.787C62.3678 13.2481 63.5295 11.7269 66.3505 11.7269L65.4378 16.7329C63.1146 16.7606 61.4275 17.2584 60.985 19.7752L59.2978 28.8193H54.3471L57.3895 12.3077Z" fill="white"/>
        <path d="M69.6418 5.8635H74.5925L72.2693 18.2818H72.3523L78.0774 12.3077H83.8855L76.3349 19.554L80.6772 28.8193H75.0627L71.8821 20.8539H71.7991L70.3609 28.8193H65.3825L69.6418 5.8635Z" fill="white"/>
        <path d="M91.7955 11.7269C86.7895 11.7269 82.3366 16.0138 81.5069 20.6326C80.5942 25.528 83.9131 29.3724 88.6425 29.3724C90.3296 29.3724 92.0721 28.8469 93.5932 27.8789C95.1697 26.9386 96.5802 25.528 97.7419 23.675H92.7082C91.8784 24.5324 90.9381 25.1961 89.3893 25.1961C87.4532 25.1961 86.0427 24.0622 86.1257 22.0985H98.4886C98.6546 21.7113 98.7099 21.4347 98.8482 20.7986C99.7885 15.7372 96.8568 11.7269 91.7955 11.7269ZM86.8171 18.7243C87.2043 17.7286 88.5595 15.8755 91.104 15.8755C93.6485 15.8755 94.2847 17.7286 94.2847 18.7243H86.8171Z" fill="white"/>
        <path d="M28.432 5.86339L19.7199 18.9178H19.6369V5.86339H15.4329L0 28.8192H5.97404L14.6309 15.7371H14.7138V28.8192H18.9731L27.6299 15.7371H27.7129V28.8192H32.6636V5.86339H28.432Z" fill="white"/>
        <path d="M111.377 12.3077H108.279L109.192 7.43997H104.85L104.49 9.32069C104.103 11.478 102.748 12.1141 100.95 12.3077H100.923L100.203 16.0415H102.637L100.286 28.7916H105.209L107.56 16.0415H110.713L111.377 12.3077Z" fill="white"/>
        <path d="M187.74 22.5409C186.135 26.2747 182.263 29.3447 177.811 29.3447C172.805 29.3447 169.707 25.4173 170.592 20.4943C171.505 15.6542 175.985 11.7268 180.936 11.7268C185.306 11.7268 188.293 14.6309 188.376 18.6965H183.37C183.066 17.5626 182.319 16.3733 180.217 16.3733C177.894 16.2627 175.958 18.1987 175.543 20.5496C175.1 22.9558 176.317 24.7535 178.696 24.7535C180.742 24.7535 181.959 23.5643 182.678 22.5409H187.74ZM146.834 0L137.237 5.86341H139.947L131.235 18.9454H131.152V5.86341H126.893L118.181 18.9454H118.098V5.86341H113.147V28.8192H117.434L126.146 15.7372H126.229V28.8192H130.488L145.894 5.86341H148.328L146.834 0ZM156.21 28.8192H151.342L151.646 27.0491H151.564C150.43 28.6532 148.217 29.4 146.281 29.4C141.054 29.4 138.758 25.279 139.615 20.5496C140.611 15.1563 145.119 11.7268 149.545 11.7268C152.255 11.7268 153.527 13.0544 153.942 14.05H154.025L154.385 12.3076H159.28L156.21 28.8192ZM147.913 24.7812C150.983 24.7812 152.532 22.1537 152.836 20.5219C153.195 18.5582 152.255 16.3456 149.462 16.3456C146.668 16.3456 144.926 18.6965 144.566 20.6049C144.29 22.1537 144.898 24.7812 147.913 24.7812ZM171.643 12.3076H168.545L169.458 7.43989H165.116L164.756 9.3206C164.369 11.4779 163.014 12.114 161.216 12.3076H161.188L160.469 16.0414H162.903L160.552 28.7915H165.475L167.826 16.0414H170.979L171.643 12.3076ZM192.386 5.86341H197.309L195.816 14.05H195.899C196.95 12.5012 198.388 11.7268 200.545 11.7268C202.122 11.7268 203.892 12.3076 204.721 13.5799C205.772 15.184 205.662 16.6499 205.109 19.6092L203.421 28.8192H198.498L200.158 19.8305C200.324 19.0284 200.794 16.3733 198.139 16.3733C195.484 16.3733 194.903 18.8625 194.765 19.6922L193.078 28.8192H188.154L192.386 5.86341Z" fill="#48A838"/>
        <path d="M206.906 25.8321C207.736 25.8321 208.4 26.5236 208.4 27.3533C208.4 28.183 207.736 28.8745 206.906 28.8745C206.077 28.8745 205.413 28.2107 205.413 27.3533C205.385 26.5236 206.049 25.8321 206.906 25.8321ZM206.879 26.0811C206.187 26.0811 205.662 26.6619 205.662 27.3257C205.662 27.9894 206.215 28.5702 206.906 28.5702C207.598 28.5702 208.123 28.0171 208.123 27.3257C208.123 26.6342 207.598 26.0811 206.879 26.0811ZM206.962 26.4959C207.238 26.4959 207.57 26.6066 207.57 26.9661C207.57 27.1321 207.515 27.2703 207.293 27.381C207.459 27.4363 207.542 27.5469 207.542 27.7682C207.57 28.0724 207.57 28.1001 207.598 28.183H207.266C207.238 28.1277 207.21 27.9065 207.21 27.7682C207.21 27.6299 207.183 27.4916 206.851 27.4916H206.602V28.183H206.27V26.4959H206.962ZM206.602 26.7448V27.2703H206.879C206.989 27.2703 207.238 27.2703 207.238 26.9938C207.238 26.7448 207.017 26.7448 206.906 26.7448H206.602Z" fill="#48A838"/>
        <path d="M6.23 48.4H5.677C5.55567 48.4 5.45767 48.3814 5.383 48.344C5.30833 48.3067 5.25933 48.2274 5.236 48.106L5.096 47.448C4.90933 47.616 4.72733 47.7677 4.55 47.903C4.37267 48.0337 4.186 48.1457 3.99 48.239C3.794 48.3277 3.584 48.3954 3.36 48.442C3.14067 48.4887 2.89567 48.512 2.625 48.512C2.34967 48.512 2.09067 48.4747 1.848 48.4C1.61 48.3207 1.40233 48.204 1.225 48.05C1.04767 47.896 0.905333 47.7024 0.798 47.469C0.695333 47.231 0.644 46.951 0.644 46.629C0.644 46.349 0.721 46.0807 0.875 45.824C1.029 45.5627 1.27633 45.3317 1.617 45.131C1.96233 44.9304 2.41267 44.767 2.968 44.641C3.52333 44.5104 4.20233 44.4357 5.005 44.417V43.864C5.005 43.3134 4.886 42.898 4.648 42.618C4.41467 42.3334 4.067 42.191 3.605 42.191C3.30167 42.191 3.045 42.2307 2.835 42.31C2.62967 42.3847 2.45 42.471 2.296 42.569C2.14667 42.6624 2.016 42.7487 1.904 42.828C1.79667 42.9027 1.68933 42.94 1.582 42.94C1.498 42.94 1.42333 42.919 1.358 42.877C1.29733 42.8304 1.24833 42.7744 1.211 42.709L0.987 42.31C1.379 41.932 1.80133 41.6497 2.254 41.463C2.70667 41.2764 3.20833 41.183 3.759 41.183C4.15567 41.183 4.508 41.2484 4.816 41.379C5.124 41.5097 5.383 41.6917 5.593 41.925C5.803 42.1584 5.96167 42.4407 6.069 42.772C6.17633 43.1034 6.23 43.4674 6.23 43.864V48.4ZM2.996 47.637C3.21533 47.637 3.416 47.616 3.598 47.574C3.78 47.5274 3.95033 47.4644 4.109 47.385C4.27233 47.301 4.42633 47.2007 4.571 47.084C4.72033 46.9674 4.865 46.8344 5.005 46.685V45.208C4.431 45.2267 3.94333 45.2734 3.542 45.348C3.14067 45.418 2.814 45.5114 2.562 45.628C2.31 45.7447 2.12567 45.8824 2.009 46.041C1.897 46.1997 1.841 46.377 1.841 46.573C1.841 46.7597 1.87133 46.9207 1.932 47.056C1.99267 47.1914 2.07433 47.3034 2.177 47.392C2.27967 47.476 2.401 47.539 2.541 47.581C2.681 47.6184 2.83267 47.637 2.996 47.637Z" fill="white"/>
        <path d="M19.7147 43.388C19.7147 44.1394 19.5957 44.823 19.3577 45.439C19.1197 46.055 18.7837 46.5824 18.3497 47.021C17.9157 47.4597 17.3954 47.8004 16.7887 48.043C16.1821 48.281 15.5101 48.4 14.7727 48.4H11.0207V38.369H14.7727C15.5101 38.369 16.1821 38.4904 16.7887 38.733C17.3954 38.971 17.9157 39.3117 18.3497 39.755C18.7837 40.1937 19.1197 40.721 19.3577 41.337C19.5957 41.953 19.7147 42.6367 19.7147 43.388ZM18.3217 43.388C18.3217 42.772 18.2377 42.2214 18.0697 41.736C17.9017 41.2507 17.6637 40.84 17.3557 40.504C17.0477 40.168 16.6744 39.9114 16.2357 39.734C15.7971 39.5567 15.3094 39.468 14.7727 39.468H12.3857V47.301H14.7727C15.3094 47.301 15.7971 47.2124 16.2357 47.035C16.6744 46.8577 17.0477 46.6034 17.3557 46.272C17.6637 45.936 17.9017 45.5254 18.0697 45.04C18.2377 44.5547 18.3217 44.004 18.3217 43.388Z" fill="white"/>
        <path d="M24.2358 41.197C24.7537 41.197 25.2204 41.2834 25.6357 41.456C26.0557 41.6287 26.4104 41.8737 26.6998 42.191C26.9938 42.5084 27.2178 42.8934 27.3717 43.346C27.5304 43.794 27.6098 44.2957 27.6098 44.851C27.6098 45.411 27.5304 45.915 27.3717 46.363C27.2178 46.811 26.9938 47.1937 26.6998 47.511C26.4104 47.8284 26.0557 48.0734 25.6357 48.246C25.2204 48.414 24.7537 48.498 24.2358 48.498C23.7178 48.498 23.2488 48.414 22.8288 48.246C22.4134 48.0734 22.0588 47.8284 21.7647 47.511C21.4707 47.1937 21.2444 46.811 21.0858 46.363C20.9271 45.915 20.8477 45.411 20.8477 44.851C20.8477 44.2957 20.9271 43.794 21.0858 43.346C21.2444 42.8934 21.4707 42.5084 21.7647 42.191C22.0588 41.8737 22.4134 41.6287 22.8288 41.456C23.2488 41.2834 23.7178 41.197 24.2358 41.197ZM24.2358 47.525C24.9358 47.525 25.4584 47.2917 25.8038 46.825C26.1491 46.3537 26.3218 45.698 26.3218 44.858C26.3218 44.0134 26.1491 43.3554 25.8038 42.884C25.4584 42.4127 24.9358 42.177 24.2358 42.177C23.8811 42.177 23.5731 42.2377 23.3118 42.359C23.0504 42.4804 22.8311 42.6554 22.6537 42.884C22.4811 43.1127 22.3504 43.395 22.2617 43.731C22.1777 44.0624 22.1357 44.438 22.1357 44.858C22.1357 45.278 22.1777 45.6537 22.2617 45.985C22.3504 46.3164 22.4811 46.5964 22.6537 46.825C22.8311 47.049 23.0504 47.2217 23.3118 47.343C23.5731 47.4644 23.8811 47.525 24.2358 47.525Z" fill="white"/>
        <path d="M28.221 41.309H29.201C29.3037 41.309 29.3877 41.3347 29.453 41.386C29.5184 41.4374 29.5627 41.498 29.586 41.568L30.944 46.132C30.9814 46.3 31.0164 46.4634 31.049 46.622C31.0817 46.776 31.1097 46.9324 31.133 47.091C31.1704 46.9324 31.2124 46.776 31.259 46.622C31.3057 46.4634 31.3547 46.3 31.406 46.132L32.904 41.54C32.9274 41.47 32.967 41.4117 33.023 41.365C33.0837 41.3184 33.1584 41.295 33.247 41.295H33.786C33.8794 41.295 33.9564 41.3184 34.017 41.365C34.0777 41.4117 34.1197 41.47 34.143 41.54L35.606 46.132C35.6574 46.2954 35.7017 46.4564 35.739 46.615C35.781 46.7737 35.8207 46.93 35.858 47.084C35.8814 46.93 35.9117 46.769 35.949 46.601C35.9864 46.433 36.026 46.2767 36.068 46.132L37.454 41.568C37.4774 41.4934 37.5217 41.4327 37.587 41.386C37.6524 41.3347 37.7294 41.309 37.818 41.309H38.756L36.46 48.4H35.473C35.3517 48.4 35.2677 48.3207 35.221 48.162L33.653 43.353C33.6157 43.2457 33.5854 43.1384 33.562 43.031C33.5387 42.919 33.5154 42.8094 33.492 42.702C33.4687 42.8094 33.4454 42.919 33.422 43.031C33.3987 43.143 33.3684 43.2527 33.331 43.36L31.742 48.162C31.6907 48.3207 31.595 48.4 31.455 48.4H30.517L28.221 41.309Z" fill="white"/>
        <path d="M46.5398 44.935C46.5398 45.495 46.4698 45.9967 46.3298 46.44C46.1945 46.8834 45.9915 47.259 45.7208 47.567C45.4548 47.8704 45.1258 48.1037 44.7338 48.267C44.3418 48.4304 43.8915 48.512 43.3828 48.512C42.9302 48.512 42.4588 48.4467 41.9688 48.316C41.9782 48.1807 41.9898 48.0477 42.0038 47.917C42.0178 47.7817 42.0318 47.6487 42.0458 47.518C42.0552 47.4387 42.0832 47.3757 42.1298 47.329C42.1812 47.2777 42.2558 47.252 42.3538 47.252C42.4378 47.252 42.5498 47.273 42.6898 47.315C42.8298 47.357 43.0165 47.378 43.2498 47.378C43.5578 47.378 43.8308 47.3314 44.0688 47.238C44.3115 47.1447 44.5145 47 44.6778 46.804C44.8458 46.608 44.9718 46.3584 45.0558 46.055C45.1445 45.747 45.1888 45.383 45.1888 44.963V38.369H46.5398V44.935Z" fill="white"/>
        <path d="M51.6615 41.197C52.1795 41.197 52.6462 41.2834 53.0615 41.456C53.4815 41.6287 53.8362 41.8737 54.1255 42.191C54.4195 42.5084 54.6435 42.8934 54.7975 43.346C54.9562 43.794 55.0355 44.2957 55.0355 44.851C55.0355 45.411 54.9562 45.915 54.7975 46.363C54.6435 46.811 54.4195 47.1937 54.1255 47.511C53.8362 47.8284 53.4815 48.0734 53.0615 48.246C52.6462 48.414 52.1795 48.498 51.6615 48.498C51.1435 48.498 50.6745 48.414 50.2545 48.246C49.8392 48.0734 49.4845 47.8284 49.1905 47.511C48.8965 47.1937 48.6702 46.811 48.5115 46.363C48.3529 45.915 48.2735 45.411 48.2735 44.851C48.2735 44.2957 48.3529 43.794 48.5115 43.346C48.6702 42.8934 48.8965 42.5084 49.1905 42.191C49.4845 41.8737 49.8392 41.6287 50.2545 41.456C50.6745 41.2834 51.1435 41.197 51.6615 41.197ZM51.6615 47.525C52.3615 47.525 52.8842 47.2917 53.2295 46.825C53.5749 46.3537 53.7475 45.698 53.7475 44.858C53.7475 44.0134 53.5749 43.3554 53.2295 42.884C52.8842 42.4127 52.3615 42.177 51.6615 42.177C51.3069 42.177 50.9989 42.2377 50.7375 42.359C50.4762 42.4804 50.2569 42.6554 50.0795 42.884C49.9069 43.1127 49.7762 43.395 49.6875 43.731C49.6035 44.0624 49.5615 44.438 49.5615 44.858C49.5615 45.278 49.6035 45.6537 49.6875 45.985C49.7762 46.3164 49.9069 46.5964 50.0795 46.825C50.2569 47.049 50.4762 47.2217 50.7375 47.343C50.9989 47.4644 51.3069 47.525 51.6615 47.525Z" fill="white"/>
        <path d="M56.5708 48.4V41.309H57.3128C57.4902 41.309 57.6022 41.3954 57.6488 41.568L57.7468 42.338C58.0548 41.9974 58.3978 41.722 58.7758 41.512C59.1585 41.302 59.5995 41.197 60.0988 41.197C60.4862 41.197 60.8268 41.2624 61.1208 41.393C61.4195 41.519 61.6668 41.701 61.8628 41.939C62.0635 42.1724 62.2152 42.4547 62.3178 42.786C62.4205 43.1174 62.4718 43.4837 62.4718 43.885V48.4H61.2258V43.885C61.2258 43.3484 61.1022 42.933 60.8548 42.639C60.6122 42.3404 60.2388 42.191 59.7348 42.191C59.3662 42.191 59.0208 42.2797 58.6988 42.457C58.3815 42.6344 58.0875 42.8747 57.8168 43.178V48.4H56.5708Z" fill="white"/>
        <path d="M67.1571 41.197C67.5818 41.197 67.9738 41.2694 68.3331 41.414C68.6925 41.554 69.0028 41.7594 69.2641 42.03C69.5255 42.296 69.7285 42.6274 69.8731 43.024C70.0225 43.416 70.0971 43.864 70.0971 44.368C70.0971 44.564 70.0761 44.6947 70.0341 44.76C69.9921 44.8254 69.9128 44.858 69.7961 44.858H65.0781C65.0875 45.306 65.1481 45.6957 65.2601 46.027C65.3721 46.3584 65.5261 46.636 65.7221 46.86C65.9181 47.0794 66.1515 47.245 66.4221 47.357C66.6928 47.4644 66.9961 47.518 67.3321 47.518C67.6448 47.518 67.9131 47.483 68.1371 47.413C68.3658 47.3384 68.5618 47.259 68.7251 47.175C68.8885 47.091 69.0238 47.014 69.1311 46.944C69.2431 46.8694 69.3388 46.832 69.4181 46.832C69.5208 46.832 69.6001 46.8717 69.6561 46.951L70.0061 47.406C69.8521 47.5927 69.6678 47.756 69.4531 47.896C69.2385 48.0314 69.0075 48.1434 68.7601 48.232C68.5175 48.3207 68.2655 48.386 68.0041 48.428C67.7428 48.4747 67.4838 48.498 67.2271 48.498C66.7371 48.498 66.2845 48.4164 65.8691 48.253C65.4585 48.085 65.1015 47.8424 64.7981 47.525C64.4995 47.203 64.2661 46.8064 64.0981 46.335C63.9301 45.8637 63.8461 45.3224 63.8461 44.711C63.8461 44.2164 63.9208 43.7544 64.0701 43.325C64.2241 42.8957 64.4435 42.5247 64.7281 42.212C65.0128 41.8947 65.3605 41.6474 65.7711 41.47C66.1818 41.288 66.6438 41.197 67.1571 41.197ZM67.1851 42.114C66.5831 42.114 66.1095 42.289 65.7641 42.639C65.4188 42.9844 65.2041 43.465 65.1201 44.081H68.9771C68.9771 43.7917 68.9375 43.528 68.8581 43.29C68.7788 43.0474 68.6621 42.8397 68.5081 42.667C68.3541 42.4897 68.1651 42.3544 67.9411 42.261C67.7218 42.163 67.4698 42.114 67.1851 42.114Z" fill="white"/>
        <path d="M75.7519 42.478C75.6959 42.5807 75.6096 42.632 75.4929 42.632C75.4229 42.632 75.3436 42.6064 75.2549 42.555C75.1663 42.5037 75.0566 42.4477 74.9259 42.387C74.7999 42.3217 74.6483 42.2634 74.4709 42.212C74.2936 42.156 74.0836 42.128 73.8409 42.128C73.6309 42.128 73.4419 42.156 73.2739 42.212C73.1059 42.2634 72.9613 42.3357 72.8399 42.429C72.7233 42.5224 72.6323 42.632 72.5669 42.758C72.5063 42.8794 72.4759 43.0124 72.4759 43.157C72.4759 43.339 72.5273 43.4907 72.6299 43.612C72.7373 43.7334 72.8773 43.8384 73.0499 43.927C73.2226 44.0157 73.4186 44.095 73.6379 44.165C73.8573 44.2304 74.0813 44.3027 74.3099 44.382C74.5433 44.4567 74.7696 44.5407 74.9889 44.634C75.2083 44.7274 75.4043 44.844 75.5769 44.984C75.7496 45.124 75.8873 45.2967 75.9899 45.502C76.0973 45.7027 76.1509 45.9454 76.1509 46.23C76.1509 46.5567 76.0926 46.86 75.9759 47.14C75.8593 47.4154 75.6866 47.6557 75.4579 47.861C75.2293 48.0617 74.9493 48.2204 74.6179 48.337C74.2866 48.4537 73.9039 48.512 73.4699 48.512C72.9753 48.512 72.5273 48.4327 72.1259 48.274C71.7246 48.1107 71.3839 47.903 71.1039 47.651L71.3979 47.175C71.4352 47.1144 71.4796 47.0677 71.5309 47.035C71.5823 47.0024 71.6499 46.986 71.7339 46.986C71.8179 46.986 71.9066 47.0187 71.9999 47.084C72.0933 47.1494 72.2053 47.2217 72.3359 47.301C72.4713 47.3804 72.6323 47.4527 72.8189 47.518C73.0103 47.5834 73.2483 47.616 73.5329 47.616C73.7756 47.616 73.9879 47.5857 74.1699 47.525C74.3519 47.4597 74.5036 47.3734 74.6249 47.266C74.7463 47.1587 74.8349 47.035 74.8909 46.895C74.9516 46.755 74.9819 46.6057 74.9819 46.447C74.9819 46.251 74.9283 46.09 74.8209 45.964C74.7183 45.8334 74.5806 45.7237 74.4079 45.635C74.2353 45.5417 74.0369 45.4624 73.8129 45.397C73.5936 45.327 73.3672 45.2547 73.1339 45.18C72.9053 45.1054 72.6789 45.0214 72.4549 44.928C72.2356 44.83 72.0396 44.7087 71.8669 44.564C71.6943 44.4194 71.5543 44.242 71.4469 44.032C71.3443 43.8174 71.2929 43.5584 71.2929 43.255C71.2929 42.9844 71.3489 42.7254 71.4609 42.478C71.5729 42.226 71.7363 42.0067 71.9509 41.82C72.1656 41.6287 72.4293 41.477 72.7419 41.365C73.0546 41.253 73.4116 41.197 73.8129 41.197C74.2796 41.197 74.6973 41.2717 75.0659 41.421C75.4393 41.5657 75.7613 41.7664 76.0319 42.023L75.7519 42.478Z" fill="white"/>
        <path d="M85.3063 42.569C85.2689 42.6204 85.2316 42.66 85.1943 42.688C85.1569 42.716 85.1033 42.73 85.0333 42.73C84.9633 42.73 84.8863 42.702 84.8023 42.646C84.7229 42.5854 84.6203 42.52 84.4943 42.45C84.3683 42.38 84.2143 42.317 84.0323 42.261C83.8549 42.2004 83.6356 42.17 83.3743 42.17C83.0289 42.17 82.7233 42.233 82.4573 42.359C82.1913 42.4804 81.9673 42.6577 81.7853 42.891C81.6079 43.1244 81.4726 43.4067 81.3793 43.738C81.2906 44.0694 81.2463 44.4404 81.2463 44.851C81.2463 45.2804 81.2953 45.663 81.3933 45.999C81.4913 46.3304 81.6289 46.6104 81.8063 46.839C81.9836 47.063 82.1983 47.2357 82.4503 47.357C82.7069 47.4737 82.9939 47.532 83.3113 47.532C83.6146 47.532 83.8643 47.497 84.0603 47.427C84.2563 47.3524 84.4196 47.2707 84.5503 47.182C84.6809 47.0934 84.7883 47.014 84.8723 46.944C84.9563 46.8694 85.0403 46.832 85.1243 46.832C85.2316 46.832 85.3109 46.8717 85.3623 46.951L85.7123 47.406C85.4043 47.784 85.0193 48.0617 84.5573 48.239C84.0953 48.4117 83.6076 48.498 83.0943 48.498C82.6509 48.498 82.2379 48.4164 81.8553 48.253C81.4773 48.0897 81.1483 47.854 80.8683 47.546C80.5883 47.2334 80.3666 46.8507 80.2033 46.398C80.0446 45.9454 79.9653 45.4297 79.9653 44.851C79.9653 44.3237 80.0376 43.836 80.1823 43.388C80.3316 42.94 80.5463 42.555 80.8263 42.233C81.1109 41.9064 81.4609 41.652 81.8763 41.47C82.2916 41.288 82.7676 41.197 83.3043 41.197C83.7989 41.197 84.2376 41.2787 84.6203 41.442C85.0029 41.6007 85.3413 41.827 85.6353 42.121L85.3063 42.569Z" fill="white"/>
        <path d="M89.8744 41.197C90.3924 41.197 90.8591 41.2834 91.2744 41.456C91.6944 41.6287 92.0491 41.8737 92.3384 42.191C92.6324 42.5084 92.8564 42.8934 93.0104 43.346C93.1691 43.794 93.2484 44.2957 93.2484 44.851C93.2484 45.411 93.1691 45.915 93.0104 46.363C92.8564 46.811 92.6324 47.1937 92.3384 47.511C92.0491 47.8284 91.6944 48.0734 91.2744 48.246C90.8591 48.414 90.3924 48.498 89.8744 48.498C89.3564 48.498 88.8874 48.414 88.4674 48.246C88.0521 48.0734 87.6974 47.8284 87.4034 47.511C87.1094 47.1937 86.8831 46.811 86.7244 46.363C86.5658 45.915 86.4864 45.411 86.4864 44.851C86.4864 44.2957 86.5658 43.794 86.7244 43.346C86.8831 42.8934 87.1094 42.5084 87.4034 42.191C87.6974 41.8737 88.0521 41.6287 88.4674 41.456C88.8874 41.2834 89.3564 41.197 89.8744 41.197ZM89.8744 47.525C90.5744 47.525 91.0971 47.2917 91.4424 46.825C91.7878 46.3537 91.9604 45.698 91.9604 44.858C91.9604 44.0134 91.7878 43.3554 91.4424 42.884C91.0971 42.4127 90.5744 42.177 89.8744 42.177C89.5198 42.177 89.2118 42.2377 88.9504 42.359C88.6891 42.4804 88.4697 42.6554 88.2924 42.884C88.1198 43.1127 87.9891 43.395 87.9004 43.731C87.8164 44.0624 87.7744 44.438 87.7744 44.858C87.7744 45.278 87.8164 45.6537 87.9004 45.985C87.9891 46.3164 88.1198 46.5964 88.2924 46.825C88.4697 47.049 88.6891 47.2217 88.9504 47.343C89.2118 47.4644 89.5198 47.525 89.8744 47.525Z" fill="white"/>
        <path d="M94.7837 48.4V41.309H95.5257C95.703 41.309 95.815 41.3954 95.8617 41.568L95.9527 42.296C96.2141 41.974 96.5057 41.7104 96.8277 41.505C97.1544 41.2997 97.5324 41.197 97.9617 41.197C98.4424 41.197 98.8297 41.33 99.1237 41.596C99.4224 41.862 99.637 42.2214 99.7677 42.674C99.8657 42.4174 99.994 42.1957 100.153 42.009C100.316 41.8224 100.498 41.6684 100.699 41.547C100.899 41.4257 101.112 41.337 101.336 41.281C101.564 41.225 101.795 41.197 102.029 41.197C102.402 41.197 102.733 41.2577 103.023 41.379C103.317 41.4957 103.564 41.6684 103.765 41.897C103.97 42.1257 104.126 42.408 104.234 42.744C104.341 43.0754 104.395 43.4557 104.395 43.885V48.4H103.149V43.885C103.149 43.3297 103.027 42.9097 102.785 42.625C102.542 42.3357 102.19 42.191 101.728 42.191C101.522 42.191 101.326 42.2284 101.14 42.303C100.958 42.373 100.797 42.478 100.657 42.618C100.517 42.758 100.405 42.9354 100.321 43.15C100.241 43.36 100.202 43.605 100.202 43.885V48.4H98.9557V43.885C98.9557 43.3157 98.8414 42.891 98.6127 42.611C98.384 42.331 98.0504 42.191 97.6117 42.191C97.3037 42.191 97.0167 42.275 96.7507 42.443C96.4894 42.6064 96.249 42.8304 96.0297 43.115V48.4H94.7837Z" fill="white"/>
        <path d="M106.282 50.801V41.309H107.024C107.201 41.309 107.313 41.3954 107.36 41.568L107.465 42.408C107.768 42.0394 108.113 41.743 108.501 41.519C108.893 41.295 109.343 41.183 109.852 41.183C110.258 41.183 110.626 41.2624 110.958 41.421C111.289 41.575 111.571 41.806 111.805 42.114C112.038 42.4174 112.218 42.7954 112.344 43.248C112.47 43.7007 112.533 44.221 112.533 44.809C112.533 45.3317 112.463 45.8194 112.323 46.272C112.183 46.72 111.982 47.1097 111.721 47.441C111.459 47.7677 111.137 48.0267 110.755 48.218C110.377 48.4047 109.95 48.498 109.474 48.498C109.035 48.498 108.659 48.4257 108.347 48.281C108.039 48.1364 107.766 47.931 107.528 47.665V50.801H106.282ZM109.439 42.191C109.033 42.191 108.676 42.2844 108.368 42.471C108.064 42.6577 107.784 42.9214 107.528 43.262V46.692C107.756 47 108.006 47.217 108.277 47.343C108.552 47.469 108.858 47.532 109.194 47.532C109.852 47.532 110.358 47.2964 110.713 46.825C111.067 46.3537 111.245 45.6817 111.245 44.809C111.245 44.347 111.203 43.9504 111.119 43.619C111.039 43.2877 110.923 43.017 110.769 42.807C110.615 42.5924 110.426 42.436 110.202 42.338C109.978 42.24 109.723 42.191 109.439 42.191Z" fill="white"/>
        <path d="M119.214 48.4H118.661C118.54 48.4 118.442 48.3814 118.367 48.344C118.293 48.3067 118.244 48.2274 118.22 48.106L118.08 47.448C117.894 47.616 117.712 47.7677 117.534 47.903C117.357 48.0337 117.17 48.1457 116.974 48.239C116.778 48.3277 116.568 48.3954 116.344 48.442C116.125 48.4887 115.88 48.512 115.609 48.512C115.334 48.512 115.075 48.4747 114.832 48.4C114.594 48.3207 114.387 48.204 114.209 48.05C114.032 47.896 113.89 47.7024 113.782 47.469C113.68 47.231 113.628 46.951 113.628 46.629C113.628 46.349 113.705 46.0807 113.859 45.824C114.013 45.5627 114.261 45.3317 114.601 45.131C114.947 44.9304 115.397 44.767 115.952 44.641C116.508 44.5104 117.187 44.4357 117.989 44.417V43.864C117.989 43.3134 117.87 42.898 117.632 42.618C117.399 42.3334 117.051 42.191 116.589 42.191C116.286 42.191 116.029 42.2307 115.819 42.31C115.614 42.3847 115.434 42.471 115.28 42.569C115.131 42.6624 115 42.7487 114.888 42.828C114.781 42.9027 114.674 42.94 114.566 42.94C114.482 42.94 114.408 42.919 114.342 42.877C114.282 42.8304 114.233 42.7744 114.195 42.709L113.971 42.31C114.363 41.932 114.786 41.6497 115.238 41.463C115.691 41.2764 116.193 41.183 116.743 41.183C117.14 41.183 117.492 41.2484 117.8 41.379C118.108 41.5097 118.367 41.6917 118.577 41.925C118.787 42.1584 118.946 42.4407 119.053 42.772C119.161 43.1034 119.214 43.4674 119.214 43.864V48.4ZM115.98 47.637C116.2 47.637 116.4 47.616 116.582 47.574C116.764 47.5274 116.935 47.4644 117.093 47.385C117.257 47.301 117.411 47.2007 117.555 47.084C117.705 46.9674 117.849 46.8344 117.989 46.685V45.208C117.415 45.2267 116.928 45.2734 116.526 45.348C116.125 45.418 115.798 45.5114 115.546 45.628C115.294 45.7447 115.11 45.8824 114.993 46.041C114.881 46.1997 114.825 46.377 114.825 46.573C114.825 46.7597 114.856 46.9207 114.916 47.056C114.977 47.1914 115.059 47.3034 115.161 47.392C115.264 47.476 115.385 47.539 115.525 47.581C115.665 47.6184 115.817 47.637 115.98 47.637Z" fill="white"/>
        <path d="M121.102 48.4V41.309H121.844C122.021 41.309 122.133 41.3954 122.18 41.568L122.278 42.338C122.586 41.9974 122.929 41.722 123.307 41.512C123.69 41.302 124.131 41.197 124.63 41.197C125.017 41.197 125.358 41.2624 125.652 41.393C125.951 41.519 126.198 41.701 126.394 41.939C126.595 42.1724 126.746 42.4547 126.849 42.786C126.952 43.1174 127.003 43.4837 127.003 43.885V48.4H125.757V43.885C125.757 43.3484 125.633 42.933 125.386 42.639C125.143 42.3404 124.77 42.191 124.266 42.191C123.897 42.191 123.552 42.2797 123.23 42.457C122.913 42.6344 122.619 42.8747 122.348 43.178V48.4H121.102Z" fill="white"/>
        <path d="M130.742 50.493C130.7 50.5864 130.646 50.661 130.581 50.717C130.52 50.773 130.424 50.801 130.294 50.801H129.37L130.665 47.987L127.739 41.309H128.817C128.924 41.309 129.008 41.337 129.069 41.393C129.129 41.4444 129.174 41.5027 129.202 41.568L131.099 46.034C131.141 46.1367 131.176 46.2394 131.204 46.342C131.236 46.4447 131.264 46.5497 131.288 46.657C131.32 46.5497 131.353 46.4447 131.386 46.342C131.418 46.2394 131.456 46.1344 131.498 46.027L133.339 41.568C133.367 41.4934 133.413 41.4327 133.479 41.386C133.549 41.3347 133.623 41.309 133.703 41.309H134.697L130.742 50.493Z" fill="white"/>
        </svg>
        </a>
                        <div class="element element--text">
                            <p class="copyright">Copyright &copy; 2023 MarketWatch, Inc. All rights reserved.</p>
                            <p class="group group--links">
                                <a class="link" href="https://www.marketwatch.com/site/subscriber-agreement" target="_blank">Subscriber Agreement &amp; Terms of Use </a><span class="bar">|</span>
                                <a class="link" href="https://www.dowjones.com/privacy-notice?mod=mw" target="_blank">Privacy Notice </a><span class="bar">|</span>
                                <a class="link" href="https://www.dowjones.com/cookie-notice?mod=mw" target="_blank">Cookie Notice</a><span class="j-hidden" id="manage-cookies"> (<a class="link"></a>)</span>.
                            </p>
                            <div id="regulation-links" class="group group--links"></div>
                        </div>
                        <ul class="list list--social">
                            <li class="social__item"><a class="icon icon--facebook" href="https://www.facebook.com/marketwatch" rel="nofollow" target="_blank"><span class="screen-reader-text">Facebook</span></a></li>
                            <li class="social__item"><a class="icon icon--twitter" href="https://twitter.com/marketwatch" rel="nofollow" target="_blank"><span class="screen-reader-text">Twitter</span></a></li>
                            <li class="social__item"><a class="icon icon--linkedin" href="https://www.linkedin.com/company/marketwatch" rel="nofollow" target="_blank"><span class="screen-reader-text">LinkedIn</span></a></li>
                            <li class="social__item app-badges">
                                <a class="app__link" href="https://itunes.apple.com/app/marketwatch/id336693422?ign-mpt=uo%3D6&mt=8" target="_blank" rel="nofollow"><img class="lazyload" data-src=https://sts3.wsj.net/bucket-a/maggie/static/images/app-store.svg alt="Download from the App Store" /></a>
                                <a class="app__link" href="https://play.google.com/store/apps/details?id=com.marketwatch&hl=en" target="_blank" rel="nofollow"><img class="lazyload" data-src=https://sts3.wsj.net/bucket-a/maggie/static/images/google-play.png alt="Download from the Google Play Store" /></a>
                            </li>
                        </ul>
                    </div>
                    <ul class="list list--footer">
                        <li class="footer__heading"><h3 class="label">MarketWatch</h3></li>
                        <li class="footer__item"><a class="link" href="https://customercenter.marketwatch.com/public">Customer Center</a></li>
                        <li class="footer__item"><a class="link" href="https://customercenter.marketwatch.com/contact">Contact Us</a></li>
                        <li class="footer__item"><a class="link" href="https://www.marketwatch.com/newsroom">Newsroom Roster</a></li>
                        <li class="footer__item"><a class="link" href="https://www.marketwatch.com/games">Virtual Stock Exchange</a></li>
                        <li class="footer__item"><a class="link" href="https://bigcharts.marketwatch.com" target="_blank">BigCharts</a></li>
                        <li class="footer__item"><a class="link" href="https://www.marketwatch.com/site/copyright-policy">Copyright Policy</a></li>
                        <li class="footer__item"><a class="link" href="https://www.marketwatch.com/site/manage-web-notifications">Manage Notifications</a></li>
                        <li class="footer__item"><a class="link" href="https://customercenter.marketwatch.com/subscription-cancel?subtype=marketwatch">Cancel My Subscription</a></li>
                    </ul>
                    <ul class="list list--footer">
                        <li class="footer__heading"><h3 class="label">Company</h3></li>
                        <li class="footer__item"><a class="link" href="https://www.dowjones.com" target="_blank">Dow Jones</a></li>
                        <li class="footer__item"><a class="link" href="https://www.dowjones.com/code-conduct/" rel="nofollow" target="_blank">Code of Conduct</a></li>
                        <li class="footer__item"><a class="link" href="https://www.marketwatch.com/column/corrections">Corrections</a></li>
                        <li class="footer__item"><a class="link" href="http://www.djreprints.com" rel="nofollow" target="_blank">Reprints &amp; Licensing</a></li>
                        <li class="footer__item"><a class="link" href="https://wsjbg-adsmanager.com/?action=login" target="_blank">Digital Self Service</a></li>
                        <li class="footer__item"><a class="link" href="https://www.dowjones.com/cookie-notice/#cookies-advertising" target="_blank">Your Ad Choices</a></li>
                        <li class="footer__item"><a class="link" href="https://corporate.marketwatch.com?mod=djm_marketwatchfooter_44669&LS=Website&utm_source=Website&utm_campaign=marketwatchfooter" target="_blank">Corporate Subscriptions</a></li>
                        <li class="footer__item"><a class="link" href="https://www.dowjones.com/accessibility-statement/" target="_blank">Accessibility</a></li>
                    </ul>
                    <ul class="list list--footer">
                        <li class="footer__heading"><h3 class="label">Dow Jones Network</h3></li>
                        <li class="footer__item"><a class="link" href="https://www.wsj.com/" target="_blank">The Wall Street Journal</a></li>
                        <li class="footer__item"><a class="link" href="https://www.barrons.com" target="_blank">Barron's</a></li>
                        <li class="footer__item"><a class="link" href="https://www.fnlondon.com" target="_blank">Financial News London</a></li>
                        <li class="footer__item"><a class="link" href="https://www.realtor.com/" target="_blank">realtor.com</a></li>
                        <li class="footer__item"><a class="link" href="https://www.mansionglobal.com/" target="_blank">Mansion Global</a></li>
                    </ul>
                    <div class="element element--legal">
                        <p class="legal">
                            Intraday Data provided by <a class="factset" href="https://www.factset.com/" rel="nofollow" target="_blank">FACTSET</a> and subject to <a class="link" href="https://www.marketwatch.com/support/investing-terms-of-use">terms of use</a>.
                            Historical and current end-of-day data provided by <a class="factset" href="https://www.factset.com/" rel="nofollow" target="_blank">FACTSET</a>.
                            All quotes are in local exchange time.
                            Real-time last sale data for U.S. stock quotes reflect trades reported through Nasdaq only.
                            Intraday data delayed at least 15 minutes or per exchange requirements.
                        </p>
                    </div>
                </div>
            </div>

            <!-- This is a placeholder for cxense widgets -->
            <div id="cx-scrim"></div>
            <div id="cx-notification"></div>
        </footer>
            
                

                <div data-track-query=".toggle--trending" class="container container--trending fixed ">
                    <input type="checkbox" class="toggle toggle--trending" data-track-code="trending_minimize" id="trending-tickers">
                    <label class="icon--close" for="trending-tickers">
                    <span class="screen-reader-text">Close Trending Tickers bar</span>
                    </label>
                    <section class="region region--full">
                        <div class="column column--full trending j-trending full-width">
                            <header class="trending__header">
                                <h4 class="trending__title">Trending Tickers</h4>
                                <div class="trending__description"><div class="status"></div>Above average volume.</div>
                            </header>
                            <ul class="list list--trending horizontal">
                                            <li class="trending__item ticker">
                                                <bg-quote class="positive" channel="/zigman2/quotes/202334875/lastsale">
                                                    <a class="trending__link" href="/investing/stock/pali?mod=trending-tickers">
                                                        <div class="link__content">
                                                            <div class="trending__data">
                                                                <span class="trending__symbol">PALI</span>
                                                                <span class="price"><bg-quote class="value" field="Last" channel="/zigman2/quotes/202334875/lastsale" format="$0,0.00">$3.46</bg-quote></span>
                                                            </div>
                                                            <div class="trending__data">
                                                                <i class="icon"></i>
                                                                <span class="trending__change percent ignore-color">
                                                                    <bg-quote field="percentChange" format="0.00%" channel="/zigman2/quotes/202334875/lastsale">30.62%</bg-quote>
                                                                </span>
                                                                <span class="trending__change points ignore-color">
                                                                    <bg-quote field="change" format="0,0.00" channel="/zigman2/quotes/202334875/lastsale">0.81</bg-quote>
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </a>
                                                </bg-quote>
                                            </li>
                                            <li class="trending__item ticker">
                                                <bg-quote class="negative" channel="/zigman2/quotes/230042524/composite">
                                                    <a class="trending__link" href="/investing/stock/pyxs?mod=trending-tickers">
                                                        <div class="link__content">
                                                            <div class="trending__data">
                                                                <span class="trending__symbol">PYXS</span>
                                                                <span class="price"><bg-quote class="value" field="Last" channel="/zigman2/quotes/230042524/composite" format="$0,0.00">$4.57</bg-quote></span>
                                                            </div>
                                                            <div class="trending__data">
                                                                <i class="icon"></i>
                                                                <span class="trending__change percent ignore-color">
                                                                    <bg-quote field="percentChange" format="0.00%" channel="/zigman2/quotes/230042524/composite">-23.83%</bg-quote>
                                                                </span>
                                                                <span class="trending__change points ignore-color">
                                                                    <bg-quote field="change" format="0,0.00" channel="/zigman2/quotes/230042524/composite">-1.43</bg-quote>
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </a>
                                                </bg-quote>
                                            </li>
                                            <li class="trending__item ticker">
                                                <bg-quote class="positive" channel="/zigman2/quotes/223592399/composite">
                                                    <a class="trending__link" href="/investing/stock/ionq?mod=trending-tickers">
                                                        <div class="link__content">
                                                            <div class="trending__data">
                                                                <span class="trending__symbol">IONQ</span>
                                                                <span class="price"><bg-quote class="value" field="Last" channel="/zigman2/quotes/223592399/composite" format="$0,0.00">$6.71</bg-quote></span>
                                                            </div>
                                                            <div class="trending__data">
                                                                <i class="icon"></i>
                                                                <span class="trending__change percent ignore-color">
                                                                    <bg-quote field="percentChange" format="0.00%" channel="/zigman2/quotes/223592399/composite">32.09%</bg-quote>
                                                                </span>
                                                                <span class="trending__change points ignore-color">
                                                                    <bg-quote field="change" format="0,0.00" channel="/zigman2/quotes/223592399/composite">1.63</bg-quote>
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </a>
                                                </bg-quote>
                                            </li>
                                            <li class="trending__item ticker">
                                                <bg-quote class="negative" channel="/zigman2/quotes/201047587/composite">
                                                    <a class="trending__link" href="/investing/stock/scyx?mod=trending-tickers">
                                                        <div class="link__content">
                                                            <div class="trending__data">
                                                                <span class="trending__symbol">SCYX</span>
                                                                <span class="price"><bg-quote class="value" field="Last" channel="/zigman2/quotes/201047587/composite" format="$0,0.00">$2.89</bg-quote></span>
                                                            </div>
                                                            <div class="trending__data">
                                                                <i class="icon"></i>
                                                                <span class="trending__change percent ignore-color">
                                                                    <bg-quote field="percentChange" format="0.00%" channel="/zigman2/quotes/201047587/composite">-1.74%</bg-quote>
                                                                </span>
                                                                <span class="trending__change points ignore-color">
                                                                    <bg-quote field="change" format="0,0.00" channel="/zigman2/quotes/201047587/composite">-0.05</bg-quote>
                                                                </span>
                                                            </div>
                                                        </div>
                                                    </a>
                                                </bg-quote>
                                            </li>
                            </ul>
                            <div class="element element--btn">
                                <a class="btn btn--subscribe" target="_blank" href="https://get.investors.com/product-overview/?src=A00619&refcode=Site%20placement%7CMarketWatch%7CMarketWatch%7C2023%7CRecurring%7COther%2FNA%7C0%7C%7C992173 ">Access Premium Tools</a>
                            </div>


                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-trending-tickers" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-trending-tickers',
                                            adUnitPath: '/2/marketwatch.com/investing/quotes/stock/overview',
                                            adSize: [[140,31]],
                                            adSizeMap: {'at4units':[],'at12units':[[140,31]]},
                                            adTargeting: {'alert':['volatility050','green']},
                                            adLocation: 'TRENDINGTICKERS',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>
                        </div>
                    </section>
                </div>
                
            


        <div class="region region--lightbox search j-new-search j-search" data-source="search">
            <div class="lightbox lightbox--search">
            <div class="container container--search-bar" role="region" aria-label="search form">
                <div class="region region--full">
                <div class="column column--full ">
                    <div class="form form--search search__form" role="search" action="/" method="get" onSubmit="return MarketWatch.SiteSearch.onSubmit()" aria-label="search form">
                        <div id="search-overlay" class="search__bar">
                            <div class="search__input">
                                <label for='mw-search'>
                                <span class='screen-reader-text'>Search</span>
                                </label>
                                <i class="icon icon--search"></i>
                                <input class="input input--search j-search-input" type='text' id='mw-search' data-isoverlay value="" placeholder="Enter a symbol or keyword"/>
                                <button class="btn btn--outline" type='button' id="btn-clear" aria-label="Clear Search"><span class="m-hide">Clear</span><i class="icon icon--close m-show"></i></button>
                                <div class="divider"></div>
                                <button class="btn btn--secondary j-search-button" type='button' id="btn-submit-search" aria-label="Submit Search">Search</button>
                            </div>
                            <div class="search__btn advanced-search">
                            <a href="https://www.marketwatch.com/search?q=" class="link j-advanced-search">Advanced Search</a><i class="icon icon--arrow-right"></i>
                            </div>
                        </div>
                    </div>
                </div>
                </div>
            </div>
            <div class="container container--ad" role="complementary" aris-label="advertisement">
                <div class="region region--ad">
                <div class="column column--full">


                    <div class="element element--ad is-loading">
                        <div is="mw-ad" id="ad-search-sponsor" class="j-ad lazyload " data-expand="200">
                            <script>
                                !function() {
                                    window.__mwads = window.__mwads || {};
                                    window.__mwads.uacQ = window.__mwads.uacQ || [];
                                    window.__mwads.uacQ.push({
                                        options: {
                                            adActivate: true,
                                            adId: 'ad-search-sponsor',
                                            adUnitPath: '/2/marketwatch.com/sponsor_search',
                                            adSize: [[1,2],['fluid']],
                                            adSizeMap: {},
                                            adTargeting: {'alert':['volatility025','green']},
                                            adLocation: 'NATIVESEARCH',
                                            isObserve: !false,
                                            observeFromUAC: !false,
                                            triggerPrebid: true,
                                            moatEnabled: true,
                                            collapseAdBeforeFetch: true
                                        }
                                    });
                                }();
                            </script>
                        </div>             
                    </div>
                </div>
                </div>
            </div>
            <div id="search-results-div" class="container container--search-results j-search-results" role="region" aria-label="search results">

                <div class="region region--full">
                <div class="column column--full">
                    <header class="header header--primary no-background">
                        <h2 class="title">
                            <span class="label">Search Results</span>
                        </h2>
                    </header>
                </div>
                </div>

                <div class="region region--primary j-search-results">
                <div class="column column--aside">


        <div class="ticker__set">
            <div class="element element--table">
            <h2 class="header header--list"><span class="header__text">Symbols</span></h2>
                <div class="loading loading--tickers j-loading-symbols">Loading...</div>
                <table class="table table--secondary" role="presentation">
                <tbody class="j-search-symbols">
                </tbody>
                </table>
            </div>
        </div>
            <template id="sr-no-results-symbols">
            <tr class="table__row">
                <td class="table__cell no-link">No results found</td>
            </tr>
            </template>
            <template id="sr-quote-template">
            <tr class="table__row">
                <td class="table__cell j-cell-marker">
                <div class="marker"></div>
                </td>
                <td class="table__cell align--left">
                <a class="primary j-result-link" href="">
                    <span class="symbol j-symbol"></span>
                    <div class="secondary">
                    <small class="company j-company"></small>
                    </div>
                </a>
                </td>
                <td class="table__cell">
                <div class="primary t-last ignore-color">
                    <bg-quote field="last" class="j-price"></bg-quote>
                </div>
                <small class="secondary">
                    <span class="point t-change">
                    <bg-quote field="change" class="j-point"></bg-quote>
                    </span>
                    <span class="percent t-percent">
                    <bg-quote field="percentChange" class="j-percent"></bg-quote>
                    </span>
                </small>
                </td>
            </tr>
            </template>


        <div class="ticker__set">
            <div class="element element--table">
            <h2 class="header header--list"><span class="header__text">Private Companies</span></h2>
                <div class="loading loading--tickers j-loading-privatecompanies">Loading...</div>
                <table class="table table--secondary" role="presentation">
                <tbody class="j-search-privatecompanies">
                </tbody>
                </table>
            </div>
        </div>

        <header class="header header--text">
            <h2 class="title">
                <span class="label">Recently Viewed Tickers</span>
            </h2>
        </header>
        <mw-quotelist class="element element--recentTickers is-loading j-tickerList" data-track-query=".btn--tickerSearch|.ticker" data-track-code="MW_Homepage_Watchlist_Search Tickers|MW_Homepage_Watchlist_Recent Tickers">
            <div class="element element--message j-message j-hidden j-no-recent-items">
                <div class="message">
                    <div class="message__text">
                        <h3 class="primary">No Recent Tickers</h3>
                        <p class="secondary">Visit a quote page and your recently viewed tickers will be displayed here.</p>
                    </div>
                    <div class="group group--buttons">
                        <button class="btn btn--primary j-tickerSearch">Search Tickers</button>
                    </div>
                </div>
            </div>
            <div class="j-hidden j-recent">
                <template class="instruments">
                    <a class="ticker t-link j-recentlyviewed-tracking">
                        <bg-quote class="posNegNeu t-updown">
                            <h4 class="ticker__symbol t-symbol"></h4>
                            <span class="ticker__price ignore-color t-price"></span>
                            <span class="ticker__company t-company"></span>
                            <div class="ticker__change ignore-color">
                                <span class="change__price ignore-color t-change"></span>
                                <span class="change__percent ignore-color t-percent"></span>
                                <i class="icon"></i>
                            </div>
                        </bg-quote>
                    </a>
                </template>
            </div>
        </mw-quotelist>
                </div>
                <div class="column column--primary">



                <div class="element element--tabs">
                    <mw-tabs>
                        <div class="element__options">
                            <ul role="tablist" class="tabs full-width" data-track-query=".tab__item">
                                    <button role="tab" aria-selected="true" class="tab__item is-selected j-tabItem" data-tab-pane="All News" data-track-code="Index_All News">All News</button>
                                    <button role="tab" aria-selected="" class="tab__item  j-tabItem" data-tab-pane="Articles" data-track-code="Index_Articles">Articles</button>
                                    <button role="tab" aria-selected="" class="tab__item  j-tabItem" data-tab-pane="Video" data-track-code="Index_Video">Video</button>
                                    <button role="tab" aria-selected="" class="tab__item  j-tabItem" data-tab-pane="Podcasts" data-track-code="Index_Podcasts">Podcasts</button>
                            </ul>
                            <div class="results__count"></div>
                        </div>
                        <div class="element__body j-tabPanes">
                                <div class="tab__pane is-active j-tabPane" data-tab-pane="All News">


                                </div>
                                <div class="tab__pane  j-tabPane" data-tab-pane="Articles">


                                </div>
                                <div class="tab__pane  j-tabPane" data-tab-pane="Video">


                                </div>
                                <div class="tab__pane  j-tabPane" data-tab-pane="Podcasts">


                                </div>
                        </div>
                    </mw-tabs>
                </div>
                </div>
                </div>

                <div class="region region--aside">
                <div class="column column--full">
                    <div class="group group--lists">

        <div class="result__list">
                <h2 class="header header--list"><span class="header__text">Authors</span></h2>
                <div class="list j-search-authors"></div>
        </div>

        <template id="sr-no-results">
        <span class="list__item no-link">No results found</span>
        </template>

        <template id="sr-multiuse-result">
            <a class="list__item link j-result-link" href="" aria-label></a>
        </template>

        <div class="result__list">
                <h2 class="header header--list"><span class="header__text">Sections</span></h2>
                <div class="list j-search-sections"></div>
        </div>

        <template id="sr-no-results">
        <span class="list__item no-link">No results found</span>
        </template>

        <template id="sr-multiuse-result">
            <a class="list__item link j-result-link" href="" aria-label></a>
        </template>

        <div class="result__list">
                <h2 class="header header--list"><span class="header__text">Columns</span></h2>
                <div class="list j-search-columns"></div>
        </div>

        <template id="sr-no-results">
        <span class="list__item no-link">No results found</span>
        </template>

        <template id="sr-multiuse-result">
            <a class="list__item link j-result-link" href="" aria-label></a>
        </template>
                    </div>
                </div>
                </div>

            </div>

            </div>
        </div>

        <div class="region region--lightbox j-video" data-source="video">
        <div class="lightbox lightbox--template j-content">
            <div class="column column--full">
            <div class="lightbox__header">
                <button class="toggle--overlay j-cancel">&times;</button>
                <header class="header header--secondary">
                    <h2 class="title">
                        <a class="link label" href="https://www.marketwatch.com/video">Video Center<i class="icon icon--arrow-right"></i></a>
                    </h2>
                </header>
                </button>
            </div>
            <div class="lightbox__body video h-auto">
                <div class="video__player"></div>
                <div class="video__info"></div>
                <template>
                    <h2 class="video__title"></h2>
                    <p class="video__paragraph"></p>
                    <a class="video__link" href="#" target="_self"></a>
                    <time class="video__time"></time>
                </template>
            </div>
            </div>
        </div>
        </div>
                <script defer async src="https://sts3.wsj.net/bucket-a/maggie/static/js/scripts-1521aaf6d7.min.js"></script>
            
            
                <script>window.__mwads=window.__mwads||{slots:{}},function(){if(window.__mwads.gptEnabled){googletag.cmd.push((function(){googletag.pubads().addEventListener("slotRequested",(function(e){performance.getEntriesByName("gpt-slotRequested").length||performance.mark("gpt-slotRequested"),e.slot.getSlotElementId()!==window.__mwads.mpuId||performance.getEntriesByName("gpt-mpuRequested").length||performance.mark("gpt-mpuRequested")})),googletag.pubads().addEventListener("slotRenderEnded",(function(e){performance.getEntriesByName("gpt-slotRenderEnded").length||performance.mark("gpt-slotRenderEnded"),e.slot.getSlotElementId()!==window.__mwads.mpuId||performance.getEntriesByName("gpt-mpuRenderEnded").length||performance.mark("gpt-mpuRenderEnded");var t=document.getElementById(e.slot.getSlotElementId());t&&(t.parentElement.classList.remove("is-loading"),t.parentElement.classList.add("is-loaded"))})),googletag.pubads().addEventListener("slotOnload",(function(e){performance.getEntriesByName("gpt-slotOnload").length||performance.mark("gpt-slotOnload"),e.slot.getSlotElementId()!==window.__mwads.mpuId||performance.getEntriesByName("gpt-mpuOnLoad").length||performance.mark("gpt-mpuOnLoad")}))}));googletag.cmd.push((function(){if(window.__mwads&&window.__mwads.uacQ){if(void 0!==window.pxSegmentIDs){var e=window.pxSegmentIDs.split(",");(t=window.__mwads.uacQ,Object.keys(t).map((function(e){return t[e]}))).forEach((function(t){t&&t.options&&t.options.adTargeting&&(t.options.adTargeting.psg=e)}))}"function"==typeof window.__buildAd?window.__mwads.uacQ.forEach((function(e){window.__buildAd(e)})):(window.uacQueue||(window.uacQueue=[]),Array.prototype.push.apply(window.uacQueue,window.__mwads.uacQ))}var t})),googletag.cmd.push((function(){var e=/curated--(A|B|C|D)/i;document.querySelectorAll(".component--curated").forEach((function(t){var n=t.querySelector(".is-native .j-ad");if(n){var a=n.getAttribute("id");if(a&&window.adslots&&window.adslots.hasOwnProperty(a)&&window.adslots[a].slot){var o=e.exec(t.className);o&&o.length>1&&(window.adslots[a].slot.setTargeting("ntvPlacement",window.__mwads.curatedMap[o[1]]),window.adslots[a].slot.setTargeting("pagetemplate","layout"+o[1]))}}}))})),window.addEventListener("curatedUpdate",(function(){document.querySelector(".component--curated .is-native")&&"undefined"!=typeof PostRelease&&"function"==typeof PostRelease.Start&&MarketWatch&&MarketWatch.Settings&&MarketWatch.Settings.snare&&PostRelease.Start({ptd:MarketWatch.Settings.snare.nativeIds})})),window.addEventListener("viewModeChanged",(function(){googletag.cmd.push((function(){if(window.adslots){for(var e=Object.keys(window.adslots),t=[],n=0;n<e.length;n++)window.adslots[e[n]]&&window.adslots[e[n]].adAlreadyRequested&&window.adslots[e[n]].slot&&t.push(window.adslots[e[n]].slot);googletag.pubads().refresh(t)}}))}))}}(),function(e,t){var n=function(e,t){"use strict";if(t.getElementsByClassName){var n,a=t.documentElement,o=e.HTMLPictureElement&&"sizes"in t.createElement("img"),s="addEventListener",i="getAttribute",r=e[s],d=e.setTimeout,l=e.requestAnimationFrame||d,c=/^picture$/i,u=["load","error","lazyincluded","_lazyloaded"],f={},m=Array.prototype.forEach,g=function(e,t){return f[t]||(f[t]=new RegExp("(\\s|^)"+t+"(\\s|$)")),f[t].test(e[i]("class")||"")&&f[t]},p=function(e,t){g(e,t)||e.setAttribute("class",(e[i]("class")||"").trim()+" "+t)},w=function(e,t){var n;(n=g(e,t))&&e.setAttribute("class",(e[i]("class")||"").replace(n," "))},y=function(e,t,n){var a=n?s:"removeEventListener";n&&y(e,t),u.forEach((function(n){e[a](n,t)}))},v=function(e,n,a,o,s){var i=t.createEvent("CustomEvent");return i.initCustomEvent(n,!o,!s,a||{}),e.dispatchEvent(i),i},h=function(t,a){var s;!o&&(s=e.picturefill||n.pf)?s({reevaluate:!0,elements:[t]}):a&&a.src&&(t.src=a.src)},z=function(e,t){return(getComputedStyle(e,null)||{})[t]},E=function(e,t,a){for(a=a||e.offsetWidth;a<n.minSize&&t&&!e._lazysizesWidth;)a=t.offsetWidth,t=t.parentNode;return a},_=function(t){var n,a=0,o=e.Date,s=function(){n=!1,a=o.now(),t()},i=function(){d(s)},r=function(){l(i)};return function(){if(!n){var e=125-(o.now()-a);n=!0,6>e&&(e=6),d(r,e)}}},b=function(){var o,u,f,E,b,A,N,S,M,R,k,B,L,W,x,I=/^img$/i,O=/^iframe$/i,q="onscroll"in e&&!/glebot/.test(navigator.userAgent),P=0,T=0,D=0,Q=function(e){T--,e&&e.target&&y(e.target,Q),(!e||0>T||!e.target)&&(T=0)},F=function(e,n){var o,s=e,i="hidden"==z(t.body,"visibility")||"hidden"!=z(e,"visibility");for(M-=n,B+=n,R-=n,k+=n;i&&(s=s.offsetParent)&&s!=t.body&&s!=a;)(i=(z(s,"opacity")||1)>0)&&"visible"!=z(s,"overflow")&&(o=s.getBoundingClientRect(),i=k>o.left&&R<o.right&&B>o.top-1&&M<o.bottom+1);return i},$=function(){var e,t,s,r,d,l,c,m,g;if((b=n.loadMode)&&8>T&&(e=o.length)){t=0,D++,null==W&&("expand"in n||(n.expand=a.clientHeight>600?a.clientWidth>860?500:410:359),L=n.expand,W=L*n.expFactor),W>P&&1>T&&D>3&&b>2?(P=W,D=0):P=b>1&&D>2&&6>T?L:0;for(;e>t;t++)if(o[t]&&!o[t]._lazyRace)if(q)if((m=o[t][i]("data-expand"))&&(l=1*m)||(l=P),g!==l&&(N=innerWidth+l*x,S=innerHeight+l,c=-1*l,g=l),s=o[t].getBoundingClientRect(),(B=s.bottom)>=c&&(M=s.top)<=S&&(k=s.right)>=c*x&&(R=s.left)<=N&&(B||k||R||M)&&(f&&3>T&&!m&&(3>b||4>D)||F(o[t],l))){if(J(o[t]),d=!0,T>9)break}else!d&&f&&!r&&4>T&&4>D&&b>2&&(u[0]||n.preloadAfterLoad)&&(u[0]||!m&&(B||k||R||M||"auto"!=o[t][i](n.sizesAttr)))&&(r=u[0]||o[t]);else J(o[t]);r&&!d&&J(r)}},j=_($),H=function(e){p(e.target,n.loadedClass),w(e.target,n.loadingClass),y(e.target,H)},U=function(e){var t,a,o=e[i](n.srcsetAttr);(t=n.customMedia[e[i]("data-media")||e[i]("media")])&&e.setAttribute("media",t),o&&e.setAttribute("srcset",o),t&&((a=e.parentNode).insertBefore(e.cloneNode(),e),a.removeChild(e))},G=function(){var e,t=[],n=function(){for(;t.length;)t.shift()();e=!1};return function(a){t.push(a),e||(e=!0,l(n))}}(),J=function(e){var t,a,o,s,r,l,u,z=I.test(e.nodeName),_=z&&(e[i](n.sizesAttr)||e[i]("sizes")),b="auto"==_;(!b&&f||!z||!e.src&&!e.srcset||e.complete||g(e,n.errorClass))&&(b&&(u=e.offsetWidth),e._lazyRace=!0,T++,G((function(){e._lazyRace&&delete e._lazyRace,(r=v(e,"lazybeforeunveil")).defaultPrevented||(_&&(b?(C.updateElem(e,!0,u),p(e,n.autosizesClass)):e.setAttribute("sizes",_)),a=e[i](n.srcsetAttr),t=e[i](n.srcAttr),z&&(o=e.parentNode,s=o&&c.test(o.nodeName||"")),l=r.detail.firesLoad||"src"in e&&(a||t||s),r={target:e},l&&(y(e,Q,!0),clearTimeout(E),E=d(Q,2500),p(e,n.loadingClass),y(e,H,!0)),s&&m.call(o.getElementsByTagName("source"),U),a?e.setAttribute("srcset",a):t&&!s&&(O.test(e.nodeName)?function(e,t){try{e.contentWindow.location.replace(t)}catch(n){e.src=t}}(e,t):e.src=t),(a||s)&&h(e,{src:t})),w(e,n.lazyClass),(!l||e.complete)&&(l?Q(r):T--,H(r))})))},K=function(){if(!f){if(Date.now()-A<999)return void d(K,999);var e,t=function(){n.loadMode=3,j()};f=!0,n.loadMode=3,T||(D?j():d($)),r("scroll",(function(){3==n.loadMode&&(n.loadMode=2),clearTimeout(e),e=d(t,99)}),!0)}};return{_:function(){A=Date.now(),o=t.getElementsByClassName(n.lazyClass),u=t.getElementsByClassName(n.lazyClass+" "+n.preloadClass),x=n.hFac,r("scroll",j,!0),r("resize",j,!0),e.MutationObserver?new MutationObserver(j).observe(a,{childList:!0,subtree:!0,attributes:!0}):(a[s]("DOMNodeInserted",j,!0),a[s]("DOMAttrModified",j,!0),setInterval(j,999)),r("hashchange",j,!0),["focus","mouseover","click","load","transitionend","animationend","webkitAnimationEnd"].forEach((function(e){t[s](e,j,!0)})),/d$|^c/.test(t.readyState)?K():(r("load",K),t[s]("DOMContentLoaded",j),d(K,2e4)),j(o.length>0)},checkElems:j,unveil:J}}(),C=function(){var e,a=function(e,t,n){var a,o,s,i,r=e.parentNode;if(r&&(n=E(e,r,n),!(i=v(e,"lazybeforesizes",{width:n,dataAttr:!!t})).defaultPrevented&&((n=i.detail.width)&&n!==e._lazysizesWidth))){if(e._lazysizesWidth=n,n+="px",e.setAttribute("sizes",n),c.test(r.nodeName||""))for(o=0,s=(a=r.getElementsByTagName("source")).length;s>o;o++)a[o].setAttribute("sizes",n);i.detail.dataAttr||h(e,i.detail)}},o=_((function(){var t,n=e.length;if(n)for(t=0;n>t;t++)a(e[t])}));return{_:function(){e=t.getElementsByClassName(n.autosizesClass),r("resize",o)},checkElems:o,updateElem:a}}(),A=function(){A.i||(A.i=!0,C._(),b._())};return function(){var t,a={lazyClass:"lazyload",loadedClass:"lazyloaded",loadingClass:"lazyloading",preloadClass:"lazypreload",errorClass:"lazyerror",autosizesClass:"lazyautosizes",srcAttr:"data-src",srcsetAttr:"data-srcset",sizesAttr:"data-sizes",minSize:40,customMedia:{},init:!0,expFactor:1.7,hFac:.8,loadMode:2};for(t in n=e.lazySizesConfig||e.lazysizesConfig||{},a)t in n||(n[t]=a[t]);e.lazySizesConfig=n,d((function(){n.init&&A()}))}(),{cfg:n,autoSizer:C,loader:b,init:A,uP:h,aC:p,rC:w,hC:g,fire:v,gW:E}}}(e,e.document);e.lazySizes=n,"object"==typeof module&&module.exports?module.exports=n:"function"==typeof define&&define.amd&&define(n)}(window);</script>
            
            <div class="region region--lightbox j-lightbox j-browserUpgradeMessage">
            <div class="lightbox lightbox--template">
                <div class="column column--full j-content">
                    <div class="lightbox__header">
                        <button class="toggle--overlay j-cancel">&times;</button>
                        <header class="header header--secondary">
                            <h2 class="title">
                                <span class="label">Time to Upgrade!</span>
                            </h2>
                        </header>
                    </div>
                    <div class="lightbox__body message h-auto">
                        <div class="element element--text">
                        <p class="text">This browser is no longer supported at MarketWatch. For the best MarketWatch.com experience, please update to a modern browser.</p>
                        </div>
                        <div class="group group--buttons">
                        <a class="btn btn--primary" href="https://www.google.com/chrome/">Chrome</a>
                        <a class="btn btn--primary" href="https://support.apple.com/downloads/safari">Safari</a>
                        <a class="btn btn--primary" href="https://www.mozilla.org/en-US/firefox/">Firefox</a>
                        <a class="btn btn--primary" href="https://www.microsoft.com/en-us/windows/microsoft-edge">Edge</a>
                        </div>
                    </div>
                </div>
            </div>
            </div>
            
                <!-- Tealium -->
                <script type="text/javascript">
                    (function() {
                        function loadTealiumScript() {
                            var script = document.createElement('script');
                            script.async = true;
                            script.src = '//tags.tiqcdn.com/utag/wsjdn/marketwatch/prod/utag.js';
                            var element = document.getElementsByTagName('script')[0];
                            element.parentElement.insertBefore(script, element);
                        }

                        __ace('djcmp', 'executeOnCmpReady', [{ cb: loadTealiumScript }]);    
                    })();
                </script>

                <script async defer src="https://sts3.wsj.net/bucket-a/maggie/static/js/thirdparty-0b98698a66.min.js"></script>
                
            
        </body>
        </html>
        """
