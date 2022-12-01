# ------------ Documentation --------
# some documentation in markdown
description = """  
## Documentation
**TODO: Read carefully before using**

This api allows you to perform basic image,video,and audio functions over the web be it in your app or webapp.  
We will also include imaging capabilitied over the web.... 



_Build credits:_

```text
    *Python imageio
    *Huggingface Models
```

___

## To run locally: ```$uvicorn app:main --reload```

"""

# -----------------------------------

from typing import Union
from fastapi import FastAPI





app = FastAPI(
    title="IPT API FOR Quick [image,audio,vedio] editing & ML Models",
    description=description,
    version="0.0.0",
    contact={
        "name": "",
        "emails": "",
    },
)

@app.get("/welcome_test/{test}")
def read_root(test:str):
    return {"test_info_success":test}


