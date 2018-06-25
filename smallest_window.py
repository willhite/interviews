

def next_bit(bits, start):
    for i in range(start, len(bits)):
        if bits[i] == '1':
            return i;
    return -1

def smallest_window(bits, num):
    start = next_bit(bits, 0)
    end = 0
    for i in range(num):
        end = next_bit(bits, end+1);
        if end == -1:
            return (None, None, None)
    (ws, we, wl) = (start, end, end - start)
    # print("1 ws:", ws, "we:", we, "wl:", wl, "bits:", bits[ws:we+1])
    while True:
        start = next_bit(bits, start+1)
        end = next_bit(bits, end+1)
        if end < 0:
            break;
        # print("2 ws:", start, "we:", end, "wl:", end-start, "bits:", bits[start:end+1])
        if end-start < wl:
            (ws, we, wl) = (start, end, end-start)
    return (ws, we, wl)



test_cases = [
    ["001100010010010001000001011100010001", 4],
    ["001100010010010001000001011100010001", 40],
    ["001100010010010001000001011100010001", 3],
    ["001100010010010001000001011100010001", 6],
    ["111111100000000000000000000000000000", 6],
]

for tc in test_cases:
    (ws, we, wl) = smallest_window(tc[0], tc[1])
    if ws is not None:
        print("smallest window, numbits:", tc[1], "ws:", ws, "we:", we, "wl:", wl, "bits:", tc[0][ws:we+1])
    else:
        print("smallest window:", None)