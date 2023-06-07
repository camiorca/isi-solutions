def find_article_references(id_list: dict):
    if len(id_list) == 0:
        return None

    test = []
    test_res = []
    for key in id_list.keys():
        test.append(
            [(key, list(filter(lambda ex: id_list[ex] == val, id_list))[0]) for val in id_list.values() if key in val]
        )

    for items in test:
        test_res = test_res + items

    return set(tuple(sorted(i)) for i in test_res)
