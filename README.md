# Global Bitcoin Price Index - GBX

## Overview

The Global Bitcoin Price Index (GBX) is a comprehensive service offering real-time and historical Bitcoin pricing data. This robust platform aggregates data from over 100 of the world's leading cryptocurrency exchanges, providing market insights for more than 1,000 crypto assets and thousands of market pairs. The GBX is recognized as a standard in the cryptocurrency industry, trusted by thousands of users worldwide, including websites, apps, services, and businesses.

## Features

- **Real-Time Data**: Receive up-to-the-second updates on Bitcoin pricing.
- **Multi-Currency Support**: Access rates in 165+ different currencies.
- **Historical Data**: Analyze daily rates dating back to 2010.
- **Flexible Data Formats**: Choose between JSON or CSV formats for data retrieval.
- **Weighted Pricing**: Benefit from a weighted price calculation that considers exchange activity, liquidity, and fee methodologies.

## Usage

The GBX server provides several key tools for accessing and utilizing Bitcoin pricing data:

### 1. Ticker Per Symbol
- **Description**: Retrieve specific ticker data for a chosen market symbol.
- **Parameters**:
  - `market`: Specify either 'global' or 'local'.
  - `symbol`: Provide a valid ISO currency symbol (e.g., BTCUSD, BTCEUR).

### 2. Ticker Data
- **Description**: Obtain ticker data for all supported symbols or filter by specified fiat currencies.
- **Parameters**:
  - `fiat`: (Optional) List ISO currency codes separated by commas.
  - `crypto`: (Optional) Specify a valid cryptocurrency, such as BTC.

### 3. Ticker Changes
- **Description**: Access ticker values and price changes for a specified market and symbol.
- **Parameters**:
  - `market`: Choose between 'global' or 'local'.
  - `symbol`: Provide a valid ISO currency symbol (e.g., BTCUSD).

### 4. Short Ticker
- **Description**: Get basic ticker data, including last and daily average price for all symbols.
- **Parameters**:
  - `fiats`: (Optional) Specify fiat currencies to filter results.
  - `crypto`: (Optional) Provide a valid cryptocurrency, such as BTC.

### 5. Custom Ticker
- **Description**: Create a custom index in a specified currency by including or excluding certain exchanges.
- **Parameters**:
  - `exchanges`: (Optional) List exchanges separated by commas.

## Conclusion

The Global Bitcoin Price Index - GBX is an invaluable resource for anyone needing accurate and reliable Bitcoin pricing data, whether for analysis, reporting, payment processing, or software integration. With its extensive historical data and real-time updates, GBX serves as a critical tool in the cryptocurrency ecosystem.