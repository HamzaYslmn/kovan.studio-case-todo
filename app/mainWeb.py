
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import json
from datetime import datetime
from agent import analyze_cv

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


def save_result(result: str) -> None:
	os.makedirs("data/results", exist_ok=True)
	filename = f"data/results/result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
	with open(filename, "w", encoding="utf-8") as f:
		f.write(result)


@app.get("/", response_class=HTMLResponse)
async def root():
	with open("static/index.html", encoding="utf-8") as f:
		return f.read()


@app.post("/analyze-cv/")
async def analyze_cv_route(file: UploadFile = File(...)):
	if not file.filename.endswith(".md"):
		raise HTTPException(status_code=400, detail="Sadece .md dosyaları yüklenebilir.")
	
	cv_content = (await file.read()).decode("utf-8")
	result_text = await analyze_cv(cv_content)
	save_result(result_text)
	return json.loads(result_text)

if __name__ == "__main__":
	import uvicorn
	uvicorn.run(app, host="0.0.0.0", port=8080)