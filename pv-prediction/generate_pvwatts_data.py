import argparse
import json
import pandas as pd 
from pathlib import Path
import os
from dotenv import load_dotenv

parser = argparse.ArgumentParser(
    prog="generate_pvwattsdata",
    description="Generates power generation data using the PVWATTS API"
) 

parser.add_argument("--path, -p")

load_dotenv()

API_KEY = os.environ.get("API_KEY")
FORMAT = "json"
PVWATTS_URL = f"https://developer.nrel.gov/api/pvwatts/v8.{FORMAT}"