from fastapi import FastAPI
from pydantic import BaseModel
from shapely import wkb


class WKB_HEX(BaseModel):
    wkb_hex: str


def convert_wkb_wkt(text: str) -> str:
    out = wkb.loads(text, hex=True)
    return str(out)

app = FastAPI()

@app.post('/get-wkt-from-wkb')
def get_wkt_from_wkb(inp:WKB_HEX):
    return convert_wkb_wkt(inp.wkb_hex)

@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')

if __name__ == '__main__':
    print(convert_wkb_wkt('010100000000b884a9329436409c878310301e5640'))
