from fastapi import FastAPI, HTTPException
import os
from typing import List

app = FastAPI()

BASE_DIRECTORY = "/path/to/base/directory"  # 基本ディレクトリを設定


def list_files(subdirectory: str) -> List[str]:
    directory = os.path.join(BASE_DIRECTORY, subdirectory)
    if not os.path.exists(directory):
        raise HTTPException(status_code=404, detail="Directory not found")

    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


@app.get("/files/{subdirectory:path}")
async def read_files(subdirectory: str):
    return list_files(subdirectory)
