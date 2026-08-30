for a in range(3):  #####dont forget to change haaaa########
    from datetime import datetime
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d") 
    current_time = now.strftime("%H:%M:%S") 
    current_day  = now.strftime("%A") 
    print(f"Timestamp")
    print(f"Date: {current_date}")
    print(f"Time: {current_time}")
    print(f"Day : {current_day}")
    def mkt_status(current_day, current_time):
        mkt_status=""
        minute=int(current_time[3:5])
        hour=int(current_time[0:2])
        active_days=["Monday","Tuesday" "Wednesday", "Thursday", "Friday"]
        if current_day in active_days and hour>8 and hour<16:
            mkt_stat="active"
        else:
            mkt_stat="closed"
        return mkt_stat
    market_status=mkt_status(current_day,current_time)
    print(market_status)

    