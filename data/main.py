import kagglehub
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent

load_dotenv()

path = kagglehub.competition_download('home-data-for-ml-course')

train_data = pd.read_csv(Path(path) / 'train.csv')
test_data = pd.read_csv(Path(path) / 'test.csv')

train_data.to_csv(DATA_DIR / 'train.csv')
test_data.to_csv(DATA_DIR / 'test.csv')