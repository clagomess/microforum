from post.dao import get_post_dao


def get_post_service(param):
    rspai = get_post_dao(param)
    rsfilho = None
    seq_post_pai = []

    to_return = {}

    for rowpai in rspai:
        if rowpai.get('num_post_filho') > 0:
            seq_post_pai.append(rowpai.get('seq_post'))

        to_return[rowpai.get('seq_post')] = rowpai

    if len(seq_post_pai) > 0 and 'seq_post_pai' not in param:
        rsfilho = get_post_dao({
            'tipo': 'filho',
            'seq_post_pai': seq_post_pai
        })

    if rsfilho:
        for rowfilho in rsfilho:
            idx = rowfilho.get('seq_post_pai')

            if 'row_filho' not in to_return[idx]:
                to_return[idx]['row_filho'] = []

            to_return[idx]['row_filho'].append(rowfilho)

    return to_return

