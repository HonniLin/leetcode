def merge(self, intervals):
    """
    给一些区间，要求这些区间如果有交集的要合并，返回合并后的区间集合
    """
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out