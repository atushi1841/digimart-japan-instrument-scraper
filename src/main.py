import asyncio
import json
import random
from urllib.parse import quote

import httpx

try:
    from apify import Actor
except ImportError:
    Actor = None

from scraper import fetch_page, parse_page


async def main():
    if Actor:
        await Actor.init()
        actor_input = await Actor.get_input() or {}
    else:
        actor_input = {}

    search_keyword = actor_input.get('searchKeyword', 'Fender') or 'Fender'
    if isinstance(search_keyword, str):
        keyword_list = [k.strip() for k in search_keyword.split(',') if k.strip()]
    elif isinstance(search_keyword, (list, tuple)):
        keyword_list = [str(k).strip() for k in search_keyword if str(k).strip()]
    else:
        keyword_list = ['Fender']
    if not keyword_list:
        keyword_list = ['Fender']

    max_items = int(actor_input.get('maxItems', 100) or 100)
    max_pages = int(actor_input.get('maxPages', 3) or 3)

    proxy_config = actor_input.get('proxyConfiguration')
    proxy_url = None
    if Actor and proxy_config:
        try:
            proxy = await Actor.create_proxy_configuration(actor_proxy_input=proxy_config)
            proxy_url = await proxy.new_url()
        except Exception:
            proxy_url = None

    collected = 0
    results = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    kwargs = {}
    if proxy_url:
        kwargs['proxy'] = proxy_url

    async with httpx.AsyncClient(headers=headers, timeout=30.0, **kwargs) as client:
        for kw in keyword_list:
            if collected >= max_items:
                break
            for page in range(1, max_pages + 1):
                if collected >= max_items:
                    break
                url = (f'https://www.digimart.net/search?dispMode=ALL&keyword={quote(kw)}'
                       f'&currentPage={page}&maxCount=20')
                html = await fetch_page(client, url)
                if html is None:
                    continue
                items = parse_page(html)
                if not items:
                    break
                for item in items:
                    if collected >= max_items:
                        break
                    if Actor:
                        await Actor.push_data(item)
                    else:
                        results.append(item)
                    collected += 1
                await asyncio.sleep(random.uniform(0.5, 1.5))

    if Actor:
        await Actor.exit()
    else:
        print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
