import os


def timeFormating(time):
    # m get the result of elapsed / 60, and s get the modulo of the operation
    m, s = divmod(time, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    progress = 0
    timeStart = os.times()
    terminalSize = os.get_terminal_size()
    barWidth = terminalSize.columns - 39

    for i, item in enumerate(lst, start=1):
        progress = int((i / total) * barWidth)
        progress_bar = f"|{'█' * progress}"
        percent = int(progress / barWidth * 100)

        elapsed_time = os.times().elapsed - timeStart.elapsed
        elapsed_timeFormated = timeFormating(elapsed_time)
        
        if (progress != 0 and barWidth != 0):
            predicted_time = elapsed_time * barWidth / progress
        else:
           predicted_time = 0
        if elapsed_time != 0 and i != 0:
            speed = i / elapsed_time
        else:
            speed = 0
        predicted_time -= elapsed_time
        predicted_time_formated = timeFormating(predicted_time)
        string = f"| {i}/{total} [{elapsed_timeFormated}<{predicted_time_formated}, {speed:.2f}it/s]"
        
        if (i % 10 == 0) or i == total:
            print(f"\r{' ' if percent != 100 else ''}{percent}%{progress_bar}{' ' * int(barWidth - progress)}{string}", end="",)
        yield item
