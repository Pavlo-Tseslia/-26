import aiohttp


async def get_price(symbol):
    mapping = {
        "ton": "the-open-network",
        "btc": "bitcoin",
        "eth": "ethereum"
    }

    coin_id = mapping.get(symbol)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

    return data.get(coin_id, {}).get("usd")
