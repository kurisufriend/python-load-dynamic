from events_def import events
triggers = [events.PER_TICK, events.ONCE]
def run(ctx):
    print("woooo, script2!")
    if ctx:
        print("run on tick:", ctx)