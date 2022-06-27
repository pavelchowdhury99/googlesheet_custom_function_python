from fastapi import Request, FastAPI
from pydantic import BaseModel
from shapely import wkb
import logging
logging.basicConfig(level=logging.DEBUG)


def convert_wkb_wkt(text: str) -> str:
    p = wkb.loads(text, hex=True)
    return str(p)

class WKB(BaseModel):
    wkb_hex: str

app = FastAPI()

@app.post("/get-wkt-from-wkb")
async def get_email(inp: WKB, request: Request):
    return convert_wkb_wkt(inp.wkb_hex)
