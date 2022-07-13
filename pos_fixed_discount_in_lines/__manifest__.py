{
    "name": "Point of Sale - Fixed Discount in Line",
    "summary": "Order discount in line instead of discount product",
    "version": "14.0.1.0.0",
    "category": "Point Of Sale",
    "author": "Ilyas, Ooops404, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/pos",
    "license": "AGPL-3",
    "depends": [
        "pos_discount",
    ],
    "data": [
        "views/pos_templates.xml",
        "views/pos_discount_views.xml",
        "views/pos_views.xml",
        "data/product.xml",
    ],
    "qweb": [
        "static/src/xml/Screens/ProductScreen/OrderSummary.xml",
        "static/src/xml/Screens/ProductScreen/OrderWidget.xml",
        "static/src/xml/Screens/PaymentScreen/PaymentScreen.xml",
        "static/src/xml/Screens/PaymentScreen/PaymentScreenStatus.xml",
    ],
}
