def render_dulce_list(dulces):

    return [
        {
            "id": dulce.id,
            "brand":dulce.brand,
            "weight":dulce.weight,
            "flavor":dulce.flavor,
            "origin":dulce.origin,
        }
        for dulce in dulces
    ]


def render_dulce_detail(dulce):

    return {
            "id": dulce.id,
            "brand":dulce.brand,
            "weight":dulce.weight,
            "flavor":dulce.flavor,
            "origin":dulce.origin,
    }