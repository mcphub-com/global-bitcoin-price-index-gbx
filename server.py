import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/blockchain-data-ltd-blockchain-data-ltd-default/api/global-bitcoin-price-index-gbx'

mcp = FastMCP('global-bitcoin-price-index-gbx')

@mcp.tool()
def ticker_per_symbol(market: Annotated[str, Field(description='Possible values: global, local')],
                      symbol: Annotated[str, Field(description='BTC, where is valid ISO currency (ex. BTCUSD, BTCEUR)')]) -> dict: 
    '''Returns ticker data for specified market symbol.'''
    url = 'https://bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com/indices/global/ticker/BTCUSD'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'market': market,
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ticker_data(fiat: Annotated[Union[str, None], Field(description='Comma separated list of ISO currency codes (ex. USD,EUR)')] = None,
                crypto: Annotated[Union[str, None], Field(description='valid value: BTC')] = None) -> dict: 
    '''If no query parameters are sent, then returns ticker data for every supported symbol. If fiat(s) are sent as parameters, then only the ticker for those values is sent.'''
    url = 'https://bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com/indices/local/ticker/all'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fiat': fiat,
        'crypto': crypto,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def ticker_changes(market: Annotated[str, Field(description='Possible values: global, local')],
                   symbol: Annotated[str, Field(description='Possible values: BTC where is valid ISO currency (ex. BTCUSD)')]) -> dict: 
    '''Returns ticker values and price changes for specified market and symbol.'''
    url = 'https://bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com/indices/local/ticker/BTCUSD/changes'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'market': market,
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def short_ticker(fiats: Annotated[Union[str, None], Field(description="If fiats parameter is included then only the values for those fiats will be returned (BTCUSD and BTCEUR in this example). If it's missing, then the response will contain ticker values of all available fiats for BTC.")] = None,
                 crypto: Annotated[Union[str, None], Field(description='Valid value: BTC')] = None) -> dict: 
    '''Returns basic ticker denoting last and daily average price for all symbols'''
    url = 'https://bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com/indices/global/ticker/short'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fiats': fiats,
        'crypto': crypto,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def custom_ticker(exchanges: Annotated[Union[str, None], Field(description='Comma separated list of exchanges.')] = None) -> dict: 
    '''This endpoint can be used to generate a custom index in a certain currency. The “inex” path parameter represents “include” or “exclude”, you can choose to generate an index removing specified exchanges, or only including the few that you require.'''
    url = 'https://bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com/indices/ticker/custom/include/BTCUSD'
    headers = {'x-rapidapi-host': 'bitcoinaverage-global-bitcoin-index-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'exchanges': exchanges,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
