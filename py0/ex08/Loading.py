import os


def timeFormating(time):
    """
    Convert a time duration in seconds to a string formatted as MM:SS.

    Parameters:
        time (float): Duration in seconds.

    Returns:
        str: Time formatted as 'MM:SS'.
    """
    # m get the result of elapsed / 60, and s get the modulo of the operation
    m, s = divmod(time, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    """
    Implementation of a progress bar similar to tqdm, using only the os module.

    Parameters:
        lst (range): Iterable sequence to iterate over, typically a range.

    Behavior:
        - Displays a progress bar with:
            * Percentage of completion
            * Dynamic progress bar width based on terminal size
            * Elapsed time
            * Estimated remaining time (ETA)
            * Iterations per second (speed)
        - Updates the display every 0.1 seconds to reduce flicker
        - Yields each item from the input iterable while updating the bar
        - Uses os.times().elapsed for timing measurements

    Returns:
        None (generator function: yields items from the iterable).
    """
    total = len(lst)
    progress = 0
    timeStart = os.times()
    terminalSize = os.get_terminal_size()
    barWidth = 1
    last_print = timeStart

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
        string = (f"| {i}/{total} [{elapsed_timeFormated}<"
                  f"{predicted_time_formated}, {speed:.2f}it/s]")
        barWidth = terminalSize.columns - len(string) - 5

        current_time = os.times()
        if (last_print.elapsed < current_time.elapsed - 0.1) or i == total:
            print(f"\r{' ' if percent != 100 else ''}"
                  f"{percent}%{progress_bar}{' ' * int(barWidth - progress)}"
                  f"{string}", end="",)
            last_print = os.times()
        yield item
