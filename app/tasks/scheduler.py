from apscheduler.schedulers.background import BackgroundScheduler
from .scraping.example import fetch_title
import atexit, logging
logging.basicConfig(level=logging.INFO)
scheduler = BackgroundScheduler()

def start():
    # 10분마다 한 번
    scheduler.add_job(lambda: logging.info(fetch_title("https://www.python.org/")),
                      "interval", minutes=10, id="title_job", replace_existing=True)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown(wait=False))
