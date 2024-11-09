
import aiohttp


URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={cpe}&isVulnerable"

async def from_cpe(cpe: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(URL.format(cpe=cpe)) as response:
            response.raise_for_status()
            return await response.json()

