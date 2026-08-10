# Digimart Japan Used Instruments Scraper — デジマート 中古楽器スクレイパー

**Full instrument listings & prices from Digimart (デジマート), Japan's largest used-instrument marketplace (~2,000 shops).**

Scrape complete product data — not just stats — for guitars, basses, keyboards, drums, wind instruments and more. Get every listing with brand, category, condition rank, price vs. list price, shop name, stock status and images. Perfect for resale arbitrage, price monitoring, and Japanese used-gear market research.

## 🚀 Quick Start

1. Open [Digimart Japan Used Instruments Scraper on Apify Store](https://apify.com/fruitful_quintessence/digimart-japan-used-instrument-scraper)
2. Enter a keyword (e.g. "Fender", "ギター", "Martin") — comma-separated for batch search
3. Run and export as JSON, CSV, or XLSX

**Pricing:** Pay per event — $0.002/result + start fee.

## 📋 Output Fields

| Field | Type | Description |
|-------|------|-------------|
| `productId` | string | Digimart product ID |
| `title` | string | Instrument title |
| `brand` | string | Brand (Fender, Gibson, Ibanez, Yamaha...) |
| `category` | string | Product category |
| `price` | int | **Selling price** in JPY |
| `listPrice` | int\|null | **Original list price** in JPY (arbitrage signal) |
| `condition` | string | Condition rank (S/A/B/C/D...) |
| `instruTypeLabel` | string | 新品 / 中古 / ビンテージ / 新品アウトレット / B-stock |
| `inStock` | bool | In-stock status |
| `shopName` | string | Selling shop (~2,000 shops across Japan) |
| `registeredAt` | string | Listing date |
| `imageUrl` | string | Product image |
| `productUrl` | string | Product page URL |
| `scrapedAt` | string | Scrape timestamp |

## 🎯 Use Cases

1. **Resale arbitrage** — find instruments priced below list price or below market
2. **Price trend tracking** — monitor specific models (e.g. a Gibson Les Paul model) over time
3. **Import/export research** — Japanese gear demand analysis for overseas resellers
4. **Shop comparison** — compare the same instrument across 2,000+ Japanese shops
5. **AI/ML datasets** — training data for price prediction models

## ⚙️ Input

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `searchKeyword` | string | Fender | Keyword(s), comma-separated for batch |
| `maxItems` | int | 100 | Max items per keyword |
| `maxPages` | int | 3 | Max pages per keyword (20 items/page) |
| `proxyConfiguration` | proxy | auto | Apify proxy (recommended) |

## 📊 Example Output

```json
{
  "productId": "DS10679421",
  "title": "Limited Edition Acoustasonic Standard Telecaster",
  "brand": "Fender",
  "category": "アコースティックギター",
  "price": 89800,
  "listPrice": 104500,
  "condition": "S",
  "instruTypeLabel": "新品",
  "inStock": true,
  "shopName": "ロッキン 岐阜店 イオンモール各務原店",
  "imageUrl": "https://img.digimart.net/prdimg/s/50/323d...",
  "productUrl": "https://www.digimart.net/cat2/shop4978/DS10679421/",
  "scrapedAt": "2026-08-10T06:00:00Z"
}
```

## ⚠️ Notes

- Data is scraped from public search pages only (factual listing data: names, prices, stock, shop).
- Digimart search index contains 170,000+ items for popular keywords.
- Polite scraping: 0.5–1.5s delay between requests.

## 🔧 Development

```bash
pip install httpx beautifulsoup4
python3 src/main.py   # local mode, prints JSON
```

MIT License. Please respect Digimart's terms of service.
