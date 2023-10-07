def _convert_to_bits(message: str):
    pass

def _add_padding(message):
    pass

def _splice_bit_sequence(message):
    pass

def _process_round(chunk, state: tuple, function: function):
    A = state[0]
    B = state[1]
    C = state[2]
    D = state[3]

    state[0] = D

    # TODO calculate new B

    state[2] = B
    state[3] = C

    return state

def _F(B, C, D):
    pass

def _G(B, C, D):
    pass

def _H(B, C, D):
    pass

def _I(B, C, D):
    pass
    
def _convert_to_hexadecimal(bit_sequence: tuple):
    pass

def MD5(message: str):
    message = _add_padding(_convert_to_bits(message))
    chunks: list = _splice_bit_sequence(message)
    state: tuple = () # TODO initialize state

    for chunk in chunks:
        state = _process_round(chunk, state, _F)
        state = _process_round(chunk, state, _G)
        state = _process_round(chunk, state, _H)
        state = _process_round(chunk, state, _I)

    return _convert_to_hexadecimal(state)