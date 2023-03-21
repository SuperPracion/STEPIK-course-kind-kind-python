def get_loss(w1, w2, w3, w4):
    try:
        y = w1 // w2
    except:
        return "деление на ноль"
    else:
        return 10 * y - 5 * w2 * w3 + w4