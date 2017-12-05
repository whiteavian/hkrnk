def is_balanced(s):
    stack = []

    for l in s:
        if l in ("[", "(", "{"):
            stack.append(l)
        else:
            if len(stack) == 0:
                return "NO"
            match = stack.pop()
            if not ((l == ")" and match == "(")
                    or (l == "}" and match == "{")
                    or (l == "]" and match == "[")
                    ):
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

def get_top(h1, h2, h3):
    h1_heights = get_heights(h1)
    h2_heights = get_heights(h2)
    h3_heights = get_heights(h3)

    while len(h1_heights) > 0 and len(h2_heights) > 0 and len(h3_heights) > 0:
        m1 = h1_heights[-1]
        m2 = h2_heights[-1]
        m3 = h3_heights[-1]

        if m1 == m2 == m3:
            return m1
        else:
            if m1 > m2 or m1 > m2:
                h1_heights.pop()
            if m1 < m2 or m3 < m2:
                h2_heights.pop()
            if m1 < m3 or m2 < m3:
                h3_heights.pop()

    return 0

def get_heights(h):
    heights = []
    height = 0

    while len(h) > 0:
        height += h.pop()
        heights.append(height)

    return heights


def largest_rectangle(h):
    max_rect = 0

    for i in range(len(h)):
        j = i - 1
        curr_max = h[i]

        while j >= 0:
            if h[j] >= h[i]:
                curr_max += h[i]
                j -= 1
            else:
                j = -1

        j = i + 1
        while j < len(h):
            if h[j] >= h[i]:
                curr_max += h[i]
                j += 1
            else:
                j = len(h)

        if curr_max > max_rect:
            max_rect = curr_max

    return max_rect


def poisonous_plants(p):
    stacks = [[p[0]]]
    days = 0

    for i in range(1, len(p)):
        if p[i] > p[i-1]:
            stacks.append([p[i]])
        else:
            stacks[-1].append(p[i])

    while len(stacks) > 1:
        days += 1
        for s in stacks[1:]:
            if len(s) > 0:
                s.pop(0)

        # Remove the empty stacks.
        i = len(stacks) - 1
        while i > 0:
            if len(stacks[i]) == 0:
                stacks.pop(i)
            i -= 1

        # Merge consecutive stacks
        i = len(stacks) - 1
        while i > 0:
            if stacks[i-1][-1] >= stacks[i][0]:
                stacks[i-1].extend(stacks.pop(i))
            i -= 1

    return days
