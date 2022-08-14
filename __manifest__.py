{
    'name': 'estate',
    'depends': ['base'],

    'application': True,

    'version': '0.1',
    'author': "Young Maeng",
    'category': 'Tutorial',

    'description': """
    This is Test Module
    """,

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
    ]
}
