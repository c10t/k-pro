#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
# from time import perf_counter


def main():
    h, w = map(int, input().split())
    max_value = h + w
    gridmap = []

    for y in range(h):
        gridmap.append([0 if v == '#' else max_value for v in input().strip()])

    values = np.array(gridmap)

    for x in range(w - 1):
        values[:, x + 1] = np.minimum(values[:, x] + 1, values[:, x + 1])

    for x in range(w - 1, 0, -1):
        values[:, x - 1] = np.minimum(values[:, x] + 1, values[:, x - 1])

    for y in range(h - 1):
        values[y + 1, :] = np.minimum(values[y, :] + 1, values[y + 1, :])

    for y in range(h - 1, 0, -1):
        values[y - 1, :] = np.minimum(values[y, :] + 1, values[y - 1, :])

    print(np.max(values))


if __name__ == '__main__':
    # st = perf_counter()
    main()
    # ed = perf_counter()
    # print(ed - st)
