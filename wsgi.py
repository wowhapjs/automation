from app import create_app
app = create_app()

# (선택) 스케줄러 쓰면 주석 해제
# from app.tasks.scheduler import start as start_scheduler
# start_scheduler()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
