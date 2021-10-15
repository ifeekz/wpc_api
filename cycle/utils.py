import datetime

def validate_cycle_dates(data):
    date_format = "%Y-%m-%d"
    
    if data is None:
      return {"status": False, "message": "No data set provided"}
    try:
      last_period_date = datetime.datetime.strptime(data['last_period_date'], date_format).date()
      start_date = datetime.datetime.strptime(data['start_date'], date_format).date()
      end_date = datetime.datetime.strptime(data['end_date'], date_format).date()
      
      if last_period_date > start_date:
        return {"status": False, "message": "last_period_date cannot be greater than start_date"}
      
      if start_date >= end_date:
        return {"status": False, "message": "end_date must be greater than start_date"}
      
      return {"status": True}
    except ValueError:
      return {"status": False, "message": "Incorrect date string format in data set. All dates should be YYYY-MM-DD"}

def validate_event_date(event_date):
    date_format = "%Y-%m-%d"
    if event_date is None:
      return {"status": False, "message": "Please specify a date in this format - YYYY-MM-DD"}
    try:
      event_date = datetime.datetime.strptime(event_date, date_format)
      return {"status": True, "data": event_date.date()}
    except ValueError:
      return {"status": False, "message": "Incorrect date string format. It should be YYYY-MM-DD"}

def calculate_total_circles(data):
    total_created_cycles = 0
    last_period_date = data.last_period_date
    start_date = data.start_date
    end_date = data.end_date
    period_start_date = data.last_period_date + datetime.timedelta(days=data.cycle_average)
    
    while last_period_date <= end_date: # while last_period_date does not exceed the end_date
      if last_period_date >= start_date: # only when last_period_date has entered the start_date
        total_created_cycles = total_created_cycles + 1 # add a circle to total_created_cycles
        period_start_date = last_period_date + datetime.timedelta(days=data.cycle_average) # recalculate period_start_date from the last_period_date
      else:
        period_start_date = period_start_date + datetime.timedelta(days=data.cycle_average) # forward the period_start_date using the last period_start_date

      last_period_date = period_start_date # set the last_period_date to the new period_start_date

    return total_created_cycles

def create_event(event_date, cycle):
    events = []
    last_period_date = cycle.last_period_date
    start_date = cycle.start_date
    end_date = cycle.end_date
    period_start_date = cycle.last_period_date + datetime.timedelta(days=cycle.cycle_average)
    period_end_date = period_start_date + datetime.timedelta(days=cycle.period_average)
    
    while last_period_date <= end_date: # while last_period_date does not exceed the end_date
      if last_period_date >= start_date: # only when last_period_date has entered the start_date
        period_start_date = last_period_date + datetime.timedelta(days=cycle.cycle_average) # recalculate period_start_date from the last_period_date
        period_end_date = period_start_date + datetime.timedelta(days=cycle.period_average)

        ovulation_date = period_start_date + datetime.timedelta(days=(cycle.cycle_average//2))
        # fertility_window: four (4) days before and four (4) days after the ovulation date
        fertility_window_start_date = ovulation_date - datetime.timedelta(days=4)
        fertility_window_end_date = ovulation_date + datetime.timedelta(days=4)

        # pre_ovulation_window = From a day after period ends to a day before fertility_window begins
        pre_ovulation_window_start_date = period_end_date + datetime.timedelta(days=1)
        pre_ovulation_window_end_date = fertility_window_start_date - datetime.timedelta(days=1)

        # post_ovulation_window = From the day after the fertility window ends to a day before the next period starts
        post_ovulation_window_start_date = fertility_window_end_date + datetime.timedelta(days=1)
        post_ovulation_window_end_date = period_start_date + datetime.timedelta(days=cycle.cycle_average-1)

        if event_date >= fertility_window_start_date and event_date <= fertility_window_end_date:
          events.append({"event": "fertility_window", "date": event_date})

        if event_date >= pre_ovulation_window_start_date and event_date <= pre_ovulation_window_end_date:
          events.append({"event": "pre_ovulation_window", "date": event_date})

        if event_date >= post_ovulation_window_start_date and event_date <= post_ovulation_window_end_date:
          events.append({"event": "post_ovulation_window", "date": event_date})
      else:
        period_start_date = period_start_date + datetime.timedelta(days=cycle.cycle_average) # forward the period_start_date using the last period_start_date
        period_end_date = period_start_date + datetime.timedelta(days=cycle.period_average)

      last_period_date = period_start_date # set the last_period_date to the new period_start_date

    return events