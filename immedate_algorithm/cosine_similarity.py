from immedate_algorithm import itemCount, pairCount
import numpy as np

def cosine():
    """
    use cosine method to caculate the items similarity
    :return:
    """
    i_p_count = itemCount.item_count()
    i_q_count = itemCount.item_count()
    p_count = pairCount.pair_count()

    dist = p_count / (np.sqrt(i_p_count) * np.sqrt(i_q_count))
    return dist